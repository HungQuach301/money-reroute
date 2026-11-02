# BÁO CÁO MR-5 — M-c phần 2 · Tập 1 `tap01-1inmm` (1inMM / Horwitz)

> Phiên Claude Code · 01–02/11/2026 · nhánh `ccr-af44ed0c-12rbdy` (từ `main` @ `d485da0`). Lệnh `[MR · MR-5]`: 14 khe Veo còn lại + nhạc.
> Giờ trong báo cáo là **UTC** (giờ Hà Nội = UTC + 7). **DỪNG ở cuối mốc, chờ rà.** Không merge, không xoá nhánh.
> Lời (`loi.json`) và `SHOT.md` **không sửa chữ nào**.

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| Trần | `mr5` thêm vào `CAPS_PHIEN` (openrouter **8,30 USD** · elevenlabs **6.000** ký tự **tính**), mốc báo 80 % (6,64 USD · 4.800) |
| Chi thật | **OpenRouter 8,00 USD** (96 % trần; 20 clip × 0,40) · **ElevenLabs 3.245 ký tự tính** (54 %). Không có 402 |
| Đối soát | Khoá MR `usage` 1,20 → 9,20 = **8,00** = sổ; tài khoản `total_usage` 79,35476 → 87,35476 = **8,00** → **chi phiên khác = 0** trong cả phiên. `/subscription` 7.043 → 10.288 = **3.245** = sổ. Khớp tuyệt đối |
| Veo | 14 khe: **8 khe đạt lượt 1**, **6 khe cần lượt 2** (V03, V04, V10, V11, V13, V16) — cả 6 đạt ở lượt 2 (3 đạt, 3 đạt có ghi chú). **16/16 khe của tập đã có clip chọn** (`reports/mr5/veo/chon.json`) |
| QC tại nguồn | Không mặt (YuNet: mọi cờ ở clip chọn là báo nhầm — bokeh, tán cọ, ly, hộp phim, xem tờ `_co.jpg`), không chữ đọc được, không logo ở 16 clip chọn. 2 lỗi chỉ cắt ở dựng (V08, V16 dùng 0–7,3 s) |
| Mốc báo 80 % | Chạm ở lượt thứ 17/20 (V13 l2, 6,80 USD) khi còn 3/20 lượt = **15 % việc** (< 20 %) → chạy tiếp theo đúng luật; ghi rõ ở §2.4 |
| Nhạc | 3 bản Eleven Music `music_v1` không lời: mở 40 s · tăng dần P15–P17 136 s · kết 60 s. **825 ký tự tính / phút** (đo thật = số tham chiếu) |
| Đơn giá thật | Veo **1,43 lượt/khe** (14 khe MR-5); cả tập 16 khe / 23 lượt = **1,44**, Veo cả tập **9,20 USD** (≤ trần M-c 9,50) |
| Bản xem | `reports/mr5/xem/to1s.jpg` (tờ 1 s 16 clip chọn), `veo_ghep.mp4` (16 clip, 2:08), `nhac.mp4` (3 bản nối, 4:00) |

## 1. Bước 0 — trần, số dư

| Thời điểm | OpenRouter (tài khoản) | Khoá MR | ElevenLabs |
|---|---|---|---|
| **Trước** 01/11 23:08:09 | `total_credits` 105 / `total_usage` 79,35476 → **còn 25,64524 USD** (≥ 8,30 × 1,2 = 9,96 — V7) | `usage` 1,20 | dùng 7.043 / 157.382 → **còn 150.339** (creator, reset 01/12/2026) |
| **Sau** 02/11 00:01:25 | 105 / 87,35476 → **còn 17,64524 USD** | `usage` **9,20** | dùng 10.288 → **còn 147.094** |

Tệp: `reports/mr5/so_du_truoc.json`, `so_du_sau.json`; `COST-LEDGER.csv` (4 dòng MR-5). `scripts/cp/budget.py`: thêm dòng `"mr5"` vào `CAPS_PHIEN` và `DUNG_BAO_PHIEN["mr5"]` (6,64 USD · 4.800); lõi không đổi. Công cụ đọc số dư: `scripts/mr5/so_du.py` (GET miễn phí, khoá do proxy tiêm, gửi giá trị giả).

