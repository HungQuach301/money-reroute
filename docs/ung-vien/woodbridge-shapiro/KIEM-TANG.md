# Kiểm tầng pháp lý độc lập — `woodbridge-shapiro`

- **Người kiểm:** tác tử độc lập MR-1 (không đọc `reports/**`, `RUI-RO.md`, phần tóm tắt `NGUON.md`; chỉ dùng CLAUDE.md, HIEN-CHUONG §3, `TANG.md`, bảng nguồn `NGUON.md`).
- **Ngày kiểm:** 01/11/2026.
- **Thang chấm:** **K** = khớp · **MH** = mạnh hơn nguồn · **S** = sai · **KKĐ** = không kiểm được · k/a = không áp dụng (không tính).

## Nguồn đã mở

| Mã | Tệp / URL | Trang đã đọc | Kiểm |
|---|---|---|---|
| N2 | `ho-so/woodbridge-shapiro/sec-complaint-2017.pdf` | tr. PDF 2–5, 7, 10–11, 19, 23–24, 28 | SHA-256 `9e5c4388…39c8b6` khớp NGUON |
| N4 | `sec-final-judgment-shapiro-2018.pdf` | tr. 1–8 | `34e7680a…6f2c5c` khớp |
| N5 | `sec-final-judgment-woodbridge-2018.pdf` | tr. 1–4 | `9a99be3e…6bfc9ff` khớp |
| N6 | `sec-admin-order-shapiro-2019.pdf` | tr. 1–3 | `2f7f5564…307cb2d` khớp |
| N8 | `plea-agreement-shapiro-2019.pdf` | tr. 1–2, 13–14 | `351304b6…2655939` khớp |
| N9 | `factual-proffer-shapiro-2019.pdf` | tr. 3–4, 6–8 | `6924f2a7…958d356` khớp |
| N10 | `judgment-shapiro-2019.pdf` | tr. 1–6 | `90c25e81…f24ca` khớp |
| N11 | `judgment-acevedo-2021.pdf` | tr. 1–3, 6 | `f35e3e9d…0f575f` khớp |
| N12 | `ca11-opinion-shapiro-2024.pdf` | tr. 1–4 | `e1863399…ec4` khớp |
| N14 | `sec-complaint-acevedo-roseman-2019.pdf` | (không cần; dùng N13) | `4db52b63…80a8d` khớp |
| N15 | `sec-final-judgment-roseman-2021.pdf` | tr. 1, 5–6 | `3ebbf43a…ea1` khớp |
| N16 | `sec-final-judgment-acevedo-2021.pdf` | tr. 1, 5–6 | `1a59528c…14af854` khớp |
| N1 | sec.gov/newsroom/press-releases/2017-235 | đoạn đầu | HTTP 200 (UA "MoneyReroute research …") |
| N3 | sec.gov/newsroom/press-releases/2019-3 | toàn văn + danh mục judgment | HTTP 200 |
| N13 | sec.gov/newsroom/press-releases/2019-55; lr-24450 | toàn văn | HTTP 200 |
| N17 | sec.gov litigation releases lr-24476, lr-24531, lr-24676, lr-24759 | đoạn đầu | HTTP 200 |
| N18 | sec.gov lr-24032 | đoạn đầu | HTTP 200 |
| N20 | justice.gov/pardon: Trump 2025–nay ("Updated October 20, 2026"); **pardons-granted-president-donald-j-trump-2017-2021** và **commutations-granted-president-donald-j-trump-2017-2021** (HTTP 200); Biden pardons ("Updated May 14, 2026") và commutations ("Updated July 9, 2025") + lớp chữ các PDF lệnh ân giảm tải được | tìm "Shapiro", "Roseman", "Acevedo" | Không có Robert Shapiro / Dane Roseman / Ivan Acevedo. Trùng tên **người khác**: "Mark Shapiro" (commutations Trump 2017–2021); "NEVIN SHAPIRO" và "JORGE ACEVEDO" trong PDF justice.gov/pardon/media/1380216 (lệnh giảm án tập thể, hết hạn 22/12/2024). Một số PDF trả 502 từ proxy (không thử lại) |
| BOP | Inmate Locator (POST `/PublicInfo/execute/inmateloc`) | 77952-112, 77953-112, tên "Dane Roseman" | SHAPIRO, ROBERT 77952-112: USP Tucson, projRelDate 07/31/2039. ACEVEDO, IVAN 77953-112: actRelDate 04/26/2024. ROSEMAN, DANE 77951-112: actRelDate 03/15/2024 |
| N7 | courtlistener.com/docket/14944566/… | — | **chưa mở được**: HTTP 403 (CloudFront). RECAP Doc. 178, 283, 286, 288, 289, 324, 341 (ba ID 547094–547096): 404 |

