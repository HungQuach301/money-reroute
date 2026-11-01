# Kiểm độc lập vòng 2 — Dàn truyện `irs-callcenter-patel`

> Đối tượng: `docs/dan-truyen/irs-callcenter-patel.md` (121 dòng, bản trong cây làm việc ngày 01/11/2026). Người kiểm: tác tử kiểm độc lập vòng 2. Chi 0 USD; không gọi API trả tiền; không sửa tệp được kiểm; không commit.
> Thang chấm: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được.

## 1. Phạm vi đọc

| Loại | Nội dung |
|---|---|
| Đã đọc | `CLAUDE.md`; `docs/HIEN-CHUONG.md` (toàn văn); tệp được kiểm (toàn văn); `docs/kho-de-tai/irs-callcenter-patel.md` **chỉ §8** (bảng N1–N8) |
| Không đọc (theo lệnh) | `reports/**`; `docs/kho-de-tai/kiem/**`; §1–§7 của tệp kho; dàn truyện khác; `docs/dan-truyen/kiem/**` (gồm kết quả vòng 1); git log/diff |
| Không mở được | Không có. (N6 BOP, N7 ân xá, N8 kháng cáo không thuộc phạm vi kiểm lần này — tệp được kiểm không dùng chúng làm trụ cho câu lời) |

## 2. Nguồn đã mở

| Mã | Đường mở | Kết quả | Ghi chú |
|---|---|---|---|
| N1 | Tệp repo `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` (tệp thật, không phải con trỏ LFS) | SHA-256 `04fb7cb3c4cfda5b444a66c9415878635346dfb1f6c3333e5acf41867a7b2bdf` — **khớp** kho §8 | Render `pdftoppm -r 80 -gray` các trang 1, 3, 4, 5, 6, 7; đọc bằng ảnh. Đầu trang: "Case 4:16-cr-00385 *SEALED* Document 6 Filed in TXSD on 10/19/16 Page x of 81"; tr. 1 có dấu "Unsealed 10/27/16", "HOUSTON DIVISION" |
| N2 | API DOJ, tiêu đề "Dozens of Individuals Indicted…" | HTTP 200; 2 bản ghi: bản USAO-SDTX (không số) và **16-1257** (OPA) | Chấm theo bản 16-1257. Đ.1–13 và đ.5 (lời HSI) trùng nội dung ở cả hai bản; đ.14 trở đi lệch số giữa hai bản |
| N3 | API DOJ, "24 Defendants Sentenced…" | HTTP 200; 1 bản ghi **18-961** (ngày 20/07/2018) | Danh sách `<li>` sau đ.12 (18 người) và sau đ.13 (3 người) đã đọc |
| N4 | API DOJ, "Indian National Pleads Guilty to Owning, Funding" | HTTP 200; **20-19** (09/01/2020) | |
| N5 | API DOJ, "Owner and Operator of India-Based Call Centers Sentenced" | HTTP 200; 3 bản ghi, chọn **20-1294** (30/11/2020) | |
| N9 | `curl` mặc định, irs.gov FS-2017-7 | HTTP 200 | Trang có dòng "News items may not be updated after their release. Please verify the date before relying on the language." |
| N10 | `curl` mặc định, reportfraud.ftc.gov | HTTP 200 | Trang dựng bằng JavaScript; đọc được `<title>` "ReportFraud.ftc.gov" và meta description "Protect your community by reporting fraud, scams, and bad business practices" |
| N11 | `curl` mặc định, tigta.gov/reportcrime-misconduct | HTTP 200 | Mục "IRS Scams and Fraud" có lựa chọn "Someone is impersonating an IRS or Treasury employee." |

Tệp tải về nằm ở `/tmp/claude-0/kiem-v2-patel/` (ngoài repo); python đọc tệp chạy với `-I`. Không request nào chứa thông tin cá nhân.

## 3. Bảng chấm từng dòng

