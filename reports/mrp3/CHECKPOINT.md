# CHECKPOINT MR-P3

## Chạy tiếp từ đây
- Mọi lượt API đã xong (OpenRouter 2,94 / 5,00 USD; ElevenLabs 759 / 3.000 ký tự). Không còn lượt trả tiền nào dự kiến.
- Clip (LFS): `lab/mrp3/veo/*.mp4` (chọn: `reports/mrp3/veo/chon.json`); âm ElevenLabs (LFS): `lab/mrp3/am/*.mp3`.
- Tiếng động CC0: tải lại 0 USD bằng `MRP3_TMP=… python3 scripts/mrp3/cc0.py` (danh sách + sha256: `reports/mrp3/am/cc0.json`).
- Tách lớp 2.5D: `python3 scripts/mrp3/sau.py <depth-anything-v2-small model.onnx>` (rev 4472b73, sha256 afb6a5c2…df10c).
- Dựng: `MRP3_TMP=… python3 scripts/mrp3/dung_p3.py goc|M1|P1|M2|P2|M3 --to` → `reports/mrp3/xem/*.mp4` (540p, LFS).
- Đo: `python3 scripts/mrp3/do_chuyen_dong.py`; so 720p/1080p: `python3 scripts/mrp3/so_720_1080.py`.
- Cần LFS: `git lfs pull --include="lab/mr4/tts/*,lab/mr5/nhac/*,lab/mr6/dung/tap01_1080p.mp4,lab/mr6/veo/K2_l1.mp4,lab/mr6/veo/K3_l2.mp4,lab/mrp1/A/*,lab/mr6/anh/*,lab/mrp3/*"`.
