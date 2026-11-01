# 1inMM Capital — Zachary Horwitz · KIỂM TẦNG PHÁP LÝ ĐỘC LẬP

- **Người kiểm:** tác tử độc lập MR-1 (không đọc `reports/**`, `RUI-RO.md`, phần tóm tắt của `NGUON.md`; chỉ dùng CLAUDE.md, HIEN-CHUONG §3, `TANG.md`, bảng danh sách nguồn của `NGUON.md` để lấy URL/tên tệp).
- **Ngày kiểm:** 01/11/2026.
- **Đối tượng chấm:** `docs/ung-vien/1inmm-horwitz/TANG.md` (bảng tầng + mục "Cách nói EN gợi ý").

## Nguồn đã mở

| Mã | Nguồn | Kết quả | Trang/đoạn đã đọc |
|---|---|---|---|
| N1 | `ho-so/1inmm-horwitz/sec-complaint-2021.pdf` | SHA-256 `b7512b6f…8fda007b6c` **khớp** NGUON.md | tr. 3–9, 11–12 (¶5–16, ¶17–31, ¶34–41, ¶49, ¶59–61, ¶69–73) |
| N4 | `ho-so/1inmm-horwitz/sec-final-judgment-horwitz-2024.pdf` | SHA-256 `2ade19ca…4d6845fcf` **khớp** | toàn bộ 4 trang |
| N6 | `ho-so/1inmm-horwitz/doj-indictment-2021.pdf` | SHA-256 `37310c59…db8947b9a8` **khớp** | tr. 1–11 |
| N7 | `ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf` | SHA-256 `a74e0508…0370491a9` **khớp** | tr. 1–2, 4, 8–12, 15–16 |
| N8 | `ho-so/1inmm-horwitz/doj-judgment-commitment-2022.pdf` | SHA-256 `fd458d3e…a012a9` **khớp** | tr. 1 (bản scan, đọc bằng ảnh dựng từ PDF), tr. 2–7 (text) |
| N10–N12 | API chính thức DOJ `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=…` | HTTP 200, toàn văn 3 thông cáo (ngày API: 06/4/2021, 04/10/2021, 14/02/2022) | toàn văn |
| N3, N5 | `https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25067`, `…/lr-25973` (UA khai báo) | HTTP 200 | toàn văn |
| N15 | 3 trang justice.gov/pardon (Trump 2025–nay "Updated October 20, 2026"; Biden pardons "Updated May 14, 2026"; Biden commutations "Updated July 9, 2025") | HTTP 200; tìm "Horwitz": 0 | 190 tệp đính kèm: 163 có lớp text, 0 kết quả "Horwitz"; 12 PDF chỉ là ảnh scan (không tìm được chữ); 15 tệp trả 404 → **27 tệp chưa kiểm được** |
| BOP | `https://www.bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&nameFirst=Zachary&nameLast=Horwitz` | HTTP 200 | 1 kết quả: ZACHARY JOSEPH HORWITZ, 39 tuổi, FPC Yankton, ngày ra tù dự kiến 03/10/2037, chưa có ngày ra thực tế |
| N9, N13, N14, N16 | courtlistener.com (trang docket, trang tìm kiếm, API v3/v4) | **Chưa mở được**: HTML trả 403 (CloudFront chặn), API trả 401 (cần khoá). Không tìm cách vượt chặn | — |

Lưu ý: định danh BOP chỉ khớp theo họ tên đệm + tuổi (39 năm 2026, khớp "34" tháng 4/2021 trong N10); số tù chưa đối chiếu được với hồ sơ toà.

## Bảng chấm

Ký hiệu: **K** = khớp · **MH** = mạnh hơn · **S** = sai · **KKĐ** = không kiểm được.

### Dòng 1 — Zachary Joseph Horwitz, vụ hình sự (●)

