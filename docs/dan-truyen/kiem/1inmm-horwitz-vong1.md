# Kiểm độc lập dàn truyện `1inmm-horwitz`, vòng 1

> Tệp được kiểm: `docs/dan-truyen/1inmm-horwitz.md` (bản NHÁP, soạn 01/11/2026).
> Người kiểm: tác tử kiểm độc lập (Claude, phiên con do điều phối giao), **01/11/2026**.
> Thang chấm: **K** khớp · **MH** mạnh hơn nguồn (chắc hơn, rộng hơn, hoặc tầng cao hơn trạng thái pháp lý) · **S** sai (số, ngày, trang, tầng, người) · **KKĐ** không kiểm được.
> Quy ước trang: N1 = số trang PDF (số in ở chân trang nhỏ hơn 1, đã xác nhận trên ảnh trang 9 và 13). N4, N6, N7, N8 = "Page x of y" của toà, và với 4 tệp này số đó trùng số trang PDF.

## 0. Phạm vi đọc

**Đã đọc:** `CLAUDE.md`; `docs/HIEN-CHUONG.md` (toàn văn); tệp dàn truyện; `docs/ung-vien/1inmm-horwitz/NGUON.md` (chỉ dùng để tra mã nguồn sang tệp/URL); 5 PDF ở `ho-so/1inmm-horwitz/` (`pdftotext -layout`, đọc toàn bộ các trang được dẫn); ảnh trang N8 tr. 1 (bản scan), N1 tr. 9 và tr. 13 (đối chiếu câu trích nguyên văn); N2, N3, N5 (sec.gov, curl với UA khai báo, HTTP 200); N10, N11, N12 (API chính thức `justice.gov/api/v1/press_releases.json`, HTTP 200, mỗi truy vấn 1 kết quả, số thông cáo 21-059, 21-207, 22-027 khớp).

**Không đọc:** `reports/**`, `docs/ung-vien/*/TANG.md`, `RUI-RO.md`, `KIEM-TANG.md`, dàn truyện vụ khác, git log/diff, thư mục tạm ngoài thư mục của người kiểm.

**Không mở được (không vượt rào):**
- N9, docket CourtListener 2:21-cr-00214: **HTTP 403 CloudFront "Request blocked"** → chưa mở được. Không thử đổi UA hay dùng bản lưu.
- N17, Investor.gov "Ponzi Scheme": **HTTP 403** với UA khai báo → chưa mở được (xem Khuyến nghị K1).
- Dkt. 58 (bản ghi nhớ tuyên án của công tố), bản Consent của Horwitz (vụ SEC): không có trong repo, không mở.

## 1. Nguồn đã mở

| Mã | Tệp / URL | Trang đã đọc | SHA-256 đo được | So với NGUON |
|---|---|---|---|---|
| N1 | `ho-so/1inmm-horwitz/sec-complaint-2021.pdf` (18 tr.) | PDF tr. 2–13 (¶1–81); ảnh tr. 9, 13 | `b7512b6f1e705b0c90e534362289548eb19200d9759b0d675ecf6d8fda007b6c` | **Khớp** |
| N4 | `ho-so/1inmm-horwitz/sec-final-judgment-horwitz-2024.pdf` (4 tr.) | tr. 1–4 | `2ade19cae9af206d099541583c4e192850353aefa9d2c7541c6b2ad4d6845fcf` | **Khớp** |
| N6 | `ho-so/1inmm-horwitz/doj-indictment-2021.pdf` (14 tr.) | tr. 1–14 | `37310c59afbc6d23b4be7243d9776a3fe7e19f6ee8d92a3cff6ce9db8947b9a8` | **Khớp** |
| N7 | `ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf` (22 tr.) | tr. 1–4, 8–14 | `a74e05082cd80fa3c6c88d9f1dacd9d4c904ed9e26d75650547b8c5a370491a9` | **Khớp** |
| N8 | `ho-so/1inmm-horwitz/doj-judgment-commitment-2022.pdf` (7 tr.) | tr. 1 (ảnh), 2–7 | `fd458d3e9c76cf371d05c16269f362ff5a5daed44ac27ba36032c88d45e012a9` | **Khớp** |
| N2 | sec.gov/newsroom/press-releases/2021-58 | toàn văn | HTML, không lưu | HTTP 200 |
| N3 | sec.gov/…/litigation-releases/lr-25067 | toàn văn | HTML, không lưu | HTTP 200 |
| N5 | sec.gov/…/litigation-releases/lr-25973 | toàn văn | HTML, không lưu | HTTP 200 |
| N10 | DOJ API, tiêu đề "Beverlywood Man Arrested…" (21-059, ngày 06/04/2021) | toàn văn | JSON, không lưu | HTTP 200 |
| N11 | DOJ API, "Beverlywood Man Pleads Guilty…" (21-207, ngày 04/10/2021) | toàn văn | JSON, không lưu | HTTP 200 |
| N12 | DOJ API, "L.A. Man Sentenced to 20 Years…" (22-027, ngày 14/02/2022) | toàn văn | JSON, không lưu | HTTP 200 |
| N9 | courtlistener.com/docket/59885055/ | — | — | **Chưa mở được** (403 CloudFront) |

