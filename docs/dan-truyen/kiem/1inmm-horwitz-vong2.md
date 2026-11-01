# Kiểm độc lập vòng 2 — dàn truyện `1inmm-horwitz`

- **Người kiểm:** tác tử kiểm độc lập vòng 2 (Claude, phiên con), không tham gia soạn dàn truyện.
- **Ngày kiểm:** 01/11/2026.
- **Đối tượng:** `docs/dan-truyen/1inmm-horwitz.md` (bản đã sửa, "NHÁP — chờ kiểm độc lập").
- **Đã đọc:** `CLAUDE.md`; `docs/HIEN-CHUONG.md` (§1, §3 gồm luật 5 và 8, §4, §5); tệp dàn truyện; `docs/ung-vien/1inmm-horwitz/NGUON.md` (chỉ tra mã → tệp/URL); 5 PDF trong `ho-so/1inmm-horwitz/` (`pdftotext -layout`; xem ảnh trang N1 tr. 9, tr. 13, N7 tr. 12, N8 tr. 1); N2, N3, N5 trên sec.gov (curl, UA khai báo "MoneyReroute research <email liên hệ — đã gỡ>"); N10, N11, N12 chỉ qua API chính thức `justice.gov/api/v1/press_releases.json?parameters[title]=…`.
- **Không đọc:** `reports/**`; `TANG.md`, `RUI-RO.md`, `KIEM-TANG.md`; các tệp khác trong `docs/dan-truyen/kiem/` (kết quả vòng 1); dàn truyện vụ khác; git log/diff. **Không mở** N9, N13 (docket CourtListener), Dkt. 58, bản Consent: nằm ngoài phạm vi nguồn được giao → những chỗ dựa vào chúng ghi "không kiểm lại".
- Không vượt rào truy cập, không gọi API trả tiền, không sửa dàn truyện, không commit. Tệp tạm: `/tmp/claude-0/-home-user-money-reroute/1c2cc4e0-12e8-59b7-bad3-2f105161639e/scratchpad/kiem2-1inmm/`.

Ký hiệu chấm: **K** = khớp nguồn và tầng · **MH** = mạnh hơn nguồn hoặc tầng · **S** = sai số/ngày/trang/tầng/người · **KKĐ** = không kiểm được.

## 1. Bảng nguồn đã mở (SHA-256 so với NGUON.md)

| Mã | Tệp / URL | Cách mở | Kết quả | SHA-256 khớp NGUON? |
|---|---|---|---|---|
| N1 | `sec-complaint-2021.pdf` | pdftotext + ảnh tr. 9, 13 | 18 tr.; PDF tr. 2 in số "1" (đúng quy ước "N1 = số trang PDF") | `b7512b6f…7b6c` — **khớp** |
| N2 | sec.gov/newsroom/press-releases/2021-58 | curl, UA khai báo | HTTP 200 | HTML, không có SHA trong NGUON |
| N3 | sec.gov/…/litigation-releases/lr-25067 | curl, UA khai báo | HTTP 200 | HTML |
| N4 | `sec-final-judgment-horwitz-2024.pdf` | pdftotext | 4 tr. | `2ade19ca…5fcf` — **khớp** |
| N5 | sec.gov/…/litigation-releases/lr-25973 | curl, UA khai báo | HTTP 200 | HTML |
| N6 | `doj-indictment-2021.pdf` | pdftotext | 14 tr. | `37310c59…b9a8` — **khớp** |
| N7 | `doj-plea-agreement-2021.pdf` | pdftotext + ảnh tr. 12 | 22 tr.; số trang PDF = "Page x of 22" | `a74e0508…91a9` — **khớp** |
| N8 | `doj-judgment-commitment-2022.pdf` | pdftotext tr. 2–7 + **ảnh tr. 1** | tr. 1 scan: "Feb 14 2022", "240 months", "3 years", aka "AVERY, Zach" | `fd458d3e…12a9` — **khớp** |
| N10 | API DOJ, title "Beverlywood Man Arrested" | API chính thức | HTTP 200, 1 kết quả, ngày 06/04/2021 | JSON |
| N11 | API DOJ, title "Beverlywood Man Pleads Guilty" | API chính thức | HTTP 200, 1 kết quả, ngày 04/10/2021 | JSON |
| N12 | API DOJ, title "L.A. Man Sentenced to 20 Years" | API chính thức | HTTP 200, 2 kết quả; chọn bản "…$650 Million Ponzi Scheme…" ngày 14/02/2022 (bản kia là vụ xổ số khác, bỏ) | JSON |

