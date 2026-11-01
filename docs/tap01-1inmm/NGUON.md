# NGUỒN — Tập 1 · 1inMM Capital / Zachary Horwitz (`tap01-1inmm`)

> MR-3 · 01/11/2026 (mở lại 15:10–15:30 UTC). Giữ mã N của `docs/ung-vien/1inmm-horwitz/NGUON.md`; thêm **N22** (Dkt. 58). **Chỉ liệt kê nguồn đã mở ở MR-3**; nguồn không mở lại được ghi ở §3 và **không** làm nguồn câu nào trong `loi.json`.
> Cách mở: PDF trong repo (Git LFS, SHA-256 tính lại khớp); sec.gov và các trang cơ quan bằng UA khai báo của kênh (địa chỉ liên hệ không ghi vào repo); thông cáo DOJ **chỉ qua API chính thức** `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=…` (trang HTML là trang kiểm tra bot — không vượt). Không đổi UA, không dùng bản lưu/mirror.
> Quy ước trang: **N1 = số trang PDF** (bản nộp kín, không có đầu trang ECF; số in ở chân trang nhỏ hơn 1). N4, N6, N7, N8, N22 = "Page x of y" của toà (trùng số trang PDF). N2, N3, N5, N10–N12 là HTML/JSON, không có trang.

## 1. Bảng nguồn đã mở

