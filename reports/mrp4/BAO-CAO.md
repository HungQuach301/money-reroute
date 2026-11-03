# BÁO CÁO MR-P4 — Sửa âm + chuyển động máy trên đoạn MR-P3 (116 s, bản M2)

> Phiên Claude Code · 03/11/2026 · nhánh `claude/friendly-hopper-rmvzyy` (từ `main` @ `a8741a4`). Lệnh `[MR · MR-P4]`. Giờ trong báo cáo là **UTC** (Hà Nội = UTC + 7).
> Trần: `openrouter_usd` **1,00**, khác 0, mốc báo 80 %. **Chi thật: OpenRouter 0,4280 USD (43 %)**, 11 lượt tranh — khớp chênh khoá MR. Không 402. Lời, giọng, L2, L3, nhãn, thẻ, clip, nhân vật hoạt hoạ, nhạc theo hồi và điểm cắt khớp phách **không đổi**. **DỪNG — chờ rà.**

## 0. Tóm tắt cho chủ dự án
| Hạng mục | Kết quả |
|---|---|
| Bản xem 540p (116,05 s) | `reports/mrp4/xem/M2_cu.mp4` (= MR-P3 M2) · **`M2_moi.mp4`** · **ghép cạnh nhau `ghep_cu_moi.mp4`** (âm của bản mới) · loa điện thoại `M2_cu_loa.mp4`, `M2_moi_loa.mp4` · **nghe so liền mạch `nghe_so_loa.mp4`** (4 đoạn 12 s, cũ → mới, loa điện thoại) · tờ tranh `truoc_sau.jpg` |
| Âm (mục 1) | Giọng nén 3:1 + **nâng 2–5 kHz +5,4 dB** (so tỉ lệ dải) + khử xì (**đỉnh xì −1,9 dB** so giọng gốc); nhạc **−13,6 dB dưới lời**, sidechain, **dâng −7,0 dB ở khoảng nghỉ**; tiếng nhấn **−6,9…−8,0 dB**; tiếng nền **−22,0…−25,0 dB**; tổng **−14,0 LUFS, đỉnh thật −1,6 dBTP** (wav) / −1,5 (mp4) |
| Loa điện thoại (300 Hz–8 kHz, mono) | cũ **−21,2 LUFS** → mới **−20,0 LUFS** (+1,2 LU, cùng −14 LUFS gốc) — phần lời rõ hơn trên loa nhỏ |
| Độ sâu (mục 2) | Chỉ số **HD (0–100)** cho 28 tranh; **ngưỡng đề xuất 45** (dưới: chỉ đứng yên/cắt), **60** cho lia. Bản đăng: 10/28 tranh dưới 45 |
| Chuyển động (mục 3) | 28 cảnh, mỗi cảnh một kiểu + lý do + từ neo: **đẩy 8 · đứng yên 9 · lia 4 · kéo ra 2 (đúng hai cú lật) · clip 5 · giật 2 (chuyển hồi)**. Bỏ hẳn trôi nhẹ đều |
| Tranh nhiều lớp (mục 4) | 10 tranh phẳng nhất tạo lại: **HD TB 36,2 → 70,0** (mọi tranh ≥ 53,8); QC máy 0 mặt, 0 chữ; mắt: b001 lượt 1 có "bóng người" ở khung cửa → lượt 2 đạt |
| Đề xuất (mục 6) | `reports/mrp4/PHONG-CACH-HINH-v2-BO-SUNG.md` — luật âm, luật độ sâu, bộ từ vựng chuyển động, khối bố cục nhiều lớp cho tiền tố lời sinh tranh |

## 1. Bước 0 — trần, số dư
- `scripts/cp/budget.py`: thêm `"mrp4": {"openrouter_usd": 1.00}` + mốc báo `{"openrouter_usd": 0.80}`, ghi căn cứ lệnh.
- Số dư **trước** (00:27 UTC): credits 176 / usage 145,9061555 → **còn 30,09 USD**; khoá MR usage 22,2513955. Trần 1,00 ≤ số dư − 20 % → đạt BAI-HOC #6.
- Số dư **sau** (01:13 UTC): usage 157,5341325 → **còn 18,47 USD**; khoá MR 22,6793725 (**+0,4280 = sổ phiên** `reports/mrp4/calls.jsonl`). Tài khoản +11,63 USD trong cửa sổ phiên → **≈ 11,20 USD chi ngoài khoá MR** (theo xác nhận trước đây của chủ dự án: kênh lost-places dùng chung) — ghi để điều phối đối chiếu.

