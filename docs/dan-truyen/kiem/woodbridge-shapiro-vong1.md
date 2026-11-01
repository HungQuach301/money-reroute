# Kiểm độc lập dàn truyện `woodbridge-shapiro` — vòng 1

- **Người kiểm:** tác tử kiểm độc lập (Claude Code, phiên con), theo lệnh của điều phối MR-2.
- **Ngày kiểm:** 01/11/2026.
- **Tệp được chấm:** `docs/dan-truyen/woodbridge-shapiro.md` (bản nháp MR-2 · M-b bước 1). Không sửa tệp này.
- **Đã đọc:** `CLAUDE.md`; `docs/HIEN-CHUONG.md` (v2, §1, §3 kể cả luật thi hành 5 và 8, §4, §5); tệp dàn truyện; `docs/ung-vien/woodbridge-shapiro/NGUON.md` (chỉ để tra mã nguồn → tệp/URL, không dùng phần tóm tắt làm bằng chứng); 12 PDF ở `ho-so/woodbridge-shapiro/` (lớp chữ bằng `pdftotext -layout`; ảnh trang 100 dpi cho mọi câu trích nguyên văn: N2 tr. 11, 22, 23, 25; N9 tr. 4, 5, 6, 7; N15 tr. 6); HTML SEC N1 (PR 2017-235 + LR-24020), N3 (PR 2019-3), N13 (PR 2019-55 + LR-24450) mở bằng curl với UA khai báo theo chính sách SEC.
- **Không đọc:** `reports/**`, `docs/ung-vien/*/TANG.md`, `RUI-RO.md`, `KIEM-TANG.md`, dàn truyện vụ khác, /tmp ngoài thư mục tạm của chính phiên này, git log/diff. Do đó các chỗ dàn truyện viện dẫn TANG/KIEM-TANG/RUI-RO **không được kiểm** ở đây.
- **Chưa mở được:** N7 (docket CourtListener 14944566) — HTTP 403 "Request blocked" (trang chặn); **không** thử vượt (không đổi UA, không mirror). Mọi câu chỉ dựa trên N7 → KKĐ. Không dùng justice.gov (không cần cho nhịp nào). Không gọi API trả tiền; chi 0 USD.

## 1. Nguồn đã mở

| Mã | Tệp / URL | Trang đã mở | SHA-256 (đo 01/11/2026) | Khớp NGUON |
|---|---|---|---|---|
| N2 | `sec-complaint-2017.pdf` (47 tr.) | 2, 3, 11, 12, 13, 14, 15, 16, 22, 23, 25 | `9e5c4388dce569a413b7b2790d87ff921fea9f5e3ab2b7f63445b06c7c39c8b6` | Khớp |
| N4 | `sec-final-judgment-shapiro-2018.pdf` (8 tr.) | 1, 5–8 | `34e7680adc6aafb9fc00774d2cfadafcfe1855d44735b912791e5cf6456c2f5c` | Khớp |
| N5 | `sec-final-judgment-woodbridge-2018.pdf` (9 tr.) | 1–2 | `9a99be3e193f7a5f0c73e8f12d85c4c1f113ef170b8c7d8fe2c22a9d86bfc9ff` | Khớp |
| N6 | `sec-admin-order-shapiro-2019.pdf` | (không cần cho nhịp nào; chỉ băm) | `2f7f5564368b2f1f5720c51c2710ec31fae41a7efbfe2034ba47ee5c7307cb2d` | Khớp |
| N8 | `plea-agreement-shapiro-2019.pdf` (18 tr.) | 1–3 | `351304b6ac9a070080145285ef9462e5b9fe7d218222c697988fe58d52655939` | Khớp |
| N9 | `factual-proffer-shapiro-2019.pdf` (9 tr.) | 1–9 | `6924f2a7af2f6656a4b5246fb9421d5e2958d356386717ece4620b0c6231df1e` | Khớp |
| N10 | `judgment-shapiro-2019.pdf` (6 tr.) | 1–3 | `90c25e81e497ca18dc1b9fadec4d3f4da6d90104bd34c61f58699af402ef24ca` | Khớp |
| N11 | `judgment-acevedo-2021.pdf` (7 tr.) | 1–2 | `f35e3e9d6680e3c551a181e97ecb5957bf8fc77b80eb6e8d448ec33c56f0575f` | Khớp |
| N12 | `ca11-opinion-shapiro-2024.pdf` (4 tr.) | 1–4 | `e1863399ba14bf523621b094ada65a40b811a107085ab2fae9fb576280dc2ec4` | Khớp |
| N14 | `sec-complaint-acevedo-roseman-2019.pdf` | (không cần; chỉ băm) | `4db52b6317d13139ed8f9b86333b8dc648a02663c8a4ffaa7d678313ed480a8d` | Khớp |
| N15 | `sec-final-judgment-roseman-2021.pdf` (7 tr.) | 1, 5–7 | `3ebbf43ad725bc07af847f398b90f2309392e00cfe830e829692a2f5b6081ea1` | Khớp |
| N16 | `sec-final-judgment-acevedo-2021.pdf` | (không cần; chỉ băm) | `1a59528c6c576d43a459ddf9255efc75ef55a749dd627728b546bf87b14af854` | Khớp |
| N1 | sec.gov/newsroom/press-releases/2017-235 ; …/lr-24020 | toàn văn | HTML, HTTP 200 (không lưu vào repo) | — |
| N3 | sec.gov/newsroom/press-releases/2019-3 | toàn văn | HTML, HTTP 200 | — |
| N13 | sec.gov/newsroom/press-releases/2019-55 ; …/lr-24450 | toàn văn | HTML, HTTP 200 | — |
| N7 | courtlistener.com/docket/14944566/… | — | **chưa mở được** (HTTP 403, trang chặn) | — |