| # | Mục | Điểm | Bằng chứng (trang/đoạn, trích ngắn) | Vấn đề + đề xuất sửa |
|---|---|---|---|---|
| 1 | Logline VI | **MH** | N4 đ.5 "the call centers would immediately turn to a network of 'runners'… to liquidate and launder"; N4 đ.1 "between 2013 and 2016"; N4 đ.6; N1 tr. 1 "HOUSTON DIVISION"; N5 đ.1 | "Ngay lập tức" trong nguồn gắn với việc call center **quay sang** mạng runner, không phải việc tiền đã **rút và rửa xong** ngay. Sửa: "…call center lập tức quay sang một mạng 'runner' ở Mỹ để rút và rửa tiền". Phần còn lại K |
| 2 | Logline EN | **MH** | Nội dung khớp N4 đ.5–6, N5 đ.1 | Câu 3 "the man who admitted operating and funding…" là ●T nhưng **không có chủ thể** — trái quy ước dòng 6 của chính tệp ("lời luôn có chủ thể"). Sửa: "…and the man who, according to the Justice Department, admitted operating and funding several of those call centers…" |
| 3 | H1 | K | Cảnh MH, không sự việc | — |
| 4 | H2 | **MH** | N4 đ.5 "impersonated officials from the IRS and… USCIS… threatened with arrest, imprisonment, fines or deportation if they did not pay" | Nội dung khớp vế "admissions", nhưng câu gắn ●T nói phẳng, không chủ thể. Sửa một trong hai: (a) thêm "According to the Justice Department, …"; hoặc (b) đổi tầng thành ●N + ●T và dẫn thêm N3 đ.14 ("According to various admissions made in connection with the defendants' guilty pleas… threatened with arrest, imprisonment, fines or deportation") và N5 đ.8 ("According to admissions in his plea agreement") |
| 5 | H3 | K | N1 tr. 3 ¶1(a) "India-based call centers impersonated U.S. Internal Revenue Service (IRS) officers", ¶1(b) "impersonated U.S. Citizen and Immigration Services (USCIS) officers"; N4 đ.5 | Đạt 8e |
| 6 | H4 | K | N4 đ.5 "employees from call centers in Ahmedabad, India"; đ.6 "Patel admitted to operating and funding several India-based call centers from which the fraud schemes were perpetrated" | Có chủ thể DOJ. Ghi chú: đ.6 nói "India-based"; gắn "of them" (Ahmedabad) đọc được từ đ.5 + đ.6 — chấp nhận |
| 7 | H5 | **MH** | N5 đ.1 "sentenced today to 20 years in prison… in the Southern District of Texas"; đ.2 "Judge David Hittner" | N5 đ.1–2 **không** có chữ "Houston". "Houston" chỉ có ở N1 tr. 1 ("HOUSTON DIVISION") và N3 đ.1 (phiên 2018 "took place in Houston, Texas, before the Honorable David Hittner"); nơi diễn ra phiên tuyên án 2020 không nguồn nào nêu. Sửa: "a federal judge in Texas" (theo N5 đ.1), hoặc giữ "Houston" nhưng dẫn thêm N1 tr. 1 và hiểu là toà ("the federal court in Houston"), không phải nơi phiên họp |
| 8 | H6 | K | N4 đ.5 "immediately turn to a network of 'runners'… to liquidate" | Câu hỏi dẫn; "cash" là cách nói của "liquidate" — chấp nhận ở câu hỏi |
| 9 | Ghi chú móc câu | K | N5 đ.4 "this con artist" (U.S. Attorney Patrick) | Đúng là không dùng |
| 10 | Nhịp 0 | K | — | Tham chiếu §1 |
| 11 | Nhịp 1 | K | N2 đ.11 "According to the indictment, one of the call centers extorted $12,300 from an 85-year-old victim… after threatening her with arrest if she did not pay fictitious tax violations" | Tầng ◐ đúng; bỏ thành phố đúng |
| 12 | Nhịp 1b | K | N2 đ.12 "The indictment also alleges… extorted $136,000… called multiple times over a period of 20 days" | Bỏ "276 cards" đúng |
| 13 | Nhịp 2 | K | N1 tr. 1 "Filed in TXSD on 10/19/16", "Unsealed 10/27/16"; N2 đ.8 "returned by a grand jury… on Oct. 19, 2016"; N2 đ.1 "61 individuals and entities… 20 individuals were arrested today… 32 individuals and five call centers in India… tens of thousands… hundreds of millions"; ngày thông cáo 27/10/2016 | Tầng TT + ◐ đúng |
| 14 | Nhịp 3 | K | N1 tr. 3 ¶1(a) "would be arrested and fined if they did not pay their alleged back taxes immediately"; ¶1(b) "deported unless they paid a fine immediately"; tr. 3–4 ¶1(c) "upfront 'worthiness fee' to demonstrate an ability to repay"; tr. 4 ¶1(d) "upfront IRS tax or processing fee. The victims received nothing in return" | — |
| 15 | Nhịp 3b | K | N4 đ.6 câu 2–3 "Patel corresponded… The scripts included… Canada Revenue Agency (CRA) impersonation, Australian Tax Office (ATO) impersonation, payday loan fraud, U.S. Government grant fraud, and debt collection fraud" | Đúng: câu này nằm **sau** câu "In his plea, Patel admitted…", không thuộc vế admitted → ◐ đúng. Có câu 8e |
| 16 | Nhịp 4 | K | N1 tr. 4–6 ¶2(a) Runner, (b) Domestic Manager, (c) Call Center Operator, (d) Caller, (e) Payment Processor, (f) Data Broker ("purchase names and PII"), (g) Hawaladar | Đủ 7 vai, đúng trang |
| 17 | Nhịp 4b | K | N1 tr. 6–7 ¶3 "five major conglomerates of call centers, all located in Ahmedabad… often acted together… sharing call scripts and lists of potential victims, processing payments for each other"; N1 tr. 1 [2] d.b.a. trùng thương hiệu | Đúng |
| 18 | Nhịp 5 | **MH** | N4 đ.5 "instructed how to provide payment, including by purchasing general purpose reloadable (GPR) cards or wiring money. Upon payment, the call centers would immediately turn to a network of 'runners'"; N2 đ.9 "often registered using misappropriated personal identifying information"; N2 đ.10 "accounts belonging to U.S.-based individuals… not aware of the illicit nature"; N1 tr. 6 ¶2(g) "made available internationally without actually moving it" | Vế "call center **chuyển cho** mạng runner" ngụ ý call center chuyển tiền sang runner — nguồn chỉ nói call center "turn to" (quay sang nhờ) runner; theo N3 đ.14 (●N) runner mua thẻ còn người ở Ấn Độ nạp tiền. Sửa: "ngay khi có tiền, call center lập tức quay sang mạng 'runner' ở Mỹ để rút và rửa". Các vế ◐ (thẻ, hawala) K |
| 19 | Nhịp 6 | **MH** | N4 đ.2 "also known as Hitesh Hinglaj, 43, of Ahmedabad"; đ.6 "In his plea, Patel admitted to operating and funding several India-based call centers… including the call center HGLOBAL"; N1 tr. 7 bảng HGLOBAL "HITESH PATEL (a.k.a. HITESH HINGLAJ) — Call Center Operator — India"; N4 đ.7 "monthly income and expense reports to his personal email" | Lời K. Vấn đề ở **hình**: ô chữ "HGLOBAL — operated and funded (admitted)" gắn HGLOBAL với lừa đảo nhưng không nhãn ◐, trong khi HGLOBAL là **bị cáo [1]** trong cáo trạng (N1 tr. 1) và chưa có nguồn nào cho thấy đã kết luận. Sửa: thêm dòng "HGLOBAL was also charged in the indictment; presumed innocent (as of Nov. 2020)" + nhãn ◐ mỗi khi tên HGLOBAL xuất hiện (N1 tr. 1; N5 đ.12) |
| 20 | Nhịp 6b | K | N4 đ.8 "A co-defendant described Patel as 'the top person in India and the boss for whom most of the other defendants worked'" | Có chủ thể; bỏ lời "bribe" đúng 8f |
| 21 | Nhịp 7 | K | N3 đ.1 "Twenty-one… sentenced this week to terms of imprisonment up to 20 years. Three other conspirators were sentenced earlier this year"; đ.9 Hardik Patel "co-owner and manager of an India-based call center"; đ.11 "Twenty-two… jointly and severally liable for restitution of $8,970,396"; đ.13 + `<li>`: Houston (S.D. Tex.), Atlanta (N.D. Ga.), Phoenix (D. Ariz.); N4 đ.11 "24 domestic defendants" | 21 + 1 (Houston, 23/3) = 22 Houston; khớp. Khuyến nghị: dẫn thêm N3 đ.8, đ.10 cho vế "quản lý runner" (đ.9 chỉ cho vế đồng sở hữu call center) |
| 22 | Nhịp 7b | K | N3 đ.15 "32 India-based conspirators and five India-based call centers… have yet to be arraigned… presumed innocent" | — |
| 23 | Nhịp 8 | K | N4 đ.9 "extradited from Singapore in April 2019… apprehended Patel at the request of the United States pursuant to a provisional arrest warrant in September 2018, after Patel flew there from India" | — |
| 24 | Nhịp 9 | **MH** | N4 đ.2 (hai tội); đ.10 "accepted the plea today"; đ.8 "Patel admitted that a reasonably foreseeable loss of more than $25 million but less than $65 million was attributable to him, **based on the government's evidence against him**" | Bỏ vế giới hạn "based on the government's evidence against him" làm lời thừa nhận chắc hơn nguồn. Sửa: giữ nguyên vế này ("…attributable to him, based on the government's evidence"). Phần tội danh và ghi chú "không nói convicted of money laundering" K |
| 25 | Nhịp 10 | K | N5 đ.1 "20 years in prison followed by three years of supervised release"; đ.2 "restitution of $8, 970,396 to identified victims"; ngày thông cáo 30/11/2020 | — |
| 26 | Nhịp 10b | K | N5 đ.12 "Charges remain pending for other India-based defendants. They are presumed innocent…" | Gắn mốc đúng |
| 27 | Nhịp 11 | K | §4 | Xem các dòng §4 |
| 28 | Ghi chú dưới bảng nhịp (dòng 53–56) | K | N3 đ.14 (trình tự thẻ), N1 tr. 4–6 ¶2(a),(e),(f); N2 đ.11–12 có thành phố; kho §8 N6/N8 khớp mô tả | — |
| 29 | §3 khuôn tập | K | N4 đ.9 | — |
| 30 | Cú treo giữa tập | **MH** | Câu 1: N3 đ.1, đ.13 (24 người, ngày 20/07/2018); N4 đ.11 "domestic". Câu 2: danh sách N3 không có Hitesh; N3 đ.15. Câu 3: N4 đ.9 | Câu 2 "the man who would later admit to operating and funding call centers in Ahmedabad" là ●T **không chủ thể** (như dòng 2). Ngoài ra đ.6 nói "India-based call centers"; "in Ahmedabad" lấy từ đ.5. Sửa: "…the man who, according to the Justice Department, would later admit to operating and funding several India-based call centers…" |
| 31 | L1 | K | N1 tr. 4–6 ¶2 (Data Broker, Caller, Payment Processor, Runner, Hawaladar); N4 đ.6 (scripts) | Lời phải giữ chủ thể "the indictment described"; câu "không phải một kẻ đơn độc" nên gắn "in this case" |
| 32 | L2 | K | N4 đ.5 "immediately"; N3 đ.14 "as quickly as possible", "Apple iTunes or other gift cards that victims purchased"; N9 "prepaid debit card, gift card or wire transfer" | Phần "vì sao" là giải thích của kênh (HIEN-CHUONG §1 cho phép), đã tách khỏi chữ hồ sơ. Không nêu tên thương hiệu thẻ — đúng |
| 33 | L3 | K | N9: "The IRS initiates most contacts through regular mail"; "taxpayers will generally first receive several letters"; "does not: Call to demand immediate payment using a specific payment method such as a prepaid debit card, gift card or wire transfer"; "Demand that you pay taxes without the opportunity to question or appeal"; "Threaten to bring in local police, immigration officers…"; "make payments to the 'United States Treasury'"; N2 đ.5 (16-1257) Edge: "U.S. government agencies do not make these types of calls" | Khuyến nghị: N9 là fact sheet 04/2017 có cảnh báo "verify the date"; trên hình ghi "IRS fact sheet, 2017" và kiểm lại trang IRS hiện hành trước khi chốt lời |
| 34 | D1 | K | N4 đ.5; N9 "threaten to arrest or deport" | — |
| 35 | D2 | K | N1 tr. 3 ¶1(a)–(b) "immediately" (◐); N9 "demand immediate payment", "without the opportunity to question or appeal" | Ghi nhãn ◐ cho vế N1 như D4, D5 cho đồng bộ |
| 36 | D3 | K | N4 đ.5 "GPR cards or wiring money"; N3 đ.14; N9 | — |
| 37 | D4 | K | N2 đ.12 "called multiple times over a period of 20 days" (◐) | Là khái quát của kênh từ một ví dụ ◐; N9 không nêu dấu hiệu này. Lời nên nói "in one case described in the indictment" |
| 38 | D5 | K | N1 tr. 3–4 ¶1(c)–(d) | — |
| 39 | P — cúp máy, tự tra số chính thức | K | Nguyên tắc chung (HIEN-CHUONG §1); gần với N2 đ.5 "contact law enforcement… before you make a payment" | Không phải câu sự việc |
| 40 | P — cơ quan thật không đổi "án" lấy thẻ quà tặng | K | N9 (IRS); N2 đ.5 (HSI: "U.S. government agencies do not make these types of calls") | — |
| 41 | P — người lớn tuổi và người nhập cư là mục tiêu | **MH** | Không dẫn nguồn. Nguồn gần nhất: N3 đ.3 lời Bộ trưởng Tư pháp Sessions "bilk older Americans, legal immigrants and many others"; N2 đ.11 (nạn nhân 85 tuổi, ◐); N1 tr. 3 ¶1(b) (doạ trục xuất, ◐) | Khái quát không nguồn. Sửa: "In this case, the Justice Department said the ring targeted older Americans and legal immigrants, among others (N3 đ.3)" — có chủ thể, không tuyệt đối |
| 42 | P — báo cáo TIGTA, FTC | K | N11 "Someone is impersonating an IRS or Treasury employee"; N9 "Contact the Treasury Inspector General for Tax Administration to report a phone scam"; N10 meta "reporting fraud, scams, and bad business practices" | Không nêu số điện thoại trên hình là đúng |
| 43 | Thẻ tổng kết EN | **MH** | Ý 1: N1 tr. 4–6, N4 đ.5 — K. Ý 3: N9 "generally first… letters", "does not… gift card", "Threaten to… have you arrested" — K | Ý 2 "money **the scammers** could move out fast": (a) gán nhãn "scammers" cho nhóm gồm cả bị cáo ở Ấn Độ chưa kết luận — trái luật 8d và trái chính §5(d) của tệp; (b) "move out" gợi chuyển ra nước ngoài, nguồn chỉ nói "liquidate and launder… as quickly as possible". Sửa: "2) Prepaid cards, gift cards and wires = money that could be cashed out and moved fast." |
| 44 | §5 (a) | K | N4 đ.10; N5 đ.1–2 | — |
| 45 | §5 (b) | **MH** | N1 tr. 1 "[1] HGLOBAL" là bị cáo; N5 đ.12 | "Nếu nói HGLOBAL cũng là bị cáo thì kèm…" quá lỏng: mọi lần nêu HGLOBAL đều ngụ ý HGLOBAL tham gia lừa đảo. Sửa: **luôn** kèm "also charged; presumed innocent (as of Nov. 2020)" + ◐ khi nêu HGLOBAL (lời và hình, nhịp 4b, 6) |
| 46 | §5 (c) | K | N1 tr. 1, tr. 7 | — |
| 47 | §5 (d) | **S** | Thẻ tổng kết (dòng 76) có "the scammers" | Kết quả rà khai "Không 'scammer…'" nhưng tệp có. Sửa thẻ tổng kết (dòng 43) rồi giữ kết quả rà |
| 48 | §5 (e) | K | N1 tr. 1 (d.b.a.); N3 đ.14 (Apple iTunes); N4 đ.6 (WhatsApp) — đều không nêu trong lời | — |
| 49 | §5 (f) | K | N4 đ.8 (lời "bribe" bỏ) | — |
| 50 | KBCB (luật 5) | K | N2 đ.10–12 | — |
| 51 | §5 tình dục | K | — | Không áp dụng |
| 52 | Phép thử "làm theo được ngay?" | K | Xem §4 dưới | — |
| 53 | §7 bảng nguồn mới | K | SHA-256 N1 khớp; N9 "FS-2017-7, April 19, 2017"; N10, N11 HTTP 200 (lần mở này) | Không mở lại consumer.ftc.gov (không dùng) |