## 2. Bảng chấm từng dòng

| Dòng | Chấm | Bằng chứng (≤ 25 từ) + trang thực tế | Ghi chú |
|---|---|---|---|
| Logline VI | K | N7 tr. 9 "license to online streaming platforms such as HBO and Netflix"; tr. 10 "25 to 45 percent"; tr. 12 "at least $650 million"; N12 "240 months" | Câu 8e có trong cùng đoạn (N3: "neither… had ever… done any business with, HBO or Netflix") |
| Logline EN | K | N7 tr. 10–11 "purported copies of the distribution agreements were fake" | "front-row seat to the streaming boom" là ẩn dụ, không phải khẳng định về người; có câu 8e |
| H1 | K | MH, không nguồn, nhãn ILLUSTRATIVE | Một câu chung, không tên nền tảng, không chép lời thật — không thành mẫu tin nhắn dùng được (xem §3) |
| H2 | K | N6 tr. 1 "aka 'Zach Avery'"; N1 tr. 2 ¶4 "a Los Angeles based actor"; tr. 5 ¶17 "purports to be an actor" | NB, không nhãn |
| H3 | K | N7 tr. 10 "typically six or twelve months… a calculated return that ranged from 25 to 45 percent" | ●T đúng |
| H4 | K | N7 tr. 9 "falsely claimed 1inMM Capital would then profitably license to online streaming platforms such as HBO and Netflix" | Câu 8e nằm ngay H5 |
| H5 | K | N7 tr. 10–11 "license agreements were fake… distribution agreements were fake"; N3 "neither… done any business with" | |
| H6 | K | N7 tr. 12 "at least $650 million"; N8 tr. 1 (ảnh) "240 months", "Feb 14 2022" | Nên ghi rõ **N8 tr. 1** (ảnh scan) thay vì "N8" |
| 0 | K | = H1–H6 | |
| 1 | K | N7 tr. 8 "In or about 2013… promoted as a film distribution company… principal place of business was in Los Angeles"; N6 tr. 1 ¶2 "sole manager" | Vế "sole manager" để ◐ là đúng |
| 2 | K | N7 tr. 9 "for further distribution in regions outside the United States" | 8e có |
| 2b | K | N1 tr. 3 ¶5 "primarily from Latin America… 'Strategic Partners[]'" | ◐ đúng. Lỗi trình bày: ngoặc đơn lặp đôi trong cột luật 8 |
| 3 | K | N7 tr. 10 "approximately $35,000 to $1.5 million… specified amount to be paid at maturity, a calculated return… 25 to 45 percent" | Chữ "trên cả kỳ hạn" là suy từ "paid at maturity"; câu nói rõ là N1 tr. 5 ¶22 "over the life of the note" (◐) — nên dẫn kèm |
| 4 | **MH** | N1 tr. 9 ¶46 "I believed that if HBO was involved, my investment was safe." (khớp ảnh); ¶47 "consistent track record of paying large profits" | "nhiều năm được **trả đúng hạn**": nguồn không nói "đúng hạn". Dùng "a consistent track record of paying large profits, the SEC alleged" |
| 5 | K | N7 tr. 12 "at least five major groups… more than 250 such sub-investors (subject to the reservation of rights…)"; tr. 14 "right to contest the number of sub-investors"; N12 "many of whom were personal friends" | Câu bảo lưu bắt đầu ở tr. 13 dòng 27 → dẫn "tr. 13–14" chính xác hơn |
| 6 | **MH** | N7 tr. 10 "listed the specific film(s)"; "did not and would not enter into any distribution agreements with the online streaming platforms **for these specified films**" | Dàn truyện ghi "một phim" (nguồn: film(s)) và bỏ vế "cho các phim đó" → rộng hơn phần ●T. Vế rộng chỉ có ở N12 (lời DOJ) / N1 ¶49 (◐) |
| 6b | K | N7 tr. 10–11 "fraudulent copies of purported license agreements… sales agents for the production companies"; "purported copies of the distribution agreements were fake" | |
| 7 | K | N7 tr. 12 "payments to prior investors, maintain 1inMM Capital's facade… disbursements to himself… lavish lifestyle" | |
| 7b | **MH** | N12 "$6 million Beverlywood residence, luxury cars, and **travel by private jet**, according to the government's sentencing memorandum"; N1 tr. 3 ¶10 "$5.7 million" | "máy bay riêng" trong danh sách tài sản dễ hiểu là **sở hữu** máy bay; nguồn chỉ nói **đi lại** bằng máy bay riêng |
| 8 | K | N7 tr. 12 "Beginning in or about December 2019… defaulting on all of its outstanding promissory notes… approximately $230.36 million" | |
| 9 | K | N7 tr. 11 "he had not been in communication with the online streaming platforms, and the correspondence… was fake"; N12 "identities of actual employees of HBO and Netflix"; N8 tr. 4 "all remaining counts ORDERED dismissed" | Counts 12–13 = N6 tr. 9–10 (aggravated identity theft) — đúng |
| 9b | K | N1 tr. 13 ¶76 "release of funds by April 9th (at the latest)" (khớp ảnh); ¶77 "investors could provide funds to 1inMM to pay legal counsel" | ◐ đúng; ngày 12/03/2021 |
| 10 | K | N3 "filed April 5, 2021"; N2 (06/04/2021) "obtained an asset freeze"; N10 (06/04/2021) "arrested this morning… taken into custody by special agents with the FBI" | |
| 11 | K | N7 tr. 1–2 "plead guilty to count one… securities fraud"; tr. 4 "move to dismiss the remaining counts"; N8 tr. 1 (ảnh) "240 months"; tr. 3 "$230,361,884"; tr. 4 Scarsi; N11 ngày 04/10/2021 | Thêm **N8 tr. 1** vào cột nguồn (240 tháng, ngày 14/02/2022 nằm ở tr. 1, không ở tr. 3–4). Tội danh còn lại: N6 Counts 1–5, 6–11, 12–13 — đúng |
| 12 | K | N4 tr. 3 §III "$62,847,901.05… $11,375,011.28… total of $74,222,912.33… deemed satisfied by the restitution order" | Lưu ý: N5 **không** có chữ "consent"; căn cứ consent là N4 tr. 1 ("consented to the Court's jurisdiction… waived findings") và §IV tr. 3 ("the Consent is incorporated") |
| 13 | K (có điều kiện) | N12 "He just played one in real life." — nguyên văn khớp, nguồn ghi "prosecutors argued in a sentencing memorandum" | Câu tách riêng vô nghĩa; nếu dùng phải kèm vế trước "was not a successful businessman or Hollywood insider". Dkt. 58 không kiểm |
| 14 | K | §4 | |
| Cú treo §3 | **MH** | N12 "For more than five years, Horwitz **raised millions of dollars** from investors…"; N7 tr. 12 "used the money to make payments to prior investors" | "more than five years" trong N12 gắn với việc **huy động tiền**, không gắn với việc **trả cho nhà đầu tư trước**; ghép hai nguồn tạo câu không nguồn nào nói, lại ghi tầng ●T. Vế "Then, beginning around December 2019…" khớp N7 tr. 12 |
| L1 | K | N1 tr. 6 ¶25 bảng: "$744,500 → $1,004,084… (6 months) 35%" | 1,35² = 1,8225 → ≈ 82 %/năm (lãi kép); lãi đơn = 70 %. "Khoảng 80 %" đúng nếu **tái đầu tư cả gốc lẫn lãi** — nên nói rõ giả định. Dẫn "tr. 6" |
| L2 | K | N1 tr. 9 ¶50 "induced investors to purchase additional notes and to raise funds from downstream investors" (◐) | Mức khái niệm; không mẫu lời dụ |
| L3 | K | N7 tr. 12 "sub-investors who did not have direct contractual agreements"; tr. 9 "notes constituted 'securities'" | Không ám chỉ nhóm trung gian có lỗi; không khuyên pháp lý |
| D | **MH** (điểm 5) | N1 tr. 13 ¶77 "suggested… investors could provide funds… 'sharing the financial burden with investors (highly doubtful)'" | (5) "xin thêm tiền" mạnh hơn "gợi ý (chính ông ghi 'highly doubtful')". (4) "không đăng ký": nếu gắn với vụ thì nguồn là N1 tr. 5 ¶18 (◐), nhịp 5 không chứa dữ kiện này |
| P | K | — | Nguyên tắc chung, không sản phẩm/tỷ trọng |
| §5 (a) | K | N8 tr. 1 "convicted as charged… Securities Fraud… Count 1"; N11; N12 | |
| §5 (b) | K | N1 tr. 2 ¶1 (1inMM là bị đơn) | "chưa có phán quyết đã mở" dựa N13 — không kiểm lại (ngoài phạm vi) |
| §5 (c) | K | — | Không có tên nhóm/LLC, ngân hàng, kế toán trong các nhịp |
| §5 (d) | K | N11 "admitted operating a Ponzi scheme"; N12 tiêu đề "$650 Million Ponzi Scheme" | "what the Justice Department called…" đúng chủ thể |
| §5 (e) | K | N3 câu "neither… done any business with" | Xem §4 dưới: nhịp 4, 9 mới ghi "kèm", chưa viết câu |
| §5 (f) | K | — | |
| §5 KBCB | K | N6 tr. 9–10 F.M., C.M., V.C., J.C.; N7 tr. 12 "Investor 1" + tên phim; N1 tr. 12 ¶73 Freeway Entertainment; N8 tr. 3 tên bên nhận bồi hoàn | Tất cả không nêu tên trong nhịp — đạt |

