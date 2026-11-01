# BÁO CÁO MR-4 — M-c phần 1 · Tập 1 `tap01-1inmm` (1inMM / Horwitz)

> Phiên Claude Code · 01/11/2026 · nhánh `ccr-aa287726-96bpjx` (từ `main` @ `2a14112`). Lệnh `[MR · MR-4]`: giọng toàn lời + thử 2 khe Veo.
> Giờ trong báo cáo là **UTC** (giờ Hà Nội = UTC + 7). **DỪNG ở cuối mốc, chờ rà.** Không merge, không xoá nhánh.
> Lời (`loi.json`) và `SHOT.md` **không sửa chữ nào**.

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| Trần | `mr4` thêm vào `CAPS_PHIEN` (openrouter 1,60 USD · elevenlabs 8.000 ký tự **tính**), mốc báo 80 % (1,28 USD · 6.400), chặn phụ **gửi** ≤ 16.000 (`TRAN_GUI_PHIEN`, mới) |
| Chi thật | **OpenRouter 1,20 USD** (75 % trần) · **ElevenLabs 6.109 ký tự tính** (76 %), 13.881 ký tự gửi (87 % chặn phụ). Không chạm mốc báo. Không có 402 |
| Đối soát | Khoá MR `usage` 0 → 1,20 = sổ; `/v1/user/subscription` 934 → 7.043 = **6.109** = sổ — **khớp tuyệt đối** |
| Giọng | voice_id `kozBJGqBNTqfBBClLNCL` ("LP-M0b-vd-1", generated) — `GET /v1/voices/{id}` **HTTP 200**. 22 đoạn P00–P21 thu đủ; 3 đoạn thu lại 1 lần (P17, P19, P01) |
| Whisper | 2 lượt (thường + chặn chữ số). Mọi số tiền, ngày, "alleged", "one-in-M-M" khớp ở ít nhất một lượt. **Còn 1 điểm cần nghe tai: "Horwitz" ở P19** (§2.3) |
| Veo | 2 khe rủi ro cao nhất: **V12** (chất lỏng) 1 lượt — **đạt có ghi chú**; **V06** (người không mặt) 2 lượt — lượt 1 **trượt**, lượt 2 **đạt có ghi chú**, cần điều phối quyết dùng (§3.4) |
| Đơn giá thật | **0,40 USD/clip 8 s** (1080p, không âm) · **1,5 lượt/khe** (2 khe khó) · **0,4401 ký tự tính / ký tự gửi** · nhịp giọng **155 từ/phút** |
| ⚠ Quỹ chung | Trong phiên, **tài khoản OpenRouter chi thêm ≈ 3,70 USD không phải của MR** (khoá MR chỉ 1,20) → có phiên khác (nhiều khả năng lost-places) chi song song, **trái tiền đề của lệnh**. Lượt Veo của MR chạy tuần tự; trong cả 3 lượt **không** có chi của phiên khác (§1.2) |
| Bản nghe | `reports/mr4/xem/tap01_giong_ghep.mp4` (13:27, −14,2 LUFS, TP −1,35 dBTP), `xem/V12_l1.mp4`, `xem/V06_l2.mp4` |

## 1. Bước 0 — trần, số dư, voice_id

### 1.1 Số dư (GET miễn phí)

| Thời điểm | OpenRouter (tài khoản) | Khoá MR | ElevenLabs |
|---|---|---|---|
| **Trước** 16:30:36 | `total_credits` 105 / `total_usage` 74,45476 → **còn 30,54524 USD** | `usage` 0, `limit` 100 | dùng 934 / 157.382 → **còn 156.448 ký tự** (creator, reset 01/12/2026) |
| **Sau** 17:04:44 | 105 / 79,35476 → **còn 25,64524 USD** | `usage` **1,20** | dùng 7.043 → **còn 150.339 ký tự** |

Tệp: `reports/mr4/so_du_truoc.json`, `so_du_sau.json`; ghi `COST-LEDGER.csv` (5 dòng MR-4).

### 1.2 Quỹ chung OpenRouter — phát hiện chi song song

Lệnh nêu "không có phiên Veo song song bên lost-places". Số đo **không khớp** tiền đề đó:

