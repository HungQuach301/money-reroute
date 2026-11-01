# Kiểm độc lập — dàn truyện `theranos-holmes` (tập 4) · vòng 1

> Tác tử kiểm độc lập · 01/11/2026 · chấm `docs/dan-truyen/theranos-holmes.md` (bản ở cây làm việc, 141 dòng) đối chiếu nguồn gốc mở đúng trang. Không sửa dàn truyện, không commit.
> Không đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài tệp này), lịch sử git, `docs/kho-de-tai/kiem/**`. Đọc `docs/kho-de-tai/theranos-holmes.md` §8 chỉ để tra URL. Không gọi API trả tiền.

## Kết luận ngắn

Dàn truyện **bám nguồn tốt**: gần như mọi sự việc khớp đúng trang N1 hoặc đúng thông cáo DOJ/SEC; phán quyết của Holmes được tách đủ bốn mảnh (kết án 4 / trắng án 4 / treo 3 / Count 9 rút) và không câu nào nói Holmes lừa bệnh nhân; Balwani chỉ theo bản án của ông; phép thử "làm theo được" đạt; số ở §6 khớp QUY-TRINH §6 và tính lại đúng.
Phải sửa trước khi duyệt: **4 S** — quan trọng nhất là câu mẫu "None of the investors, **board members** … was accused" **sai** (Balwani là thành viên HĐQT và bị truy tố — N4, N7, N8; Holmes là Chairperson — N6); ngày phán quyết 03/01/2022 dẫn N5 nhưng N5 không có ngày (ngày nằm ở N6/N7/N8); tiêu đề ghi "N10–N16" nhưng bảng chỉ có tới N15. **8 MH**, chủ yếu là các câu "not accused" chưa giới hạn "in these cases", logline EN bỏ vế treo, thẻ tổng kết nói "partners who won't confirm the partnership" (Walgreens có quan hệ đối tác thật; điều bị khai sai là "đang mở rộng"), và tên nhân chứng "Das" bị ghi trong bảng KBCB của chính tài liệu.

**Đếm:** K = 71 · MH = 8 · S = 4 · KKĐ = 4 (tổng 87 dòng chấm).

## Nguồn đã mở (vòng này)

