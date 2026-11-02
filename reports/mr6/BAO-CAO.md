# BÁO CÁO MR-6 — Tập 1 `tap01-1inmm` theo PHONG-CACH-HINH v1 → bản dựng chờ G2

> Phiên Claude Code · 02/11/2026 · nhánh `ccr-93d57c5c-q2ib0q` (từ `main` @ `f3cff07`). Lệnh `[MR · MR-6]`. Giờ trong báo cáo là **UTC** (Hà Nội = UTC + 7).
> Trần: `openrouter_usd` 10,00 · khác 0 · mốc báo 8,00. **Chi thật 7,4795 USD** (khớp khoá). Không 402. Lời, giọng, nhạc **không sửa**. **DỪNG — chờ rà + G2.**

## 0. Tóm tắt cho chủ dự án
| Hạng mục | Kết quả |
|---|---|
| Bản xem | **`reports/mr6/xem/tap01_540p.mp4`** (960×540, 14:32) · bản cuối 1080p `lab/mr6/dung/tap01_1080p.mp4` (LFS) · tờ 1 s `reports/mr6/xem/to1s_1…4.jpg` |
| Bảng shot mới | `docs/tap01-1inmm/SHOT2.md` — **267 cảnh**, mỗi câu 1–3 cảnh (+ cảnh chen ở câu dài), mốc theo whisper giọng thật; `SHOT.md` giữ làm lịch sử |
| L1 tranh | **166 tranh** dùng (148 mới MR-6 + 18 MR-P1) · 192 cảnh tranh, TB **2,70 s/cảnh** · 150 tranh sinh, **0 sinh lại**, 6 sửa bằng cắt khung, 2 bỏ |
| L2 đồ hoạ động | **20 đồ hoạ** (G01–G20) bằng mã, hiện theo mốc từ, hạt tiền, số đếm, 1 điểm nhấn đỏ cam — 54 cảnh, 259 s |
| L3 hồ sơ thật | **14 crop trang** (5 PDF), nền ngà, khoanh câu — 63 s; tránh mọi trang/dòng cấm của SHOT |
| Cảnh động | Veo ảnh→video: **3 clip dùng** (K2 thành phố, K3 điện thoại đêm, K5 hải đăng); K1 hết 2 lượt (bị lọc), K4 loại ở QC · clip tả thực cũ chỉ **V10–V13** chỉnh màu |
| Âm | **−14,3 LUFS, đỉnh thật −1,3 dBTP** (tệp 1080p; ebur128) |
| Kiểm | tờ 1 s cả phim; quét V8 4 clip Veo; máy đối chiếu chữ **300 chuỗi, 0 cờ thật** (1 báo nhầm URL đã duyệt); **kiểm pháp lý lần 2 (tác tử độc lập): vòng 1 CHƯA ĐẠT (1 CHẶN + 9 nên sửa) → 2 vòng sửa → ĐẠT**; N2/N3/N18 mở lại **HTTP 200**; trạng thái vụ ngày dựng: không ân xá/giảm án |
| Gói phát hành | `docs/tap01-1inmm/phat-hanh/PHAT-HANH.md` — T1, mô tả EN (12 nguồn + dòng khai AI), 21 chương, thẻ, "AI use = Yes", ngày đọc trang Help |

## 1. Bước 0 — trần, số dư, chi phiên khác
- `scripts/cp/budget.py`: thêm `"mr6": {"openrouter_usd": 10.00}` vào `CAPS_PHIEN` và mốc báo `"mr6": {"openrouter_usd": 8.00}`.
- Số dư **trước** (03:26:21): OpenRouter credits 125 / usage 105,68662 → **còn 19,31338 USD**; khoá MR 10,831859. ElevenLabs dùng 17.963 / 157.382 → còn 139.419.
- Số dư **sau** (04:11:16): usage 113,16616 → **còn 11,83384 USD**; khoá MR **18,3113955**. ElevenLabs không đổi (17.963).
- **Đối soát:** khoá +7,47954 = tài khoản +7,47954 → **chi phiên khác = 0** trong cửa sổ phiên (03:26–04:11). Cột `chi_phien_khac` từng lượt dao động (±0,40) do `/key` và `/credits` cập nhật lệch nhau — cộng dồn bằng 0.
- **Ngoài cửa sổ phiên** (sau MR-P1 02:26 → trước MR-6 03:26): tài khoản OpenRouter +15,70 USD và ElevenLabs +7.675 ký tự **không phải khoá MR** (khoá MR đứng yên 10,831859) — ghi để chủ dự án đối chiếu (lần thứ ba sau MR-4, MR-P1).
- Sổ: `reports/mr6/calls.jsonl`, `COST-LEDGER.csv` (4 dòng MR-6), `so_du_truoc.json`, `so_du_sau.json`.