| Mã | Cơ quan | Tài liệu | Số vụ / docket | Ngày tài liệu | URL | Trang đã đọc ở MR-3 | Đã mở (MR-3) | Tệp + SHA-256 |
|---|---|---|---|---|---|---|---|---|
| N1 | SEC | Complaint, SEC v. Zachary J. Horwitz and 1inMM Capital, LLC | 2:21-cv-02927 (C.D. Cal.) | nộp 05/4/2021 (N3) | https://www.sec.gov/files/litigation/complaints/2021/comp-pr2021-58.pdf | tr. 2–6, 9–10, 13 (¶4–31, ¶45–57, ¶75–78); ảnh trang tr. 9, 13 cho câu trích | 01/11/2026, tệp LFS | `ho-so/1inmm-horwitz/sec-complaint-2021.pdf` · `b7512b6f1e705b0c90e534362289548eb19200d9759b0d675ecf6d8fda007b6c` (khớp) |
| N2 | SEC | Press Release 2021-58 "SEC Obtains Emergency Asset Freeze, Charges Actor with Operating a $690 Million Ponzi Scheme" | 2021-58 | 06/4/2021 | https://www.sec.gov/newsroom/press-releases/2021-58 | Toàn văn | 01/11/2026, HTTP 200 (UA khai báo) | HTML, không lưu |
| N3 | SEC | Litigation Release No. 25067 | 21-civ-02927 (C.D. Cal. filed April 5, 2021) | 08/4/2021 | https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25067 | Toàn văn (câu: "1inMM ('one in a million') Capital"; "neither Horwitz nor 1inMM had ever sold any movie rights to, or done any business with, HBO or Netflix") | 01/11/2026, HTTP 200 (UA khai báo) | HTML, không lưu |
| N4 | Toà án (C.D. Cal., TP Christina A. Snyder) | Final Judgment as to Defendant Zachary J. Horwitz, Dkt. 323 | 2:21-cv-02927-CAS-PD | 14/02/2024 | https://www.sec.gov/files/judg21-cv-02927horwitz.pdf | tr. 1 (consent thẩm quyền, từ bỏ kết luận sự kiện và kháng cáo), tr. 3 §III (tiền), §IV (Consent), §V (chỉ cho mục đích phá sản — **không dùng**) | 01/11/2026, tệp LFS | `ho-so/1inmm-horwitz/sec-final-judgment-horwitz-2024.pdf` · `2ade19cae9af206d099541583c4e192850353aefa9d2c7541c6b2ad4d6845fcf` (khớp) |
| N5 | SEC | Litigation Release No. 25973 | 2:21-cv-02927 | 11/4/2024 | https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25973 | Toàn văn | 01/11/2026, HTTP 200 (UA khai báo) | HTML, không lưu |
| N6 | Toà án / DOJ | Indictment, U.S. v. Zachary Joseph Horwitz, aka "Zach Avery", Dkt. 25 | 2:21-cr-00214-MCS | 04/5/2021 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.25.0.pdf | tr. 1 (aka, "sole manager", tội danh), tr. 9–10 (Counts 12–13) | 01/11/2026, tệp LFS | `ho-so/1inmm-horwitz/doj-indictment-2021.pdf` · `37310c59afbc6d23b4be7243d9776a3fe7e19f6ee8d92a3cff6ce9db8947b9a8` (khớp) |
| N7 | DOJ USAO C.D. Cal. | Plea Agreement, Dkt. 45 | CR 21-214-MCS | nộp 01/9/2021 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.45.0.pdf | tr. 1–2 (Count 1), tr. 4 (USAO đề nghị bác các tội còn lại), tr. 8–12 (Factual Basis), tr. 13–14 (bảo lưu số nhà đầu tư con) | 01/11/2026, tệp LFS | `ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf` · `a74e05082cd80fa3c6c88d9f1dacd9d4c904ed9e26d75650547b8c5a370491a9` (khớp) |
| N8 | Toà án (C.D. Cal., TP Mark C. Scarsi) | Judgment and Probation/Commitment Order, Dkt. 75 | 2:21-cr-00214-MCS-1 | tuyên 14/02/2022, nộp 16/02/2022 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.75.0.pdf | **tr. 1 đọc bằng ảnh trang** (scan: "Feb 14 2022", GUILTY, Count 1, 240 months, 3 năm quản chế); tr. 3 (bồi hoàn $230,361,884); tr. 4 ("all remaining counts ORDERED dismissed", tên thẩm phán). **Không dùng ảnh tr. 1 (4 số SSN, điều kiện quản chế) và tr. 3 (tên bên nhận bồi hoàn) trên hình** | 01/11/2026, tệp LFS | `ho-so/1inmm-horwitz/doj-judgment-commitment-2022.pdf` · `fd458d3e9c76cf371d05c16269f362ff5a5daed44ac27ba36032c88d45e012a9` (khớp) |
| N10 | DOJ USAO C.D. Cal. | Press release 21-059 (tiêu đề có tên khu phố — không đọc trên hình) | — | 06/4/2021 | https://www.justice.gov/usao-cdca/pr/beverlywood-man-arrested-allegedly-bilking-investors-falsely-claiming-license-latin | Toàn văn qua API chính thức (title "Beverlywood Man Arrested") | 01/11/2026, API HTTP 200 | JSON, không lưu |
| N11 | DOJ USAO C.D. Cal. | Press release 21-207 (nhận tội) | — | 04/10/2021 | https://www.justice.gov/usao-cdca/pr/beverlywood-man-pleads-guilty-securities-fraud-admitting-massive-ponzi-falsely-claimed | Toàn văn qua API (title "Beverlywood Man Pleads Guilty") | 01/11/2026, API HTTP 200 | JSON, không lưu |
| N12 | DOJ USAO C.D. Cal. | Press release 22-027 "L.A. Man Sentenced to 20 Years in Federal Prison for $650 Million Ponzi Scheme…" | — | 14/02/2022 | https://www.justice.gov/usao-cdca/pr/la-man-sentenced-20-years-federal-prison-650-million-ponzi-scheme-falsely-claimed | Toàn văn qua API (title "L.A. Man Sentenced to 20 Years"; API trả 2 kết quả, chọn số 22-027, bỏ thông cáo 20-209 vụ khác) | 01/11/2026, API HTTP 200 | JSON, không lưu |
| N15 | DOJ Office of the Pardon Attorney | Clemency Grants by President Donald J. Trump (2025–Present) ("Updated October 20, 2026"); Pardons Granted by President Joseph Biden; Commutations Granted by President Joseph Biden | — | — | https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present ; https://www.justice.gov/pardon/pardons-granted-president-joseph-biden-2021-2025 ; https://www.justice.gov/pardon/commutations-granted-president-joseph-biden-2021-2025 | Tìm "Horwitz" trong 3 trang HTML: **0 kết quả**. Tệp đính kèm (danh sách tập thể) **không mở lại** ở MR-3 | 01/11/2026, HTTP 200 (3 trang) | HTML, không lưu |
| N18 | SEC | Submit a Tip or Complaint | — | — | https://www.sec.gov/submit-tip-or-complaint | Tiêu đề trang | 01/11/2026, HTTP 200 | — |
| N19 | FINRA | BrokerCheck ("Find a broker, investment or financial advisor") | — | — | https://brokercheck.finra.org/ | Tiêu đề trang | 01/11/2026, HTTP 200 | — |
| N20 | SEC | Investment Adviser Public Disclosure (IAPD) | — | — | https://adviserinfo.sec.gov/ | Tiêu đề trang | 01/11/2026, HTTP 200 | — |
| N21 | FTC | ReportFraud.ftc.gov | — | — | https://reportfraud.ftc.gov/ | Tiêu đề trang | 01/11/2026, HTTP 200 | — |
| N22 | DOJ USAO C.D. Cal. | (mới ở MR-3) Government's Sentencing Position for Defendant Zachary Joseph Horwitz, Dkt. 58 | 2:21-cr-00214-MCS | nộp 31/01/2022 | https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.58.0.pdf (RECAP — đường chính thức theo CLAUDE.md) | tr. 1 (tiêu đề), **tr. 6 dòng 3–14 và 21–22** (đọc text + **đối chiếu ảnh trang**); các trang khác chưa đọc, không dùng | 01/11/2026, HTTP 200 | `ho-so/1inmm-horwitz/doj-sentencing-position-2022.pdf` · `3626166db8ce40e1cfa945cca89bd6a59eee1bae636edc4824585b6d67761575` (28 tr., PDF có text) |

