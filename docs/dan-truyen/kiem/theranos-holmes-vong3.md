# Kiểm độc lập vòng 3 — dàn truyện `theranos-holmes` (tập 4)

> Tác tử kiểm độc lập · 01/11/2026 · đối tượng: `docs/dan-truyen/theranos-holmes.md` (141 dòng, bản trong cây làm việc). Không đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài tệp này), `docs/kho-de-tai/kiem/**`, lịch sử git; `docs/kho-de-tai/theranos-holmes.md` chỉ đọc §8 để tra URL. Không sửa dàn truyện, không commit, 0 USD.
> Điểm: **K** khớp · **MH** mạnh hơn nguồn/tầng · **S** sai (số, ngày, trang, chủ thể, tội danh; tự mâu thuẫn trong tệp) · **KKĐ** không kiểm được.

## Kết luận

**Đạt có điều kiện. Còn 5 dòng S (4 lỗi gốc) và 1 dòng MH. Cả 6 dòng sửa được trong tệp, không phải đổi khung tập.** Các điểm kiểm riêng (1), (2), (3), (6), (7) đạt. Điểm (4) còn một lỗi: câu gộp ở nhịp 18 nói "none of the companies… was accused… apart from Holmes and Balwani", trong khi Theranos (một công ty có mặt trong truyện) bị SEC kiện (N2, N3). Điểm (5) đạt. Lỗi tự mâu thuẫn lớn nhất là "bảy câu hỏi = bảy nhóm của cáo trạng" (§0, nhịp 3). Thực tế Kiểm 7 "Danh tiếng" không thuộc nhóm nào của cáo trạng, còn nhóm (F) lại không có câu kiểm riêng.

Nguồn đã mở trong lần kiểm này (01/11/2026):
- N1 tệp repo: SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**. Đã đọc bằng `pdftotext -layout` từng trang: tr. 1–2, 3 (để xác nhận phần Summary), 6–17, 30–33, 52–54.
- N4–N8: API DOJ `press_releases.json?parameters[title]=Theranos`, HTTP 200, 6 kết quả. N4 = 15/06/2018, N5 = 04/01/2022, N7 = 07/07/2022, N6 = 18/11/2022, N8 = 07/12/2022 (theo trường `date`); kết quả còn lại là thông cáo 2022 "Seeks Information From Victims" (không dùng).
- N2, N3: chỉ đọc bản phiên chính đã tải (`scratchpad/src/sec/lr-24069.*`, `2018-41.*`), không tải lại.
- N9: HTTP 200, có "Updated October 20, 2026", 0 kết quả "Holmes"/"Balwani".
- N11: HTTP 200. N12: HTTP 200.
- N14: cả hai số đăng ký trả HTTP 200 JSON. 24965-111 → Bryan, ngày ra dự kiến 02/22/2030; 24966-111 → Lompoc II, 04/21/2033.
- Tất cả dùng curl mặc định, không đổi User-Agent.

## Bảng chấm

