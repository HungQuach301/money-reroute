# Kiểm độc lập vòng 4 — dàn truyện `theranos-holmes` (tập 4)

> Tác tử kiểm độc lập · 01/11/2026 · đối tượng: `docs/dan-truyen/theranos-holmes.md` (141 dòng, bản trong cây làm việc tại thời điểm kiểm). Đối chiếu: `docs/HIEN-CHUONG.md` §3 (luật 1–8), §4, §5; `docs/QUY-TRINH-TAP.md` §6; `docs/kho-de-tai/theranos-holmes.md` (tra URL, dẫn chiếu kho).
> Không đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài việc ghi tệp này), `docs/kho-de-tai/kiem/**`, lịch sử git. Không gọi API trả tiền. Không sửa dàn truyện, không commit.

## Nguồn đã mở trong vòng này
| Mã | Đường mở | Kết quả |
|---|---|---|
| N1 | `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf` (LFS, `%PDF-1.6`, 54 tr.) | SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**. Đọc `pdftotext -layout` tr. 1–2, 7–17, 30–33, 52–54; số trang in = số trang PDF (đã xác nhận). Không dùng tr. 3–6 |
| N2, N3 | Bản phiên chính đã tải: `…/scratchpad/src/sec/lr-24069.html` (+ `.txt`), `2018-41.html` (+ `.txt`) | Đọc toàn văn bản lưu. **Không** tự tải sec.gov |
| N4–N8 | `https://www.justice.gov/api/v1/press_releases.json?parameters%5Btitle%5D=Theranos&pagesize=50` | HTTP 200; 6 kết quả (5 thông cáo kho §8 + "U.S. Government Seeks Information From Victims Of Theranos Frauds"); đọc body HTML |
| N9 | curl mặc định trang Clemency Grants Trump 2025– | HTTP 200; "Updated October 20, …"; 0 kết quả "Holmes"/"Balwani" |
| N11 | curl mặc định `https://brokercheck.finra.org/` | HTTP 200, tiêu đề "BrokerCheck - Find a broker, investment or financial advisor" |
| N12 | curl mặc định `https://reportfraud.ftc.gov/` | HTTP 200, tiêu đề "ReportFraud.ftc.gov" |
| N14 | curl mặc định BOP inmateloc JSON, 24965-111 và 24966-111 | HTTP 200, `Captcha:false`; Holmes — Bryan, projRelDate 02/22/2030; Balwani — Lompoc II, projRelDate 04/21/2033 |

## Kết luận
**Đạt có điều kiện — 1 MH, 3 S (2 lỗi gốc), không lỗi tầng ở phán quyết.** Bốn mảnh phán quyết Holmes tách bạch đúng (N1 tr. 15; N5; N6), Balwani chỉ theo bản án riêng (N1 tr. 16; N7; N8), không tên bệnh nhân/nhà đầu tư/nhân chứng/hãng dược ở bất kỳ dòng nào (kể cả ghi chú), cấu trúc "bảy câu kiểm" nhất quán, ước chi khớp QUY-TRINH §6 và tính lại đúng. Phải sửa trước khi duyệt: (1) dẫn nguồn trích "Pharmaceutical companies never validated…" sai cho N2 ở nhịp 7 (thực ở N1 tr. 8); (2) Hồi 1 thiếu câu kèm "nhà đầu tư không bị cáo buộc" dù §0 đặt quy tắc "lần nêu đầu mỗi hồi" (nhịp 3 nêu nhà đầu tư, câu kèm gộp không có). Nên sửa: nhịp 4 nói "các xét nghiệm khác" rộng hơn nguồn.