## 3. Móc câu, cú treo, bài học

- **Móc câu H1–H6:** không có câu nào ám chỉ HBO/Netflix hay nhóm trung gian có lỗi; H5 đặt câu "not accused" ngay sau lần nêu tên ở H4. Không nhãn "con man"/"Hollywood scammer" (đã ghi rõ ở ghi chú). H1 là một câu chung ("Delay on the platform side. Funds by next week."), không tên nền tảng, không thông tin liên lạc — **không** thành mẫu tin nhắn chép dùng được theo §1; giữ đúng mức này ở MR-3 (không mở rộng thành chuỗi tin nhắn).
- **Cú treo:** không ám chỉ bên thứ ba; vấn đề duy nhất là **ghép nguồn** làm câu mạnh hơn (xem bảng). Không có hướng dẫn làm.
- **Bài học:** L1 là phép tính phòng vệ (đổi lợi nhuận kỳ hạn ra năm) — không phải cách dựng kỳ phiếu. L2 ở mức giai đoạn, không lời dụ. L3 không giải thích cách chia tầng để né đăng ký. D(2) hướng người xem tự liên hệ công ty qua kênh chính thức — phòng vệ. P không khuyên sản phẩm. **Không** có chỗ nào thành hướng dẫn làm (§1 đạt). Nhịp 3 và 6b đã ghi "không mô tả cấu trúc ở mức sao chép được", "không nói cách làm giả" — đạt.

