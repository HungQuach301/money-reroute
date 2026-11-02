# CHECKPOINT — MR-5 (M-c phần 2, tập 1 `tap01-1inmm`)

## Chạy tiếp từ đây
**MR-5 đã DỪNG ở cuối mốc (chờ rà).** Không còn lượt trả tiền nào đang chạy. Mọi tệp tốn tiền đã đẩy LFS.
- Sổ trần: `MR_PHIEN=mr5 python3 scripts/cp/budget.py` → openrouter **8,00 / 8,30 USD**; elevenlabs **3.245 / 6.000** ký tự tính.
- **Hết lượt Veo theo V7** ở 6 khe đã dùng lượt 2 (V03, V04, V10, V11, V13, V16) và V06 (MR-4). Trần còn 0,30 USD < 1 clip → **không sinh thêm** trong MR-5.
- Clip chọn cho dựng (M-d): `reports/mr5/veo/chon.json` (16 khe, V06/V12 từ MR-4; đoạn cắt V08 0–7,3 s, V16 0–7,3 s, tuỳ chọn V12 2,0–8,0 s).
- Nhạc: `lab/mr5/nhac/N1_mo.mp3` (40 s), `N2_tang_dan.mp3` (136 s), `N3_ket.mp3` (60 s) — kế hoạch `reports/mr5/nhac/ke_hoach.json`. Trộn mức (−24 → −18 dB), cắt lặng 1,5 s ở S080 làm ở M-d.
- Dựng lại bản xem (0 USD): `python3 scripts/mr5/tao_xem.py` (cần `git lfs pull --include "lab/mr4/veo/V06_l2.mp4,lab/mr4/veo/V12_l1.mp4"`).
- QC lại một clip (0 USD): `python3 scripts/mr5/qc_veo.py lab/mr5/veo/V03_l2.mp4 V03` rồi `python3 scripts/mr5/soi_co.py V03_l2`
  (cần `pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision` + `pip install opencv-python-headless ultralytics`;
  `/tmp/yunet.onnx` từ huggingface.co/opencv/face_detection_yunet, `/tmp/yolov8s.pt` từ github.com/ultralytics/assets v8.2.0).
  Tờ quét V8 `lab/mr5/do/` dựng lại được → **không đẩy**.

## Đã xong (giờ UTC)
| Giờ | Việc | Tệp (LFS) |
|---|---|---|
| 23:08 (01/11) | Số dư trước; trần `mr5` | `reports/mr5/so_du_truoc.json` |
| 23:10–23:37 | Veo lượt 1 × 14 (V01–V05, V07–V11, V13–V16), tuần tự | `lab/mr5/veo/V??_l1.mp4` |
| 23:16–23:19 | Nhạc N1, N2, N3 | `lab/mr5/nhac/*.mp3` |
| 23:39–23:50 | Veo lượt 2 × 6 (V04, V03, V10, V13, V11, V16), tuần tự | `lab/mr5/veo/V??_l2.mp4` |
| 23:40–00:00 | QC máy + mắt, chọn clip, bản xem | `reports/mr5/veo/`, `reports/mr5/xem/` |
| 00:01 (02/11) | Số dư sau | `reports/mr5/so_du_sau.json` |
