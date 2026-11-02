# Kiểm độc lập — dàn truyện `theranos-holmes` · vòng 10

> Tác tử kiểm độc lập · 02/11/2026 · chỉ đọc `docs/HIEN-CHUONG.md` §3, `docs/dan-truyen/theranos-holmes.md` và nguồn; **không** đọc `reports/**`, các biên bản kiểm khác, lịch sử git. Không sửa dàn truyện, không commit.
> Thang điểm: **K** = khớp nguồn và tầng · **MH** = mạnh hơn nguồn/tầng · **S** = sai, tự mâu thuẫn hoặc gán sai nguồn/tầng. Chỉ chấm MH/S khi có căn cứ cụ thể; gợi ý văn phong ghi riêng ở cuối.

## Nguồn đã đối chiếu
| Mã | Tệp / đường | Kiểm |
|---|---|---|
| N1 | `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf` | SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**; `pdftotext -layout -f P -l P` các tr. 1–2, 7–17, 30–33, 52–54; số trang in = số trang PDF (đã thấy ở đầu trang). Không dùng tr. 3–6 (Summary). |
| N2, N3 | bản đã tải sẵn trong scratchpad (`lr-24069.html/.txt`, `2018-41.html/.txt`) | đọc văn bản; **không** tải lại sec.gov |
| N4–N8 | API DOJ `press_releases.json?parameters[title]=Theranos&pagesize=50` | HTTP 200, 6 kết quả; N4 = cáo trạng (15/06/2018), N5 = phán quyết Holmes, N7 = phán quyết Balwani, N6 = tuyên án Holmes (18/11/2022), N8 = tuyên án Balwani (07/12/2022); bản "Seeks Information From Victims" không dùng |

Mốc trang N1 dùng khi chấm: tr. 7–8 phần mở đầu opinion; "Factual Background" bắt đầu tr. 8; "D. Scheme to Defraud Patients" tr. 14–15; "Procedural History" tr. 15–17; phân tích CMS tr. 30–32 (tr. 30 chủ yếu là lập luận của Holmes); "Voiding Results" tr. 32–33; bồi hoàn tr. 52–54.

## Bảng chấm

