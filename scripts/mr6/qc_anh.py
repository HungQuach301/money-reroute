#!/usr/bin/env python3
"""MR-6 · QC máy mọi tranh MR-6 (0 USD), như MR-P1: dò mặt (OpenCV YuNet) + dò chữ (RapidOCR) + tờ ghép cho mắt.
  python3 scripts/mr6/qc_anh.py <yunet.onnx>   → reports/mr6/qc_may.json + /tmp/claude-0/qc_to_*.jpg (tờ mắt, dựng lại được)
Luật: mặt chỉ được có ở tranh loại "nv" (nhà đầu tư — nhân vật đại diện tự nghĩ ra); tranh "man"/"empty" có mặt = CỜ (mắt xem);
chữ OCR đọc được (điểm ≥ 0,6, ≥ 2 ký tự chữ/số) = CỜ. Cờ máy chỉ dẫn mắt, không thay mắt."""
import glob, json, os, re, sys
import cv2
from PIL import Image, ImageDraw
from rapidocr_onnxruntime import RapidOCR
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = json.load(open(os.path.join(ROOT, "reports", "mr6", "loi_anh.json")))["tranh"]
det = cv2.FaceDetectorYN.create(sys.argv[1], "", (320, 320), 0.6); ocr = RapidOCR()
OUT = os.path.join(ROOT, "reports", "mr6", "qc_may.json"); out = json.load(open(OUT)) if os.path.exists(OUT) else {}
fs = sorted(glob.glob(os.path.join(ROOT, "lab", "mr6", "anh", "b*_l*.png")))
for f in fs:
    k = os.path.relpath(f, ROOT)
    if k in out: continue
    im = cv2.imread(f); h, w = im.shape[:2]; det.setInputSize((w, h))
    _, faces = det.detect(im); faces = [] if faces is None else faces.tolist()
    r, _ = ocr(f); chu = [(t, round(float(s), 2)) for _, t, s in (r or []) if float(s) >= 0.6 and len(re.sub(r"[^A-Za-z0-9]", "", t)) >= 2]
    tid = os.path.basename(f)[:4]; loai = A[tid]["loai"]
    out[k] = {"loai": loai, "mat": [{"x": int(a[0]), "y": int(a[1]), "w": int(a[2]), "h": int(a[3]), "diem": round(a[-1], 2)} for a in faces],
              "chu": chu, "co_mat": bool(faces) and loai != "nv", "co_chu": bool(chu)}
    print(k, loai, "mặt", len(faces), "chữ", chu, "CỜ MẶT" if out[k]["co_mat"] else "", flush=True)
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
# tờ mắt: 5×4 tranh / tờ, ô ghi mã + cờ
for n in range(0, len(fs), 20):
    to = Image.new("RGB", (5 * 400, 4 * 245), "black"); d = ImageDraw.Draw(to)
    for j, f in enumerate(fs[n:n + 20]):
        k = os.path.relpath(f, ROOT); x, y = (j % 5) * 400, (j // 5) * 245
        to.paste(Image.open(f).convert("RGB").resize((400, 223)), (x, y + 22))
        c = out[k]; tag = os.path.basename(f)[:-4] + " " + c["loai"] + (" MẶT!" if c["co_mat"] else "") + (" CHỮ!" if c["co_chu"] else "")
        d.text((x + 4, y + 4), tag, fill="red" if (c["co_mat"] or c["co_chu"]) else "white")
    to.save(f"/tmp/claude-0/qc_to_{n // 20:02d}.jpg", quality=82)
print("cờ mặt:", [k for k, v in out.items() if v["co_mat"]]); print("cờ chữ:", [(k, v["chu"]) for k, v in out.items() if v["co_chu"]])
