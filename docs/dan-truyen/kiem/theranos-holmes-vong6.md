# Kiểm độc lập vòng 6 — dàn truyện `theranos-holmes` (tập 4)

> Đối tượng: `docs/dan-truyen/theranos-holmes.md` (141 dòng, bản trong cây làm việc ngày kiểm). Ngày kiểm: 01–02/11/2026.
> Căn cứ: `docs/HIEN-CHUONG.md` §3 (luật 1–8), §4, §5; `docs/QUY-TRINH-TAP.md` §6. Không đọc `reports/**`, `docs/dan-truyen/kiem/**` (trừ tệp này), lịch sử git, `docs/kho-de-tai/kiem/**`. Có đọc `docs/kho-de-tai/theranos-holmes.md` (bảng mã nguồn) và `docs/NHAT-KY.md` (chỉ để kiểm hai câu dẫn MR-4, K5).
> Điểm: **K** khớp · **MH** mạnh hơn nguồn/tầng · **S** sai (số, ngày, trang, chủ thể, tội danh; tự mâu thuẫn; trích gán sai; câu có thể bị hiểu sai chủ thể/tội) · **KKĐ** không kiểm được theo lệnh.

## Nguồn đã mở trong vòng này

| Mã | Cách mở | Kết quả |
|---|---|---|
| N1 | `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf`; `pdftotext -layout -f P -l P` từng trang 1–54 | SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**; đọc tr. 1–2, 7–17, 30–33, 52–54. Số trang in = số trang PDF (xác nhận). |
| N4–N8 | API DOJ `press_releases.json?parameters[title]=Theranos&pagesize=50`, curl mặc định | HTTP 200, 6 kết quả: N4 (15/06/2018), N5 (04/01/2022), N7 (07/07/2022), thông cáo 18/08/2022 (không dùng), N6 (18/11/2022), N8 (07/12/2022) |
| N2, N3 | Bản phiên chính trong scratchpad `src/sec/lr-24069.*`, `2018-41.*` (không tự tải sec.gov) | Đọc toàn văn |
| N9 | curl mặc định | HTTP 200; "Updated October 20, 2026"; 0 lần "Holmes"/"Balwani" |
| N11 | curl mặc định | HTTP 200, trang BrokerCheck |
| N12 | curl mặc định | HTTP 200, trang ReportFraud.ftc.gov |
| N14 | curl mặc định, JSON công khai BOP, 24965-111 và 24966-111 | HTTP 200, `"Captcha":false`; Holmes — Bryan, projRelDate 02/22/2030; Balwani — Lompoc II, 04/21/2033 |
| N10, N13, N15, investor.gov | — | Không mở (sec.gov / trang SEC không mở theo lệnh) |

Không gọi API trả tiền; không đổi User-Agent; không gặp 403/CAPTCHA.

## Kết luận

Dàn truyện **gần đạt**: mọi số, ngày, số trang và tội danh đối chiếu được đều khớp nguồn; phán quyết của Holmes được tách đúng bốn mảnh ở nhịp 14 và câu nối nhịp 15; Balwani chỉ nói theo bản án của ông; không tên bệnh nhân, nhà đầu tư, nhân chứng; không có nội dung làm theo được; ước chi khớp đơn giá đo thật QUY-TRINH §6 và cộng đúng.
Còn **3 lỗi S, 0 MH**:
1. **Câu kèm nhịp 10** và **mẫu tương ứng ở §5 (e)**: "Apart from Holmes and Balwani, none of the companies … was accused of wrongdoing in these cases" — sai chủ thể: Theranos là công ty và **bị SEC cáo buộc** (N2, N3), chính tệp xếp Theranos ở ◐ (§5 (b), nhịp 12) và câu gộp nhịp 18 đã viết đúng "Apart from Theranos, Holmes and Balwani…". Tính 2 dòng S.
2. **§3** viết "bảy câu kiểm (sáu nhóm lời hứa theo cáo trạng + một câu của kênh)" — mâu thuẫn với §0 và nhịp 3 (cáo trạng có **bảy** nhóm; sáu câu kiểm được dựng từ bảy nhóm, (A)+(F) gộp). Cấu trúc "bảy câu kiểm" ở mọi mục khác nhất quán.

