# BÁO CÁO MR-S23 — Tập 2 (`irs-callcenter-patel`) + tập 3 (`romance-sunmola`): áp G1 lời + bảng shot PHONG-CACH-HINH v1

> Phiên Claude Code, 02/11/2026. Nhánh `claude/brave-gauss-8c6982` từ `main` @ `f7527af`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD.** Không gọi API trả tiền, không sinh hình/giọng, không gặp 402; `scripts/cp/budget.py` không đổi (MR-S23 không có dòng trần = cấm gọi). Không mạng ngoài `git lfs pull` hai PDF hồ sơ trong repo (SHA-256 khớp NGUON). Không thông tin cá nhân của chủ dự án trong request hay repo.
> Preflight chạy riêng, chỉ commit khi mã thoát 0; `--range origin/main..HEAD` trước khi đẩy. Không merge, không xoá nhánh, không force-push.

## 1. Sản phẩm

| Tệp | Tập 2 — Patel | Tập 3 — Sunmola |
|---|---|---|
| `loi.json` + `LOI.md` (dựng máy) | S021 sửa (§2); `loi: []` | S023 → thẻ chữ (§2); `loi: []` |
| `SHOT2.md` (mới, dựng máy; `SHOT.md` giữ làm lịch sử) | 185 cảnh · ước **12:53** | 207 cảnh · ước **12:21** |
| `UOC-CHI.md` (thay bản MR-K23) | giữa **7,72 USD** + ≈ 9.909 ký tự | giữa **9,43 USD** + ≈ 9.452 ký tự |
| `PHUONG-AN.md` mục 00 (mới) | T1 đã duyệt · 3 tiêu đề Short · luật thumbnail | như trên |
| `phat-hanh/THUMBNAIL-RULES.txt` (mới) | dán nguyên vào công cụ ảnh (khuôn tập 1) | như trên |
| `kiem/mrs23.md` | 2 vòng kiểm câu đổi | 1 vòng kiểm câu đổi |

Công cụ mới (`scripts/mrs23/`, 0 USD, dựng lại được): `shot2.py` (bộ sinh SHOT2 + máy kiểm), `du_lieu_tap02.py`, `du_lieu_tap03.py` (dữ liệu cảnh), `uoc_chi.py`. Sửa `scripts/mrk23/loi_md.py`: thêm luật **KE** (§2). Tóm tắt máy: `reports/mrs23/shot2_tap02.json`, `shot2_tap03.json`.

## 2. Bước 1 — áp quyết định G1 (KBCB đọc ở lần nêu đầu, sau đó thẻ chữ)

**Luật máy mới KE** (`kiem_rieng.kbcb_doc_dau` trong `loi.json`): trong các câu KBCB của cơ quan bị mạo danh, đúng **một** câu đọc. Câu đó phải là câu KBCB đầu tiên, nằm sau lần nêu đầu và cùng đoạn với lần nêu đầu. Mọi câu KBCB còn lại là thẻ chữ.
- Kiểm âm: bản tập 3 trước khi sửa → trượt "2 câu ĐỌC (S004, S023)".
- Kiểm âm: tập 2 đổi S003 ↔ S011 → trượt "không phải câu đầu tiên ngay sau lần nêu đầu".

| Tập | Trước | Sau | Kiểm độc lập |
|---|---|---|---|
| 2 | S003 đọc (lần nêu đầu S002) ✓; S011, S067 thẻ ✓; **S021 đọc** "None of these agencies, in the United States, Canada or Australia…" — đọc lại phần KBCB cơ quan Mỹ (vòng 1 phát hiện) | **S021** chỉ đọc phần Canada/Úc (lần nêu đầu S020): "The tax agencies of Canada and Australia had nothing to do with the calls either."; IRS/USCIS lên thẻ chữ: "The IRS, USCIS and the tax agencies of Canada and Australia had nothing to do with these calls." | Vòng 2: **KHỚP** N4 đ.5–6, không mạnh hơn. Góp ý văn phong "either" (§6) |
| 3 | S004 đọc (lần nêu đầu S002–S003) ✓; **S023 đọc** "To be clear, the U.S. military had nothing to do with it." — đọc lần 2 | **S023 → thẻ chữ** (doc=false), chữ thống nhất với S017/S057/S072: "The U.S. Army and the U.S. military had nothing to do with this scheme." | **KHỚP** N2 tr. 10; mạch S022 → S024 vẫn trôi |

