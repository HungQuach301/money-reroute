#!/usr/bin/env python3
"""MR-P3 · So 1:1 clip 720p phóng lên 1080p (Lanczos, như bộ dựng) với clip 1080p CÙNG lời, CÙNG khung đầu (V02 b040 vs V02b), 0 USD.
Đo trên tranh vẽ: độ nét (phương sai Laplace) toàn khung + 3 vùng chi tiết, mức nhiễu khối (chênh 8×8), và tờ cắt 1:1 384×216 ở 0,5 / 2 / 3,5 s.
Kèm khung đầu = tranh gốc (đúng khung bản đăng) làm mốc độ nét. Ra: reports/mrp3/so_720_1080.json + reports/mrp3/xem/so_720_1080.jpg."""
import json, os, sys
import numpy as np, cv2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("MR6_TMP", os.path.join(os.environ.get("MRP3_TMP", "/tmp/claude-0/mrp3"), "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))
import dung as D  # noqa: E402
import glob


def khung(f, t):
    cap = cv2.VideoCapture(f); fps = cap.get(cv2.CAP_PROP_FPS) or 24; cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps)); ok, x = cap.read()
    if x.shape[1] != 1920: x = cv2.resize(x, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)
    return x


def lap(x): return float(cv2.Laplacian(cv2.cvtColor(x, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var())


def khoi(x):
    g = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY).astype(np.float32); d = np.abs(np.diff(g, axis=1))
    return float(d[:, 7::8].mean() / (d.mean() + 1e-6))


def main():
    f1 = sorted(glob.glob(os.path.join(ROOT, "lab/mrp3/veo/V02_b040_1080p_l*.mp4")))[-1]; f7 = sorted(glob.glob(os.path.join(ROOT, "lab/mrp3/veo/V02b_b040_720p_l*.mp4")))[-1]
    goc = np.array(D.tranh("b040").convert("RGB"))[..., ::-1]
    VUNG = {"trang_phan_chieu": (560, 380, 944, 596), "ngon_cay": (1300, 200, 1684, 416), "bo_hồ_co": (80, 760, 464, 976)}
    kq = {"tep_1080p": os.path.relpath(f1, ROOT), "tep_720p": os.path.relpath(f7, ROOT), "goc_tranh": {"lap": round(lap(goc), 1)}, "khung": {}}
    rows = []
    for t in (0.5, 2.0, 3.5):
        a, b = khung(f1, t), khung(f7, t); r = {"lap_1080": round(lap(a), 1), "lap_720_len": round(lap(b), 1), "khoi_1080": round(khoi(a), 3), "khoi_720_len": round(khoi(b), 3)}
        for k, (x0, y0, x1, y1) in VUNG.items():
            r["lap_" + k] = [round(lap(a[y0:y1, x0:x1]), 1), round(lap(b[y0:y1, x0:x1]), 1)]
            row = np.hstack([goc[y0:y1, x0:x1], a[y0:y1, x0:x1], b[y0:y1, x0:x1]]).copy()
            for j, s in enumerate(("tranh goc", f"1080p {t}s", f"720p->1080 {t}s")): cv2.putText(row, s, (6 + 384 * j, 20), 0, 0.6, (0, 255, 255), 2)
            rows.append(row)
        kq["khung"][str(t)] = r
    kq["ti_le_net_720_tren_1080_tb"] = round(float(np.mean([v["lap_720_len"] / v["lap_1080"] for v in kq["khung"].values()])), 3)
    json.dump(kq, open(os.path.join(ROOT, "reports", "mrp3", "so_720_1080.json"), "w"), indent=1, ensure_ascii=False)
    cv2.imwrite(os.path.join(ROOT, "reports", "mrp3", "xem", "so_720_1080.jpg"), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(json.dumps(kq, ensure_ascii=False)[:800])


if __name__ == "__main__":
    main()