## 2. Bảng chấm từng nhịp

### 2.1 Logline (chấm thêm, không tính vào tổng)

| Mục | Điểm | Bằng chứng (trang thực tế) | Vấn đề |
|---|---|---|---|
| Logline VI | **MH** | N7 tr. 12: "fraudulently obtained at least $650 million"; "used the money to make payments to prior investors" | Câu "tiền người mới trả cho người cũ — ít nhất 650 triệu USD" đọc như 650 triệu USD là số tiền đã xoay vòng trả người cũ. 650 triệu là **tổng huy động**. "Bán cho bạn bè" là lời DOJ (N12), không nằm trong plea. |
| Logline EN | **S** | N7 tr. 10–11: license agreements với sales agents "were fake"; 1inMM "generally did not… acquire" quyền phim | "The deals with HBO and Netflix were the one thing… that wasn't real" sai: hợp đồng cấp phép với đại lý cũng giả, quyền phim nhìn chung không được mua. Câu này cũng nêu HBO/Netflix mà không có câu "không liên quan" (luật 8e). |

### 2.2 Móc câu H1–H6

| # | Tầng gán | Điểm | Bằng chứng (≤ 25 từ, trang thực tế) | Ghi chú |
|---|---|---|---|---|
| H1 | MH (minh hoạ) | **K** | N7 tr. 11: "defendant sent the investors emails and text messages regarding progress addressing the actions purportedly causing the missed payments" | Cảnh minh hoạ có gốc hồ sơ, nhãn đúng §4. Lời "Delay on the platform side" lặp lại lời đổ lỗi cho nền tảng **trước** câu miễn trừ ở H5; chấp nhận được vì H5 nằm trong cùng 30 giây (xem §3). |
| H2 | NB | **K** | N6 tr. 1: "ZACHARY JOSEPH HORWITZ, aka 'Zach Avery,'"; N1 tr. 2 ¶4: "Horwitz, a Los Angeles based actor"; N1 tr. 5 ¶17: "purports to be an actor" | N8 tr. 1 (ảnh) cũng ghi "akas: AVERY, Zach"; N10: "used the screen name 'Zach Avery'". |
| H3 | ●T | **K** | N7 tr. 10: "typically six or twelve months… a calculated return that ranged from 25 to 45 percent" | "often" ≈ "typically": đạt. |
| H4 | ●T | **K** | N7 tr. 9: "profitably license to online streaming platforms such as HBO and Netflix for further distribution in regions outside the United States" | |
| H5 | ●T + 8e | **K** | N7 tr. 11: "the purported copies of the distribution agreements were fake"; N3: "1inMM actually had no business relationship with either company" | Vế "according to the SEC" phải giữ chủ thể SEC (N3 là thông cáo về đơn kiện). |
| H6 | ●T / ● | **K** | N7 tr. 12: "obtained at least $650 million"; N8 tr. 1 (ảnh): "Feb 14 2022… imprisoned for a term of 240 months" | N12 cũng ghi "sentenced today to 240 months". |