12/12 PDF có SHA-256 khớp NGUON.md.

## 2. Bảng chấm từng nhịp

K = khớp · MH = mạnh hơn nguồn / tầng cao hơn · S = sai · KKĐ = không kiểm được.

| Nhịp | Khẳng định chính | Bằng chứng (≤ 25 từ) + trang thực tế | Tầng gán → đúng? | Điểm | Ghi chú |
|---|---|---|---|---|---|
| Logline VI | "…năm bang ra lệnh dừng mà việc bán vẫn tiếp tục — **cho tới khi** ông bị tuyên 25 năm tù" | N9 tr. 7: bán tiếp "through the filing of Woodbridge's bankruptcy in December 2017"; N10 tr. 1: tuyên "October 15, 2019" | ●T/● | **MH** | Câu đọc được là việc bán kéo dài tới lúc tuyên án; thực tế dừng 12/2017, tuyên án 10/2019. Phần còn lại K (N9 tr. 4–6) |
| Logline EN | Lãi đến mỗi tháng; người đứng sau sau này thừa nhận trước toà tiền thật đến từ đâu | N9 tr. 4 "short-term promissory notes that purportedly paid investors monthly interest"; tr. 6 "misused to pay … 'returns'" | ●T | K | "five years": tr. 4 "August 2012 through … December 2017" |
| H1 | Cảnh bàn bếp, sao kê, lãi đúng hạn | — (cảnh tổng hợp) | MH → đúng | K | Không mang sự việc pháp lý; nhãn ILLUSTRATIVE có |
| H2 | ~10.000 người, ~1,29 tỷ USD | N9 tr. 4: "approximately $1.29 billion from approximately 10,000 investors across the United States" | ●T → đúng | K | N9 tr. 7 lại ghi "more than approximately 9,000"; SEC ghi 8.400 (N1, N2 tr. 2). Xem khuyến nghị R1 |
| H3 | Được nói tiền cho vay có bất động sản bảo đảm, "safe" | N9 tr. 4: "misleadingly claimed that these investments were adequately secured by real property owned by third-party borrowers, and thus safe" | ●T → đúng | K | Đối chiếu ảnh trang tr. 4: trích đúng |
| H4 | Năm bang ra lệnh dừng; vẫn bán | N9 tr. 7: "at least five states … issued cease and desist orders … nonetheless continued to sell" | ●T → đúng | K | Nguồn ghi "at least five" và chủ ngữ bán tiếp là "SHAPIRO and his co-conspirators"; xem R2 |
| H5 | 2019 Shapiro thừa nhận tiền người mới trả "returns" người cũ; bị tuyên 25 năm | N9 tr. 6: "hundreds of millions of dollars invested by new investors were misused to pay false and misleading 'returns'"; N10 tr. 2: "term of 300 months" | ● / ●T → đúng | K | |
| H6 | Lời kênh | — | — | K | Không khẳng định về người thật |
| 0 | Móc câu H1–H6 | như trên | — | K | (tổng hợp) |
| 1 | Trụ sở ban đầu Boca Raton, sau Sherman Oaks; Shapiro chủ, chủ tịch, CEO, người ký duy nhất | N9 tr. 2 "owner, president, and chief executive officer"; tr. 3 "sole signatory on all of Woodbridge's bank accounts"; tr. 2 chú thích: "Sherman Oaks, California-based … formed in 2014"; N1: "formerly headquartered in Boca Raton, Florida" | ●T → **sai một phần** | **MH** | Chi tiết Boca Raton chỉ có ở N1 (thông cáo SEC về cáo buộc), không có trong N9 → không được gắn ●T. N1 nói "formerly", không nói "ban đầu" |
| 2 | FPCM ngắn hạn trả lãi tháng + quỹ 5 năm; chào là có bảo đảm bằng BĐS của người vay bên thứ ba | N9 tr. 4: "(a) short-term promissory notes … First Position Commercial Mortgage … (b) unit offerings with five-year terms"; tr. 5 "'first-position'" | ●T → đúng | K | |
| 2b | Người vay 11–15 %; FPCM 5–8 %, 12–18 tháng | N2 tr. 13 ¶42 "twelve-to-eighteen month term promissory note bearing 5%-8%"; ¶44 "11-15% annual interest"; tr. 16 ¶56 "5-8%, payable monthly"; N1 "5-10 percent" | ◐ → đúng | K | Đã ghi chênh N1/N2; chọn N2 tr. 16 là đúng |
| 3 | Kênh bán (telemarketing, hàng trăm đại lý, radio, TV, báo, MXH, hội thảo); duyệt > 80 triệu USD hoa hồng bằng tiền nhà đầu tư | N9 tr. 4 "telemarketing; a nationwide network of hundreds of external sales agents; radio, television, and newspaper … social media; websites; and conferences"; tr. 5 "authorized payment of more than $80 million in commissions … funded by investor money" | ●T → đúng | K | SEC ghi 64,5 triệu (N1; N2 tr. 14 ¶46) — không trộn hai số (R3) |
| 3b | Câu quảng cáo hưu trí; ≥ 2.600 nhà đầu tư IRA, gần 400 triệu | N2 tr. 25 (ảnh trang): "Let us help you protect your retirement funds from market volatility."; tr. 13 ¶41 "At least 2,600 … Individual Retirement Account funds to invest nearly $400 million" | ◐ → đúng | K | Trích khớp ảnh trang |
| 4 | Cảnh MH nhà đầu tư tổng hợp | — | MH → đúng | K | |
| 5 | Phần lớn BĐS do thực thể Shapiro kiểm soát qua RS Trust và > 270 LLC; không đủ dòng tiền; tiền mới trả "lợi nhuận" người cũ | N9 tr. 2–3 "network of more than 270 limited liability companies"; tr. 5–6 "he controlled the vast majority of these properties"; tr. 6 "failed to generate sufficient cash flow"; "diverted recently collected investors' funds to pay purported profits to prior investors" | ●T → đúng | K | |
| 5b | Chỉ ~13,7 triệu lãi thật từ người vay độc lập so với > 1,22 tỷ | N2 tr. 2 ¶2 "only generated approximately $13.7 million in interest income from truly unaffiliated third-party borrowers"; tr. 14 ¶48 | ◐ → đúng | K | |
| 6 | Giấy nợ cho BĐS chưa từng mua | N9 tr. 6 "issued notes in respect to properties that Woodbridge never actually acquired" | ●T → đúng | K | Nguồn nói "on certain occasions" — kịch bản giữ "some notes" |
| 7 | Chiếm dụng ~25–95 triệu cho bản thân và người nhà trực tiếp; > 20 triệu trả thẻ tín dụng đứng tên người nhà; du lịch xa xỉ, tranh, nội thất | N9 tr. 6–7 "misappropriated at least approximately $25 million to $95 million … to himself and his immediate family members"; tr. 7 "more than $20 million … credit card accounts held in the name of his wife"; "extravagant travel, art, and luxury furnishings" | ●T → đúng | K | Không nêu tên người nhà: đạt |
| 8 | ≥ 5 bang (TX, MA, AZ, PA, MI) ra cease-and-desist vì bán chứng khoán không đăng ký; vẫn bán cho cư dân các bang đó | N9 tr. 7 "issued cease and desist orders … based on their unregistered sale of securities … continued to sell … to residents of those states" | ●T → đúng | K | |
| 8b | "Over 90% national renewal rate!"; chuyển khách sang quỹ dài hạn | N2 tr. 22 ¶90 (ảnh trang): "Over 90% national renewal rate!"; "sought to move FPCM Investors into the longer five-year term Fund Offerings"; tr. 23 ¶94; N1 cùng câu | ◐ → đúng | K | ¶94 nêu "DR" — dàn truyện không nêu: đạt |
| 9 | SEC hai lần ra toà buộc nộp tài liệu (17/07/2017, 31/10/2017) | N2 tr. 11 ¶34 "On July 17, 2017, the Commission brought a subpoena enforcement action"; ¶35 "On October 31, 2017 … second subpoena enforcement action"; N1 "court orders in September and November … forced the unregistered companies to open their books" | TT → đúng cho ngày nộp | K | Hai ngày trong dàn truyện là ngày **nộp** đơn; ngày **lệnh** toà là tháng 9 và 11 (N1). Lý do (không nộp tài liệu) là lời SEC (◐). Xem R4 |
| 10 | 2017 quyết định phá sản; không báo mất khả năng thanh toán; vẫn thu tiền tới khi nộp đơn 12/2017; ngay trước đó chuyển hàng triệu USD sang tài khoản đứng tên người nhà lập doanh nghiệp mới | N9 tr. 7 "At some point in 2017, SHAPIRO made the decision …"; "Without disclosing to investors that Woodbridge was insolvent …"; "Immediately prior … diverted millions of dollars to several bank accounts opened in the name of his wife … to fund new business ventures" | ●T → đúng | K | |
| 10b | Chapter 11 ngày 04/12/2017 — dẫn **N2 tr. 3, 13** | N2 **tr. 2** ¶3 "on December 4, 2017, Shapiro caused most of his companies to file Chapter 11 bankruptcy"; **tr. 12** ¶37; **tr. 15**. Tr. 3 và tr. 13 **không** có ngày nộp đơn Chapter 11 (tr. 13 ¶41 chỉ "through at least December 4, 2017") | TT → đúng | **S** (trang) | Nội dung đúng, trang dẫn sai |
| 11 | Đơn SEC mở niêm phong 21/12/2017 + phong toả tài sản; 12/2018 dàn xếp không thừa nhận/không phủ nhận; phạt dân sự 100 triệu + hoàn trả + lãi | N1 "unsealed today" (Dec. 21, 2017), "temporary asset freeze"; N4 tr. 1 "without admitting or denying the allegations of the Amended Complaint"; tr. 5 "civil penalty in the amount of $100,000,000"; disgorgement $18,546,643 + lãi $2,163,613.69; N5 tr. 1; docket 12/27/2018; N3 | ◐ → đúng | K | Cấm dùng N4 tr. 7 mục VI: đúng (mục VI chỉ "solely for purposes of" phá sản) |
| 12-i | "Tháng 4/2019 Shapiro, Acevedo, Roseman bị bắt và bị truy tố" | N13 (11/04/2019): "were separately arrested and charged by criminal authorities, along with Woodbridge owner Robert H. Shapiro" — không nêu ngày/tháng bắt | ● | **KKĐ** | Tháng bắt không có trong nguồn đã mở; docket N7 chưa mở được (403). Chỉ nói được "By April 2019" |
| 12-ii | 08/2019 nhận tội âm mưu gian lận thư + điện tín và trốn nộp thuế; 15/10/2019 tuyên 300 tháng (240 + 60 nối tiếp) | N8 tr. 1 "Count 1 … conspiracy to commit mail fraud and wire fraud … Count 10 … evasion of payment of federal income taxes" (docket 08/07/2019); N10 tr. 1 "Date of Imposition of Sentence: October 15, 2019"; tr. 2 "240 months as to Count 1, and 60 months as to Count 10, to run consecutively" | ● → đúng | K | |
| 12b | Câu mẫu "he also admitted evading **federal income taxes**"; thuế nợ ≥ ~6,06 triệu | N10 tr. 1 / N8 tr. 1: tội danh "Evasion of **Payment** of Federal Income Taxes"; N9 tr. 8 "total tax due and owing of at least approximately $6,061,134" (năm 2000–2005) | ●T → câu EN **rộng hơn tội danh** | **MH** | Luật 8d: chỉ dùng đúng tên tội danh. Số 6,06 triệu K |
| 13 | Acevedo nhận tội §371, 60 tháng, 17/09/2021; Roseman "convicted and sentenced" | N11 tr. 1 "pleaded guilty to Count 1 … 18 U.S.C. § 371 Conspiracy To Commit Mail and Wire Fraud"; "September 17, 2021"; tr. 2 "60 months"; N15 tr. 6 (ảnh trang) "in light of Defendant's criminal conviction and sentence in United States v. Roseman" | ● → đúng | K | Chức danh: N13 ghi "former directors of investments" (R5) |
| 14 | 2024, CA11 giữ nguyên quyết định bác đơn giảm án | N12 tr. 1 "Date Filed: 03/13/2024"; tr. 4 "the district court's denial of Shapiro's motion for a sentence reduction is AFFIRMED" | ● → đúng | K | Đơn theo §3582(c)(1)(A); không suy ra lý do sức khoẻ (8f) |
| 15 | Phần lớn mất tiền; tổn thất "likely to exceed at least one hundred million dollars" | N9 tr. 7–8 "most of Woodbridge's investors lost money, with total losses likely to exceed at least one hundred million dollars" | ●T → đúng | K | |
| 16 | Bài học + dấu hiệu (§4) | xem §3 dưới | — | **MH** | D(2) gắn sự việc ◐ (đại lý không đăng ký) vào nhịp 3 ●T |
| Cú treo | "And when the end came, the money kept coming in." | N9 tr. 7 "caused Woodbridge to collect additional money from investors through the filing of Woodbridge's bankruptcy in December 2017" | ●T → đúng | K | |