Sau khi sửa 3 dòng này, dàn truyện đủ điều kiện về nguồn để chuyển chủ dự án duyệt (các dòng KKĐ chỉ phụ thuộc trang sec.gov đã mở ở phiên chính).

## Bảng chấm

| Dòng (tệp) | Mục | Điểm | Nguồn + trang | Ghi chú / sửa |
|---|---|---|---|---|
| 3–11 | Đầu tệp, quy ước trang, ký hiệu tầng | K | N1 tr. 3–6 (Summary), tr. 15–16; N7; N8 | Quy ước số trang đúng; Holmes chỉ ● 4 tội (Count 1, 6–8), Balwani 12 tội đúng |
| 14 | §0 — bốn mảnh phán quyết Holmes | K | N1 tr. 15; N5 | Kết án Count 1, 6–8; trắng án Count 2, 10–12; treo 3–5 (C-1); Count 9 bị rút — khớp |
| 15 | §0 — Balwani theo bản án riêng | K | N1 tr. 15–16; N7; N8 | 2 âm mưu + 10 đường dây, 155 tháng; lý do tách phiên (tr. 15) và quan hệ (tr. 9; N8 "former romantic partner") đúng là có trong nguồn và bị loại |
| 16 | §0 — không tên | K | N1 tr. 10, 12, 13 | Các trang này nêu tên nhà đầu tư/nhân chứng — đúng |
| 17 | §0 — quy tắc câu không liên quan | K | — | Quy tắc nhất quán với bảng nhịp (xem dòng 47–66) |
| 18 | §0 — giới hạn cơ chế | K | N1 tr. 10–12 | Không dùng "null protocol"/cách sửa máy trong lời |
| 19 | §0 — bảy câu kiểm (6 từ bảy nhóm + 1 của kênh) | K | N1 tr. 10–11 | Bảy nhóm (A)–(G) khớp nguyên văn opinion |
| 23 | Logline VI | K | N6; N1 tr. 7, 15–16, 54 | "theo DOJ … hàng chục nhà đầu tư … hàng trăm triệu USD" = N6; 4/4/3 đúng. Không nêu Count 9 — chấp nhận (không phải phán quyết bồi thẩm; nhịp 14 nói đủ) |
| 25 | Logline EN | K | N1 tr. 15, 17; N6 | "hundreds of millions" có trụ ● (bồi hoàn 397 triệu USD cho 12 nhà đầu tư, tr. 17) |
| 31 | H1 | K | N1 tr. 7 | Trích đúng "[O]ne tiny drop changes everything."; toà gọi là "vision" — đúng |
| 32 | H2 | K | N1 tr. 7; N3 | Gần nguyên văn tr. 7; "Silicon Valley-based" ở N3 |
| 33 | H3 | K | N6 ("was able to induce dozens of investors…") | ●D, có chủ thể DOJ |
| 34 | H4 | K | N1 tr. 15; N5; N6 ("On January 3, 2022…") | 1 âm mưu + 3 đường dây; trắng án 4; treo 3 — đúng |
| 35 | H5 + câu kèm nhà đầu tư | K | N1 tr. 16 ("twelve investors … were 'victims'"); N4 (chỉ Holmes, Balwani bị truy tố) | |
| 37 | Ghi chú §1 | K | — | |
| 45 | Nhịp 0 | K | §1 | |
| 46 | Nhịp 1 | K | N1 tr. 8–9 | 2003; CEO tới 2018; "Holmes's claimed goal"; Edison; Balwani vào 2009, President và COO — khớp |
| 47 | Nhịp 2 + câu kèm Walgreens, nhà đầu tư | K | N1 tr. 10 (mùa thu 2013, C-1 cuối 2013, C-2 2014, "not publicly traded"); tr. 17 (Walgreens nạn nhân được bồi hoàn); tr. 16 | |
| 48 | Nhịp 2b | K | N3 (Peikin, Co-Director Enforcement: "…no exemption … non-public, development-stage, or the subject of exuberant media attention.") | Chủ thể "an SEC enforcement official said in 2018" đúng |
| 49 | Nhịp 3 + câu gộp | K | N1 tr. 10–11 ("The Indictment alleged…"); tr. 8; N4; N2 | (A)–(G) khớp. Gợi ý văn phong (không tính): "alleged lies" → "alleged false and misleading statements" (nguyên văn tr. 10) và "generally fell into seven categories" |
| 50 | Nhịp 4 — Kiểm 1 | K | N1 tr. 10 (300/12, "general chemistry tests", máy hãng thứ ba có sửa); tr. 11 (trượt QC, "dismissed … or shifted blame") | |
| 51 | Nhịp 4b + câu kèm | K | N1 tr. 12 ("Multiple investors testified…"); tr. 16; N4 | |
| 52 | Nhịp 5 — Kiểm 2 | K | N1 tr. 12 | "led to believe", "surreptitiously" — khớp; không dùng "null protocol" |
| 53 | Nhịp 6 — Kiểm 3 | K | N1 tr. 12 | 0 doanh thu 2012–2013; lỗ 57/92 triệu; 15 triệu tiền mặt, 2 triệu/tuần (11/2013); 1.944.948 USD (IRS 2015); dự báo lãi 230 triệu cuối 2015 — khớp |
| 54 | Nhịp 6b | K | N6 ("over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015"); N5 | "gần 1 tỷ" theo N6 (N5 viết "approximately") — giữ chữ của N6 |
| 55 | Nhịp 7 — Kiểm 4 + câu kèm | K | N1 tr. 14; tr. 8; tr. 17 | Holmes thừa nhận tự gắn logo; email gửi Walgreens; đại diện các hãng khai không thẩm định, không cho phép — khớp; hãng không tên |
| 56 | Nhịp 8 — Kiểm 5 + câu kèm | K | N1 tr. 12–13 | 200 triệu USD từ DoD; lời vị tướng (thực địa, medevac, chiến trường); ghi âm 12/2013 trích đúng nguyên văn tr. 13 |
| 57 | Nhịp 9 — Kiểm 6 + câu kèm | K | N1 tr. 13–14; N6 ("from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating") | |
| 58 | Nhịp 10 — Kiểm 7, câu kèm | **S** | N1 tr. 7; N6; **N2, N3** ("charged … Theranos Inc., its founder…") | Nội dung (cuốn hút, quan hệ, sĩ quan cao cấp; 4 tỷ USD cuối 2014, bìa tạp chí qua "prosecutors said") khớp. **Lỗi ở câu kèm**: "Apart from Holmes and Balwani, none of the companies … was accused of wrongdoing in these cases" — Theranos là công ty bị SEC cáo buộc (◐, chính tệp §5 (b), nhịp 12), nên câu sai chủ thể và mâu thuẫn câu gộp nhịp 18. **Sửa:** "Apart from Theranos, Holmes and Balwani, none of the other companies, investors, board members, military officers or prominent backers was accused of wrongdoing in these cases." (sửa luôn chú thích "chỉ Holmes, Balwani bị truy tố (N4), SEC chỉ kiện Theranos, Holmes, Balwani (N2)" — đã đúng) |
| 59 | Nhịp 11 | K | N1 tr. 7–8 (báo chí cuối 2015), tr. 11 (CMS thanh tra không báo trước cuối 2015, "immediate jeopardy"), tr. 30–31 (báo cáo phát hành 01/2016, Theranos nhận đầu 2016), tr. 32 (nhân chứng khai huỷ mọi kết quả Edison) | |
| 60 | Nhịp 12 + câu kèm | K | N2; N3 | 14/03/2018; > 700 triệu USD; "elaborate, years-long fraud"; 500.000 USD, cấm 10 năm officer/director công ty đại chúng, 18,9 triệu cổ phần, từ bỏ quyền biểu quyết; "subject to court approval"; "neither admitted nor denied"; SEC kiện Balwani tại toà — khớp. ◐ đúng |
| 61 | Nhịp 13 | K | N1 tr. 8, 15; N4 (truy tố 14/06/2018, công bố 15/06); N5/N6/N8 (cáo trạng thay thế 28/07/2020) | Xử riêng, cuối 2021/đầu 2022, gần bốn tháng — tr. 15 |
| 62 | Nhịp 14 | K | N1 tr. 15; N5 (> 140 triệu USD; Count 9 "dismissed during the trial"); N6 (03/01/2022) | Bốn mảnh đúng, nhãn ● chỉ 4 ô |
| 63 | Nhịp 15 + câu nối | K | N1 tr. 15–16; N7 (07/07/2022, "a separate jury", tất cả tội); N8 (07/12/2022, 155 tháng, 3 năm giám sát; 6 + 4 tội); thông cáo 18/08/2022 | Câu nối "acquitted of the patient conspiracy count and three patient wire-fraud counts; one other patient count was dismissed" khớp N1 tr. 8, 15 (Count 9 là tội bệnh nhân). Diễn ý "these inaccurate results" đúng tr. 15 |
| 64 | Nhịp 16 + câu kèm Safeway/Walgreens | K | N6 (18/11/2022, Davila, 135 tháng, 3 năm, "No fine", "ordered to surrender on April 27, 2023"); N1 tr. 15 (120 triệu), 16 (135; 05/2023; liên đới), 17 (452 / 397 / 54,5) | |
| 65 | Nhịp 17 | K | N1 tr. 2 ("Filed February 24, 2025"), 8 ("We affirm."), 53 (không bán được; trích nhà đầu tư nguyên văn), 54 ("affirm … restitution order in its entirety"); N14; N9 | Trạng thái BOP và N9 khớp lần mở 01/11/2026 của vòng này |
| 66 | Nhịp 18 + câu gộp | K | N1 tr. 8, 16–17; N4; N2 | Câu gộp loại trừ đúng Theranos, Holmes, Balwani |
| 68 | Ghi chú MH | K | — | |
| 69 | Ghi chú lời người thật | K | N1 tr. 7, 9 ("ultimately all roads"), 13, 53; N3 | |
| 73–74 | §3 khuôn tập | **S** | §0 (dòng 19), nhịp 3 (dòng 49); N1 tr. 10–11 | "bảy câu kiểm (sáu nhóm lời hứa theo cáo trạng + một câu của kênh)" — cáo trạng có **bảy** nhóm, không phải sáu; mâu thuẫn trong tệp. **Sửa:** "bảy câu kiểm (sáu câu dựng từ bảy nhóm lời khai sai theo cáo trạng + một câu của kênh)". Phần lập luận 0b, so tập 1 (~16 phút, `1inmm-horwitz.md`), 12:55 (QUY-TRINH §6) khớp |
| 76–77 | Cú treo câu 1 | K | N6 ("In its memorandum filed for the sentencing hearing… By the end of 2014, her stock in Theranos was valued at more than $4 billion") | ●D có chủ thể |
| 76–77 | Cú treo câu 2 | K | N1 tr. 11 ("unannounced inspection … in late 2015") | |
| 83 | L1 | K | N1 tr. 10, 53; N3 | Không khuyên sản phẩm |
| 84 | L2 | K | N1 tr. 7, 8 ("never validated"), 13–14; N6 | |
| 85 | L3 | K | N1 tr. 12; N3 (Jina Choi, Director SF Regional Office — trích đúng nguyên văn) | |
| 86 | D (1) | K | N1 tr. 14 | |
| 86 | D (2) | K | N1 tr. 12 | |
| 86 | D (3) | K | N1 tr. 12 | |
| 86 | D (4) | K | N1 tr. 13 | Gợi ý văn phong: ngoặc kép "từ Bộ Quốc phòng" không phải trích nguyên văn — bỏ ngoặc hoặc dùng "from the Department of Defense" |
| 86 | D (5) | K | N1 tr. 13–14 | |
| 87 | P | K | N11, N12 (mở được, 200); N10, N13 KKĐ (sec.gov) | Nguyên tắc chung; không khuyên pháp lý/sản phẩm |
| 89 | Thẻ tổng kết | K | N1 tr. 53; N10 (KKĐ) | Không nhắc bệnh nhân/phán quyết; không hướng dẫn làm theo |
| 90 | Ghi chú thẻ | K | — | |
| 96 | §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | |
| 97 | §5 (b) | K | N2; N4 | Theranos ◐, không bị truy tố hình sự |
| 98 | §5 (c) | K | — | Rà toàn tệp: không tên nhà đầu tư, nhân chứng, bệnh nhân, nhân viên, quan chức SEC/DOJ |
| 99 | §5 (d) | K | N1 tr. 7 ("mirage"), tr. 8 ("half-truths and outright lies") | |
| 100 | §5 (e) | **S** | N2, N3; dòng 66 | Mẫu "Nhà đầu tư / thành viên HĐQT / nhân vật nổi tiếng — 'Apart from Holmes and Balwani, none of the companies…'" cùng lỗi với nhịp 10. **Sửa** như nhịp 10 ("Apart from Theranos, Holmes and Balwani, none of the other companies…"). Các mẫu Walgreens, Safeway, hãng dược, quân đội, nhà đầu tư đúng chủ thể và có nguồn |
| 101 | §5 (f) | K | N1 tr. 7, 9, 15; N6 | |
| 102 | §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32; N8 | |
| 103 | Phép thử làm theo được | K | — | Rà toàn tệp: đạt |
| 107 | §6 đơn giá | K | QUY-TRINH §6 | 0,40 USD/clip 8 s; 1,5 lượt/khe (2 khe); 0,4401; 155 từ/phút; 12.230/2.005 = 6,1; nhạc ~825 chưa đo; NB2.1 không khoá — khớp |
| 111 | Veo | K | — | 14×0,40×1,0 = 5,60; 18×0,40×1,25 = 9,00; 22×0,40×1,5 = 13,20 |
| 112 | TTS | K | — | 17×155 ≈ 2.635 từ ≈ 2.600; ×6,1 ≈ 15.900; ×0,4401 ≈ 7.000; +25 %/+50 % = 8.750/10.500; 17:45/17 ≈ +4,4 % |
| 113 | Music | K | — | 2.475 / 3.300 / 4.125 |
| 114 | Tổng tiền | K | — | |
| 115 | Tổng ký tự | K | — | 9.475 ≈ 9.500; 12.050; 14.625 ≈ 14.600 |
| 117 | Ràng buộc hình | K | NHAT-KY dòng 124–125 (ngược sáng → bóng, MR-4) | |
| 118 | Trần đề xuất | K | — | 9,00 × 1,15 = 10,35 ≈ 10,40; 12.050 × 1,15 ≈ 13.860 ≈ 14.000 |
| 124 | §7 N1 | K | SHA-256 khớp; tr. đọc | |
| 125 | §7 N2 | KKĐ | — | Nội dung khớp bản phiên chính; HTTP/đường mở sec.gov không kiểm theo lệnh. Gợi ý: cột "Dùng cho" còn thiếu các câu kèm (nhịp 2, 3, 7, 8, 9, 16, 18; §5 (b)) |
| 126 | §7 N3 | KKĐ | — | Như trên; "Dùng cho" thiếu H2 |
| 127 | §7 N4–N8 | K | API DOJ, 200, 6 kết quả | Gợi ý: "Dùng cho" thiếu H4, H5, câu kèm (N4), nhịp 14 dùng cả N5 |
| 128 | §7 N9 | K | curl 200; "Updated October 20, 2026"; 0 kết quả | |
| 129 | §7 N10 | KKĐ | — | sec.gov không mở theo lệnh |
| 130 | §7 N11 | K | curl 200 | |
| 131 | §7 N12 | K | curl 200 | |
| 132 | §7 N13 | KKĐ | — | adviserinfo.sec.gov không mở theo lệnh |
| 133 | §7 N14 | K | BOP JSON 200 | Tên trại không lên hình — đúng |
| 134 | §7 N15 | KKĐ | — | sec.gov; không dùng cho nhịp nào |
| 135 | §7 investor.gov | KKĐ | — | Không mở theo lệnh; tệp ghi "không dùng" — không ảnh hưởng nội dung |
| 138 | §8 kiểm trạng thái | K | — | |
| 139 | §8 Judgment/PACER | K | NHAT-KY dòng 117 (K5 hoãn PACER) | |
| 140 | §8 ảnh trang hồ sơ | K | N1 tr. 1, 9, 10, 12–15, 54 | Gợi ý văn phong: cụm "(… không crop phần tên nhà đầu tư ở tr. 10)" đặt trong ý về tr. 15 gây rối; lưu ý đoạn phán quyết tr. 15 nằm ngay dưới đoạn lý do tách phiên — crop phải loại hẳn đoạn đó |
| 141 | §8 trích nguyên văn nhịp 8 | K | N1 tr. 13 | |