## Bảng chấm
| Dòng | Điểm | Nguồn + trang | Ghi chú / sửa |
|---|---|---|---|
| Đầu tệp (quy ước trang, ký hiệu tầng, dòng 3–11) | K | N1 tr. 15–16; N7; N8 | Quy ước trang đúng; Summary tr. 3–6 không bị dẫn ở đâu khác ngoài dòng quy ước |
| §0 b1 (bốn mảnh phán quyết) | K | N1 tr. 15 ("dismissed Count 9… acquitted… Count 2… 10–12… convicted… Count 1… 6–8… hung… 3–5"); N5 | Đúng từng số tội |
| §0 b2 (Balwani theo bản án riêng; không lý do tách phiên) | K | N1 tr. 9, 15, 16; N7; N8 ("former romantic partner") | 12/12 = 2 âm mưu + 10 wire fraud ✓ |
| §0 b3 (không tên) | K | N1 tr. 10, 12, 13 nêu tên | Kiểm toàn tệp: không có tên nhà đầu tư, kiểm soát viên, tướng, nhân chứng, hãng dược, quan chức SEC |
| §0 b4 (quy tắc câu không liên quan) | **S** (tự mâu thuẫn) | — | Nói "lần nêu đầu **mỗi hồi** (H5, nhịp 4b, nhịp 12)" nhưng bỏ Hồi 1 (nhịp 1–3), trong khi nhịp 3 nêu "lời khai sai với nhà đầu tư". Sửa cùng lỗi ở dòng nhịp 3 câu kèm |
| §0 b5 (cơ chế) | K | N1 tr. 12 ("null protocol" có trong nguồn, dàn không dùng) | |
| §0 b6 (bảy câu kiểm) | K | N1 tr. 10–11 (A)–(G) | Khớp H5, nhịp 3, 4–10 (xem mục kiểm riêng 8) |
| Logline VI | K | N6 ("induce dozens of investors… hundreds of millions"); N1 tr. 7, 15–16, 54 | |
| Logline EN | K | N1 tr. 7, 15; N6 | "acquitted her on the patient counts" — N1 tr. 15 dùng đúng cụm "the patient-related counts" cho Count 2, 10–12. Đề xuất (không bắt buộc): "on the four patient counts" cho đồng nhất với H4, vì Count 9 (bệnh nhân) bị rút, không trắng án |
| H1 | K | N1 tr. 7 ("[O]ne tiny drop changes everything." … "the vision shared by…") | Chữ trích đúng nguyên văn |
| H2 | K | N1 tr. 7 ("In the early 2010s, Theranos claimed…"); N3 ("Silicon Valley-based") | |
| H3 | K | N6 ("was able to induce dozens of investors… to invest hundreds of millions of dollars") | ●D có chủ thể DOJ |
| H4 | K | N1 tr. 15; N5; ngày: N6/N7 ("On January 3, 2022") | Đề xuất thêm N6 vào cột nguồn cho vế "January 2022" (N1 tr. 15 và thân N5 không ghi ngày phán quyết) |
| H5 + câu kèm | K | N1 tr. 16 ("twelve investors… were 'victims'"); N4 (chỉ Holmes, Balwani bị truy tố) | Câu kèm trong cùng đoạn mở với H3 |
| Ghi chú §1 | K | — | |
| Nhịp 0 | K | §1 | |
| Nhịp 1 | K | N1 tr. 8 (2003, CEO tới 2018, "claimed goal"), tr. 9 (Edison; Balwani 2009, President/COO) | Không nhắc quan hệ riêng ✓ |
| Nhịp 2 | K | N1 tr. 10 (Walgreens thu 2013; C-1 cuối 2013; C-2 2014; "not publicly traded") | |
| Nhịp 2 câu kèm Walgreens | K | N1 tr. 8, 17 ("two other victims, Safeway and Walgreens"); N4; N2 | |
| Nhịp 2b | K | N3 (Peikin, Co-Director Enforcement: "no exemption… non-public, development-stage, or the subject of exuberant media attention") | "an SEC enforcement official" đúng chức danh |
| Nhịp 3 | K | N1 tr. 10–11 ("The Indictment alleged… (A)…(G)") | ◐ đúng: phân loại của cáo trạng |
| Nhịp 3 câu kèm gộp | **S** (thiếu theo quy tắc tự nêu) | N4; N2; N1 tr. 16 | Là lần nêu nhà đầu tư đầu tiên của Hồi 1 nhưng câu gộp chỉ có Walgreens, hãng dược, quân đội. **Sửa:** "These were the indictment's allegations against Holmes and Balwani; the investors, Walgreens, the drug companies and the U.S. military were not accused of wrongdoing in these cases." và thêm "Hồi 1 (nhịp 3)" vào danh sách §0 b4 và §5 (e) |
| Nhịp 4 | **MH** (nhẹ) | N1 tr. 10 ("Other 'general chemistry tests' conducted by Theranos were run on third-party-manufactured machines"), tr. 11 | "300 xét nghiệm… chỉ 12 chạy trên Edison; **các xét nghiệm khác** chạy trên máy hãng thứ ba" ngụ ý 288 xét nghiệm còn lại đều chạy trên máy hãng khác; nguồn chỉ nói "other general chemistry tests conducted". **Sửa:** "các xét nghiệm hoá sinh thông thường khác mà Theranos thực hiện được chạy trên máy do hãng thứ ba sản xuất, một số đã bị sửa". Vế nhân viên khai ✓ tr. 11 |
| Nhịp 4b | K | N1 tr. 12 ("Multiple investors testified…") | |
| Nhịp 4b câu kèm | K | N1 tr. 16; N4 | Lần nêu đầu Hồi 2 ✓ |
| Nhịp 5 | K | N1 tr. 12 ("VIP" guests… "surreptitiously run on third-party devices") | Không "null protocol" ✓ |
| Nhịp 6 | K | N1 tr. 12 (0 doanh thu 2012–2013; lỗ $57M/$92M; 11/2013 $15M, $2M/tuần; IRS $1,944,948; dự báo lãi $230M cuối 2015) | Tách lời khai/toà thuật lại đúng |
| Nhịp 6b | K | N6 ("zero revenue in 2012 and 2013… over $100 million… 2014… nearly $1 billion in 2015"); N5 | |
| Nhịp 7 (nội dung) | K | N1 tr. 14 ("Holmes admitted that she personally affixed…"; email Walgreens; đại diện các hãng khai; "vouching") | Hãng dược không tên ✓ |
| Nhịp 7 (cột nguồn) | **S** (dẫn sai nguồn) | Câu "Pharmaceutical companies never validated the technology, as Holmes and Balwani had told investors" là **N1 tr. 8**, không có trong N2 (bản lưu lr-24069) | **Sửa:** "N1 tr. 14; tr. 8 ("Pharmaceutical companies never validated the technology, as Holmes and Balwani had told investors"); câu kèm Walgreens: N1 tr. 17; N4; N2" |
| Nhịp 7 câu kèm (hãng dược, Walgreens) | K | N1 tr. 14 ("neither independently validated… nor authorized the use of their company logo"), tr. 17; N4 | |
| Nhịp 8 | K | N1 tr. 12–13 ($200M "from the Department of Defense"; tướng khai never in field / never on military medevac / never used on battlefield; cuộc gọi 12/2013 — trích khớp nguyên văn) | Vị tướng không tên ✓ |
| Nhịp 8 câu kèm quân đội | K | N4; N2 (suy từ danh sách bị đơn) | Cột nguồn không ghi nguồn cho câu kèm (các nhịp khác ghi "N4; N2"). Đề xuất thêm "câu kèm: N4; N2" |
| Nhịp 9 | K | N1 tr. 13–14 (đại diện Walgreens: "expanding… actually contracting… pilot program was not going as hoped"); N6 ("from a few dozen to 900… stagnating") | |
| Nhịp 9 câu kèm | K | N1 tr. 17; N4; N2 | |
| Nhịp 10 | K | N1 tr. 7 ("captivated"; "major companies, investors, and prominent figures, including high-ranking members of the United States military"); N6 ("In its memorandum filed for the sentencing hearing… By the end of 2014, her stock… more than $4 billion"; bìa tạp chí) | Vế 4 tỷ là lập luận trong bản ghi nhớ tuyên án mà DOJ thuật lại, không phải "bằng chứng xét xử" theo định nghĩa ●D ở đầu tệp; lời đã có chủ thể "prosecutors said" nên không nâng tầng. Đề xuất ghi chú ●D bao cả "bản ghi nhớ tuyên án" |
| Nhịp 10 câu kèm | K | N4 (chỉ Holmes, Balwani bị truy tố); N2 (SEC kiện Theranos, Holmes, Balwani) | Balwani là thành viên HĐQT (N7) — câu "Apart from Holmes and Balwani…" vẫn đúng |
| Nhịp 11 | K | N1 tr. 7–8 (news late 2015), tr. 11 (CMS, unannounced, "immediate jeopardy"), tr. 31 (nhận đầu 2016), tr. 32 (voided all patient tests run on the Edison) | Không tên nhân chứng ✓ |
| Nhịp 12 | K | N2/N3 bản lưu (14/03/2018; >$700M; "elaborate, years-long fraud"; $500.000; cấm 10 năm; 18,9 triệu cổ phần; chuyển Class B→A; "subject to court approval"; "neither admitted nor denied"; "will litigate its claims against Balwani") | ◐ đúng; "agreed to pay" ✓. Việc trang sec.gov mở được 200 → KKĐ |
| Nhịp 12 câu kèm | K | N1 tr. 16; N4 | Lần nêu đầu Hồi 3 ✓ |
| Nhịp 13 | K | N1 tr. 8 (điều tra hai năm rưỡi), tr. 15 (cuối 2021 / đầu 2022 / gần bốn tháng); N4 (06/2018); N5 (July 28, 2020 superseding indictment) | |
| Nhịp 14 | K | N1 tr. 15; N5 (">$140 million"); N6 ("On January 3, 2022") | Bốn mảnh, nhãn ● chỉ 4 ô ✓ |
| Nhịp 15 | K | N1 tr. 15 (bệnh nhân khai; "evidence linked Balwani to the transmission of these inaccurate results"), tr. 16 (all counts); N7 ("patients who paid for Theranos' blood testing services"; "separate jury" — N7 phần Holmes); N8 (July 7, 2022; 155 tháng; 3 năm) | Câu nối "Holmes was acquitted of the patient counts." — xem ghi chú Logline EN |
| Nhịp 16 | K | N6 (18/11/2022; Davila; 135 tháng; 3 năm; "No fine"; "ordered to surrender on April 27, 2023"); N1 tr. 15 ($120M), tr. 16–17 (05/2023; $452M liên đới; $397M; $54,5M Safeway, Walgreens) | |
| Nhịp 16 câu kèm Safeway/Walgreens | K | N1 tr. 17; N4; N2 | |
| Nhịp 17 | K | N1 tr. 2 ("Filed February 24, 2025"), tr. 8 ("We affirm."), tr. 53 ("[un]able to liquidate"; trích nhà đầu tư khớp nguyên văn), tr. 54 ("affirm… restitution order in its entirety… AFFIRMED") | |
| Nhịp 17 trạng thái | K | N14 (curl 01/11/2026: 02/22/2030; 04/21/2033); N9 (0 kết quả) | |
| Nhịp 18 + câu kèm | K | §4; N4; N2; N1 tr. 8, 16–17 | |
| Ghi chú dưới bảng nhịp (MH; lời người thật) | K | N1 tr. 7, 9 ("ultimately all roads"), 13, 53; N3 | |
| §3 khuôn tập | K | QUY-TRINH §6 (12:55); `docs/dan-truyen/1inmm-horwitz.md` (~16 phút) | |
| Cú treo câu 1 | K | N6 (memo; "more than $4 billion") | |
| Cú treo câu 2 | K | N1 tr. 11 ("unannounced inspection… in late 2015") | |
| L1 | K | N1 tr. 10, 53; N3 | |
| L2 | K | N1 tr. 7, 13–14; N6 | |
| L3 | K | N1 tr. 12; N3 (Jina Choi, Director SF Regional Office — trích khớp nguyên văn) | "quan chức SEC" đúng |
| D (5 dấu hiệu) | K | N1 tr. 12, 13, 13–14, 14 | Dấu hiệu (4): $200M ở đầu tr. 13 ✓ |
| P | K | N11, N12 (200); N10, N13 → KKĐ | Không sản phẩm/tỷ trọng |
| Thẻ tổng kết | K | N1 tr. 53; N10 (KKĐ) | Không nhắc bệnh nhân/phán quyết ✓ |
| §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | |
| §5 (b) | K | N2; N4 | |
| §5 (c) | K | — | Thẩm phán được nêu tên trong vai công vụ — không thuộc (c) |
| §5 (d) | K | N1 tr. 7 ("mirage"), tr. 8 ("half-truths and outright lies") | |
| §5 (e) | **S** (cùng lỗi gốc §0 b4) | — | Dòng "Nhà đầu tư (lần nêu đầu mỗi hồi)" — bổ sung Hồi 1 (nhịp 3) |
| §5 (f) | K | N1 tr. 9, 15; N6 (lối sống) | |
| §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32; N8 | |
| §5 phép thử | K | — | Không có bước làm theo được |
| §6 đơn giá | K | QUY-TRINH §6 (0,40 USD/8 s; 1,5 lượt/khe; 0,4401; 155 từ/phút; 825 ký tự/phút chưa đo; 12.230/2.005 = 6,10) | |
| §6 phép tính | K | tính lại | 5,60/9,00/13,20 USD; 15.860→6.998≈7.000; 8.750; 10.500; nhạc 2.475/3.300/4.125; tổng ≈9.475/12.050/14.625; trần 10,35≈10,40 USD; 13.858≈14.000 ✓ |
| §6 "MR-D4 chi 0 USD" | KKĐ | — | Không đọc reports |
| §7 N1 | K | tệp repo, LFS, SHA khớp | |
| §7 N2, N3, N10, N13, N15 | KKĐ | — | sec.gov không mở theo lệnh |
| §7 N4–N8 | K | DOJ API 200, 6 kết quả | |
| §7 N9 | K | curl 200 | |
| §7 N11, N12 | K | curl 200 | |
| §7 N14 | K | curl 200 | |
| §7 Investor.gov 403 | KKĐ | — | Không thử lại |
| §8 b1 (kiểm trạng thái) | K | kho §5 | |
| §8 b2 (judgment, PACER hoãn K5) | K | NHAT-KY MR-D23 (K5 hoãn PACER) | |
| §8 b3 (trang được/không được chụp) | K | N1 tr. 1, 9, 10, 12–15, 54 | tr. 15 đoạn phán quyết không có tên; tr. 14 có tên hãng dược ✓ |
| §8 b4 (trích nhịp 8 nguyên văn) | K | N1 tr. 13 | |