## 2. Mục 2 — Máy kiểm độ sâu: chỉ số "độ sâu hữu dụng" (HD)
`scripts/mrp4/sau.py` (gọi lại `scripts/mrp2/sau.py`: Depth Anything V2 Small, Apache-2.0, ONNX @ 4472b73, sha256 khớp MR-P2/P3; ~5,7 s/tranh CPU):
- **HD = 100 · TRẢI · TÁCH · f(GẦN)** — TRẢI = (p95 − p5)/p95 độ sâu thô (độ trải trong khung); TÁCH = trung vị độ sâu lớp gần − phần còn lại (dốc đều như mặt bàn/sàn → nhỏ); GẦN = diện tích lớp gần (% khung), f = min(GẦN/12 %, 1), giảm khi > 55 % (cả khung là vật gần cũng như mặt phẳng). Kèm MÉP (tỉ lệ điểm có mép độ sâu rõ) — chỉ ghi.
- **Thực tế:** TRẢI gần 1 ở hầu hết tranh (mô hình cho độ sâu tương đối) → phân biệt chủ yếu nhờ **TÁCH × diện tích lớp gần**. Xếp hạng khớp mắt trên tờ độ sâu: thấp nhất là a10 (phòng khách nhìn xa, lớp gần 3,7 %), b118 (xích sát mặt tủ), b003 (hành lang = một dốc đều), b141 (mặt bàn nhìn chéo), b116 (đường chân trời không tiền cảnh).
- **Ngưỡng đề xuất:** **HD < 45 → không trượt/không 2.5D** (đứng yên + lớp trong khung, hoặc cắt vào); **45–60 → đẩy/kéo, dolly nhẹ, không lia**; **≥ 60 → mọi kiểu**. Căn cứ: khoảng trống tự nhiên trong phân bố (45,5 a03 … 41,5 b002) và mắt: mọi tranh ≥ 45 có một lớp gần tách khỏi nền; dưới 45 thì không. Giới hạn: 28 tranh một phong cách; ngưỡng cần kiểm lại trên tập 2.
- Cổng chạy tự động trong bộ dựng (`scripts/mrp4/may.py` `cong()`); ở M2_moi không cảnh nào bị hạ kiểu vì 10 tranh dưới ngưỡng đã được tạo lại (b052 HD 42 là clip Veo — không áp máy).

### Bảng độ sâu từng tranh (trước = tranh bản đăng; sau = tranh MR-P4)
| Tranh | HD trước | TÁCH · GẦN % | HD sau | TÁCH · GẦN % | Ở M2_moi |
|---|---|---|---|---|---|
| a10 | **23,4** | 0,84 · 3,7 | **83,5** | 0,86 · 27,9 | tạo lại → lia |
| b118 | **30,6** | 0,35 · 32,0 | **64,8** | 0,71 · 30,6 | tạo lại → đứng yên + rung |
| b003 | **33,1** | 0,37 · 38,0 | **53,8** | 0,57 · 46,6 | tạo lại → đứng yên |
| b141 | **34,8** | 0,42 · 29,8 | **82,6** | 0,83 · 18,6 | tạo lại → đẩy |
| b116 | **35,6** | 0,85 · 5,1 | **72,8** | 0,73 · 23,0 | tạo lại → đẩy |
| b001 | **35,9** | 0,48 · 11,4 | **69,1** | 0,746 · 20,3 | tạo lại (lượt 2) → đẩy |
| b070 | **40,0** | 0,56 · 39,0 | **56,5** | 0,66 · 24,4 | tạo lại → đẩy |
| a12 | **41,0** | 0,41 · 22,0 | **83,6** | 0,86 · 25,5 | tạo lại → đứng yên |
| b002 | **41,5** | 0,44 · 22,1 | **68,2** | 0,69 · 23,0 | tạo lại → đẩy |
| b052 | **42,0** | 0,48 · 32,7 | — | — | clip V06 (giữ) |
| a03 | 45,5 | 0,79 · 7,4 | — | — | clip V01 (giữ) |
| a09 | 46,0 | 0,49 · 28,6 | **64,9** | 0,66 · 24,9 | tạo lại (thay b052) → lia |
| b066 | 49,4 | 0,54 · 30,2 | — | — | clip V03 → kéo ra |
| a01 · a04 | 54,0 · 54,7 | 0,64 · 10,8 / 0,68 · 10,3 | — | — | nhân vật hoạt hoạ → đẩy |
| b065 · b053 | 54,7 · 55,0 | | — | | đẩy · đứng yên |
| a02 · a05 · a15 | 57,0 · 57,3 · 58,5 | | — | | đứng yên · đứng yên · clip |
| b074 · b062 · b067 · a07 | 61,1 · 65,3 · 65,8 · 65,9 | | — | | đứng yên · đứng yên · lia · giật + đứng yên |
| b051 · b064 · b040 · b063 | 66,5 · 69,0 · 69,6 · 71,5 | | — | | clip+giật · lia · clip · kéo ra |
Toàn văn số: `reports/mrp4/do_sau.json`, `do_sau_moi.json`; tờ so cùng khung (tranh | độ sâu | lớp gần tô cam): **`reports/mrp4/xem/truoc_sau.jpg`**.