## 3. Móc câu, cú treo, bài học

**Móc câu (H1–H6).** Không câu nào gợi ý **công ty** Woodbridge bị kết án: nhãn ● CONVICTED chỉ gắn H5 với tên Shapiro. Không gán nhãn "fraudster/con man". "safe" là lời chào bán, đúng N9 tr. 4. Một điểm nhỏ ở H4: "It kept selling" lấy công ty làm chủ ngữ, trong khi N9 tr. 7 ghi chủ ngữ là "SHAPIRO and his co-conspirators". Câu này không nâng tầng ai, nhưng nên giữ đúng chủ thể (R2). Không có hướng dẫn làm.

**Cú treo.** Khớp ●T (N9 tr. 7). "the end" là cách nói kịch tính và không gán thêm sự việc. Đạt.

**L1 (Ponzi).** Mức khái niệm, không có bước thao tác: đạt §1. Có hai điểm cần chỉnh:
- (a) Câu "cần bán liên tục, hoa hồng cao và giữ khách không rút" đọc như danh sách việc kẻ vận hành phải làm. Nên viết từ góc người xem ("that's why these schemes push nonstop sales and pressure you not to cash out"), để thành dấu hiệu chứ không thành công thức.
- (b) L1 gắn nhịp 10 với câu "Khi tiền vào chậm lại, nó sụp". N9 không nói Woodbridge sụp vì tiền vào chậm, mà nói Shapiro "made the decision" nộp đơn phá sản. Việc "Fundraising from investors was halted" và lỡ hạn trả lãi chỉ có ở N2 tr. 2 ¶3, tr. 15 (◐). Vì vậy câu nhân quả về Woodbridge phải gắn "the SEC alleged", hoặc để L1 ở mức chung, không áp vào vụ.