| Giờ UTC | `total_usage` tài khoản | Ghi chú |
|---|---|---|
| 16:28:49 | 74,15476 | đọc thử đầu phiên |
| 16:30:36 | 74,45476 | +0,30 — khoá MR vẫn 0 |
| 16:31:49 | 74,75476 | +0,30 |
| 16:33:28 | 75,05476 | +0,30 |
| 16:42:56 – 16:44:38 | 77,35476 | +2,30 trong 10 phút; đứng yên ~2 phút |
| 16:45:29 | 76,95476 | **giảm** 0,40 (hoàn tiền một lượt?) |
| 16:45:55 | 77,75476 | +0,80 |
| 16:56:49 | 78,95476 | gồm 0,80 của MR (V12 l1, V06 l1) → phiên khác +0,40 |
| 17:04:44 | 79,35476 | +0,40 = V06 l2 của MR |

→ Phiên khác chi ≈ **4,00 USD** từ 16:28 đến ~16:56 (bước 0,30/0,40 — khớp giá clip Veo 6 s/8 s), **0 USD trong cả ba lượt Veo của MR** (`chi_phien_khac` = 0,0 ở `reports/mr4/veo_luot.jsonl`). Cách xử lý: số dư (≥ 25 USD) lớn hơn nhiều chi ước phiên × 1,2 (1,92 USD); MR chạy **tuần tự 1 lượt**, kiểm `/credits` và `/key` trước/sau mỗi lượt, ghi giờ. **Điều phối nên đối chiếu nhật ký lost-places** cho cửa sổ 16:28–16:56 UTC.

| Lượt Veo MR | Bắt đầu | Xong | Chi khoá MR | Chi phiên khác trong lượt |
|---|---|---|---|---|
| V12 l1 | 16:47:36 | 16:50:28 | 0,40 | 0,00 |
| V06 l1 | 16:51:14 | 16:53:03 | 0,40 | 0,00 |
| V06 l2 | 16:56:54 | 17:00:02 | 0,40 | 0,00 |

### 1.3 voice_id
`GET /v1/voices/kozBJGqBNTqfBBClLNCL` → **HTTP 200**: name "LP-M0b-vd-1", category `generated` (Voice Design), settings mặc định của giọng (stability 0,5, similarity 0,75, style 0, speed 1,0) — MR-4 dùng nguyên settings lưu trong giọng, không gửi `voice_settings`. Giọng tổng hợp, không nhái người thật (HIEN-CHUONG §4).

### 1.4 `scripts/cp/budget.py`
Thêm dòng `"mr4"` vào `CAPS_PHIEN`, `DUNG_BAO_PHIEN["mr4"]` (1,28 USD · 6.400), và **chặn phụ đơn vị gửi** `TRAN_GUI_PHIEN` + `gui()` + `check_gui()` (sổ ghi meta `"gui"`). Phần lõi không đổi.

## 2. Bước 1 — TTS `eleven_v4`, toàn lời

### 2.1 Cách làm
`scripts/mr4/tts.py`: một lượt mỗi đoạn, text = các câu `"doc"` ≠ false của đoạn, nối bằng dấu cách, áp bảng phát âm sẵn có của `scripts/mr3/loi_md.py` (`SEC` → "S-E-C", `FBI`, `HBO`, `FINRA` → "FIN-rah"); `mp3_44100_128`. Mỗi lượt: `check()` + `check_gui()` với ước xấu nhất hệ số 1,0 (bảng `/v1/models` ghi `eleven_v4` `character_cost_multiplier` **1,0** — **không đúng với số tính thật**, xem dưới).

### 2.2 Hệ số ký tự (đo trước, dự phóng, rồi đo toàn bộ)
- **P00–P02 trước:** gửi 1.366 → tính 602 (header `Character-Cost` 124 + 354 + 124; `/subscription` 934 → 1.536 = +602) → **hệ số 0,4407**. Dự phóng toàn lời: 12.230 gửi × 0,4407 ≈ **5.390 ký tự tính < trần 8.000** → tiếp tục.
- **Toàn phiên:** 25 lượt, gửi **13.881**, tính **6.109** → **0,4401** (dải từng lượt 0,4391–0,4413).
- Sự cố đo (đã sửa, không làm lệch tổng): `/subscription` cập nhật trễ (P00 không đổi sau 30 s; P04 dồn sang P05) → sổ tạm ghi sai P00 (0) và P05 (524); polling liên tục bị **HTTP 429** ở P08 (tệp đã lưu, chưa kịp ghi sổ). Đã sửa sổ theo header `Character-Cost` từng lượt (ghi rõ trường `"sua"` ở từng dòng), P08 ghi tay 325 = chênh `/subscription`. Script đổi sang **header `Character-Cost`** làm số chính; tổng đối soát đầu–cuối khớp tuyệt đối (6.109).

