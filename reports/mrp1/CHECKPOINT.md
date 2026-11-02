# CHECKPOINT — MR-P1 (thử phong cách minh hoạ, P00–P03 tập 1)

## Chạy tiếp từ đây
**MR-P1 đã DỪNG ở cuối mốc (chờ rà).** Không còn lượt trả tiền nào đang chạy; mọi tệp tốn tiền đã đẩy LFS.
- Sổ trần: `MR_PHIEN=mrp1 python3 scripts/cp/budget.py` → openrouter **1,6319 / 2,00 USD** (mốc báo 1,60 đã chạm ở lượt cuối).
- Sinh thêm một tranh (chỉ khi có lệnh mới): `MR_PHIEN=mrp1 python3 scripts/mrp1/anh.py <A|B> <aNN> <lượt>` (≤ 2 lượt/tranh).
- Dựng lại bản xem (0 USD): `git lfs pull --include "lab/mrp1/**,lab/mr4/tts/P00.mp3,lab/mr4/tts/P01_l2.mp3,lab/mr4/tts/P02.mp3,lab/mr4/tts/P03.mp3,lab/mr5/nhac/N1_mo.mp3,ho-so/1inmm-horwitz/*.pdf"` rồi `python3 scripts/mrp1/dung.py A` / `B` (~2,5 phút mỗi bản).
- QC máy (0 USD): `pip install opencv-python-headless rapidocr_onnxruntime`; yunet `face_detection_yunet_2023mar.onnx` (huggingface.co/opencv/face_detection_yunet); `python3 scripts/mrp1/qc_anh.py <yunet.onnx>`.

## Đã xong (giờ UTC, 02/11/2026)
| Giờ | Việc | Tệp |
|---|---|---|
| 01:59 | Số dư trước; giá model ảnh | `reports/mrp1/so_du_truoc.json`, `gia_model.json` |
| 02:03–02:08 | A a01–a20 lượt 1 | `lab/mrp1/A/` |
| 02:08–02:14 | B a01–a20 lượt 1 | `lab/mrp1/B/` |
| 02:15 | a14 lượt 2 (A, B) | `lab/mrp1/{A,B}/a14_l2.png` |
| 02:17–02:26 | QC máy + mắt, bằng chứng, dựng bản xem | `reports/mrp1/qc_may.json`, `reports/mrp1/xem/` |
| 02:26 | Số dư sau | `reports/mrp1/so_du_sau.json` |