| Khoản | Lượt | Chi (USD) | Căn cứ |
|---|---|---|---|
| Tranh NB 2.1 (16:9, 1K) | 150 đạt + 2 mất kết nối | **5,8795** | `usage.cost` 150 lượt (TB **0,0387**, 0,0380–0,0422) + **0,07792** điều chỉnh đối soát khoá cho 2 lượt mất kết nối (b038, b057: `ConnectionResetError` sau khi gửi — tính tiền, không nhận ảnh) |
| Veo 3.1 Lite ảnh→video | 4 đạt + 3 failed | **1,60** | 4 × 0,40 (`usage.cost`); 3 lượt failed tính 0 (đối soát khoá: chênh trong cửa sổ K1 l1 = đúng tiền 9 tranh chạy song song) |
| **Tổng** | | **7,4795 / 10,00** | = chênh khoá. Mốc 8,00 **không chạm** |

Ghi sổ có 2 dòng điều chỉnh (đều có lý do trong dòng): −0,3471 (K1 l1 ghi nhầm chênh khoá lẫn tiền tranh song song) và +0,07792 (2 lượt mất kết nối). Sau đó `veo.py` sửa: không dùng chênh khoá khi có lượt song song (completed → `usage.cost`/đơn giá; failed → 0); `anh.py` ghi sự kiện mất kết nối vào `anh_luot.jsonl` và vòng chạy thử lại 1 lần.

## 2. Bước 1 — SHOT2 (mỗi câu 1–3 cảnh, mốc whisper giọng thật)
- `scripts/mr6/moc_cau.py` → `reports/mr6/moc_cau.json`: căn 101 câu đọc với từ whisper (bản "sochu", MR-4) bằng so khớp token; 99/101 câu khớp ≥ 0,8 (thấp nhất S103 0,67 — "BrokerCheck" chép rời), mọi mốc tăng đơn điệu. Dòng thời gian = giọng đã duyệt (`tap01_giong_ghep.json`) + **4 khe không lời 4 s** cho thẻ KBCB chỉ chữ (S019 sau P03, S033 sau P06, S072 sau P15, S076 sau P16 — S076 đặt cuối P16 vì lời P16 liền mạch).
- `scripts/mr6/shot2.py` (dữ liệu bảng) → `docs/tap01-1inmm/SHOT2.md` + `reports/mr6/shot2.json`. Tổng **872,0 s (14:32)**: giọng 824,1 s + giữ thẻ tổng kết 8 s + danh sách nguồn ~40 s (nhạc N3).
- Phân bổ: L1 tranh 192 cảnh / 519 s · Veo ảnh→video 3 cảnh / 17 s · clip tả thực cũ 4 / 14 s · L2 54 / 259 s · L3 14 / 63 s. Cảnh đổi 0,35 s trước tiếng; hoà cảnh 0,5 s.
- Mỗi tranh dùng ≤ 2 lần (lần 2 khung cắt/chuyển động khác — `shot2.py` chặn bằng assert).

