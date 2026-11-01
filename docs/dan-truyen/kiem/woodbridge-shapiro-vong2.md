# Kiểm độc lập vòng 2 — dàn truyện `woodbridge-shapiro`

- **Người kiểm:** tác tử kiểm độc lập vòng 2 (Claude, phiên con của điều phối MR-2)
- **Ngày kiểm:** 01/11/2026
- **Đối tượng:** `docs/dan-truyen/woodbridge-shapiro.md` (bản đã sửa, đọc ngày 01/11/2026)
- **Đã đọc:** `CLAUDE.md`; `docs/HIEN-CHUONG.md` (§1, §3 gồm luật 5 và luật 8, §4, §5); tệp dàn truyện; `docs/ung-vien/woodbridge-shapiro/NGUON.md` (chỉ để tra mã → tệp/URL và SHA-256); 12 PDF trong `ho-so/woodbridge-shapiro/` (`pdftotext -layout`; câu trích nguyên văn đối chiếu ảnh trang `pdftoppm -r 100`: N2 tr. 22, 25; N9 tr. 4, 7; N15 tr. 6); HTML sec.gov tải bằng curl với User-Agent "MoneyReroute research <email liên hệ — đã gỡ>": N1 (PR 2017-235 + LR 24020), N3 (PR 2019-3), N13 (PR 2019-55 + LR 24450), và N17 (LR 24476, 24531, 24676, 24759) để kiểm một dòng ở §5(c). Tất cả HTTP 200.
- **Không đọc:** `reports/**`; `docs/ung-vien/*/TANG.md`, `RUI-RO.md`, `KIEM-TANG.md`; mọi tệp khác trong `docs/dan-truyen/kiem/`; dàn truyện vụ khác; git log/diff; CourtListener (N7) và justice.gov (N21–N23) — không mở trong vòng này. Không gọi API trả tiền; không vượt rào truy cập.
- Tệp tạm: `/tmp/claude-0/-home-user-money-reroute/1c2cc4e0-12e8-59b7-bad3-2f105161639e/scratchpad/kiem2-wb/`.

Ký hiệu chấm: **K** khớp · **MH** mạnh hơn nguồn hoặc tầng · **S** sai (số, ngày, trang, tầng, người) · **KKĐ** không kiểm được trong vòng này.

## 1. Bảng nguồn và SHA-256

| Mã | Tệp | SHA-256 đo lại | So NGUON | Số trang PDF |
|---|---|---|---|---|
| N2 | `sec-complaint-2017.pdf` | `9e5c4388…c39c8b6` | khớp | 47 |
| N4 | `sec-final-judgment-shapiro-2018.pdf` | `34e7680a…6456c2f5c` | khớp | 8 |
| N5 | `sec-final-judgment-woodbridge-2018.pdf` | `9a99be3e…86bfc9ff` | khớp | 9 |
| N6 | `sec-admin-order-shapiro-2019.pdf` | `2f7f5564…307cb2d` | khớp | 3 (dàn truyện không dùng) |
| N8 | `plea-agreement-shapiro-2019.pdf` | `351304b6…52655939` | khớp | 18 |
| N9 | `factual-proffer-shapiro-2019.pdf` | `6924f2a7…6231df1e` | khớp | 9 |
| N10 | `judgment-shapiro-2019.pdf` | `90c25e81…02ef24ca` | khớp | 6 |
| N11 | `judgment-acevedo-2021.pdf` | `f35e3e9d…0c56f0575f` | khớp | 7 |
| N12 | `ca11-opinion-shapiro-2024.pdf` | `e1863399…280dc2ec4` | khớp | 4 |
| N14 | `sec-complaint-acevedo-roseman-2019.pdf` | `4db52b63…a480a8d` | khớp | 25 (dàn truyện không dùng) |
| N15 | `sec-final-judgment-roseman-2021.pdf` | `3ebbf43a…b6081ea1` | khớp | 7 |
| N16 | `sec-final-judgment-acevedo-2021.pdf` | `1a59528c…bf87b14af854` | khớp | 7 (dàn truyện không dùng) |
| N1, N3, N13, N17 | HTML sec.gov | không lưu (NGUON cũng không lưu) | nội dung khớp những câu dàn truyện dẫn | — |

