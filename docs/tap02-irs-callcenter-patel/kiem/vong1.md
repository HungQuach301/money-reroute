# Kiểm lời độc lập (K-lời) — Tập 2 `tap02-irs-callcenter-patel` — Vòng 1

- **Thời điểm kiểm:** 2026-11-01 23:23–23:40 UTC.
- **Đối tượng:** `docs/tap02-irs-callcenter-patel/loi.json` (bản "MR-K23 nháp G1", 71 câu S001–S071). Không sửa loi.json, không commit.
- **Cách làm:** chấm độc lập. Chỉ đọc `docs/HIEN-CHUONG.md`, `NGUON.md` và loi.json. Không đọc dan-truyen, kho-de-tai hay reports. Mọi nguồn được mở lại trong thư mục tạm riêng; Python chạy với `-I`.

## Nguồn đã mở thực sự

| Mã | Nguồn | Cách mở | Kết quả |
|---|---|---|---|
| N1 | `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` | `sha256sum` khớp NGUON (`04fb7cb3…7b2bdf`); 81 trang; render tr. 1, 3, 4, 5, 6, 7 bằng `pdftoppm -r 80 -gray` rồi đọc ảnh | Đã đọc. Tr. 1: "Unsealed 10/27/16", FILED October 19, 2016, danh sách bị cáo ([1] HGLOBAL, [6] Hitesh Madhubhai Patel). Tr. 3–4: ¶1(a)–(d). Tr. 4–6: ¶2(a)–(g). Tr. 6–7: ¶3. Tr. 7: bảng HGLOBAL |
| N2 | DOJ OPA 16-1257, `https://www.justice.gov/archives/opa/pr/dozens-individuals-indicted-multimillion-dollar-indian-call-center-scam-targeting-us-victims` | API `justice.gov/api/v1/press_releases.json`, tham số `parameters[title]`, curl mặc định | HTTP 200; trường body giống hệt bản lưu trong repo; 18 đoạn |
| N3 | DOJ OPA 18-961, `…/archives/opa/pr/24-defendants-sentenced-multimillion-dollar-india-based-call-center-scam-targeting-us-victims` | như trên | HTTP 200; body giống bản repo; 19 đoạn + 21 `<li>` |
| N4 | DOJ OPA 20-19, `…/archives/opa/pr/indian-national-pleads-guilty-owning-funding-and-operating-india-based-call-centers-scammed` | như trên | HTTP 200; body giống bản repo; 16 đoạn |
| N5 | DOJ OPA 20-1294, `…/archives/opa/pr/owner-and-operator-india-based-call-centers-sentenced-prison-scamming-us-victims-out-millions` | như trên | HTTP 200; body giống bản repo; 17 đoạn |
| N9 | IRS FS-2017-7, `https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door` | curl mặc định | HTTP 200 (109.882 byte) |
| N10 | `https://reportfraud.ftc.gov/` | curl mặc định | HTTP 200. Trang là ứng dụng JS; chỉ đọc được `<title>ReportFraud.ftc.gov` và meta "Protect your community by reporting fraud, scams, and bad business practices" |
| N11 | `https://www.tigta.gov/reportcrime-misconduct` | curl mặc định | HTTP 200; mục "IRS Scams and Fraud": "Someone is impersonating an IRS or Treasury employee." |

Cách đánh đoạn: đ.n là thẻ `<p>` thứ n không rỗng trong body của bản OPA. Cách đánh khớp với ghi chú của NGUON.md (N4 đ.5 "According to admissions…", N5 đ.12 "The indictment in this case…").

**Chưa mở được hoặc không mở:** N6, N7, N8 không có câu nào trong lời dùng tới, nên không mở. Không gặp nguồn nào trả 403 hay CAPTCHA. Không đổi user-agent, không gửi thông tin cá nhân, không gọi API trả tiền.

Viết tắt: **LTĐ** = Làm theo được ngay (phép thử HIEN-CHUONG §1).

## Bảng chấm 71 câu