## 3. Bước 2 — L1 tranh (Nano Banana 2.1)
- Lời: `scripts/mr6/tranh_ds.py` → `reports/mr6/loi_anh.json` (150 cảnh mới; tiền tố + hậu tố **nguyên văn** tờ A MR-P1). **Hai tham chiếu** theo PHONG-CACH-HINH §4: `ref_nv` = `lab/mrp1/A/a01_l1.png` (chỉ cảnh có nhà đầu tư, 24 tranh), `ref_canh` = `lab/mrp1/A/a15_l1.png` (cảnh không nhà đầu tư, 126 tranh, lời ghi rõ "The investor woman is NOT in this scene"). Kết quả: **không còn lỗi "nhân vật lọt cảnh"** của MR-P1 (0/126).
- Sinh: `scripts/mr6/anh.py` + `chay_anh.sh` — tuần tự, mỗi lượt `check()` trần + `/credits` ≥ ước + 1 USD; đẩy LFS theo lô ≤ 5 phút (preflight chạy riêng, mã 0 mới commit): 19 lô 03:32–04:10.
- Dùng lại MR-P1: 18 tranh A (a14 l2 giữ khung cắt MR-P1; a17 bỏ ở vòng sửa 2 — lộ má/tai người vest tối). a01, a04, a13 cũng dùng như tranh tĩnh.
- **QC** (`scripts/mr6/qc_anh.py`, YuNet + RapidOCR, như MR-P1 → `reports/mr6/qc_may.json`) + **mắt** xem tờ ghép 150 tranh:

| Kiểm | Máy | Mắt — kết luận |
|---|---|---|
| Chữ/số/logo đọc được | **0/150** | Marquee rạp (b083) trống; màn hình/giấy trắng hoặc mờ; không tiền giấy |
| Mặt ngoài nhân vật đại diện | 9 cờ (b015, b019, b031, b035, b084, b085, b096, b123, b136) | Người vest tối: chỉ lưng/bóng (b031 bóng đen ngược sáng, không nét mặt) — đạt. Khách/đám đông tự sinh: b015, b019, b084, b085, b096 chỉ dáng/lưng, mặt tối — giữ. **b136** (chuỗi người thì thầm, nhiều mặt rõ) → **bỏ** |
| Lỗi khác (mắt) | — | **Cắt khung (0 USD)**: b021, b023 (bóng người lạ trong cảnh "không người"), **b049** (viền nghiêng đầu ở mép phải — luật §4 "không góc nghiêng"), b082 (người bạn lộ má), b107 (bóng mặt phản chiếu trên kính), b123 (hình tròn giống con dấu trên tường). **Bỏ b127** (giống trang tài liệu có dòng chữ + chữ ký — HIEN-CHUONG §4) |
| Biếm hoạ sắc tộc | — | Không thấy |

Sinh lại: **0** (≤ 1/tranh cho phép, không cần). Tệp sửa: `reports/mr6/cat_khung.json`.

## 4. Bước 3 — L2 đồ hoạ động (10 luật §2)
`scripts/mr6/l2.py` (vẽ PIL theo khung, 0 USD). Mọi đồ hoạ: nền than + lưới mờ; hiện dần đúng **mốc từ** của giọng (`tw(câu, từ)`); tiền = **hạt chạy dọc đường nối**; số **đếm lên** rồi phóng nhẹ khi dừng; **một** điểm nhấn đỏ cam; easing; nhãn tầng + nguồn ở lớp tĩnh góc dưới (do `dung.py`, theo `loi.json`).

