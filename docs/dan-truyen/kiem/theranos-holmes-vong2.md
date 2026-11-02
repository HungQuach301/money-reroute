# Biên bản kiểm độc lập — dàn truyện `theranos-holmes` (tập 4) · vòng 2

> Kiểm 01/11/2026 · tác tử kiểm độc lập · đối tượng: `docs/dan-truyen/theranos-holmes.md` (141 dòng, bản trong cây làm việc).
> Không đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài việc ghi tệp này), lịch sử git, `docs/kho-de-tai/kiem/**`. Kho `docs/kho-de-tai/theranos-holmes.md` chỉ đọc §8 để tra URL. Không gọi API trả tiền (chi 0 USD). Không tự tải trang sec.gov nào.

## Kết luận

**Sự việc vững; còn 1 lỗi số/sự việc, 1 câu mạnh hơn nguồn và 1 nhóm lỗ hổng luật 8(e) phải sửa trước khi duyệt.**

- Mọi số, ngày, tội danh, số trang dẫn của N1 đều khớp đúng trang (đã mở từng trang 1–2, 7–17, 31–33, 52–54). Phán quyết Holmes được tách đúng 4 phần (kết án 4 / trắng án 4 / treo 3 / Count 9 bị rút). Không câu nào nói hoặc ám chỉ Holmes bị kết án lừa bệnh nhân. Balwani chỉ được mô tả theo bản án của ông. Không có tên bệnh nhân, nhà đầu tư hay nhân chứng nào (người duy nhất có tên ngoài hai bị cáo là Thẩm phán Edward J. Davila, một quan chức đang thi hành công vụ). Các số ở §6 tính lại đều khớp QUY-TRINH §6.
- **S (1):** nhịp 16 viết "bà trình diện thi hành án 27/04/2023", nhưng nguồn (N6, N8) chỉ nói bà **bị lệnh** trình diện ngày đó.
- **MH (1):** nhịp 1 viết "mục tiêu", trong khi N1 tr. 8–9 viết "Holmes's **claimed** goal".
- **S, luật 8(e) (5):** §0 yêu cầu mỗi đoạn có nêu Walgreens, hãng dược, quân đội, nhà đầu tư, thành viên HĐQT hay nhân vật nổi tiếng phải kèm câu "không liên quan". Bảng nhịp chưa làm đủ: thiếu ở nhịp 3, ở nhịp 7 (phần Walgreens), ở nhịp 10 (phần quân đội), ở nhịp 18 (L2, D) và với nhà đầu tư ở hầu hết các nhịp. Mỗi câu mẫu ở §5(e) đều đúng và có nguồn. Lỗi nằm ở chỗ đặt câu.

## Nguồn đã mở

| Mã | Cách mở (01/11/2026) | Kết quả |
|---|---|---|
| N1 | Tệp repo `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf`; `sha256sum` = `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` (**khớp**); `pdfinfo` 54 tr.; `pdftotext -layout -f P -l P` từng trang | Số trang in trùng số trang PDF (đã đối chiếu tr. 2, 7–17, 31–33, 52–54). Opinion bắt đầu ở tr. 7 ("OPINION / NGUYEN, Circuit Judge"), nên không trích dẫn nào rơi vào tr. 3–6 |
| N2 | Bản phiên chính tải sẵn `…/scratchpad/src/sec/lr-24069.html` (SHA-256 `a024c2a0…793d`) | Đọc toàn văn. Lit. Rel. No. 24069 / March 19, 2018 |
| N3 | Bản phiên chính tải sẵn `…/scratchpad/src/sec/2018-41.html` (SHA-256 `7b00d258…4278`) | Đọc toàn văn. Press Release 2018-41, March 14, 2018 |
| N4–N8 | `curl` API chính thức `justice.gov/api/v1/press_releases.json?parameters[title]=Theranos&pagesize=50` → 200, `count` = 6; body HTML được tách sang chữ | N4 = phần tử 0 (15/06/2018) · N5 = phần tử 1 (04/01/2022) · N7 = phần tử 2 (07/07/2022) · (thông cáo "Seeks Information From Victims", 2022, không dùng) · N6 = phần tử 4 (18/11/2022) · N8 = phần tử 5 (07/12/2022) |
| N9 | `curl` mặc định → 200 | "Updated October 20, 2026"; 0 lần xuất hiện "Holmes", 0 lần "Balwani" |
| N11 | `curl -L` mặc định → 200 | Tiêu đề "BrokerCheck - Find a broker, investment or financial advisor" |
| N12 | `curl -L` mặc định → 200 | Tiêu đề "ReportFraud.ftc.gov" |
| N14 | `curl` mặc định JSON BOP, IRN 24965-111 và 24966-111 → 200 cả hai | Holmes: FPC "Bryan", projRelDate 02/22/2030. Balwani: FCI "Lompoc II", projRelDate 04/21/2033 |
| N10, N13, N15, investor.gov | Không mở (sec.gov, theo lệnh) | KKĐ |