| Ô | Phán | Đã đọc + trích |
|---|---|---|
| Tầng ● CONVICTED | K | N8 tr. 1: "defendant has been convicted as charged of the offense(s) of: Securities Fraud … as charged in Count 1". Nhận tội được toà chấp nhận = HIEN-CHUONG §3 (a). |
| Loại phán quyết: nhận tội được toà chấp nhận, Change of Plea 04/10/2021 | K (ngày: qua N11; mục 47 docket KKĐ) | N8 tr. 1: "GUILTY, and the court being satisfied that there is a factual basis for the plea". N11 (ngày 04/10/2021): "pleaded guilty this afternoon to a federal securities fraud charge". |
| Một tội gian lận chứng khoán, Count 1, 15 U.S.C. §§ 78j(b), 78ff; 17 C.F.R. § 240.10b-5 | K | N7 tr. 1–2: "plead guilty to count one … securities fraud, in violation of 15 U.S.C. §§ 78j(b), 78ff". |
| Tuyên 14/02/2022; 240 tháng; 3 năm quản chế | K | N8 tr. 1: ngày "Feb 14 2022"; "imprisoned for a term of 240 months"; "supervised release for a term of 3 years". |
| Bồi hoàn $230.361.884; phí đặc biệt $100 | K | N8 tr. 3: "restitution in the total amount of $230,361,884"; "special assessment of $100". |
| Phán quyết tịch thu tiền | K | N8 tr. 4: "money judgment of forfeiture … incorporated by reference into this judgment". |
| **"Counts 2–13 (gian lận chuyển tiền qua đường dây, trộm danh tính nghiêm trọng)"** | **S** | N6 tr. 1, 5–6: "COUNTS ONE THROUGH FIVE [15 U.S.C. §§ 78j(b), 78ff …]" — Counts 2–5 là **gian lận chứng khoán**; tr. 7: Counts 6–11 wire fraud (18 U.S.C. § 1343); tr. 9–10: Counts 12–13 aggravated identity theft (§ 1028A). |
| Các count còn lại bị bác theo đề nghị của công tố | K | N8 tr. 4: "On Government's motion, all remaining counts ORDERED dismissed." N7 tr. 4: USAO cam kết "move to dismiss the remaining counts". |
| Tự trình diện 14/3/2022 | KKĐ | N8 tr. 4 chỉ là **lệnh**: "report on or before March 14, 2022 at noon". Mục 77 docket (N9) chưa mở được. |
| Kháng cáo — điều khoản từ bỏ (N7 tr. 15–16) | K | N7 tr. 15: "WAIVER OF APPEAL OF CONVICTION" (trừ khiếu nại nhận tội không tự nguyện); "LIMITED MUTUAL WAIVER OF APPEAL OF SENTENCE". N8 tr. 4: "Defendant advised of his right to appeal." |
| Kháng cáo — docket tới mục 94, 9th Cir. 0 kết quả, kết luận "chưa xác minh" | KKĐ (phần docket/9th Cir.); cách kết luận K | CourtListener 403/401. Bảng **không** nói "không kháng cáo", chỉ nói "chưa xác minh" → không mạnh hơn. Dữ kiện gián tiếp: BOP ngày ra dự kiến 03/10/2037, khớp án 240 tháng. |
| Ân xá/giảm án: không có tên, "chưa xác minh trọn vẹn" | K | N15: 3 trang 0 kết quả; tôi kiểm 163/190 tệp đính kèm có text, 0 kết quả; 27 tệp chưa kiểm được (bảng ghi 49). Kết luận "chưa xác minh trọn vẹn" đúng mức. |
| Đã chết?: "chưa xác minh" | K (có thể cập nhật) | BOP 01/11/2026: đang giam tại FPC Yankton, chưa có ngày ra thực tế → còn trong hệ thống BOP (định danh theo tên + tuổi). |
| Vai trò: sáng lập, quản lý duy nhất 1inMM; aka "Zach Avery" | K | N6 tr. 1: "Defendant HORWITZ was 1inMM Capital's sole manager"; "also known as 'Zach Avery'". N7 tr. 8: "defendant founded 1inMM Capital". |
| Trang nguồn được dẫn | K (thiếu sót nhỏ) | N8 tr. 1 không được dẫn dù là trang chứa án 240 tháng (đọc được bằng ảnh); N6 cần thêm tr. 5–7 (Counts 1–11). |

### Dòng 2 — Zachary J. Horwitz, vụ dân sự SEC (◐)