## Kiểm riêng
1. **Phán quyết Holmes:** tách bạch ở logline VI/EN, H4, §0 b1, nhịp 14 (kết án Count 1, 6–8; trắng án Count 2, 10–12; treo 3–5; Count 9 rút — N1 tr. 15). Không dòng nào nói/ám chỉ Holmes bị kết án lừa bệnh nhân; nhịp 15 có câu nối trắng án. **Đạt.**
2. **Balwani:** chỉ theo bản án riêng (N1 tr. 16; N7; N8), "separate trial · separate jury". **Đạt.**
3. **Không tên** bệnh nhân/nhà đầu tư/nhân chứng/hãng dược/quan chức trong toàn tệp (grep 14 tên trong nguồn: 0 kết quả). **Đạt.**
4. **Câu không liên quan:** nội dung đúng chủ thể, có nguồn (N4, N2, N1 tr. 14, 16, 17). Lệch quy tắc tự nêu: Hồi 1 thiếu câu nhà đầu tư (S); nhịp 8 thiếu ghi nguồn câu kèm (đề xuất).
5. **Luật 8 (a)–(f):** đạt. (a) Holmes ●; (b) ◐ chỉ cho Theranos/vụ SEC; (c) không tên; (d) không nhãn, lời mạnh của toà chỉ làm chữ trích; (e) xem mục 4; (f) không quan hệ riêng, lý do tách phiên, lối sống.
6. **Không hướng dẫn làm theo được:** đạt.
7. **Số trang:** đúng ở mọi dòng; lỗi duy nhất là gán trích dẫn tr. 8 cho N2 ở nhịp 7 (S).
8. **Bảy câu kiểm:** §0 (6 từ 7 nhóm, (A)+(F) gộp Kiểm 1, Kiểm 7 = K), H5 ("7 checks"), nhịp 3 ("6 from the indictment's categories + 1 lesson"), nhịp 4 (A+F), 5 (C), 6 (B), 7 (G), 8 (E), 9 (D), 10 (K) — **nhất quán.**

## Không kiểm được
- N2, N3, N10, N13, N15: việc trang sec.gov mở được HTTP 200 (sec.gov không mở theo lệnh; nội dung N2/N3 đối chiếu bằng bản lưu của phiên chính).
- Investor.gov (403) — không thử lại.
- §6 "MR-D4 chi 0 USD" (không đọc reports).

## Tổng đếm
| Điểm | Số dòng |
|---|---|
| K | 72 |
| MH | 1 (nhịp 4) |
| S | 4 dòng — 2 lỗi gốc: (i) nhịp 7 cột nguồn; (ii) Hồi 1 thiếu câu kèm nhà đầu tư (§0 b4, nhịp 3 câu kèm, §5 (e)) |
| KKĐ | 3 (§6 chi 0 USD; §7 nhóm sec.gov; §7 Investor.gov) |
| **Tổng** | **80** |