## 3. Mục 1 — Âm
Bộ dựng `scripts/mrp4/dung_p4.py am`; số đo `reports/mrp4/am_do.json` (pyloudnorm BS.1770 cho lớp; ffmpeg `ebur128 peak=true` cho tệp). Mức lớp tính **tương đối với độ to giọng** (LUFS tích hợp trên các khung có lời).
- **Giọng:** `highpass 70 Hz → acompressor 3:1 (ngưỡng −22 dB, attack 8 ms, release 120 ms, +3 dB) → −1,5 dB @ 250 Hz → +4 dB @ 3,2 kHz (Q 0,9) → −3 dB @ 7 kHz → deesser (i 0,4)`. Chọn sau **thử 7 cấu hình**: bản đầu (nâng 1,3 octave quanh 3,5 kHz) làm dải 5–9 kHz tăng 2,6 dB và đỉnh xì không giảm; khử xì mạnh (i 0,7–0,8) lại cắt cả dải 2–5 kHz. Bản chọn: tỉ lệ dải 2–5 kHz **−15,0 → −9,6 dB** (+5,4), dải 5–9 kHz −16,5 → −14,8 (+1,7, do cả phổ nghiêng lên), **đỉnh xì p95 (khung 20 ms) −4,2 → −6,0 dB** (ít chói hơn giọng gốc).
- **Nhạc:** nhạc theo hồi của MR-P3 (N1/N2 + Eleven Music, cú lật giữ nguyên) qua `sidechaincompress` do giọng điều khiển (−32 dBFS, 6:1, attack 25 ms, release 450 ms) rồi đặt mức đích −13,5 dB dưới lời.
- **Tiếng động:** mỗi tiếng một tệp, đo rồi đặt mức theo đích: nhấn −8 dB (độ to tức thời 400 ms lớn nhất), nền −25 dB (tích hợp). Thêm 2 tiếng vút ở 2 cú giật; bỏ tiếng vút cũ S004 vì trùng cú giật (đo lần đầu: hai tiếng chồng → −5,0 dB, vượt khung).
- **Tổng:** một hệ số tuyến tính về −14 LUFS; đỉnh thật trước limiter > −1,2 dBTP → limiter ở 192 kHz rồi đưa lại −14.