**L2 (thế chấp, bên liên quan).** Đạt. Chỉ là khái niệm, khớp N9 tr. 5–6.

**L3 (đăng ký; hai vụ song song).** Đạt. Đúng tầng: SEC là dàn xếp (N4, N5), hình sự là kết án (N10). Không giải thích miễn trừ.

**D (5 dấu hiệu).**
- (1), (3), (4), (5): đạt; nguồn và tầng đúng nhịp.
- **(2) lỗi tầng.** "Người bán ăn hoa hồng, **không đăng ký**" được gắn nhịp 3 (●T). Nhưng N9 không nói đại lý không đăng ký. Chi tiết này chỉ có ở N2 tr. 14 ¶46 ("virtually none of these sales agents were registered", ◐) và N1. Nếu để nguyên, kịch bản sẽ đưa một cáo buộc lên ●T. Ngoài ra, câu này dễ hiểu thành mọi đại lý đều phạm luật, trong khi đại lý là KBCB hoặc ◐ chưa xác minh kết quả.

**P (nguyên tắc chung).** Không nêu sản phẩm, mã hay tỷ trọng: đạt §1. Câu "đòi gốc về trước khi tái tục" mang tính mệnh lệnh cá nhân, gần ranh "khuyên tài chính". Nên chuyển thành dấu hiệu hoặc câu hỏi (R6).