## 2. Bước 1 — Veo 3.1 Lite (14 khe)

### 2.1 Cấu hình và cách chạy
`scripts/mr5/veo.py` (chép `scripts/mr4/veo.py`, đổi đường dẫn và ngưỡng): `google/veo-3.1-lite`, **1080p, 16:9, 8 s, `generate_audio: false`**, `negativePrompt` qua `provider.options["google-vertex"]`. Trước **mỗi** lượt: `budget.check()` + `/credits` còn ≥ 0,40 + 1 USD; ghi giờ bắt đầu/xong, `total_usage` tài khoản và `usage` khoá trước/sau vào `reports/mr5/veo_luot.jsonl`. Chạy **tuần tự 1 lượt** (`scripts/mr5/chay_khe.sh`: sinh → preflight riêng, mã thoát 0 → commit → đẩy LFS). Không khung khoá (không khoá Gemini) → V1 "không áp dụng".

**Lời** (`reports/mr5/veo/loi_veo.json`, gửi nguyên văn) dựng từ cột "Nội dung hình" + "Khe Veo" của SHOT, áp bài học MR-4: giấu mặt bằng **ngược sáng / bóng / khung chặt ở tầm mặt bàn** (V07, V14, V16), cảnh **kết bằng trạng thái vật** (ly rời khung, điện thoại nằm lại, bút nằm lại) thay vì chỉ dẫn vị trí; màn hình **úp hoặc nhìn sát mặt bàn**; mô tả khẳng định (cát, sóng, mặt bê tông sạch) ở lượt 2 thay cho phủ định.

### 2.2 Bảng lượt (giờ UTC; chi 0,40 USD mỗi lượt theo `usage.cost` 20/20)

| Lượt | Bắt đầu | Xong | `total_usage` trước → sau | Khoá trước → sau | Còn trước |
|---|---|---|---|---|---|
| V01 l1 | 23:10:15 | 23:12:25 | 79,35 → 79,75 | 1,2 → 1,6 | 25,65 |
| V02 l1 | 23:12:50 | 23:14:41 | 79,75 → 80,15 | 1,6 → 2,0 | 25,25 |
| V03 l1 | 23:14:57 | 23:16:33 | 80,15 → 80,55 | 2,0 → 2,0 | 24,85 |
| V04 l1 | 23:16:46 | 23:18:21 | 80,55 → 80,95 | 2,0 → 2,4 | 24,45 |
| V05 l1 | 23:18:33 | 23:20:23 | 80,95 → 81,35 | 2,4 → 3,2 | 24,05 |
| V07 l1 | 23:20:35 | 23:22:10 | 81,35 → 81,75 | 3,2 → 3,2 | 23,65 |
| V08 l1 | 23:22:23 | 23:24:14 | 81,75 → 81,75 | 3,2 → 3,6 | 23,25 |
| V09 l1 | 23:24:24 | 23:26:14 | 81,75 → 82,15 | 3,6 → 4,0 | 23,25 |
| V10 l1 | 23:26:26 | 23:28:16 | 82,15 → 82,95 | 4,0 → 4,8 | 22,85 |
| V11 l1 | 23:28:28 | 23:30:02 | 82,95 → 83,35 | 4,8 → 5,2 | 22,05 |
| V13 l1 | 23:30:13 | 23:32:04 | 83,35 → 83,75 | 5,2 → 5,6 | 21,65 |
| V14 l1 | 23:32:15 | 23:34:05 | 83,75 → 83,75 | 5,6 → 5,6 | 21,25 |
| V15 l1 | 23:34:15 | 23:36:07 | 83,75 → 84,15 | 5,6 → 6,0 | 21,25 |
| V16 l1 | 23:36:18 | 23:37:53 | 84,15 → 84,95 | 6,0 → 6,4 | 20,85 |
| V04 l2 | 23:39:04 | 23:40:40 | 84,95 → 85,35 | 6,8 → 6,8 | 20,05 |
| V03 l2 | 23:40:54 | 23:42:45 | 85,35 → 85,75 | 7,2 → 7,2 | 19,65 |
| V10 l2 | 23:43:00 | 23:44:34 | 85,75 → 86,15 | 7,2 → 8,0 | 19,25 |
| V13 l2 | 23:44:45 | 23:46:21 | 86,15 → 86,55 | 8,0 → 8,0 | 18,85 |
| V11 l2 | 23:46:33 | 23:48:40 | 86,55 → 86,95 | 8,0 → 8,8 | 18,45 |
| V16 l2 | 23:48:51 | 23:50:25 | 86,95 → 87,35 | 8,8 → 9,2 | 18,05 |