## Bảng chấm từng ô

| # | Chủ thể | Ô | Bảng nói | Chấm | Bằng chứng (≤ 25 từ) |
|---|---|---|---|---|---|
| 1 | Robert H. Shapiro (hình sự) | Tầng | ● CONVICTED | **K** | N10 tr. 1: "The defendant pled guilty to Counts 1 and 10 of the Indictment… adjudicated guilty" |
| | | Loại phán quyết | Nhận tội theo plea, toà chấp nhận (07/08/2019) | **K** | N8 tr. 1 (lọc 08/07/2019): "agrees to plead guilty to Counts 1 and 10"; N10 tr. 1. Mô tả docket "Guilty Counts 1,10": KKĐ (gộp ô) |
| | | Tội danh + án | §1349 (kết thúc 12/2017); §7201 (04/2019); 300 tháng = 240 + 60 nối tiếp = tối đa 20 + 5; 3 năm; 200 USD; Count 2–9 bãi | **K** | N10 tr. 1 "Conspiracy to Commit Mail Fraud and Wire Fraud December 2017"; "Evasion of Payment of Federal Income Taxes April 2019"; tr. 2 "300 months… 240 months as to Count 1, and 60 months as to Count 10, to run consecutively"; N8 tr. 2 "total sentence of 25 years"; N8 tr. 1 "dismissal of Counts 2 through 9" |
| | | Bồi hoàn 478.912.763 USD (Amended Judgment 04/11/2019) | chỉ mô tả docket | **KKĐ** | N10 tr. 5 "TO BE DETERMINED"; Doc. 178 không mở được |
| | | Kháng cáo | Miễn kháng cáo mức án (N8 tr. 13); đơn giảm án bị bác 28/07/2023; CA11 giữ nguyên 13/03/2024 | **K** | N8 tr. 13: "waives all rights… to appeal any sentence imposed, including any forfeiture or restitution"; N12 tr. 2: "summarily affirm the district court's denial of Shapiro's motion for a sentence reduction". Ngày 28/07/2023: KKĐ |
| | | Ân xá | Không có | **K** | N20, 0 kết quả cho Robert Shapiro (chỉ "Mark Shapiro", "Nevin Shapiro" — người khác) |
| | | Đã chết? | Còn sống tới 13/03/2024; sau đó chưa xác minh | **K** (cập nhật được) | BOP 01/11/2026: 77952-112 tại USP Tucson, projRelDate 07/31/2039, chưa có actRelDate |
| | | Nguồn | N10 tr. 1–2, 5; N8 tr. 1–2, 13; N9; N12 tr. 1–4; N7… | **K** | đúng trang; các mục N7 KKĐ |
| 2 | Shapiro (dân sự SEC) | Tầng | ◐ ALLEGED (settled) | **K** | N4 tr. 1: "consented to entry of this Final Judgment without admitting or denying the allegations of the Amended Complaint" |
| | | Loại phán quyết | Consent final judgment, vào docket 27/12/2018 | **K** | N4 tr. 1 dòng đầu "Entered on FLSD Docket 12/27/2018" |
| | | Nội dung | §5, §17(a), §10(b)/10b-5, §20(a), tiếp tay §15(a); 18.546.643 + 2.163.613,69 + 100.000.000 = 120.710.256,69; mục VI chỉ cho phá sản | **K** | N4 tr. 1–5; tr. 5 "disgorgement of $18,546,643… $2,163,613.69, and a civil penalty in the amount of $100,000,000"; tr. 7 "solely for purposes of exceptions to discharge… the allegations in the complaint are true and admitted" |
| | | Kháng cáo | Không có trong hồ sơ; chưa xác minh | **K** (thận trọng hơn cần) | N4 tr. 1: "waived any right to appeal from this Final Judgment" |
| | | Đã chết? | như trên | **K** | BOP |
| | | Nguồn | N4 tr. 1, 5, 7; N3 | **K** | — |
| 3 | Shapiro (hành chính SEC) | Tầng | ◐ ALLEGED (settled) | **K** | N6 tr. 1: "without admitting or denying the findings herein, except… paragraph III.2 below, which are admitted" |
| | | Loại phán quyết | Thoả thuận không thừa nhận | **K** | N6 tr. 1 "Offer of Settlement". Lưu ý: III.2 (việc có consent judgment) **được thừa nhận** |
| | | Nội dung | Cấm vĩnh viễn liên kết broker… và penny stock (theo N3; 34-85004, 30/01/2019) | **K** | N3: "permanently barring Shapiro from association with any broker, dealer, investment adviser…"; N6 tr. 1 "Release No. 85004 / January 30, 2019". Lệnh cấm nằm ở N6 **tr. 2–3** |
| | | Kháng cáo | chưa xác minh | **K** | — |
| | | Đã chết? | như trên | **K** | — |
| 4 | Woodbridge + công ty liên quan (Debtor Defendants) | Tầng | ◐ ALLEGED (settled) | **K** | N5 tr. 1: "consented to entry of this Final Judgment without admitting or denying the allegations" |
| | | Loại phán quyết | Final Judgment as to Debtor Defendants, 27/12/2018 | **K** | N5 tr. 3 "this 27th day of December 2018" |
| | | Nội dung | 892.173.765 USD liên đới, thoả mãn qua Liquidation Trust; 17-12560 (KJC); 142 + 130 công ty | **K** | N5 tr. 2: "disgorgement in the amount of $892,173,765 on a joint and several basis… deemed satisfied by the Liquidation Trust"; tr. 1 "142 Woodbridge-Affiliated Property… 130… Holding" |
| | | "Woodbridge không bị truy tố hình sự (N7 mục 3)" | | **KKĐ** | Docket không mở được; N13 chỉ nói ba cá nhân "separately arrested and charged" |
| | | Kháng cáo | chưa xác minh | **K** (thận trọng hơn cần) | N5 tr. 1: "waived any right to appeal from this Final Judgment" |
| | | Nguồn | N5 tr. 1–2; N3; N18 | **K** | N18: lệnh toà phá sản Delaware 17-12560 (KJC) |
| 5 | Ivan Acevedo (hình sự) | Tầng | ● CONVICTED | **K** | N11 tr. 1: "pleaded guilty to Count 1 of the Superseding Information"; "adjudicated guilty of this offense" |
| | | Loại phán quyết | Nhận tội (Superseding Information), toà chấp nhận 12/07/2021 | **K** | N11 tr. 1. Vế "từ bỏ quyền truy tố bằng cáo trạng" và ngày 12/07/2021: KKĐ (chỉ có trên docket) |
| | | Tội danh + án | §371, kết thúc 12/2017; 17/09/2021; 60 tháng; 3 năm; 100 USD; bồi hoàn 51.000.000 USD | **K** | N11 tr. 1 "18 U.S.C. § 371 Conspiracy To Commit Mail and Wire Fraud December 2017"; tr. 2 "60 months"; tr. 3 "three (3) years"; tr. 6 "$100.00 $51,000,000.00" |
| | | Kháng cáo | chưa xác minh | **KKĐ** | Docket 403 |
| | | Ân xá | Không | **K** | N20; "JORGE ACEVEDO" trong PDF 1380216 là người khác |
| | | Đã chết? | chưa xác minh | **K** | BOP: 77953-112 actRelDate 04/26/2024 (đã ra tù) |
| | | Nguồn | N11 tr. 1–3, 6 | **K** | — |
| 6 | Acevedo (dân sự SEC) | Tầng | ◐ (settled) | **K** | N16 tr. 1: "consented to entry of this Final Judgment" |
| | | Loại phán quyết | Consent final judgment 14/12/2021; không có cụm "without admitting or denying" | **K** | N16 tr. 1 không có cụm này (lớp chữ OCR) |
| | | Nội dung | 743.059 + 161.303,92, thoả mãn bởi bồi hoàn hình sự; phạt dân sự bị bãi | **K** | N16 tr. 5: "disgorgement of $743,059… $161,303.92"; tr. 6 "civil penalty… dismissed in light of Defendant's criminal conviction and sentence" |
| | | Kháng cáo | chưa xác minh | **K** (thận trọng hơn cần) | N16 tr. 1: "waived any right to appeal from this Final Judgment" |
| | | Đã chết? | như trên | **K** | BOP |
| | | Nguồn | N16 tr. 1, 5–6 | **K** | — |
| 7 | Dane R. Roseman (hình sự) | Tầng | ● CONVICTED | **K** | N15 tr. 6 (văn bản của toà): "in light of Defendant's criminal conviction and sentence in United States v. Roseman, No. 19cr20178" |
| | | Loại phán quyết | Nhận tội (Count 1ss) 12/07/2021 | **KKĐ** | Chỉ có trên docket (403). N15 không nói là nhận tội hay bị xử |
| | | Tội danh + án | chưa mở được; không dùng số báo chí | **K** | đúng trạng thái |
| | | Kháng cáo | chưa xác minh | **KKĐ** | Docket 403 |
| | | Ân xá | Không | **K** | N20 0 kết quả "Roseman" |
| | | Đã chết? | chưa xác minh | **K** | BOP: ROSEMAN, DANE 77951-112 actRelDate 03/15/2024 |
| | | Nguồn | N7…; N15 tr. 5–6 | **K** | N15 tr. 5–6 đúng; N7 KKĐ |
| 8 | Roseman (dân sự SEC) | Tầng | ◐ (settled) | **K** | N15 tr. 1: "consented to entry of this Final Judgment" |
| | | Loại phán quyết | Consent 14/12/2021; không có cụm "without admitting or denying" | **K** | N15 tr. 1 |
| | | Nội dung | 2.430.550 + 423.308 = 2.853.858, thoả mãn bởi Doc. 324; phạt bị bãi | **K** | N15 tr. 5–6: "$2,853,858 is deemed satisfied by the amount of restitution… docket entry #324" |
| | | Kháng cáo | chưa xác minh | **K** (thận trọng hơn cần) | N15 tr. 1: "waived any right to appeal from this Final Judgment" |
| | | Đã chết? | như trên | **K** | BOP |
| | | Nguồn | N15 tr. 1, 5–6 | **K** | — |
| 9 | RS Protection Trust | Tầng | ◐ (settled) | **K** | N3: "All defendants and relief defendants, without admitting or denying the SEC's allegations, consented" |
| | | Loại phán quyết | Consent (theo N3), PDF riêng chưa mở | **K** | N3 liệt kê "Final Judgment - RS Protection" |
| | | Nội dung | 5,3 triệu USD chung; N2 tr. 7; N9 tr. 3, 8 | **K** | N3: "RS Protection Trust and several relief defendants were collectively ordered to pay $5.3 million"; N2 tr. 7 "irrevocable domestic asset protection trust settled under Nevada law"; N9 tr. 8 "creating RS Trust in the State of Nevada… to conceal his assets and income" |
| | | Kháng cáo | chưa xác minh | **K** | — |
| | | Nguồn | N3; N2 tr. 7; N9 tr. 3, 8 | **K** | — |
| 10 | Vợ của Shapiro (relief defendant) | Tầng | ○ — người không bị cáo buộc | **S** (nhãn) | ○ là UNVERIFIED theo §3. Bà có consent final judgment (N3 liệt kê "Final Judgment - Jeri Shapiro"); câu "nhận tiền" là cáo buộc SEC → ◐ |
| | | Loại phán quyết | Consent, PDF chưa mở | **K** | N3 |
| | | Nội dung | Shapiro thừa nhận dùng tài khoản đứng tên bà | **K** | N9 tr. 4: "SHAPIRO also used the accounts established in these entities' names, as well as in J.S.'s name, for his own use and benefit" |
| | | "Không bị truy tố hình sự" | | **KKĐ** | Docket 403 |
| | | Nguồn | N2 tr. 5 (¶11); N9 tr. 3–4, 6–7; N3 | **K** | N2 tr. 5 "Relief defendants [tên], (Shapiro's wife)" |
| 11 | Relief defendant công ty | Tầng | ○ | **S** (nhãn) | Như dòng 10; N2 tr. 5: "all received proceeds of the fraud without any legitimate entitlement" là **cáo buộc** → ◐ |
| | | Loại phán quyết | Consent (N3) | **K** | N3 liệt kê Schwartz Media, Woodbridge Realty, Woodbridge Luxury Homes, Riverdale Funding, WFS Holding (và Carbondale Glen Lot 18, Carbondale Glen Owners, Carbondale Basalt Owners — bảng chưa nêu) |
| | | Nguồn | N2 tr. 1, 5; N3 | **K** | — |
| 12 | Đại lý bán hàng | Tầng | ◐ ALLEGED | **K** | N17: các lr đều "charges… violating the securities registration… and broker-dealer registration provisions" |
| | | Loại phán quyết | Đơn kiện; kết quả chưa xác minh | **K** | — |
| | | Nội dung | Chủ yếu bán không đăng ký / broker không đăng ký; tên và số vụ | **K** | lr-24476 "Robert S. Davis, Jr., et al., Case No. 18-cv-10481 (C.D. Cal.)"; lr-24759 "Church-Koegel, David H. Goldman, and Nicole J. Walker". Lưu ý: lr-24676 viết "19… highest-earning unregistered brokers with allegedly stealing over a billion dollars" — không trích câu này |
| | | "Không ai có trong vụ hình sự 19-cr-20178" | | **KKĐ** | Docket 403 |
| | | Kháng cáo | chưa xác minh | **K** | — |
| | | Nguồn | N17 | **K** | — |
| 13 | "DR" (Head of Sales), Controller | Nội dung | Không gán người; chỉ "the SEC alleges" | **K** | N2 tr. 19: "led by Head of Sales 'DR'"; tr. 23 "DR, the Head of Sales, reported directly to Shapiro"; tr. 11 "Woodbridge's Controller" |
| | | Nguồn | N2 tr. 19, 23–24 | **K** | — |