- Không đổi câu nào khác. Câu ◐ HGLOBAL giữ nguyên ("is presumed innocent"). `loi_md.py` chạy lại cả hai tập: **0 lỗi** (K1–K8, KA–KE).
- Thống kê sau sửa:
  - Tập 2: 71 câu (69 đọc, 2 thẻ), 1.857 từ, 11.551 ký tự gửi TTS.
  - Tập 3: 80 câu (75 đọc, 5 thẻ), 1.735 từ, 10.752 ký tự gửi TTS.
- Biên bản kiểm: `docs/tap02-irs-callcenter-patel/kiem/mrs23.md`, `docs/tap03-romance-sunmola/kiem/mrs23.md`.

## 3. Bước 2 — SHOT2 theo khuôn tập 1

| | Tập 2 | Tập 3 |
|---|---|---|
| Cảnh / câu | 1–3 (máy kiểm) | 1–3 |
| L1 tranh | 127 cảnh, TB 3,6 s · **106 tranh mới** (vật/cảnh trống 88 · người thật bóng/lưng/tay 8 · N1 7 · N2 3) | 151 cảnh, TB 3,1 s · **144 tranh mới** (127 · 4 · N1 11 · N2 2) |
| L2 đồ hoạ động | **15** (G01–G15) + thẻ tổng kết, nguồn | **17** (G01–G17) + thẻ tổng kết, nguồn |
| L3 hồ sơ thật | 3 crop N1 tr. 3 (¶1 a), tr. 6 (¶2 g) + 2 thẻ trích nguyên văn | 2 crop N2 tr. 1, 18 + 2 thẻ trích |
| Veo ảnh→clip | **5**, khung đầu đều tranh loại E: không người, không màn hình/thẻ/nhãn (cửa sổ bếp, mưa trên kính, châu thổ, cánh máy bay, bếp sáng) | **5**, như trên (phòng khách đèn, hiên nhà, cổng bay, phòng xử, bình minh) |
| Nhân vật đại diện | N1 người nghe máy (nam ~55, cardigan navy); N2 người con | N1 người phụ nữ (~50, khăn hổ phách); N2 người bạn |

**Máy kiểm `shot2.py` — ĐẠT cả hai tập.** Các luật máy kiểm:
- mỗi câu 1–3 cảnh; cảnh tranh ≥ 1,5 s; mỗi tranh dùng tối đa 2 lần;
- ≥ 6 đồ hoạ L2 động, mỗi đồ hoạ ghi câu hỏi nó trả lời và một điểm nhấn;
- ≤ 5 khoảnh khắc Veo, khung đầu không có người;
- tranh có người thật phải có từ khoá bóng/lưng/tay và không lộ mặt;
- từ cấm hình: biếm hoạ, trang phục dân tộc, quân phục, phù hiệu, logo, con dấu, cờ;
- regex cấm của từng tập (`cam_them`) quét cả tệp SHOT2;
- KB: dòng nào có tên call center phải kèm nguyên câu ◐;
- KC: chữ gợi nhánh ảnh riêng tư xuất hiện ≤ 1 dòng (tập 3 thực tế: 0 dòng);
- tập 3 S033 chỉ là thẻ tối 6 s, không tranh, không nhạc.