| Đoạn | Gửi | Tính | Dài (s) | Đoạn | Gửi | Tính | Dài (s) |
|---|---|---|---|---|---|---|---|
| P00 | 281 | 124 | 17,9 | P11 | 645 | 284 | 40,1 |
| P01 (+ l2) | 804 + 804 | 354 + 354 | 51,3 (l2) | P12 | 408 | 180 | 25,8 |
| P02 | 281 | 124 | 18,3 | P13 | 232 | 102 | 14,5 |
| P03 | 525 | 231 | 32,5 | P14 | 314 | 138 | 17,8 |
| P04 | 587 | 258 | 37,4 | P15 | 731 | 322 | 44,6 |
| P05 | 604 | 266 | 38,7 | P16 | 606 | 267 | 40,3 |
| P06 | 372 | 164 | 24,8 | P17 (+ l2) | 387 + 387 | 170 + 170 | 26,7 |
| P07 | 647 | 285 | 39,4 | P18 | 678 | 298 | 40,5 |
| P08 | 739 | 325 | 45,0 | P19 (+ l2) | 460 + 460 | 202 + 202 | 28,4 |
| P09 | 499 | 220 | 31,8 | P20 | 309 | 136 | 19,9 |
| P10 | 386 | 170 | 25,8 | P21 | 1.735 | 763 | 112,6 |
| **Một lượt toàn lời** | **12.230** | **5.383** | **774,6 s = 12:55** | **Thu lại (3)** | 1.651 | 726 | |

Nhịp thật: 2.005 từ / 12:55 = **155 từ/phút** (SHOT ước 145 → lời ngắn hơn ước ≈ 55 s; SHOT đóng băng, M-d căn lại mốc thời gian theo tệp thật).

### 2.3 Kiểm whisper (0 USD, máy cục bộ)
`scripts/mr4/kiem_whisper.py`: faster-whisper **medium.en** (int8, CPU), so từng từ với text đã gửi sau chuẩn hoá (số → chữ bằng num2words, URL, gạch nối, "S-E-C"…). Hai lượt: **(1) thường**; **(2) `--so-chu`** — chặn mọi token có chữ số/%/$ để whisper buộc chép số **bằng chữ**, kiểm số tiền/ngày/thứ tự đúng từng từ. Bản chép + mốc từng từ: `reports/mr4/whisper/*.json`. Cờ máy chỉ dẫn; **chưa có ai nghe bằng tai** (phiên không có đường nghe).

| Từ quan trọng | Kết quả |
|---|---|
| **Số tiền, số, ngày** (650 triệu, 25–45 %, 35.000 – 1,5 triệu, 2,33 triệu, 5,7 triệu, ~230 triệu, 230.361.884, 240 tháng, 74,2 triệu, các năm 2013–2024, "April fifth", "February fourteenth"…) | **Khớp** ở ít nhất một lượt, mọi đoạn. Lệch chỉ là cách viết của whisper ("25% to 45%" chèn thêm "%"; "1.5 million"; "sec.gov"); lượt 2 bỏ năm vì chính cơ chế chặn chữ số — lượt 1 đã khớp các năm đó. "fourteenth" (P18) lượt 1 chép "14," mơ hồ → lượt 2 xác nhận **"fourteenth"** |
| **"alleged" / "alleges"** | Khớp mọi câu (0 lệch ở cả hai lượt) |
| **"one-in-M-M"** (14 lần) | Khớp 13/14 ở lượt 1. **P17** lượt 1: "won an MM" → **thu lại P17**; P17_l2 lệch y hệt ở cả hai lượt; sau đó lượt 2 trên **P17 bản 1** ra sạch "one in M M" → **dùng P17 bản 1**. (Lượt thu lại P17 hoá ra không cần — 170 ký tự — do lượt 2 whisper chưa có lúc quyết thu lại.) |
| **Zachary Horwitz / Zach Avery / Mark C. Scarsi / HBO / Netflix / Los Angeles / Latin America / FBI / FINRA** | Khớp, trừ "Horwitz" → "Horowitz": **P19** (cả hai lượt, p 0,92) và **P01** (chỉ lượt 2). Thu lại cả hai (1 lần): **P01_l2 sạch cả hai lượt → dùng P01_l2**; **P19_l2 vẫn "Horowitz"** ở cả hai lượt → hết lượt thu lại, **giữ P19 bản 1, đánh dấu cần nghe tai**. Độ dài từ "Horwitz" ở P19 (0,32–0,36 s) nằm trong dải các lần đúng (0,20–0,52 s) → không thấy dấu hiệu chèn âm tiết; nhiều khả năng whisper thiên chính tả "Horowitz" trong ngữ cảnh "judgment against …". Cần rà bằng tai |
| Khác (không phải từ quan trọng) | "films'" ↔ "film's" (P09, đồng âm), "principal" ↔ "principle" (P14, đồng âm), "sub-investors" viết liền, "antifraud" tách, "adviser/advisor", "BrokerCheck" tách — không lệch âm |