**Chi phiên khác trong lượt:** cột `chi_phien_khac` từng dòng của `veo_luot.jsonl` dao động ±0,40 vì `/key` và `/credits` cập nhật **trễ một lượt** so với nhau (đọc sau 5 s); cộng dồn cả cửa sổ 23:10–23:50 (và tới 00:01): tài khoản +8,00 = khoá +8,00 → **phiên khác chi 0 USD**. Khác MR-4 (≈ 4,00 USD không rõ nguồn), lần này không thấy chi song song.

### 2.3 QC tại nguồn (0 USD)
Mỗi clip (20 clip): `scripts/mr5/qc_veo.py` (chép `scripts/mr4/qc_veo.py`; MR-5 thêm lùi 0,1 s khi khung cuối rỗng — lỗi gặp ở V10_l2): ffprobe; **tờ 0,5 s** + neo (`reports/mr5/veo/<clip>_to05.jpg`, `_neo.jpg`); **YuNet** mỗi 1/8 s (ngưỡng 0,5); **YOLOv8s** mỗi 1/4 s; **`quet_v8.py`** 5 cột. Mới: `scripts/mr5/soi_co.py` cắt các vùng YuNet cờ thành tờ `<clip>_co.jpg` để mắt xác nhận. **Mắt xem** mọi tờ + crop 1:1 vùng chữ/logo/mặt nghi. Máy: OpenCV 5.0, ultralytics, torch 2.15 CPU.

Thông số chung 20/20 clip: 1920×1080, 24 fps, 8,0 s, **không âm**.