## 2. Câu trích nguyên văn dùng trên hình (đối chiếu ảnh trang)

| Câu (`loi.json`) | Nguyên văn | Nguồn | Đối chiếu |
|---|---|---|---|
| S013 | 1inMM ("one in a million") Capital, LLC | N3 | HTML |
| S018 | "Strategic Partners[]" (hiện: "Strategic Partners") | N1 tr. 3 ¶5 | text PDF |
| S024 | "over the life of the note" | N1 tr. 5 ¶22 | text PDF |
| S031 | "I believed that if HBO was involved, my investment was safe." | N1 tr. 9 ¶46 | **ảnh trang** |
| S032 | "consistent track record of paying large profits" | N1 tr. 9 ¶47 | **ảnh trang** |
| S051 | "lavish lifestyle" | N7 tr. 12 | text PDF |
| S067 | "to lull the investors into believing their funds were safely invested" | N7 tr. 11 dòng 16–17 | text PDF |
| S073 | "a release of funds by April 9th (at the latest)" | N1 tr. 13 ¶76 | **ảnh trang** |
| S075 | "sharing the financial burden with investors (highly doubtful)" | N1 tr. 13 ¶77 | **ảnh trang** |
| S090 | "Defendant Zachary Horwitz portrayed himself as a Hollywood success story." | N22 tr. 6 dòng 3–4 | **ảnh trang** |
| S091 | "…was not a successful businessman or Hollywood insider. He just played one in real life." | N22 tr. 6 dòng 13–14 (bản gốc: "defendant was not…"; N12 chép là "[Horwitz] was not…") | **ảnh trang** |
| S092 | "the largest known Ponzi scheme in the history of this District" | N22 tr. 6 dòng 21–22 | **ảnh trang** |