| id | Kết luận | Tầng đúng? | LTĐ | Căn cứ (trích nguyên văn ngắn + mã/trang) | Đề xuất sửa |
|---|---|---|---|---|---|
| S001 | KHÔNG CẦN NGUỒN | đúng (MH, cảnh dựng, không người thật) | Không | — | — |
| S002 | KHỚP | đúng: ●T, có chủ thể "According to the Justice Department" | Không | N4 đ.5: "impersonated officials from the IRS and U.S. Citizenship and Immigration Services… threatened with arrest, imprisonment, fines or deportation if they did not pay" | — |
| S003 | KHỚP | đúng (KBCB, luật 8e) | Không | N4 đ.5 "impersonated officials from the IRS and… USCIS"; N1 tr. 3 ¶1(a) "India-based call centers impersonated U.S. Internal Revenue Service (IRS) officers", ¶1(b) "impersonated… (USCIS) officers" | — |
| S004 | KHỚP | đúng (●T; chủ thể DOJ phủ cả câu) | Không | N4 đ.5 "call centers in Ahmedabad, India"; đ.6 "Patel admitted to operating and funding several India-based call centers" | — |
| S005 | KHỚP | đúng (NB) | Không | N4 đ.2 / N5 đ.2 "Hitesh Madhubhai Patel" | — |
| S006 | KHỚP | đúng (●, có năm và toà Texas) | Không | N5 đ.1 "sentenced today to 20 years in prison… in the Southern District of Texas"; đ.2 "sentenced by U.S. District Judge David Hittner" | — |
| S007 | MẠNH HƠN (nhẹ) | đúng (CHUNG, câu hỏi dẫn) | Không | N4 đ.5 "the call centers would immediately turn to a network of 'runners' based in the United States". Nguồn nói *based in the United States*, không nói quốc tịch. N3 (các `<li>`) cho thấy nhiều người bị cho trục xuất hoặc đưa về Ấn Độ, nên "American hands" rộng hơn nguồn | "…turn into money in the hands of people in the United States, almost immediately?" |
| S008 | KHÔNG CẦN NGUỒN | đúng (CHUNG; lời hứa kênh, không nêu sự việc mới) | Không | — | — |
| S009 | KHỚP | đúng (◐, "According to the indictment"; đã bỏ thành phố của nạn nhân) | Không | N2 đ.11 "According to the indictment, one of the call centers extorted $12,300 from an 85-year-old victim… after threatening her with arrest if she did not pay fictitious tax violations" | — |
| S010 | KHỚP | đúng (◐) | Không | N2 đ.12 "The indictment also alleges that the defendants extorted $136,000 from a victim… who they called multiple times over a period of 20 days, fraudulently purporting to be IRS agents" | — |
| S011 | KHỚP (chỉ thẻ chữ) | đúng (KBCB cho đoạn P01) | Không | như S003 | — |
| S012 | KHỚP | đúng (TT) | Không | N2 đ.8 "returned by a grand jury in the U.S. District Court for the Southern District of Texas on Oct. 19, 2016"; N1 tr. 1 "FILED October 19, 2016" | — |
| S013 | KHỚP | đúng (TT) | Không | N1 tr. 1 "Unsealed 10/27/16" (19/10 cộng 8 ngày = 27/10); N2 đ.1 "an indictment was unsealed charging a total of 61 individuals and entities" | — |
| S014 | KHỚP | đúng (TT) | Không | N2 đ.1 "20 individuals were arrested today in the United States and 32 individuals and five call centers in India were charged" | — |
| S015 | KHỚP | đúng (◐; nói rõ là cáo buộc) | Không | N2 đ.1 "has victimized tens of thousands of persons… hundreds of millions of dollars in losses" | — |
| S016 | KHỚP | đúng (◐) | Không | N1 tr. 3 ¶1 "a number of different confidence scams" | — |
| S017 | KHỚP | đúng (◐) | Không | N1 tr. 3 ¶1(a) "owed money to the IRS and would be arrested and fined if they did not pay their alleged back taxes immediately" | — |
| S018 | KHỚP | đúng (◐) | Không | N1 tr. 3 ¶1(b) "would be deported unless they paid a fine immediately for alleged issues with their USCIS paperwork" | — |
| S019 | KHỚP | đúng (◐) | Không | N1 tr. 4 ¶1(c) "pay an upfront 'worthiness fee'… The victims received nothing in return"; ¶1(d) "pay an upfront IRS tax or processing fee. The victims received nothing in return" | — |
| S020 | KHỚP | đúng (◐, có chủ thể DOJ; xếp thận trọng là ◐ dù đ.6 mở đầu bằng "In his plea") | Không | N4 đ.6 "exchange… telephone scam scripts… The scripts included… Canada Revenue Agency (CRA) impersonation, Australian Tax Office (ATO) impersonation… debt collection fraud" | — |
| S021 | KHỚP | đúng (KBCB cho P03) | Không | N4 đ.6 "impersonation" | — |
| S022 | KHỚP (ghi chú) | đúng (◐) | Không | N1 tr. 4 ¶2 "The defendants held one or more of the following roles". Chữ "industry" là lời diễn giải của người kể; N3 đ.3 có "India call center scam industry" | Không bắt buộc: thêm N3 đ.3 vào cột nguồn cho chữ "industry" |
| S023 | KHỚP | đúng (◐) | Không | N1 tr. 5 ¶2(d) "received lead list information and call scripts… purporting to be U.S. government officials or money lenders" | — |
| S024 | KHỚP | đúng (◐) | Không | N1 tr. 5 ¶2(c) "located in India and oversaw and managed the day-to-day operations"; ¶2(e) "located in India… intermediaries between the call centers and the Runners" | — |
| S025 | KHỚP | đúng (◐) | Không. Chỉ nêu vai trò; bỏ cách đăng ký thẻ và nguồn mua dữ liệu | N1 tr. 6 ¶2(f) "to purchase names and PII for registering GPR cards and targeting potential victims"; tr. 4 ¶2(a) "Runners were located in the United States… Runners were often directed by Domestic Managers" | — |
| S026 | KHỚP | đúng (◐) | Không | N1 tr. 6 ¶2(g) "liaised between hawaladars in cities outside India and the India-based call centers… A hawala is an underground banking system" | — |
| S027 | KHỚP | đúng (◐; không nêu tên bốn nhóm còn lại) | Không | N1 tr. 6–7 ¶3 "five major conglomerates of call centers, all located in Ahmedabad… often acted together… sharing call scripts and lists of potential victims, processing payments for each other" | — |
| S028 | KHỚP | đúng (●T, có chủ thể DOJ). Câu ◐ về HGLOBAL đi ngay sau ở S029, nên lần nêu này có kèm | Không | N4 đ.6 / N5 đ.9 "In his plea, Patel admitted to operating and funding several India-based call centers… including the call center HGLOBAL" | — |
| S029 | KHỚP (ghi chú) | đúng (◐). Lời và chữ khớp đúng chuỗi quyết định MR-5 (`can_loi`/`can_chu`) | Không | N1 tr. 1 "[1] HGLOBAL" (là bị cáo); N3 đ.15 "32 India-based conspirators and five India-based call centers… have yet to be arraigned" (20/07/2018); N5 đ.12 "Charges remain pending for other India-based defendants. They are presumed innocent" (30/11/2020) | Câu không suy ra trạng thái HGLOBAL sau 7/2018. Riêng vế "it **is** presumed innocent" ở thì hiện tại hàm ý đến nay HGLOBAL chưa bị kết án, mà điều này chỉ có nguồn đến 11/2020. Chuỗi do chủ dự án khoá nên không sửa ở đây; cần kiểm lại ở ngày đăng (luật 4). Nếu chủ dự án cho sửa: "was presumed innocent" |
| S030 | KHỚP | đúng (◐) | Không | N1 tr. 7, bảng HGLOBAL: "HITESH PATEL (a.k.a. HITESH HINGLAJ) / Call Center Operator / India" | — |
| S031 | KHỚP | đúng (◐) | Không | N4 đ.7 "received monthly income and expense reports to his personal email from the call centers" | — |
| S032 | KHỚP | đúng (◐; chữ "boss" chỉ nằm trong lời trích của đồng bị cáo) | Không | N4 đ.8 "A co-defendant described Patel as 'the top person in India and the boss for whom most of the other defendants worked'" (cũng N5 đ.10); chữ trên hình khớp nguyên văn | — |
| S033 | KHỚP | đúng (CHUNG, câu rào) | Không | N4 đ.8 (là lời mô tả của đồng bị cáo) | — |
| S034 | KHỚP | đúng (●T) | Không. Chỉ nêu loại phương thức, không nêu thao tác | N4 đ.5 "were instructed how to provide payment, including by purchasing general purpose reloadable (GPR) cards or wiring money" | — |
| S035 | KHỚP | đúng (●T) | Không | N4 đ.5 "Upon payment, the call centers would immediately turn to a network of 'runners' based in the United States to liquidate and launder" | — |
| S036 | KHỚP | đúng (◐) | Không. Không nêu cách đăng ký thẻ | N2 đ.9 (thuộc đoạn "According to the indictment") "The prepaid debit cards were often registered using misappropriated personal identifying information of thousands of identity theft victims" | — |
| S037 | **MẠNH HƠN** | **sai**: vế đầu "Some of the money also moved through hawala" là cáo buộc mà nói như sự thật. Chủ thể "the indictment" chỉ phủ vế định nghĩa (luật 2) | Không | N2 đ.10 "The co-conspirators **allegedly** used 'hawalas'… to direct the extorted funds"; N1 tr. 6 ¶2(g) "money can be made available internationally without actually moving it" | "**According to the indictment,** some of the money also moved through hawala, a system the indictment described as a way to make money available in another country without actually moving it there." |
| S038 | KHỚP | đúng (◐) | Không. Mức khái niệm, đúng như cáo trạng | N1 tr. 6 ¶2(g) "The first hawaladar then owes the transferred amount to the second, and the debt is frequently repaid by transactions conducted in the reverse direction" | — |
| S039 | KHỚP | đúng (◐) | Không | N2 đ.10 "According to the indictment, these individuals were expecting the hawala transfers but were not aware of the illicit nature of the funds" | — |
| S040 | KHỚP | đúng (●N, có chủ thể DOJ, theo nhóm, không tên) | Không | N3 đ.14 "According to various admissions made in connection with the defendants' guilty pleas… runners… to liquidate and launder the extorted funds as quickly as possible" | — |
| S041 | KHÔNG CẦN NGUỒN | đúng (CHUNG; có câu tự rào "That framework is ours"). Phần áp vào vụ ("payments onto cards or as wire transfers") đã có ở N4 đ.5 | Không | — | — |
| S042 | KHÔNG CẦN NGUỒN | đúng (CHUNG, không nêu sự việc mới) | Không | — | — |
| S043 | **MẠNH HƠN** (nhẹ) | đúng tầng (●N) | Không | N3 đ.1 "sentenced… to terms of imprisonment up to 20 years"; N4 đ.11 "24 domestic defendants… convicted and sentenced to terms of imprisonment of up to 20 years in the Southern District of Texas, District of Arizona and Northern District of Georgia". Tuy vậy, danh sách `<li>` của N3 ghi "Nilesh Pandya… three years probation" và "Raman Patel… received a probationary sentence". Hai trong 24 người không bị án tù, nên "sentenced… to prison terms" rộng hơn sự thật | "…had been convicted and sentenced, in federal courts in Texas, Arizona and Georgia, to sentences ranging from probation to twenty years in prison." |
| S044 | KHỚP | đúng (●N, không tên) | Không | N3 đ.8 "manager of a Chicago-based crew of 'runners'"; đ.9 "a co-owner and manager of an India-based call center… After moving to the United States in 2015"; đ.10 "member of a Houston-based crew of runners that he co-managed" | — |
| S045 | KHỚP | đúng (●N) | Không | N3 đ.11 "Twenty-two of the defendants… were held jointly and severally liable for restitution of $8,970,396 payable to identified victims"; chữ trên hình khớp | — |
| S046 | **MẠNH HƠN** | **sai một phần**: "they **are** presumed innocent" (hiện tại) suy trạng thái của cả nhóm 32 người và 5 call center đến nay, vượt mốc 7/2018 của nguồn. Nhóm này gồm cả Patel (N1 tr. 1 [6] và bảng tr. 7 ghi Location India), người đã bị kết án năm 2020 | Không | N3 đ.15 "charged 32 India-based conspirators and five India-based call centers… These defendants have yet to be arraigned… presumed innocent" | "…As of July twenty eighteen, the Justice Department said, those defendants had yet to be arraigned, and they **were** presumed innocent." |
| S047 | KHỚP | đúng (●T, có chủ thể DOJ) | Không | N3 đ.1 (21 người cộng 3 người là 24); N4 đ.6 "admitted to operating and funding several India-based call centers" | — |
| S048 | KHỚP | đúng (TT) | Không | N4 đ.9 "Singapore authorities apprehended Patel at the request of the United States… in September 2018, after Patel flew there from India" | Biên tập (không bắt buộc): S048 và S049 trùng ý |
| S049 | KHỚP | đúng (TT) | Không | N4 đ.9 "pursuant to a provisional arrest warrant" | — |
| S050 | KHỚP | đúng (TT) | Không | N4 đ.9 "extradited from Singapore in April 2019 to face charges" | — |
| S051 | KHỚP | đúng (●; 2 tội; rửa tiền chỉ là một mục đích của âm mưu chung, không phải tội riêng) | Không | N4 đ.2 "pleaded guilty to wire fraud conspiracy and general conspiracy to commit identification fraud, access device fraud, money laundering, and impersonation of a federal officer or employee"; ngày thông cáo 09/01/2020, đ.1 "today" | — |
| S052 | KHỚP | đúng (●) | Không | N4 đ.10 "U.S. District Judge David Hittner… accepted the plea today" | — |
| S053 | KHỚP | đúng (●T) | Không | N4 đ.8 "Patel admitted that a reasonably foreseeable loss of more than $25 million but less than $65 million was attributable to him, based on the government's evidence against him" | — |
| S054 | KHỚP | đúng (●) | Không | N5 đ.1 "sentenced today to 20 years in prison followed by three years of supervised release" (thông cáo ngày 30/11/2020); đ.2 Judge Hittner | — |
| S055 | KHỚP | đúng (●) | Không | N5 đ.2 "restitution of $8, 970,396 to identified victims" (khoảng trắng là lỗi gõ của thông cáo) | — |
| S056 | KHỚP | đúng (◐; có mốc 11/2020 và chủ thể DOJ; "other" đã loại Patel) | Không | N5 đ.12 "Charges remain pending for other India-based defendants. They are presumed innocent unless and until convicted through due process of law." | Cần kiểm lại ở ngày đăng (luật 4) |
| S057 | KHÔNG CẦN NGUỒN | đúng. Số đếm khớp: 3 bài học (S058–S060), 5 dấu hiệu (S062–S066), 1 quy tắc (S068) | Không | — | — |
| S058 | KHỚP | đúng (◐) | Không | N1 tr. 4–6 ¶2: Runner, Domestic Manager, Call Center Operator, Caller, Payment Processor, Data Broker, Hawaladar | — |
| S059 | **MẠNH HƠN** (nhẹ) | sai một phần: câu gắn ●T (Patel thừa nhận theo DOJ) nhưng (1) "gift cards" không có trong N4 đ.5 mà đến từ N3 đ.14 (●N, các bị cáo khác); (2) "payments were cashed out and laundered immediately" chắc hơn nguồn, vì nguồn nói call center "immediately turn to" runners để rửa tiền, còn N3 nói "as quickly as possible"; (3) "through many hands" là diễn giải | Không | N4 đ.5 "Upon payment, the call centers would immediately turn to a network of 'runners'… to liquidate and launder"; N3 đ.14 "Apple iTunes or other gift cards that victims purchased" | "…In this case, according to the Justice Department, once a victim paid, the call centers immediately turned to a network of runners in the United States to cash out and launder the money. In our terms, the money was placed, and then layered." Vế mở đầu "prepaid cards, gift cards or a wire transfer" giữ được nếu thêm N9 vào nguồn (lời khuyên chung của IRS) |
| S060 | KHỚP | đúng (CHUNG, có chủ thể IRS) | Không | N9: "The IRS initiates most contacts through regular mail…"; "Note that the IRS does not: Call to demand immediate payment using a specific payment method such as a prepaid debit card, gift card or wire transfer… without the opportunity to question or appeal… Threaten to bring in local police, immigration officers…" | — |
| S061 | KHỚP | đúng (CHUNG, lời quan chức có nguồn); chữ trên hình trích nguyên văn | Không | N2 đ.5 (Executive Associate Director Edge, HSI): "U.S. government agencies do not make these types of calls"; thông cáo ngày 27/10/2016 | — |
| S062 | KHỚP | đúng (●T) | Không | N4 đ.5 "threatened with arrest, imprisonment, fines or deportation if they did not pay" | — |
| S063 | **MẠNH HƠN** (nhẹ) | đúng tầng (◐), nhưng "described **exactly** that demand" quy cho cáo trạng cả vế "with no chance to check", trong khi cáo trạng chỉ nói "immediately" | Không | N1 tr. 3 ¶1(a) "if they did not pay… immediately"; ¶1(b) "paid a fine immediately". Vế "no chance to question or appeal" thuộc N9, là lời của IRS | "Two: pressure to pay immediately, with no chance to check; the indictment described demands to pay immediately, and the IRS says it does not demand payment without a chance to question or appeal." Hoặc chỉ bỏ chữ "exactly" và ghi: "the indictment described demands to pay immediately." |
| S064 | KHỚP | đúng (●T) | Không | N4 đ.5 "including by purchasing general purpose reloadable (GPR) cards or wiring money" | — |
| S065 | KHỚP | đúng (◐) | Không | N2 đ.12 "called multiple times over a period of 20 days" | — |
| S066 | KHỚP | đúng (◐) | Không | N1 tr. 4 ¶1(c)–(d) "The victims received nothing in return." | — |
| S067 | KHỚP (chỉ thẻ chữ) | đúng (KBCB cho P11) | Không | như S003 | — |
| S068 | KHÔNG CẦN NGUỒN | đúng (CHUNG; lời khuyên an toàn chung, không phải lời khuyên pháp lý) | Không | (hợp với N9 "If an IRS representative visits you… the representative will provide you with a dedicated IRS telephone number") | — |
| S069 | KHỚP | đúng (◐, có chủ thể) | Không | N3 đ.3 (Attorney General Sessions): "conspired to bilk older Americans, legal immigrants and many others out of their life savings" | — |
| S070 | KHỚP | đúng (CHUNG); không đọc số điện thoại | Không | N9 "Contact the Treasury Inspector General for Tax Administration to report a phone scam"; N11 "Someone is impersonating an IRS or Treasury employee."; N10 trang ReportFraud.ftc.gov, meta "reporting fraud, scams" | — |
| S071 | KHÔNG CẦN NGUỒN | đúng | Không | — | — |