## 4. Hướng dẫn làm / lời gọi dựng lại / nhận diện nạn nhân

- **Hướng dẫn làm (phép thử HIEN-CHUONG §1): Đạt.** Móc câu, cú treo, bài học, dấu hiệu và thẻ tổng kết chỉ nêu tên vai + chức năng, loại thủ đoạn và dấu hiệu phòng vệ. Không có trình tự đăng ký/nạp/rút thẻ, cách vận hành hawala, nguồn mua dữ liệu, số điện thoại hay URL của kẻ gian. Nhịp 5 vẽ hawala ở mức "bù trừ giữa hai người môi giới" — mức khái niệm, không đủ để làm theo. Cảnh báo dòng 55 (không chép N3 đ.14, N1 ¶2(a),(e),(f)) cần giữ ở phiên kịch bản.
- **Lời gọi dựng lại: Đạt.** Không có câu thoại của "người gọi", không chữ kịch bản trên màn hình, H1 chỉ "Unknown". H2 và logline EN tóm tắt lời doạ ở ngôi thứ ba / gián tiếp ("said you'd be arrested if you didn't pay") — không thành kịch bản chép dùng được. Nhịp 3 nêu bốn loại mồi (thuế, di trú, vay, trợ cấp) ở mức nhãn, không lời mẫu. Lưu ý phiên kịch bản: không mở rộng nhịp 3 thành câu thoại mẫu ("worthiness fee"…).
- **Nhận diện nạn nhân: Đạt.** Đã bỏ thành phố (San Diego, Hayward ở N2 đ.11–12), không tên, không ngày; chỉ tuổi 85 + số tiền theo cáo trạng. Không dùng ảnh chụp thông cáo N2. Nạn nhân không nhận diện được từ nội dung tập. Người bị đánh cắp PII và người nhận hawala: KBCB, không tên.