## 3. Nguồn KHÔNG mở lại được ở MR-3 (không làm nguồn câu nào)

| Mã | Nguồn | Kết quả MR-3 | Xử lý |
|---|---|---|---|
| N9 | Docket CourtListener 2:21-cr-00214 (HTML) và CourtListener REST API v4 | HTML: **HTTP 403** (CloudFront chặn); API: **HTTP 401** (cần khoá tài khoản) | **Chưa mở được.** Không vượt. Không dùng mục docket nào (ngày nhận tội lấy từ N11; bác tội từ N8 tr. 4) |
| N13 | Docket SEC 2:21-cv-02927 (CourtListener) | không thử lại (cùng chặn như N9) | Chưa mở được. Không dùng; vì vậy **không** nói gì về phán quyết với 1inMM Capital hay số tiền receiver thu hồi |
| N14, N16 | Tìm kiếm CourtListener (vụ liên quan; Ninth Circuit) | không thử lại | Chưa mở được ở MR-3; không dùng. Lời **không** nói "không kháng cáo" |
| N17 | Investor.gov — Ponzi Scheme | **HTTP 403** với UA khai báo (đúng cách) | **Chưa mở được.** Không đổi UA. Lời kết **không** dẫn Investor.gov; dùng N18–N21 |
| — | Bản **Consent** của Horwitz trong vụ SEC | không có trên sec.gov | Chưa mở được → lời **không** nói "without admitting or denying" |
| — | Docket mục 94 (18/5/2026), danh sách giảm án tập thể (49 tệp ở MR-1) | không thử lại | Chưa mở được; kiểm lại trước ngày đăng (luật 4) |
| — | Dkt. 1 (Criminal Complaint + affidavit) | không mở | Không dùng; các câu "affidavit states" trong N10 không đưa vào lời |

## 4. Kiểm trạng thái vụ (HIEN-CHUONG §3 luật 4) — ngày chốt lời 01/11/2026
- Ân xá/giảm án: tên "Horwitz" **không có** trên 3 trang DOJ (N15, kiểm 01/11/2026 15:24 UTC; trang Trump cập nhật 20/10/2026). Tệp danh sách tập thể chưa kiểm lại.
- Kháng cáo / §2255 / docket mới: **chưa kiểm được ở MR-3** (N9 bị chặn). Bản án có lời "Defendant advised of his right to appeal" (N8 tr. 4); plea có điều khoản từ bỏ kháng cáo (N7 tr. 15–16, đọc ở MR-1). Lời phim không nói gì về kháng cáo.
- Vụ SEC đối với 1inMM Capital: **chưa có phán quyết đã mở** → 1inMM chỉ nói qua lời Horwitz thừa nhận (●T) hoặc "the SEC alleged" (◐).
- Phải kiểm lại vào **ngày đăng** (M-f), ghi vào gói phát hành.

## 5. Chênh số giữa nguồn (lời dùng số đã nhận tội)
| Mục | SEC (◐) | Plea / DOJ | Lời dùng |
|---|---|---|---|
| Tiền huy động | "over $690 million" (N1 ¶4; N2) | "at least $650 million" (N7 tr. 12) | at least six hundred fifty million (S009) |
| Gốc chưa trả | "more than $234 million" (N1 ¶13) | ≈ $230.36 million (N7 tr. 12) | about two hundred thirty million (S065) |
| Lợi nhuận hứa | 35–45 % (N1 ¶22) | 25–45 % (N7 tr. 10) | twenty-five to forty-five percent (S005, S023) |
| Năm bắt đầu | từ 03/2014 (N1 ¶4) | "in or about March 2014" (N7 tr. 8); "2015" (N10, lúc bắt) | lời không nêu năm bắt đầu bán; chỉ "around 2013" lập công ty (N7 tr. 8) |