## Bảng chấm

| # | Dòng | Điểm | Nguồn đã mở + trang | Ghi chú / sửa cụ thể |
|---|---|---|---|---|
| 1 | Đầu tệp: quy ước trang, ký hiệu tầng (dòng 5–11) | K | N1 tr. 3–6 là Summary, tr. 7 bắt đầu opinion; N1 tr. 16; N7; N8 | Balwani 12 tội đúng theo tr. 16, N7 ("guilty on all counts") và N8 |
| 2 | §0 · phán quyết 4 phần, Count 9 bị công tố rút | K | N1 tr. 15 ("the government dismissed Count 9… acquitted… convicted… hung"); N5 | — |
| 3 | §0 · Balwani: bồi thẩm khác, phiên riêng, 12/12, 155 tháng; lý do tách phiên (tr. 15) và quan hệ riêng (tr. 9; N8) không dùng | K | N1 tr. 9, 15, 16; N8 ("a different federal jury"; "former romantic partner") | — |
| 4 | §0 · không tên ("N1 tr. 10, 12, 13 nêu tên") | K | N1 tr. 10 (6 nhà đầu tư), 12 (kiểm soát viên, 2 nhà đầu tư), 13 (vị tướng); thêm tr. 32 (nhân chứng việc huỷ kết quả) | tr. 32 đã có ở §5 (KBCB). Nên thêm "32" vào §0 cho đồng bộ |
| 5 | §0 · câu "không liên quan" (quy tắc) | K | — | Quy tắc đúng. Chỗ áp dụng còn thiếu: xem các dòng 80–84 |
| 6 | §0 · cơ chế (không "null protocol") | K | N1 tr. 12 có "null protocol"; dàn truyện không dùng | — |
| 7 | §0 · góc "bảy nhóm lời hứa" (A)–(G) | K | N1 tr. 10–11 ("The Indictment alleged…") | — |
| 8 | Logline VI | K | N6 ("was able to induce dozens of investors… hundreds of millions"); N1 tr. 15–16, 8 ("We affirm."), 2 (2025) | Có chủ thể "theo DOJ"; nêu đủ 4 kết án / 4 trắng án / 3 treo |
| 9 | Logline EN | K | N1 tr. 15; tr. 16–17 ($397 million cho 12 nhà đầu tư nên "hundreds of millions" có nguồn toà) | — |
| 10 | H1 "[O]ne tiny drop changes everything." | K | N1 tr. 7 (nguyên văn) | Ghi chú nội bộ gọi đây là "khẩu hiệu", nhưng N1 viết "That was the vision shared by Holmes and Balwani". Lời kịch bản không được gọi là "slogan"; giữ nguồn "quoted in U.S. v. Holmes (9th Cir. 2025)" |
| 11 | H2 | K | N1 tr. 7 ("In the early 2010s, Theranos claimed…"); N3 ("Silicon Valley-based private company") | — |
| 12 | H3 | K | N6 ("Evidence showed that Holmes… was able to induce dozens of investors… to invest hundreds of millions of dollars") | ●D, có chủ thể |
| 13 | H4 | K | N1 tr. 15; N5; N6 ("On January 3, 2022") | "one conspiracy count and three wire-fraud counts" đúng; trắng án 4 (Count 2, 10–12); treo 3 |
| 14 | H5 | K | — (lời kênh) | — |
| 15 | Nhịp 0 | K | §1 | — |
| 16 | Nhịp 1 | **MH** | N1 tr. 8–9 | N1 viết "Holmes's **claimed** goal was to create technology to run blood tests on small samples… fingerstick". Dàn truyện viết "mục tiêu", tức coi đó là mục tiêu thật (chạm luật 8f vì nói về động cơ). **Sửa:** "mục tiêu bà tuyên bố: xét nghiệm trên mẫu máu nhỏ…" / EN "her stated goal". Các vế còn lại K: lập Theranos 2003, CEO tới 2018, "Edison", Balwani vào 2009, sau là President/COO (tr. 8–9) |
| 17 | Nhịp 2 | K | N1 tr. 10 (Walgreens mùa thu 2013; C-1 cuối 2013; C-2 2014; "Theranos shares were not publicly traded"); câu kèm: tr. 8 (cáo trạng chỉ buộc tội Holmes, Balwani), tr. 17 (Walgreens là nạn nhân được bồi hoàn); N4; N2 | Câu kèm Walgreens có. Câu kèm nhà đầu tư thiếu, xem dòng 84 |
| 18 | Nhịp 2b | K | N3 (Steven Peikin, Co-Director Enforcement: "…no exemption from the anti-fraud provisions… non-public, development-stage, or the subject of exuberant media attention.") | Chủ thể "an SEC enforcement official said in 2018" đúng |
| 19 | Nhịp 3 (sự việc) | K | N1 tr. 10–11 (A)–(G) | Tầng ◐ "The indictment grouped…" đúng. Câu kèm thiếu, xem dòng 80 |
| 20 | Nhịp 4 | K | N1 tr. 10 (300 / 12 / máy hãng thứ ba / "various modifications"); tr. 11 ("Theranos employees testified at both trials… dismissed these concerns or shifted blame") | — |
| 21 | Nhịp 4b | K | N1 tr. 12 ("Multiple investors testified…") | — |
| 22 | Nhịp 5 | K | N1 tr. 12 ("Employees testified… 'VIP' guests… led to believe… surreptitiously run on third-party devices") | Không dùng "null protocol", đạt |
| 23 | Nhịp 6 | K | N1 tr. 12 (Corporate Controller: không doanh thu 2012–2013, lỗ $57M/$92M; 11/2013 $15M tiền mặt, tới $2M/tuần; IRS 2015 $1,944,948; nhà đầu tư khai dự báo lãi $230M cuối 2015) | N1 chỉ ghi vế doanh thu và lỗ là lời kiểm soát viên. Vế 11/2013 và vế IRS là toà thuật lại. Khi viết lời, đừng để dấu hai chấm "Theo lời khai kiểm soát viên:" phủ cả ba vế |
| 24 | Nhịp 6b | K | N6 ("Holmes misrepresented to other investors that Theranos, which had zero revenue in 2012 and 2013, was projected to generate over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015"); N5 (bằng chứng xét xử: >$100M 2014, ~$1B 2015) | — |
| 25 | Nhịp 7 (sự việc) | K | N1 tr. 14 (Holmes thừa nhận tự gắn logo; email gửi Walgreens; đại diện các hãng khai không thẩm định, không cho phép dùng logo; báo cáo đưa nhà đầu tư, "vouching"); tr. 8 | Hãng dược không có tên, đạt. Câu kèm Walgreens thiếu, xem dòng 81 |
| 26 | Nhịp 8 | K | N1 tr. 12–13 (nhà đầu tư: $200M từ DoD; vị tướng khai ba điều "never"; ghi âm 12/2013 tại phiên Holmes, trích nguyên văn khớp); tr. 13 chú thích 2 (không dùng ở phiên Balwani) | Câu kèm quân đội có và đúng |
| 27 | Nhịp 9 | K | N1 tr. 13–14 (đại diện Walgreens: "contracting… pilot program was not going as hoped"); N6 ("from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating"); N8 (cùng câu) | Câu kèm Walgreens có |
| 28 | Nhịp 10 (sự việc) | K | N1 tr. 7 ("captivated… major companies, investors, and prominent figures, including high-ranking members of the United States military"); N6 ("In its memorandum filed for the sentencing hearing… By the end of 2014, her stock… more than $4 billion… adorning the cover of…") | Chủ thể "prosecutors said in a sentencing filing" đúng. Câu kèm nhà đầu tư/HĐQT/nhân vật nổi tiếng đúng (N4 chỉ truy tố Holmes và Balwani; N2/N3 chỉ kiện Theranos, Holmes, Balwani). Phần quân đội thiếu, xem dòng 82 |
| 29 | Nhịp 11 | K | N1 tr. 7–8 (báo chí cuối 2015); tr. 11 (CMS thanh tra không báo trước cuối 2015; "immediate jeopardy"); tr. 32 (nhân chứng khai Theranos "voided all patient tests run on the Edison"); tr. 31 (Theranos nhận báo cáo đầu 2016) | Ghi chú: "cùng năm, CMS… thanh tra…, **kết luận**…" dễ được hiểu là có kết luận ngay năm 2015, trong khi tr. 31 ghi Theranos nhận báo cáo đầu 2016. Nên viết "thanh tra cuối 2015; báo cáo sau đó kết luận…". Gợi ý (không bắt buộc): vì nhịp này nói về bệnh nhân và nằm trong mạch kể về Holmes, có thể thêm một vế "a finding about the company's lab" để người xem không hiểu nhầm trước nhịp 14 |
| 30 | Nhịp 12 | K | N2 và N3 (14/03/2018; >$700 million; "elaborate, years-long fraud"; $500,000; cấm 10 năm làm officer/director công ty đại chúng; 18.9 million shares; bỏ quyền biểu quyết chi phối; "subject to court approval"; "neither admitted nor denied"; "will litigate its claims against Balwani") | Lời EN phải là "agreed to pay…", không phải "paid" |
| 31 | Nhịp 13 | K | N4 (cáo trạng 06/2018, "returned yesterday and unsealed today"); N5, N6 ("initially charged on June 14, 2018"; superseding 28/07/2020); N1 tr. 8 (điều tra hai năm rưỡi), tr. 15 (cuối 2021 / đầu 2022 / gần 4 tháng); N7 (phiên Balwani bắt đầu 09/03/2022) | Nếu kịch bản cần tên chính xác: N1 tr. 8 gọi bản này là "Third Superseding Indictment" |
| 32 | Nhịp 14 | K | N1 tr. 15; N5 và N6 ("wire transfers totaling more than $140 million"; 03/01/2022) | 4 + 4 + 3 + 1 = 12 ô, đúng |
| 33 | Nhịp 15 | K | N1 tr. 15 ("The evidence linked Balwani to the transmission of these inaccurate results"), tr. 16 (12 tội: Count 1, 2, 3–8, 9–12; 155 tháng); N7 (07/07/2022, "all counts"); N8 (07/12/2022, 155 tháng, 3 năm giám sát; "a different federal jury") | Câu nối "Holmes was acquitted of the patient counts" có nguồn N1 tr. 15. Trong N1, chữ "these" trong câu trích chỉ các kết quả HIV và thai kỳ mà dàn truyện không nêu, nên khi trích cần thêm "[inaccurate test results]" hoặc diễn đạt lại để không lửng nghĩa |
| 34 | Nhịp 16 | **S** | N6 ("Holmes was ordered to surrender on April 27, 2023"); N8 ("She was ordered to surrender… on April 27, 2023"); N1 tr. 15 ($120 million), tr. 16–17 ($452M; $397M cho 12 nhà đầu tư; $54.5M cho Safeway và Walgreens; liên đới; 05/2023); N6 (18/11/2022; 135 tháng; 3 năm; "No fine was assessed") | "Bà **trình diện** thi hành án 27/04/2023" là sự việc khác với nguồn: nguồn chỉ nói bà **bị lệnh** trình diện ngày đó, còn ngày trình diện thật chưa có nguồn đã mở. **Sửa:** "bà bị lệnh trình diện thi hành án ngày 27/04/2023 (N6)" / EN "She was ordered to report to prison on April 27, 2023", hoặc bỏ vế này. Các vế còn lại K |
| 35 | Nhịp 17 | K | N1 tr. 2 ("Filed February 24, 2025"), tr. 8 ("We affirm."), tr. 53 ("[un]able to liquidate"; trích nhà đầu tư nguyên văn khớp), tr. 54 ("affirm the district court's restitution order in its entirety… AFFIRMED"); N14; N9 | BOP và trang ân xá khớp nguyên văn ngày 01/11/2026. Ghi chú: toà nói toà sơ thẩm có sai (không trừ giá trị còn lại của cổ phần) nhưng sai đó vô hại (tr. 52–53). Cách diễn "lý do bồi hoàn toàn bộ" chấp nhận được |
| 36 | Nhịp 18 | K | §4 | Xem dòng 83 |
| 37 | Cú treo câu 1 | K | N6 (memorandum tuyên án; "more than $4 billion" cuối 2014) | — |
| 38 | Cú treo câu 2 | K | N1 tr. 11 ("unannounced inspection of Theranos in late 2015") | — |
| 39 | L1 | K | N1 tr. 10, 53; N3 | Vế "lời của kênh" đã ghi rõ |
| 40 | L2 (sự việc) | K | N1 tr. 14, 13–14, 13, 7; N6 | Thiếu câu kèm, xem dòng 83 |
| 41 | L3 | K | N1 tr. 12; N3 (Jina Choi, Director SF Regional Office: trích nguyên văn khớp) | Chủ thể "an SEC official" đúng |
| 42 | D (5 dấu hiệu, sự việc) | K | (1) N1 tr. 14 · (2) tr. 12 · (3) tr. 12 · (4) tr. 12–13 (câu $200M vắt sang tr. 13; thiết bị chưa ra thực địa ở tr. 13) · (5) tr. 13–14 | Dấu (5) nêu tên Walgreens, dấu (4) nêu Bộ Quốc phòng mà không có câu kèm, xem dòng 83 |
| 43 | P | K | N11 (200), N12 (200) | N10 và N13 thuộc sec.gov: KKĐ (sec.gov không mở theo lệnh). Không có sản phẩm, không tỷ trọng |
| 44 | Thẻ tổng kết | K | N1 tr. 53 ("investors could not sell"); N11 | "SEC IAPD", "sec.gov/tcr": KKĐ (sec.gov không mở theo lệnh). Không nêu bệnh nhân, không nhắc lại phán quyết, đạt |
| 45 | Dòng 68–69 (lời người thật chỉ là chữ trích) | K | N1 tr. 7, 9 ("ultimately all roads"), 13, 53; N3 | — |
| 46 | §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | — |
| 47 | §5 (b) | K | N2; N4 (chỉ Holmes và Balwani bị truy tố; Theranos không bị truy tố hình sự) | — |
| 48 | §5 (c) | K | — | Không có tên nào ngoài Holmes, Balwani, Thẩm phán Davila (grep tên các nhà đầu tư, kiểm soát viên, vị tướng, nhân chứng tr. 32, tên hãng dược: 0 kết quả) |
| 49 | §5 (d) | K | N1 tr. 7 ("nothing more than a mirage"), tr. 8 ("half-truths and outright lies") | Không có "fraudster/scammer…" ở giọng kể |
| 50 | §5 (e) câu Walgreens | K | N4, N2/N3 (bị đơn / bị cáo); N1 tr. 17 (nạn nhân được bồi hoàn) | — |
| 51 | §5 (e) câu Safeway và Walgreens | K | N1 tr. 17 ("two other victims, Safeway and Walgreens") | — |
| 52 | §5 (e) câu hãng dược | K | N1 tr. 14 ("neither independently validated… nor authorized the use of their company logo") | — |
| 53 | §5 (e) câu quân đội | K | N4; N2/N3 | — |
| 54 | §5 (e) câu nhà đầu tư/HĐQT/nhân vật nổi tiếng | K | N4; N2/N3; N4 và N7 (Balwani là thành viên HĐQT nên vế "Apart from Holmes and Balwani" cần và đúng) | — |
| 55 | §5 (f) | K | N6 và N8 có chi tiết lối sống, động cơ; dàn truyện không dùng | Ngoại lệ ở nhịp 1, xem dòng 16 |
| 56 | §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32; N8 | — |
| 57 | §5 phép thử "làm theo được" | K | — | Không có cách sửa máy, không giao thức trình diễn, không cách làm giả logo/báo cáo |
| 58 | §6 đơn giá | K | QUY-TRINH §6 | 0,40 USD/clip 8 s; 1,5 lượt trên 2 khe (khe dễ ~1,0); 0,4401; 155 từ/phút; 12.230 / 2.005 = 6,10; nhạc ~825 (chưa đo); NB2.1 không có khoá: đều khớp |
| 59 | §6 Veo | K | tính lại | 14 × 0,40 × 1,0 = 5,60 · 18 × 0,40 × 1,25 = 9,00 · 22 × 0,40 × 1,5 = 13,20 |
| 60 | §6 TTS | K | tính lại | 2.600 × 6,1 = 15.860 ≈ 15.900; × 0,4401 ≈ 6.980 ≈ 7.000; +25 % = 8.750; +50 % = 10.500. Ghi chú: bảng nhịp chạy tới 17:45, ~2.750 từ, ≈ 7.390 ký tự tính ở mức thấp, tức ước hiện tại thấp hơn khoảng 5 %, vẫn nằm trong dự phòng 15 % |
| 61 | §6 nhạc | K | tính lại | 3/4/5 × 825 = 2.475 / 3.300 / 4.125 |
| 62 | §6 tổng | K | tính lại | 9.475 ≈ 9.500 · 12.050 · 14.625 ≈ 14.600 |
| 63 | §6 trần đề xuất | K | tính lại | 9,00 × 1,15 = 10,35 ≈ 10,40 USD · 12.050 × 1,15 = 13.858 ≈ 14.000 |
| 64 | §3 khuôn 1 tập; "dài hơn tập 1 khoảng 1 phút" | KKĐ | QUY-TRINH §6: lời tập 1 thật là 12:55 | Không xác định được "tập 1" dùng mốc nào để so. Nếu so với lời thật 12:55 thì tập này dài hơn ~4–5 phút, không phải ~1 phút. **Đề nghị** ghi rõ mốc so ("so với khuôn dàn truyện tập 1 ~16 phút" hoặc "so với lời thật 12:55") |
| 65 | §7 N1 | K | sha256sum khớp; 54 tr. | — |
| 66 | §7 N2 (đã mở, 200, UA khai báo) | KKĐ | Chỉ có bản phiên chính tải sẵn | KKĐ (sec.gov không mở theo lệnh). Nội dung bản tải sẵn khớp mọi câu nhịp 12 |
| 67 | §7 N3 | KKĐ | như trên | KKĐ (sec.gov không mở theo lệnh). Nội dung khớp 2b, H2, 12, L1, L3 |
| 68 | §7 N4–N8 | K | API DOJ 200, 6 kết quả | Thứ tự N4–N8 khớp kho §8 |
| 69 | §7 N9 | K | 200; "Updated October 20, 2026"; 0 Holmes/Balwani | — |
| 70 | §7 N10 | KKĐ | — | sec.gov không mở theo lệnh |
| 71 | §7 N11 | K | 200 | — |
| 72 | §7 N12 | K | 200 | — |
| 73 | §7 N13 | KKĐ | — | sec.gov không mở theo lệnh |
| 74 | §7 N14 | K | 200 cả hai IRN; ngày dự kiến ra trại khớp | — |
| 75 | §7 N15 | KKĐ | — | sec.gov không mở theo lệnh; không dùng cho nhịp nào |
| 76 | §7 investor.gov ("chưa mở được") | KKĐ | — | Không mở (sec.gov / investor.gov); không dùng |
| 77 | §8 dòng 1 (kiểm lại trạng thái; Counts 3–5) | K | N9, N14 | Đúng cách xử lý: giữ "could not reach a verdict" |
| 78 | §8 dòng 2 (judgment N.D. Cal., lệnh chấp thuận dàn xếp SEC) | KKĐ | — | PACER không có trần; giữ "agreed to settle" là đúng |
| 79 | §8 dòng 3 (ảnh trang hồ sơ) | K | N1 tr. 1 (chỉ tên hai bị cáo), tr. 15 (đoạn phán quyết; phần trên có bệnh nhân và lý do tách phiên), tr. 54 ("AFFIRMED") | Ngoặc "không crop phần tên nhà đầu tư ở tr. 10" đặt cạnh tr. 15 gây khó hiểu. Nên tách: "tr. 15 chỉ đoạn 'A. Holmes's Conviction and Sentence'". Tr. 14 (tên hãng dược) cũng nên thêm vào danh sách "không dùng" |
| 80 | **Kiểm riêng (4) · Nhịp 3** | **S** | §0; §5(e) | Thẻ 7 ô nêu Walgreens (D), quân đội Mỹ (E), hãng dược (G), nhưng cột "Rà luật 8" chỉ ghi "Đạt", không có câu kèm, trái §0. **Sửa:** thêm một câu gộp trong cùng đoạn, vd "These were the indictment's allegations against Holmes and Balwani; Walgreens, the drug companies and the U.S. military were not accused of wrongdoing in these cases." (nguồn: N4; N2/N3; N1 tr. 8) |
| 81 | **Kiểm riêng (4) · Nhịp 7 (Walgreens)** | **S** | N1 tr. 14 | Nhịp nêu "email gửi Walgreens" nhưng chỉ có câu kèm cho hãng dược. **Sửa:** thêm câu Walgreens theo mẫu §5(e), hoặc bỏ tên ("in emails to a retail partner") |
| 82 | **Kiểm riêng (4) · Nhịp 10 (quân đội)** | **S** | N1 tr. 7 | Nhịp nêu "các sĩ quan cao cấp quân đội Mỹ"; câu gộp "investors, board members or prominent backers" không nhắc quân đội. **Sửa:** "Apart from Holmes and Balwani, none of the investors, board members, military officers or prominent backers was accused of wrongdoing in these cases." |
| 83 | **Kiểm riêng (4) · Nhịp 18 / L2 / D** | **S** | §4 | L2 nêu logo hãng lớn, đối tác bán lẻ, quân đội, nhân vật nổi tiếng, báo chí; D(4) nêu "Bộ Quốc phòng"; D(5) nêu tên Walgreens. Không có câu kèm nào. **Sửa:** ở nhịp 18 hoặc nói chung không tên ("a retail partner", "drug companies", "the military"), hoặc thêm một câu gộp: "None of the companies, the military, the investors or board members mentioned in this story was accused of wrongdoing in these cases." (N4; N2/N3) |
| 84 | **Kiểm riêng (4) · Nhà đầu tư (toàn bảng)** | **S** | §0 dòng 17; N1 tr. 12 ("investor-victim"), tr. 16 (12 nhà đầu tư là "victims") | §0 yêu cầu câu kèm ở mọi đoạn nêu nhà đầu tư, nhưng bảng chỉ có câu này ở nhịp 10. Nhà đầu tư lại xuất hiện ở các nhịp 2, 3, 4b, 5, 6, 6b, 8, 9, 14, 16, 17, nên quy tắc và bảng tự mâu thuẫn. **Sửa (chọn một):** (a) thêm câu ở lần nêu đầu (nhịp 2): "The investors in this story were victims; none was accused of wrongdoing." (N1 tr. 16), lặp lại ở nhịp 10, và sửa §0 thành "lần nêu đầu mỗi hồi"; hoặc (b) chèn câu ở mỗi đoạn như §0 đang ghi |