### Bảng mức âm đo được từng lớp
| Lớp | Đích lệnh | **M2_cu** (MR-P3, tái dựng lớp) | **M2_moi** |
|---|---|---|---|
| Giọng (LUFS, đoạn có lời) | — | −14,0 | −13,9 |
| Nhạc dưới lời (so giọng) | −12…−15 dB | −13,8 | **−13,6** |
| Nhạc ở khoảng nghỉ (so giọng) | dâng | −14,8 (không dâng) | **−7,0** |
| Tiếng nhấn (so giọng; cũ 12 tiếng, mới 13) | −6…−10 dB | **−7,8 … −45,6** (búa −7,8; còn lại −15 … −46: gần như không nghe) | **−6,9 … −8,0** |
| Tiếng nền (so giọng, 5 tiếng) | −22…−28 dB | −26,0 … −48,4 | **−22,0 … −25,0** |
| Tổng (tệp mp4) | −14 LUFS, TP ≤ −1 | −14,0 LUFS · TP −1,4 · LRA 2,9 | **−14,0 LUFS · TP −1,5 · LRA 2,2** |
| Bản loa điện thoại (tệp) | để nghe so | −21,2 LUFS | **−20,0 LUFS** |
Ghi chú thật: độ to tích hợp **không đổi** (−14 LUFS là mức YouTube chuẩn hoá; to hơn sẽ bị hạ lại). Cảm giác "to hơn" ở bản mới đến từ (1) giọng có thêm dải 2–5 kHz (dải tai nghe nhạy nhất, loa điện thoại phát được) — đo thấy +1,2 LU trên bản loa; (2) nén giọng (LRA 2,9 → 2,2); (3) tiếng nhấn/nền nghe thấy được (trước đây −15 … −48 dB dưới lời). **Phiên không nghe được âm** — đánh giá cuối cần chủ dự án nghe `nghe_so_loa.mp4` và `ghep_cu_moi.mp4`.

## 4. Mục 3 — Từ vựng chuyển động theo nhịp lời
`scripts/mrp4/may.py`: mỗi cảnh **một kiểu**, chuyển động bắt đầu ở **từ neo − 0,15 s** (mốc whisper của giọng), cubic in-out (gia tốc/giảm tốc), tối thiểu 0,9 s; hoặc đứng yên hẳn. Máy cũ (M2_cu) ở mọi cảnh tranh là **trôi đều** (trượt 30 px — 22 px cảnh có người — + phóng 1,06 → 1,11 suốt cảnh); nhân vật: phóng 1,04 → 1,09 + trượt 20 px. Giật nhanh: 0,14 s ra + 0,18 s vào, lệch 45 % khung, nhoè ngang tới 300 px, tiếng vút; thay hoà cảnh 0,5 s.

### Bảng kiểu chuyển động từng cảnh (M2_moi; giờ bản thử)
| Giờ | Cảnh | HD | Kiểu (M2_moi) | Từ neo | Biên độ | Lý do |
|---|---|---|---|---|---|---|
| 0,00 | a01 | 54,0 | đẩy vào chi tiết | S001 "phone" | phóng 20 % | lời gọi vào điện thoại đang sáng |
| 3,08 | b064 | 69,0 | lia theo dòng tiền | S001 "schedule" | ≈ 14 % khung + thị sai | khoản trả "đúng hẹn" đi vào máy |
| 5,27 | a03 | — | clip V01 | — | — | mưa trên kính (trong khung) |
| 7,02 | b065 | 54,7 | đẩy vào chi tiết | S002 "delay" | 22 % | đẩy vào tin nhắn |
| 8,77 | a02 | 57,0 | đứng yên | S002 "side" | 0 | cảnh 1,3 s — để mắt đọc |
| 10,08 | a04 | 54,7 | đẩy vào chi tiết | S002 "next" | 18 % | nét lo trên mặt nhân vật |
| 11,83 | a05 | 57,3 | đứng yên | S003 "reconstruction" | 0 | câu khẳng định nặng |
| 15,00 | b066 | — | **kéo ra lộ cảnh** | S003 "real" | 22 % | **cú lật** — lộ kho hồ sơ công khai (trên clip V03) |
| 19,10 | a07 | 65,9 | **giật** + đứng yên | S004 "man" | — | **chuyển hồi** sang nhân vật chính |
| 20,54 | b001* | 69,1 | đẩy vào chi tiết | S004 "Horwitz" | 16 % | gương phòng hoá trang |
| 21,99 | b067 | 65,8 | lia | S004 "actor" | ≈ 14 % | lia qua trường quay |
| 23,43 | b062 | 65,3 | đứng yên | S004 "screen" | 0 | 1,4 s, giữ nhịp chuỗi 5 cảnh |
| 24,88 | b002* | 68,2 | đẩy vào chi tiết | S004 "Avery" | 18 % | đồng hồ cát (thời hạn kỳ phiếu) |
| 34,86 | a09* | 64,9 | lia theo dòng tiền | S006 "money" | ≈ 14 % | "the money … would buy film rights" |
| 37,38 | b070* | 56,5 | đẩy vào chi tiết | S006 "rights" | 20 % | "film rights" |
| 39,90 | a10* | 83,5 | lia theo dòng tiền | S006 "such" | ≈ 14 % | tiền "licensed to streaming platforms" → TV |
| 47,22 | b003* | 53,8 | đứng yên | S008 "not" | 0 | câu pháp lý KBCB |
| 50,04 | a15 | — | clip V04 | — | — | chùm máy chiếu |
| 53,05 | b074 | 61,1 | đứng yên | S008 "neither" | 0 | câu pháp lý KBCB |
| 62,46 | a12* | 83,6 | đứng yên | S010 "years" | 0 | **bản án** 20 năm |
| 65,29 | b063 | 71,5 | **kéo ra lộ cảnh** | S011 "story" | 20 % | "This is the story" — mở chuyện |
| 77,84 | b040 | — | clip V02 | — | — | hồ sương ("lull") |
| 96,08 | b141* | 82,6 | đẩy vào chi tiết | S073 "April" | 22 % | hạn 9/4 — điện thoại úp |
| 98,44 | b051 | — | **giật** + clip V05 | — | — | **chuyển hồi** "Closing in" |
| 103,38 | b116:2* | 72,8 | đẩy vào chi tiết | S078 "Horwitz" | 18 % | "emergency case against Horwitz" |
| 105,24 | b052 | — | clip V06 | — | — | cửa két đóng |
| 109,47 | b118:2* | 64,8 | đứng yên + rung | S079 "freeze" | rung đúng chữ | **lệnh phong toả** (câu nặng) |
| 115,78 | b053 | 55,0 | đứng yên | — | 0 | lặng sau cảnh bắt |
(* tranh tạo lại ở MR-P4.) L2, L3, K2, K3 giữ như bản đăng. Toàn văn: `reports/mrp4/dung_M2_moi.json`. Mọi từ neo nằm trong cảnh của nó (lần đầu a12 neo "twenty" rơi vào câu trước — đổi sang "years").