| Lệnh tối thiểu | Đồ hoạ | Điểm nhấn |
|---|---|---|
| Lời hứa vs thực tế (P03/P08) | G03 vòng chào mời (5 nút, hạt chạy, vòng quay về) · G08 "ON PAPER vs IN FACT — admitted" (✗ rights not acquired / no distribution agreements; dòng ◐ SEC riêng) · G09 giấy tờ "FAKE — admitted" → "ALL FROM HIM" | vòng "paid back" · ✗ · dấu FAKE |
| Kỳ phiếu + 35 % → ~82 % (P04–P05) | G01, G04 (securities · $35,000–$1.5M · 6/12 tháng · +25–45 % đếm) · G05 cột "over the life of the note" 35 % → 1.35 × 1.35 = 1.8225 → ≈ 82 %; cột 70 % (×2) | ≈ 82 % |
| Phễu 5 nhóm → 250+ (P07) | G07 (5 nhóm hiện ở "five", ~140 chấm nhà đầu tư con, đếm 250+, "a figure he reserved the right to contest", vạch đứt NO DIRECT CONTRACT) | NO DIRECT CONTRACT |
| Dòng tiền + vòng Ponzi (P10–P12) | G10 (nhánh film rights gạch bỏ; 4 dòng hạt) · G11 ◐ co-investment ($2.33M, ≈ $5.7M cash) · G12 vòng Ponzi (dòng trả "PAID ON TIME" quay về, BUY MORE NOTES · RAISE MONEY FROM OTHERS) | earlier investors / tiền nhà đầu tư khác |
| Trục vỡ nợ → đếm ngược 9/4 → bắt (P13–P17) | G13 (~Dec. 2019, ≈ $230 MILLION) · G14 · **G15** trục ~Mar. 12 → Apr. 5 → Apr. 6 → May 4, ô APRIL 9 viền đỏ cam, bộ đếm 28 → 4 → 3 DAYS, **dừng ở S080** rồi xám (không ghi gì vào ô April 9) | ô APRIL 9 |
| Số đếm lên | $650,000,000+ (G02) · 20 YEARS (G02, G16 240 MONTHS = 20 YEARS) · $230,361,884 (G16) · ≈ $74.2M (G17) | |
| Thẻ tổng kết động (P21) | G18 (3 LESSONS · 5 RED FLAGS · 1 RULE hiện theo "three/five/one"; 3 thẻ bài học có hình gọi lại) · thẻ dấu hiệu chồng lên tranh gọi lại đoạn tương ứng · G19 thẻ tổng kết (chữ SHOT.md §3 đã duyệt) giữ 8 s · G20 danh sách nguồn | số đỏ cam RED FLAG |

## 5. Bước 4 — L3 hồ sơ thật + thẻ nền tối
- 14 crop (`SHOT2.md` §3): ảnh trang pdftoppm 220 dpi, **không vẽ lại chữ**, nền ngà `#F4F1EA`, khung khoanh đỏ cam + nền dạ quang nhạt hiện sau 0,7 s; vị trí khoanh tìm máy từ `pdftotext -bbox` (bỏ qua số dòng lề). Trang dùng: N7 tr. 8, 11 (×2), 12 dòng 11–14; N1 tr. 3 ¶5, tr. 5 ¶22, tr. 9 ¶46–47, tr. 13 ¶76–77; N4 tr. 3 §III; N22 tr. 6 dòng 3–4, 13–15, 21–22. **Không** dùng N8 tr. 1/3, N1 bảng ¶25, N7 tr. 12 dòng 23–28, N22 tr. 1, N22 tr. 6 dòng 10 (danh sách cấm SHOT).
- Thẻ KBCB: nền tối chồng lên tranh, **4 s** (S008, S019, S033, S045, S072, S076); tiêu đề kênh, thẻ tên, thẻ bài học (trích đúng lời), thẻ dấu hiệu P21 — đều nền tối chồng tranh, ≤ 4 s (thẻ dấu hiệu theo cả câu).

## 6. Bước 5 — Cảnh động
| Khe | Khung đầu | Kết quả | Dùng |
|---|---|---|---|
| K1 (P00) | a01 (nhà đầu tư, bếp) | l1, l2 **failed** — "no output (content may have been filtered)"; l2 đã đổi lời + `personGeneration: allow_adult` | **Hết lượt V7** → S001 dùng tranh tĩnh a01 (không lượt 3) |
| K2 (P01 S011) | a06 (bóng lưng, thành phố) | đạt l1; người đứng yên, chỉ lưng | ✔ |
| K3 (P15 S068) | l1 a04 (nhà đầu tư) **bị chặn ảnh đầu vào** (Vertex); l2 đổi khung đầu b065 (điện thoại sáng trên bàn đêm, không người) | đạt l2; màn hình mờ, crop 1:1 không đọc được | ✔ |
| K4 (P17 S081) | b053 (văn phòng trống) | sinh đạt, nhưng **mắt thấy vệt bụi/khói xoáy** quanh đèn 2,5–8 s (V5/V8) — `quet_v8.py` c2 không bắt (chỉ tính mảng từ dưới đường trời) | **Loại** → tranh tĩnh b053 |
| K5 (P21 S102) | b148 (hải đăng) — đổi trước lượt 1 sau bài học K1/K3 | đạt l1 | ✔ |
**Bài học:** Veo ảnh→video qua OpenRouter **không nhận khung đầu có người** (kể cả nhân vật tự nghĩ ra, người lớn) — lọc/chặn, không tính tiền. Từ tập 2: khung đầu Veo chỉ cảnh vật/không người.
Clip tả thực cũ: V10 (máy bay, P10), V11 (chìa khoá, P11 — kéo sáng thêm −0,13), V12 (tháp ly rót, P12), V13 (tháp ly cạn, P13) — chỉnh màu teal–hổ phách + hạt (`GRADE` trong `dung.py`). Tờ 0,5 s mắt xem + `quet_v8.py` cột 1–4: `reports/mr6/veo/quet_v8.json`; chọn: `reports/mr6/veo/chon.json`.

