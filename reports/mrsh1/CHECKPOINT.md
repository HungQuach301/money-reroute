# CHECKPOINT — MR-SH1 (Short dọc 1 từ tập 1 `tap01-1inmm`)

## Chạy tiếp từ đây
- 0 USD, không gọi API trả tiền (trần 0 mọi khoản — không thêm dòng `CAPS_PHIEN`).
- Kéo đầu vào: `git lfs pull --include "lab/mr4/tts/P01_l2.mp3,lab/mr5/nhac/N1_mo.mp3,lab/mr6/veo/K2_l1.mp4,lab/mrp1/A/a0*,lab/mrp1/A/a1*,lab/mr6/anh/b00[1-9]_l1.png,lab/mr6/anh/b06*,lab/mr6/anh/b07*,ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf"`.
- Dựng (~1–2 phút, 4 tiến trình): `MRSH1_TMP=<thư mục tạm> python3 scripts/mrsh1/short1.py` → `reports/mrsh1/xem/short1.mp4`; soát 1 khung: `--khung <giây>`.
- Kiểm: `pip install opencv-python-headless`; YuNet `face_detection_yunet_2023mar.onnx` (huggingface.co/opencv/face_detection_yunet, sha256 `8f2383e4…52fa4`); `python3 scripts/mrsh1/kiem.py <yunet.onnx>` → tờ 0,5 s, `doi_chieu_chu.json`, `qc_mat.json`.

## Trạng thái: **MR-SH1 DỪNG ở cuối mốc — chờ rà.** Bản xem đã đẩy LFS.