## 5. Tổng điểm

| K | MH | S | KKĐ | Tổng dòng |
|---|---|---|---|---|
| 41 | 11 | 1 | 0 | 53 |

## 6. Danh sách sửa bắt buộc

1. **Thẻ tổng kết (dòng 76) + §5(d):** bỏ "the scammers" (luật 8d) và "move out"; đề xuất "Prepaid cards, gift cards and wires = money that could be cashed out and moved fast."
2. **HGLOBAL (nhịp 6 hình, nhịp 4b, §5(b)):** HGLOBAL là bị cáo [1] (N1 tr. 1), chưa có kết luận → **mỗi lần** nêu tên đều kèm ◐ "also charged; presumed innocent (as of Nov. 2020)" (N5 đ.12).
3. **Chủ thể cho câu ●T:** logline EN câu 3, H2, cú treo câu 2 thêm "according to the Justice Department" (hoặc H2 đổi tầng ●N + dẫn N3 đ.14, N5 đ.8). Cú treo đổi "call centers in Ahmedabad" → "several India-based call centers" cho khớp N4 đ.6.
4. **Nhịp 9:** giữ vế "based on the government's evidence against him" khi nêu khoảng thiệt hại 25–65 triệu USD (N4 đ.8).
5. **H5:** "Houston" không có trong N5 đ.1–2 → đổi "a federal judge in Texas" hoặc dẫn N1 tr. 1 và nói "the federal court in Houston".
6. **P (người lớn tuổi, người nhập cư):** gắn nguồn và chủ thể — "the Justice Department said the ring targeted older Americans and legal immigrants, among others" (N3 đ.3).
7. **Nhịp 5 và logline VI:** "chuyển cho mạng runner" / "rút và rửa ngay lập tức" → "lập tức quay sang mạng runner ở Mỹ để rút và rửa" (N4 đ.5).

**Khuyến nghị (không bắt buộc):** nhịp 7 dẫn thêm N3 đ.8, đ.10; D2 ghi ◐ cho vế N1; D4 nói "in one case described in the indictment"; L3 ghi năm fact sheet (2017) và kiểm lại trang IRS hiện hành trước khi chốt lời; có thể dẫn song song N5 đ.8–9 ("admissions in his plea agreement") cho các câu ●T.