## 7. Bước 6 — Dựng
`scripts/mr6/dung.py` (0 USD; 4 tiến trình theo khúc, concat): 1920×1080, 25 fps, H.264 CRF 19 → `lab/mr6/dung/tap01_1080p.mp4`; 540p từ bản 1080p. Phông: IBM Plex chưa có đường tải chính thức (như MR-P1) → Liberation Serif / Inter / JetBrains Mono.
Âm: giọng 22 đoạn đã duyệt (P01_l2, còn lại bản 1) đặt theo `moc_cau.json`; **N1** 0–40 s (−20 dB, tắt dần); **N2** từ 487,9 s, mức −24 → −18 dB, **cắt lặng 1,5 s ở S080** (603,3 s) rồi đoạn "Aftermath" (126–136 s của bản nhạc) −26 dB; **N3** từ 812 s tới hết, nâng khi hết lời, tắt dần 3 s. Loudnorm hai lượt (đích −14 / TP −1,5). Đo trên tệp ra (`reports/mr6/do_am.json`): âm trộn −14,3 LUFS / −1,5 dBTP; **1080p (AAC 256k) −14,3 LUFS / −1,3 dBTP**.

## 8. Bước 7 — Kiểm
| Kiểm | Kết quả | Tệp |
|---|---|---|
| Tờ 1 s cả phim | 872 ô; phiên xem cả 4 tờ sau mỗi lần dựng → sửa: bộ đếm sai "25–12%" (G01), màn đen 13:53–14:05 (danh sách nguồn), V11 quá sáng | `reports/mr6/xem/to1s_1…4.jpg` |
| Quét V8 (clip Veo) | `quet_v8.py` cột 1–4: 0 cờ ở K2, K3, K4, K5; mắt loại K4 (máy lọt vệt khói xoáy) | `reports/mr6/veo/quet_v8.json` |
| Chữ trên hình ↔ lời/hồ sơ | `scripts/mr6/doi_chieu_chu.py` trên sổ chữ do bộ dựng ghi (`chu_tren_hinh.json`): lần đầu 70 cờ (số đếm trung gian + 5 tiêu đề L2 dùng từ ngoài lời: "countdown", "stake", "paperwork", "reassurances") → sửa (tiêu đề dùng chữ của lời; sổ chỉ ghi số dừng) → **300 chuỗi, 1 cờ** (`adviserinfo.sec.gov` — URL trong chân thẻ đã duyệt SHOT.md §3; máy tách từ theo dấu chấm nên báo nhầm) | `reports/mr6/doi_chieu_chu.json` |
| Kiểm pháp lý lần 2 (tác tử độc lập, chỉ đọc) | Vòng 1: **CHƯA ĐẠT** — CHẶN: thiếu "not the real person" khi nhân vật xuất hiện lần đầu ở P05, P08, P12, P15, P16; nên sửa: G15 thiếu ◐ cho trích ¶76, ngoặc kép giả trích (G06, G11), "NONE" mạnh hơn thừa nhận (G08), câu bảo lưu 250+ quá nhỏ, dòng nguồn tràn (S071, S088), số đếm trung gian, ký hiệu "35% × 35%", a17 lộ má/tai. **Vòng sửa 1** sửa hết → kiểm lại: **ĐẠT** (còn #10 một phần) → **vòng sửa 2**: a17 thay bằng a08 | `docs/tap01-1inmm/kiem/mr6_phap_ly_lan2.md` |
| S052 (N12) | Xác minh qua API DOJ (HTTP 200, 22-027): "$6 million … residence, luxury cars, and travel by private jet, according to the government’s sentencing memorandum" — khớp thẻ | như trên |
| N2, N3, N18 | Mở lại bằng UA khai báo của kênh (chỉ trong header; script đọc từ biến môi trường, **không** ghi vào repo): **HTTP 200** cả ba; câu then chốt có ("Emergency Asset Freeze", "690 Million", "one in a million", "HBO or Netflix", "April 5, 2021"; trang tip) | `docs/tap01-1inmm/kiem/mr6_nguon.json` |
| Trạng thái vụ ngày dựng | 03:51 UTC: "Horwitz" **không có** trên 3 trang ân xá/giảm án DOJ (Trump "Updated October 20, 2026"; Biden pardons "May 14, 2026"; commutations "July 9, 2025"). Docket (N9) vẫn chưa mở được (MR-3: 403, không vượt) → không nói gì về kháng cáo | như trên; `PHAT-HANH.md` §5 |

## 9. Bước 8 — Gói phát hành
`docs/tap01-1inmm/phat-hanh/PHAT-HANH.md` (sinh máy `scripts/mr6/phat_hanh.py`): tiêu đề **T1** "How an Actor Raised $650 Million on Fake Film Deals"; mô tả EN (tóm tắt, câu KBCB, ghi chú nhãn tầng, **21 chương** theo mốc giọng, **12 nguồn** đã mở có liên kết, 4 liên kết kiểm/báo cáo, dòng khai AI HIEN-CHUONG §6); 12 thẻ (không HBO/Netflix, không "scam"); **"AI use" = Yes**; trang Help https://support.google.com/youtube/answer/14328491 ("Disclosing use of GenAI content") đọc **02/11/2026 03:53 UTC**, HTTP 200. Thumbnail: không làm (lệnh không yêu cầu).

## 10. Lệch so với lệnh / việc chưa đạt (nói rõ)
1. **Cảnh động: 3 clip Veo ảnh→video** (lệnh ≤ 5): K1 bị lọc 2/2 lượt, K4 loại ở QC. Không sinh thêm khe mới (giữ đúng V7 và tinh thần "khoảnh khắc lớn"); trần còn 2,52 USD.
2. **Số tranh** 166 dùng (lệnh ~170–190): 150 sinh − 2 bỏ + 18 MR-P1 (a17 bỏ ở vòng sửa 2). Kèm 3 cảnh Veo + 4 clip cũ, mật độ L1 TB 2,70 s/cảnh (PHONG-CACH ~2,5 s).
3. **Âm** −14,3 LUFS (lệch 0,3 LU so với đích −14; trong dung sai đo thường dùng ±0,5); đỉnh thật −1,3 dBTP đạt ≤ −1.
4. Mất kết nối 2 lượt tranh (tiền 0,078 USD không nhận ảnh) — đã sửa công cụ, đã ghi sổ qua đối soát khoá.
5. Hai bản thử ngắn có tranh giữ chỗ lọt vào commit `2331907` (LFS) → đã gỡ khỏi cây ở `38037a4` (lịch sử còn).
6. Tầng ◐ cho phán quyết đồng thuận SEC (S087–S089) ghi nhãn "◐ ALLEGED · consent judgment, no findings of fact"; lời công tố S090–S092 "◐ ALLEGED · prosecutors' words" — điều phối xem cách viết nhãn.

## 11. Cần chủ dự án / điều phối
1. **G2:** xem `reports/mr6/xem/tap01_540p.mp4` (+ 1080p), gói `PHAT-HANH.md`, chi 7,48 / 10,00 USD.
2. Đối chiếu chi ngoài khoá MR (+15,70 USD OpenRouter, +7.675 ký tự ElevenLabs, 02:26–03:26 UTC).
3. Quyết luật Veo tập 2: khung đầu không người (bài học K1/K3).
4. Trước ngày đăng: đọc lại trang Help khai AI, kiểm lại trạng thái vụ (N9 docket vẫn chưa mở được — không vượt).