### Câu "Cách nói EN gợi ý"

| # | Câu | Chấm | Bằng chứng |
|---|---|---|---|
| E1 | Shapiro "In August 2019… pleaded guilty in federal court in Miami to conspiracy to commit mail and wire fraud and to tax evasion… October 2019… 25 years — the maximum for those two counts"; "admitted that new investors' money was used to pay 'returns' to earlier investors"; "In 2024, a federal appeals court upheld the denial of his request for early release" | **K** | N8 lọc 08/07/2019; N10 tr. 1 "MIAMI DIVISION", "October 15, 2019"; N8 tr. 2 "total sentence of 25 years"; N9 tr. 6 "invested by new investors were misused to pay false and misleading 'returns' to existing Woodbridge investors"; N12 tr. 2 |
| E2 | "settled the SEC's civil case without admitting or denying… $100 million civil penalty"; "The SEC alleged that most… third-party borrowers were actually companies Shapiro owned" | **K** | N4 tr. 1, 5; N2 tr. 2 "nearly all the purported third-party borrowers were actually limited liability companies owned and controlled by Shapiro" |
| E3 | Woodbridge: không nói "convicted"; "filed for bankruptcy in December 2017"; "settled… without admitting or denying" | **K** | N9 tr. 7 "bankruptcy in December 2017"; N5 tr. 1 |
| E4 | Acevedo "pleaded guilty to a fraud conspiracy charge… sentenced in 2021 to five years" | **K** | N11 tr. 1–2 |
| E5 | Roseman "also pleaded guilty in 2021" | **KKĐ** | Không văn bản nào đã mở nói Roseman **nhận tội**; N15 tr. 6 chỉ nói "criminal conviction and sentence" |
| E6 | Đại lý: "alleging they sold Woodbridge notes without being registered as brokers" | **K** | N17 |
| E7 | Vợ / relief defendants: không nêu tên | **K** | luật thi hành 5 |