Quyết định thiết kế cần điều phối biết:
1. **Mật độ.** Lệnh giới hạn 1–3 cảnh/câu, nên số tranh (106 / 144) thấp hơn mức ~190 tranh/tập của PHONG-CACH-HINH §6, và cảnh L1 trung bình 3,6 s / 3,0 s (chuẩn ~2,5 s).
   - SHOT2 ghi luật: cảnh tranh > 5 s tách thành 2 khung cắt của **cùng** tranh, không tốn thêm tiền.
   - Nếu muốn đúng mật độ, dùng mức "cao" của UOC-CHI (+40 % tranh).
2. **Mốc là ước.** Chưa có giọng, nên mốc tính theo 155 từ/phút. Ở M-c thay bằng mốc whisper như tập 1.
3. **Người thật.** Không vẽ người thật nào ngoài bóng/lưng/tay.
   - Nạn nhân trong hồ sơ: chỉ vẽ đồ vật.
   - Nhân vật đại diện không dùng cho câu về nạn nhân cụ thể (tập 2 S009–S010; tập 3 S034).
   - Tập 3: nhân vật giả "soldier/colonel" vẽ thành **khung hồ sơ trống**, không quân phục, để tránh giống những người đàn ông thật bị lấy ảnh.
4. **L3 tập 3.**
   - N2 tr. 1 chỉ crop tới "Defendant-Appellant.", vì dòng "Appeal from…" có tên thẩm phán quận, tên này nằm trong regex cấm của tập.
   - N2 tr. 10 không crop (có câu trích lời bị cáo và chủ đề khủng bố).
   - **N2 tr. 17 là đề xuất, chưa dùng** (S059 dùng L2 G14). Điều phối thêm trang vào NGUON §4 thì dùng được làm crop.
5. **L3 tập 2.** N1 là PDF quét (không có lớp chữ). Vùng crop mô tả theo đoạn; tọa độ đo bằng ảnh trang ở M-d. Đã xem ảnh tr. 3 và tr. 6 để xác định vùng tránh ¶2(f) và ¶3 (tên 5 nhóm call center); cắt bỏ dòng dấu ECF "*SEALED*" đầu trang. ¶1(b) (USCIS) chưa nằm trong vùng NGUON §4 cho phép → S018 dùng L2; đề xuất điều phối thêm.

## 4. Bước 3 — ước chi + đề xuất trần MỘT phiên M-c+M-d (BAI-HOC mục 9)

Đơn giá BAI-HOC: tranh 0,0389 USD (sinh lại 5 %); Veo 0,40 USD × 1,44 lượt/khe; TTS 0,4401 ký tự tính/gửi; nhạc 825 ký tự/phút.

| | Tập 2 thấp / **giữa** / cao | Tập 3 thấp / **giữa** / cao |
|---|---|---|
| OpenRouter (tranh + Veo) | 6,41 / **7,72** / 10,73 USD | 7,96 / **9,43** / 13,11 USD |
| ElevenLabs ký tự tính (TTS + nhạc) | ≈ 8.067 / **9.909** / 15.117 | ≈ 7.680 / **9.452** / 14.414 |
| **Trần đề xuất** `openrouter_usd` | **9,70** (báo 7,76) | **11,80** (báo 9,44) |
| **Trần đề xuất** `elevenlabs_chars` (tính) | **12.500** (báo 10.000) · gửi ≤ 24.000 | **12.000** (báo 9.600) · gửi ≤ 22.000 |
| Số dư cần (trần ≤ số dư − 20 %) | ≥ 12,13 USD khả dụng cho MR | ≥ 14,75 USD |

- Mức giữa nằm trong khoảng BAI-HOC ước cho tập sau (≈ 9–11 USD).
- Tập 2 rẻ hơn vì ít tranh hơn (§3 mục 1).
- Hai tập chạy liền nhau cần ≈ 21,50 USD trần, tức ≥ 26,88 USD khả dụng. Quỹ OpenRouter chung với lost-places; số dư gần nhất ghi được là 11,83 USD sau MR-6 → **cần nạp trước M-c**.

## 5. Bước 4 — PHUONG-AN

