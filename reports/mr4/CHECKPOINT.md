# CHECKPOINT — MR-4 (M-c phần 1, tập 1 `tap01-1inmm`)

## Chạy tiếp từ đây
- Trần: `MR_PHIEN=mr4 python3 scripts/cp/budget.py` (sổ `reports/mr4/calls.jsonl`; openrouter 1,60 USD; elevenlabs 8.000 ký tự tính, gửi ≤ 16.000).
- TTS: `MR_PHIEN=mr4 python3 scripts/mr4/tts.py P03 … P21` — bỏ qua đoạn đã có tệp `lab/mr4/tts/Pxx.mp3`.
- Hệ số ký tự tính đo P00–P02: 602 / 1.366 = 0,4407 (header Character-Cost = chênh /v1/user/subscription).

## Đã xong
| Giờ (UTC) | Việc | Tệp |
|---|---|---|
| 16:30–16:33 | TTS P00, P01, P02 | lab/mr4/tts/P00.mp3, P01.mp3, P02.mp3 (LFS) |