Bản đã chọn cho dựng: **P01 → `P01_l2`; còn lại bản 1** (P17, P19 bản 1). Ghi trong `reports/mr4/xem/tap01_giong_ghep.json` và `scripts/mr4/ghep_giong.py`.

## 3. Bước 2 — Veo 3.1 Lite qua OpenRouter (2 khe)

### 3.1 Cấu hình
`POST /api/v1/videos` (bất đồng bộ, poll 15 s, tải `/content`), `google/veo-3.1-lite`, **1080p, 16:9, 8 s, `generate_audio: false`**, `negativePrompt` qua `provider.options["google-vertex"]` (có trong `allowed_passthrough_parameters`). Giá trên `/api/v1/videos/models` (đọc 01/11/2026): 0,05 USD/s không âm (0,08 có âm) → 0,40 USD/clip. **Không khung khoá** (không có khoá Gemini) → **V1 "không áp dụng"**. Lời gửi nguyên văn: `reports/mr4/veo/loi_veo.json` (dựng từ cột "Nội dung hình" + "Khe Veo" của SHOT, không đổi nội dung cảnh).

### 3.2 Chọn khe và lý do
Xếp 16 khe SHOT theo ba yếu tố rủi ro của lệnh (chuyển động · hơi nước/chất lỏng · dáng người không mặt):
- **V12** (hàng 29, P12 — tháp ly rượu, rót từ đỉnh tràn xuống tầng dưới): **chất lỏng chảy liên tục + vật thuỷ tinh xếp chồng** — vật lý chất lỏng và hình học ly là chỗ Veo hay hỏng (ly biến dạng, nước bắn/nổ). Hình này còn dùng lại ở V13 và thẻ bài học L2 (P21) → thử sớm có lợi nhất. Rủi ro cao hơn V05 (hơi nước nhẹ) và V07 (chỉ nâng ly).
- **V06** (hàng 17, P06 — người lưng quay về máy, ngoài nét, bên cửa sổ, cầm điện thoại; neo cuối người ra khỏi khung): khe **duy nhất có cả dáng người toàn thân + chuyển động đi ra khỏi khung + màn hình**; rủi ro mặt (HIEN-CHUONG §4), V3 (neo cuối), V8 (người mờ dần/hiện lại), màn hình có chữ. Rủi ro cao hơn V07/V14/V16 (chỉ tay).

### 3.3 QC tại nguồn (`scripts/mr4/qc_veo.py`, 0 USD)
Mỗi clip: ffprobe; **tờ 0,5 s** (17 ô) + neo đầu/cuối (`reports/mr4/veo/<clip>_to05.jpg`, `_neo.jpg`); dò mặt **YuNet** mỗi 1/8 s (ngưỡng 0,5 — thấp để bắt cả mặt mờ/nghiêng); dò người **YOLOv8s** mỗi 1/4 s; **`scripts/common/quet_v8.py`** 5 cột trên chính clip (dung một khe). Mắt xem mọi tờ + soi crop 1:1 các vùng bị cờ. Máy/mô hình: OpenCV 5.0 (không còn `CascadeClassifier` → dùng YuNet), ultralytics 8.4.197, torch 2.15 CPU.

