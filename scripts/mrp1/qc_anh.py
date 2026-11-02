#!/usr/bin/env python3
"""MR-P1 · QC máy mọi tranh (0 USD): dò mặt (OpenCV YuNet) + dò chữ (RapidOCR). Cờ máy chỉ dẫn mắt, không thay mắt.
  python3 scripts/mrp1/qc_anh.py <yunet.onnx>  → reports/mrp1/qc_may.json
Cần: pip install opencv-python-headless rapidocr_onnxruntime; yunet từ huggingface.co/opencv/face_detection_yunet
(face_detection_yunet_2023mar.onnx).
Luật đối chiếu: mặt chỉ được có ở tranh có nhân vật đại diện (MAT_DUOC); mọi chữ OCR đọc được (điểm ≥ 0,6, ≥ 2 ký tự chữ/số) = cờ."""
import glob, json, os, re, sys
import cv2
from rapidocr_onnxruntime import RapidOCR
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MAT_DUOC = {"a01", "a04", "a13", "a16", "a17"}  # tranh được có mặt nhà đầu tư (nhân vật đại diện tự nghĩ ra); a16 chỉ B
det = cv2.FaceDetectorYN.create(sys.argv[1], "", (320, 320), 0.6)
ocr = RapidOCR(); out = {}
for f in sorted(glob.glob(os.path.join(ROOT, "lab", "mrp1", "*", "a*_l*.png"))):
    im = cv2.imread(f); h, w = im.shape[:2]; det.setInputSize((w, h))
    _, faces = det.detect(im); faces = [] if faces is None else faces.tolist()
    r, _ = ocr(f); chu = [(t, round(float(s), 2)) for _, t, s in (r or []) if float(s) >= 0.6 and len(re.sub(r"[^A-Za-z0-9]", "", t)) >= 2]
    k = os.path.relpath(f, ROOT); tid = os.path.basename(f)[:3]
    out[k] = {"mat": [{"x": int(a[0]), "y": int(a[1]), "w": int(a[2]), "h": int(a[3]), "diem": round(a[-1], 2)} for a in faces],
              "chu": chu, "co_mat_ngoai_danh_sach": bool(faces) and tid not in MAT_DUOC, "co_chu": bool(chu)}
    print(k, "mặt", len(faces), "chữ", chu, "CỜ MẶT" if out[k]["co_mat_ngoai_danh_sach"] else "", flush=True)
json.dump(out, open(os.path.join(ROOT, "reports", "mrp1", "qc_may.json"), "w"), ensure_ascii=False, indent=1)
