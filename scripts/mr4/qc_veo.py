#!/usr/bin/env python3
"""MR-4 · QC tại nguồn một clip Veo (0 USD, máy cục bộ). Bổ trợ cho mắt, không thay mắt.
  python3 scripts/mr4/qc_veo.py lab/mr4/veo/V12_l1.mp4 V12
Ra (reports/mr4/veo/):
  <tên>_to05.jpg   tờ 0,5 s: 17 ô (0,0 … 8,0 s), mỗi ô ghi giây — V8 "tờ 0,5 s mọi khe có chuyển động"
  <tên>_neo.jpg    neo đầu / neo cuối cỡ lớn (V3: neo cuối không người tiền cảnh)
  <tên>_qc.json    thông số tệp (ffprobe) + dò mặt Haar (chính diện + nghiêng, 2 chiều) mỗi 1/8 s + dò người YOLOv8s mỗi 1/4 s
                   + quet_v8.py (5 cột) chạy trên chính clip như một bản dựng một khe (dung: f0 0, n = số khung)
Cờ máy (mặt/người/V8) chỉ dẫn mắt; kết luận QC ghi ở báo cáo sau khi xem tờ."""
import json, os, subprocess, sys
import cv2, numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RA = os.path.join(ROOT, "reports", "mr4", "veo")


def probe(p):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", p],
                                  capture_output=True, text=True, check=True).stdout)
    v = [s for s in j["streams"] if s["codec_type"] == "video"][0]
    return {"w": v["width"], "h": v["height"], "fps": v["r_frame_rate"], "nb_frames": v.get("nb_frames"), "codec": v["codec_name"],
            "dur": float(j["format"]["duration"]), "audio": [s["codec_name"] for s in j["streams"] if s["codec_type"] == "audio"],
            "bytes": int(j["format"]["size"])}


def khung(p, t, w=None):
    vf = ["-vf", f"scale={w}:-2"] if w else []
    b = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", p, "-frames:v", "1", *vf, "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True, check=True).stdout
    return cv2.imdecode(np.frombuffer(b, np.uint8), cv2.IMREAD_COLOR)


def to05(p, ten, dur):
    ts = [min(i * 0.5, dur - 0.05) for i in range(17)]
    o = []
    for t in ts:
        f = khung(p, t, 480)
        cv2.rectangle(f, (0, 0), (92, 30), (0, 0, 0), -1)
        cv2.putText(f, f"{t:.1f}s", (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        o.append(f)
    while len(o) % 4: o.append(np.zeros_like(o[0]))
    rows = [np.hstack(o[i:i + 4]) for i in range(0, len(o), 4)]
    cv2.imwrite(os.path.join(RA, f"{ten}_to05.jpg"), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 80])
    a, b = khung(p, 0.0, 960), khung(p, dur - 0.05, 960)
    cv2.imwrite(os.path.join(RA, f"{ten}_neo.jpg"), np.hstack([a, b]), [cv2.IMWRITE_JPEG_QUALITY, 85])


def mat(p, dur):
    d = cv2.data.haarcascades
    cs = [cv2.CascadeClassifier(d + "haarcascade_frontalface_default.xml"), cv2.CascadeClassifier(d + "haarcascade_profileface.xml")]
    hits = []
    cap = cv2.VideoCapture(p); fps = cap.get(cv2.CAP_PROP_FPS) or 24; i = 0
    while True:
        ok, f = cap.read()
        if not ok: break
        if i % max(1, round(fps / 8)) == 0:
            g = cv2.cvtColor(cv2.resize(f, (960, 540)), cv2.COLOR_BGR2GRAY)
            for k, c in enumerate(cs):
                for gg, flip in ((g, False), (cv2.flip(g, 1), True)):
                    if k == 0 and flip: continue
                    for (x, y, w, h) in c.detectMultiScale(gg, 1.1, 6, minSize=(24, 24)):
                        hits.append({"t": round(i / fps, 2), "loai": ["chinh_dien", "nghieng"][k], "lat": flip, "o": [int(x), int(y), int(w), int(h)]})
        i += 1
    return hits


def nguoi(p):
    try:
        from ultralytics import YOLO
    except Exception as e:
        return {"loi": str(e)}
    m = YOLO(os.environ.get("YOLO_W", "/tmp/yolov8s.pt"))
    cap = cv2.VideoCapture(p); fps = cap.get(cv2.CAP_PROP_FPS) or 24; i = 0; o = []
    while True:
        ok, f = cap.read()
        if not ok: break
        if i % max(1, round(fps / 4)) == 0:
            r = m.predict(cv2.resize(f, (960, 540)), classes=[0], conf=0.15, verbose=False)[0]
            o.append({"t": round(i / fps, 2), "n": len(r.boxes), "conf": [round(float(c), 2) for c in r.boxes.conf]})
        i += 1
    return o


def v8(p, ten, n):
    dj = os.path.join(RA, f"{ten}_dung.json")
    json.dump({"doan": [{"id": ten, "f0": 0, "n": n}]}, open(dj, "w"))
    ra = os.path.join(ROOT, "lab", "mr4", "do", f"{ten}_v8")
    os.makedirs(os.path.dirname(ra), exist_ok=True)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "common", "quet_v8.py"), p, dj, "--ra", ra, "--buoc", "2"],
                       capture_output=True, text=True, env={**os.environ, "YOLO_W": os.environ.get("YOLO_W", "/tmp/yolov8s.pt")})
    out = {"rc": r.returncode, "stdout": r.stdout[-3000:], "stderr": r.stderr[-1500:]}
    if os.path.exists(ra + ".json"): out["ket_qua"] = json.load(open(ra + ".json"))
    return out


if __name__ == "__main__":
    p, khe = sys.argv[1], sys.argv[2]; ten = os.path.splitext(os.path.basename(p))[0]
    os.makedirs(RA, exist_ok=True)
    m = probe(p); to05(p, ten, m["dur"])
    n = int(m["nb_frames"]) if m.get("nb_frames") else int(round(m["dur"] * 24))
    q = {"tep": os.path.relpath(p, ROOT), "khe": khe, "probe": m, "mat_haar": mat(p, m["dur"]), "nguoi_yolo": nguoi(p), "quet_v8": v8(p, ten, n)}
    json.dump(q, open(os.path.join(RA, f"{ten}_qc.json"), "w"), ensure_ascii=False, indent=1)
    ny = q["nguoi_yolo"]
    print(json.dumps({"tep": q["tep"], "probe": m, "so_mat_haar": len(q["mat_haar"]),
                      "nguoi_max": max((x["n"] for x in ny), default=0) if isinstance(ny, list) else ny,
                      "nguoi_neo_cuoi": ny[-1] if isinstance(ny, list) and ny else None,
                      "v8_rc": q["quet_v8"]["rc"], "v8_out": q["quet_v8"]["stdout"][-800:]}, ensure_ascii=False, indent=1))