### 2.3 Bảng nhịp

| # | Tầng gán | Điểm | Bằng chứng (≤ 25 từ, trang thực tế) | Ghi chú |
|---|---|---|---|---|
| 0 | ●/●T/MH | **K** | (tổng hợp H1–H6) | |
| 1 | ●T | **MH** | N7 tr. 8: "In or about 2013, defendant founded 1inMM Capital… promoted as a film distribution company… principal place of business was in Los Angeles" | Vế "**người quản lý duy nhất**" không có trong Factual Basis. Nó chỉ có ở **cáo trạng** N6 tr. 1 ¶2 ("sole manager") và đơn kiện SEC N1 tr. 5 ¶17 ("sole principal"), tức tầng ◐, nhưng đang được gán ●T. |
| 2 | ●T | **K** | N7 tr. 9: "would purchase distribution rights to certain films… license to online streaming platforms such as HBO and Netflix" | |
| 2b | ◐ | **K** | N1 tr. 3 ¶5: "primarily from Latin America… HBO, Netflix, and other media corporations were 1inMM's 'Strategic Partners[]'" | Nhịp nêu HBO/Netflix nhưng cột luật 8 **không** ghi kèm câu "không liên quan" (xem §4, 8e). |
| 3 | ●T | **K** | N7 tr. 10: "principal… ranged from approximately $35,000 to $1.5 million… calculated return that ranged from 25 to 45 percent" | Lợi nhuận này tính **trên cả kỳ hạn**, không phải theo năm (quan trọng cho L1). |
| 4 | ◐ | **K** | N1 tr. 9 ¶46: "One investor stated that 'I believed that if HBO was involved, my investment was safe.'"; ¶47: "consistent track record of paying large profits" | Đã đối chiếu ảnh trang 9: trích đúng nguyên văn. Vế "nhiều năm" có ở N2/N3 ("for many years paid supposed returns", SEC cáo buộc). Vế "đúng hạn" hơi mạnh hơn: ¶47 chỉ nói "consistent track record". Nhịp nêu HBO nhưng chưa kèm câu 8e. |
| 5 | ●T | **MH** | N7 tr. 12: "at least five major groups… more than 250 such sub-investors (subject to the reservation of rights in paragraph 12 below)"; N7 tr. 14: "defendant reserves the right to contest the number of sub-investors" | (1) Con số "hơn 250" **không** phải sự việc thừa nhận trọn vẹn: Horwitz bảo lưu quyền tranh cãi con số này. (2) "Nhiều người là bạn bè" là lời DOJ trong thông cáo N12 ("many of whom were personal friends"), không có trong plea, nên không phải ●T. |
| 6 | ●T | **K** | N7 tr. 10: "1inMM Capital generally did not and would not acquire… and… did not and would not enter into any distribution agreements with the online streaming platforms for these specified films" | Dàn viết "không ký hợp đồng phân phối nào với nền tảng" mà bỏ mất phần giới hạn "**for these specified films**". Nên giữ phần này (Khuyến nghị). |
| 6b | ●T | **K** | N7 tr. 10–11: "fraudulent copies of purported license agreements… sales agents for the production companies"; tr. 11: "distribution agreements were fake" | |
| 7 | ●T | **K** | N7 tr. 12: "payments to prior investors, maintain 1inMM Capital's facade of legitimate operations, make disbursements to himself… finance his own lavish lifestyle" | |
| 7b | ◐ | **K** | N12: "$6 million Beverlywood residence, luxury cars, and travel by private jet, according to the government's sentencing memorandum"; N1 tr. 3 ¶10: "$5.7 million personal home" | Viết là "**đi** máy bay riêng" (travel by private jet), không phải sở hữu máy bay. N1 tr. 11 ¶59 ("chartered jets") là cáo buộc. |
| 8 | ●T | **K** | N7 tr. 12: "Beginning in or about December 2019, 1inMM Capital began defaulting on all of its outstanding promissory notes… approximately $230.36 million" | |
| 9 | ●T / ● | **MH** | N7 tr. 11: "he had not been in communication with the online streaming platforms, and the correspondence he was supposedly forwarding was fake"; N12: "using the identities of actual employees of HBO and Netflix" | Vế đổ lỗi và thư từ giả là **●T**: K. Vế "**danh tính nhân viên thật**" chỉ là lời DOJ (N12), không có trong Factual Basis; các tội **trộm danh tính nghiêm trọng** (N6 tr. 9–10, Counts 12–13) **đã bị bác** (N8 tr. 4). Gán ● cho vế này là nâng tầng. |
| 9b | ◐ | **K** | N1 tr. 13 ¶76: "release of funds by April 9th (at the latest)"; ¶77: "investors could provide funds to 1inMM to pay legal counsel" | Đã đối chiếu ảnh trang 13. ¶77 có câu Horwitz tự thêm "**(highly doubtful)**": nếu trích thì trích đủ. |
| 10 | TT | **K** | N3: "C.D. Cal. filed April 5, 2021"; N2 (06/04/2021): "obtained an asset freeze"; N10 (06/04/2021): "arrested this morning… taken into custody by special agents with the FBI" | |
| 11 | ● | **K** | N7 tr. 1–2: "plead guilty to count one… securities fraud"; N11 (04/10/2021): "pleaded guilty this afternoon"; N8 tr. 3: "restitution in the total amount of $230,361,884"; N8 tr. 4: "On Government's motion, all remaining counts ORDERED dismissed"; N6 tr. 7–10 (Counts 6–13) | Thiếu trang: vế "như thoả thuận" nằm ở **N7 tr. 4** ("move to dismiss the remaining counts"); vế bác tội và tên thẩm phán nằm ở **N8 tr. 4**. N9 chưa mở được, nhưng các nguồn khác đã đủ. |
| 12 | ◐ consent | **K** (diễn đạt phải sửa) | N4 tr. 3 §III: "disgorgement of $62,847,901.05… prejudgment interest… $11,375,011.28, for a total of $74,222,912.33… deemed satisfied by the restitution order" | Câu "~74,2 triệu USD hoàn trả + lãi" dễ bị viết thành EN "$74.2 million in disgorgement plus interest", mà như vậy là **sai**. 74,2 triệu USD là **tổng** (62,8 triệu hoàn trả + 11,4 triệu lãi). Consent: N4 tr. 1 "consented… waived findings of fact"; tr. 3 §IV "the Consent is incorporated". |
| 13 | ◐ (lời công tố) | **K** đối với N12 | N12: "'…He just played one in real life.'" (prosecutors argued in a sentencing memorandum) | Bản gốc Dkt. 58: KKĐ (chưa mở), nên giữ điều kiện như dàn ghi. |
| 14 | — | **MH** | (xem §3: L1, L3, D5) | |