Cả 12 PDF trùng SHA-256 đầy đủ trong NGUON (so từng ký tự bằng `sha256sum`). Số trang N2 in ở chân trang trùng số trang PDF (đã xem tr. 22, 25).

## 2. Bảng chấm từng dòng

### 2.1 Logline và móc câu

| Dòng | Chấm | Bằng chứng (≤ 25 từ) + trang thực tế | Ghi chú |
|---|---|---|---|
| Logline VI | **MH** | Phần lớn khớp N9 tr. 4–7. Riêng "nhiều người dùng tiền hưu" chỉ có ở SEC: "At least 2,600 … used their Individual Retirement Account funds" (N2 tr. 13 ¶41; N3 "many of them seniors who had invested retirement funds") | Proffer N9 không nhắc tiền hưu → chi tiết ◐ đang nói như sự thật. Xem Sửa bắt buộc 1 |
| Logline EN | K | "short-term promissory notes that purportedly paid investors monthly interest" (N9 tr. 4); "signed thousands of checks to investors" (N9 tr. 3); kỳ Aug 2012–Dec 2017 (N9 tr. 4) | "Five years" ≈ 2012–2017, chấp nhận được; một FPCM chỉ 12–18 tháng nên câu nói về dòng thời gian của công ty, không phải một nhà đầu tư |
| H1 | K | Cảnh MH có nhãn "ILLUSTRATIVE" | Đúng HIEN-CHUONG §4 |
| H2 | K | "approximately $1.29 billion from approximately 10,000 investors across the United States" (N9 tr. 4, ảnh trang đã xem); tr. 7 "more than approximately 9,000"; N2 tr. 2 ¶1 "over 8,400" | Ghi chú chênh số người đúng |
| H3 | K | "misleadingly claimed that these investments were adequately secured by real property owned by third-party borrowers, and thus safe" (N9 tr. 4, ảnh trang) | "safe" là lời chào bán, đúng |
| H4 | K | "at least five states … issued cease and desist orders … nonetheless continued to sell" (N9 tr. 7, ảnh trang) | |
| H5 | K | "new investors were misused to pay false and misleading 'returns' to existing investors" (N9 tr. 6); "300 months" (N10 tr. 2), tuyên 15/10/2019 (N10 tr. 1) | |
| H6 | K | Lời kênh, không mang sự việc | Khuyến nghị K1 về "the whole time" |

### 2.2 Bảng nhịp