**Phép thử "làm theo được ngay".** Không mục nào đạt ngưỡng hướng dẫn. Nhịp 5 và 12b đã chủ động bỏ cấu trúc trust/LLC và Offer in Compromise: đúng. Câu quảng cáo ở 3b là một khẩu hiệu đơn lẻ, dùng làm dấu hiệu, không phải kịch bản lời dụ chép dùng được. Nên hiện bằng ảnh trang đơn kiện kèm nguồn, không dựng lại đồ hoạ quảng cáo.

## 4. Rà luật 8 (a–f) và luật 5

| Điểm | Kết quả kiểm |
|---|---|
| (a) | Shapiro ● (N10 tr. 1–2; N8 tr. 1). **Đạt.** |
| (b) | ◐ chỉ dùng cho chi tiết đơn kiện SEC (vụ đã khép bằng consent: N4 tr. 1, N5 tr. 1, N3) và cho Woodbridge. **Đạt.** Lưu ý: consent judgment nói về **Amended Complaint**, còn dàn truyện trích **đơn gốc** N2. Cả hai vẫn là cáo buộc nên tầng ◐ đúng. Bảng §5(b) liệt kê nhịp 9 là ◐, trong khi bảng nhịp gán TT; nên thống nhất. |
| (c) | Không nêu tên đại lý, "DR", Controller, nhân viên SEC (N1 có tên nhân viên SEC: không dùng). **Đạt**, trừ lỗi tầng D(2) ở §3. |
| (d) | Không có "fraudster/scammer". **Lỗi nhỏ:** câu mẫu 12b "evading federal income taxes" không đúng tên tội danh "evasion of payment of federal income taxes" (N10 tr. 1). Woodbridge không bị gọi "convicted". Câu "công ty không bị truy tố hình sự" → **KKĐ** (không có nguồn đã mở nói điều này; kịch bản không được khẳng định, đúng như dàn truyện đã ghi). |
| (e) | Không có. **Đạt.** |
| (f) | Không suy đoán động cơ. Chi tiêu chỉ lấy từ N9 tr. 6–7; không dùng lời N2 tr. 2 "lived in the lap of luxury". Nhịp 14 không nêu lý do đơn giảm án. **Đạt.** |
| Luật 5 | Tên người được nêu: Shapiro, Acevedo, Roseman (cả ba ●). Người nhà: không nêu tên. **Cảnh báo hình:** N3 có liên kết "Final Judgment – [vợ Shapiro, nêu tên đầy đủ]" (relief defendant); N9 tr. 3–4 liệt kê các thực thể "in the name of his wife, J.S."; N9 tr. 6 có hai địa chỉ; N9 tr. 7 nêu tên hai công ty mới. Nếu chiếu ảnh trang hồ sơ, phải cắt hoặc che các phần này (R7). |