## 5. Mục 4 — Tạo lại 10 tranh "phẳng nhất" với bố cục nhiều lớp
- **Chọn:** 10 tranh HD thấp nhất, trừ b052 (là clip V06 trong M2 — đổi tranh sẽ lệch clip) → thêm a09 (HD 46,0). Các tranh này không phải khung đầu của clip nào trong M2 và không có nhân vật đại diện.
- **Lời:** tiền tố phong cách A + hậu tố y nguyên `reports/mr6/loi_anh.json`, **thêm khối "COMPOSITION — LAYERED DEPTH"** sau tiền tố; mỗi cảnh ghi FOREGROUND / MIDGROUND / BACKGROUND, chủ thể giữ như lời gốc (MR-P1 A / MR-6). Tham chiếu `ref_canh` (a15_l1). `reports/mrp4/anh/loi_anh.json`; script `scripts/mrp4/anh.py` (chép `scripts/mr6/anh.py`, chỉ đổi phiên/đường dẫn).
- **Lượt:** 10/10 có ảnh lượt 1 (0,0384–0,0393 USD/tranh); **1 lượt 2** (b001). Đẩy LFS 2 lô: 00:34:03 và 00:35:11 UTC (tranh sinh 00:31–00:35), lượt 2 đẩy 00:37:52.
- **QC như MR-6:** YuNet + RapidOCR (`scripts/mrp4/qc_anh.py` → `anh/qc_may.json`): **0 mặt, 0 chữ** trên 11 ảnh. Mắt xem từng tranh ở 1376 px:
  - **b001 lượt 1 KHÔNG ĐẠT:** khung cửa mở phía sau có áo tối treo + đôi giày — đọc như **bóng người đứng** trong cảnh phải "không ai"; tờ giấy dán tường có vệt giống chữ. Lượt 2 đổi lời (cửa đóng, tường trống) → đạt.
  - b118: lời ghi "no hands" — đạt (lượt 1 bản đăng có tay). b002: chỉ tay + tay áo + khuy măng sét (đúng luật người vest tối). a10: TV chỉ mảng màu mờ, không logo. a12, b116: không chữ/biển/cờ.