| Nhịp | Chấm | Bằng chứng + trang thực tế | Ghi chú |
|---|---|---|---|
| 0 | K | như §1 | |
| 1 | K | "owner, president, and chief executive officer" (N9 tr. 2); "sole signatory on all of Woodbridge's bank accounts" (N9 tr. 3); "Sherman Oaks, California-based" (N9 tr. 2 chú thích 1); "formerly headquartered in Boca Raton" (N1) | Ghi chú "Boca Raton chỉ có ở thông cáo SEC" **không chính xác**: N2 tr. 12 ¶39 cũng có "headquartered in Boca Raton". Tầng ◐ vẫn đúng (đều là SEC). Khuyến nghị K2 |
| 2 | K | FPCM + "unit offerings with five-year terms"; "secured by real property owned by third-party borrowers" (N9 tr. 4); "'first-position' on the real property" (N9 tr. 5) | |
| 2b | K | "Third-Party Borrowers were paying the company 11-15% annual interest" (N2 tr. 13 ¶44); "twelve (or sometimes up to eighteen) months … 5-8%, payable monthly" (N2 tr. 16 ¶56; tr. 13 ¶42); "5-10 percent" (N1) | Ghi chú chênh N1/N2 đúng |
| 3 | K | "telemarketing; a nationwide network of hundreds of external sales agents; radio, television, and newspaper … social media; websites; and conferences" (N9 tr. 4); "more than $80 million in commissions … funded by investor money" (N9 tr. 5); "$64.5 million" (N2 tr. 14 ¶46) | |
| 3b | K | "Let us help you protect your retirement funds from market volatility." (N2 tr. 25, ảnh trang khớp nguyên văn); "At least 2,600 … nearly $400 million" (N2 tr. 13 ¶41) | |
| 4 | K | Cảnh MH, không lấy chi tiết từ lời khai | |
| 5 | K | "network of more than 270 limited liability companies" (N9 tr. 2–3); "controlled the vast majority of these properties … failed to generate sufficient cash flow … diverted recently collected investors' funds to pay purported profits" (N9 tr. 6) | |
| 5b | K | "only generated approximately $13.7 million in interest income from truly unaffiliated third-party borrowers" (N2 tr. 2 ¶2; tr. 14 ¶48); "$1.22 billion" (N2 tr. 2 ¶1) | |
| 6 | K | "issued notes in respect to properties that Woodbridge never actually acquired" (N9 tr. 6) | Không đưa địa chỉ lên hình — đúng luật 5 |
| 7 | K | "at least approximately $25 million to $95 million … to himself and his immediate family members" (N9 tr. 6–7); "more than $20 million … credit card accounts held in the name of his wife"; "extravagant travel, art, and luxury furnishings" (N9 tr. 7, ảnh trang) | Khuyến nghị K3: giữ "at least" |
| 8 | K | N9 tr. 7 (TX, MA, AZ, PA, MI; "nonetheless continued to sell … to residents of those states") | |
| 8b | K | "Over 90% national renewal rate!" (N2 tr. 22 ¶90, ảnh trang khớp nguyên văn); "move your loan … to our higher-return Mortgage Investment Fund" (N2 tr. 23 ¶94) | |
| 9 | K | "On July 17, 2017 … subpoena enforcement action"; "On October 31, 2017 … second subpoena enforcement action" (N2 tr. 11 ¶34–35); "court orders in September and November … forced the unregistered companies to open their books" (N1) | N1 không ghi năm của "September and November" nhưng thông cáo ngày 21/12/2017 → 2017 là đọc hợp lý |
| 10 | K | "At some point in 2017, SHAPIRO made the decision … collect additional money from investors through the filing … December 2017"; "diverted millions of dollars to several bank accounts opened in the name of his wife … to fund new business ventures" (N9 tr. 7, ảnh trang) | |
| 10b | K | "on December 4, 2017, Shapiro caused most of his companies to file Chapter 11" (N2 tr. 2 ¶3); ¶37 tr. 12 | |
| 11 | K | "unsealed today … asset freeze" (N1, 21/12/2017); "without admitting or denying the allegations" (N4 tr. 1; N5 tr. 1); "civil penalty in the amount of $100,000,000" + $18,546,643 + $2,163,613.69 (N4 tr. 5); vào docket 27/12/2018 | Lệnh cấm dùng N4 tr. 7 mục VI đúng chỗ (mục VI "Bankruptcy Nondischargeability" ở tr. 7) |
| 12 | K | "separately arrested and charged by criminal authorities, along with … Shapiro" (N13, 11/04/2019); Plea Agreement vào docket 08/07/2019 (N8 tr. 1); "pled guilty to Counts 1 and 10"; §1349 + §7201 (N10 tr. 1); "300 months … 240 … 60 … consecutively" (N10 tr. 2); tuyên 15/10/2019 (N10 tr. 1) | |
| 12b | K | "Evasion of Payment of Federal Income Taxes" (N10 tr. 1); "at least approximately $6,061,134" (N9 tr. 8) | Đúng §1: không nêu kỹ thuật thuế |
| 13 | K | Acevedo: "pleaded guilty to Count 1 … 18 U.S.C. § 371 Conspiracy To Commit Mail and Wire Fraud"; "60 months"; 17/09/2021 (N11 tr. 1–2). Roseman: "in light of Defendant's criminal conviction and sentence in United States v. Roseman" (N15 tr. 6, ảnh trang) | Chức danh "former directors of investments" đến từ N13, không phải N11/N15 → Khuyến nghị K4 |
| 14 | K | "summarily affirm the district court's denial of Shapiro's motion for a sentence reduction" (N12 tr. 2, 4); ngày 13/03/2024 | Đơn theo 18 U.S.C. §3582(c)(1)(A) |
| 15 | K | "most of Woodbridge's investors lost money, with total losses likely to exceed at least one hundred million dollars" (N9 tr. 7–8, ảnh tr. 7) | |
| 16 | K | Dẫn sang §4 | |

### 2.3 Cú treo, bài học, nguồn kết tập