| Khe | Lượt | Máy (YuNet / YOLO / V8) | Mắt xem — kết luận |
|---|---|---|---|
| V01 | l1 | 0 / 0 / 0 | **Đạt có ghi chú.** Điện thoại trên bàn, màn hình chỉ là mảng sáng; 1–5 s viền thân máy sáng trắng rồi tối (ánh sáng lan — có thể trông như đổi màu). Không người; neo cuối chỉ điện thoại (V3) |
| V02 | l1 | 118 (bokeh — báo nhầm) / 0 / 0 | **Đạt có ghi chú.** Giọt trên kính đứng yên 0–8 s (so khung 0/4/7,9 s) — V6 đạt. Điện thoại ngửa, nhìn sát mặt bàn: màn hình thành ô màu nhoè, không chữ đọc được (crop 1:1) |
| V03 | l1 | 116 (tán cọ) / 0 / 0 | **Trượt:** lề đường tiền cảnh có 2 biển quảng cáo (một biển hình + chữ giả gần đọc được) và xe đèn sáng |
| V03 | **l2** | 45 (tán cọ, bóng nước) / ≤ 1 conf 0,16–0,22 (chòi) / c3 0,6 s (sóng) | **Đạt.** Bãi cát, sóng, cọ bóng đen, thành phố dải đèn xa; không biển/chữ/logo/người. Sóng → dùng đủ 8 s (V2) |
| V04 | l1 | 5 / 0 / c1 2, c2 1 | **Trượt:** **logo Apple rõ** trên nắp laptop (3,5–8 s); sợi "khói" trôi trên tường |
| V04 | **l2** | 3 (hộp phim nhoè) / 0 / c1 1,5 s, 3,3 s (trụ kệ khi lia) | **Đạt.** Không laptop, khung tranh giấy trắng, hộp phim trơn, không chữ/logo |
| V05 | l1 | 0 / ≤ 1 (báo nhầm) / 0 | **Đạt có ghi chú.** Hơi nước mảnh liên tục; sổ trắng; máy tính bỏ túi có **ký hiệu phím chung** (00, +, ×) rõ ở 0–1 s rồi ngoài nét, không thương hiệu, màn hình trống |
| V07 | l1 | 15 (ly, nến) / ≤ 3 (tay) / 0 | **Đạt.** Tay áo vest nâng ly ra khỏi khung, máy đứng yên — không đầu/mặt; neo cuối 6–8 s bàn trống (V3) |
| V08 | l1 | 0 / 0 / 0 | **Đạt có ghi chú.** Hộp kim loại trống, nắp tự nâng 0–1,5 s; **7,4–8,0 s nắp bắt đầu khép** → dựng 0–7,3 s. Bản lề trơn, không chữ |
| V09 | l1 | 0 / 0 / c3 1,9 s, 4,6 s (giấy bay) | **Đạt.** Giấy trắng hai mặt, không chữ/chữ ký; chuyển động tự nhiên |
| V10 | l1 | 0 / 0 / c5 1 | **Trượt V5:** dải bụi/hơi cuộn bùng dọc đường băng 0–8 s. Không số hiệu/sơn hãng |
| V10 | **l2** | 0 / 0 / c2 5,8 s (loá mặt trời trên bê tông — báo nhầm) | **Đạt.** Máy bay đỗ, bóng ngược sáng, không số hiệu/chữ (crop 1:1); bê tông sạch, không bụi/khói |
| V11 | l1 | 0 / 0 / 0 | **Trượt (V8 vật hiện):** vật dài nâu đỏ tự trượt vào nền từ 1 s; đầu chìa có khắc chữ giả |
| V11 | **l2** | 0 / 0 / 0 | **Đạt có ghi chú.** Máy đứng yên, mặt đá trống, hết vật lạ. **Đầu chìa vẫn khắc chữ giả** (ký tự vô nghĩa, không đọc được, crop 1:1) — lời "smooth, unmarked" bị bỏ qua cả 2 lần; hết lượt |
| V13 | l1 | 0 / 0 / 0 | **Trượt nội dung:** ly tầng dưới **đầy** suốt clip (SHOT: "ly tầng dưới trống"); chai có nhãn giấy (chữ mờ) lấn góc 6,0–6,5 s |
| V13 | **l2** | 5 (miệng ly) / 0 / 0 | **Đạt có ghi chú.** Chỉ ly đỉnh có rượu, **ly tầng dưới trống, khô** suốt 8 s; dòng rót đổ đầy ly đỉnh rồi dừng ~6 s, không tràn ("mảnh dần" kém rõ hơn l1); mép cổ chai xanh **không nhãn** lấn góc 0–0,5 s, ~5,5 s. Khung chặt hơn V12 |
| V14 | l1 | 0 / ≤ 2 (tay) / c3 2,3 s (tay) | **Đạt có ghi chú.** Tay (chung chung) cầm điện thoại, màn hình quay ra xa; đặt xuống **ngửa** (lời: úp) — nhìn sát mặt bàn chỉ là mảng xanh, không chữ (crop 1:1); neo cuối 6–8 s không tay |
| V15 | l1 | 0 / 0 / c1 0,0 s (rãnh cột) | **Đạt có ghi chú.** Bậc đá + chân cột, không biển tên/cờ/huy hiệu/người; một dải chạm trên cột (0–2 s) có nét giống ký tự — vô nghĩa, không đọc được |
| V16 | l1 | 1 / ≤ 1 / c3 3 | **Trượt nội dung:** bút nằm sẵn + tay mang cây bút thứ hai, không đặt xuống |
| V16 | **l2** | 0 / ≤ 2 (tay), **neo cuối 1** / 0 | **Đạt có ghi chú.** Một bút; tay ngược sáng (bóng) đặt bút **lên** bìa sổ (lời: cạnh sổ), rút ra tay không ~4,6 s; **7,5–8,0 s đầu ngón tay ló lại mép phải** (YOLO bắt đúng) → dựng 0–7,3 s, neo 4,8–7,3 s không tay (V3) |