- **Kết quả độ sâu:** HD TB **36,2 → 70,0**; nhỏ nhất b003 53,8 (lớp gần rộng 46,6 % — cây + khung cửa), lớn nhất a12 83,6. Tờ so cùng khung: `xem/truoc_sau.jpg`.
- **Chỉ thay trong bản thử** (`dung_p4.py` nạp đè `dung.tranh` lúc dựng); `lab/mr6/anh` và bản đăng không đổi. Lớp phủ (đèn, bụi, cát, sương) đặt lại toạ độ theo tranh mới (`HIEU_MOI`).

## 6. Mục 5 — Bản xem
- `M2_cu.mp4` = bản sao `reports/mrp3/xem/M2.mp4` (cùng đối tượng LFS). `M2_moi.mp4`: dựng 1080p 260 s (4 tiến trình), xuất 540p. Điểm cắt khớp phách **13/13 trùng M2 cũ** (cùng nguồn phách) → so sánh cùng khung giờ.
- `ghep_cu_moi.mp4` 1920×540 (trái cũ, phải mới; âm bản mới). `M2_*_loa.mp4`: âm lọc 300 Hz–8 kHz, mono. `nghe_so_loa.mp4`: 0–12, 12–24, 90–102, 102–114 s, mỗi đoạn cũ rồi mới (loa điện thoại).
- Đã xem tờ khung cạnh nhau (30 thời điểm): đẩy/kéo/lia/giật đúng từ neo; giật ở 19,1 s và 98,44 s không còn hoà cảnh ma (lỗi bản thử khung đầu — đã sửa trước khi dựng).

## 7. Lệch so với lệnh / việc chưa đạt (nói rõ)
1. **Chưa nghe được âm, chưa xem phát liên tục** — mọi kết luận âm là số đo; chủ dự án nghe `nghe_so_loa.mp4`, `ghep_cu_moi.mp4`.
2. Độ to tích hợp giữ **−14 LUFS** đúng lệnh; nếu chủ dự án vẫn thấy nhỏ thì nguyên nhân là cảm nhận phổ/động, không phải mức tổng — có thể nâng thêm dải 2–5 kHz hoặc nén mạnh hơn (LRA hiện 2,2, đã thấp).
3. Chỉ số HD dùng độ sâu tương đối: TRẢI gần bão hoà (0,7–1,0) nên chưa phân biệt mạnh; ngưỡng 45/60 lập trên 28 tranh một phong cách — cần kiểm lại ở tập 2.
4. b052 (HD 42) và a03 (45,5) không tạo lại vì là khung đầu clip Veo trong M2. b066 là clip nên "kéo ra" là phóng 2D trên clip (không 2.5D).
5. Cảnh a07 đứng yên sau cú giật: lời "The man at the center" có thể hợp đẩy chậm hơn — chọn đứng yên để cú giật đọc rõ; chủ dự án xem quyết.
6. Tiếng vút cũ S004 bị bỏ (trùng cú giật). Số đo lớp "cũ" là **tái dựng** từ mức trong `dung_p3.py` + hệ số loudnorm tuyến tính (tổng đo trên tệp thật khớp −14,0).
7. Tải lại tiếng động CC0 qua `scripts/mrp3/cc0.py` ghi đè giờ tải trong `reports/mrp3/am/cc0.json` — đã hoàn lại tệp (không sửa báo cáo phiên khác); 13/13 sha256 khớp.

## 8. Cần chủ dự án / điều phối
1. Nghe `nghe_so_loa.mp4` + xem `ghep_cu_moi.mp4` → duyệt hướng âm (mức lớp ở §3) và từ vựng máy (§4).
2. Duyệt ngưỡng độ sâu **45 / 60** và luật tạo lại tranh nhiều lớp (đích HD ≥ 55; chi ~0,04 USD/tranh, ~10 % lượt 2).
3. Duyệt `reports/mrp4/PHONG-CACH-HINH-v2-BO-SUNG.md` cùng `reports/mrp3/PHONG-CACH-HINH-v2-DE-XUAT.md` → `docs/PHONG-CACH-HINH.md` v2. Dự phóng: áp khối bố cục nhiều lớp từ đầu cho tranh tập 2 thì **không tốn thêm** (cùng giá tranh); nếu tạo lại tranh cũ: ~0,04 USD/tranh.
