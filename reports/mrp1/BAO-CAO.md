# BÁO CÁO MR-P1 — Thử phong cách minh hoạ + bằng chứng thật (tập 1, P00–P03)

> Phiên MR-P1 · 02/11/2026 · nhánh `claude/mrp1-illustration-episode-1-8n4p6c` (từ `main` @ `fd703b2`). Trần: openrouter 2,00 USD, khác 0. **Chi thật 1,6319 USD** (42 lượt ảnh). Không 402. **DỪNG — chờ rà.**

## 0. Tóm tắt cho chủ dự án
- Hai bản xem 540p, cùng giọng thật P00–P03 + nhạc N1, cùng thẻ chữ B1 và 2 trang hồ sơ thật:
  - **A — bán hiện thực, tông tối:** `reports/mrp1/xem/A.mp4` · tờ 1 s `A_to1s.jpg`
  - **B — phẳng/đồ hoạ theo B1:** `reports/mrp1/xem/B.mp4` · tờ 1 s `B_to1s.jpg`
- Giá thật **0,0389 USD/tranh** (Nano Banana 2.1, 16:9, 1K). Sinh lại **2/40 = 5 %** (a14 ở cả hai biến thể), cộng 3 tranh sửa bằng cắt khung (0 USD).
- Dự phóng cả tập (≈ 16 phút): **6,0 USD** (mật độ như bản thử) · **7,8 USD** (dày hơn, ~2,5 s/cảnh) · **12,7 USD** (≈ 2,2 s/cảnh như video tham chiếu, mỗi cảnh một tranh mới) — §5.
- Cần chủ dự án quyết: A hay B (hoặc trộn), mật độ cảnh, và xử lý 16 clip Veo đã làm (9,20 USD) — §7.

## 1. Bước 0 — trần, số dư, giá model
- Thêm dòng `"mrp1": {"openrouter_usd": 2.00}` vào `CAPS_PHIEN` và mốc báo `1.60` (80 %) vào `DUNG_BAO_PHIEN` (`scripts/cp/budget.py`).
- Số dư **trước** (01:59 UTC): OpenRouter total_credits 115 / total_usage 87,35476 → **còn 27,64524 USD**; khoá MR usage 9,2. ElevenLabs còn 147.094 ký tự (không dùng). `reports/mrp1/so_du_truoc.json`.
- Số dư **sau** (02:26 UTC): total_usage 89,98662 → **còn 25,01338 USD**; khoá MR 10,831859 (+1,631859 = sổ phiên, khớp). `reports/mrp1/so_du_sau.json`.
- **Quỹ chung:** tài khoản tăng 2,63186 USD trong phiên = MR 1,63186 + **1,00000 USD không phải của MR**. Đối chiếu số dư ghi theo từng lượt (`anh_luot.jsonl`): đến hết lượt cuối của MR (02:15:41 UTC) phần ngoài khoá = 0; 1,00 USD phát sinh **sau** lượt cuối, trước lúc đọc số dư sau (02:15:41–02:26:26 UTC). Nguồn chưa xác định (như MR-4) — chờ chủ dự án đối chiếu.
- **Model ảnh (GET `/api/v1/models` + `/endpoints`, miễn phí; `reports/mrp1/gia_model.json`):** `google/gemini-nano-banana-2.1` tồn tại ("Google: Nano Banana 2.1", nhà cung cấp Google AI Studio), giá prompt 0,0000015 · completion 0,0000075 · **image_output 0,00003 USD/token**. Các model ảnh khác trong danh mục: `gemini-3.1-flash-image` (0,00006/token ảnh), `gemini-3-pro-image` (0,00012), `gemini-3.1-flash-lite-image` (0,00003), `openai/gpt-5.4-image-2`, `gpt-5-image(-mini)`, `gemini-2.5-flash-image`. Dùng NB 2.1 theo lệnh.