Chung 16 clip chọn: không mặt người (thật hay dựng), không chữ đọc được, không logo, không giao diện ứng dụng, không tài liệu; nhân vật chung chung (tay) không nhắm tới người thật nào. Nhãn "ILLUSTRATIVE" thêm ở M-d theo SHOT. Tờ quét V8 `lab/mr5/do/` dựng lại được — **không đẩy**.

### 2.4 Lượt 2, V7 và mốc báo
- Lượt 2 **đổi lời** cả 6 khe (trường `doi_loi` trong `loi_veo.json`); `veo.py` chặn gửi lượt 2 trùng lời lượt 1 và chặn lượt 3.
- Thứ tự lượt 2 theo mức nặng: V04 (logo) → V03 (biển chữ) → V10 (V5) → V13 (sai nội dung cú treo) → V11 (vật hiện) → V16 (hai bút).
- **Mốc báo 80 % (6,64 USD)** chạm sau V13 l2 (6,80 USD) — lúc đó đã xong 17/20 lượt, còn 3 lượt = **15 % việc** (< 20 %) → luật cho chạy tiếp; tổng cuối 8,00 ≤ trần 8,30. Còn 0,30 USD < giá 1 clip → không còn lượt nào khả dụng trong MR-5.

### 2.5 Clip chọn cho dựng (`reports/mr5/veo/chon.json`)
V01 l1 · V02 l1 · **V03 l2** · **V04 l2** · V05 l1 · V06 l2 (MR-4) · V07 l1 · V08 l1 (0–7,3 s) · V09 l1 · **V10 l2** · **V11 l2** · V12 l1 (MR-4; tuỳ chọn 2,0–8,0 s) · **V13 l2** · V14 l1 · V15 l1 · **V16 l2** (0–7,3 s).

### 2.6 Bài học lời Veo (bổ sung MR-4)
- **Hiệu quả:** tay ở tầm mặt bàn + máy đứng yên + vật rời khung (V07) → không lộ mặt ngay lượt 1; ngược sáng biến tay thành bóng (V16 l2); thay phủ định bằng **cảnh khẳng định không còn chỗ cho vật cấm** (bãi cát thay đường có biển — V03; bê tông sạch, máy bay đỗ — V10; bàn chỉ có đèn — V04).
- **Kém:** "no billboards", "smooth unmarked keys", "lower glasses empty" (khi tầng dưới nằm trong khung lúc rót), "face down" (V14), "beside the notebook" — Veo Lite bỏ qua. Chữ giả hay mọc trên **vật thật vốn có chữ** (chìa khoá, laptop, biển, nhãn chai) → nên tránh hẳn vật đó trong lời.
- "Heat shimmer" → Veo vẽ bụi/hơi cuộn (V10 l1); "dust motes" → sợi khói (V04 l1).

## 3. Bước 2 — Nhạc Eleven Music

### 3.1 Cách làm
`scripts/mr5/nhac.py`: `POST /v1/music` (`model_id: music_v1`, `composition_plan`, `mp3_44100_192`). Mỗi lượt `budget.check()` với ước xấu nhất; ký tự tính = **chênh `/v1/user/subscription`** đọc trước và **60 s sau** (bài học MR-4: cập nhật trễ). Phản hồi **không có header ký tự** (chỉ `Song-Id`). Kế hoạch: `reports/mr5/nhac/ke_hoach.json`.