## Kiểm riêng

1. **Chủ thể:** mọi câu ●T đều có "According to the Justice Department" hoặc "admitted, according to the Justice Department". Lời nhắc tới 2 tội; không có tội rửa tiền riêng (S051). Có hai chỗ biến cáo buộc thành sự thật, hoặc vượt mốc thời gian của nguồn: S037 và S046.
2. **HGLOBAL:** được nêu ở S028 (lời) và S029 (lời và chữ). Câu ◐ khớp đúng chuỗi MR-5 và đi ngay sau S028. Ba nguồn đều đúng: N1 tr. 1, N3 đ.15, N5 đ.12. Không câu nào suy trạng thái HGLOBAL sau 7/2018; riêng chữ "is presumed innocent" ở thì hiện tại cần kiểm lại ở ngày đăng (xem S029).
3. **Cơ quan bị mạo danh:** mỗi đoạn có nêu IRS hay cơ quan khác đều có câu "không liên quan": P00 S003, P01 S011, P03 S021, P11 S067. Không có thương hiệu, ứng dụng hay thành phố của nạn nhân; không nêu tên bị cáo chưa xử ngoài HGLOBAL đã kèm câu ◐. Chữ "boss" chỉ nằm trong lời trích của đồng bị cáo. Không có "scammer", "con artist" hay "fraudster" ở giọng kể.
4. **Số liệu, ngày và số người:** đều khớp, gồm $12,300; 85 tuổi; $136,000; 20 ngày; 19/10/2016; 8 ngày; 61; 20; 32 + 5; 5 nhóm; 24 người (22 ở Houston, 1 ở Atlanta, 1 ở Phoenix); 22 người với $8,970,396; 9/2018; 4/2019; 9/1/2020; $25–65 triệu; 30/11/2020; 20 năm + 3 năm. Ngoại lệ là S043: "prison terms" không đúng cho 2 người chỉ bị quản chế.
5. **Làm theo được ngay:** 0 câu. Các câu về thẻ trả trước, runner, hawala và data broker chỉ ở mức vai trò và khái niệm. Không có thao tác đăng ký thẻ, tên thẻ quà tặng, ứng dụng, dịch vụ chuyển tiền hay ngưỡng nào.

