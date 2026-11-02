# Kiểm độc lập dàn truyện `theranos-holmes` (tập 4) — vòng 5

> Tác tử kiểm độc lập · 01/11/2026 · đối tượng: `docs/dan-truyen/theranos-holmes.md` (141 dòng, bản trên đĩa lúc kiểm).
> Căn cứ chấm: `docs/HIEN-CHUONG.md` §3 (luật 1–8), §4, §5; `docs/QUY-TRINH-TAP.md` §6; `docs/kho-de-tai/theranos-holmes.md`.
> Không đọc: `reports/**`, `docs/dan-truyen/kiem/**` (các vòng trước), `docs/kho-de-tai/kiem/**`, lịch sử git.
> Điểm: **K** khớp · **MH** mạnh hơn nguồn/tầng · **S** sai (số, ngày, trang, chủ thể, tội danh; tự mâu thuẫn trong tệp; trích gán sai nguồn) · **KKĐ** không kiểm được.

## Nguồn đã mở trong vòng này
| Mã | Cách mở | Kết quả |
|---|---|---|
| N1 | `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf`; `sha256sum` = `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**; `pdfinfo` 54 trang; `pdftotext -layout -f P -l P` từng trang 1–54; đọc tr. 1–2, 7–17, 30–33, 53–54 | Số trang in = số trang PDF (đã đối chiếu tr. 2, 7–17, 30–33, 53–54). Dàn truyện không dẫn tr. 3–6 làm nguồn sự việc |
| N2, N3 | Bản phiên chính tải sẵn trong scratchpad (`src/sec/lr-24069.html`, `2018-41.html` và bản .txt đi kèm); đối chiếu cụm chính có trong cả .html | Đọc được; **không** tự tải sec.gov |
| N4–N8 | `curl` API `justice.gov/api/v1/press_releases.json?parameters[title]=Theranos&pagesize=50` → HTTP 200, 6 kết quả (5 thông cáo kho §8 + "U.S. Government Seeks Information From Victims…") | Đọc toàn văn body N4 (15/06/2018), N5 (04/01/2022), N6 (18/11/2022), N7 (07/07/2022), N8 (07/12/2022) |
| N9 | `curl` mặc định → 200; "Updated October 20, 2026"; 0 lần "Holmes", 0 lần "Balwani" | Khớp dàn truyện |
| N11 | `curl` mặc định → 200 (title "BrokerCheck - Find a broker…") | Mở được |
| N12 | `curl` mặc định → 200 (title "ReportFraud.ftc.gov") | Mở được |
| N14 | `curl` mặc định JSON BOP 24965-111 / 24966-111 → 200, `Captcha:false` | Holmes: projRelDate 02/22/2030; Balwani: 04/21/2033 — khớp |
| N10, N13, N15, investor.gov | sec.gov / adviserinfo.sec.gov / investor.gov — **không mở theo lệnh** | KKĐ |

## Kết luận
- **0 MH, 3 S, 6 KKĐ**, còn lại K. Không có câu nào nâng tầng; không có lỗi số, ngày, trang hay tội danh trong các câu sự việc.
- (1) Phán quyết Holmes tách bạch đúng N1 tr. 15 và N5/N6/N7: kết án 4 (Count 1, 6–8), trắng án 4 (Count 2, 10–12), treo 3 (Counts 3–5), Count 9 rút. Không câu nào nói Holmes bị kết án lừa bệnh nhân. **Một lỗi S** ở câu nối nhịp 15 ("the four patient counts" đứng ngay sau bốn tội bệnh nhân Counts 9–12 của Balwani → trỏ sai bộ tội; Holmes không được trắng án Count 9, mà Count 9 bị rút).
- (2) Balwani chỉ theo bản án của ông (N1 tr. 16; N7; N8) — đạt.
- (3) Không tên bệnh nhân/nhà đầu tư/nhân chứng — đạt (tên trong N1 tr. 10, 12, 13, 14, 32 đều bị loại).
- (4) Câu không liên quan: đúng chủ thể, có nguồn (N1 tr. 8, 16, 17; N2; N4) ở mọi đoạn nêu Walgreens, Safeway, hãng dược, quân đội, nhà đầu tư, HĐQT/nhân vật nổi tiếng — đạt (hai gợi ý không tính điểm ở dưới).
- (5) Luật 8 (a)–(f) đạt. (6) Không có nội dung làm theo được. (7) Mọi số trang N1 được dẫn đều đúng.
- (8) Cấu trúc "bảy câu kiểm": nhịp 3–10, §0, H5 nhất quán (6 câu từ nhóm cáo trạng + 1 câu của kênh); **hai lỗi S** ở §3 và §6 vẫn gọi là "bảy lời hứa" / "bảy thẻ 'lời hứa…'", trái với chính quy ước của tệp.

## Bảng chấm

| # | Dòng | Điểm | Nguồn + trang | Ghi chú / sửa |
|---|---|---|---|---|
| 1 | Đầu tệp: quy ước trang N1, ký hiệu tầng (Holmes chỉ 4 tội nhà đầu tư; Balwani 12 tội theo bản án riêng) | K | N1 tr. 3 ("Summary" không thuộc opinion), 15, 16; N7; N8 | — |
| 2 | §0 b1 — bốn mảnh phán quyết Holmes; Counts 3–5 sau xử chưa có nguồn | K | N1 tr. 15; N5; N6; N7 | Đúng cả 4 vế |
| 3 | §0 b2 — Balwani: phiên riêng, 12/12 tội, 155 tháng; không dùng lý do tách phiên/quan hệ riêng | K | N1 tr. 9, 15, 16; N7; N8 ("former romantic partner") | — |
| 4 | §0 b3 — không tên bệnh nhân/nhà đầu tư/nhân viên/nhân chứng | K | N1 tr. 10, 12, 13 (có tên) | — |
| 5 | §0 b4 — quy tắc câu kèm (Walgreens, Safeway, hãng dược, quân đội: mỗi đoạn; nhà đầu tư: lần đầu mỗi hồi + nhịp 10, 18) | K | — | Gợi ý (không tính): xem mục "Gợi ý" về nhịp 2 |
| 6 | §0 b5 — cơ chế ở mức "ran samples on other companies' machines"; không "null protocol" | K | N1 tr. 10–12 | Toàn tệp không có chữ "null protocol" ngoài câu cấm |
| 7 | §0 b6 — bảy câu kiểm = 6 từ nhóm (A)–(G) (A+F gộp) + 1 câu kênh | K | N1 tr. 10–11 | Khớp phân loại (A)–(G) |
| 8 | Logline VI | K | N1 tr. 7, 15, 16, 54; N6 ("dozens of investors… hundreds of millions") | — |
| 9 | Logline EN | K | N1 tr. 7, 15; N6 | Gợi ý: "the four patient counts" — cáo trạng có 5 tội bệnh nhân (Count 2, 9–12, N1 tr. 8); bồi thẩm chỉ xét 4 vì Count 9 bị rút. Nên viết "on four patient counts" (bỏ "the"), như H4 |
| 10 | H1 — chữ trích "[O]ne tiny drop changes everything." | K | N1 tr. 7 | Đúng nguyên văn, đúng ngữ cảnh "vision" |
| 11 | H2 | K | N1 tr. 7; N3 ("Silicon Valley-based") | — |
| 12 | H3 (●D) | K | N6 ("Evidence showed that Holmes… was able to induce dozens of investors… hundreds of millions of dollars") | Có chủ thể DOJ |
| 13 | H4 — tháng 01/2022: 4 tội (1 âm mưu + 3 wire fraud); trắng án 4; treo 3 | K | N1 tr. 15; N5; N6 ("On January 3, 2022") | — |
| 14 | H5 + câu kèm nhà đầu tư ("twelve of them as victims") | K | N1 tr. 16 (12 nhà đầu tư là "victims" theo MVRA); N4 (chỉ Holmes, Balwani bị truy tố); N2 | — |
| 15 | Ghi chú sau móc câu (8d; H4 không rút gọn) | K | — | — |
| 16 | Nhịp 0 | K | §1 | — |
| 17 | Nhịp 1 — lập 2003, CEO tới 2018, "claimed goal", Edison, Balwani 2009 → President/COO | K | N1 tr. 8–9 | Không nhắc quan hệ riêng |
| 18 | Nhịp 2 — ra mắt tại Walgreens thu 2013; C-1 cuối 2013; C-2 2014; không giao dịch công khai | K | N1 tr. 10 | — |
| 19 | Nhịp 2 câu kèm Walgreens | K | N1 tr. 8 (chỉ Holmes, Balwani bị truy tố), 17 ($54,5 triệu cho "two other victims, Safeway and Walgreens"); N4; N2 | — |
| 20 | Nhịp 2b — câu SEC "no exemption… non-public, development-stage, or the subject of exuberant media attention" | K | N3 (Steven Peikin, Co-Director, Enforcement Division) | "an SEC enforcement official said in 2018" đúng chức danh |
| 21 | Nhịp 3 — bảy nhóm (A)–(G) theo cáo trạng; tầng ◐ | K | N1 tr. 10–11 ("The Indictment alleged…") | Tên nhóm khớp |
| 22 | Nhịp 3 câu gộp | K | N1 tr. 8; N4; N2 | — |
| 23 | Nhịp 4 — 300 xét nghiệm / 12 trên Edison; "general chemistry tests" trên máy hãng thứ ba, một số bị sửa; nhân viên khai QC trượt, hai người gạt đi/đổ lỗi | K | N1 tr. 10, 11 | — |
| 24 | Nhịp 4b — nhà đầu tư khai bị khiến tin chỉ chạy trên máy Theranos | K | N1 tr. 12 | — |
| 25 | Nhịp 4b câu kèm nhà đầu tư | K | N1 tr. 16; N4 | — |
| 26 | Nhịp 5 — trình diễn VIP | K | N1 tr. 12 | "máy không xét nghiệm mẫu đó" diễn đúng ý mà không lộ thuật ngữ |
| 27 | Nhịp 6 — 0 doanh thu 2012–2013; lỗ $57/$92 triệu; 11/2013 còn $15 triệu, chi tới $2 triệu/tuần; IRS 2015 $1.944.948; dự báo lãi $230 triệu cuối 2015 | K | N1 tr. 12 | Tách đúng lời khai kiểm soát viên và phần toà thuật tiếp |
| 28 | Nhịp 6b (●D) — >$100 triệu 2014, gần $1 tỷ 2015 | K | N6 ("…projected to generate over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015"); N5 | — |
| 29 | Nhịp 7 — Holmes thừa nhận tự gắn logo; email gửi Walgreens; đại diện hãng khai không thẩm định, không cho phép; báo cáo đưa nhà đầu tư | K | N1 tr. 14; tr. 8 | — |
| 30 | Nhịp 7 câu kèm hãng dược + Walgreens | K | N1 tr. 14, 17; N4; N2 | Hãng dược không nêu tên |
| 31 | Nhịp 8 — $200 triệu "từ Bộ Quốc phòng"; vị tướng khai (field, medevac, battlefield); trích cuộc gọi 12/2013 | K | N1 tr. 12–13 | Trích đúng nguyên văn; bản ghi âm chỉ ở phiên Holmes (tr. 13 chú thích 2) |
| 32 | Nhịp 8 câu kèm quân đội | K | N4; N2 | — |
| 33 | Nhịp 9 — đại diện Walgreens khai thu hẹp, pilot không như kỳ vọng; ●D vài chục → 900 | K | N1 tr. 13–14; N6 ("from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating") | — |
| 34 | Nhịp 9 câu kèm Walgreens | K | N1 tr. 8, 17; N4; N2 | — |
| 35 | Nhịp 10 — "captivated"; quan hệ với công ty lớn, nhà đầu tư, nhân vật nổi tiếng, sĩ quan cao cấp; ●D cổ phần >$4 tỷ cuối 2014, bìa tạp chí | K | N1 tr. 7; N6 ("In its memorandum filed for the sentencing hearing…") | Gợi ý (không tính): xem "Gợi ý" |
| 36 | Nhịp 10 câu kèm ("Apart from Holmes and Balwani…") | K | N4 (chỉ hai người bị truy tố); N2 (SEC kiện Theranos, Holmes, Balwani) | Theranos không thuộc các nhóm được liệt kê nên câu đúng |
| 37 | Nhịp 11 — báo chí cuối 2015; CMS thanh tra không báo trước cuối 2015; báo cáo nhận đầu 2016; "immediate jeopardy"; nhân chứng khai huỷ toàn bộ kết quả trên Edison | K | N1 tr. 7–8, 11, 30 ("issued in January 2016"), 31, 32 | Gợi ý: N1 tr. 32 không nêu thời điểm huỷ; chữ "sau đó" không sai với nguồn nhưng nên bỏ hoặc giữ mơ hồ ("A witness testified that Theranos voided…") |
| 38 | Nhịp 12 — SEC 14/03/2018; >$700 triệu; dàn xếp không thừa nhận; $500.000 "agreed to pay"; cấm 10 năm; 18,9 triệu cổ phần; từ bỏ quyền biểu quyết; chờ toà chấp thuận; SEC theo kiện Balwani | K | N2; N3 | ◐ đúng; không "court ordered" |
| 39 | Nhịp 12 câu kèm nhà đầu tư | K | N1 tr. 16; N4 | — |
| 40 | Nhịp 13 — truy tố 06/2018 sau điều tra 2,5 năm; cáo trạng thay thế 28/07/2020; xử riêng: Holmes cuối 2021, Balwani đầu 2022, mỗi phiên gần 4 tháng | K | N1 tr. 8, 15; N4; N5 ("On July 28, 2020…"); N6 | Không lý do tách phiên |
| 41 | Nhịp 14 — 03/01/2022, bốn mảnh; Counts 6–8 chuyển khoản >$140 triệu | K | N1 tr. 15; N5; N6 | Đạt kiểm riêng (1) |
| 42 | Nhịp 15 — Balwani 07/07/2022, 12/12 tội (2 âm mưu + 6 nhà đầu tư + 4 bệnh nhân); bệnh nhân khai kết quả sai, bằng chứng gắn Balwani; 07/12/2022: 155 tháng, 3 năm giám sát | K | N1 tr. 15–16; N7; N8 | — |
| 43 | Nhịp 15 câu nối bắt buộc "Holmes was acquitted of the four patient counts." | **S** | N1 tr. 15 (Holmes: trắng án Count 2 và Counts 10–12; Count 9 bị rút); tr. 16 (Balwani: "patient wire fraud (Counts 9–12)") | Câu đứng ngay sau "4 tội lừa bệnh nhân" của Balwani (Counts 9–12) nên "the four patient counts" trỏ vào Counts 9–12. Holmes **không** được trắng án Count 9 (bị rút) và được trắng án tội âm mưu Count 2, không nằm trong bốn tội đó. **Sửa:** "At her separate trial, Holmes was acquitted of the patient conspiracy count and three patient wire-fraud counts; one other patient count was dismissed." |
| 44 | Nhịp 16 — 18/11/2022 Davila: 135 tháng, 3 năm giám sát, không phạt tiền; thiệt hại $120 triệu; lệnh trình diện 27/04/2023; 05/2023 bồi hoàn liên đới $452 triệu ($397 triệu/12 nhà đầu tư; $54,5 triệu Safeway và Walgreens) | K | N1 tr. 15–17; N6 ("ordered to surrender on April 27, 2023"; "No fine was assessed") | — |
| 45 | Nhịp 16 câu kèm Safeway và Walgreens | K | N1 tr. 8, 17; N4; N2 | — |
| 46 | Nhịp 17 — 24/02/2025 giữ nguyên; toàn bộ lệnh bồi hoàn; nhà đầu tư không bán được; trích "there was never a legitimate opportunity…" | K | N1 tr. 2, 8 ("We affirm."), 53, 54 ("affirm the district court's restitution order in its entirety") | Trích đúng nguyên văn; "one investor who testified at both trials" |
| 47 | Nhịp 17 trạng thái — BOP 22/02/2030 và 21/04/2033; không có tên trên trang ân xá | K | N14 (mở lại, 200); N9 (mở lại, 200, 0 kết quả) | — |
| 48 | Nhịp 18 — bài học, dấu hiệu, nguyên tắc, nơi kiểm/báo cáo | K | §4 | — |
| 49 | Nhịp 18 câu gộp ("Apart from Theranos, Holmes and Balwani…") | K | N1 tr. 8, 16–17; N4; N2 | Đúng chủ thể (Theranos bị SEC kiện nên được loại trừ) |
| 50 | Dòng 68–69 — chỉ H1, nhịp 5 là MH; lời người thật chỉ là chữ trích (tr. 7, 9, 13, 53; N3) | K | N1 tr. 7, 9, 13, 53; N3 | — |
| 51 | §3 — đề xuất 1 tập ~17 phút; xét 2 phần | **S** | Chính tệp: §0 b6, nhịp 3, nhịp 10, H5 | Lập luận 0b hợp lệ, so với tập 1 ("~16 phút", `docs/dan-truyen/1inmm-horwitz.md` dòng 57) và lời thật 12:55 (QUY-TRINH §6) khớp. **Lỗi:** "chỉ có nghĩa khi đã xem **bảy lời hứa** ở P1" mâu thuẫn quy ước của tệp: chỉ 6 câu dựng từ nhóm lời khai sai của cáo trạng, còn Kiểm 7 là câu của kênh, không phải lời hứa (H5 cấm ghi "7 claims"). **Sửa:** "…khi đã xem bảy câu kiểm (sáu nhóm lời hứa theo cáo trạng + một câu của kênh) ở P1" |
| 52 | Cú treo câu 1 (●D) — ">$4 tỷ cuối 2014, prosecutors said" | K | N6 | — |
| 53 | Cú treo câu 2 (●C) — thanh tra liên bang không báo trước cuối 2015 | K | N1 tr. 11 | — |
| 54 | L1 | K | N1 tr. 10, 53; N3 | — |
| 55 | L2 | K | N1 tr. 7, 13, 14; N6 | — |
| 56 | L3 — trích "Innovators who seek…" | K | N1 tr. 12; N3 (Jina Choi, Director, SF Regional Office) | Trích đúng nguyên văn, đúng "quan chức SEC năm 2018" |
| 57 | D — 5 dấu hiệu | K | N1 tr. 12, 13 (cả tr. 12–13 cho $200 triệu), 13–14, 14 | Mỗi dấu hiệu gắn đúng nhịp |
| 58 | P — nguyên tắc chung + nơi kiểm/báo cáo | K | N11, N12 (mở được); N10, N13: KKĐ (sec.gov) | Không khuyên sản phẩm/tỷ trọng |
| 59 | Thẻ tổng kết | K | N1 tr. 53; §4 | "sec.gov/tcr" phụ thuộc N10 → phần đó KKĐ (sec.gov không mở theo lệnh) |
| 60 | §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | — |
| 61 | §5 (b) | K | N2; N4 | — |
| 62 | §5 (c) | K | — | — |
| 63 | §5 (d) — "mirage", "half-truths and outright lies" chỉ làm chữ trích | K | N1 tr. 7 ("mirage"), 8 ("half-truths and outright lies") | — |
| 64 | §5 (e) — câu mẫu | K | N1 tr. 8, 14, 16, 17; N2; N4 | — |
| 65 | §5 (f) | K | N1 tr. 7, 9, 15; N6; N8 | — |
| 66 | §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32; N8 | — |
| 67 | §5 phép thử "làm theo được ngay?" | K | — | Đạt kiểm riêng (6) |
| 68 | §6 ghi chú đơn giá | K | QUY-TRINH §6 (0,40 USD/clip 8 s; 1,5 lượt/khe, khe dễ ~1,0; 0,4401; 155 từ/phút; 12.230/2.005 = 6,10; Music ~825 chưa đo; NB2.1 không khoá) | — |
| 69 | §6 bảng ước chi | K | Tính lại: 14×0,40×1,0 = 5,60; 18×0,40×1,25 = 9,00; 22×0,40×1,5 = 13,20; 2.600×6,1 ≈ 15.900 × 0,4401 ≈ 7.000 → 8.750 / 10.500; 3/4/5 × 825 = 2.475/3.300/4.125; tổng 9.475 / 12.050 / 14.625 | Số học khớp |
| 70 | §6 đoạn "Vì sao số khe…" | **S** | Chính tệp: §0 b6, nhịp 10, H5 | "Hồi 2 là **bảy thẻ 'lời hứa / hồ sơ / câu hỏi'**" gán ô "lời hứa" cho cả Kiểm 7, trong khi nhịp 10 ghi rõ Kiểm 7 là câu của kênh, không phải nhóm của cáo trạng. **Sửa:** "Hồi 2 là bảy thẻ câu kiểm (sáu thẻ 'lời hứa / hồ sơ / câu hỏi' + một thẻ câu của kênh)" |
| 71 | §6 đề xuất trần (≈ 10,40 USD; ≈ 14.000 ký tự) | K | 9,00 × 1,15 = 10,35; 12.050 × 1,15 ≈ 13.858 | Làm tròn lên hợp lý |
| 72 | §7 N1 | K | sha256sum, pdfinfo | — |
| 73 | §7 N2 (200, UA khai báo) | KKĐ | — | sec.gov không mở theo lệnh; nội dung bản phiên chính đã đối chiếu ở dòng 38 |
| 74 | §7 N3 | KKĐ | — | Như trên; nội dung đã đối chiếu ở dòng 20, 38, 56 |
| 75 | §7 N4–N8 (API, 6 kết quả) | K | API DOJ, 200, 6 kết quả | Gợi ý: cột "Dùng cho" thiếu H4, H5, nhịp 2–3, 7–8, 12 (câu kèm N4), 17 |
| 76 | §7 N9 | K | curl 200, "Updated October 20, 2026", 0 kết quả | — |
| 77 | §7 N10 | KKĐ | — | sec.gov không mở theo lệnh |
| 78 | §7 N11 | K | curl 200 | — |
| 79 | §7 N12 | K | curl 200 | — |
| 80 | §7 N13 | KKĐ | — | adviserinfo.sec.gov không mở theo lệnh |
| 81 | §7 N14 | K | curl JSON 200, khớp ngày | — |
| 82 | §7 N15 (không dùng) | KKĐ | — | sec.gov không mở theo lệnh; không dùng cho nhịp nào |
| 83 | §7 investor.gov ("chưa mở được", không dùng) | KKĐ | — | Không mở theo lệnh; tệp không dùng |
| 84 | §8 b1 — kiểm lại trạng thái | K | — | — |
| 85 | §8 b2 — "agreed to settle", không "court ordered" | K | N2; N3 ("subject to court approval") | — |
| 86 | §8 b3 — chỉ dùng ảnh N1 tr. 1, 15 (đoạn phán quyết), 54; tránh tr. 9, 10, 12–14, phần trên tr. 15 | K | N1 tr. 9, 10, 12–15, 54 | Lưu ý: đoạn phán quyết tr. 15 nằm **ngay dưới** đoạn lý do tách phiên → crop sát |
| 87 | §8 b4 — trích nhịp 8 đúng nguyên văn | K | N1 tr. 13 | — |

## Kiểm riêng (1)–(8)
| # | Mục | Kết quả |
|---|---|---|
| 1 | Phán quyết Holmes tách bạch | Đạt ở §0, logline, H4, nhịp 14, §5(a). **S** câu nối nhịp 15 (dòng 43) |
| 2 | Balwani chỉ theo bản án của ông | Đạt |
| 3 | Không tên bệnh nhân/nhà đầu tư/nhân chứng | Đạt |
| 4 | Câu không liên quan | Đạt; hai gợi ý (nhịp 2, nhịp 10) không tính điểm |
| 5 | Luật 8 (a)–(f) | Đạt |
| 6 | Không hướng dẫn làm theo được | Đạt |
| 7 | Số trang dẫn | Đúng hết |
| 8 | Cấu trúc "bảy câu kiểm" | Nhịp 3–10, §0, H5 nhất quán; **S** ở §3 (dòng 51) và §6 (dòng 70) |

## Gợi ý văn phong / phòng ngừa (không tính điểm)
- **Nhịp 2:** nếu câu EN nói "raised money from investors" thì đó là lần nêu nhà đầu tư đầu tiên của Hồi 1 (trước nhịp 3). Hoặc đưa câu kèm nhà đầu tư lên nhịp 2, hoặc viết nhịp 2 không có chữ "investors" ("Theranos sold new shares").
- **Nhịp 10:** sự việc có nêu "major companies"; câu kèm chỉ liệt kê "investors, board members, military officers or prominent backers". Có thể thêm "companies" cho trọn.
- **Logline EN, H4:** giữ "on four patient counts" (không mạo từ "the"), như dòng 9.
- **Nhịp 11:** bỏ "sau đó" ở vế huỷ kết quả vì N1 tr. 32 không nêu thời điểm.
- Câu kèm ở nhịp 2 dùng "in these cases" khi vụ án chưa được giới thiệu; kịch bản có thể viết "in the cases that followed".

## Không kiểm được
- N2, N3 (phần "đã mở 200, UA khai báo"), N10, N13, N15: sec.gov không mở theo lệnh. Nội dung N2, N3 đã đối chiếu với bản phiên chính tải sẵn.
- investor.gov: không mở; tệp đã ghi không dùng.
- Không mở trong vòng này (tệp cũng không dùng làm nguồn): judgment N.D. Cal., lệnh chấp thuận dàn xếp SEC, kết cục SEC v. Balwani, số phận Counts 3–5, certiorari. Tệp đã ghi đúng là chưa có nguồn.

## Tổng đếm
| Điểm | Số dòng |
|---|---|
| K | 78 |
| MH | 0 |
| S | 3 (dòng 43, 51, 70) |
| KKĐ | 6 (dòng 73, 74, 77, 80, 82, 83) |
| **Tổng** | **87** |