**Không giai điệu nhận ra được:** lời yêu cầu **không nêu tên nghệ sĩ, bài, phim hay tác phẩm nào**; chỉ mô tả nhạc cụ, nhịp, giọng điệu, cấu trúc lớp; `negative_global_styles` có "famous theme", "recognizable melody", "vocals", "lyrics"; motif tối giản (nốt bass kéo dài, ostinato hai nốt, motif piano bốn nốt tự sáng tác). **Chưa ai nghe bằng tai** (phiên không có đường nghe) → điều phối/chủ dự án nghe `reports/mr5/xem/nhac.mp4`.

### 3.2 Kết quả (đo thật)

| Bản | Theo SHOT | Kế hoạch | Dài thật | Ký tự tính | Độ to (I / LRA / đỉnh) |
|---|---|---|---|---|---|
| **N1_mo** | mở tập P00 → thẻ tiêu đề | 3 đoạn: piano tắt tiếng + pad → cello drone → một nốt piano (70 bpm, D minor) | 40,07 s | **550** | −12,6 LUFS / 6,7 LU / −1,3 dBFS |
| **N2_tang_dan** | §4 P15–P17 | 5 đoạn: nhịp tim 60 bpm + bass (38 s) → thêm tích-tắc gỗ (18 s) → dây ostinato 80 bpm (44 s) → thêm trống trầm, dây lên nửa cung (26 s, kết cắt gọn) → nốt piano thấp (10 s) | 136,02 s | **1.870** | −15,4 / 11,2 / −1,3 |
| **N3_ket** | thẻ tổng kết + nguồn chạy chữ | 3 đoạn: motif piano → dây ấm → kết lặng (72 bpm, F major) | 60,03 s | **825** | −17,1 / 1,8 / −3,4 |
| **Tổng** | | 4 phút | 236,1 s | **3.245** (= 825,0 / phút, cả 3 bản) | |

Phổ tần: `reports/mr5/nhac/*_pho.png`. N2 tăng dần đúng cấu trúc: độ to ngắn hạn −42 (0 s) → −24 (15 s) → −13 (30 s), giữ −12…−16 tới 120 s, đoạn kết −17 → −21 rồi tắt ở ~131 s; lớp mới thấy trên phổ ở ~17 s, ~32 s, ~56 s, ~100 s. Ranh giới lớp không trùng khít số giây kế hoạch → **M-d căn theo tệp thật** khi trộn; cắt lặng 1,5 s ở S080 và mức −24 → −18 dB dưới lời làm ở hậu kỳ (SHOT §4).

## 4. Bước 3 — LFS, CHECKPOINT, 402
- Mọi tệp tốn tiền đẩy LFS **trong ≤ 2 phút** sau khi sinh: mỗi clip Veo đẩy ngay sau lượt (commit 23:12:31 … 23:50:31, mỗi commit một clip, ~10 s sau `tai_xong`); nhạc N1 sinh 23:16:50 → đẩy 23:18:05; N2/N3 sinh 23:18:23 / 23:19:33 → đẩy 23:20:44.
- `reports/mr5/CHECKPOINT.md` có mục "Chạy tiếp từ đây".
- **Không có HTTP 402** ở dịch vụ nào; không có lỗi HTTP nào ở lượt trả tiền.

## 5. Bước 4 — Bản xem (`reports/mr5/xem/`)
| Tệp | Nội dung |
|---|---|
| `to1s.jpg` | tờ 1 s toàn bộ 16 clip chọn (hàng = khe, cột 0…8 s) |
| `veo_ghep.mp4` (LFS) | 16 clip chọn nối theo thứ tự khe, nhãn khe, 720p, 2:08, không âm |
| `nhac.mp4` (LFS) | N1 → N2 → N3 (cách 2 s), nền phổ tần cuộn, 4:00 |
Tờ 0,5 s từng clip (cả clip trượt) ở `reports/mr5/veo/*_to05.jpg`. Dựng lại: `python3 scripts/mr5/tao_xem.py`.

