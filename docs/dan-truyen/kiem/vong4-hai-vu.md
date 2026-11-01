# Kiểm độc lập vòng 4 — `irs-callcenter-patel` và `romance-sunmola`

> Ngày kiểm: 01/11/2026 · tác tử kiểm độc lập (vòng 4) · không sửa tệp được kiểm, không commit/push · chi 0 USD.
> Thang chấm: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được.

## 1. Phạm vi đọc
- Đã đọc: `CLAUDE.md`, `docs/HIEN-CHUONG.md` (đủ), `docs/dan-truyen/irs-callcenter-patel.md` (đủ 121 dòng), `docs/dan-truyen/romance-sunmola.md` (đủ 123 dòng), `docs/kho-de-tai/irs-callcenter-patel.md` **chỉ §8**, `docs/kho-de-tai/romance-sunmola.md` **chỉ §8**.
- Không đọc: `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 hai tệp kho, dàn truyện khác, các tệp khác trong `docs/dan-truyen/kiem/**`, git log/diff.
- Mục §6 (ước chi) và §8 (việc phải làm) hai tệp không chứa câu sự việc về người/vụ → không chấm (trừ chỗ có dẫn nguồn).

## 2. Nguồn đã mở (01/11/2026)
| Mã | Đường mở | Kết quả |
|---|---|---|
| Patel N1 | `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf`; `pdftoppm -r 80 -gray` tr. 1, 3, 4, 5, 6, 7, xem ảnh | SHA-256 `04fb7cb3…7b2bdf` **khớp** kho §8 |
| Patel N2 | API `justice.gov/api/v1/press_releases.json`, title "Dozens of Individuals Indicted…" → bản số **16-1257** (27/10/2016) | HTTP 200; đ.1–18 |
| Patel N3 | API, "24 Defendants Sentenced…" → 18-961 (20/07/2018) | HTTP 200; đ.1–19 (đ.12, đ.13 có `<li>`) |
| Patel N4 | API, "Indian National Pleads Guilty to Owning, Funding" → 20-19 (09/01/2020) | HTTP 200; đ.1–16 |
| Patel N5 | API, "Owner and Operator of India-Based Call Centers Sentenced" → chọn **20-1294** (30/11/2020; API trả 3 bản) | HTTP 200; đ.1–17 |
| Patel N9 | https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door | HTTP 200; FS-2017-7, 19/04/2017 |
| N10 / Sunmola N8 | https://reportfraud.ftc.gov/ | HTTP 200; trang JS, meta: "Protect your community by reporting fraud, scams, and bad business practices" |
| Patel N11 | https://www.tigta.gov/reportcrime-misconduct | HTTP 200; "Submit a Complaint", mục "Someone is impersonating an IRS or Treasury employee" |
| Sunmola N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf`; `pdftotext -layout`, tách form-feed, đọc đủ các trang được dẫn | SHA-256 `cc362fa0…59953b` **khớp** kho §8; số in đầu trang = trang PDF |
| Sunmola N1 | API, title "Prince Charming" → 1 kết quả (02/02/2017) | HTTP 200; đ.1–15 (thẻ `<p>` không rỗng) |
| Sunmola N6 | https://www.ic3.gov/PSA/2019/PSA190805 | HTTP 200; I-080519-PSA, 05/8/2019 |
| Sunmola N7 | https://www.ic3.gov/ | HTTP 200; "Home Page - Internet Crime Complaint Center (IC3)" |

Không gặp 403/CAPTCHA; không đổi User-Agent, không mirror, không PACER, không API trả tiền. Tệp tải về ở `/tmp/claude-0/v4src/`, python đọc chạy `-I`.

## 3. Patel — bảng chấm từng dòng
| # | Dòng (tệp) | Nguồn kiểm, trích ngắn | Chấm | Ghi chú |
|---|---|---|---|---|
| P1 | Ký hiệu tầng (d.6): nhận tội, toà chấp nhận 09/01/2020; tuyên án 30/11/2020 | N4 (ngày 09/01/2020) đ.10 "accepted the plea today"; N5 (30/11/2020) đ.1 | K | |
| P2 | Logline VI | N4 đ.1 "between 2013 and 2016"; đ.5; đ.6; đ.9; N5 đ.1; N1 tr. 1 "HOUSTON DIVISION" | **MH** | Vế "Hitesh Madhubhai Patel — **người thừa nhận** điều hành và cấp vốn…" (và vế mở "các call center … gọi … doạ bắt") **không có chủ thể "theo DOJ"** — trái quy ước ●T của chính tệp (plea agreement chưa mở được). Các sự việc khác khớp |
| P3 | Logline EN (3 câu) | N4 đ.5 "impersonated officials from the IRS… threatened with arrest…"; đ.6 "admitted to operating and funding several"; N5 đ.1 "20 years in prison" | K | Cả hai câu ●T có "According to the Justice Department"; câu 2 là câu 8e |
| P4 | H1 (cảnh) | — | K | Không sự việc; không lời thoại, không chữ kịch bản |
| P5 | H2 | N4 đ.5 "victims throughout the United States… threatened with arrest, imprisonment, fines or deportation if they did not pay" | K | Có chủ thể DOJ; ngôi thứ ba, mức khái niệm |
| P6 | H3 | N1 tr. 3 ¶1(a)–(b) "impersonated U.S. Internal Revenue Service (IRS) officers… impersonated … (USCIS) officers"; N4 đ.5 | K | Câu 8e |
| P7 | H4 | N4 đ.5 "call centers in Ahmedabad, India"; đ.6 | K | |
| P8 | H5 | N5 đ.1 "sentenced today to 20 years in prison… in the Southern District of Texas"; đ.2 Judge Hittner | K | |
| P9 | H6 | N4 đ.5 "would immediately turn to a network of 'runners'… to liquidate and launder" | K | Câu hỏi dẫn |
| P10 | Ghi chú móc câu ("con artist" N5 đ.4) | N5 đ.4 "bringing this con artist to justice" (U.S. Attorney Patrick) | K | |
| P11 | Nhịp 1 (12.300 USD, 85 tuổi, doạ bắt, "according to the indictment") | N2 đ.11 "According to the indictment… extorted $12,300 from an 85-year-old victim… threatening her with arrest if she did not pay fictitious tax violations" | K | Đã bỏ thành phố |
| P12 | Nhịp 1b | N2 đ.12 "The indictment also alleges… $136,000… called multiple times over a period of 20 days" | K | |
| P13 | Nhịp 2 | N1 tr. 1 "Filed in TXSD on 10/19/16", "Unsealed 10/27/16"; N2 đ.8 "returned… on Oct. 19, 2016"; đ.1 "61 individuals and entities… 20 individuals were arrested today… 32 individuals and five call centers in India" | K | Số "tens of thousands"/"hundreds of millions" gắn ◐ đúng |
| P14 | Nhịp 3 (a)–(d) | N1 tr. 3–4 ¶1(a) "arrested and fined… back taxes immediately"; (b) "deported unless they paid a fine immediately"; (c) "upfront 'worthiness fee' to demonstrate an ability to repay"; (d) "upfront IRS tax or processing fee… received nothing in return" | K | |
| P15 | Nhịp 3b | N4 đ.6 "The scripts included IRS impersonation, USCIS impersonation, Canada Revenue Agency (CRA) impersonation, Australian Tax Office (ATO) impersonation, payday loan fraud, U.S. Government grant fraud, and debt collection fraud" | K | Gắn ◐ lời DOJ (thận trọng hơn nguồn) |
| P16 | Nhịp 4 (7 vai) | N1 tr. 4–6 ¶2(a) Runner, (b) Domestic Manager, (c) Call Center Operator, (d) Caller, (e) Payment Processor, (f) Data Broker "purchase names and PII", (g) Hawaladar | K | |
| P17 | Nhịp 4b | N1 tr. 6–7 ¶3 "five major conglomerates of call centers, all located in Ahmedabad… often acted together… sharing call scripts and lists of potential victims, processing payments for each other"; tr. 1 "[1] HGLOBAL", "[2] … d.b.a. …"; N3 đ.15 "have yet to be arraigned"; N5 đ.12 "Charges remain pending for other India-based defendants" | K | Câu ◐ gắn mốc 07/2018 và 11/2020 |
| P18 | Nhịp 5 | N4 đ.5 "instructed how to provide payment, including by purchasing general purpose reloadable (GPR) cards or wiring money. Upon payment, the call centers would immediately turn to…"; N2 đ.9 "often registered using misappropriated personal identifying information"; N2 đ.10 "outside of the formal banking system… not aware of the illicit nature of the funds"; N1 tr. 6 ¶2(g) "without actually moving it", hai hawaladar bù trừ | K | ●T có "theo DOJ"; khung "đưa vào/phân lớp" ghi rõ là của kênh |
| P19 | Nhịp 6 | N4 đ.2 "also known as Hitesh Hinglaj… of Ahmedabad"; đ.6 "admitted to operating and funding several India-based call centers… including the call center HGLOBAL"; đ.7 "monthly income and expense reports to his personal email"; N1 tr. 7 bảng HGLOBAL: "HITESH PATEL… Call Center Operator"; N3 đ.15 | K | Báo cáo thu chi gắn ◐ lời DOJ — đúng |
| P20 | Nhịp 6b | N4 đ.8 "A co-defendant described Patel as 'the top person in India and the boss for whom most of the other defendants worked'" | K | Lời "hối lộ" cùng đoạn bị bỏ — đúng 8f |
| P21 | Nhịp 7 | N3 đ.1 "Twenty-one… sentenced this week to terms of imprisonment up to 20 years… Three other conspirators were sentenced earlier this year… in Houston"; đ.8 (quản lý runner), đ.9 ("co-owner and manager of an India-based call center", "of Illinois"); đ.11 "$8,970,396"; đ.13 (1 Houston, 1 Atlanta, 1 Phoenix); N4 đ.11 "Southern District of Texas, District of Arizona and Northern District of Georgia" | K | 21+1 Houston = 22 — khớp |
| P22 | Nhịp 7b | N3 đ.15 | K | |
| P23 | Nhịp 8 | N4 đ.9 "extradited from Singapore in April 2019… apprehended… pursuant to a provisional arrest warrant in September 2018, after Patel flew there from India" | K | |
| P24 | Nhịp 9 | N4 đ.2 "wire fraud conspiracy and general conspiracy to commit identification fraud, access device fraud, money laundering, and impersonation of a federal officer or employee"; đ.10; đ.8 "more than $25 million but less than $65 million… based on the government's evidence against him" | K | |
| P25 | Nhịp 10 | N5 đ.1 "20 years… three years of supervised release"; đ.2 "restitution of $8, 970,396 to identified victims" | K | |
| P26 | Nhịp 10b | N5 đ.12 "Charges remain pending for other India-based defendants. They are presumed innocent…" | K | |
| P27 | Ghi chú dòng 54–55 (lời người thật chỉ là chữ trích; N3 đ.14, N1 ¶2(a),(e),(f) có thao tác) | N3 đ.14; N1 tr. 4–6 | K | Cảnh báo đúng nội dung nguồn |
| P28 | Cú treo (3 câu) | N3 (20/07/2018) đ.1, đ.13; N4 đ.11 "24 domestic defendants"; N4 đ.6; N4 đ.9 | K | Không nói "still in India" — đúng |
| P29 | L1 | N1 tr. 4–6 ¶2; tr. 5 ¶2(d) "received lead list information and call scripts" | K | |
| P30 | L2 | N4 đ.5 "immediately"; N3 đ.14 "as quickly as possible"; N9 "Call to demand **immediate** payment using a specific payment method such as a prepaid debit card, gift card or wire transfer" | **MH** | Vế cuối "IRS nói rõ **không** gọi đòi trả bằng thẻ trả trước, thẻ quà tặng hay chuyển tiền" bỏ chữ "ngay" (immediate) → rộng hơn N9 (IRS vẫn nhận thanh toán bằng chuyển khoản; N9 chỉ phủ nhận việc gọi đòi trả **ngay** bằng phương thức chỉ định). L3 cùng tệp viết đúng |
| P31 | L3 | N9 "initiates most contacts through regular mail"; "does not: Call to demand immediate payment…"; "Demand that you pay taxes without the opportunity to question or appeal"; "Threaten to bring in local police, immigration officers…"; "payments to the 'United States Treasury'"; N2 đ.5 (HSI Edge) "U.S. government agencies do not make these types of calls" | K | |
| P32 | D (5 dấu hiệu) | (1) N4 đ.5; N9 "threaten to arrest or deport" · (2) N1 tr. 3 "immediately"; N3 đ.8 "pay immediately"; N9 · (3) N4 đ.5; N3 đ.14 "gift cards"; N9 · (4) N2 đ.12 ◐ · (5) N1 tr. 3–4 ◐ | K | |
| P33 | P (nguyên tắc) | N9; N3 đ.3 (AG Sessions) "bilk older Americans, legal immigrants and many others"; N11 mục mạo danh IRS; N10 | K | "Cúp máy; tự tra số…" không gắn nguồn và không bị gắn nguồn sai (nên ghi rõ "lời khuyên chung của kênh" cho nhất quán — không tính MH) |
| P34 | Thẻ tổng kết EN | ý 1: N1 tr. 4–6, N4 đ.5 "launder"; ý 2: N4 đ.5, N3 đ.14; ý 3: N9 "generally first receive several letters", "Call to demand immediate payment… gift card", "Threaten… to have you arrested" | K | Giữ "generally" — đúng |
| P35 | Rà (a) | N4 đ.10; N5 đ.1–2 | K | |
| P36 | Rà (b) | N3 đ.15; N5 đ.12; N4 đ.6 (HGLOBAL) | K | |
| P37 | Rà (c) | N1 tr. 1, 7 | K | |
| P38 | Rà (d) | N4 đ.2; N4 đ.8 | K | |
| P39 | Rà (e) | N1 tr. 1 (d.b.a.); N3 đ.14 (tên thẻ quà tặng); N4 đ.6 (tên ứng dụng nhắn tin) | K | |
| P40 | Rà (f), KBCB, §5 | N4 đ.8 | K | |
| P41 | Phép thử | toàn tệp | K | Xem §5 |
| P42 | §7 nguồn N9–N11 | như §2 bảng trên | K | Ngày/HTTP khớp lần mở này |

**Tổng Patel: 42 dòng — K 40 · MH 2 · S 0 · KKĐ 0.**

## 4. Sunmola — bảng chấm từng dòng
| # | Dòng (tệp) | Nguồn kiểm, trích ngắn | Chấm | Ghi chú |
|---|---|---|---|---|
| S1 | Ký hiệu tầng (d.6) | N2 tr. 3 "Three days into trial, Sunmola openly pleaded guilty to all counts… without a plea agreement"; tr. 5 "324 months"; tr. 1 "DECIDED APRIL 16, 2018"; tr. 18 "AFFIRM" | K | |
| S2 | §0 giới hạn (dẫn N2 tr. 2, tr. 8; N1) | N2 tr. 2 (đoạn khai thác tình dục, có bang); tr. 8 (ca cụ thể có tuổi + hoàn cảnh); N1 đ.2 (tên giả), đ.8 (váy cưới, ý nghĩ tự sát) | K | Mô tả đúng chỗ cần tránh (không chép chi tiết ở đây) |
| S3 | Logline VI | N2 tr. 2 "from the Republic of South Africa, targeting middle-aged women in the United States… under fictitious names"; tr. 10 (soldier / colonel; "money or equipment… work-related purposes"); tr. 3 (London; nhận 8 tội); tr. 5; tr. 18 | K | |
| S4 | Logline EN | N2 tr. 10 "In some instances… American soldier… In other instances… colonel in the U.S. Army deployed to South Africa"; tr. 2; tr. 5 / N1 đ.11 "27-year prison term" | K | Sự việc do toà phúc thẩm mô tả khi giữ nguyên tăng nặng (●C) — nói thẳng không nâng tầng |
| S5 | H1 (cảnh) | — | K | Chữ chat mờ, không logo |
| S6 | H2 | N2 tr. 10 "pretended to be an American soldier, stranded in Nigeria on a mission… held himself out as a colonel in the U.S. Army deployed to South Africa… purchase and ship computer equipment to him to help him finish his assignments" | K | |
| S7 | H3 | N2 tr. 2 "Starting in March 2008… from the Republic of South Africa, targeting middle-aged women in the United States"; tr. 10 "misrepresented to his victims that he was acting on behalf of… the U.S. military" | K | Câu 8e có |
| S8 | H4 | N1 đ.2 "Sunmola's purpose was to lead each of his victims to believe that he was her 'Prince Charming'" | K | ◐D, chủ thể "Prosecutors said" |
| S9 | H5 | N2 tr. 4 (phiên 02/02/2017), tr. 5 "324 months' imprisonment"; N1 (02/02/2017) đ.1 "sentenced this morning to serve 324 months" | K | |
| S10 | H6 | N2 tr. 17 "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being" | K | Trích đúng từng chữ |
| S11 | Ghi chú H6 | N1 đ.10 "…without laying hands or even eyes…"; tiêu đề N1 "Nigerian Romance Scammer" | K | |
| S12 | Nhịp 1 | N1 đ.2 "began investigating Sunmola in 2012, when a woman in the Southern District of Illinois complained… one of the dozens of fictitious online profiles Sunmola and his confederates concocted" | K | Tên giả, tên trang hẹn hò không dùng — đúng |
| S13 | Nhịp 2 | N2 tr. 2 "created profiles… under fictitious names and led women to believe they were successful businessmen. Sunmola often used pictures of men in U.S. military uniforms"; N1 đ.2 "photographs stolen from the hacked online accounts of real American men"; N1 đ.1 "from 2007 to 2014" | K | Hai vế tách đúng; mốc 3/2008 của toà |
| S14 | Nhịp 3 | N1 đ.2 "showered the women with poetry, cards, flowers, stuffed animals, and chocolates"; "researched facts about the American cities he pretended to be from" | K | |
| S15 | Nhịp 4 | N2 tr. 2 "After gaining the women's trust… ask for money and merchandise… ship electronics and make electronic fund transfers under the false claims of financial distress"; tr. 10 | K | |
| S16 | Nhịp 4b | N1 đ.3–4 "manufacture phony emergencies, each of which required increasingly large amounts… direct their shipments to 'Ilumsa Sunmola,' who was passed off as their lover's driver, or a co-worker, or a hotel manager. In fact, it was Sunmola himself… abruptly end the relationship" | K | N2 tr. 14 có tên dịch vụ chuyển tiền — tệp không nêu, đúng |
| S17 | Nhịp 5 | N2 tr. 11–12 "recruited accomplices, placed the orders for merchandise… received the stolen goods and wire transfers, and directed everyone else on what to tell the victims… evidence suggesting that Sunmola commanded a larger share"; tr. 2 "evidence of credit card fraud affecting various businesses"; N1 đ.7 "over $800,000" | K | "gây thiệt hại" cho "affecting" — N1 đ.7 "businesses were also defrauded" đỡ; chấp nhận |
| S18 | Nhịp 6 (một câu) | N2 tr. 2 "threatened to post photos of a third woman" | K | Câu nói **ít** hơn nguồn ("at least one"), không mô tả; không nối với Count Eight — đúng |
| S19 | Nhịp 7 | N1 đ.6 "at least three women to file for bankruptcy. Several more lost their jobs and their homes"; N2 tr. 4 "two upward departures the Government requested, one for psychological injury… a second for gratuitous infliction of injury"; tr. 5 (danh sách điểm kháng cáo không có hai lần này); tr. 6 "listed seven victims who suffered substantial financial hardship" / "five or more victims" | K | |
| S20 | Nhịp 8 | N2 tr. 3 "On November 20, 2013… eight-count indictment… conspiracy… mail fraud (Counts Two through Four); wire fraud (Counts Five through Seven); interstate extortion (Count Eight)… August 9, 2014… traveling in London… February 26, 2015"; N1 đ.5 "about to board a plane from London to Johannesburg" | K | |
| S21 | Nhịp 9 | N2 tr. 3 "Trial commenced on February 29, 2016… ensure he knowingly and voluntarily entered the pleas… accepted the guilty pleas without a plea agreement"; N1 đ.5 "March 2, 2016, after two full days of trial" | K | |
| S22 | Nhịp 10 | N2 tr. 3–4 (12/8/2016; 02/02/2017; 39 nạn nhân bổ sung; các mức tăng nặng; "intended loss of $2,054,972.66"); tr. 5 "$1,707,260.98… amended… $1,669,050.98"; tr. 14 "39 additional victims beyond the 13 listed in the PSR… around $1.7 million was an underestimate" | K | Hai số thiệt hại tách đúng |
| S23 | Nhịp 11 | N2 tr. 1; tr. 8 "chose the women… specifically targeting women they believed would be susceptible… Many of these women had been divorced, abandoned, widowed, or ignored by the men in their lives… most of the targeted women were middle-aged rather than elderly"; tr. 18 | K | Không dùng ca cụ thể — đúng |
| S24 | Nhịp 11b | N1 đ.11 "removed to his native home of Nigeria… Over $200,000 in proceeds from the sale of Sunmola's four properties in South Africa… disbursed to the individual identified victims"; N2 tr. 4 "$220,000 liquidated assets" | K | |
| S25 | Ghi chú dòng 54–55 (lời người thật; đồng phạm) | N1 đ.6 (câu nạn nhân — không dùng); N2 tr. 11–12 | K | |
| S26 | Cú treo | N2 tr. 3; tr. 1 (S.D. Ill.) | K | "would not make it to a verdict" đúng (nhận tội ngày thứ ba) |
| S27 | L1 | N2 tr. 11–12 | K | "có thể không phải một người" là suy luận có rào ("có thể"), tựa "directed everyone else on what to tell the victims" |
| S28 | L2 | N2 tr. 8–9; N6 "the elderly, women, and those who have lost a spouse are often targeted" | K | Câu "lời của kênh" không bị gắn nguồn |
| S29 | L3 | N2 tr. 4 (psychological injury); tr. 14 "attempted to contact many other individuals, but he was unable to reach all" | K | Câu "lời khuyên chung của kênh" không bị gắn nguồn |
| S30 | D (5 dấu hiệu) | (1) N2 tr. 10; N1 đ.2 "engineer working on a large government contract"; N6 "claims to be a U.S. service member serving overseas" · (2) N2 tr. 2, 10; N1 đ.4 "cell phones"; N6 "Asks for money, goods" · (3) N1 đ.4 · (4) N1 đ.3–4; N6 "sudden personal crisis… increasingly aggressive" · (5) N2 tr. 2; N1 đ.2; N6 "Most cyber criminals do not use their own photographs" | K | Không nhắc nhánh ảnh riêng tư |
| S31 | P (nguyên tắc) | N6 "Never send money to someone you meet online, especially by wire transfer"; N6 "reverse image search…"; N6/N7 báo IC3; N8 | **MH** | Vế đầu "Không gửi tiền **hay hàng** cho người chỉ quen trên mạng, chưa gặp trực tiếp" được gắn "(FBI, N6)": lời khuyên "Never" của FBI chỉ nói **tiền**; "goods… never met in person" ở N6 là **dấu hiệu** ("Asks for money, goods…"), không phải lời khuyên "never" → gắn nguồn rộng hơn nguồn |
| S32 | Thẻ tổng kết EN | N2 tr. 11–12; tr. 8–9 "seeking companionship through online dating"; tr. 4, 14; N1 đ.3–4; N6 | K | Không nhắc nhánh ảnh riêng tư |
| S33 | Rà (a) | N2 tr. 1, 3, 5, 18 | K | |
| S34 | Rà (b) | — | K | Không có người/tổ chức có tên ở ◐ |
| S35 | Rà (c) | N1 đ.2 (tên trang hẹn hò), đ.7; N2 tr. 14 | K | |
| S36 | Rà (d) | tiêu đề N1; N2 tr. 3 (tội danh) | K | |
| S37 | Rà (e) | N2 tr. 10 | K | |
| S38 | Rà (f) | N2 tr. 8 | K | |
| S39 | KBCB | N2 tr. 4, 14 (tên điều tra viên), N1 đ.9 (tên chuyên gia) | K | Tệp không nêu tên — đúng |
| S40 | §5 tình dục | N2 tr. 2 "middle-aged women"; tr. 8 "middle-aged rather than elderly"; tìm "minor/child/juvenile/teen/underage/girl" trong N2 và N1: 0 kết quả liên quan | K | |
| S41 | §7 nguồn N6–N8 | như §2 bảng trên | K | |

**Tổng Sunmola: 41 dòng — K 40 · MH 1 · S 0 · KKĐ 0.**

## 5. Hướng dẫn làm / lời gọi / §5 / nhận diện
- **Patel — lời gọi:** không có câu thoại của "người gọi", không giọng đóng vai, không chữ kịch bản trên màn hình (H1 chỉ "Unknown"; H2 tóm tắt lời doạ ở ngôi thứ ba; nhịp 3/3b chỉ nêu loại kịch bản, không nội dung). **Đạt.**
- **Patel — hướng dẫn làm (HIEN-CHUONG §1):** vai chỉ tên + một câu chức năng; không cách đăng ký/rút thẻ, không nguồn mua dữ liệu, không vận hành hawala (chỉ định nghĩa khái niệm "không thực sự chuyển tiền đi"), không số điện thoại; N3 đ.14 và N1 ¶2(a),(e),(f) được đánh dấu cấm chép; không nêu cách trả 276 thẻ. Phép thử "làm theo được ngay": **Không. Đạt.**
- **Patel — nhận diện nạn nhân:** chỉ tuổi + số tiền; thành phố (có trong N2 đ.11–12) đã bỏ; cấm dùng ảnh chụp thông cáo. **Đạt.**
- **Sunmola — §5:** nhánh đe doạ ảnh riêng tư đúng **một câu khái niệm** (nhịp 6), thẻ chữ, không mô tả, không dựng, không trích câu đe doạ; không lặp ở L, D, P, thẻ tổng kết, cú treo (đã rà toàn tệp: chỉ còn mô tả giới hạn ở §0, rà §5 và §8 — văn bản nội bộ, không phải lời). Nạn nhân người lớn (N2 tr. 2, 8); không thấy dấu hiệu vị thành niên. **Đạt.**
- **Sunmola — nhận diện:** không tên, không bang, không tổ hợp tuổi + hoàn cảnh (tr. 8 chỉ dùng câu khái quát), không trích lời nạn nhân, không số tiền từng người; nhân vật minh hoạ tổng hợp có nhãn. **Đạt.**
- **Sunmola — hướng dẫn làm:** không mẫu tin nhắn/thơ/hồ sơ, không cách lấy ảnh, không cách mua dữ liệu thẻ hay chọn cửa hàng nhận hàng (N2 tr. 11), không tên dịch vụ chuyển tiền. Nhịp 4b ("gửi cho người thứ ba") ở mức khái niệm, dùng làm dấu hiệu. **Đạt.**
- **Luật 8 a–f, luật 5:** cả hai tệp đạt (8d: không gán "scammer/con man/boss" ở giọng kể; 8e: IRS, USCIS, CRA, ATO, U.S. Army có câu không liên quan; người chưa kết luận không tên, ngoại lệ HGLOBAL có lý do — nằm trong lời nhận tội theo DOJ — và câu ◐ gắn mốc).

## 6. Tổng điểm
| Vụ | Dòng | K | MH | S | KKĐ |
|---|---|---|---|---|---|
| Patel | 42 | 40 | 2 | 0 | 0 |
| Sunmola | 41 | 40 | 1 | 0 | 0 |

## 7. Sửa bắt buộc
1. **Patel P2 — Logline VI:** thêm chủ thể DOJ cho các vế ●T, vd: "Theo DOJ, từ 2013 đến 2016, các call center ở Ahmedabad… Hitesh Madhubhai Patel — người, **theo DOJ**, đã thừa nhận điều hành và cấp vốn cho nhiều call center trong số đó — …".
2. **Patel P30 — L2:** đổi "IRS nói rõ không gọi đòi trả bằng thẻ trả trước, thẻ quà tặng hay chuyển tiền (N9)" thành "IRS nói rõ không gọi để đòi trả **ngay** bằng một phương thức chỉ định như thẻ trả trước, thẻ quà tặng hay chuyển tiền (N9)" (khớp L3).
3. **Sunmola S31 — P:** tách: "Không gửi tiền cho người chỉ quen trên mạng (FBI, N6: 'Never send money to someone you meet online')" · "người chưa gặp trực tiếp mà xin tiền hay hàng là dấu hiệu (N6 'Asks for money, goods… especially if you have never met in person')"; hoặc ghi vế "hay hàng" là lời khuyên chung của kênh, không gắn FBI.

Góp ý không bắt buộc (không tính MH): Patel P — ghi rõ "Cúp máy; tự tra số chính thức…" là lời khuyên chung của kênh, như vế "nói trước với người thân".