| # | Dòng | Điểm | Nguồn + trang | Ghi chú |
|---|---|---|---|---|
| 1 | Định nghĩa **●C** (đầu tệp, dòng 8) | **S** | N1 tr. 7–8, 8–17, 30–33, 53 | Định nghĩa chỉ bao sự việc **do toà phúc thẩm thuật lại trong opinion**. Nhưng nhãn ●C đang được gắn cho cả vế lấy từ nguồn ngoài opinion: (i) H2 vế "Silicon Valley" — từ N3 (SEC), N1 tr. 7 không nói Theranos đặt ở Thung lũng Silicon (chỉ "Silicon Valley spectators"); (ii) câu kèm "not accused of wrongdoing in these cases" — vế "không bị cáo buộc" dựa vào N4 (cáo trạng chỉ nêu Holmes, Balwani) và N2 (SEC chỉ kiện Theranos, Holmes, Balwani), được ghi "câu kèm = ●C" ở H5 và nằm dưới cột tầng ●C ở nhịp 2, 4b, 7, 8, 9. Nội dung đúng; lỗi là nhãn không khớp định nghĩa của chính tệp. **Sửa:** thêm vào Ký hiệu: "Câu kèm 'không bị cáo buộc' = **TT** (N1 tr. 8; N4; N2) — vế 'court treated … as victims' = ●C (N1 tr. 16–17)"; H2 đổi tầng thành "●C / NB (N3: 'Silicon Valley-based')". Các dòng ●C còn lại (nhịp 1, 2, 4–11, 15, 17, L1, L2, D) đều dẫn trang nằm trong phạm vi định nghĩa. Nhịp 13 **không** mang ●C (tầng TT/◐) — không phải lỗi. |
| 2 | H1 (chữ trích "[O]ne tiny drop changes everything.") | K | N1 tr. 7 | Đúng nguyên văn; toà gọi là "the vision shared by…". |
| 3 | H2 | **S** (nhãn) | N1 tr. 7; N3 | Câu đúng nguồn (tr. 7: "In the early 2010s, Theranos claimed that it could run fast, accurate, and affordable tests with just a drop of blood…"); vế "a Silicon Valley company" chỉ có ở N3 ("Silicon Valley-based private company") → không thuộc ●C. **Sửa:** tầng "●C / NB (N3)" hoặc bỏ "Silicon Valley" khỏi câu ●C. |
| 4 | H3 | K | N6 ("was able to induce dozens of investors, many of whom were prominent public figures, to invest hundreds of millions of dollars") | ●D, có chủ thể DOJ, thông cáo sau bản án. |
| 5 | H4 | K | N1 tr. 15; N5; N6 ("On January 3, 2022…") | Tách đúng: kết án 4 (Count 1 âm mưu + 3 wire fraud — Counts 6–8), trắng án 4 bệnh nhân (Count 2; 10–12), treo 3 nhà đầu tư (Counts 3–5); "the same jury" đúng; tháng 1/2022 đúng. |
| 6 | H5 — câu kèm "…the court treated twelve of them as victims." | **S** (nhãn) | N1 tr. 16 ("twelve investors … were 'victims' under the MVRA"); N4; N2 | Nội dung đúng (toà sơ thẩm xác định 12 nhà đầu tư là "victims"). Nhãn "câu kèm = ●C" sai một nửa: vế "not accused of wrongdoing in these cases" dựa vào N4/N2, không phải opinion. **Sửa:** "câu kèm = TT (không bị cáo buộc — N1 tr. 8; N4; N2) + ●C (12 nạn nhân — N1 tr. 16)". |
| 7 | Logline VI | K | N6; N1 tr. 15–16, 54; N5 | "theo DOJ" có chủ thể; ba vế tách đúng; 135 tháng (tr. 16; N6); phúc thẩm giữ nguyên 2025 (tr. 2, 54). |
| 8 | Logline EN | K | N1 tr. 7, 15, 16–17; N5; N6 | Tách đúng 4 / 4 / 3, năm 2022. Vế "investors put in hundreds of millions" không có chủ thể nhưng được toà xác nhận (bồi hoàn 397 triệu USD = tiền 12 nạn nhân đã đầu tư, tr. 16–17). |
| 9 | Nhịp 1 | K | N1 tr. 8–9 | 2003; CEO tới 2018; "Holmes's claimed goal"; Edison "miniaturized device"; Balwani vào 2009, sau là President và COO. |
| 10 | Nhịp 2 | K | N1 tr. 10, 17; N4; N2 | Walgreens mùa thu 2013, C-1 cuối 2013, C-2 2014, "Theranos shares were not publicly traded" (tr. 10). Câu kèm Walgreens: tr. 17 ("two other victims, Safeway and Walgreens"). Nhãn câu kèm: xem dòng 1. |
| 11 | Nhịp 2b | K | N3 (Steven Peikin, Co-Director, Enforcement Division) | "an SEC enforcement official said in 2018" khớp chức danh. |
| 12 | Nhịp 3 + câu gộp | K | N1 tr. 10–11; tr. 8; N4; N2 | Bảy nhóm (A)–(G) đúng thứ tự, "generally fell" đúng; ◐ đúng. Câu gộp "These were the indictment's allegations against Holmes and Balwani; the investors, Walgreens, the drug companies and the U.S. military were not accused…" đúng chủ thể (cáo trạng chỉ nêu Holmes, Balwani — tr. 8; N4). |
| 13 | Nhịp 4 | K | N1 tr. 10, 11 | 300 / 12 (tr. 10); "general chemistry tests" trên máy hãng thứ ba, "various modifications" (tr. 10); QC liên tục trượt, báo Holmes/Balwani, "dismissed … or shifted blame" (tr. 11). |
| 14 | Nhịp 4b | K | N1 tr. 12 | "Multiple investors testified … solely on devices manufactured by Theranos … would have impacted their investment decisions." |
| 15 | Nhịp 5 | K | N1 tr. 12 | "VIP guests, including investors … led to believe … some of the VIP samples were surreptitiously run on third-party devices." |
| 16 | Nhịp 6 | K | N1 tr. 12 | Controller: 0 doanh thu 2012–2013, lỗ 57/92 triệu; 11/2013 15 triệu tiền mặt / 2 triệu mỗi tuần; IRS 2015: 1.944.948 USD; nhà đầu tư khai dự báo lãi 230 triệu cuối 2015. Đoạn "toà thuật tiếp, không thuộc lời khai" tách đúng. |
| 17 | Nhịp 6b | K | N6 ("Holmes misrepresented to other investors that Theranos, which had zero revenue in 2012 and 2013, was projected to generate over $100 million in revenue in 2014 and to reach nearly $1 billion in 2015"); N5 | ●D, có chủ thể. |
| 18 | Nhịp 7 — sự việc | K | N1 tr. 14; tr. 8 | "Holmes admitted that she personally affixed the logo…"; email gửi Walgreens "independent and technical validation"; đại diện các hãng "neither independently validated … nor authorized the use of their company logo"; nhà đầu tư "found it significant". Câu tr. 8 trích đúng. |
| 19 | Nhịp 7 — nhãn "LOGOS ADDED — Holmes admitted it, per the appeals court (9th Cir. 2025)" | K | N1 tr. 14 | Đúng chủ thể (Holmes thừa nhận) và đúng nguồn (toà phúc thẩm thuật lại). Không mạnh hơn nguồn. |
| 20 | Nhịp 7 — câu kèm (hãng dược; Walgreens) | K | N1 tr. 14, 17; N4; N2 | Hãng dược không tên; vế "representatives testified they did not authorize their logos on these reports" đúng tr. 14; Walgreens "victim owed restitution" đúng tr. 17. |
| 21 | Nhịp 8 | K | N1 tr. 12–13 | 200 triệu từ DoD (nhà đầu tư khai, tr. 12–13); vị tướng: "never put into the field … never installed on a military medevac … never used to treat servicemembers on the battlefield"; trích ghi âm 12/2013 đúng nguyên văn; "At Holmes's trial" đúng. |
| 22 | Nhịp 9 | K | N1 tr. 13–14; N6 | Đại diện Walgreens khai "expanding … actually contracting, and the pilot program was not going as hoped"; vế 900 = ●D: N6 "from a few dozen to 900, despite knowing that the relationship with Walgreens was stagnating". |
| 23 | Nhịp 10 | K | N1 tr. 7; N6 | "captivated", "relationships with major companies, investors, and prominent figures, including high-ranking members of the United States military"; 4 tỷ USD cuối 2014 và bìa tạp chí nằm trong đoạn "In its memorandum filed for the sentencing hearing…" → "prosecutors said" đúng. |
| 24 | Nhịp 10 — câu kèm "Apart from Theranos, Holmes and Balwani, none of the other companies…" | K | N4 (chỉ Holmes, Balwani bị truy tố); N2 (SEC kiện Theranos, Holmes, Balwani) | Đúng chủ thể. Balwani từng là thành viên HĐQT (N4) — đã được loại trừ bởi "Apart from…", không mâu thuẫn. |
| 25 | Nhịp 11 | K | N1 tr. 7–8, 11, 31, 32–33 | Báo chí cuối 2015 (tr. 7–8); CMS thanh tra không báo trước cuối 2015, "immediate jeopardy" (tr. 11); Theranos nhận báo cáo đầu 2016 (tr. 31 — lời toà, không phải tr. 30 lập luận của Holmes, đúng). Vế "voided all patient tests run on the Edison" nằm trong câu toà mô tả lập luận của Holmes (tr. 32) — xem gợi ý cuối. |
| 26 | Nhịp 12 | K | N2; N3 | 14/03/2018; "more than $700 million"; dàn xếp không thừa nhận; 500.000 USD "agreed to pay"; cấm 10 năm; 18,9 triệu cổ phần; bỏ quyền biểu quyết chi phối; "subject to court approval"; SEC kiện tiếp Balwani. |
| 27 | Nhịp 13 | K | N1 tr. 8, 15; N4; N5/N6 | Truy tố 14/06/2018 (N4 ngày 15/06, "returned yesterday"; N6 "June 14, 2018"); thay thế 28/07/2020 (N5); xử riêng, Holmes cuối 2021, Balwani đầu 2022, gần bốn tháng (tr. 15). Tầng TT, không phải ●C. |
| 28 | Nhịp 14 | K | N1 tr. 15; N5; N6 | Bốn mảnh đúng; "wire transfers totaling more than $140 million" (N5, N6); Count 9 "the government dismissed" (tr. 15). |
| 29 | Nhịp 15 + câu nối | K | N1 tr. 15–16; N7; N8 | 07/07/2022 cả 12 tội; "patients who paid for Theranos' blood testing services" (N7); bệnh nhân khai nhận kết quả sai, "evidence linked Balwani to the transmission" (tr. 15); 155 tháng, 3 năm giám sát, 07/12/2022 (N8). Câu nối đúng (tr. 15; N5). |
| 30 | Nhịp 16 | K | N1 tr. 15–17; N6 | 18/11/2022; Davila; 135 tháng; 3 năm giám sát; "No fine was assessed"; "ordered to surrender on April 27, 2023"; 120 triệu thiệt hại lượng hình (tr. 15); bồi hoàn 05/2023, liên đới 452 / 397 / 54,5 triệu (tr. 16–17). |
| 31 | Nhịp 17 | K | N1 tr. 2, 8, 52–54 | Giữ nguyên bản án, mức án ("We affirm.", tr. 8) và "restitution order in its entirety" (tr. 54). "[un]able to liquidate their shares" sau khi gian lận lộ ra là kết luận của toà sơ thẩm (tr. 53, dẫn Holmes II tại 1059); toà phúc thẩm thấy bằng chứng phía bị cáo "not enough to render the district court's finding clearly erroneous" → "giữ kết luận đó" đúng. Lời trích đúng nguyên văn; "One investor who testified at both trials". Xem gợi ý về chủ thể của "Lý do…" và tr. 52. |
| 32 | Nhịp 18 — câu gộp | K | N1 tr. 8, 16–17; N4; N2 | "Apart from Theranos, Holmes and Balwani, none of the companies, the U.S. military, the investors or the prominent backers mentioned in this story was accused…" nhất quán với nhịp 10 và nhịp 3; đúng chủ thể (Theranos chỉ bị SEC kiện; chỉ Holmes, Balwani bị truy tố). |
| 33 | Cú treo giữa tập | K | N6; N1 tr. 11 | Câu 1 "prosecutors said"; câu 2 "unannounced inspection … in late 2015". |
| 34 | §4 L1 | K | N1 tr. 10, 53; N3 | Từng vế đúng chủ thể: không giao dịch công khai (toà phúc thẩm thuật lại); toà sơ thẩm xác định không bán được sau khi gian lận lộ ra, toà phúc thẩm giữ; nguyên tắc chống gian lận "theo SEC" (Peikin). Phần cuối có nhãn "Lời của kênh". |
| 35 | §4 L2 | K | N1 tr. 7, 13–14; N6 | Logo (tr. 14), đối tác bán lẻ (tr. 13–14), quân đội (tr. 13), nhân vật nổi tiếng (tr. 7), báo chí (N6 ●D — bìa tạp chí). Vế đại diện hãng dược khai đúng tr. 14. |
| 36 | §4 L3 | K | N1 tr. 12; N3 (Jina Choi, Director, San Francisco Regional Office) | Lời trích SEC đúng nguyên văn; "quan chức SEC" đúng. |
| 37 | D(1) | K | N1 tr. 14 | Đúng. |
| 38 | D(2) | K | N1 tr. 12 | Đúng ("led to believe"). |
| 39 | D(3) | K | N1 tr. 12 | Đúng. |
| 40 | D(4) | K | N1 tr. 12–13 | Đúng (nhà đầu tư khai; vị tướng khai). |
| 41 | D(5) | K | N1 tr. 13–14 | "Walgreens thực tế thu hẹp": tr. 13–14 là lời khai của đại diện Walgreens, và toà cũng thuật như sự việc ("Walgreens's decision to reduce the number of stores…", tr. 14) → không mạnh hơn nguồn. Xem gợi ý. |
| 42 | Thẻ tổng kết — vế 1 "in this case, the court found the defrauded investors could not sell" | **MH** | N1 tr. 53 | Nguồn giới hạn thời điểm: toà sơ thẩm xác định nạn nhân "[un]able to liquidate their shares **after the fraud came to light**"; toà phúc thẩm còn ghi bằng chứng phía bị cáo gợi ý "some opportunity to sell shares to some parties at some unidentified time" (chỉ là không đủ để coi kết luận sai rõ ràng). "could not sell" không giới hạn rộng hơn nguồn. **Sửa:** "…the court found the defrauded investors could not sell their shares after the fraud came to light." |
| 43 | Thẻ tổng kết — các vế còn lại (2, 3, red flags, BrokerCheck/IAPD, sec.gov/tcr) | K | N1 tr. 12–14; N10; N11; N13 | Lời của kênh, mỗi dấu hiệu khớp một D(1)–D(5); không nhắc bệnh nhân/phán quyết. |
| 44 | §5(b) | K | N2; N4; N1 tr. 8 | Theranos chỉ bị SEC kiện (dàn xếp không thừa nhận); cáo trạng và mọi thông cáo DOJ N4–N8 chỉ nêu Holmes, Balwani là bị cáo. |
| 45 | §5(e) — các câu mẫu | K | N1 tr. 14, 16–17; N4; N2 | Câu "Apart from Theranos, Holmes and Balwani…" trùng nhịp 10; câu Walgreens/Safeway khớp tr. 17; câu hãng dược khớp tr. 14; nhất quán với §0 (nhịp 10, 18 dùng câu gộp). |
| 46 | §0 — ba phần phán quyết, Count 9, Balwani 12/12 | K | N1 tr. 15–16; N5; N7; N8 | Đúng. |