Không câu EN nào dùng "convicted" hoặc "fraud" khẳng định cho chủ thể chưa ●. "Fraud" chỉ đi với Shapiro và Acevedo (●) hoặc nằm trong "The SEC alleged…".

## Tổng

| Khớp | Mạnh hơn | Sai | Không kiểm được |
|---|---|---|---|
| **69** | **0** | **2** (nhãn ○ ở dòng 10, 11) | **8** |

(4 ô "khớp" ở mục kháng cáo dân sự — dòng 2, 4, 6, 8 — thận trọng hơn mức nguồn cho phép, xem sửa 4.)

## Sửa bắt buộc

1. **Nhãn ○ (dòng 10, 11):** bỏ ○ (là UNVERIFIED). Ghi "relief defendant — không bị cáo buộc vi phạm". Mọi câu về việc họ nhận tiền là ◐: "The SEC alleged… ; they settled without admitting or denying" (N3). Vẫn không nêu tên.
2. **EN Roseman (E5):** đến khi mở được Doc. 286/324 hoặc thông cáo N22, đổi thành câu chỉ dựa trên N15 tr. 6, vd "Court records show Dane Roseman was also convicted and sentenced in the same federal case." Không nói "pleaded guilty", không nói mức án. Ô "Loại phán quyết" dòng 7 ghi "chưa kiểm độc lập".
3. **Bồi hoàn Shapiro 478.912.763 USD**, ngày bác đơn giảm án 28/07/2023, "Woodbridge không bị truy tố", "không đại lý nào trong vụ hình sự": cùng nguồn docket N7, lần kiểm này **không mở được** (403). Không dùng trên hình hoặc lời cho tới khi mở PDF (Doc. 178, 341) hoặc docket.
4. **Kháng cáo dân sự (dòng 2, 4, 6, 8):** thay "chưa xác minh" bằng "đã từ bỏ quyền kháng cáo final judgment (N4/N5/N15/N16 tr. 1: 'waived any right to appeal from this Final Judgment')".
5. **"Đã chết?":** cập nhật theo BOP 01/11/2026: Shapiro đang giam USP Tucson, dự kiến ra 31/07/2039; Acevedo ra tù 26/04/2024; Roseman (số 77951-112) ra tù 15/03/2024. Ra tù **không** phải ân giảm; không nói "freed early".
6. **Ân xá:** ghi chú các trùng tên người khác (Mark Shapiro; Nevin Shapiro và Jorge Acevedo trong PDF justice.gov/pardon/media/1380216) để người sau không nhầm. Sửa mâu thuẫn trong bảng nguồn N20: trang Trump 2017–2021 **mở được** tại `…/pardon/pardons-granted-president-donald-j-trump-2017-2021` và `…/commutations-granted-president-donald-j-trump-2017-2021`.
7. **Trang nguồn dòng 3:** lệnh cấm trong N6 nằm ở tr. 2–3 (tr. 1 chỉ có câu "without admitting or denying"). Ghi rõ III.2 của N6 được Shapiro thừa nhận.