| Dòng | Điểm | Nguồn + trang | Ghi chú / sửa |
|---|---|---|---|
| Đầu tệp, quy ước trang, ký hiệu tầng (d. 3–11) | K | N1 tr. 3 ("This summary constitutes no part of the opinion"), tr. 15–16; N7; N8 | Tr. 3–6 đúng là Summary |
| §0-1 Phán quyết Holmes ba phần + Count 9 | K | N1 tr. 15; N5; N6 | Kết án Count 1, 6–8; trắng án Count 2, 10–12; treo Count 3–5; công tố rút Count 9 |
| §0-2 Balwani riêng | K | N1 tr. 9, 15–16; N7; N8 ("former romantic partner") | 2 tội âm mưu + 10 tội wire fraud; 155 tháng |
| §0-3 Không tên | K | N1 tr. 10, 12, 13 có nêu tên | Tệp đúng là không dùng các tên này |
| §0-4 Quy tắc câu kèm (e) | K | — | Quy tắc tự nêu; việc áp dụng chấm ở từng nhịp |
| §0-5 Cơ chế | K | N1 tr. 10, 12 | Tệp không có "null protocol" |
| §0-6 Góc riêng: "bảy nhóm… mỗi nhóm thành một câu hỏi kiểm chứng" | **S** (tự mâu thuẫn) | N1 tr. 10–11 | Hồi 2 không khớp với bảy nhóm (A)–(G). Kiểm 7 "Danh tiếng" (nhịp 10) không phải nhóm của cáo trạng. Nhóm (F) "dùng máy hãng khác" không có Kiểm riêng mà gộp vào 4b dưới Kiểm 1. **Sửa:** chọn một trong hai. (a) Tách 4b thành Kiểm riêng cho (F); chuyển "Danh tiếng" thành bài học của kênh nằm ngoài bảy nhóm, có nhãn K. (b) Giữ cấu trúc hiện tại nhưng đổi câu §0 và thẻ nhịp 3 / H5 thành "six of the indictment's categories + one lesson", và ghi rõ (F) nằm trong Kiểm 1 |
| Logline VI | K | N6 ("induce dozens of investors… hundreds of millions"); N1 tr. 15–16, 54 | — |
| Logline EN | K | N1 tr. 7, 15; N6 | "acquitted her on the patient counts" khớp cách nói của N1 tr. 15 ("acquitted Holmes on the patient-related counts") |
| H1 | K | N1 tr. 7 | Trích đúng nguyên văn; toà gọi là "vision" |
| H2 | K | N1 tr. 7; N3 ("Silicon Valley-based") | — |
| H3 | K | N6 ("was able to induce dozens of investors, many of whom were prominent public figures, to invest hundreds of millions") | Có chủ thể DOJ |
| H4 | K | N1 tr. 15; N6 ("On January 3, 2022") | Ba vế tách bạch |
| H5 | K | N1 tr. 16–17; N4; N2 | Câu kèm đúng. Thẻ "7 claims · 7 checks" chịu cùng lỗi §0-6 |
| Ghi chú §1 (d. 37) | K | — | — |
| Nhịp 0 | K | §1 | — |
| Nhịp 1 | K | N1 tr. 8–9 | Lập công ty 2003; CEO tới 2018; "Holmes's claimed goal"; Edison; Balwani vào 2009, sau là President/COO |
| Nhịp 2 | K | N1 tr. 10; câu kèm N1 tr. 17 | Ra mắt tại Walgreens mùa thu 2013; C-1 cuối 2013, C-2 năm 2014; "not publicly traded" |
| Nhịp 2b | K | N3 (Co-Director Enforcement: "no exemption… non-public, development-stage, or the subject of exuberant media attention") | — |
| Nhịp 3 | **S** (tự mâu thuẫn, cùng gốc §0-6) | N1 tr. 10–11 | Bảy nhóm (A)–(G) dịch đúng. Nhưng câu "→ bảy câu hỏi thẩm định của tập" và "thẻ 7 ô, mỗi ô một câu hỏi" không khớp với Kiểm 1–7 ở Hồi 2. **Sửa:** như §0-6. Câu kèm đúng: N4 chỉ truy tố Holmes, Balwani; N2 chỉ kiện Theranos, Holmes, Balwani |
| Nhịp 4 | K | N1 tr. 10, 11 | 300 xét nghiệm, 12 chạy trên Edison; máy hãng thứ ba, có sửa; nhân viên khai; hai người "dismissed… or shifted blame" |
| Nhịp 4b | K | N1 tr. 12; câu kèm N1 tr. 16; N4; N2 | — |
| Nhịp 5 | K | N1 tr. 12 | "Máy không xét nghiệm mẫu đó" diễn ý "null protocol", không nêu tên giao thức — đạt §0 |
| Nhịp 6 | K | N1 tr. 12 | 0 doanh thu 2012–2013; lỗ 57 và 92 triệu USD; 11/2013 còn 15 triệu, chi tới 2 triệu/tuần; IRS 1.944.948 USD; dự báo lãi 230 triệu cuối 2015 |
| Nhịp 6b | K | N6 ("over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015") | N5 viết "approximately"; câu bám N6 ("nearly" = "gần") |
| Nhịp 7 | K | N1 tr. 14, 8; câu kèm N1 tr. 17 | Holmes "admitted that she personally affixed the logo"; email gửi Walgreens; các hãng không thẩm định, không cho phép |
| Nhịp 8 | **MH** | N1 tr. 12–13 | Lời khai của vị tướng ở N1 là "never installed on a military medevac". "Medevac" không chỉ là trực thăng, nên "trực thăng cứu thương" cụ thể hơn nguồn được dẫn. (Chữ "medevac helicopters" có ở N2, nhưng đó là cáo buộc ◐ của SEC, không phải lời khai.) **Sửa:** VI "chưa từng lắp trên phương tiện tải thương (medevac) của quân đội"; EN giữ "a military medevac". Phần còn lại K: 200 triệu USD "from the Department of Defense"; trích ghi âm đúng nguyên văn; "(phiên Holmes)" đúng theo chú thích 2 |
| Nhịp 9 | K | N1 tr. 13–14; N6 ("from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating") | — |
| Nhịp 10 | K | N1 tr. 7; N6 (đoạn "In its memorandum filed for the sentencing hearing…": "more than $4 billion", "adorning the cover of…") | Câu kèm đúng theo N4/N2. Đối chiếu thêm: N7 cho thấy Balwani là thành viên HĐQT, đã được "Apart from Holmes and Balwani" bao |
| Nhịp 11 | K | N1 tr. 7–8, 11, 30–31 (Report "issued in January 2016", "received by Theranos" đầu 2016), 32 ("voided all patient tests run on the Edison") | — |
| Nhịp 12 | K | N2, N3 (bản phiên chính) | 14/03/2018; "more than $700 million"; 500.000 USD; cấm 10 năm; 18,9 triệu cổ phần; từ bỏ quyền biểu quyết; "subject to court approval"; "neither admitted nor denied"; SEC sẽ kiện Balwani tại toà |
| Nhịp 13 | K | N1 tr. 8 (điều tra hai năm rưỡi), 15; N5/N6 ("initially charged on June 14, 2018"; "On July 28, 2020… superseding indictment") | — |
| Nhịp 14 | K | N1 tr. 15; N5 ("more than $140 million"); N6 (03/01/2022) | Bốn mảnh nói đủ |
| Nhịp 15 | K | N1 tr. 15–16; N7 ("patients who paid for Theranos' blood testing services"); N8 (07/07/2022; 155 tháng; 3 năm) | Chỉ theo bản án Balwani; có câu nối "Holmes was acquitted" |
| Nhịp 16 | K | N1 tr. 15 (120 triệu), 16–17 (135 tháng; 05/2023; 452 / 397 / 54,5 triệu; liên đới); N6 (18/11/2022; Davila; 3 năm; không phạt tiền; trình diện 27/04/2023) | — |
| Nhịp 17 | K | N1 tr. 2, 8, 53–54; N14; N9 | Trạng thái 01/11/2026 khớp lần mở lại |
| Nhịp 18 | **S** (chủ thể) | N2, N3: SEC kiện "Theranos Inc." | Câu gộp nói "None of the companies… mentioned in this story was accused of wrongdoing in these cases — apart from Holmes and Balwani." Theranos là công ty có mặt trong truyện và bị SEC kiện (nhịp 12), nên câu sai. **Sửa:** "Apart from Theranos, Holmes and Balwani, none of the companies, the U.S. military, the investors or the board members mentioned in this story was accused of wrongdoing in these cases." |
| d. 68 (không nhịp MH thiếu nguồn) | K | — | — |
| d. 69 (lời người thật chỉ là trích) | **S** (tự mâu thuẫn, nhẹ) | N1 tr. 7, 9, 13, 53; N3 | Gọi câu ở N1 tr. 7 là "khẩu hiệu", trái với H1 ("**không** gọi là slogan"). **Sửa:** "N1 tr. 7 (câu mở opinion, 'vision')" |
| §3 khuôn 1 tập | K | QUY-TRINH §6 (tập 1 đọc 12:55); `docs/dan-truyen/1inmm-horwitz.md` (~16 phút) | — |
| §3 cú treo | K | N6; N1 tr. 11 | — |
| §3 ghi chú cú treo | K | — | — |
| L1 | K | N1 tr. 10, 53; N3 | — |
| L2 | K | N1 tr. 7, 13, 14; N6 | — |
| L3 | K | N1 tr. 12; N3 (Director, SF Regional Office, trích đúng nguyên văn) | — |
| D (5 dấu hiệu) | K | N1 tr. 12, 13, 13–14, 14 | Trang đúng |
| P | K (phần N10/N13 xem KKĐ) | N11, N12 mở 200 | — |
| Thẻ tổng kết | K | N1 tr. 53 | "sec.gov/tcr" phụ thuộc N10 (KKĐ) |
| d. 90 | K | — | — |
| §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | — |
| §5 (b) | K | N2; N4 (chỉ truy tố Holmes, Balwani) | — |
| §5 (c) | K | — | Rà toàn tệp: không có tên nhà đầu tư, nhân chứng, bệnh nhân, hãng dược hay tạp chí. Chỉ có tên thẩm phán (công chức, N6) và tên trại giam ở ghi chú §7 |
| §5 (d) | K | N1 tr. 7 ("mirage"), 8 ("half-truths and outright lies") | — |
| §5 (e) | K | — | Câu mẫu đúng; câu gộp nhịp 18 xem S ở trên |
| §5 (f) | K | N1 tr. 7, 9, 15; N6 | — |
| §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32 | — |
| §5 phép thử | K | — | Không có trình tự làm theo được |
| §6 đơn giá | K | QUY-TRINH §6 (0,40 USD; 1,5 lượt/khe; 0,4401; 155 từ/phút; 12.230 / 2.005 = 6,1; 825 chưa đo) | "MR-D4 chi 0 USD" xem KKĐ |
| §6 Veo | K | — | 14×0,40×1,0 = 5,60; 18×0,40×1,25 = 9,00; 22×0,40×1,5 = 13,20 |
| §6 TTS | K | — | 2.600×6,1 ≈ 15.860; ×0,4401 ≈ 6.980; +25 % = 8.750; +50 % = 10.500 |
| §6 Music | K | — | 2.475 / 3.300 / 4.125 |
| §6 tổng USD | K | — | — |
| §6 tổng ký tự | K | — | 9.475 ≈ 9.500; 12.050; 14.625 ≈ 14.600 |
| §6 ràng buộc hình | K | — | — |
| §6 trần đề xuất | K | — | 9,00×1,15 = 10,35 ≈ 10,40; 12.050×1,15 ≈ 13.860 ≈ 14.000 |
| §7 N1 | **S** (tự mâu thuẫn, nhẹ) | — | SHA khớp. Danh sách trang đã đọc "1–2, 7–17, 32–33, 53–54" thiếu tr. 31, trong khi nhịp 11 dẫn tr. 31 (và nội dung "January 2016" nằm ở tr. 30). **Sửa:** "1–2, 7–17, 30–33, 53–54" |
| §7 N2 | KKĐ | — | sec.gov không mở theo lệnh. Nội dung khớp bản phiên chính |
| §7 N3 | KKĐ | — | Như trên |
| §7 N4–N8 | K | API DOJ, 200, 6 kết quả | — |
| §7 N9 | K | 200; "Updated October 20, 2026"; 0 kết quả | — |
| §7 N10 | KKĐ | — | sec.gov |
| §7 N11 | K | 200 | — |
| §7 N12 | K | 200 | — |
| §7 N13 | KKĐ | — | adviserinfo.sec.gov |
| §7 N14 | K | 200 JSON | Bryan 02/22/2030; Lompoc II 04/21/2033 |
| §7 N15 | KKĐ | — | sec.gov; tệp không dùng |
| §7 Investor.gov | KKĐ | — | Không mở trong lần kiểm này; tệp đã ghi "không dùng" |
| §8-1 trạng thái | K | — | Phần "certiorari (kho §5)" thuộc kho §5, không đọc theo lệnh |
| §8-2 judgment/SEC | K | N2 ("subject to court approval") | — |
| §8-3 ảnh trang | K | N1 tr. 1, 9, 10, 12–15, 54 | Trang đúng nội dung |
| §8-4 trích nhịp 8 | K | N1 tr. 13 | — |

