# Kiểm độc lập vòng 2 — dàn truyện `romance-sunmola` (United States v. Olayinka I. Sunmola, 7th Cir. No. 17-1299; S.D. Ill. 3:13-cr-30272)

> Tác tử kiểm độc lập vòng 2 · 01/11/2026 · Tệp được kiểm: `docs/dan-truyen/romance-sunmola.md` (không sửa). Không commit, không push. Chi 0 USD (không gọi API trả tiền).

## 1. Phạm vi đọc
- **Đã đọc:** `CLAUDE.md`; `docs/HIEN-CHUONG.md` (toàn văn, v2); `docs/dan-truyen/romance-sunmola.md` (toàn văn, §0–§8); `docs/kho-de-tai/romance-sunmola.md` **chỉ §8** (bảng N1–N5).
- **Không đọc:** `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 tệp kho, dàn truyện khác, `docs/dan-truyen/kiem/**` (kể cả kết quả vòng trước), git log/diff.
- §6 (ước chi) không chứa sự việc về vụ → **không chấm**.

**Ký hiệu điểm:** **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được. (Lưu ý: tệp được kiểm dùng "MH" cho tầng *cảnh minh hoạ*; trong bảng dưới, cột "Điểm" là điểm kiểm, tầng minh hoạ ghi là "minh hoạ".)

## 2. Nguồn đã mở

| Mã | Đường mở | Kết quả | Ghi chú |
|---|---|---|---|
| N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` (tệp thật, không phải con trỏ LFS) | SHA-256 `cc362fa04d95dd71c5af59f50a3f2e6ab4b0393a9c65f54754e7ab710959953b` — **khớp** kho §8; `pdftotext -layout`, tách form-feed: 18 trang, số in đầu trang tr. 2–18 trùng số trang PDF (tr. 1 không in số) | Đọc đủ 18 trang |
| N1 | `curl -sS -G https://www.justice.gov/api/v1/press_releases.json --data-urlencode "parameters[title]=Prince Charming"` | HTTP 200, **1 kết quả**; tiêu đề "'Prince Charming' Behind Bars: Nigerian Romance Scammer Nets 27-Year Prison Sentence"; `date` 1486036800 = 02/02/2017 | `body` HTML; đoạn "Once he had successfully beguiled…" bị tách thẻ `<p>` giữa câu ("…wiring" / "him money…") — khớp cách tệp dẫn "đoạn kế" |
| N6 | `curl https://www.ic3.gov/PSA/2019/PSA190805` (mặc định) | HTTP 200; Alert Number I-080519-PSA, August 5, 2019; tiêu đề khớp | |
| N7 | `curl https://www.ic3.gov/` | HTTP 200; "the central hub for reporting cyber-enabled crime. It is run by the FBI" | |
| N8 | `curl https://reportfraud.ftc.gov/` | HTTP 200; trang SPA, `<title>ReportFraud.ftc.gov</title>`, meta "Protect your community by reporting fraud, scams, and bad business practices" | Đủ để xác nhận là cổng báo cáo của FTC |
| N3–N5, FTC consumer, fbi.gov | — | **Không mở lại** (ngoài danh sách nguồn của lệnh) | Chỉ đối chiếu với bảng kho §8 |

Tệp tải về lưu ở `/tmp/claude-0/sunmola-v2/` (ngoài repo); python đọc tệp chạy `-I`. Không có 403/CAPTCHA ở các nguồn đã mở.

## 3. Bảng chấm từng dòng

### 3.1 Đầu tệp và §0

| Mục | Điểm | Bằng chứng (trang + trích ngắn) | Vấn đề / đề xuất |
|---|---|---|---|
| Dòng 6 — ký hiệu tầng ● Sunmola | K | N2 tr. 1 "Three days into trial, Sunmola pleaded guilty to all eight counts… 324 months"; tr. 3 "accepted the guilty pleas without a plea agreement"; tr. 18 "we AFFIRM"; tr. 1 "DECIDED APRIL 16, 2018" | "Ngày thứ ba" = tr. 3 "Trial commenced on February 29, 2016. Three days into trial" + N1 "on March 2, 2016, after two full days of trial" (29/02, 01/03, 02/03) — khớp khi ghép hai nguồn |
| §0 dòng 9 — nhánh ảnh: một câu | K | Quy tắc nội bộ; xem §4 | — |
| §0 dòng 10 — không tổ hợp nhận diện | K | N2 tr. 8 có các ca tuổi + hoàn cảnh (không chép ở đây) | Nhỏ: tr. 8 có tuổi + hoàn cảnh, **không có bang** (bang ở tr. 2). Có thể viết "N2 tr. 8 có tổ hợp tuổi + hoàn cảnh; tr. 2 nêu bang" — không bắt buộc |
| §0 dòng 11 — "ý nghĩ tự sát của nạn nhân (N1, N2)" | **S** (nội bộ) | N1 "Two victims told the court they had seriously contemplated suicide" — có. N2: **không** có câu nào về ý nghĩ của nạn nhân; tr. 2 chỉ có lời đe doạ của bị cáo (không chép) | Dẫn sai N2. Sửa: "(N1; N2 tr. 2 chỉ có câu đe doạ của bị cáo — cũng không dùng)". Không tới người xem nhưng là dẫn nguồn sai |
| §0 dòng 12 — N1 nêu một tên giả | K | N1 đoạn "The U.S. Postal Inspection Service began…" có một tên giả (không chép) | — |

### 3.2 Logline và móc câu

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| Logline VI | K | N2 tr. 2 ("created profiles on dating websites under fictitious names", "targeting middle-aged women in the United States", "ask for money and merchandise… ship electronics"); tr. 10 (soldier/colonel, "work for, or on behalf of, the U.S. government"); tr. 3 (London, all counts); tr. 1, 5 (324 months); tr. 18 | Nguồn: "Sunmola **and his co-conspirators** created profiles" — logline nói một mình Sunmola lập; chấp nhận được ở mức logline |
| Logline EN câu 1 | K | N2 tr. 10 "In some instances… American soldier, stranded in Nigeria on a mission… In other instances… a colonel in the U.S. Army deployed to South Africa" | Khuyến nghị (8e): nếu logline EN dùng ra ngoài (mô tả, pitch), thêm "The U.S. Army had nothing to do with it." — hiện chỉ H3 có |
| Logline EN câu 2 | K | N2 tr. 2 "carried out an international online romance scheme from the Republic of South Africa" | — |
| Logline EN câu 3 | K | N2 tr. 1, 5 "324 months"; N1 "27-year prison term" | — |
| H1 (cảnh) | K | Không sự việc; chữ mờ, không logo | Không dựng tin nhắn đọc được — đạt §1, §5 |
| H2 | K | N2 tr. 10 "pretended to be an American soldier, stranded in Nigeria on a mission… held himself out as a colonel in the U.S. Army deployed to South Africa, telling his victims he needed them to purchase and ship computer equipment to him to help him finish his assignments" | Mô tả vai ở mức khái niệm, không lời thoại → không phải mẫu lời dụ |
| H3 | K | N2 tr. 2 (trích đúng như tệp); tr. 10 "misrepresented… the U.S. military", "his false military status" | Câu 8e có. Có thể thêm tr. 10 "his false military status" vào cột nguồn cho "None of it was true" |
| H4 | K | N1 "Sunmola's purpose was to lead each of his victims to believe that he was her 'Prince Charming'" | Gắn "Prosecutors said" — đúng ◐D; động cơ là lời DOJ, không suy đoán (8f) |
| H5 | K | N2 tr. 1, 5 "324 months"; năm 2017: N2 **tr. 4** "On February 2, 2017, the district court held the second half of the sentencing hearing"; N1 ngày 02/02/2017 "sentenced this morning to serve 324 months" | tr. 1, 5 không ghi năm. Đề xuất thêm "tr. 4" vào cột nguồn |
| H6 | K | N2 tr. 17 nguyên văn "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being" | — |
| Ghi chú dòng 32 | K | N1 "…without laying hands or even eyes…" (không có "someone"); tiêu đề N1 có "Romance Scammer" | — |

### 3.3 Bảng nhịp

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| Nhịp 0 | K | Tổng hợp §1 | — |
| Nhịp 1 | K | N1 "began investigating Sunmola in 2012, when a woman in the Southern District of Illinois complained…"; "merely one of the dozens of fictitious online profiles Sunmola and his confederates concocted" | ◐D có "according to prosecutors". Người khiếu nại: chỉ quận + năm, không tuổi/hoàn cảnh — không nhận diện được |
| Nhịp 2 | K | N2 tr. 2 "Starting in March 2008… middle-aged women… under fictitious names… successful businessmen… often used pictures of men in U.S. military uniforms"; N1 "photographs stolen from the hacked online accounts of real American men"; N1 "from 2007 to 2014" | Tách tầng đúng (●C / ◐D); chọn mốc 2008 của toà đúng |
| Nhịp 3 | K | N1 "showered the women with poetry, cards, flowers, stuffed animals, and chocolates"; "researched facts about the American cities he pretended to be from" | Không dựng thư/thơ — đạt |
| Nhịp 4 | K | N2 tr. 2 "After gaining the women's trust… ask for money and merchandise… false claims of financial distress"; tr. 10 "would be used for work-related purposes, specifically to complete work for, or on behalf of, the U.S. government", "clearly misrepresented… acting on behalf of… the U.S. military", "did not err in applying this enhancement" | Lặp câu 8e ở nhịp 4 — đúng |
| Nhịp 4b | K | N1 "manufacture phony emergencies, each of which required increasingly large amounts of money"; đoạn kế "The women were invariably told to direct their shipments to 'Ilumsa Sunmola,' who was passed off as their lover's driver, or a co-worker, or a hotel manager. In fact, it was Sunmola himself…"; "When the money inevitably ran out, or the women refused to send more, Sunmola would abruptly end the relationship" | Mức khái niệm (cơ chế người nhận trung gian), không thao tác. Không tên dịch vụ chuyển tiền (N2 tr. 14 có) — đạt |
| Nhịp 5 | K | N2 tr. 11–12 "He recruited accomplices, placed the orders for merchandise… received the stolen goods and wire transfers, and directed everyone else on what to tell the victims. The Government also presented evidence suggesting that Sunmola commanded a larger share of the profits"; tr. 12 "we do not find the application of this enhancement clearly erroneous"; tr. 2 "evidence of credit card fraud affecting various businesses"; N1 "The loss incurred by one computer manufacturer alone was over $800,000" | Nhỏ: "gây thiệt hại cho" ≈ "affecting" — câu EN nên giữ "affecting various businesses". Đã loại đúng hai vế thao tác ở tr. 11 (dữ liệu thẻ, chọn cửa hàng) |
| Nhịp 6 | K | N2 tr. 2 "In some instances, Sunmola sexually exploited the victims" (số nhiều → "some of the women"); "threatened to post photos of a third woman" | Câu tới người xem nhẹ hơn nguồn (nguồn còn có hành vi đã thực hiện) — đúng lệnh "mức khái niệm", không sai. Đề xuất thêm "In some instances" vào cột nguồn để đỡ vế số nhiều. Không nối với Count Eight — đúng (tr. 3 chỉ nêu tên tội) |
| Nhịp 7 | K | N1 "The crime forced at least three women to file for bankruptcy. Several more lost their jobs and their homes"; N2 tr. 6 "the PSR, which listed seven victims who suffered substantial financial hardship", "five or more victims"; tr. 7 "did not clearly err"; tr. 4 "two upward departures the Government requested, one for psychological injury to a victim and a second for gratuitous infliction of injury to a victim" | "Không bị kháng cáo" là suy từ danh sách điểm kháng cáo (tr. 2, 5) — đúng nhưng nên viết "không nằm trong các điểm kháng cáo toà phúc thẩm liệt kê (tr. 2, 5)" |
| Nhịp 8 | K | N2 tr. 3 "On November 20, 2013… eight-count indictment with conspiracy… (Count One); mail fraud… (Counts Two through Four); wire fraud… (Counts Five through Seven); and interstate extortion… (Count Eight)"; "On August 9, 2014… arrested Sunmola while he was traveling in London… February 26, 2015"; N1 "as he was about to board a plane from London to Johannesburg" | Dịch: "interstate extortion" nên là "tống tiền xuyên bang" (không phải "liên bang"); EN đã đúng |
| Nhịp 9 | K | N2 tr. 3 "Trial commenced on February 29, 2016. Three days into trial, Sunmola openly pleaded guilty to all counts. The judge asked Sunmola questions to ensure he knowingly and voluntarily entered the pleas… accepted the guilty pleas without a plea agreement"; N1 "March 2, 2016, after two full days of trial" | — |
| Nhịp 10 | K | N2 tr. 3–4 (12/8/2016 "victim impact testimony and expert testimony on the psychological impact"; 02/02/2017 Postal Inspector, "39 additional victims' losses"); tr. 4 sáu mức tăng nặng, "intended loss of $2,054,972.66"; tr. 14 "39 additional victims beyond the 13 listed in the PSR", "around $1.7 million was an underestimate", "actual loss calculation of $1,669,050.98"; tr. 5 "$1,707,260.98… amended… $1,669,050.98" | Tách đúng hai số thiệt hại; "ước thấp" gắn lời điều tra viên — đúng tầng |
| Nhịp 11 | K | N2 tr. 1, 18; tr. 8 "chose the women they developed relationships with, specifically targeting women they believed would be susceptible…", "Many of these women had been divorced, abandoned, widowed, or ignored by the men in their lives", "most of the targeted women were middle-aged rather than elderly" | Chỉ câu khái quát — đạt |
| Nhịp 11b | K | N1 "When Sunmola has completed his 27-year prison term, he will be removed to his native home of Nigeria… Over $200,000 in proceeds from the sale of Sunmola's four properties in South Africa has already been turned over to the District Court and will be proportionally disbursed to the individual identified victims"; N2 tr. 4 "$220,000 liquidated assets" (Government advised the judge) | BOP 2037 khớp kho §8 (N3 không mở lại). Đề xuất câu EN: "Prosecutors said in 2017 that…" vì trục xuất là việc tương lai theo lời DOJ năm 2017 |
| Nhịp 12 | K | Cấu trúc | — |
| Dòng 54 — không lời thoại; N1 có một câu nạn nhân | K | N1 có một câu trích lời nạn nhân viết cho toà (không chép) | — |
| Dòng 55 — đồng phạm không tên | K | N2 không nêu tên đồng phạm | — |

### 3.4 §3 khuôn tập và cú treo

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| Khuôn 1 tập, lý do không chia | K | N2 tr. 3 (nhận tội giữa phiên xử) | — |
| Cú treo câu 1 | K | N2 tr. 3 "On August 9, 2014, authorities arrested Sunmola while he was traveling in London" | — |
| Cú treo câu 2 | K | N2 tr. 3 "Trial commenced on February 29, 2016"; tr. 1 S.D. Ill. | "A year and a half later" là khoảng tính từ hai ngày (≈ 18,7 tháng) — đúng phép tính; khuyến nghị "In February 2016, his trial began in Illinois" để khỏi làm tròn |
| Cú treo câu 3 | K | N2 tr. 3 (nhận tội ngày thứ ba, không phán quyết của bồi thẩm) | Không ám chỉ bị bác — đạt |

### 3.5 §4 bài học, dấu hiệu, nguyên tắc, thẻ tổng kết

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| L1 | K | N2 tr. 11–12 (như nhịp 5) | "Có thể không phải một người" là suy luận của kênh, có căn cứ ("directed everyone else on what to tell the victims") và nói "có thể" |
| L2 | K | N2 tr. 8–9 (như nhịp 11; tr. 8 "seeking companionship through online dating"; tr. 9 "Their prior relationships left these women unusually vulnerable"); N6 "the elderly, women, and those who have lost a spouse are often targeted" | Thân bài đúng. Câu "Cô đơn sau mất mát… đó là thứ kẻ gian tìm" là khung của kênh, có căn cứ (tr. 8–9, N6) — nên giữ đúng nghĩa này khi viết EN, không biến thành "luôn luôn" |
| L3 | **MH** | N2 tr. 4 (departure "for psychological injury to a victim") — khớp. N2 tr. 14: "he saw that Sunmola had attempted to contact many other individuals, but he was **unable to reach all** of these individuals. Thus, he concluded… an underestimate" | "Vì **nhiều người** không liên lạc được" mạnh hơn nguồn: nguồn chỉ nói không liên lạc được **hết**, không nói số nhiều. Sửa: "điều tra viên cho rằng ~1,7 triệu USD là ước thấp, vì Sunmola đã tìm cách liên lạc với nhiều người khác mà ông không liên lạc được hết (N2 tr. 14)". Câu "báo cáo… giúp cơ quan thấy đúng quy mô" — gắn N7 ("It helps us understand the broader threat landscape") hoặc ghi "lời khuyên chung của kênh" |
| D(1) | K | N2 tr. 10; N1 "an engineer working on a large government contract in South Africa"; N6 "claims to be a U.S. service member serving overseas", "Claims to be from the U.S. but is currently living, working, or traveling abroad" | — |
| D(2) | K | N2 tr. 2, 10; N1 "laptop computers, tablets, and cell phones"; N6 "Asks for money, goods, or any similar type of financial assistance" | — |
| D(3) | K | N1 "driver, or a co-worker, or a hotel manager" | — |
| D(4) | K | N1 "phony emergencies… increasingly large amounts", "abruptly end the relationship"; N6 "Reports a sudden personal crisis… Be especially wary if the demands become increasingly aggressive" | Trích N6 có "…" nối hai câu — chấp nhận được |
| D(5) | K | N2 tr. 2 (ảnh quân phục); N1 (ảnh lấy cắp); N6 "Most cyber criminals do not use their own photographs" | Chỉ nói "kiểm xem ảnh có xuất hiện nơi khác", không chép các bước của N6 — đạt |
| P(1) FBI | K | N6 "Never send money to someone you meet online, especially by wire transfer"; vế "hàng… chưa gặp trực tiếp" có ở N6 "Asks for money, goods… especially if you have never met in person" | Khuyến nghị dẫn cả hai câu N6 cho vế "hàng" và "chưa gặp" |
| P(2) kể với người tin cậy | K | Tệp tự ghi "lời khuyên chung của kênh, không gắn nguồn" — không bị gắn nguồn sai | — |
| P(3) kiểm ảnh | K | N6 "A reverse image search can determine if a profile picture is being used elsewhere" | — |
| P(4) nơi báo cáo | K | N7 "central hub for reporting cyber-enabled crime… run by the FBI"; N8 "reporting fraud, scams"; N6 "Report the activity to the Internet Crime Complaint Center" | — |
| Thẻ — mục 1 | K | N2 tr. 11–12 | "can be" — không tuyệt đối |
| Thẻ — mục 2 | **MH** | N2 tr. 8 "specifically targeting women they believed would be susceptible… Many of these women had been divorced, abandoned, widowed…"; "seeking companionship through online dating" | "targets were **picked by** life circumstances: loss, divorce, seeking companionship" biến mô tả ("many… had been") thành **tiêu chí chọn**; "seeking companionship" là lý do toà cho rằng họ dễ tổn thương, không phải tiêu chí chọn. Sửa: "2) In this case, the court said the group chose women it believed would be easy to deceive — many divorced, widowed or abandoned, looking for companionship online." |
| Thẻ — mục 3 | K | N2 tr. 4, 14 | — |
| Thẻ — 5 dấu hiệu | K | như D(1)–D(5) | Dấu hiệu ở dạng chung, không phải lời dụ |
| Thẻ — câu kết | K | N6 "Never send money to someone you meet online"; N7, N8 | — |
| Dòng 76 — thẻ không nhắc nhánh ảnh | K | Kiểm văn bản thẻ: không có | — |

### 3.6 §5 rà luật

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| (a) | K | N2 tr. 1, 3, 5, 18 | — |
| (b) | K | Mọi câu ◐D trong nhịp có "Theo DOJ"/"according to prosecutors"/"Prosecutors said" (H4, nhịp 1, 2, 3, 4b, 5, 7, 8, 11b, D1, D5) | — |
| (c) | K | Không tên trang hẹn hò (N1, N2 tr. 14 có), hãng máy tính (N1 không nêu), dịch vụ chuyển tiền (N2 tr. 14 có) | — |
| (d) | K | N2 tr. 3 tội danh; giọng kể dùng "romance scheme" (N2 tr. 2) | — |
| (e) | K | H3 + nhịp 4 | Không nhất quán nhỏ: §5 ghi "nhịp 4 **nếu xa**", nhịp 4 ghi "**bắt buộc**" → thống nhất "bắt buộc". Logline EN chưa có câu 8e (xem 3.2) |
| (f) | K | "chọn mục tiêu" — N2 tr. 8 (lời toà); động cơ "Prince Charming" — N1 (lời DOJ) | — |
| KBCB | K | Nạn nhân, người khiếu nại, đàn ông bị lấy ảnh, điều tra viên (N2 tr. 4, 14 có tên), chuyên gia (N1 có tên), công tố (N1 có tên) — không dùng tên | — |
| §5 tình dục | K | N2 tr. 2 "middle-aged women"; tr. 8 "middle-aged rather than elderly"; đọc toàn văn N1 + N2: không có chi tiết nạn nhân vị thành niên | — |
| Phép thử "làm theo được ngay?" | K | xem §4 dưới | — |

### 3.7 §7, §8

| Mục | Điểm | Bằng chứng | Vấn đề / đề xuất |
|---|---|---|---|
| §7 N1 | K | HTTP 200, 1 kết quả, ngày 02/02/2017 | — |
| §7 N2 | K | SHA-256 khớp, 18 trang | — |
| §7 N6 | K | I-080519-PSA, 05/8/2019, tiêu đề khớp | — |
| §7 N7, N8 | K | HTTP 200 | — |
| §7 hai dòng "chưa mở được" (FTC consumer, fbi.gov) | KKĐ | Không mở lại (ngoài danh sách nguồn của lệnh) | Không dùng cho câu nào → không ảnh hưởng |
| §8 "887 F.3d 830" | KKĐ | Không có bản reporter trong phạm vi | Tệp đã tự ghi chưa đối chiếu và dùng "No. 17-1299 (7th Cir. Apr. 16, 2018)" — đúng (tr. 1) |
| §8 tội danh dựa N2 tr. 3 | K | N2 tr. 3 | — |
| §8 ảnh trang: chỉ tr. 1 hoặc tr. 18 | K | tr. 18 "we AFFIRM"; tr. 2, 8 đúng là các trang phải tránh | — |

## 4. §5 / nhánh ảnh riêng tư / nhận diện nạn nhân / hướng dẫn làm

- **Nhánh đe doạ phát tán ảnh riêng tư — đếm chỗ:**
  - **Nội dung tới người xem: 1 chỗ** — nhịp 6, câu *"With some of the women, it went further: he threatened to expose private images."* Mức khái niệm, không mô tả ảnh, không dựng cảnh (thẻ chữ tối). Không xuất hiện ở logline, H1–H6, cú treo, L1–L3, D, P, thẻ tổng kết. Nhịp 8 nêu tên tội "interstate extortion" nhưng **không** nối với ảnh — đúng.
  - **Ghi chú quy tắc nội bộ (không tới người xem): 6 chỗ** — §0 dòng 9; cột nguồn/rà nhịp 6; dòng 76; §5 hàng "§5 tình dục"; §6 dòng 105; §8 dòng 123.
  - Không trích lời đe doạ của bị cáo (N2 tr. 2) — đạt.
- **Nạn nhân không nhận diện được:** không tên; không tổ hợp tuổi + hoàn cảnh + bang (N2 tr. 8 không dùng; bang ở tr. 2 không dùng cho nạn nhân); không trích lời nạn nhân (N1 có một câu — không dùng); không số tiền từng người (N1 có một số — không dùng); không ý nghĩ tự sát, không "váy cưới". Người khiếu nại 2012 chỉ có quận + năm — không đủ nhận diện. **Đạt.**
- **Chỉ nạn nhân người lớn:** N2 tr. 2, tr. 8 ("middle-aged"); không có chi tiết vị thành niên trong N1, N2. **Đạt.**
- **Hướng dẫn làm (phép thử §1):** móc câu, cú treo, L1–L3, D1–D5, P, thẻ tổng kết — **không** có trình tự thao tác, không mẫu tin nhắn/thơ/hồ sơ, không tên trang hẹn hò hay dịch vụ chuyển tiền, không cách lấy ảnh/dữ liệu thẻ/chọn cửa hàng (tr. 11 đã loại). H2 và nhịp 4b mô tả vai giả và người nhận trung gian ở mức cơ chế, không lời thoại chép dùng được. D5/P3 chỉ nói "kiểm ảnh có xuất hiện nơi khác", không chép các bước của N6. **Đạt.**

## 5. Tổng điểm

| Điểm | Số dòng |
|---|---|
| K | 68 |
| MH | 2 (L3; thẻ tổng kết mục 2) |
| S | 1 (§0 dòng 11 — dẫn N2 sai, nội bộ) |
| KKĐ | 2 (§7 hai nguồn 403 không mở lại — không dùng; §8 "887 F.3d 830" — tệp tự ghi chưa đối chiếu) |
| **Tổng dòng chấm** | **73** (§6 ước chi không chấm) |

## 6. Danh sách sửa bắt buộc
1. **L3 (MH):** thay "vì nhiều người không liên lạc được" → "vì Sunmola đã tìm cách liên lạc với nhiều người khác mà điều tra viên không liên lạc được hết (N2 tr. 14)"; câu "báo cáo… giúp cơ quan thấy đúng quy mô" gắn N7 hoặc ghi "lời khuyên chung của kênh".
2. **Thẻ tổng kết mục 2 (MH):** thay bằng "In this case, the court said the group chose women it believed would be easy to deceive — many divorced, widowed or abandoned, looking for companionship online." (N2 tr. 8).
3. **§0 dòng 11 (S, nội bộ):** "(N1, N2)" → "(N1; N2 tr. 2 chỉ có câu đe doạ của bị cáo — cũng không dùng)".

**Khuyến nghị (không bắt buộc):** thêm câu 8e vào logline EN nếu dùng ra ngoài; thống nhất §5(e) với nhịp 4 ("bắt buộc"); H5 thêm N2 tr. 4 cho năm 2017; nhịp 5 giữ "affecting" trong EN; nhịp 6 thêm "In some instances" (tr. 2) vào cột nguồn; nhịp 7 viết "không nằm trong các điểm kháng cáo (tr. 2, 5)"; nhịp 8 "tống tiền xuyên bang"; cú treo "In February 2016" thay "A year and a half later"; nhịp 11b EN "Prosecutors said in 2017 that…"; P(1) dẫn thêm câu N6 "especially if you have never met in person"; §0 dòng 10 ghi rõ tr. 8 có tuổi + hoàn cảnh, bang ở tr. 2.