## Tổng đếm
**46 dòng: K 42 · MH 1 · S 3.**
- **S (3, cùng một gốc — nhãn, nội dung đúng):** định nghĩa ●C không bao vế lấy từ N3 (H2) và vế "không bị cáo buộc" của câu kèm lấy từ N4/N2 (ghi rõ ở H5; ngầm ở nhịp 2, 4b, 7, 8, 9).
- **MH (1):** thẻ tổng kết vế 1 bỏ giới hạn "after the fraud came to light".

## Gợi ý văn phong (không phải lỗi)
1. Nhịp 17: câu "Lý do bồi hoàn toàn bộ tiền đầu tư: …" chưa có chủ thể. Lý lẽ "không bán được → bồi hoàn toàn bộ" là của **toà phúc thẩm** (tr. 52–53: toà phúc thẩm thấy toà sơ thẩm sai khi không trừ giá trị còn lại của cổ phần, nhưng lỗi vô hại vì kết luận "[un]able to liquidate"). Đề xuất: "Toà phúc thẩm giải thích việc giữ bồi hoàn bằng toàn bộ tiền đầu tư: toà sơ thẩm đã xác định các nhà đầu tư bị hại không bán được cổ phần sau khi gian lận lộ ra…" và dẫn thêm N1 **tr. 52**.
2. Nhịp 11: vế "voided all patient tests run on the Edison" — câu ở tr. 32 là toà mô tả lập luận của Holmes; dẫn kèm tr. 33 ("allowed Das to testify regarding the voiding") để vế lời khai đứng trên lời của toà. N6/N8 cũng có "voided all tests with its analyzer" nhưng thuộc đoạn bản ghi nhớ tuyên án (●D) — không cần dùng.
3. D(5): thêm chủ thể cho đồng nhất với D(1)–D(4): "một đại diện Walgreens khai quan hệ thực tế đang thu hẹp (N1 tr. 13–14, ●C)". D(1), D(5) chưa ghi nhãn ●C như D(2)–D(4).
4. Định nghĩa ●C ghi "vd tr. 30–33" rồi loại "vd tr. 30" — nên ghi "tr. 31–33" cho gọn.
5. L1 tiêu đề VI ("không có thị trường công khai để thoát ra") tuyệt đối hơn thẻ EN ("may have no exit"); nên đồng bộ "có thể không có đường thoát".