## 6. Đơn giá thật (ghi `docs/QUY-TRINH-TAP.md` §6)
| Khoản | Trước MR-5 | **Đo thật MR-5** |
|---|---|---|
| Veo Lite 1080p 8 s không âm | 0,40 USD/clip (MR-4) | **0,40** (20/20) |
| Lượt/khe | 1,5 (2 khe khó, MR-4) | **1,43** (14 khe); cả tập **1,44** (23 lượt / 16 khe) |
| Veo cả tập 1 (M-c) | ước 7,68 (giữa) – 13,20 (cao) | **9,20 USD** (MR-4 1,20 + MR-5 8,00) |
| Eleven Music | ~825 ký tự/phút (tham chiếu, chưa đo) | **825,0** ký tự tính/phút |
| ElevenLabs M-c cả tập | ước ≈ 11.190 tính (giữa) | **9.354** (TTS 6.109 + nhạc 3.245) |

## 7. Tệp
| Tệp | Nội dung |
|---|---|
| `scripts/cp/budget.py` | dòng trần `mr5`, mốc báo |
| `scripts/mr5/so_du.py` · `veo.py` · `chay_khe.sh` · `qc_veo.py` · `soi_co.py` · `nhac.py` · `tao_xem.py` | công cụ phiên |
| `lab/mr5/veo/*.mp4` (20, LFS) · `lab/mr5/nhac/*.mp3` (3, LFS) | tài sản tốn tiền |
| `reports/mr5/calls.jsonl` · `veo_luot.jsonl` · `nhac_luot.jsonl` | sổ trần, chi tiết lượt (giờ, job, usage, quỹ trước/sau) |
| `reports/mr5/veo/loi_veo.json` · `chon.json` · `*_to05.jpg` · `*_neo.jpg` · `*_co.jpg` · `*_qc.json` | lời Veo + kết luận QC, clip chọn, tờ, kết quả máy |
| `reports/mr5/nhac/ke_hoach.json` · `*_pho.png` | kế hoạch nhạc, phổ tần |
| `reports/mr5/xem/` | bản xem |
| `reports/mr5/so_du_truoc.json` · `so_du_sau.json` · `COST-LEDGER.csv` · `CHECKPOINT.md` | số dư, sổ chi, chạy tiếp |
| `docs/QUY-TRINH-TAP.md` §6 | đơn giá đo thật |

## 8. Tự kiểm và điểm còn mở
- Preflight chạy riêng trước **mọi** commit (mã thoát 0; script đẩy chỉ commit khi preflight trả 0); `--range` trước lần đẩy cuối. Không in khoá API (proxy tiêm, gửi giá trị giả); không đưa thông tin cá nhân chủ dự án vào request/repo. Mô hình YuNet/YOLO và torch CPU tải từ nguồn công khai (0 USD).
- **Mở 1 — nghe tai nhạc** (`xem/nhac.mp4`): xác nhận không gợi giai điệu tác phẩm có sẵn và hợp không khí; máy không kiểm được điều này.
- **Mở 2 — quyết các clip "đạt có ghi chú"**: V11 l2 (khắc chữ giả trên đầu chìa, không đọc được — phương án 0 USD: làm mờ ở M-d), V13 l2 (dòng rót đổ đầy rồi dừng thay vì mảnh dần; mép cổ chai không nhãn), V16 l2 (bút đặt lên bìa sổ; cắt 7,3 s), V14 l1 (điện thoại ngửa), V01/V02/V05/V08/V15 (ghi chú nhỏ ở §2.3). Mọi khe trên **đã hết lượt** hoặc trần còn 0,30 USD — sinh lại cần lệnh + trần mới.
- **Mở 3 — V13 và V12 khác khung** (V13 l2 khung chặt hơn, tháp thấy 2 tầng); hai khe nối tiếp nhau ở P12 → P13: M-d cân nhắc chuyển cảnh mềm.
- Kế tiếp đề xuất: **M-d** (dựng, quét V8 cả phim, tờ 1 s cả phim, kiểm pháp lý lần 2) — 0 USD theo UOC-CHI.

**DỪNG — chờ rà.**