### 2.4 Cú treo (§3 dàn)

| Câu | Tầng gán | Điểm | Bằng chứng | Vấn đề |
|---|---|---|---|---|
| "For five years, the payments kept coming. Then, in December 2019, they stopped — on every note." | ●T | **MH** | N7 tr. 12: "Beginning in or about December 2019, 1inMM Capital **began defaulting** on all…"; N11, N12: "Investors started to complain after 1inMM Capital began defaulting on notes in 2019"; N10: "defaulting on notes at various times in 2019" | (1) Factual Basis **không** nói các khoản trả "kept coming" liền 5 năm. Nó chỉ nói tiền được dùng "to make payments to prior investors". (2) "In December 2019 they stopped — on every note" là gọn hơn nguồn: nguồn ghi "in or about" và "began defaulting", còn DOJ cho thấy vỡ nợ lẻ tẻ đã có trong năm 2019. |

## 3. Móc câu, cú treo, bài học cơ chế

**Ám chỉ quá tầng:**
- **HBO/Netflix:** H1 hiện lời đổ lỗi "platform side" trước H5. Chấp nhận được với điều kiện H5 nằm trong cùng đoạn 30 giây và H1 không nêu tên nền tảng, không có giao diện. Logline EN nêu HBO/Netflix mà không có câu miễn trừ (phải sửa).
- **Nhóm nhà đầu tư trung gian:** không có câu nào ám chỉ họ có lỗi. Nhịp 5 và L3 gọi đúng vai "sub-investors"/nhóm. **Lưu ý:** N8 tr. 3 in tên 4 bên nhận bồi hoàn. Nếu dùng ảnh trang N8 trên hình thì phải che phần này.
- **Nhãn:** không có "con man" hay "scammer". Câu N12 ở nhịp 13 không gán nhãn ngoài tội danh. Đạt.

