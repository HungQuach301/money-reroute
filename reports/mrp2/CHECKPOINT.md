# CHECKPOINT — MR-P2 (thử giảm cảm giác ảnh tĩnh, ~60 s tập 1)

## Chạy tiếp từ đây
- Sổ trần: `MR_PHIEN=mrp2 python3 scripts/cp/budget.py` (trần openrouter 1,50, mốc 1,20; đã chi 1,00). **Không sinh thêm Veo** nếu không có lệnh mới.
- Môi trường: `pip install onnxruntime opencv-python-headless`; mô hình độ sâu tải về scratch: `https://huggingface.co/onnx-community/depth-anything-v2-small/resolve/4472b7362082ad9968fee890ca0f1e5aca36b93d/onnx/model.onnx` (sha256 `afb6a5c28f3b6bf1618c6e43f02073ef9dfdc70e937502d51603e57b0a1df10c`, Apache-2.0).
- LFS: `git lfs pull --include "lab/mr6/dung/tap01_1080p.mp4,lab/mr6/anh/b0*_l1.png,lab/mr6/anh/b143_l1.png,lab/mrp2/veo/**"`.
- `export MRP2_TMP=<thư mục scratch>`; độ sâu + tách lớp: `python3 scripts/mrp2/sau.py <model.onnx>`.
- Dựng: `python3 scripts/mrp2/dung_thu.py goc|A|B|C|P --to` → `reports/mrp2/xem/`. QC mép: `python3 scripts/mrp2/qc_mep.py`. Đo: `python3 scripts/mrp2/do_chuyen_dong.py P A B C`.
- Veo (chỉ khi có lệnh): `bash scripts/mrp2/chay_veo.sh V?` (LUOT=2 cho lượt 2, lời phải đổi).

## Trạng thái: **MR-P2 DỪNG ở cuối mốc — chờ rà.** Chi 1,00 / 1,50 USD (khớp khoá). Mọi clip Veo đã đẩy LFS (≤ 1 phút sau khi sinh).

## Đã xong (UTC, 02/11/2026)
| Giờ | Việc |
|---|---|
| 14:57 | Trần mrp2; số dư trước; GET danh mục video (Veo Lite 4 s = 0,20 USD) |
| 15:00–15:02 | Độ sâu + tách 3 lớp + vá, 12 tranh |
| 15:03–15:13 | Veo V1–V5 lượt 1 đạt cả 5, đẩy LFS từng clip |
| 15:10–15:41 | Dựng goc/A/B/C; QC mép 2 vòng; quét V8 0 cờ |
| 15:29 | Số dư sau + đối soát (ngoài khoá MR 6,20 USD) |
| 15:41–16:06 | Đối chứng P; thước đo v3; báo cáo |
