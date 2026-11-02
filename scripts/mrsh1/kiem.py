#!/usr/bin/env python3
"""MR-SH1 · Kiểm Short 1 (0 USD): tờ 0,5 s · máy đối chiếu chữ trên hình · dò mặt YuNet trên khung đã cắt dọc.
  python3 scripts/mrsh1/kiem.py <yunet.onnx>
   → reports/mrsh1/xem/to05s.jpg (tờ 0,5 s), reports/mrsh1/doi_chieu_chu.json, reports/mrsh1/qc_mat.json
YuNet: huggingface.co/opencv/face_detection_yunet (face_detection_yunet_2023mar.onnx); `pip install opencv-python-headless`.
Đối chiếu chữ (sổ reports/mrsh1/chu_tren_hinh.json do short1.py ghi khi vẽ, mỗi chuỗi kèm loại):
  phu_de / kbcb / moc_cau / do_hoa / ten: sau khi đổi chữ số → chữ theo bảng DOI, chuỗi phải là đoạn LIỀN của một câu S004–S011 (loi.json);
     không thì phải có trong bảng RIENG (câu + các cụm bắt buộc có trong câu đó, kèm lý do). Còn lại = CỜ.
  nhan: thuộc tập nhãn HIEN-CHUONG §3–§4 và khớp tầng loi.json của câu; nguon: đúng chuỗi dung.nguon(câu) (sinh từ loi.json);
  l3_tieu: đoạn của tiêu đề L3 đã duyệt ở MR-6 (shot2.json T01); the_cuoi: ghép lại = nguyên văn lệnh."""
import json, os, re, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.environ.setdefault("MRSH1_TMP", "/tmp/claude-0/mrsh1_dung")
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrsh1"))
import short1 as S  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

VID = os.path.join(ROOT, "reports", "mrsh1", "xem", "short1.mp4")
TMP = os.path.join(S.SCR, "kiem"); os.makedirs(TMP, exist_ok=True)