**Phép thử "làm theo được ngay":**
- H1: lời nhắn chung chung, không phải kịch bản dụ dùng lại được. **Đạt.**
- **L1, kiểm số học:** 1,40² = 1,96, tức lãi kép khoảng 96 %/năm ("gần gấp đôi"): **đúng**. Lãi đơn năm hoá là 80 %. Có hai vấn đề: (a) cặp "40 % trong 6 tháng" **không** có trong N7. N7 chỉ cho dải 25–45 % với kỳ "typically six or twelve months", nên mức thấp (25 % trong 12 tháng) chỉ là 25 %/năm. Bảng mẫu của SEC (N1 tr. 6 ¶25, ◐) ghi 35–36 % cho kỳ 6 tháng (1,35² ≈ 1,82, tức khoảng 82 %/năm) và 43 % cho kỳ 12 tháng. (b) "mức không doanh nghiệp bình thường nào trả đều đặn" là câu tuyệt đối không có nguồn đã mở (N17 chưa mở được). Không phải hướng dẫn làm: **đạt** phép thử, nhưng phải sửa độ chính xác.
- L2: không có lời dụ hay mẫu tin nhắn: **đạt**. Vế "khiến người cũ đầu tư thêm và rủ người mới" lấy từ N1 tr. 9 ¶50 (◐), nên ghi "the SEC alleged" nếu nói về vụ này.
- **L3:** (a) "có thể không có quyền đòi trực tiếp" là **suy luận pháp lý** không có trong nguồn: N7 tr. 12 chỉ nói "did not have direct contractual agreements". Câu này gần với khuyên pháp lý (§1). (b) "Kỳ phiếu như vậy vẫn là chứng khoán" khái quát hoá N7 tr. 9 ("which notes constituted 'securities'"), là câu chỉ cho vụ này, nên **MH**. (c) "nên phải đăng ký hoặc được miễn": nguồn pháp luật chưa mở, nên **KKĐ**. Không giải thích cách né đăng ký: **đạt** phép thử.
- **D(5)** "xin thêm tiền": N1 tr. 13 ¶77 chỉ là "suggested… investors could provide funds", kèm chính lời ông "(highly doubtful)". "Xin" hơi mạnh, nên đổi thành "gợi ý góp thêm tiền". D(1)–(4), P: đạt.

## 4. Luật 8 (a–f) và luật 5

| Điểm | Kết quả kiểm | Ghi chú |
|---|---|---|
| (a) | **Đạt** | Horwitz ●: N8 tr. 1 "convicted as charged of… Securities Fraud… Count 1". |
| (b) | **Đạt** | 1inMM chỉ qua ●T hoặc "the SEC alleged". Vụ SEC đối với Horwitz là consent (N4). Phán quyết đối với 1inMM: KKĐ (chưa mở). |
| (c) | **Đạt** | Không nêu tên nhóm trung gian, ngân hàng hay bên bị kiện tư. Lưu ý che tên bên nhận bồi hoàn trên N8 tr. 3 nếu dùng ảnh trang. |
| (d) | **Đạt về nhãn; S về nguồn dẫn** | §5(d) của dàn dẫn "Ponzi scheme… N7 tr. 12", nhưng chữ "Ponzi" **không xuất hiện trong N7** (đã tìm toàn văn). Từ này có ở N11 ("admitted operating a Ponzi scheme", lời DOJ), N12, N6 tr. 4 (cáo buộc) và N1 ¶4 (cáo buộc). Phải dẫn N11/N12 và nói qua chủ thể DOJ. |
| (e) | **Chưa đạt trọn** | §5(e) khẳng định "mỗi đoạn có nêu kèm câu không liên quan", nhưng nhịp 2b, 4, 9b (¶77 nhắc HBO nếu trích đủ) và Logline EN chưa ghi kèm. Câu "according to the SEC, neither company ever did business with 1inMM" khớp N2/N3 ("neither Horwitz nor 1inMM had ever… done any business with, HBO or Netflix"). Không nêu pháp nhân con (N1 tr. 12 ¶66–70: "HBO Latin America Holdings"): đạt. |
| (f) | **Đạt** | Không suy đoán động cơ. **Lưu ý:** N8 tr. 1 có điều kiện quản chế về điều trị nghiện và sức khoẻ tâm thần cùng 4 số cuối SSN. Không dùng, không hiện ảnh trang này. "Beverlywood" có trong tiêu đề DOJ; không hiện hình ảnh hay địa chỉ nhà. |
| Luật 5 | **Đạt** | Không nêu tên nạn nhân, Investor 1–3, F.M./C.M./V.C./J.C. (N6 tr. 9–10), Freeway Entertainment (N1 tr. 11 ¶73), nhà thiết kế nội thất, nhân viên HBO/Netflix, phim. Lưu ý N7 tr. 12 có "Investor 1, located in Illinois" và tên phim: không đọc. |