| Ô | Phán | Đã đọc + trích |
|---|---|---|
| Tầng ◐ (consent, không sau xét xử) | K | N4 tr. 1: "consented to the Court's jurisdiction … waived findings of fact and conclusions of law". Không có xét xử → không đủ ● JUDGMENT (§3). |
| Loại phán quyết: consent judgment; từ bỏ kết luận sự kiện, từ bỏ kháng cáo | K | N4 tr. 1: "waived any right to appeal from this Final Judgment"; tr. 3 §IV: "the Consent is incorporated herein". |
| Final Judgment 14/02/2024; cấm vĩnh viễn §17(a), §10(b), Rule 10b-5 | K | N4 tr. 1–2 (§I, §II); tr. 4: "Dated: February 14, 2024". N5: "permanently enjoining Horwitz from violating the antifraud provisions". |
| $62.847.901,05 + $11.375.011,28 = $74.222.912,33, coi như đã thoả mãn bằng bồi hoàn hình sự | K | N4 tr. 3 §III: "for a total of $74,222,912.33, but that disgorgement figure is deemed satisfied by the restitution order". |
| §V: chỉ cho mục đích phá sản, cáo buộc coi là đúng và được thừa nhận | K | N4 tr. 3 §V: "for purposes of exceptions to discharge … the allegations in the complaint are true and admitted by Defendant". |
| Kháng cáo: đã từ bỏ (N4 tr. 1) | K | như trên. |
| Ân xá: không áp dụng; Đã chết: — | K | Vụ dân sự. |
| Nguồn N4 tr. 1–4; N5 | K | — |

### Dòng 3 — 1inMM Capital, LLC (◐)

| Ô | Phán | Đã đọc + trích |
|---|---|---|
| Vai trò: LLC California lập 09/2013, phát hành kỳ phiếu | K | N6 tr. 1: "California limited liability company … created in September 2013"; N1 ¶18 tr. 5: "formed in September 2013". |
| Tầng ◐ | K | N1 ¶16 tr. 4; N3: "The complaint charges Horwitz and 1inMM Capital with violating the antifraud provisions". |
| Loại phán quyết: chưa có phán quyết đã mở được; vụ SEC còn mở, mục mới nhất 21/10/2026 | KKĐ | N13 CourtListener 403. N4 chỉ là judgment "as to Defendant Zachary J. Horwitz". |
| SEC cáo buộc §17(a), §10(b)/Rule 10b-5; công ty không bị truy tố hình sự | K | N1 ¶16 tr. 4; N6 tr. 1: chỉ một bị cáo "ZACHARY JOSEPH HORWITZ". |
| "Hành vi của 1inMM đã được Horwitz thừa nhận … có thể nói ở tầng ● qua miệng Horwitz" | K có điều kiện | N7 tr. 10: "1inMM Capital generally did not and would not acquire or possess the film distribution rights". Chỉ đúng nếu câu luôn gắn "Horwitz admitted in his plea agreement…" và giữ nguyên mức độ của lời thừa nhận; công ty vẫn ◐ (tương tự §3 luật 6a). |
| Kháng cáo / ân xá: không áp dụng | K | Không có vụ hình sự đối với công ty. |
| Nguồn N1; N3; N6 tr. 1; N7 tr. 8–12; N13 | K (N13 KKĐ) | — |

### Dòng 4–14 — các bên không bị cáo buộc / viên chức

