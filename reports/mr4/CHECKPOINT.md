# CHECKPOINT — MR-4 (M-c phần 1, tập 1 `tap01-1inmm`)

## Chạy tiếp từ đây
**MR-4 đã DỪNG ở cuối mốc (chờ rà).** Không còn lượt trả tiền nào đang chạy. Mọi tệp tốn tiền đã đẩy LFS.
- Sổ trần: `MR_PHIEN=mr4 python3 scripts/cp/budget.py` → openrouter 1,20 / 1,60 USD; elevenlabs 6.109 / 8.000 ký tự tính; gửi 13.881 / 16.000.
- Bản giọng đã chọn cho dựng (M-d): `reports/mr4/xem/tap01_giong_ghep.json` mục `doan` (P01 → `P01_l2`, còn lại bản 1 — kể cả P17, P19).
  Dựng lại bản nghe (0 USD): `python3 scripts/mr4/ghep_giong.py`.
- Kiểm whisper lại một đoạn (0 USD): `python3 scripts/mr4/kiem_whisper.py P19` và `--so-chu P19` (cần `pip install faster-whisper` + `pip install --no-deps num2words`).
- QC lại một clip (0 USD): `python3 scripts/mr4/qc_veo.py lab/mr4/veo/V06_l2.mp4 V06` (cần `/tmp/yunet.onnx` từ huggingface.co/opencv/face_detection_yunet,
  SHA-256 `8f2383e4…52fa4`; `/tmp/yolov8s.pt` từ github.com/ultralytics/assets v8.2.0, SHA-256 `1f47a78b…aa78a`; `pip install ultralytics`).
- Phiên kế (M-c phần 2) sinh 14 khe Veo còn lại: `scripts/mr4/veo.py` dùng được (sửa `MR_PHIEN`, thêm lời vào `loi_veo.json`), chạy TUẦN TỰ.
  Không sinh lại V06 (đã 2 lượt — hết lượt theo V7) và V12 trừ khi điều phối cho phép.

## Đã xong (giờ UTC, 01/11/2026)
| Giờ | Việc | Tệp (LFS) |
|---|---|---|
| 16:28–16:30 | Đọc số dư trước; kiểm voice_id (HTTP 200) | `reports/mr4/so_du_truoc.json` |
| 16:30–16:41 | TTS P00–P21 (22 lượt) | `lab/mr4/tts/P00.mp3` … `P21.mp3` |
| 16:47:36–16:50:28 | Veo V12 lượt 1 | `lab/mr4/veo/V12_l1.mp4` |
| 16:48 | TTS thu lại P17 | `lab/mr4/tts/P17_l2.mp3` |
| 16:51:14–16:53:03 | Veo V06 lượt 1 (trượt QC) | `lab/mr4/veo/V06_l1.mp4` |
| 16:56:54–17:00:02 | Veo V06 lượt 2 | `lab/mr4/veo/V06_l2.mp4` |
| 16:57 | TTS thu lại P19, P01 | `lab/mr4/tts/P19_l2.mp3`, `P01_l2.mp3` |
| 17:04 | Bản xem + số dư sau | `reports/mr4/xem/*.mp4`, `reports/mr4/so_du_sau.json` |