## 5. Tổng điểm

Tính trên **26 mục bắt buộc** (H1–H6, nhịp 0–14 kể cả 2b/6b/7b/9b, cú treo):

| K | MH | S | KKĐ |
|---|---|---|---|
| **21** | **5** (nhịp 1, 5, 9, 14, cú treo) | **0** | **0** |

Ngoài bảng: Logline VI **MH**, Logline EN **S**; §5(d) dẫn nguồn **S**. Các vế KKĐ: Dkt. 58 (nhịp 13), N9 docket (chưa mở được, 403), L3 "phải đăng ký hoặc được miễn".

## 6. Sửa bắt buộc

1. **Nhịp 9: hạ tầng vế "nhân viên thật".** Thay bằng: *"In his plea agreement, Horwitz admitted the messages he forwarded from 'platform representatives' were fake. Prosecutors later said he used the identities of real HBO and Netflix employees."* Tầng ●T + lời DOJ (N12). Không gán ●. Không đặt cạnh nhịp 11 theo kiểu ngụ ý ông bị kết tội trộm danh tính (Counts 12–13 đã bị bác, N8 tr. 4).
2. **Nhịp 5 và L3: con số 250 và "bạn bè".** Thay bằng: *"At least five major investor groups put money in. Behind them, according to the plea agreement, were more than 250 sub-investors with no direct contract with 1inMM — a number Horwitz reserved the right to dispute. Prosecutors said many investors were personal friends."* Dẫn N7 tr. 12, tr. 14; N12.
3. **Cú treo: viết lại cho đúng nguồn.** *"For more than five years, earlier investors kept getting paid — with newer investors' money. Then, beginning around December 2019, 1inMM started defaulting on all of its outstanding notes."* ●T, dẫn N7 tr. 8, 12. "More than five years" khớp N12.
4. **Nhịp 1:** bỏ "ông là người quản lý duy nhất", hoặc tách thành câu ◐ *"According to the indictment, he was the company's sole manager."* (N6 tr. 1).
5. **Logline EN** (sai sự thật và thiếu 8e). Thay bằng: *"He sold investors a front-row seat to the streaming boom. In his plea agreement, he admitted the deals behind it were fake. HBO and Netflix were not accused of any wrongdoing."*
6. **Logline VI.** Thay bằng: *"…ông sau đó thừa nhận trước toà rằng các hợp đồng đó là giả và tiền của nhà đầu tư mới được dùng để trả nhà đầu tư cũ; tổng cộng ông huy động ít nhất 650 triệu USD và bị tuyên 20 năm tù."* Bỏ "bạn bè", hoặc ghi rõ là lời công tố.
7. **Nhịp 12: tách số.** *"…hoàn trả lợi bất chính 62,85 triệu USD cộng lãi trước phán quyết 11,38 triệu USD (tổng ≈ 74,2 triệu USD), coi như đã thoả mãn bằng lệnh bồi hoàn 230.361.884 USD của vụ hình sự"* (N4 tr. 3). Không dùng §V của N4 ("allegations… true and admitted", chỉ cho mục đích phá sản) để nói ông "admitted" trong vụ SEC.
8. **§5(d): nguồn cho "Ponzi scheme".** Đổi "N7 tr. 12" thành N11/N12. Câu EN phải có chủ thể, ví dụ: *"…what the Justice Department called a $650 million Ponzi scheme."*
9. **L1: sửa cho khớp nguồn và bỏ câu tuyệt đối.** *"A 35 percent return in six months — the kind of note the SEC described in this case — works out to roughly 80 percent a year if you roll it over. Returns that high, promised in advance, are a classic warning sign."* Câu "promised in advance… warning sign" chỉ dùng sau khi mở được N17; nếu chưa mở được thì bỏ. Ghi rõ dải 25–45 % là **trên cả kỳ hạn**.
10. **L3: bỏ suy luận pháp lý.** Thay bằng: *"In this case, more than 250 people had invested through a middle layer and had no contract with 1inMM itself. Before you invest, ask: who exactly is my contract with?"* Bỏ "nên phải đăng ký hoặc được miễn" cho tới khi có nguồn đã mở. Giữ "the notes counted as securities" ở dạng riêng cho vụ này: *"In his plea agreement, the notes were described as securities under federal law"* (N7 tr. 9).
11. **Luật 8e:** thêm câu "HBO and Netflix were not accused of any wrongdoing…" (hoặc bảo đảm câu này có trong cùng đoạn) cho nhịp 2b, 4, 9b. Sửa §5(e) cho khớp thực tế.
12. **Nhịp 11: bổ sung trang:** N7 tr. 4 (cam kết đề nghị bác tội còn lại), N8 tr. 3 (bồi hoàn), N8 tr. 4 (bác tội, Thẩm phán Scarsi).

