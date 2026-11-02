# PHƯƠNG ÁN GU — Tập 2 · `tap02-irs-callcenter-patel` (tiêu đề, giọng, bảng màu, thumbnail)

> MR-K23 · 01/11/2026 · NHÁP G1 — **chủ dự án chọn tiêu đề** (QUY-TRINH §1). Giọng và bảng màu **theo tập 1** (lệnh MR-K23), không đề xuất lại. 0 USD (không sinh mẫu giọng, không sinh ảnh).


## 00. MR-S23 · 02/11/2026 — tiêu đề đã duyệt, tiêu đề Short, luật thumbnail

### Tiêu đề tập (ĐÃ DUYỆT G1, NHAT-KY 02/11/2026 10:25)
**T1 "Fake IRS Calls From India: How the Money Got Out"** (48 ký tự, `len()`). Căn cứ tầng như §1. Mô tả video phải có câu KBCB IRS/USCIS ngay dòng đầu (8e: tiêu đề nêu tên cơ quan bị mạo danh, chữ "Fake" + câu không liên quan ở mô tả và ở S003, giây ~20). Kiểm lại trạng thái vụ ngày đăng (HIEN-CHUONG §3 luật 4; NGUON §2).

### Tiêu đề Short (đề xuất — chủ dự án chọn; qua cùng kiểm tầng + luật 8e như tập dài, BAI-HOC mục 3)
| Mã | Tiêu đề | Ký tự | Đoạn Short gợi ý | Kiểm tầng | Luật 8e / 8d |
|---|---|---|---|---|---|
| **SH1 (khuyến nghị)** | `He Funded Fraud Call Centers in India. He Got 20 Years.` | 55 | P00 **S002–S006** (giữ S003 KBCB đọc) + P09–P10 (S051, S054) | ●T "admitted to operating and funding several India-based call centers **from which the fraud schemes were perpetrated**" (N4 đ.6) → "fraud call centers"; ● 20 năm (N5 đ.1–2). Không nói "all", không số tiền. (Rà độc lập MR-S23: bản cũ "He Funded Call Centers in India…" bỏ mất hành vi gian lận, dễ đọc thành bị án vì góp vốn) | Không tên cơ quan → không cần KBCB trong tiêu đề; mô tả Short có câu KBCB IRS/USCIS ở dòng đầu. Không nhãn người (luật 8d) |
| SH2 | `Why Victims Were Told to Pay by Prepaid Card or Wire` | 52 | P06 S034–S035, S041 | ●T "instructed how to provide payment, including by purchasing … reloadable (GPR) cards or wiring money" (N4 đ.5). "Why" trả lời bằng S035 (●T runner rút tiền ngay) — không dùng S037–S039 (hawala ◐) làm câu trả lời | Không tên cơ quan, không tên thương hiệu thẻ (KD). Nếu Short có S034 thì phải có S003 hoặc thẻ KBCB vì lời nhắc "victims were told" trong bối cảnh cuộc gọi mạo danh |
| SH3 | `Hang Up, Then Look the Agency Up Yourself` | 41 | P11 S060–S061, S068 | CHUNG (nguyên tắc kênh) + S060 lời IRS (N9) + S061 HSI (N2 đ.5) | "Agency" chung, không tên; Short có S060 nêu IRS → kèm thẻ KBCB S067 |

Không dùng trong tiêu đề Short: "IRS", "USCIS" (tiêu đề hiện ở bảng tin không kèm câu KBCB — bài học Short 1), tên call center (không chứa được câu ◐), "scam/scammer" (8d), "$65 million" (là cận trên khoảng thiệt hại thừa nhận, không phải số chiếm được), "hundreds of millions" (◐ lúc khởi tố).

### Luật thumbnail riêng tập 2
Tệp dán nguyên vào công cụ ảnh: `docs/tap02-irs-callcenter-patel/phat-hanh/THUMBNAIL-RULES.txt` (khuôn tập 1). Điểm riêng: **không chữ "IRS"/"USCIS" trên thumbnail** (thumbnail hiện ở bảng tin không kèm câu KBCB — cùng lý do tiêu đề Short; chữ gợi ý "THE CALLS WERE FAKE"; nếu chủ dự án muốn áp tiền lệ T1 cho thumbnail thì quyết riêng); không logo/con dấu/huy hiệu IRS, USCIS, DHS hay cơ quan thuế Canada/Úc; không số điện thoại, kể cả số giả; không giao diện cuộc gọi; không mặt, không người già nhận ra được; không bản đồ/cờ/trang phục/biểu tượng tôn giáo gợi định kiến về Ấn Độ; không tên call center; không "SCAMMER".