## Kiểm riêng

1. **Phán quyết Holmes: đạt.** H4, nhịp 14, logline và §0 tách rõ kết án 4 / trắng án 4 / treo 3 / Count 9 bị rút. Không câu nào nói Holmes "defrauded patients". Nhịp 11 (CMS, huỷ kết quả) có chủ thể là Theranos. Nhịp 15 có câu nối bắt buộc.
2. **Balwani: đạt.** Mọi thông tin về ông đều theo N1 tr. 15–16, N7, N8.
3. **Không tên: đạt,** kể cả trong ghi chú.
4. **Câu "không liên quan": còn một lỗi.** Walgreens có câu kèm ở các nhịp 2, 3, 7, 9, 16 và câu gộp ở nhịp 18. Hãng dược ở nhịp 3, 7, 18; quân đội ở nhịp 3, 8, 10, 18; Safeway ở nhịp 16. Nhà đầu tư có câu kèm ở H5, 4b, 12, 10, 18, đúng quy tắc §0. Lỗi duy nhất là câu gộp nhịp 18 bỏ sót Theranos (S).
5. **Luật 8: đạt.** (a) Holmes ở tầng ●. (b) Theranos ở tầng ◐, có trụ ●. (c) Không có tên người chưa kết luận. (d) Từ mạnh của toà chỉ xuất hiện dưới dạng trích. (e) Đạt, trừ câu gộp nhịp 18 ở mục 4. (f) Không dùng quan hệ riêng, lý do tách phiên hay lối sống.
6. **Không hướng dẫn làm theo được: đạt.**
7. **Số trang dẫn: đạt,** trừ danh sách trang đã đọc ở §7 N1 (S nhẹ).

## Không kiểm được

- N2, N3, N10, N13, N15: sec.gov / adviserinfo.sec.gov không mở theo lệnh. Nội dung N2 và N3 đã đối chiếu với bản phiên chính và khớp.
- Investor.gov: không mở.
- "MR-D4 chi 0 USD": số tự khai, không có số đo.
- Certiorari / kho §5: ngoài phạm vi được đọc.

## Tổng đếm

**81 dòng: K 69 · MH 1 · S 5 · KKĐ 6.**
- S: §0-6, nhịp 3, nhịp 18, d. 69, §7 N1. Hai dòng §0-6 và nhịp 3 cùng một gốc, nên có 4 lỗi gốc.
- MH: nhịp 8.