## 5. Tổng điểm

Tổng 33 dòng chấm (gồm logline VI/EN, H1–H6, nhịp 0–16 kể cả các nhịp "b", nhịp 12 tách hai ý, cú treo):

| K | MH | S | KKĐ |
|---|---|---|---|
| **27** | **4** (Logline VI, nhịp 1, 12b, 16/D(2)) | **1** (10b — trang) | **1** (12-i — tháng bắt) |

Không có lỗi số tiền, số người, ngày tuyên án hay tội danh trong phần sự việc chính. 12/12 PDF khớp SHA-256.

## 6. Sửa bắt buộc

1. **Nhịp 10b — trang dẫn sai.** Đổi "N2 tr. 3, 13" → "**N2 tr. 2 ¶3** (và tr. 12 ¶37)".
2. **Nhịp 12b — tên tội danh.** Câu mẫu "he also admitted evading federal income taxes" → *"He also pleaded guilty to evading payment of federal income taxes."* (N10 tr. 1; N8 tr. 1). Nếu nêu số: *"…at least about $6.1 million owed for tax years 2000 through 2005"* (N9 tr. 8, ●T).
3. **Nhịp 12 — tháng bắt.** Câu "Tháng 4/2019 … bị bắt và bị truy tố" → *"By April 2019, Shapiro and two former Woodbridge directors of investments had been arrested and criminally charged."* (N13, 11/04/2019). Giữ nguyên câu này cho tới khi mở được docket N7 bằng đường chính thức.
4. **Nhịp 1 — tầng Boca Raton.** Tách chi tiết Boca Raton khỏi ●T. Câu mẫu: *"Woodbridge was formerly headquartered in Boca Raton, Florida (SEC), and later based in Sherman Oaks, California."* Gắn TT/nguồn N1 cho Boca Raton, ●T N9 tr. 2 cho Sherman Oaks. Bỏ chữ "ban đầu" vì N1 chỉ nói "formerly".
5. **§4 D(2) — tầng.** Đổi thành: *"(2) Người bán ăn hoa hồng — the SEC alleged that virtually none of Woodbridge's sales agents were registered (N2 tr. 14 ¶46, ◐) → tra FINRA BrokerCheck / Investor.gov"*. Gắn nhịp 3 **chỉ** cho phần hoa hồng ●T (N9 tr. 5). Không ngụ ý đại lý cụ thể nào phạm luật.
6. **Logline VI — thời gian.** Bỏ "cho tới khi ông bị tuyên 25 năm tù" khỏi mệnh đề "việc bán vẫn tiếp tục". Câu thay: *"…năm bang đã ra lệnh dừng mà việc bán vẫn tiếp tục cho tới khi công ty nộp đơn phá sản cuối năm 2017; năm 2019 ông bị tuyên 25 năm tù."* (N9 tr. 7; N10 tr. 1–2).