## 0. Theo tập 1 (đã chọn ở NHAT-KY MR-3 22:48 và 22:58)

| Mục | Lựa chọn | Thi hành ở tập 2 |
|---|---|---|
| **Giọng đọc** | Giọng kênh: Voice Design W4 "LP-M0b-vd-1", ElevenLabs `voice_id` **`kozBJGqBNTqfBBClLNCL`**, TTS `eleven_v4` | Không thử giọng lại. Áp bảng phát âm `LOI.md` (IRS → "I-R-S", FTC, TIGTA → "TIG-tah", HGLOBAL → "H-Global"); **nghe tai** ở M-c các tên: Ahmedabad, Hitesh Madhubhai Patel, Hittner, hawala/hawaladar (bài học MR-4: whisper chép sai "Horwitz") |
| **Bảng màu / chữ** | **B1 "Hồ sơ"**: nền `#F4F1EA`, chữ `#1B1F24`, dòng tiền `#2B7A78`, cảnh báo `#D9480F`, phụ `#8A8F98`; IBM Plex Serif SemiBold / Inter / IBM Plex Mono | Mọi SD/CT/NEN và thẻ tổng kết (`SHOT.md` §3). Nhãn `● CONVICTED · admitted in plea, per DOJ` dùng ô đỏ cam như `● CONVICTED` |
| **Thumbnail** | Chủ dự án tự làm (ChatGPT) theo luật thumbnail của kênh (`docs/tap01-1inmm/phat-hanh/THUMBNAIL-RULES.txt`) | Thêm cho tập này: không logo/con dấu IRS, USCIS, DHS; không số điện thoại (kể cả giả); không mặt người già; không chữ tên call center; không gọi Patel là "scammer". Gợi ý §2 |

## 1. Tiêu đề (≤ 60 ký tự, đếm máy `len()`)

| # | Tiêu đề | Ký tự | Tầng / căn cứ | Ghi chú |
|---|---|---|---|---|
| **T1 (đề xuất)** | Fake IRS Calls From India: How the Money Got Out | 48 | ●T theo DOJ: gọi từ call center ở Ahmedabad, mạo danh IRS (N4 đ.5); tiền chuyển qua runner (N4 đ.5) | "Fake" nói rõ IRS bị mạo danh; câu không liên quan có ngay ở S003 (giây đầu). Hướng câu hỏi của móc câu (S007) |
| T2 | "Pay Now or Be Arrested": Inside a Call Center Ring | 51 | ●T: doạ bắt nếu không trả (N4 đ.5); "immediately" (N1 tr. 3, ◐; N3 đ.8, ●N) | **Không tên cơ quan** trong tiêu đề → tránh hẳn câu hỏi luật 8e. Ngoặc kép là tóm tắt lời doạ, không phải trích lời gọi thật — nếu chủ dự án thấy dễ hiểu nhầm là trích, dùng T1 |
| T3 | Gift Cards, Wires, Runners: Inside the Fake IRS Calls | 53 | Thẻ quà tặng: N3 đ.14 (●N, lời thừa nhận của các bị cáo ở Mỹ); chuyển tiền, runner: N4 đ.5 (●T) | Hướng bài học (L2). Không tên thương hiệu thẻ |

Không dùng trong tiêu đề: "HGLOBAL" (tiêu đề không chứa được câu ◐ bắt buộc); "scammer/con artist" (lời U.S. Attorney ở N5 đ.4 — luật 8d); "$65 million" (khoản thiệt hại thừa nhận là **khoảng** "> 25 triệu và < 65 triệu", không phải số chiếm được); "hundreds of millions" (cáo buộc lúc khởi tố, ◐).

## 2. Thumbnail (gợi ý cho chủ dự án; đồ hoạ phẳng, không mặt, không logo)

| # | Ý | Bố cục | Chữ |
|---|---|---|---|
| TN1 (đi với T1/T3) | "Điện thoại → thẻ trắng" | Điện thoại phẳng màn hình chữ "UNKNOWN" bên trái; mũi tên đỏ cam sang chồng **thẻ nhựa trắng trơn** bên phải; bản đồ mờ India → USA nền | "FAKE IRS CALLS" (nhãn đỏ) |
| TN2 (đi với T2) | "Lời doạ" | Bong bóng chữ lớn "PAY NOW OR BE ARRESTED" (chữ in, không giao diện ứng dụng) trên nền xanh đêm; dấu ✗ đỏ cam | "IT WASN'T THE IRS" |