| Dòng · ô | Phán | Đã đọc + trích |
|---|---|---|
| HBO: không bị cáo buộc; không cấp phép nội dung từ 1inMM (¶49, ¶69–70, tr. 9, 12) | K | N1 ¶49 tr. 9: "did not have business relationships with Netflix or HBO"; ¶70 tr. 12: "HBO-Latin America Group never licensed content from 1inMM". N7 tr. 11: hợp đồng phân phối "were fake". |
| Netflix: ¶49 | K | N1 ¶49 tr. 9 (như trên). |
| **Nhân viên thật HBO/Netflix = "F.M.; C.M., V.C., J.C."** | **MH** | N12: "using the identities of actual employees of HBO and Netflix" (không nêu ai). N6 tr. 9–10 chỉ ghi "victim F.M." và "victims C.M., V.C., and J.C.", **không** nói họ làm cho HBO/Netflix; Count 12 gắn với Count 6 (chuyển tiền 14/12/2018), không gắn với thư giả của HBO. Gán vai trò là suy luận. |
| Cùng dòng: "victim" ở Counts 12–13, các tội đã bị bác | K | N6 tr. 9–10; N8 tr. 4. |
| Sales agents / phim làm tài sản bảo đảm: 1inMM không ký các hợp đồng đó | K | N7 tr. 11: "had not entered into the asserted license agreements with the identified sales agents". N1 ¶25 tr. 5–6, ¶41 tr. 8 nêu tên phim. |
| Freeway Entertainment: chỉ là lời Horwitz nói với nhà đầu tư (¶73 tr. 12) | K | N1 ¶73: "Horwitz then represented to at least some investors that … a collections account was established at Freeway Entertainment". |
| City National Bank: giữ tài khoản 1inMM và tài khoản cá nhân | K | N6 tr. 2: "a City National Bank account in the name of 1inMM Capital"; N1 ¶59 tr. 11: "his personal City National Bank account". |
| City National Bank: đương sự docket SEC; bị receiver kiện vụ riêng | KKĐ | N13, N14 CourtListener 403. |
| American Express; "celebrity interior designer" (¶12, ¶61) | K | N1 ¶12 tr. 3–4: "payments to American Express of at least $1,842,840 and paid almost $700,000 to a celebrity interior designer" (¶61 tr. 11 ghi "decorator"). |
| Nhà đầu tư: 5 nhóm + hơn 250 nhà đầu tư con; Investor 1/2/3 | K (lưu ý) | N7 tr. 12: "at least five major groups … more than 250 such sub-investors"; N6 tr. 8 "Investor 1/2/3". N1 ¶31 tr. 6 ghi "more than 200 downstream investors" — ¶30–31 không chứa số 250. |
| Receiver | KKĐ | N13 403. |
| Các tên khác trên docket: không xếp tầng, không dùng | K (về cách xử lý); nội dung KKĐ | N13/N14 403. |
| Thẩm phán Scarsi, Snyder; AUSA Schwab, Chao | K | N8 tr. 4 "U. S. District Judge Mark C. Scarsi"; N4 tr. 3 "THE HON. CHRISTINA A. SNYDER"; N7 tr. 1 "ALEXANDER B. SCHWAB … DAVID H. CHAO". |

### Cách nói EN gợi ý

| Câu | Phán | Đã đọc + trích |
|---|---|---|
| "In October 2021, … pleaded guilty in federal court in Los Angeles to one count of securities fraud. In February 2022, a federal judge sentenced him to 20 years … about $230 million in restitution." | K | N11; N12: "Horwitz pleaded guilty in October 2021 to one count of securities fraud"; N8 tr. 1, 3. |
| "In his plea agreement, Horwitz admitted that…" (chỉ Factual Basis N7 tr. 8–12) | K | N7 tr. 8: "Defendant admits that defendant is, in fact, guilty". |
| Không nói "convicted of wire fraud / identity theft" | K | N8 tr. 1 chỉ Count 1. |
| "Prosecutors had also charged wire fraud and aggravated identity theft; those counts were dismissed under the plea deal" | K (thiếu) | Câu đúng nhưng bỏ sót 4 count gian lận chứng khoán khác (Counts 2–5, N6 tr. 5–6) cũng bị bác; nên nói "additional securities fraud counts, wire fraud and aggravated identity theft". |
| SEC: "In 2024 he consented to a final judgment, without a trial, … the roughly $74 million … deemed satisfied by the criminal restitution order." | K | N4 tr. 1, 3. Không dùng "found liable", "convicted" cho vụ dân sự — đúng §3. |
| Không dùng "without admitting or denying" | K | Bản Consent không có trong hồ sơ đã mở; N4 §V có thừa nhận cho mục đích phá sản. |
| 1inMM: "The SEC alleged that Horwitz and his company, 1inMM Capital…" | K | N3. |
| **"Horwitz admitted that his company, 1inMM Capital, never acquired the film rights…"** | **MH** | N7 tr. 10: "1inMM Capital **generally** did not and would not acquire or possess the film distribution rights". "never" mạnh hơn lời thừa nhận. ("never" chỉ có trong cáo buộc SEC, N1 ¶8 / N3 — ◐.) |
| HBO/Netflix: "were not accused of any wrongdoing; according to the SEC, neither company ever did business with 1inMM." | K | N3: "neither Horwitz nor 1inMM had ever sold any movie rights to, or done any business with, HBO or Netflix". |
| Nạn nhân: "investors, many of them his personal friends" (N12); "five major investor groups and more than 250 sub-investors" (N7) | K | N12: "many of whom were personal friends"; N7 tr. 12. |
| Rà "convicted"/"fraud"/"Ponzi" cho chủ thể chưa ● | K | Không câu EN nào dùng "convicted" hay "Ponzi" cho 1inMM hoặc vụ dân sự; "antifraud laws" là tên luật. |