## 2. Hai biến thể — tranh và tờ phong cách
| | A — bán hiện thực, tối | B — phẳng, B1 |
|---|---|---|
| Tờ phong cách | `reports/mrp1/A/PHONG-CACH.md` | `reports/mrp1/B/PHONG-CACH.md` |
| Lời sinh | `reports/mrp1/A/loi_anh.json` | `reports/mrp1/B/loi_anh.json` |
| Tranh (LFS) | `lab/mrp1/A/a01–a20_l1.png` + `a14_l2.png` | `lab/mrp1/B/a01–a20_l1.png` + `a14_l2.png` |
| Số tranh dùng | 20 | 20 |
| Chi | 0,8097 USD (21 lượt) | 0,8222 USD (21 lượt) |

- 20 cảnh giống nhau cho hai biến thể (chỉ khác tiền tố phong cách) để so phong cách trên cùng nội dung. Nhất quán nhân vật: `a01` sinh trước, mọi tranh sau gửi kèm `a01` làm tham chiếu → nhà đầu tư giữ đúng tóc/kính/áo vàng mù tạt ở a01, a02, a04, a05, a08, a13, a17, a18 (cả A và B — xem tờ 1 s).
- **Cảnh dưới ~20 tranh/biến thể (ngưỡng thấp của lệnh "~20–25")** để còn dư trần cho sinh lại; tranh dùng lại bằng khung cắt khác (a09, a12, a13 × 2) → 23 cảnh tranh.

## 3. QC mỗi tranh (luật hình)
Máy: `scripts/mrp1/qc_anh.py` (YuNet dò mặt + RapidOCR dò chữ) → `reports/mrp1/qc_may.json`. Mắt: tờ ghép + phóng 1:1 các vùng nghi.

| Kiểm | Kết quả |
|---|---|
| Chữ/số/logo đọc được (OCR, điểm ≥ 0,6) | **0/42 tranh**. Mắt: màn hình/poster/phong bì đều trắng hoặc mờ; mặt tiền toà án không khắc chữ; không tiền giấy, không tài liệu |
| Mặt người thật / Horwitz | Người vest tối chỉ lưng/bóng/tay ở a06, a07, a08, a14, a16, a17, a18, a20. **a14 lượt 1 (A và B) lộ mép má + tai** ở góc 3/4 sau (máy cờ mặt ở B, điểm 0,66) → **sinh lại lượt 2** ("đèn trước mặt, đầu vai thành bóng đen thuần") → đạt (bóng thuần) |
| Mặt ngoài nhân vật đại diện | a17 (A, B): khách nền nhà hàng có mặt nhỏ, mờ (máy cờ 2 mặt) — người tự sinh, không phải người thật, nhưng trái tờ phong cách → **cắt khung bỏ** (0 USD) |
| Nhân vật lọt cảnh | a14 lượt 2 (A, B) và a16 (B): tham chiếu `a01` kéo nhà đầu tư vào cảnh "chỉ một người quản lý" → **cắt khung bỏ** (0 USD). Bài học ghi trong tờ phong cách: tách tham chiếu nhân vật và tham chiếu cảnh |
| Biếm hoạ sắc tộc/quốc tịch | Không thấy. Quả địa cầu (a19) chỉ là cung sáng, không nhãn |
| Tài liệu giả | Không có (cảnh "giấy nợ" thay bằng bắt tay + thẻ số liệu; phong bì trắng) |
| Nhãn | "ILLUSTRATIVE — not the real person" ở cảnh đầu mỗi đoạn (P00 a01, P01 a06, P02 a14, P03 a17); bong bóng tin nhắn chung có "ILLUSTRATIVE — not a real message" (SHOT hàng 1–2) |

Khung cắt dùng trong bản xem: `CAT` trong `scripts/mrp1/dung.py` (A: a14 l2, a17; B: a14 l2, a17, a16).