## Kiểm riêng

1. **Phán quyết Holmes 4/4/3 + Count 9:** đúng ở §0, nhịp 14 (đủ bốn mảnh), câu nối nhịp 15, §5 (a). Logline VI/EN, H4 nêu ba vế bồi thẩm, không nêu Count 9 — chấp nhận (Count 9 bị rút, không phải phán quyết). Không câu nào nói/ám chỉ Holmes bị kết án lừa bệnh nhân; nhịp 11 (CMS, huỷ kết quả) đi trước phán quyết nhưng nhịp 14–15 nói rõ trắng án. **Đạt.**
2. **Balwani:** chỉ theo bản án của ông (N7, N8, N1 tr. 16); không gán cho Holmes. **Đạt.**
3. **Không tên** bệnh nhân/nhà đầu tư/nhân chứng: **đạt** (tên duy nhất ngoài hai bị cáo là Thẩm phán Davila).
4. **Câu không liên quan:** Walgreens, Safeway, hãng dược (không tên), quân đội, nhà đầu tư — đúng chỗ và đúng chủ thể; **trừ** câu nhóm "Apart from Holmes and Balwani, none of the companies…" (nhịp 10, §5 (e)) — S.
5. **Luật 8 (a)–(f):** đạt; (e) có lỗi ở mục 4.
6. **Không hướng dẫn làm theo được:** đạt.
7. **Số trang dẫn:** mọi số trang N1 đã đối chiếu đều đúng; không dẫn tr. 3–6.
8. **Cấu trúc bảy câu kiểm:** nhất quán ở §0, H5, nhịp 3–10, §6; **lệch** ở §3 — S.

## Không kiểm được

- N2, N3: trạng thái HTTP/đường mở sec.gov (nội dung đã đối chiếu bằng bản phiên chính).
- N10 (sec.gov/tcr), N13 (adviserinfo.sec.gov), N15 (complaint SEC): sec.gov không mở theo lệnh.
- investor.gov (tệp ghi 403, không dùng): không mở theo lệnh.

## Tổng đếm

| Điểm | Số dòng |
|---|---|
| K | 76 |
| MH | 0 |
| S | 3 (nhịp 10 dòng 58; §3 dòng 73–74; §5 (e) dòng 100) |
| KKĐ | 6 (§7: N2, N3, N10, N13, N15, investor.gov) |
| **Tổng** | **85** |