- **Tiêu đề tập đã duyệt (G1):**
  - Tập 2 T1: "Fake IRS Calls From India: How the Money Got Out" (48 ký tự).
  - Tập 3 T1: "A Fake Soldier, 27 Years in Prison: A Romance Scheme" (52 ký tự).
  - Mô tả mỗi tập phải có câu KBCB ở dòng đầu (8e).
- **Tiêu đề Short.** Mỗi tập 3 phương án. Đếm ký tự bằng `len()`, mở lại nguồn để kiểm:

  | Tập | Khuyến nghị | Căn cứ |
  |---|---|---|
  | 2 | **SH1 "He Funded Fraud Call Centers in India. He Got 20 Years."** (55) | ●T N4 đ.6 "operating and funding several India-based call centers from which the fraud schemes were perpetrated"; ● N5 |
  | 3 | **SH1 "A Fake Colonel, a Romance Scheme, 27 Years in Prison"** (52) | ●C N2 tr. 10 "held himself out as a colonel…"; ● 324 tháng |

  - Không tiêu đề Short nào có tên cơ quan bị mạo danh (bài học Short 1).
  - Phương án SH2 tập 2 đã đổi từ "demanded" sang "were told to pay", cho khớp chữ "instructed how to provide payment" ở N4 đ.5.
- **Luật thumbnail riêng:** ở `PHUONG-AN.md` mục 00 và `phat-hanh/THUMBNAIL-RULES.txt` (khuôn 9 điều cấm của tập 1, giữ nhận diện nền ngà).
  - Tập 2 thêm: **không chữ "IRS"/"USCIS"** trên thumbnail (8e — sửa sau rà độc lập; trước đó bản nháp cho "FAKE IRS CALLS"); không logo/con dấu cơ quan; không số điện thoại; không định kiến về Ấn Độ; không tên call center.
  - Tập 3 thêm: **không người nào** (kể cả bóng), không quân phục/phù hiệu, không giao diện hẹn hò, không gì gợi thân mật, không "Nigerian / Prince Charming / scammer".

## 6. Rà độc lập bảng shot + tiêu đề Short

Một tác tử mới (không đọc báo cáo này) rà `SHOT2.md`, `PHUONG-AN.md` mục 00 và `THUMBNAIL-RULES.txt` của hai tập, tự mở nguồn. Kết quả lượt rà: **cần sửa** ở 5/6 tệp. Đã áp hết các sửa dưới đây (commit thứ hai), rồi chạy lại máy: `shot2.py` ĐẠT cả hai tập.