### Kiểm §3 luật 6–7

- Luật 6(a) DPA/NPA: không có. 6(b) chết trước phán quyết: không (BOP cho thấy đang thụ án). 6(c) ân xá/giảm án: không tìm thấy (163/190 tệp + 3 trang); 27 tệp chưa kiểm → giữ "chưa xác minh trọn vẹn". **K**.
- Luật 7 (cột loại phán quyết): cả 3 dòng có phán quyết/cáo buộc đều ghi loại (nhận tội; consent; chưa có phán quyết). **K**. Ghi chú: consent judgment ở đây **không** phải loại "không thừa nhận" thuần (N4 §V), bảng đã nói đúng điều này.

## Tổng điểm

| Phán | Số ô |
|---|---|
| Khớp | 49 |
| Mạnh hơn | 2 |
| Sai | 1 |
| Không kiểm được | 5 |

(Tổng 57 ô thực chất, gồm 2 ô kiểm §3 luật 6–7. Các ô "khớp có lưu ý/thiếu" tính là khớp. 5 ô KKĐ: tự trình diện 14/3/2022; docket/9th Cir. về kháng cáo; phán quyết đối với 1inMM; CNB trên docket/vụ receiver; receiver. Mục 47 docket và nội dung các tên khác trên docket cũng chưa mở được nhưng không tính ô riêng.)

## Sửa bắt buộc

1. **(S) Dòng Horwitz hình sự:** đổi "Counts 2–13 (gian lận chuyển tiền qua đường dây, trộm danh tính nghiêm trọng)" thành "Counts 2–13 (Counts 2–5 gian lận chứng khoán; Counts 6–11 gian lận chuyển tiền qua đường dây; Counts 12–13 trộm danh tính nghiêm trọng)"; dẫn N6 tr. 5–10. Sửa câu EN tương ứng: "Prosecutors had also charged additional securities fraud counts, wire fraud and aggravated identity theft; those counts were dismissed at sentencing on the government's motion, as the plea agreement provided" (N8 tr. 4; N7 tr. 4).
2. **(MH) Câu EN 1inMM:** đổi "never acquired the film rights" thành "Horwitz admitted in his plea agreement that 1inMM Capital generally did not acquire the film distribution rights it pledged as collateral" (N7 tr. 10).
3. **(MH) Dòng nhân viên HBO/Netflix:** bỏ phép gán "F.M.; C.M., V.C., J.C." là nhân viên HBO/Netflix. Ghi tách: "Nhân viên thật của HBO/Netflix bị dùng danh tính (N12, không nêu tên)" và "Các 'victim' F.M.; C.M., V.C., J.C. ở Counts 12–13 (N6 tr. 9–10; cáo trạng không nêu nơi làm việc)".
4. **(KKĐ → đổi cách ghi)** "Tự trình diện thi hành án 14/3/2022": ghi "Lệnh tự trình diện trước trưa 14/3/2022 (N8 tr. 4)" cho tới khi mở được mục 77.
5. Khuyến nghị (không bắt buộc): thêm N8 tr. 1 vào cột nguồn; cập nhật ô "Đã chết?" theo BOP (đang thụ án tại FPC Yankton, ngày ra dự kiến 03/10/2037; định danh theo tên + tuổi); ghi rõ N1 ¶31 nói "more than 200", con số 250 chỉ từ N7/N12; ghi lại số tệp ân xá chưa kiểm (theo lần kiểm này: 27/190).