| Clip | Thông số | Mặt (YuNet) | Người (YOLO) | quet_v8 | Mắt xem |
|---|---|---|---|---|---|
| **V12 l1** | 1920×1080, 24 fps, 192 khung, 8,0 s, không âm | 9 cờ → **báo nhầm** (rơi vào chân/miệng ly) | 0–1,5 s: 1 (conf 0,24–0,34) | 0 nghi; dãn khung không | Rót–tràn liên tục, ly không biến dạng, không bắn/nổ; tháp 2 tầng (lời: 4 tầng). **0–1,6 s: đầu ngón tay + cổ chai + mép tay áo ở góc trên trái** (lời ghi "no hand"), trượt ra khỏi khung tự nhiên khi máy tiến — không mặt. Chai nền **nhãn trơn, mờ, không chữ/logo đọc được** (crop 1:1). Neo cuối: không người |
| **V06 l1** | như trên | 5 cờ: 3,0 s; **4,5–4,9 s** | 1 người 0–5,25 s; 0 từ 5,5 s | c1 2,0 s (nếp rèm — báo nhầm) | **TRƯỢT:** 0,3 s **lộ rõ mặt nghiêng được chiếu sáng** (mũi, môi, mắt); 4,6–5,0 s quay nghiêng; người to, nét (SHOT: "ngoài nét"); đi ra **trái** (lời: phải). V3 neo cuối đạt |
| **V06 l2** | như trên | 1 cờ 0,62 s (vùng tóc) | 1 người 0–5,5 s; 0 từ 5,75 s | c1 3,0 s (nếp rèm khi máy lia) + c3 2,8 s, 4,2 s (khung cửa dịch do lia) — **cả ba báo nhầm** (xem tờ `lab/mr4/do/V06_l2_v8-to/`, không đẩy) | **Đạt có ghi chú:** người **ngược sáng thành bóng**, chỉ thấy gáy/lưng; 0–3 s có **viền sáng tai và mi** của bóng nghiêng — không thấy mắt/mũi/miệng. Đầu **vẫn trong khung** (lời yêu cầu cắt ngang vai). Màn hình điện thoại **quay về máy**, hiện khung ngắm cửa sổ (người đang chụp cửa sổ), một dấu chữ rất nhỏ ở đầu màn hình **không đọc được**. Đi ra **trái** lúc ~5,6 s, máy lia theo mượt, không nhảy/mờ dần. Neo cuối 6–8 s: cửa sổ trống — **V3 đạt** |

Chung cả 3 clip: không logo, không chữ đọc được, không giao diện nền tảng, không tài liệu; không có người thật nào được nhắm tới (nhân vật chung chung, HIEN-CHUONG §4). Nhãn "ILLUSTRATIVE — not the real person" thêm ở hậu kỳ (M-d) theo SHOT.

### 3.4 Kết luận khe và việc cần điều phối quyết
- **V12: đạt sau lượt 1** (không dùng lượt 2). Dựng có thể vào từ 2,0 s nếu muốn bỏ hẳn đầu ngón tay; SHOT/HIEN-CHUONG cho phép tay không mặt nên giữ cả 8 s cũng được.
- **V06: đạt có ghi chú sau lượt 2 — hết lượt theo V7.** Điểm cần quyết: (a) bóng nghiêng ngược sáng có viền tai/mi ở 0–3 s có tính là "không mặt" theo SHOT ("tay, lưng, bóng, ngoài nét") không — phiên đánh giá **đạt** vì không lộ nét mặt nào; (b) màn hình quay ra máy (không chữ đọc được). Nếu điều phối thấy chưa đạt: phương án 0 USD là dùng **5,8–8,0 s** (cửa sổ trống) + đầu clip làm mờ thêm ở hậu kỳ, hoặc **đổi thiết kế khe** ở tập sau (tay + điện thoại cận, không có đầu) — sinh thêm lượt V06 cần lệnh mới.
- Bài học lời Veo (cho M-c phần 2): Veo Lite **bỏ qua** "no hand", "head never inside the frame", "steps to the right", "four tiers", "small in the frame" — chỉ dẫn **phủ định và vị trí** kém tin cậy; chỉ dẫn **ánh sáng** (ngược sáng → bóng) hiệu quả nhất để giấu mặt.

## 4. Bước 3 — LFS, CHECKPOINT, 402
- Mọi tệp tốn tiền đẩy LFS **≤ 10 phút** sau khi sinh (thời điểm đẩy: 16:33:48 cho P00–P02 sinh 16:30–16:33; 16:37:36 cho P03–P07; 16:39:13 cho P08; 16:41:17 cho P09–P21 sinh 16:39–16:41; 16:50:14 cho P17_l2 sinh 16:48; 16:51:06 cho V12_l1 sinh 16:50; 16:53:36 cho V06_l1 sinh 16:53; 16:57:47 cho P19_l2/P01_l2 sinh 16:57; 17:01:21 cho V06_l2 sinh 17:00; 17:05:05 cho bản xem). Tệp dựng lại được (tờ quét V8 `lab/mr4/do/`) **không đẩy**.
- `reports/mr4/CHECKPOINT.md` có mục "Chạy tiếp từ đây".
- **Không có HTTP 402** ở dịch vụ nào. Có 1 lần **HTTP 429** của `GET /v1/user/subscription` (đọc số dư, miễn phí) — không phải lượt trả tiền; đã bỏ polling.