## Kiểm riêng (1)–(7)

1. **Phán quyết Holmes tách bạch: đạt.** H4, logline VI/EN, §0, nhịp 14 và thẻ 12 ô đều nêu đủ: kết án 4 (Count 1, 6–8), trắng án 4 (Count 2, 10–12), treo 3 (Counts 3–5), Count 9 bị công tố rút (N1 tr. 15). Không câu nào nói hoặc ám chỉ Holmes "defrauded patients". Nhịp 15 có câu nối "Holmes was acquitted of the patient counts". Lưu ý thêm ở nhịp 11 (dòng 29).
2. **Balwani chỉ theo bản án của ông: đạt.** Nhịp 15 dùng N1 tr. 15–16, N7, N8. Không gán kết luận của phiên này sang phiên kia. Ghi âm 12/2013 được ghi đúng là chỉ dùng ở phiên Holmes (N1 tr. 13, chú thích 2).
3. **Không tên: đạt.** Cả ghi chú nội bộ cũng không có tên bệnh nhân, nhà đầu tư, nhân chứng, kiểm soát viên hay vị tướng. Tên trại giam ở N14 chỉ là ghi chú, có dặn "không đưa lên hình".
4. **Câu "không liên quan": các câu mẫu đều đúng và có nguồn (dòng 50–54), nhưng chưa đặt đủ chỗ.** S ở các dòng 80–84.
5. **Luật 8:** (a) đạt · (b) đạt · (c) đạt · (d) đạt · (e) thiếu chỗ, xem (4) · (f) có một MH ở nhịp 1 ("claimed goal"), phần còn lại đạt.
6. **Không có hướng dẫn làm theo được: đạt.**
7. **Số trang dẫn: đạt.** Mọi trang N1 được dẫn đều có đúng đoạn được nêu. Không trích dẫn nào thuộc tr. 3–6.

## Không kiểm được (KKĐ)

- N2, N3: việc trang sec.gov "mở được, 200, UA khai báo". Nội dung đã đối chiếu với bản phiên chính tải sẵn và khớp.
- N10 (sec.gov/tcr), N13 (adviserinfo.sec.gov), N15 (complaint SEC): sec.gov không mở theo lệnh.
- investor.gov: không mở, dàn truyện cũng không dùng.
- Judgment N.D. Cal. và lệnh chấp thuận dàn xếp SEC của Holmes: cần PACER, chưa có trần.
- §3 "dài hơn tập 1 khoảng 1 phút": không xác định được mốc so sánh.

## Tổng

| K | MH | S | KKĐ | Tổng dòng |
|---|---|---|---|---|
| 69 | 1 | 6 | 8 | 84 |