## Tổng kết

| Kết luận | Số câu | id |
|---|---|---|
| KHỚP | 58 | các câu còn lại (kể cả S011 và S067, là câu KBCB chỉ hiện trên thẻ chữ) |
| MẠNH HƠN | 6 | S007, S037, S043, S046, S059, S063 |
| SAI | 0 | — |
| KHÔNG CẦN NGUỒN | 7 | S001, S008, S041, S042, S057, S068, S071 |
| **Tổng** | **71** | |

**Làm theo được ngay = Có:** 0 câu.

## Danh sách sửa đề xuất

1. **S037 (bắt buộc):** thêm "According to the indictment," ở đầu câu → "According to the indictment, some of the money also moved through hawala, a system the indictment described as a way to make money available in another country without actually moving it there."
2. **S046 (bắt buộc):** "and they are presumed innocent" → "and they were presumed innocent". Lý do: nhóm này gồm cả Patel, người đã bị kết án năm 2020.
3. **S043:** "to prison terms of up to twenty years" → "to sentences ranging from probation to twenty years in prison". Căn cứ: danh sách `<li>` của N3 có 2 người chỉ bị quản chế.
4. **S059:** "payments were cashed out and laundered immediately, through many hands" → "once a victim paid, the call centers immediately turned to a network of runners in the United States to cash out and launder the money". Thêm N9 (và N3 đ.14 nếu giữ chữ "gift cards") vào cột nguồn.
5. **S063:** bỏ "exactly" → "the indictment described demands to pay immediately". Có thể thêm vế của IRS (N9) cho ý "no chance to question or appeal".
6. **S007:** "money in American hands" → "money in the hands of people in the United States".
7. **Ghi chú, không bắt buộc:** S029 (chuỗi đã khoá): xin chủ dự án xem có đổi "is presumed innocent" thành "was presumed innocent" không; nếu giữ thì kiểm lại ở ngày đăng. S056: kiểm lại ở ngày đăng. S022: thêm N3 đ.3 cho chữ "industry". S048 và S049 trùng ý.