## 5. Bước 4 — đơn giá THẬT (thay số tham chiếu)
Đã ghi vào `docs/QUY-TRINH-TAP.md` §6 (thêm cột "Đo thật MR-4", giữ cột tham chiếu):

| Khoản | Tham chiếu (lost-places) | **Đo thật MR-4** |
|---|---|---|
| Veo 3.1 Lite 1080p, 8 s, không âm | 0,40 USD/clip | **0,40 USD/clip** (`usage.cost` 3/3) |
| Lượt/khe | ~1,1–1,2 | **1,5** (V12: 1, V06: 2) — mẫu 2 khe khó nhất; khe tĩnh dễ hơn có thể ~1,0 |
| TTS `eleven_v4` ký tự tính / gửi | ~0,44 | **0,4401** (6.109 / 13.881) |
| Nhịp giọng | 145 từ/phút (SHOT ước) | **155 từ/phút** |

Dự phóng phần còn lại của M-c (để điều phối đặt trần phiên sau; chưa phải đề xuất chính thức): 14 khe Veo còn lại × 0,40 × 1,2–1,5 lượt = **6,72–8,40 USD** (+ biên lượt 2); nhạc chưa đo. Giọng toàn lời đã xong.

## 6. Tệp
| Tệp | Nội dung |
|---|---|
| `scripts/cp/budget.py` | dòng trần `mr4`, mốc báo, chặn phụ gửi |
| `scripts/mr4/tts.py` · `kiem_whisper.py` · `veo.py` · `qc_veo.py` · `ghep_giong.py` | công cụ phiên |
| `lab/mr4/tts/*.mp3` (25, LFS) · `lab/mr4/veo/*.mp4` (3, LFS) | tài sản tốn tiền |
| `reports/mr4/calls.jsonl` · `tts_luot.jsonl` · `veo_luot.jsonl` | sổ trần, chi tiết lượt TTS/Veo (giờ, job, usage, quỹ trước/sau) |
| `reports/mr4/whisper/*.json` | bản chép whisper + mốc từ + danh sách lệch |
| `reports/mr4/veo/` | lời Veo + kết luận QC (`loi_veo.json`), tờ 0,5 s, neo, `*_qc.json` |
| `reports/mr4/xem/` | **bản nghe**: `tap01_giong_ghep.mp4` (+ `.json` mốc đoạn), `V12_l1.mp4`, `V06_l2.mp4` |
| `reports/mr4/so_du_truoc.json` · `so_du_sau.json` · `COST-LEDGER.csv` · `CHECKPOINT.md` | số dư, sổ chi, chạy tiếp |
| `docs/QUY-TRINH-TAP.md` §6 | cột đơn giá đo thật |

## 7. Tự kiểm và điểm còn mở
- Preflight chạy riêng trước **mọi** commit (mã thoát 0); `--range origin/main..HEAD` trước lần đẩy cuối. Không có email/khoá trong tệp; không in khoá API (proxy tiêm, script gửi giá trị giả).
- Không chép thông tin cá nhân chủ dự án vào request/repo. Không truy cập trang chặn bot. Mô hình whisper/YuNet/YOLO tải từ Hugging Face / GitHub release công khai (0 USD).
- **Mở 1 — nghe tai** P19 ("Horwitz") và nghe toàn bản ghép (whisper không thay tai: ngữ điệu, nhấn, ngắt câu chưa được chấm).
- **Mở 2 — quỹ chung:** đối chiếu chi ≈ 4,00 USD của phiên khác 16:28–16:56 UTC với nhật ký lost-places; xác nhận quy tắc chạy song song cho M-c phần 2.
- **Mở 3 — V06:** quyết dùng V06_l2 hay đổi thiết kế khe (§3.4).
- `/v1/models` ElevenLabs ghi hệ số 1,0 cho `eleven_v4` nhưng tính thật 0,44 → trần phiên sau tính theo số đo, giữ chặn phụ ký tự gửi.

**DỪNG — chờ rà.**