## 4. Lớp bằng chứng thật + dựng
**Hai crop trang hồ sơ thật** (tài liệu chính phủ Mỹ, PDF trong repo, SHA-256 tính lại khớp `NGUON.md`), ảnh trang pdftoppm 200 dpi, **không vẽ lại** — chỉ thêm khung khoanh đỏ cam + nền dạ quang nhạt, tiêu đề tài liệu, huy hiệu tầng, dòng nguồn:
| Cảnh | Nguồn | Cắt | Khoanh | Tầng | Câu lời |
|---|---|---|---|---|---|
| TL1 0:42,5–0:46,8 | N7 Plea Agreement, Dkt. 45, **tr. 11 dòng 8–15** | dòng 8–15 | "purported copies of the / distribution agreements were fake." | ● CONVICTED · admitted in plea | S007 (nguồn N7 tr. 11) |
| TL2 1:57,3–2:04,9 | N1 SEC Complaint **¶5, tr. 3 (số trang PDF), dòng 4–13** | dòng 4–13 (không lấy dòng 1–3 về nhà riêng) | "primarily / from Latin America," và "“Strategic Partners[]”" | ◐ ALLEGED | S018 (nguồn N1 tr. 3 ¶5) |
Cả hai trang không thuộc danh sách cấm crop của SHOT. TL2 có tên HBO/Netflix → thẻ KBCB S019 hiện ngay sau (6 s, không lời) như SHOT hàng 12.

**Dựng** (`scripts/mrp1/dung.py`, 0 USD, dựng lại được): dòng thời gian = giọng thật đã duyệt (`tap01_giong_ghep.json`: P00 0,00 · P01_l2 19,45 · P02 72,28 · P03 92,14) + thẻ S019 6 s → **132 s**. 34 cảnh: 23 tranh (TB 3,2 s), 9 thẻ chữ/sơ đồ B1 (TB 5,1 s), 2 bằng chứng (TB 6,0 s); máy đẩy/kéo/lia có làm mượt, hoà cảnh 0,5 s, mở/đóng đen. Mốc cảnh theo từ whisper (`reports/mr4/whisper/`). Bảng cảnh: `reports/mrp1/xem/{A,B}_khung.json`. Nhãn tầng + nguồn theo `loi.json`/SHOT: S004 (Indictment p. 1), S005 (● Plea pp. 9–10), S009 (● Plea p. 12), S010 (● Judgment Dkt. 75 p. 1; DOJ 22-027), S012 (● Plea p. 8), S013 (SEC Lit. Rel. 25067), S014 (◐ Indictment p. 1), S015–S017 (● Plea pp. 9–10), S018 (◐ Complaint ¶5), S008/S019 KBCB. Không chữ nào trên hình ngoài lời/nguồn đã có.
**Âm:** giọng P00–P03 + nhạc N1 (`lab/mr5/nhac/N1_mo.mp3`, 40 s) **lặp nối** cho đủ 132 s, mức −20 dB dưới lời, nâng lên trong 6 s thẻ S019; loudnorm. Đo trên tệp ra: **−14,6 LUFS, đỉnh −1,4 dBFS** (A và B). Nhạc lặp nghe được chỗ nối ở ~0:40, ~1:20 — chỉ cho bản thử; bản thật dùng N1 + N2/N3 theo SHOT.
**Bản xem:** `reports/mrp1/xem/A.mp4`, `B.mp4` (960×540, H.264, 25 fps, AAC, 132,0 s, LFS) + tờ 1 s `A_to1s.jpg`, `B_to1s.jpg`.

## 5. Giá thật, tỷ lệ sinh lại, dự phóng cả tập
- **Giá thật:** 42 lượt, `usage.cost` 42/42; **0,0389 USD/tranh** TB (0,0369–0,0411). Cấu thành: 1.120 token ảnh × 0,00003 = 0,0336 + token chữ đầu ra (~300–700 × 0,0000075) + đầu vào (348 token chữ; ~1.700 khi kèm ảnh tham chiếu × 0,0000015). Tham chiếu chỉ thêm ~0,002 USD/tranh.
- **Sinh lại:** 2/40 = **5 %** (a14 A, a14 B — lộ mép má). Có lỗi phải xử lý tổng 5/40 = 12,5 % (3 sửa bằng cắt khung, 0 USD). Lượt 2 a14 đạt luật mặt nhưng lại lọt nhân vật (sửa bằng cắt) → với tham chiếu tách đôi (tờ phong cách) dự kiến giảm.
- **Thời gian:** ~12–15 s/tranh, tuần tự; 42 lượt trong 12 phút.