| Dòng | Chấm | Bằng chứng + trang | Ghi chú |
|---|---|---|---|
| Cú treo §3 "And when the end came, the money kept coming in." | K | "caused Woodbridge to collect additional money from investors through the filing of Woodbridge's bankruptcy in December 2017" (N9 tr. 7) | Đúng tầng ●T. Khuyến nghị K5: câu kế tiếp nêu "Shapiro admitted" |
| L1 | K | "new investors were misused to pay … 'returns' to existing investors" (N9 tr. 6); "required a continuous infusion of new investor funds" (N2 tr. 14 ¶49, ◐) | Gắn "the SEC alleged" cho ý "tiền vào chậm thì sụp" đúng |
| L2 | K | "he controlled the vast majority of these properties" (N9 tr. 6) | Khái niệm rủi ro bên liên quan |
| L3 | K | "cease and desist orders … based on their unregistered sale of securities" (N9 tr. 7) | Đúng: không giải thích miễn trừ |
| D (5 dấu hiệu) | K | (2) "commissions … funded by investor money" (N9 tr. 5); "virtually none of these sales agents were registered" (N2 tr. 14 ¶46, ◐) | Đều là hướng phòng vệ |
| P | K | Nguyên tắc chung, HIEN-CHUONG §1 cho phép | Không có sản phẩm, mã hay tỷ trọng |
| Nguồn chính thức kết tập (6 trang) | KKĐ | Vòng này không mở lại Investor.gov, BrokerCheck, FTC, CFPB | Kiểm HTTP lại trước khi chốt lời |

### 2.4 Bảng §5 (rà luật 8 tổng hợp)

| Điểm | Chấm | Bằng chứng | Ghi chú |
|---|---|---|---|
| (a) | K | N10 tr. 1: "adjudicated guilty" | |
| (b) | K | N4 tr. 1, N5 tr. 1 (consent, không thừa nhận) | Danh sách nhịp ◐ thiếu nhịp 1 (Boca), nhịp 3 (64,5 triệu), D(2); nhịp 9 trong bảng nhịp gắn TT, không phải ◐ → Khuyến nghị K6 |
| (c) | K | N17: bốn LR nêu tên 6 người (Nilosek; Wieniewitz; Pittsenbargar; Church-Koegel, Goldman, Walker) | LR 24676 còn nêu "19 of Woodbridge's other highest-earning unregistered brokers" bị SEC kiện → "6 người" không phải toàn bộ. Luật không nêu tên vẫn đúng. Khuyến nghị K7 |
| (d) | KKĐ | Vế "công ty không bị truy tố hình sự": vòng này không mở docket N7. Các bản án/judgment đã mở chỉ ghi tên cá nhân (N10, N11; N15 tr. 6 "United States v. Roseman") | Dàn truyện đã tự ghi "chưa kiểm độc lập" và kịch bản không khẳng định → không cần sửa |
| (e) | K | Không có thương hiệu bị mạo danh trong nguồn đã đọc | |
| (f) | K | Chi tiêu chỉ lấy từ N9 tr. 7 | |
| KBCB (luật 5) | K | Vợ là relief defendant (N2 tr. 1), không bị buộc tội; N9 chỉ ghi "J.S." | Ảnh trang N2 tr. 1 và trang N3 (danh mục "Final Judgment - Jeri Shapiro") có tên → đã có ở §7 mục che tên |

## 3. Móc câu, cú treo, bài học — phép thử tầng và phép thử "làm theo được ngay?"