## 4. Rà luật 8 và luật 5

| Điểm | Kết quả |
|---|---|
| 8a | Đạt — Horwitz ● (N8 tr. 1: nhận tội, kết án Count 1) |
| 8b | Đạt — 1inMM chỉ qua ●T hoặc "the SEC alleged"; vụ dân sự Horwitz là consent (◐) |
| 8c | Đạt — không tên nhóm nhà đầu tư, LLC, ngân hàng, kế toán, receiver |
| 8d | Đạt — không nhãn; "Ponzi" qua chủ thể DOJ; nhịp 11 không nói "convicted of wire fraud/identity theft" |
| 8e | Đạt có điều kiện. Câu đầy đủ có ở: logline VI, logline EN, H5 (phủ H4), nhịp 2, 2b. Nhịp 4 và 9 chỉ ghi "kèm câu không liên quan" — phải **viết thành lời** ở MR-3. Nhịp 9b có điều kiện ("nếu trích phần nhắc HBO") — ¶77 nhắc HBO ngay trong câu dẫn của SEC, nên coi như **luôn** cần. Nhịp 6/6b nói "nền tảng" không tên — đạt, nhưng nếu hình đặt cạnh tên HBO/Netflix thì lặp câu 8e |
| 8f | Đạt — không suy đoán động cơ; chi tiêu theo N12/N1 (7b cần sửa chữ "máy bay riêng") |
| Luật 5 | Đạt — nhà đầu tư nhịp 4 ẩn danh; nhân viên HBO/Netflix không tên; Investor 1–3, F.M./C.M./V.C./J.C., phim, đại lý, Freeway Entertainment, bên nhận bồi hoàn N8 tr. 3, nhà thiết kế nội thất: không nêu tên. §7 cấm dùng ảnh N8 tr. 1 và tr. 3 — đúng (tr. 1 có 4 số cuối SSN) |

