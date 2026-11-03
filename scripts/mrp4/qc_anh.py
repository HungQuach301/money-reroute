#!/usr/bin/env python3
"""NGUỒN: scripts/mr6/qc_anh.py (repo này, main @ a8741a4) — MR-P4 đổi: tranh lab/mrp4/anh, lời reports/mrp4/anh/loi_anh.json,
ra reports/mrp4/anh/qc_may.json; tờ mắt 1:1 nửa khung ở $MRP4_TMP. Luật như MR-6: mặt chỉ được ở loại "nv" (ở đây không có) → mọi mặt = CỜ;
chữ OCR (điểm ≥ 0,6, ≥ 2 ký tự chữ/số) = CỜ. Cờ máy chỉ dẫn mắt, không thay mắt.
  python3 scripts/mrp4/qc_anh.py <face_detection_yunet_2023mar.onnx>"""
import glob, json, os, re, sys
import cv2
from rapidocr_onnxruntime import RapidOCR
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = json.load(open(os.path.join(ROOT, "reports", "mrp4", "anh", "loi_anh.json")))["tranh"]
det = cv2.FaceDetectorYN.create(sys.argv[1], "", (320, 320), 0.6); ocr = RapidOCR()
OUT = os.path.join(ROOT, "reports", "mrp4", "anh", "qc_may.json"); out = {}
for f in sorted(glob.glob(os.path.join(ROOT, "lab", "mrp4", "anh", "*_l*.png"))):
    k = os.path.relpath(f, ROOT); im = cv2.imread(f); h, w = im.shape[:2]; det.setInputSize((w, h))
    _, faces = det.detect(im); faces = [] if faces is None else faces.tolist()
    r, _ = ocr(f); chu = [(t, round(float(s), 2)) for _, t, s in (r or []) if float(s) >= 0.6 and len(re.sub(r"[^A-Za-z0-9]", "", t)) >= 2]
    tid = os.path.basename(f).split("_")[0]; loai = A[tid]["loai"]
    out[k] = {"loai": loai, "kich_thuoc": [w, h], "mat": [{"x": int(a[0]), "y": int(a[1]), "w": int(a[2]), "h": int(a[3]), "diem": round(a[-1], 2)} for a in faces],
              "chu": chu, "co_mat": bool(faces) and loai != "nv", "co_chu": bool(chu)}
    print(k, loai, "mặt", len(faces), "chữ", chu, flush=True)
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print("cờ mặt:", [k for k, v in out.items() if v["co_mat"]]); print("cờ chữ:", [(k, v["chu"]) for k, v in out.items() if v["co_chu"]])