| Mức | Phát hiện | Đã sửa |
|---|---|---|
| Cao | Tập 3 S010: nhân vật đại diện N1 gắn vào câu về **một nạn nhân cụ thể** (người khiếu nại 2012) | Thay bằng tranh chỉ có vật (phong bì trên quầy bưu điện) |
| Cao | Thumbnail tập 2 cho chữ "FAKE IRS CALLS" — tên cơ quan trên bảng tin không kèm câu KBCB, mâu thuẫn với luật tiêu đề Short | Cấm mọi tên cơ quan trên thumbnail; gợi ý "THE CALLS WERE FAKE"; để chủ dự án quyết nếu muốn áp tiền lệ T1 (§7 mục 6) |
| Trung bình | Crop ngoài vùng NGUON §4 cho phép: tập 2 ¶1(b) tr. 3; tập 3 tr. 17 vẫn được dùng ở S059 | Bỏ khỏi bảng cảnh, thay bằng L2; ghi thành đề xuất (§7 mục 2). Thêm luật cắt bỏ dòng dấu "*SEALED*" ở crop N1 |
| Trung bình | Khung đầu Veo có vật vốn mang chữ (màn hình điện thoại/máy tính/laptop, thẻ nhựa, nhãn thùng) — BAI-HOC mục 2 | Đổi cả 5 khung liên quan sang cảnh không chữ (cửa sổ bếp, mưa trên kính, châu thổ, phòng khách, hiên nhà); màn hình sáng làm ở hậu kỳ trên tranh tĩnh (0 USD) |
| Trung bình | G11 tập 2 dùng cho S046 (◐) mà cột nhãn chỉ ghi ● | Thêm "S046 ◐ ALLEGED" |
| Trung bình | Tranh gợi điều hồ sơ không nêu: "12 ghế" cho đại bồi thẩm đoàn; "thang máy bay chính phủ" cho dẫn độ | Phòng nhiều hàng ghế không đếm được; hành lang mở ra ánh sáng |
| Trung bình | Short SH2 tập 3: đoạn gợi ý toàn câu ◐ về nhân vật chính (luật 8b) | Mở rộng đoạn thành S020–S027 (S020–S022 ●C làm trụ) |
| Thấp | Tập 2: cảnh nạn nhân S010 dùng lại bếp của N1; tranh "cười rửa bát" lệch giọng S069; mô tả đèn tự mâu thuẫn; G04 "hai thẻ" liệt kê ba; S021 thiếu lớp chồng | Sửa cả năm |
| Thấp | Short SH1 tập 2 bỏ mất hành vi gian lận; ghi chú "giữ S003" không khớp đoạn gợi ý | Đổi thành "He Funded Fraud Call Centers in India. He Got 20 Years." (N4 đ.6 "from which the fraud schemes were perpetrated"); đoạn S002–S006 |
| Thấp | Tập 3: "Colonel" trong SH1 thuộc nhóm từ quân đội; G03 chấm bản đồ; hình ảnh ảnh úp mặt | Ghi: mô tả Short có KBCB dòng đầu; chấm rải ngẫu nhiên, không theo bang; thay hai tranh ảnh úp mặt |

Các điểm người rà xác nhận đạt:
- Người thật chỉ bóng/lưng/tay; không biếm hoạ sắc tộc; tập 3 không quân phục.
- Veo ≤ 5; mọi dòng có tên call center kèm nguyên câu ◐.
- S033 chỉ là thẻ tối, không chỗ nào khác gợi lại.
- T01 tập 3 cắt trước dòng có tên thẩm phán quận.
- Q01/Q02 khớp nguyên văn.
- Thumbnail tập 3 đạt.

Các sửa này không đổi lời (`loi.json`), nên không cần kiểm lời lại.

## 7. Cần điều phối / chủ dự án quyết
1. **S021 tập 2 — văn phong.** Giữ "…had nothing to do with the calls either." (đã kiểm khớp), hay dùng phương án mượt hơn của vòng 2: "Those agencies, too, were only being impersonated; the tax agencies of Canada and Australia had nothing to do with the calls." (chưa kiểm vòng riêng nếu chọn).
2. **Trang crop thêm:** tập 3 N2 tr. 17 (S059) và tập 2 N1 tr. 3 ¶1(b) (S018) có thêm vào NGUON §4 không? Hiện cả hai dùng L2 thay thế.
6. **Thumbnail tập 2:** giữ luật không chữ "IRS" (khuyến nghị), hay áp tiền lệ T1 ("Fake IRS…") cho thumbnail?
3. **Mật độ:** chấp nhận 1–3 cảnh/câu (103 / 144 tranh) hay cho chen tới ~190 tranh (mức cao UOC-CHI)?
4. **Trần M-c+M-d:** tập 2 9,70 USD + 12.500 ký tự; tập 3 11,80 USD + 12.000 ký tự. Nạp OpenRouter trước.
5. **Tiêu đề Short:** chọn mỗi tập một phương án.

## 8. Còn mở (chuyển sang phiên sản xuất)
- Nghe tai tên riêng ở M-c (bảng phát âm `LOI.md`).
- Kiểm trạng thái vụ ngày đăng: BOP, ân xá, HGLOBAL/các bị cáo ở Ấn Độ.
- Đo tọa độ crop L3 tập 2 trên ảnh trang.
- Phiên dựng phải sinh `.srt` và gói Short (BAI-HOC mục 4).

**DỪNG — chờ điều phối rà.**
