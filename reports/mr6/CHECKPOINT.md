# CHECKPOINT — MR-6 (tập 1 `tap01-1inmm`, phong cách PHONG-CACH-HINH v1)

## Chạy tiếp từ đây
- Sổ trần: `MR_PHIEN=mr6 python3 scripts/cp/budget.py` (trần openrouter 10,00 USD, mốc báo 8,00).
- Tranh L1: `bash scripts/mr6/chay_anh.sh <id…>` (tuần tự, đẩy LFS theo lô ≤ 5 phút; mất kết nối → thử lại 1 lần). Còn thiếu: `python3 -c "import json,os;print([k for k in json.load(open('reports/mr6/loi_anh.json'))['tranh'] if not os.path.exists(f'lab/mr6/anh/{k}_l1.png')])"`.
- Veo ảnh→video: `LUOT=<1|2> bash scripts/mr6/chay_veo.sh K?` — K1 hết lượt (2 failed), K3 đã dùng lượt 2, K2/K4/K5 lượt 1 (K4 loại ở QC). **Không sinh thêm Veo.**
- QC tranh: `python3 scripts/mr6/qc_anh.py <yunet.onnx>` (yunet: huggingface.co/opencv/face_detection_yunet; `pip install opencv-python-headless rapidocr_onnxruntime`). Sửa bằng cắt khung: `reports/mr6/cat_khung.json`.
- SHOT2: `python3 scripts/mr6/shot2.py` (→ `docs/tap01-1inmm/SHOT2.md`, `reports/mr6/shot2.json`).
- Dựng (0 USD): `git lfs pull --include "lab/mr6/**,lab/mrp1/A/**,lab/mr4/tts/**,lab/mr5/nhac/**,lab/mr5/veo/V1[013]_l2.mp4,lab/mr4/veo/V12_l1.mp4,ho-so/1inmm-horwitz/*.pdf"` rồi `python3 scripts/mr6/dung.py` (~15–20 phút, 4 tiến trình).
- Kiểm: `python3 scripts/mr6/doi_chieu_chu.py` (chữ trên hình ↔ nguồn), `scripts/common/quet_v8.py` trên clip Veo, tờ 1 s.
- Mở nguồn: `MR_UA="<UA khai báo do lệnh cấp>" python3 scripts/mr6/mo_nguon.py` (UA chỉ trong header, không ghi repo).

## Trạng thái: **MR-6 DỪNG ở cuối mốc — chờ rà + G2.** Không còn lượt trả tiền nào; chi 7,4795 / 10,00 USD (khớp khoá). Mọi tệp tốn tiền đã đẩy LFS.

## Đã xong (UTC, 02/11/2026)
| Giờ | Việc | Tệp |
|---|---|---|
| 03:26 | Trần mr6, số dư trước, mốc câu whisper | `reports/mr6/so_du_truoc.json`, `moc_cau.json` |
| 03:30–04:10 | 150 tranh L1 (19 lô LFS) | `lab/mr6/anh/` |
| 03:33–03:49 | Veo ảnh→video: K2, K3 l2, K4, K5 đạt sinh; K1 ×2, K3 l1 failed | `lab/mr6/veo/` |
| 03:51 | Mở lại N2/N3/N18, trạng thái vụ | `docs/tap01-1inmm/kiem/mr6_nguon.json` |
| 04:11 | Số dư sau + đối soát | `reports/mr6/so_du_sau.json` |
| 04:12–05:40 | Dựng, tờ 1 s, đối chiếu chữ, kiểm pháp lý lần 2 + 2 vòng sửa | `lab/mr6/dung/`, `reports/mr6/xem/`, `docs/tap01-1inmm/kiem/mr6_phap_ly_lan2.md` |