## 7. Khuyến nghị

- **R1 (H2, số nhà đầu tư).** Nguồn có ba con số: N9 tr. 4 "approximately 10,000", N9 tr. 7 "more than approximately 9,000", SEC 8.400. Giữ "about 10,000" kèm "according to his plea agreement's factual proffer", và không đặt cạnh số 8.400 của SEC khi không giải thích.
- **R2 (H4).** Viết *"At least five states ordered Woodbridge entities to stop selling unregistered securities. Shapiro admitted the sales continued."* — đúng "at least five" và đúng chủ thể (N9 tr. 7).
- **R3 (nhịp 3).** Hoa hồng: dùng một số nhất quán (> 80 triệu, ●T, N9 tr. 5). Nếu nhắc 64,5 triệu thì phải gắn "the SEC alleged" (N1; N2 tr. 14).
- **R4 (nhịp 9).** Phân biệt ngày nộp (17/07 và 31/10/2017, N2 tr. 11) với lệnh toà (tháng 9 và 11, N1). Cụm "forced … to open their books" là lời SEC, nên dẫn "the SEC said".
- **R5 (nhịp 13).** Dùng chức danh theo N13: "former directors of investments" thay vì "giám đốc huy động vốn".
- **R6 (P, L1).** Viết lại theo góc người xem/dấu hiệu, như đã nêu ở §3. Câu L1 về "tiền vào chậm thì sụp" chỉ áp vào Woodbridge khi có "the SEC alleged" (N2 tr. 2 ¶3).
- **R7 (hình hồ sơ).** Khi chiếu trang N9, N3, cắt hoặc che tên vợ Shapiro, danh sách thực thể đứng tên vợ (N9 tr. 3–4), hai địa chỉ (N9 tr. 6), tên hai công ty mới (N9 tr. 7), và tên nhân viên SEC (N1, N3).
- **R8 (§5 dàn truyện).** Thống nhất tầng nhịp 9 (TT hay ◐) giữa bảng nhịp và bảng §5(b).
- **R9 (luật 4).** Docket N7 hiện trả 403 với phiên kiểm. Kiểm trạng thái vụ (ân xá, giảm án) trước ngày chốt lời phải đi đường chính thức khác hoặc ghi "chưa mở được".