- **Ám chỉ mạnh hơn tầng:** H1–H5 không vượt N9/N10. H1 ghép bàn bếp minh hoạ với H2 (số thật) nhưng có nhãn ILLUSTRATIVE, nên chấp nhận được. H6 "red flags that were there the whole time" ngầm khẳng định mốc thời gian của dấu hiệu, trong khi tầng ●T (N9 tr. 7) chỉ nói lệnh của bang có "during the course of the conspiracy"; mốc "Since 2015" là ◐ (N2 tr. 11 ¶36). Đây là lời kênh nên chỉ ở mức khuyến nghị (K1). Logline VI có một chi tiết ◐ nói như sự thật (Sửa bắt buộc 1).
- **Cú treo:** đúng tầng ●T, không ám chỉ động cơ.
- **Hướng dẫn làm:** không dòng nào cho người có ý xấu một trình tự làm theo được. Nhịp 5 cố ý không mô tả cấu trúc trust/LLC; nhịp 12b không nêu kỹ thuật trốn thuế (trust Nevada, Form 656-L ở N9 tr. 8 bị bỏ, đúng); L3 không giải thích miễn trừ đăng ký. Nhịp 7 và 10 có nêu kênh "tài khoản/thẻ đứng tên người nhà", nhưng ở mức dấu vết đã được thừa nhận, không có bước nào → **đạt**, chỉ cần không mở rộng khi viết lời (K3).
- **Lời dụ chép dùng được:** chỉ có hai câu quảng cáo ngắn (N2 tr. 25, tr. 22), dùng làm dấu hiệu nhận diện. Không có kịch bản gọi điện hay trang mẫu → đạt §1.

## 4. Luật 8 (a–f) và luật 5 — kết luận

- (a) Đạt: Shapiro ● (N10). (b) Đạt: ◐ chỉ dùng cho chi tiết đơn kiện SEC trong vụ đã khép bằng consent (N4, N5). (c) Đạt: không nêu tên đại lý, "DR" hay Controller. (d) Đạt: chỉ dùng tội danh; Woodbridge không bị gọi "convicted". (e) Không áp dụng. (f) Đạt.
- Luật 5: đạt. Người nhà, chủ hiện tại hai bất động sản, nạn nhân và nhân viên SEC đều không có tên trong dàn truyện. Việc che tên trên ảnh trang N1, N2, N3, N9 đã có ở §7.

## 5. Tổng điểm

| K | MH | S | KKĐ | Tổng dòng |
|---|---|---|---|---|
| 42 | 1 | 0 | 2 | 45 |

(Logline 2 + móc câu 6 + nhịp 23 + cú treo 1 + bài học 5 + nguồn kết tập 1 + bảng §5 7 = 45.)

## 6. Sửa bắt buộc

1. **Logline VI — "nhiều người dùng tiền hưu":** chi tiết này chỉ có trong hồ sơ SEC (◐: N2 tr. 13 ¶41; N3), không có trong N9. Sửa một trong hai cách: thêm "(theo SEC, ít nhất 2.600 người dùng tài khoản IRA)" hoặc bỏ cụm này. Nếu logline được dùng cho mô tả hay tiêu đề video, phải mang "the SEC alleged".

## 7. Khuyến nghị (không chặn)

- **K1 (H6):** cân nhắc "the red flags that were there" thay cho "…the whole time", vì mốc thời gian của dấu hiệu chưa có ở tầng ●T.
- **K2 (nhịp 1):** sửa ghi chú nguồn: Boca Raton có ở N1 **và** N2 tr. 12 ¶39 ("Prior to 2016 … headquartered in Boca Raton"), cả hai đều là SEC, tầng ◐ giữ nguyên.
- **K3 (nhịp 7):** giữ "at least approximately $25 million to $95 million" (N9 tr. 6–7); không mở rộng cơ chế tài khoản/thẻ đứng tên người nhà quá mức "accounts in a family member's name".
- **K4 (nhịp 13):** chức danh "former directors of investments" lấy từ N13 (SEC) → ghi N13 vào cột nguồn.
- **K5 (cú treo):** câu ngay sau cú treo nên nói rõ "Shapiro admitted…" để giữ nhãn ●T.
- **K6 (§5 b):** bổ sung nhịp 1 (Boca Raton), nhịp 3 (64,5 triệu USD), D(2) vào danh sách dùng ◐; ghi rõ nhịp 9 là TT dẫn từ đơn kiện SEC.
- **K7 (§5 c):** đổi "kể cả 6 người bị SEC kiện riêng" thành "kể cả các đại lý bị SEC kiện riêng (N17: ít nhất 6 người nêu tên ở LR 24476/24531/24676/24759; LR 24676 nói thêm 19 đại lý khác bị kiện trước đó)".
- Trước khi chốt lời: kiểm HTTP lại 6 trang nguồn chính thức kết tập; nếu muốn khẳng định Woodbridge không bị truy tố hình sự, mở docket N7 qua CourtListener/RECAP (đường chính thức).