| Mã | Cách mở | Kết quả |
|---|---|---|
| N1 | Tệp repo `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf`; `sha256sum` = `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**; `pdftotext -layout -f P -l P` từng trang 1–54; đọc kỹ tr. 1–2, 7–17, 31–33, 52–54 | Số trang in = số trang PDF (đã đối chiếu đầu trang). Không dùng tr. 3–6 (Summary) |
| N2, N3 | **Kiểm trên bản phiên chính đã tải** (`…/scratchpad/src/sec/lr-24069.html`, `2018-41.html`); tác tử kiểm **không** tự tải sec.gov. SHA-256 bản HTML: lr-24069 `a024c2a0…793d`, 2018-41 `7b00d258…4278` | Đọc toàn văn phần `<main>` |
| N4–N8 | API chính thức `justice.gov/api/v1/press_releases.json?parameters[title]=Theranos&pagesize=50`, curl mặc định, HTTP 200, 6 kết quả; body HTML bóc chữ | N4 = 15/06/2018; N5 = 04/01/2022; N7 = 07/07/2022; N6 = 18/11/2022; N8 = 07/12/2022 (trường `date`); kết quả thứ 6 ("Seeks Information From Victims") không dùng |
| N9 | curl mặc định, 200; tiêu đề "Clemency Grants by President Donald J. Trump (2025-Present)", "Updated October 20, 2026" | 0 kết quả "Holmes", 0 kết quả "Balwani" |
| N11 | `brokercheck.finra.org`, curl mặc định, 200 (tiêu đề "BrokerCheck - Find a broker…") | — |
| N12 | `reportfraud.ftc.gov`, curl mặc định, 200 (tiêu đề "ReportFraud.ftc.gov") | — |
| N14 | BOP JSON công khai, 24965-111 và 24966-111, curl mặc định, 200, `"Captcha":false` | HOLMES ELIZABETH — Bryan, projRelDate 02/22/2030; BALWANI RAMESH — Lompoc II, projRelDate 04/21/2033 |
| N10, N13, N15 | sec.gov / adviserinfo.sec.gov — **không mở** theo lệnh (tác tử kiểm không tự tải sec.gov; phiên chính không chuyển bản tải) | → mục "Không kiểm được" |

## Bảng chấm

Ký hiệu: K khớp đúng trang · MH mạnh hơn nguồn/tầng · S sai · KKĐ không kiểm được.

### Đầu tệp và §0

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú + sửa đề xuất |
|---|---|---|---|---|
| 1 | Quy ước trang N1 (số in = số PDF; không dẫn tr. 3–6); ký hiệu tầng; "Balwani: cả 12 tội (N1 tr. 16; N7; N8)" | K | N1 tr. 3–6 (Summary), tr. 16; N7 "found guilty on all counts"; N8 | — |
| 2 | "Mã nguồn N1–N9 theo kho §8; **N10–N16** mở ở MR-D4 (§7)" | **S** | §7 dàn truyện | Bảng §7 chỉ có N10–N15; không có N16. Sửa: "N10–N15". |
| 3 | §0 ba phần phán quyết Holmes + Count 9 rút (N1 tr. 15; N5) | K | N1 tr. 15 ("the government dismissed Count 9… acquitted… Count 2… Counts 10–12… convicted… Count 1… Counts 6–8… hung… Counts 3–5"); N5 | — |
| 4 | §0 Balwani: bồi thẩm khác, 12/12 (2 âm mưu + 10 wire fraud), 155 tháng; lý do tách phiên tr. 15, quan hệ riêng tr. 9, N8 | K | N1 tr. 9, 15, 16; N7; N8 ("a different federal jury", "former romantic partner") | Trang dẫn đúng |
| 5 | §0 không tên; "N1 tr. 10, 12, 13 nêu tên" | K | N1 tr. 10 (6 nhà đầu tư), 12 (kiểm soát viên, 2 nhà đầu tư), 13 (vị tướng) | Bổ sung cho đủ: tr. 14 nêu tên 3 hãng dược và tr. 32–33 nêu tên nhân chứng — cũng không dùng |
| 6 | §0 Walgreens/Safeway/hãng dược/nhà đầu tư/HĐQT không bị cáo buộc, mỗi đoạn có câu kèm | K | — (quy tắc) | Xem dòng 34, 65–67 về nội dung câu mẫu |
| 7 | §0 cơ chế: "ran samples on other companies' machines"; không "null protocol" | K | N1 tr. 12 có "null protocol" — dàn truyện không đưa vào lời | Đạt kiểm (6) |
| 8 | §0 bảy nhóm theo cáo trạng (N1 tr. 10–11) | K | N1 tr. 10–11 "(A)…(G)" | — |

### Logline và móc câu

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú + sửa đề xuất |
|---|---|---|---|---|
| 9 | Logline VI | K | N1 tr. 7, 15, 16, 54; N3 ("Silicon Valley-based private company"); N6 ("induce dozens of investors… hundreds of millions") | Đủ ba vế kết án / trắng án / treo; có "theo DOJ" |
| 10 | Logline EN "…A federal jury convicted its founder of defrauding investors — and acquitted her of the patient charges." | **MH** | N1 tr. 15; N6 | Bỏ vế treo 3 tội nhà đầu tư → người đọc hiểu mọi tội nhà đầu tư đều bị kết án (trái §0 "nói đủ"). Sửa: "*A federal jury convicted its founder on four counts of defrauding investors, acquitted her on the patient counts, and deadlocked on three more.*" |
| 11 | H1 khẩu hiệu "[O]ne tiny drop changes everything." | K | N1 tr. 7 (câu mở opinion) | Trên hình dàn truyện viết "One tiny drop…" — khi hiện chữ trích nên giữ đúng "[O]ne" như opinion (hoặc ghi "quoted in"). |
| 12 | H2 "a Silicon Valley company called Theranos claimed…" | K | N1 tr. 7 ("In the early 2010s, Theranos claimed that it could run fast, accurate, and affordable tests with just a drop of blood…"); "Silicon Valley-based": N3 | tr. 7 gọi là "a biotechnology company"; chữ "Silicon Valley" nằm ở N3 (và "Silicon Valley spectators" tr. 7). Thêm N3 vào cột nguồn. |
| 13 | H3 "According to the Justice Department… induced dozens of investors… hundreds of millions" | K | N6 ("Evidence showed that Holmes… was able to induce dozens of investors… to invest hundreds of millions of dollars") | Có chủ thể DOJ |
| 14 | H4 ba vế (Jan 2022; 4 kết án; 4 trắng án; 3 treo) | K | N1 tr. 15; N5 (ngày phát 04/01/2022); N6 ("On January 3, 2022") | "four counts of defrauding investors" gộp 1 tội âm mưu + 3 tội wire fraud; chấp nhận được (DOJ cũng dùng "fraud on investors"). Khuyến nghị cho đúng tội danh (8d): "*four investor-fraud counts — one conspiracy count and three wire-fraud counts*". Nguồn "No. 5:18-cr-00258 (N.D. Cal.)" khớp N1 tr. 1. Nên dẫn thêm N6 cho "January". |
| 15 | H5 (K, lời kênh) | K | — | Không có sự việc về người thật |

### Bảng nhịp

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú + sửa đề xuất |
|---|---|---|---|---|
| 16 | Nhịp 0 | K | §1 | — |
| 17 | Nhịp 1 (2003; CEO tới 2018; mẫu máu đầu ngón tay; Edison; Balwani 2009, President & COO) | K | N1 tr. 8 ("founded Theranos in 2003… until 2018"), tr. 9 (Edison; Balwani "joined the company in 2009… President and Chief Operating Officer") | Không nhắc quan hệ riêng (tr. 9) — đạt 8f |
| 18 | Nhịp 2 (ra mắt Walgreens thu 2013; C-1 cuối 2013; C-2 2014; cổ phần không giao dịch công khai) | K | N1 tr. 10 | — |
| 19 | Nhịp 2 câu kèm Walgreens "…not accused of wrongdoing in these cases; the court later treated it as a victim owed restitution." | K | Vế nạn nhân: N1 tr. 17 ("$54.5 million for two other victims, Safeway and Walgreens"). Vế "not accused in these cases": N1 tr. 8 (cáo trạng chỉ buộc Holmes, Balwani); N4; N2/N3 (SEC chỉ kiện Theranos, Holmes, Balwani) | Cột nguồn chỉ ghi tr. 17 — thêm N1 tr. 8; N4; N2 cho vế "not accused". |
| 20 | Nhịp 2b câu khung SEC "no exemption… non-public, development-stage, or the subject of exuberant media attention" | K | N3 (lời Co-Director Enforcement Division) | Trích đúng; chủ thể "an SEC enforcement official said in 2018" đúng chức danh |
| 21 | Nhịp 3 bảy nhóm (A)–(G), tầng ◐ "The indictment grouped the alleged lies…" | K | N1 tr. 10–11 ("The Indictment alleged… generally fell in the following categories") | Đúng tầng |
| 22 | Nhịp 4 (300 / 12 xét nghiệm; máy hãng thứ ba, một số đã sửa; nhân viên khai trượt QC; báo Holmes, Balwani; gạt đi/đổ lỗi) | K | N1 tr. 10 (300, twelve, "modifications to third-party machines"), tr. 11 ("testified at both trials… consistently failed quality control… dismissed these concerns or shifted blame") | Opinion: "Other 'general chemistry tests'… were run on third-party… machines" — giữ "other tests" ở mức chung là được |
| 23 | Nhịp 4b nhiều nhà đầu tư khai bị khiến tin chỉ chạy trên máy Theranos | K | N1 tr. 12 ("Multiple investors testified…") | — |
| 24 | Nhịp 5 khách "VIP" kể cả nhà đầu tư; tin máy chạy mẫu của mình; một số mẫu chạy kín trên máy hãng khác | K | N1 tr. 12 | Không dùng "null protocol" — đạt |
| 25 | Nhịp 6 (0 doanh thu 2012–2013; lỗ 57 và 92 triệu; 11/2013 còn 15 triệu, chi tới 2 triệu/tuần; IRS 2015 1.944.948 USD; dự báo lãi 230 triệu cuối 2015) | K | N1 tr. 12 | Lời khai kiểm soát viên chỉ phủ vế doanh thu/lỗ; các vế tiền mặt và IRS là toà thuật lại — khi viết lời, đừng gán cả câu cho "the controller testified" |
| 26 | Nhịp 6b theo DOJ: >100 triệu 2014, gần 1 tỷ 2015 | K | N6 ("Holmes misrepresented to other investors that Theranos, which had zero revenue in 2012 and 2013, was projected to generate over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015"); N5 ("approximately $1 billion") | — |
| 27 | Nhịp 7 (Holmes thừa nhận gắn logo; email Walgreens; đại diện hãng khai không thẩm định độc lập, không cho phép logo; báo cáo đưa nhà đầu tư) + tr. 8 "never validated" | K | N1 tr. 14; tr. 8 | Hãng dược không nêu tên (tr. 14 có tên — không dùng) |
| 28 | Nhịp 7 câu kèm "The drug companies were not accused of wrongdoing; their representatives testified they **never** authorized the use of their logos." | **MH** | N1 tr. 14 ("neither independently validated… nor authorized the use of their company logo **on these reports**") | (i) "never authorized" rộng hơn "not… on these reports"; (ii) "not accused of wrongdoing" không giới hạn — nguồn chỉ cho thấy họ không bị buộc tội **trong các vụ này** (N1 tr. 8; N4; N2). Sửa: "*The drug companies were not accused of wrongdoing in these cases; their representatives testified they did not authorize their logos on these reports.*" Sửa đồng thời §5(e). |
| 29 | Nhịp 8 (nhà đầu tư khai được nói 200 triệu từ DoD; vị tướng khai chưa ra thực địa/medevac/chiến trường; trích cuộc gọi 12/2013 ở phiên Holmes) | K | N1 tr. 12–13; chú thích 2 tr. 13 (bản ghi không đưa ra ở phiên Balwani) | Trích nguyên văn khớp tr. 13 |
| 30 | Nhịp 8 câu kèm "The U.S. military was not accused of **any** wrongdoing." | **MH** | Nguồn chỉ cho thấy không bị buộc tội trong các vụ này (N1 tr. 8; N4; N2) | "any wrongdoing" là khẳng định tuyệt đối không có nguồn. Sửa: "*The U.S. military was not accused of wrongdoing in these cases.*" Sửa đồng thời §5(e). |
| 31 | Nhịp 9 (đại diện Walgreens khai đang thu hẹp, thử không như kỳ vọng; DOJ: từ vài chục lên 900, dù biết đang chững lại) | K | N1 tr. 13–14; N6 ("from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating") | — |
| 32 | Nhịp 9 câu kèm Walgreens | K | Như dòng 19 | Thêm nguồn cho vế "not accused" |
| 33 | Nhịp 10 (bị cuốn hút; quan hệ với công ty lớn, nhà đầu tư, nhân vật nổi tiếng, sĩ quan cao cấp; DOJ: cổ phần >4 tỷ cuối 2014; bìa tạp chí) | K | N1 tr. 7; N6 ("In its memorandum filed for the sentencing hearing… By the end of 2014, her stock in Theranos was valued at more than $4 billion… adorning the cover of…") | Vế 4 tỷ/bìa là **lập luận của công tố trong bản ghi nhớ tuyên án** do DOJ thuật lại — giữ "prosecutors said in a sentencing filing". Không dùng dinh thự/máy bay (cùng đoạn N6) — đạt 8f |
| 34 | Nhịp 10 câu kèm "None of the investors, **board members** or prominent backers was accused of wrongdoing in these cases." | **S** | N4 ("Balwani worked… as a member of the company's board of directors"); N7, N8 (như trên); N6 (Holmes "held the positions of Chairperson and Chief Executive Officer") | Câu sai: Balwani là thành viên HĐQT và bị truy tố, kết án; Holmes là Chủ tịch HĐQT. Sửa: "*Apart from Holmes and Balwani, none of the investors, board members or prominent backers was accused of wrongdoing in these cases.*" (nguồn: N1 tr. 8; N4; N2). Sửa đồng thời §5(e). |
| 35 | Nhịp 11 (cuối 2015 báo chí; CMS thanh tra không báo trước, "immediate jeopardy"; nhân chứng khai Theranos huỷ toàn bộ kết quả trên Edison) | K | N1 tr. 7–8 (báo chí late 2015), tr. 11 (CMS), tr. 32 ("allowing [nhân chứng] to testify that Theranos voided all patient tests run on the Edison") | Rủi ro ám chỉ (kiểm 1): N1 tr. 32 ghi bồi thẩm được dặn báo cáo CMS chỉ dùng cho trạng thái nhận thức, Holmes không thể bị kết tội chỉ vì vi phạm quy định; Holmes trắng án tội bệnh nhân. Đề xuất kịch bản không nối nhịp 11 với "patients were defrauded"; giữ ở "the lab". "sau đó" — opinion không nêu thời điểm huỷ; bỏ "sau đó" hoặc giữ chung |
| 36 | Nhịp 12 SEC 14/03/2018; >700 triệu; dàn xếp không thừa nhận/không phủ nhận; 500.000 USD; cấm 10 năm; trả 18,9 triệu cổ phần; từ bỏ quyền biểu quyết chi phối; chờ toà chấp thuận; SEC theo kiện Balwani | K | N2; N3 (bản phiên chính tải) | Đúng tầng ◐; không "court ordered" |
| 37 | Nhịp 13 (truy tố 06/2018; điều tra 2,5 năm; cáo trạng thay thế 28/07/2020; xử riêng: Holmes cuối 2021, Balwani đầu 2022, mỗi phiên gần 4 tháng) | K | N4 (phát 15/06/2018, "indictment returned yesterday"); N5 ("initially charged on June 14, 2018. On July 28, 2020… superseding indictment"); N1 tr. 8 ("two-and-a-half-year investigation"), tr. 15 | N1 gọi là "Third Superseding Indictment"; nói "a superseding indictment" là an toàn |
| 38 | Nhịp 14 "Phán quyết **03/01/2022**" — nguồn ghi "N1 tr. 15; N5" | **S** | N1 tr. 15 và N5 **không có** ngày 03/01/2022 (N5 chỉ "A jury found…", phát 04/01/2022). Ngày có ở N6 ("On January 3, 2022"), N7, N8 | Nội dung bốn mảnh khớp N1 tr. 15; "hơn 140 triệu USD" khớp N5/N6. Sửa cột nguồn: "N1 tr. 15; N5; **N6** (ngày 03/01/2022)". |
| 39 | Nhịp 15 Balwani (07/07/2022 bồi thẩm khác, 12 tội: 2 âm mưu, 6 nhà đầu tư, 4 bệnh nhân; trích "the evidence linked Balwani…"; 07/12/2022, 155 tháng, 3 năm giám sát) + câu nối "Holmes was acquitted of the patient counts." | K | N1 tr. 15 (trích nguyên văn), tr. 16 (Counts 1, 2, 3–8, 9–12; 155 months); N7 (07/07/2022); N8 (07/12/2022; 3 năm giám sát; "a different federal jury") | Lưu ý tr. 15 "Multiple patients testified at **the trials**" (cả hai phiên) — giữ lời khai bệnh nhân **chỉ** trong đoạn Balwani và bắt buộc câu nối, như dàn truyện đã làm |
| 40 | Nhịp 16 (18/11/2022; Thẩm phán Davila; 135 tháng; 3 năm giám sát; không phạt tiền; thiệt hại 120 triệu cho lượng hình; trình diện 27/04/2023; 05/2023 liên đới 452 triệu = 397 triệu cho 12 nhà đầu tư + 54,5 triệu Safeway, Walgreens) | K | N6 (sentenced today; supervision; "No fine was assessed"; surrender April 27, 2023); N1 tr. 2 (Davila), tr. 15 ($120 million), tr. 16 (135), tr. 16–17 (restitution) | — |
| 41 | Nhịp 16 câu kèm Safeway/Walgreens | K | N1 tr. 17 ("two other victims"); N1 tr. 8; N4; N2 | Thêm nguồn vế "not accused" |
| 42 | Nhịp 17 (24/02/2025 giữ nguyên; toàn bộ lệnh bồi hoàn; nhà đầu tư không bán được; trích "there was never a legitimate opportunity…") | K | N1 tr. 2 ("Filed February 24, 2025"), tr. 8 ("We affirm"), tr. 52–54 (harmless; "[un]able to liquidate"; trích; "affirm… in its entirety"; "AFFIRMED") | Nhà đầu tư trích "testified at both trials" — không tên, đạt. Thêm tr. 8 cho vế giữ nguyên bản án/mức án |
| 43 | Nhịp 17 trạng thái: BOP Holmes ra dự kiến 22/02/2030, Balwani 21/04/2033; không có trên trang ân xá | K | N14 (JSON, 200); N9 (200, "Updated October 20, 2026", 0 kết quả) | Mở lại 01/11/2026, khớp |
| 44 | Nhịp 18 | K | §4 | — |
| 45 | §2 ghi chú lời người thật: tr. 7, tr. 9 ("ultimately all roads"), tr. 13, tr. 53, N3 | K | N1 tr. 7, 9, 13, 53; N3 | Trang đúng |

### Cú treo, bài học, dấu hiệu, nguyên tắc, thẻ

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú + sửa đề xuất |
|---|---|---|---|---|
| 46 | Cú treo câu 1 "By the end of 2014, prosecutors said, her stake was valued at more than four billion dollars." | K | N6 (đoạn bản ghi nhớ tuyên án) | — |
| 47 | Cú treo câu 2 "In late 2015, federal inspectors arrived at the lab without warning." | K | N1 tr. 11 ("unannounced inspection of Theranos in late 2015") | — |
| 48 | L1 (cổ phần không giao dịch; không bán được; SEC: không miễn trừ cho công ty tư nhân) | K | N1 tr. 10, 53; N3 | — |
| 49 | L2 (logo tr. 14; bán lẻ tr. 13–14; quân đội tr. 13; nổi tiếng/báo chí tr. 7, N6; hãng dược khai chưa thẩm định, chưa cho phép logo) | K | N1 tr. 7, 8, 13, 14; N6 | Như dòng 28: giữ "trên các báo cáo này" khi viết lời |
| 50 | L3 "Buổi trình diễn do người gọi vốn điều khiển (tr. 12), **dự báo do họ soạn** (tr. 12)" | **MH** | N1 tr. 12 ("financial documents she **received from** Holmes and Balwani showed… projecting a profit of $230 million") | Opinion nói nhà đầu tư nhận tài liệu từ họ, không nói ai soạn. Sửa: "dự báo do chính họ đưa ra/gửi". Câu SEC trong L3 khớp N3 nguyên văn (lời Giám đốc Văn phòng vùng San Francisco) |
| 51 | D1 bảo chứng không xác nhận được (tr. 14) | K | N1 tr. 14 | — |
| 52 | D2 trình diễn do người bán điều khiển (tr. 12) | K | N1 tr. 12 | — |
| 53 | D3 dự báo vênh (0 doanh thu 2012–2013; lãi 230 triệu cuối 2015) | K | N1 tr. 12 | — |
| 54 | D4 hợp đồng quân đội (200 triệu "từ Bộ Quốc phòng"; chưa ra thực địa) | K | N1 tr. 12–13 | 200 triệu là điều **một nhà đầu tư khai đã được nói** — khi lên thẻ giữ khung "investors were told…" |
| 55 | D5 quan hệ "đang mở rộng" mà đối tác không xác nhận; Walgreens thực tế thu hẹp | K | N1 tr. 13–14 | — |
| 56 | P — nội dung nguyên tắc; FINRA BrokerCheck (N11); FTC ReportFraud (N12) | K | N11, N12 (200) | Không khuyên sản phẩm/tỷ trọng — đạt §1 |
| 57 | P — SEC Tips (N10), SEC IAPD (N13) | **KKĐ** | Không mở (sec.gov, theo lệnh) | Phiên chính hoặc điều phối xác nhận lại hai URL trước khi chốt lời |
| 58 | Thẻ tổng kết "…partners who won't confirm **the partnership**…" | **MH** | N1 tr. 10 (Walgreens hợp tác từ 2010, ra mắt 2013), tr. 13–14 (điều bị khai sai là quan hệ "đang mở rộng") | Quan hệ đối tác có thật; nói "won't confirm the partnership" gợi ý không có đối tác. Sửa: "*partners who won't confirm the growth you're told about*". Các vế còn lại của thẻ khớp L1–L3, D1–D4 (N1 tr. 12–14, 53). "sec.gov/tcr" → KKĐ (dòng 57/81) |

### §5 rà luật 8, luật 5

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú + sửa đề xuất |
|---|---|---|---|---|
| 59 | (a) Holmes ● 4 tội, 135 tháng, phúc thẩm giữ nguyên | K | N1 tr. 15–16, 54; N5; N6 | — |
| 60 | (b) Theranos ◐ dàn xếp, không bị truy tố hình sự; SEC v. Balwani kết cục chưa mở | K | N2; N4 (chỉ Holmes, Balwani bị truy tố) | — |
| 61 | (c) danh sách không tên | K | — | Xem dòng 69 |
| 62 | (d) không nhãn; "half-truths and outright lies", "nothing more than a mirage" chỉ làm chữ trích | K | N1 tr. 7 ("nothing more than a mirage"), tr. 8 ("half-truths and outright lies") | Trang đúng |
| 63 | (e) Walgreens | K | N1 tr. 17; tr. 8; N4; N2 | Thêm nguồn vế "not accused" |
| 64 | (e) Safeway | K | Như trên | — |
| 65 | (e) Hãng dược | **MH** | N1 tr. 14 | Như dòng 28 |
| 66 | (e) Quân đội | **MH** | — | Như dòng 30 |
| 67 | (e) Nhà đầu tư / thành viên HĐQT / nhân vật nổi tiếng | **S** | N4, N6, N7, N8 | Như dòng 34 |
| 68 | (f) không động cơ, tâm lý, quan hệ riêng, lý do tách phiên, lối sống | K | N1 tr. 9, 15; N6; N8 | Liên quan §8: ảnh tr. 15 — đoạn "Procedural History" ngay dưới đoạn bệnh nhân nêu lý do tách phiên (quan hệ riêng, 8f). Khi crop "đoạn phán quyết" tr. 15, loại cả đoạn tách phiên, không chỉ "dòng đầu" |
| 69 | Hàng KBCB: "…nhân chứng **"Das"** (tr. 32)…" | **MH** | N1 tr. 32–33 | Không phải sai sự việc nhưng chính tài liệu ghi tên nhân chứng — trái kiểm (3)/luật 5 và ý §0 "không tên". Sửa: "nhân chứng về việc huỷ kết quả (tr. 32)". |
| 70 | Phép thử "làm theo được ngay?" | K | — | Không có giao thức trình diễn, cách sửa máy, mẫu tài liệu, cách giả logo — đạt kiểm (6) |

### §6 ước chi (đối chiếu QUY-TRINH-TAP.md §6)

| # | Dòng | Điểm | Nguồn | Ghi chú |
|---|---|---|---|---|
| 71 | Veo 3.1 Lite 0,40 USD/clip 8 s (đo, không âm); 1,0–1,5 lượt; 14/18/22 khe → 5,60 / 9,00 / 13,20 USD | K | QUY-TRINH §6 (MR-4) | 14×0,40×1,0 = 5,60; 18×0,40×1,25 = 9,00; 22×0,40×1,5 = 13,20 |
| 72 | TTS 0,4401; 155 từ/phút; 6,1 ký tự/từ; ~2.600 từ → ~15.900 gửi → ~7.000 tính; +0/25/50 % → 7.000 / 8.750 / 10.500 | K | QUY-TRINH §6 (6.109/13.881; 12.230/2.005 = 6,10; 155 từ/phút) | 17×155 = 2.635; 2.600×6,1 = 15.860; ×0,4401 ≈ 6.980 |
| 73 | Eleven Music ~825 ký tự/phút (chưa đo) → 2.475 / 3.300 / 4.125 | K | QUY-TRINH §6 ("chưa đo") | — |
| 74 | Tổng tiền 5,60 / 9,00 / 13,20 USD | K | Tính lại | Ảnh NB2.1 "không có khoá" khớp QUY-TRINH |
| 75 | Tổng ký tự ElevenLabs ≈ 9.500 / 12.050 / 14.600 | K | Tính lại (9.475; 12.050; 14.625) | — |
| 76 | Trần đề xuất ≈ 10,40 USD; ≈ 14.000 ký tự | K | 9,00×1,15 = 10,35; 12.050×1,15 = 13.858 | Làm tròn lên hợp lý; chủ dự án quyết |

### §7 bảng nguồn

| # | Dòng | Điểm | Nguồn | Ghi chú |
|---|---|---|---|---|
| 77 | N1 SHA-256 khớp, 54 tr. | K | `sha256sum` vòng này | — |
| 78 | N2, N3 (SEC) | K | Bản phiên chính tải | Nội dung khớp nhịp 2b, 12, L1, L3. Kiểm trên bản phiên chính tải, không tự tải sec.gov |
| 79 | N4–N8 qua API, 6 kết quả | K | API DOJ, 200, 6 kết quả | — |
| 80 | N9 "Updated October 20, 2026", 0 kết quả | K | 200 | — |
| 81 | N10 SEC Tips `sec.gov/tcr` | **KKĐ** | Không mở (sec.gov) | — |
| 82 | N11 BrokerCheck 200 | K | 200 | — |
| 83 | N12 ReportFraud 200 | K | 200 | — |
| 84 | N13 SEC IAPD `adviserinfo.sec.gov` | **KKĐ** | Không mở (miền sec.gov) | — |
| 85 | N14 BOP | K | 200, `Captcha:false` | Tên trại không lên hình — đúng |
| 86 | N15 Complaint SEC (không dùng) | **KKĐ** | Không mở (sec.gov) | Không dùng cho nhịp nào nên không ảnh hưởng nội dung |
| 87 | §8 việc trước chốt lời (luật 4; PACER hoãn; ảnh trang hồ sơ; trích nguyên văn tr. 13) | K | N1 tr. 1, 9, 10, 12–13, 15, 54 | Bổ sung cho mục ảnh trang: xem dòng 68 (đoạn tách phiên ở tr. 15); tr. 14 có tên hãng dược — không dùng |

## Kiểm riêng (1)–(7)

1. **Phán quyết Holmes đủ và tách bạch:** đạt ở §0, H4, nhịp 14, thẻ 12 ô (4 + 4 + 3 + 1 = 12) — N1 tr. 15; N5; N6. Không câu nào nói/ám chỉ Holmes lừa bệnh nhân. Hai điểm cần giữ: logline EN thiếu vế treo (dòng 10, MH); nhịp 11 (CMS, huỷ kết quả) không được nối thành "patients were defrauded" (dòng 35).
2. **Balwani chỉ theo bản án của ông:** đạt (nhịp 15; N1 tr. 15–16; N7; N8); có câu nối "Holmes was acquitted of the patient counts".
3. **Không tên bệnh nhân/nhà đầu tư/nhân chứng:** lời và hình đạt; **chính tài liệu** ghi "Das" ở hàng KBCB (dòng 69, MH).
4. **Câu "not accused":** có ở mọi chỗ nêu Walgreens, Safeway, hãng dược, quân đội, nhà đầu tư/HĐQT/nhân vật nổi tiếng. Nguồn cho vế "not accused in these cases" = N1 tr. 8 + N4 + N2 (cần ghi vào cột nguồn). Câu HĐQT **sai** (dòng 34/67); câu hãng dược và quân đội **mạnh hơn nguồn** (dòng 28/30/65/66).
5. **Luật 8 (a)–(f):** (a), (b), (c) đạt; (d) đạt — không nhãn, trích lời toà có nguồn trang đúng; (e) xem mục 4; (f) đạt — không động cơ/lối sống/quan hệ riêng/lý do tách phiên trong lời; lưu ý ảnh tr. 15 (dòng 68).
6. **Không hướng dẫn làm theo được:** đạt (dòng 7, 70).
7. **Số trang dẫn:** đúng ở mọi dòng đã kiểm, trừ nguồn ngày 03/01/2022 ở nhịp 14 (dòng 38, S); nên thêm N3 cho "Silicon Valley" (dòng 12), tr. 8 cho "giữ nguyên bản án" (dòng 42), N1 tr. 8/N4/N2 cho vế "not accused".

## Không kiểm được

- **N10** SEC Tips (`sec.gov/tcr`), **N13** SEC IAPD (`adviserinfo.sec.gov`), **N15** complaint SEC: thuộc sec.gov — theo lệnh, tác tử kiểm không tự tải sec.gov và phiên chính không chuyển bản tải → **chưa mở được** ở vòng này. N10/N13 được dùng ở P và thẻ tổng kết ("sec.gov/tcr", "SEC IAPD") → cần xác nhận trước khi chốt lời. N15 không dùng cho nhịp nào.
- N2, N3 kiểm trên bản HTML **phiên chính đã tải** (không tải lại); không xác minh độc lập được chuỗi chuyển hướng URL ghi ở §7.
- Trạng thái certiorari, số phận Counts 3–5 sau phiên xử, judgment N.D. Cal., lệnh chấp thuận dàn xếp SEC: dàn truyện đã tự ghi "chưa có nguồn/chưa mở" và không dùng — vòng này cũng không mở.
- Khoản "MR-D4 chi 0 USD" (§6): số tự khai, không có số đo để đối chiếu.