**Dự phóng chi ảnh cho cả tập 1** (≈ 973 s theo SHOT; giá 0,0389; +5 % sinh lại; chưa gồm tranh tham chiếu ~0,1 USD):
| Mức | Giả định | Số tranh | Chi |
|---|---|---|---|
| Thấp — như bản thử | 0,152 tranh/s (20 tranh / 132 s), thẻ + bằng chứng chiếm ~44 % thời lượng | ~148 | **≈ 6,0 USD** |
| Giữa | cảnh tranh 2,5 s, tranh chiếm 56 % thời lượng, dùng lại 1,15 cảnh/tranh | ~190 | **≈ 7,8 USD** |
| Cao — nhịp video tham chiếu | 2,2 s/cảnh, tranh chiếm 70 %, mỗi cảnh một tranh mới | ~310 | **≈ 12,7 USD** |
So sánh: Veo tập 1 đã chi 9,20 USD cho 16 clip (~2 phút hình). Nhịp bản thử ~3,9 s/cảnh (tranh 3,2 s) **thưa hơn** lệnh "~2–3 s/cảnh" vì thẻ chữ/bằng chứng cần thời gian đọc; muốn ~2,5 s cần mức Giữa trở lên.

## 6. Lệch so với lệnh (nói rõ)
1. **Độ dài:** lệnh ghi "60 giây mở đầu (P00–P03)", nhưng giọng thật P00–P03 dài **124,7 s** (+ thẻ S019 6 s). Phiên dựng **đủ P00–P03 = 132 s** theo giọng đã duyệt, không cắt lời. Muốn bản 60 s: cắt ở hết S011 (0:70) là ~71 s.
2. **Số tranh** 20/biến thể (ngưỡng thấp ~20–25) để giữ dư trần; mật độ 2–3 s đạt ở cảnh tranh (TB 3,2 s), không đạt ở thẻ chữ.
3. **Mốc 80 %:** lượt thứ 42 (a14 B lượt 2) đưa tổng lên 1,6319 > 1,60. Lúc đó **không còn việc trả tiền nào** (phần còn lại 0 USD: bằng chứng, dựng, QC, báo cáo) → không phải tình huống "còn > 20 % việc"; sau đó **dừng sinh**. Còn 0,368 USD trần chưa dùng.
4. **Phông B1** (IBM Plex) không có trong máy; tải từ github.com/google/fonts trả **403** → không vượt, dùng Liberation Serif Bold / Inter / JetBrains Mono. Ký hiệu ◐/● vẽ bằng DejaVu.
5. Thẻ chữ dùng **B1 cho cả A** (bảng màu đã duyệt) — thẻ sáng chen giữa tranh tối là điểm cần chủ dự án xem.

## 7. Cần chủ dự án quyết
1. Phong cách: **A**, **B**, hay trộn (vd tranh A + thẻ B1 như bản thử).
2. Mật độ cảnh (§5) → trần chi ảnh cho tập 1 và các tập sau.
3. 16 clip Veo tập 1 (9,20 USD, phong cách tả thực): bỏ, hay chen vào như "cảnh vật thể" (ly, chìa khoá, giấy trắng) — lệch phong cách với tranh.
4. Nguồn 1,00 USD chi tài khoản chung 02:15–02:26 UTC (không phải MR).

## 8. Kiểm
- `bash tools/preflight.sh` chạy riêng trước mọi commit (mã thoát 0 mới commit); `--range origin/main..HEAD` trước lần đẩy cuối.
- Tệp tốn tiền (42 PNG) đẩy LFS theo lô trong vòng ≤ 10 phút sau sinh (commit 02:04, 02:06, 02:08, 02:11, 02:14, 02:16 UTC). Bản xem MP4 đẩy LFS. Tờ 1 s, khung json, QC json là tệp dựng lại được (nhỏ, giữ để rà).
- Không gọi ElevenLabs/Gemini/khác. Không khoá API trong tệp. Không thông tin cá nhân chủ dự án trong request/repo.