# ---------- 1. tờ 0,5 s ----------
def to05():
    for f in os.listdir(TMP):
        if f.startswith("f"): os.remove(os.path.join(TMP, f))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VID, "-vf", "fps=2", "-q:v", "3", os.path.join(TMP, "f%04d.jpg")], check=True)
    fs = sorted(f for f in os.listdir(TMP) if f.startswith("f")); cot = 11; w, h = 180, 320
    to = Image.new("RGB", (cot * w, ((len(fs) + cot - 1) // cot) * (h + 22)), "black"); d = ImageDraw.Draw(to)
    for i, f in enumerate(fs):
        x, y = (i % cot) * w, (i // cot) * (h + 22)
        to.paste(Image.open(os.path.join(TMP, f)).resize((w, h)), (x, y + 22)); d.text((x + 4, y + 4), f"{i * 0.5:.1f}s", fill="white")
    out = os.path.join(ROOT, "reports", "mrsh1", "xem", "to05s.jpg"); to.save(out, quality=80)
    return [os.path.join(TMP, f) for f in fs], out


# ---------- 2. đối chiếu chữ ----------
DOI = [("$650,000,000+", "six hundred fifty million dollars"), ("$650 million", "six hundred fifty million dollars"),
       ("25–45%", "twenty-five to forty-five percent"), ("20 years", "twenty years"), ("2022", "twenty twenty-two"),
       ("1inMM", "one-in-M-M"), ("25", "twenty-five"), ("45", "forty-five"), ("6", "six"), ("12", "twelve"), ("20", "twenty")]
RIENG = {  # chuỗi không liền trong lời nhưng mọi cụm đều có trong câu
    "FAKE — admitted": ("S007", ["admitted", "fake"], "S007 'he admitted the distribution deals were fake' (●T, N7 tr. 11)"),
    "$650,000,000+": ("S009", ["at least", "six hundred fifty million dollars"], "'+' = 'at least' (●T, N7 tr. 12)"),
    "SENTENCED IN 2022": ("S010", ["sentenced", "twenty twenty-two"], "S010 (●, N8 tr. 1)"),
    "aka “Zach Avery” · actor, Los Angeles": ("S004", ["zach avery", "actor", "los angeles", "screen name"], "thẻ tên MR-6; 'aka' = 'used the screen name'"),
}
NHAN_OK = {"ILLUSTRATIVE", "ILLUSTRATIVE — not the real person", "● CONVICTED", "● CONVICTED · admitted in plea"}
tok = lambda s: [t for t in (re.sub(r"[^a-z0-9]", "", x.lower()) for x in re.split(r"[\s\-–—·,]+", s)) if t]


def doi(s):
    for a, b in DOI: s = re.sub(r"(?<![\w$])" + re.escape(a) + r"(?![\w])", b, s, flags=re.I) if a[0].isalnum() else s.replace(a, b)
    return s


def lien(sub, cau):
    a, b = tok(sub), tok(cau)
    return bool(a) and any(b[i:i + len(a)] == a for i in range(len(b) - len(a) + 1))


def doi_chieu():
    chu = json.load(open(os.path.join(ROOT, "reports", "mrsh1", "chu_tren_hinh.json")))
    loi = {c: S.LOI[c]["loi"] for c in S.CAUS}
    nguon_ok = {S.dung.nguon(c): c for c in S.CAUS if S.dung.nguon(c)}
    tieu_l3 = json.load(open(os.path.join(ROOT, "reports", "mr6", "shot2.json")))["l3"]["T01"][4]
    out = []
    for x in chu:
        s, k = x["chuoi"], x["loai"]; ok, cc = False, ""
        if k in ("phu_de", "kbcb", "moc_cau", "do_hoa", "ten"):
            hit = [c for c, l in loi.items() if lien(doi(s), l)]
            if s in RIENG:
                c, cums, ly = RIENG[s]; ok = all(lien(m, loi[c]) for m in cums); cc = f"{c}: {ly}"
            elif hit: ok, cc = True, "đoạn liền của " + ",".join(hit)
        elif k == "nhan":
            ok = s in NHAN_OK; cc = "HIEN-CHUONG §3–§4"
        elif k == "nguon":
            ok = s in nguon_ok; cc = "= dung.nguon(" + nguon_ok.get(s, "?") + ")"
        elif k == "l3_tieu":
            ok = s in tieu_l3; cc = "đoạn của: " + tieu_l3
        elif k == "the_cuoi":
            ok = " ".join(S.THE_CUOI) == "Full case + 5 red flags → Money Reroute" and s in S.THE_CUOI; cc = "nguyên văn lệnh MR-SH1"
        out.append({"chuoi": s, "loai": k, "dat": ok, "can_cu": cc})
    # nhãn tầng từng cảnh khớp loi.json
    tang = []
    for c in S.CANH:
        cau = c["cau"]
        if cau: tang.append({"canh": c["ma"], "cau": cau, "tang_loi_json": S.LOI[cau]["tang"], "nhan": (S.dung.nhan_tang(cau) or [None])[0], "nguon": S.dung.nguon(cau)})
    r = {"chuoi": len(out), "co": [o for o in out if not o["dat"]], "tat_ca": out, "nhan_theo_canh": tang}
    json.dump(r, open(os.path.join(ROOT, "reports", "mrsh1", "doi_chieu_chu.json"), "w"), ensure_ascii=False, indent=1)
    return r


# ---------- 3. mặt (YuNet) trên khung đã cắt dọc ----------
def mat(model, frames):
    import cv2
    det = cv2.FaceDetectorYN.create(model, "", (320, 320), 0.3)
    def quet(img):
        h, w = img.shape[:2]; det.setInputSize((w, h)); _, f = det.detect(img)
        return [] if f is None else [{"x": int(a[0]), "y": int(a[1]), "w": int(a[2]), "h": int(a[3]), "diem": round(float(a[-1]), 2)} for a in f]
    r = {"nguong": 0.3, "tranh_cat_doc": {}, "khung_0_5s": {}}
    import numpy as np
    for c in S.CANH:
        if c["lop"] == "L1":
            im = S.cat_doc(c["ma"], c["cx"]); arr = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            z = S.khung(im, ((0.5, 0.5, 1.09), (0.5, 0.5, 1.09)), 0); arr2 = cv2.cvtColor(np.array(z), cv2.COLOR_RGB2BGR)
            r["tranh_cat_doc"][c["ma"]] = {"cx": c["cx"], "mat": quet(arr), "mat_phong_1_09": quet(arr2)}
    k2 = S.k2_dir()
    for f in sorted(os.listdir(k2))[::15]:
        r["tranh_cat_doc"]["K2/" + f] = {"mat": quet(cv2.imread(os.path.join(k2, f)))}
    for i, f in enumerate(frames):
        m = quet(cv2.imread(f))
        if m: r["khung_0_5s"][f"{i * 0.5:.1f}"] = m
    r["so_khung_quet"] = len(frames)
    r["co"] = [k for k, v in r["tranh_cat_doc"].items() if v["mat"] or v.get("mat_phong_1_09")] + ["t=" + k for k in r["khung_0_5s"]]
    json.dump(r, open(os.path.join(ROOT, "reports", "mrsh1", "qc_mat.json"), "w"), ensure_ascii=False, indent=1)
    return r


if __name__ == "__main__":
    frames, to = to05(); print("tờ 0,5 s:", to, len(frames), "khung")
    r = doi_chieu(); print("chữ:", r["chuoi"], "chuỗi;", len(r["co"]), "cờ")
    for c in r["co"]: print("  CỜ", c)
    m = mat(sys.argv[1], frames); print("mặt: cờ", m["co"])