## 5. Tổng

**40 dòng: K 35 · MH 5 · S 0 · KKĐ 0.** (Không kiểm lại: trạng thái phán quyết 1inMM qua N13, Dkt. 58 cho nhịp 13 — dàn truyện đã tự ghi là chưa mở.)

Tầng, số tiền, ngày, số vụ, tên thẩm phán đều khớp nguồn. Không có lỗi S. Năm chỗ MH đều là lời mạnh hơn nguồn một nấc, sửa bằng đổi chữ.

## 6. Sửa bắt buộc

1. **Cú treo §3:** bỏ ghép "for more than five years" với việc trả nhà đầu tư trước. Ví dụ: *"For more than five years, he kept raising money, the Justice Department said — and in his plea agreement he admitted using new money to pay earlier investors. Then, beginning around December 2019, 1inMM started defaulting on all of its outstanding notes."* (N12; N7 tr. 12).
2. **Nhịp 4:** thay "nhiều năm được trả đúng hạn" bằng "the SEC alleged investors were deceived by his consistent track record of paying large profits" (N1 tr. 9 ¶47).
3. **Nhịp 6:** "một hoặc vài phim" (film(s)); vế ●T giữ "không ký hợp đồng phân phối nào với nền tảng **cho các phim đó**" (N7 tr. 10). Nếu muốn câu rộng → gắn chủ thể DOJ (N12) hoặc "the SEC alleged" (N1 ¶49).
4. **Nhịp 7b:** "máy bay riêng" → "đi lại bằng máy bay riêng" / "travel by private jet" (N12).
5. **Bài học D(5):** "xin thêm tiền" → "gợi ý nhà đầu tư góp tiền chi phí kiện" hoặc dạng chung "asks investors for more money to 'fix' the delay" **không** gắn trực tiếp vào lời Horwitz; nếu gắn nhịp 9b phải giữ đúng "suggested… (highly doubtful)", ◐.

## 7. Khuyến nghị

- Dẫn trang chính xác: H6 và nhịp 11 thêm **N8 tr. 1** (ảnh scan: 240 tháng, 14/02/2022); nhịp 5 "N7 tr. 13–14" cho câu bảo lưu; L1 "N1 tr. 6 ¶25"; nhịp 3 dẫn kèm N1 tr. 5 ¶22 cho chữ "over the life of the note".
- Nhịp 12: ghi căn cứ consent là N4 tr. 1 và §IV tr. 3; N5 không có chữ "consent".
- L1: nêu giả định "tái đầu tư cả gốc lẫn lãi"; có thể kèm lãi đơn ≈ 70 %/năm để người xem thấy cả hai cách tính.
- Nhịp 13: nếu dùng, trích kèm vế "was not a successful businessman or Hollywood insider" để câu có nghĩa; vẫn phải đối chiếu Dkt. 58.
- Nhịp 4, 9, 9b: viết sẵn câu 8e thành lời trong bảng (hiện chỉ ghi "kèm").
- D(4): nếu nói 1inMM không đăng ký thì gắn "the SEC alleged" (N1 tr. 5 ¶18).
- Trình bày: nhịp 2b cột luật 8 có ngoặc đơn lặp đôi.
- H1: giữ ở một câu chung, không tên nền tảng, không số/email, để không thành mẫu tin nhắn (§1).
