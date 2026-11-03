# CHECKPOINT MR-P4

## Chạy tiếp từ đây
- Mọi lượt API đã xong: OpenRouter **0,4280 / 1,00 USD** (11 lượt tranh NB 2.1: 10 lượt 1 + b001 lượt 2). Không còn lượt trả tiền nào dự kiến.
- Tranh mới (LFS): `lab/mrp4/anh/*_l*.png`; chọn: `reports/mrp4/anh/chon.json` (b001 = lượt 2).
- Cần LFS: `git lfs pull --include="lab/mr4/tts/*,lab/mr5/nhac/*,lab/mr6/dung/tap01_1080p.mp4,lab/mr6/veo/K2_l1.mp4,lab/mr6/veo/K3_l2.mp4,lab/mrp1/A/*,lab/mr6/anh/*,lab/mrp3/*,lab/mrp4/*,ho-so/**"`.
- Mô hình (không vào repo): Depth Anything V2 Small ONNX `onnx-community/depth-anything-v2-small` @ 4472b73 `onnx/model.onnx` (sha256 afb6a5c2…df10c); YuNet `face_detection_yunet_2023mar.onnx` (opencv_zoo, sha256 8f2383e4…52fa4). Gói: `opencv-python-headless soundfile scipy pyloudnorm rapidocr_onnxruntime`.
- Tiếng động CC0 (0 USD): `MRP3_TMP=$MRP4_TMP python3 scripts/mrp3/cc0.py` (13/13 sha256 khớp `reports/mrp3/am/cc0.json`).
- Thứ tự (đặt `MRP4_TMP=<scratch>`):
  1. `python3 scripts/mrp4/sau.py <model.onnx>` → `do_sau.json` (28 tranh bản đăng); `python3 scripts/mrp4/sau.py <model.onnx> --moi` → `do_sau_moi.json`
  2. `python3 scripts/mrp4/qc_anh.py <yunet.onnx>`; `python3 scripts/mrp4/to_truoc_sau.py` → `xem/truoc_sau.jpg`
  3. `python3 scripts/mrp4/dung_p4.py am` → `am_do.json` + `$MRP4_TMP/am_M2_moi.wav`
  4. `python3 scripts/mrp4/dung_p4.py M2_moi` (≈ 260 s, 4 tiến trình) → `xem/M2_moi.mp4`, `dung_M2_moi.json`
  5. `python3 scripts/mrp4/dung_p4.py xem` → `xem/M2_cu.mp4`, `ghep_cu_moi.mp4`, `M2_{cu,moi}_loa.mp4`, `nghe_so_loa.mp4`