## 7. Khuyến nghị

- **K1.** NGUON ghi N17 (Investor.gov) "HTTP 200 (UA trình duyệt; UA khai báo bị 403)". Mở nguồn bằng cách đổi sang UA trình duyệt sau khi bị 403 có thể trái luật "không đổi user-agent để vượt" trong CLAUDE.md. Điều phối nên xem lại; người kiểm này **không** mở N17. Cho tới khi có đường chính thức, câu nào dựa vào N17 phải ghi "chưa mở được".
- **K2.** N9 (CourtListener) bị 403 trong lần kiểm này. Trạng thái vụ (luật 4) cần kiểm lại ở MR-3 qua đường được phép.
- **K3.** Nhịp 6: giữ phần giới hạn "for these specified films" ("không ký hợp đồng phân phối nào với nền tảng **cho các phim đó**").
- **K4.** Nhịp 4: đổi "được trả đúng hạn" thành "có thành tích trả lãi lớn đều đặn" (N1 ¶47 "consistent track record"), và ghi nguồn N2/N3 cho vế "nhiều năm" ("for many years", SEC cáo buộc).
- **K5.** Nhịp 9b và D(5): nếu trích ¶77 thì trích đủ cả "(highly doubtful)". Đổi "xin thêm tiền" thành "gợi ý nhà đầu tư góp thêm tiền".
- **K6.** Nhịp 7b: viết "travel by private jet" / "đi máy bay riêng", không viết "máy bay riêng" (dễ hiểu thành sở hữu).
- **K7.** Nếu dùng ảnh trang hồ sơ: không dùng N8 tr. 1 (SSN, điều kiện điều trị) và N8 tr. 3 (tên bên nhận bồi hoàn). Che tên phim và "Investor 1, Illinois" ở N7 tr. 12, N6 tr. 5–8.
- **K8.** Nhịp 10: theo N2, SEC đã "obtained" lệnh phong toả ngày 06/04/2021 (nộp đơn 05/04). Lời phim có thể dùng "obtained an emergency asset freeze".
- **K9.** L2: khi gắn với vụ này, ghi vế "đầu tư thêm, rủ người mới" là "the SEC alleged" (N1 ¶50).
