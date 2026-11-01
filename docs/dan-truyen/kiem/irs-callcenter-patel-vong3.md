# Kiểm độc lập vòng 3 — Dàn truyện `irs-callcenter-patel`

> Tệp được kiểm: `docs/dan-truyen/irs-callcenter-patel.md` (bản trong cây làm việc ngày 01/11/2026). Người kiểm: tác tử kiểm độc lập, vòng 3. Không sửa tệp được kiểm; không commit/push. Chi 0 USD (không gọi API trả tiền, không PACER).

## 1. Phạm vi đọc
- Đã đọc: `CLAUDE.md`, `docs/HIEN-CHUONG.md`, toàn bộ tệp được kiểm, `docs/kho-de-tai/irs-callcenter-patel.md` **chỉ §8**.
- Không đọc: `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 tệp kho, dàn truyện khác, `docs/dan-truyen/kiem/**` (ngoài tệp này do tôi viết), git log/diff.

## 2. Nguồn đã mở (01/11/2026)
| Mã | Đường mở | Kết quả |
|---|---|---|
| N1 | Tệp repo `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf`; `pdftoppm -r 80 -gray` tr. 1, 3, 4, 5, 6, 7, xem ảnh | SHA-256 `04fb7cb3c4cfda5b444a66c9415878635346dfb1f6c3333e5acf41867a7b2bdf` — **khớp** kho §8; `pdfinfo` 81 trang |
| N2 | API `justice.gov/api/v1/press_releases.json`, tiêu đề "Dozens of Individuals Indicted…" | HTTP 200, số 16-1257, ngày 27/10/2016 |
| N3 | như trên, "24 Defendants Sentenced…" | HTTP 200, số 18-961, ngày 20/07/2018 |
| N4 | như trên, "Indian National Pleads Guilty to Owning, Funding" | HTTP 200, số 20-19, ngày 09/01/2020 |
| N5 | như trên, "Owner and Operator of India-Based Call Centers Sentenced" — chọn bản số 20-1294 (API trả 3 bản; 2 bản không số bỏ qua) | HTTP 200, ngày 30/11/2020 |
| N9 | https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door (curl mặc định) | HTTP 200; FS-2017-7, April 19, 2017 |
| N10 | https://reportfraud.ftc.gov/ | HTTP 200; trang ứng dụng JS, chỉ đọc được `<title>` "ReportFraud.ftc.gov" và mô tả "Protect your community by reporting fraud, scams, and bad business practices" |
| N11 | https://www.tigta.gov/reportcrime-misconduct | HTTP 200; có mục "Someone is impersonating an IRS or Treasury employee." |
| (bổ sung, để kiểm dòng trạng thái §2 cuối) | https://www.justice.gov/pardon/pardons-granted-president-donald-j-trump-2017-2021 và …/commutations-granted-president-donald-j-trump-2017-2021 | HTTP 200 ×2; tìm "Hitesh", "Hinglaj", "Patel": 0 kết quả |

Quy ước: đ.n = thẻ `<p>` không rỗng thứ n trong `body` (đã đếm lại bằng script; `<li>` ghi riêng, không tính vào n). Số đoạn tệp được kiểm dùng **khớp** cách đếm này ở mọi chỗ đã dò.

## 3. Bảng chấm từng dòng
K = khớp · MH = mạnh hơn nguồn · S = sai · KKĐ = không kiểm được.

| Dòng | Điểm | Bằng chứng (nguồn, trang/đoạn) | Ghi chú |
|---|---|---|---|
| Logline VI | K | N4 đ.1 ("between 2013 and 2016"), đ.5 (IRS/USCIS, "arrest… deportation", "GPR cards or wiring money", "immediately turn to a network of 'runners'… liquidate and launder"), đ.6 ("operating and funding several"), đ.9 (Singapore, dẫn độ); N1 tr. 1 "HOUSTON DIVISION"; N5 đ.1 (20 năm) | Câu VI nội bộ, không thu âm; vế đầu (gọi, giả IRS/USCIS) chưa gắn "theo DOJ" — khi chuyển sang EN phải gắn (xem dòng kế) |
| Logline EN | **MH** | N4 đ.5 | Câu 1 ("The caller claimed to be from the IRS, and said you'd be arrested…") và câu 3 ("The call came from India.") là nội dung ●T (lời nhận tội theo DOJ) nhưng **không có chủ thể** "according to the Justice Department"; chủ thể chỉ xuất hiện ở câu 4. Trái quy ước ●T của chính tệp (dòng 6) |
| H1 | K | — | Cảnh MH, không sự việc |
| H2 | K | N4 đ.5 ("throughout the United States", "impersonated officials from the IRS and… USCIS", "threatened with arrest, imprisonment, fines or deportation if they did not pay") | Có chủ thể DOJ |
| H3 | K | N1 tr. 3 ¶1(a)–(b) ("impersonated"); N4 đ.5 | Câu không liên quan (8e) |
| H4 | **MH** | N4 đ.5, đ.6 | Câu 1 "The calls came from call centers in Ahmedabad, India." là ●T (N4 đ.5 nằm trong "According to admissions…"), đứng riêng sau H3, **không có chủ thể**; chủ thể DOJ chỉ gắn ở câu 2 |
| H5 | K | N5 đ.1 ("20 years in prison… in the Southern District of Texas"), đ.2 (Judge Hittner); ngày N5 = 30/11/2020 | |
| H6 | K | N4 đ.5 ("immediately") | Câu hỏi dẫn |
| Nhịp 1 | K | N2 đ.11 ("According to the indictment… extorted $12,300 from an 85-year-old victim… threatening her with arrest… fictitious tax violations") | ◐ đúng; đã bỏ thành phố |
| Nhịp 1b | K | N2 đ.12 ("The indictment also alleges… $136,000… called multiple times over a period of 20 days") | ◐ đúng |
| Nhịp 2 | K | N1 tr. 1 ("Filed in TXSD on 10/19/16", "Unsealed 10/27/16"), tr. 3 ("SUPERSEDING INDICTMENT"); N2 đ.1 (61 cá nhân và tổ chức; 20 bị bắt "today"; 32 người + 5 call center ở Ấn Độ; "tens of thousands", "hundreds of millions"), đ.8 (grand jury S.D. Tex., Oct. 19, 2016) | Số nạn nhân/thiệt hại gắn ◐ "alleged at the time" — đúng |
| Nhịp 3 | K | N1 tr. 3 ¶1(a) ("arrested and fined if they did not pay their alleged back taxes immediately"), (b) ("deported unless they paid a fine immediately"), (c) tr. 3–4 ("upfront 'worthiness fee' to demonstrate an ability to repay"; "received nothing in return"), (d) tr. 4 ("upfront IRS tax or processing fee") | ◐ "the indictment described" |
| Nhịp 3b | K | N4 đ.6 ("The scripts included IRS impersonation, USCIS impersonation, Canada Revenue Agency (CRA) impersonation, Australian Tax Office (ATO) impersonation, payday loan fraud, U.S. Government grant fraud, and debt collection fraud") | Xếp ◐ (câu nằm sau vế "admitted") — thận trọng, đúng; có câu 8e |
| Nhịp 4 | K | N1 tr. 4 ¶2(a) Runner, (b) Domestic Manager; tr. 5 (c) Call Center Operator, (d) Caller, (e) Payment Processor; tr. 6 (f) Data Broker ("purchase names and PII"), (g) Hawaladar ("a person who operates a 'hawala'") | Đủ 7 vai, đúng chức năng |
| Nhịp 4b | **MH** | N1 tr. 6–7 ¶3 ("five major conglomerates of call centers, all located in Ahmedabad… often acted together… sharing call scripts and lists of potential victims, processing payments for each other"); N1 tr. 1 (HGLOBAL là [1]); N5 đ.12 | Phần mô tả ¶3: K. Câu EN "as of November 2020, **charges against India-based defendants remained pending**" bỏ chữ "**other**" của N5 đ.12 ("Charges remain pending for **other** India-based defendants") → khái quát thành toàn bộ bị cáo ở Ấn Độ (kể cả Patel, khi ấy đã bị tuyên án) và, đặt ngay sau "HGLOBAL was also charged", ngụ ý **riêng HGLOBAL** còn treo tới 11/2020 — N5 không nêu trạng thái HGLOBAL. Nguồn có trạng thái 5 call center chỉ là N3 đ.15 (07/2018, "have yet to be arraigned") |
| Nhịp 5 | K | N4 đ.5 (●T: "instructed how to provide payment, including by purchasing general purpose reloadable (GPR) cards or wiring money. Upon payment, the call centers would immediately turn to…"); N2 đ.9 (◐ "often registered using misappropriated personal identifying information"), đ.10 (◐ hawala "outside of the formal banking system"; người nhận "not aware of the illicit nature"); N1 tr. 6 ¶2(g) ("made available internationally without actually moving it") | Tách đúng ●T/◐; khung "đưa vào → phân lớp" ghi rõ là của kênh |
| Nhịp 6 | **MH** | N4 đ.2 (aka Hitesh Hinglaj, of Ahmedabad), đ.6 ("In his plea, Patel admitted to operating and funding several India-based call centers… including the call center HGLOBAL"), đ.7 (báo cáo thu chi qua email cá nhân); N1 tr. 7 (bảng HGLOBAL: "HITESH PATEL (a.k.a. HITESH HINGLAJ) — Call Center Operator — India") | Phần sự việc: K. Vế "HGLOBAL… **chưa kết luận tới 11/2020**" là **suy diễn trạng thái** của một tổ chức có tên: N5 đ.12 chỉ nói "other India-based defendants" còn treo, không nêu HGLOBAL; nguồn gần nhất có trạng thái call center là N3 đ.15 (07/2018) |
| Nhịp 6b | **MH** | N4 đ.8 ("A co-defendant described Patel as 'the top person in India and the boss for whom most of the other defendants worked'") | Trích đúng. Nhưng dòng chữ trên hình "a co-defendant **told investigators**, according to the Justice Department" thêm **người nghe** (investigators) không có trong nguồn — N4 đ.8 chỉ có "described" |
| Nhịp 7 | K | N3 đ.1 (21 người tuần đó ở Houston trước Hittner + 3 người trước đó; "up to 20 years"), đ.9 (co-owner and manager of an India-based call center), đ.11 (22 người liên đới bồi hoàn $8,970,396), danh sách sau đ.13 (Houston 23/3, Atlanta 14/2, Phoenix 29/1) → 22 Houston/1 Atlanta/1 Phoenix; N4 đ.11 ("24 domestic defendants… Southern District of Texas, District of Arizona and Northern District of Georgia") | Theo nhóm, không tên — đúng |
| Nhịp 7b | K | N3 đ.15 ("32 India-based conspirators and five India-based call centers… have yet to be arraigned… presumed innocent") | |
| Nhịp 8 | **MH** (cột Hình) | N4 đ.9 ("Singapore authorities apprehended Patel… provisional arrest warrant in September 2018, after Patel flew there from India"; "extradited from Singapore in April 2019") | Cột "Sự việc": K. Cột "Hình": bản đồ "**Ahmedabad** → Singapore → **Houston**" gắn hai **địa điểm suy diễn**: nguồn chỉ nói bay "from India" (không nói từ Ahmedabad) và dẫn độ sang Hoa Kỳ (không nói tới Houston). Chính tệp đã tránh "Houston" ở H5 vì lý do tương tự |
| Nhịp 9 | K | N4 đ.1–2 (tội danh), đ.10 (Hittner "accepted the plea today"; ngày N4 = 09/01/2020), đ.8 ("reasonably foreseeable loss of more than $25 million but less than $65 million… based on the government's evidence against him") | Ghi chú 8d đúng |
| Nhịp 10 | K | N5 đ.1 (20 năm + 3 năm giám sát), đ.2 (Hittner; "$8, 970,396" — lỗi gõ khoảng trắng của DOJ, số = 8.970.396) | |
| Nhịp 10b | K | N5 đ.12 ("Charges remain pending for other India-based defendants. They are presumed innocent…") | Trích có "other" — đúng; gắn mốc 11/2020 |
| Nhịp 11 | K | §4 | Thẻ tổng kết |
| Cú treo | K | N3 đ.1, đ.13 (24 người ở Mỹ, 07/2018); N4 đ.6 ("operating and funding", chủ thể DOJ có), đ.9 (tháng 9/2018 bị bắt sau khi bay từ Ấn Độ, theo yêu cầu của Mỹ), đ.11 ("24 domestic defendants") | Không nói nơi ở 07/2018 — đúng |
| L1 | **MH** | N1 tr. 4–6 ¶2 (vai); N1 tr. 5 ¶2(d) ("Callers received lead list information and call scripts") | Nội dung vai: K. Nhưng câu bài học viết **khái quát tuyệt đối**, không gắn vụ và không gắn ◐: "Cuộc gọi **chỉ là** mặt tiền của một dây chuyền… Người nghe máy đang đối mặt cả một tổ chức có kịch bản, không phải một kẻ đơn độc." Nguồn chỉ mô tả (◐, theo cáo trạng) dây chuyền **trong vụ này**; thẻ EN đã viết đúng "In this case", nhưng dòng L1 (căn cứ cho phiên kịch bản) thì chưa |
| L2 | K | N4 đ.5 ("immediately"); N3 đ.14 ("as quickly as possible by purchasing reloadable cards or retrieving wire transfers"; "Apple iTunes or other gift cards"); N9 ("does not: Call to demand immediate payment using a specific payment method such as a prepaid debit card, gift card or wire transfer") | Có "trong vụ này"; khung rửa tiền ghi rõ của kênh. Lưu ý chính xác: N9 nói IRS không **gọi đòi trả ngay** bằng phương thức cụ thể — phiên kịch bản giữ vế "demand immediate payment" |
| L3 | K | N9 ("initiates most contacts through regular mail…"; "generally first receive several letters"; ba gạch "does not"; "make payments to the 'United States Treasury'"); N2 đ.5 (lời HSI "U.S. government agencies do not make these types of calls") | |
| D(1) Doạ bắt/phạt/trục xuất | K | N4 đ.5; N1 tr. 3 ¶1(a)–(b); N9 | |
| D(2) Đòi trả ngay, không cho hỏi lại | K | N1 tr. 3 ¶1(a)–(b) "immediately"; N9 ("without the opportunity to question or appeal") | Có thể thêm N3 đ.8 ("would be arrested or deported if they did not pay immediately" — ●N, factual basis plea) |
| D(3) Đòi phương thức trả cụ thể | K | N4 đ.5; N3 đ.14; N9 | |
| D(4) Gọi lại nhiều lần | K | N2 đ.12 (◐) | Ghi rõ "một trường hợp cáo trạng mô tả" |
| D(5) Vay/trợ cấp đòi phí trước | K | N1 tr. 3–4 ¶1(c)–(d) (◐) | |
| P | K | N9 (gift card); N3 đ.3 (Sessions: "older Americans, legal immigrants and many others"); N11 (mục "Someone is impersonating an IRS or Treasury employee"); N10 (trang báo cáo gian lận FTC); N9 cũng chỉ TIGTA và FTC | Câu "nói trước với người thân" tự ghi là lời khuyên chung của kênh — không gắn nguồn sai |
| Thẻ tổng kết EN | K | Ý 1: N1 tr. 4–6 + tội âm mưu rửa tiền đã kết án (N3 đ.8, danh sách; N5 đ.2 — "general conspiracy to commit… money laundering"); ý 2: N4 đ.5, N3 đ.14; ý 3: N9 ("generally… letters"; không gọi đòi trả bằng gift card; không doạ cho cảnh sát tới bắt) | "In this case" và "generally" giữ đúng mức |
| §5 (a) | K | N4 đ.10; N5 đ.1–2 | |
| §5 (b) | **MH** | N5 đ.12; N3 đ.15 | "Các bị cáo và call center ở Ấn Độ (**chưa xử tới 11/2020**)" — cùng gốc với 4b/6: N5 chỉ nói "other India-based defendants" còn treo, không nói toàn bộ, không nói từng call center |
| §5 (c)–(f), KBCB, §5 tình dục, phép thử | K | N1 tr. 1 (d.b.a. trùng thương hiệu lớn), N3 đ.14 (tên thương hiệu thẻ quà tặng), N4 đ.6 (tên ứng dụng nhắn tin) — đều không nêu | |
| §2 cuối: trạng thái ân xá Trump 2017–2021 | K | Tự mở 2 trang Pardon Attorney 2017–2021: 0 kết quả "Hitesh/Hinglaj/Patel" | |
| §2 cuối: BOP, kháng cáo | KKĐ | Ngoài danh sách nguồn vòng này; tệp đã tự ghi "chưa kiểm", không đưa vào lời | Không chấm vào tổng nội dung |
| §1 ghi chú H2: "Vế 'ngay lập tức' **chỉ có** trong cáo trạng N1 tr. 3" | ghi chú nguồn (không chấm) | N3 đ.8 cũng có "if they did not pay immediately" (factual basis plea của một bị cáo đã kết án) | Câu ghi chú sai nhẹ về phạm vi nguồn nhưng làm lời **yếu hơn**, không mạnh hơn; nên sửa cho chính xác |

## 4. Hướng dẫn làm · lời gọi · nhận diện nạn nhân
- **Hướng dẫn làm (HIEN-CHUONG §1): Đạt.** Nhịp 4 chỉ tên vai + một câu chức năng; nhịp 5 nêu thẻ GPR, đăng ký bằng PII bị đánh cắp, hawala bù trừ ở mức khái niệm, không có trình tự (không cách mua/đăng ký/nạp/rút thẻ, không cách đổi money order, không nguồn mua "lead list"). Tệp đã cảnh báo đúng các đoạn nguồn có trình tự thao tác (N3 đ.14; N1 tr. 4–6 ¶2(a), (e), (f)).
- **Lời gọi chép dùng được: Không có.** Không câu thoại, không giọng đóng vai, không chữ kịch bản trên màn hình; H2 tóm ở ngôi thứ ba; nhịp 3 chỉ tên loại mánh; không số điện thoại kẻ gian. Đạt.
- **Nhận diện nạn nhân: Đạt.** Nhịp 1/1b bỏ thành phố, chỉ còn tuổi + số tiền (N2 đ.11–12 công khai thành phố, nhưng tệp cấm ảnh chụp thông cáo); không tên, không mặt.
- **8d:** không gán "scammer/con man/con artist" cho Patel hay ai; "boss" chỉ trong chữ trích có chủ thể. **8e:** IRS, USCIS (H3), CRA, ATO (3b) có câu không liên quan; thương hiệu trùng d.b.a., thẻ quà tặng, ứng dụng nhắn tin không nêu. **Luật 5/8c:** chỉ nêu tên HGLOBAL (ngoại lệ có lý do: nằm trong lời nhận tội, N4 đ.6) kèm câu ◐ — đạt về nguyên tắc, nhưng câu ◐ đó hiện mạnh hơn nguồn (mục 3: 4b, 6, §5b).

## 5. Tổng
Tổng số dòng chấm (nội dung): **40** — **K 32 · MH 8 · S 0 · KKĐ 0** (thêm 1 KKĐ ngoài nội dung: BOP/kháng cáo, đã tự khai chưa kiểm; 1 ghi chú nguồn không chấm).

MH: Logline EN · H4 · 4b · 6 · 6b · 8 (cột Hình) · L1 · §5(b). Bốn trong đó (4b, 6, §5b) cùng một gốc: trạng thái bị cáo ở Ấn Độ/HGLOBAL.

**Kết luận vòng 3: chưa đạt 0 MH.** Không có S.

## 6. Sửa bắt buộc
1. **Logline EN:** mở bằng chủ thể DOJ cho cả câu 1 và 3, vd: *"According to the Justice Department, callers posing as the IRS told people they'd be arrested if they didn't pay — and the calls came from India. The IRS had nothing to do with it. One man admitted operating and funding several of those call centers…"*
2. **H4:** gộp chủ thể: *"According to the Justice Department, the calls came from call centers in Ahmedabad, India — and one man admitted to operating and funding several of them."*
3. **4b, 6, §5(b) (trạng thái HGLOBAL/bị cáo Ấn Độ):** giữ đúng chữ "other" của N5 đ.12 và không gán trạng thái riêng cho HGLOBAL. Đề xuất EN: *"HGLOBAL was also charged in the indictment and is presumed innocent. As of July 2018, the India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants."* (N3 đ.15; N5 đ.12). Ở nhịp 6 và §5(b) VI: thay "chưa kết luận tới 11/2020" bằng "bị truy tố; 07/2018 chưa ra hầu toà (N3 đ.15); trạng thái sau đó chưa có nguồn".
4. **6b:** bỏ "told investigators" → *"a co-defendant described him, according to the Justice Department"*.
5. **Nhịp 8 (Hình):** bản đồ "India → Singapore → United States" (hoặc nhãn "S.D. Tex." cho nơi xét xử, không mũi tên "tới Houston"); không đặt điểm xuất phát ở Ahmedabad.
6. **L1:** gắn vụ và tầng: "**Trong vụ này, theo cáo trạng**, cuộc gọi là mặt tiền của một dây chuyền…; người nghe máy khi đó đối mặt một tổ chức có kịch bản (N1 tr. 5 ¶2(d))" — bỏ "chỉ là" và mệnh đề khái quát "không phải một kẻ đơn độc" hoặc giới hạn vào vụ.

Không bắt buộc (chính xác nguồn): sửa ghi chú H2 "chỉ có trong cáo trạng" → "có ở N1 tr. 3 (◐) và N3 đ.8 (●N, factual basis của một bị cáo khác); không có trong N4 đ.5"; D(2) có thể thêm N3 đ.8.
