# Kiểm độc lập vòng 1 — dàn truyện `romance-sunmola` (U.S. v. Olayinka I. Sunmola, 7th Cir. No. 17-1299)

> Tác tử kiểm độc lập · 01/11/2026 · đối tượng: `docs/dan-truyen/romance-sunmola.md` (bản trong cây làm việc, không sửa). Chi 0 USD; không gọi API trả tiền; không PACER; không commit.
> Thang điểm: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được.

## 1. Phạm vi đọc

| Loại | Nội dung |
|---|---|
| Đã đọc | `CLAUDE.md`; `docs/HIEN-CHUONG.md` (toàn văn); `docs/dan-truyen/romance-sunmola.md` (toàn văn); `docs/kho-de-tai/romance-sunmola.md` **chỉ §8** (bảng nguồn N1–N5) |
| Không đọc (theo lệnh) | `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 tệp kho, các dàn truyện khác, `docs/dan-truyen/kiem/**` (chỉ liệt kê thư mục để biết chỗ ghi), git log/diff |
| Không mở được | Không có (mọi nguồn được giao đều HTTP 200). Không kiểm lại N3 (BOP) — tệp không dùng N3 làm nguồn cho câu lời (nhịp 11b chỉ ghi "kiểm lại ngày chốt lời"). Không kiểm "887 F.3d 830" (§8 tệp tự ghi là việc chờ) |

## 2. Nguồn đã mở

| Mã | Tệp / URL | Trang/phần | HTTP | SHA-256 / ghi chú |
|---|---|---|---|---|
| N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` (có sẵn trong repo, không cần `git lfs pull`) | 18 trang; `pdftotext -layout`, tách theo form-feed; số in đầu trang trùng thứ tự PDF | — | `cc362fa04d95dd71c5af59f50a3f2e6ab4b0393a9c65f54754e7ab710959953b` — **khớp** kho §8 |
| N1 | `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=Prince Charming` | `count: 1`; tiêu đề "'Prince Charming' Behind Bars: Nigerian Romance Scammer Nets 27-Year Prison Sentence"; `date` 1486036800 = 02/02/2017; URL khớp kho §8; trường `body` đọc toàn văn | 200 | JSON tải về (thư mục tạm, không lưu repo) `51add97e…f75ba` — chỉ để vết, JSON API có thể đổi |
| N6 | https://www.ic3.gov/PSA/2019/PSA190805 | Toàn văn PSA I-080519-PSA, ngày August 5, 2019 | 200 | curl mặc định |
| N7 | https://www.ic3.gov/ | Trang chủ IC3 ("File A Complaint") | 200 | curl mặc định |
| N8 | https://reportfraud.ftc.gov/ | Trang dựng bằng JS; HTML tĩnh chỉ có tiêu đề "ReportFraud.ftc.gov" + meta "reporting fraud, scams, and bad business practices" | 200 | curl mặc định — đủ để xác nhận đây là cổng báo cáo của FTC |

Tệp tải về ở `/tmp/claude-0/kiem-sunmola-v1/` (ngoài repo); đọc bằng `python3 -I`.

## 3. Bảng chấm từng dòng

H1 là mô tả cảnh dựng, không có sự việc → **không chấm** (đã kiểm phần hình: chữ chat mờ, không logo, có nhãn — đạt).

| # | Mục | Điểm | Bằng chứng (nguồn đúng trang, trích ngắn) | Vấn đề + đề xuất sửa |
|---|---|---|---|---|
| 1 | Logline VI | K | N2 tr. 2 (Nam Phi, "fictitious names", "middle-aged women"), tr. 10 (lính/đại tá), tr. 3 (bắt ở London; "Three days into trial… pleaded guilty to all counts"), tr. 5 (324 tháng), tr. 18 ("we AFFIRM") | — |
| 2 | Logline EN câu 1 "He told the women he was an American officer on a mission overseas." | **MH** | N2 tr. 10: "**In some instances**, Sunmola pretended to be an American soldier, stranded in Nigeria on a mission… **In other instances**… a colonel in the U.S. Army deployed to South Africa" | "the women" = mọi nạn nhân; toà chỉ nói "some/other instances" (tr. 2 còn nói hồ sơ giới thiệu "successful businessmen"). Ghép "officer" (đại tá) với "on a mission" (vai lính). Sửa: *"He told some of the women he was an American soldier or Army officer serving overseas."* |
| 3 | Logline EN câu 2 | K | N2 tr. 2: "carried out an international online romance scheme from the Republic of South Africa" | — |
| 4 | Logline EN câu 3 | K | N2 tr. 5: "324 months' imprisonment"; N1 "27-Year Prison Sentence" | — |
| 5 | H2 | K | N2 tr. 10 (trích như tệp, khớp từng chữ) | Ghi chú lời: "Sometimes he was an American soldier" ở giọng kể nên viết "Sometimes he **posed as**…" để không nghe như sự thật (câu H3 có gỡ, nhưng tách câu thì rủi ro) |
| 6 | H3 (●C + 8e) | K | N2 tr. 2 (trích khớp); tr. 10: "Sunmola clearly **misrepresented** to his victims that he was acting on behalf of… the U.S. military" | Câu 8e có mặt (đạt luật 8e). "had nothing to do with it" là câu gỡ do hiến chương đòi, có cơ sở ở tr. 10 (toà xác định là mạo xưng); khuyên viết sát nguồn hơn: *"…he was not acting for the U.S. military — the court found that was a misrepresentation."* |
| 7 | H4 (◐D) | K | N1: "Sunmola's purpose was to lead each of his victims to believe that he was her 'Prince Charming'" | Đúng tầng: lời DOJ, có chủ thể "Prosecutors said" |
| 8 | H5 (●) | K | N2 tr. 5 (324 tháng); tr. 4 (phiên tuyên án thứ hai 02/02/2017); N1 ngày 02/02/2017, "sentenced this morning to serve 324 months" | — |
| 9 | H6 (lời thẩm phán qua toà phúc thẩm) | K | N2 tr. 17: "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being" — khớp từng chữ | — |
| 10 | Ghi chú dưới H6 (N1 khác chữ) | K | N1: "…without laying hands or even eyes on another human being" (không có "someone") | Nhận xét đúng; dùng bản N2 là đúng |
| 11 | Nhịp 0 | K | Tham chiếu §1 | — |
| 12 | Nhịp 1 (◐D) | K | N1: "The U.S. Postal Inspection Service began investigating Sunmola in 2012, when a woman in the Southern District of Illinois complained…"; "…merely one of the dozens of fictitious online profiles Sunmola and his confederates concocted on dating websites" | Đúng tầng ◐D. Tệp đã bỏ tên giả và tên trang hẹn hò (N1 có cả hai) — đạt |
| 13 | Nhịp 2 | K | N2 tr. 2: "Starting in March 2008…"; "created profiles… under fictitious names and led women to believe they were successful businessmen"; "often used pictures of men in U.S. military uniforms"; N1: "photographs stolen from the hacked online accounts of real American men"; N1 "from 2007 to 2014" | Đúng tầng (●C / vế ảnh ◐D). Lưu ý lời: chủ ngữ "lập hồ sơ" ở tr. 2 là "Sunmola **and his co-conspirators**" — giữ cả hai |
| 14 | Nhịp 3 (◐D) | K | N1: "showered the women with poetry, cards, flowers, stuffed animals, and chocolates"; "researched facts about the American cities he pretended to be from" | — |
| 15 | Nhịp 4 (●C) | K | N2 tr. 2: "After gaining the women's trust, Sunmola and his co-conspirators would ask for money and merchandise… under the false claims of financial distress"; tr. 10: "would be used for work-related purposes, specifically to complete work for, or on behalf of, the U.S. government"; tr. 10 kết luận "the district court did not err in applying this enhancement" | Cột "Rà luật 8" ghi câu 8e lần hai "nếu đoạn xa H3": nhịp 4 bắt đầu 4:30, H3 ở ~0:15 → **đã xa**; nên đổi thành **bắt buộc** |
| 16 | Nhịp 4b (◐D) | K | N1: "Once he had successfully beguiled his target, Sunmola began to manufacture phony emergencies, each of which required increasingly large amounts of money"; đoạn kế (HTML API tách ở "wiring / him money"): "…direct their shipments to 'Ilumsa Sunmola,' who was passed off as their lover's driver, or a co-worker, or a hotel manager. In fact, it was Sunmola himself…"; "When the money inevitably ran out, or the women refused to send more, Sunmola would abruptly end the relationship." | Neo "đoạn kế" đúng với HTML hiện tại. N2 tr. 14 đúng là có tên dịch vụ chuyển tiền — tệp không dùng, đạt |
| 17 | Nhịp 5 — cầm đầu, tuyển, đặt hàng, nhận hàng/tiền, chỉ đạo lời nói | K | N2 tr. 11–12: "He recruited accomplices, placed the orders for merchandise… received the stolen goods and wire transfers, and directed everyone else on what to tell the victims"; tr. 12: "we do not find the application of this enhancement clearly erroneous" | — |
| 18 | Nhịp 5 — "có bằng chứng ông lấy phần lớn hơn" | **MH** | N2 tr. 12: "The Government also presented evidence **suggesting** that Sunmola commanded a larger share of the profits" | Toà chỉ ghi công tố đưa bằng chứng **cho thấy có thể**; không phải toà kết luận. Sửa: "công tố đưa ra bằng chứng cho thấy ông có thể hưởng phần lớn hơn" (EN: *"prosecutors presented evidence suggesting he took a larger share"*) |
| 19 | Nhịp 5 — "theo toà, còn có gian lận thẻ tín dụng **nhắm vào** doanh nghiệp" | **MH** | N2 tr. 2: "During the investigation, authorities also discovered **evidence of** credit card fraud **affecting** various businesses" (tr. 11 có chi tiết thao tác — tệp đúng là không dùng) | Bỏ mất "evidence of"; "affecting" thành "nhắm vào"; và cáo trạng (tr. 3) không có tội danh riêng về thẻ. Sửa: "theo toà, nhà điều tra còn tìm thấy bằng chứng gian lận thẻ tín dụng gây thiệt hại cho nhiều doanh nghiệp" |
| 20 | Nhịp 5 — hãng máy tính > 800.000 USD (◐D) | K | N1: "The loss incurred by one computer manufacturer alone was over $800,000." | Đúng tầng; N1 không nêu tên hãng — đạt 8c |
| 21 | Nhịp 6 — câu duy nhất | K | N2 tr. 2: câu mở đoạn "In some instances, Sunmola sexually exploited the victims" + câu về đe doạ đăng ảnh của một phụ nữ (không chép chi tiết); N1 (◐D) xác nhận nhánh này với "at least two women" | "some of the women" có cơ sở ("In some instances"; tr. 2 nêu nhiều hơn một người). Câu là mức khái niệm, **nhẹ hơn** nguồn (không nói ảnh đã bị đăng) — không phải MH. Ghi chú "N2 không nói Count Eight dựa trên hành vi nào": **đúng** (tr. 3 chỉ ghi "interstate extortion, in violation of 18 U.S.C. § 875(d) (Count Eight)") |
| 22 | Nhịp 7 — phá sản, mất việc, mất nhà (◐D) | K | N1: "The crime forced at least three women to file for bankruptcy. **Several more** lost their jobs and their homes" | Câu EN phải dùng "several more", không "many" |
| 23 | Nhịp 7 — tăng nặng ≥ 5 nạn nhân, PSR 7 người (●C) | K | N2 tr. 6: "substantial financial hardship to five or more victims"; "the PSR, which listed seven victims"; tr. 7: "the district court did not clearly err in applying the 'substantial financial hardship' enhancement" | — |
| 24 | Nhịp 7 — "**hai lần** tăng vượt khung **vì tổn hại tâm lý**" | **S** | N2 tr. 4: "two upward departures… **one for psychological injury to a victim and a second for gratuitous infliction of injury to a victim**" | Lần thứ hai là "cố ý gây tổn hại không cần thiết", không phải tổn hại tâm lý. Thêm: hai lần vượt khung **không bị kháng cáo** (tr. 5 liệt kê điểm kháng cáo), nên dấu ngoặc "(được phúc thẩm giữ nguyên)" chỉ được áp cho mức tăng nặng khó khăn tài chính. Sửa: "…và (theo phần Background của toà phúc thẩm) toà sơ thẩm chấp nhận hai đề nghị tăng vượt khung của công tố: một vì tổn hại tâm lý cho nạn nhân, một vì cố ý gây tổn hại không cần thiết" — tầng ●C (mô tả), không ghi "giữ nguyên" |
| 25 | Nhịp 8 (TT; vế máy bay ◐D) | K | N2 tr. 3: "On November 20, 2013, a grand jury sitting in the Southern District of Illinois charged…" (Count One conspiracy; Two–Four mail fraud; Five–Seven wire fraud; Eight interstate extortion); "On August 9, 2014… while he was traveling in London… February 26, 2015"; N1: "as he was about to board a plane from London to Johannesburg" | Dịch "tống tiền liên bang" → lời EN dùng đúng "interstate extortion" |
| 26 | Cú treo câu 1 | K | N2 tr. 3: "On August 9, 2014, authorities arrested Sunmola while he was traveling in London" | — |
| 27 | Cú treo câu 2 | K | N2 tr. 3: "Trial commenced on February 29, 2016"; tr. 1 S.D. Ill. — 08/2014 → 02/2016 ≈ 18,7 tháng ≈ "a year and a half" | — |
| 28 | Cú treo câu 3 "It would not make it to a verdict." | K | N2 tr. 3: "Three days into trial, Sunmola openly pleaded guilty to all counts" | Không ám chỉ vụ bị bác; được giải ngay ở nhịp 9 — đạt |
| 29 | Nhịp 9 (●) | K | N2 tr. 3: "…openly pleaded guilty to all counts. The judge asked Sunmola questions to ensure he knowingly and voluntarily entered the pleas… accepted the guilty pleas without a plea agreement"; tr. 1 "Three days into trial"; N1 "on March 2, 2016, after two full days of trial" (29/2–2/3/2016 nhất quán) | — |
| 30 | Nhịp 10 — hai giai đoạn, 13 + 39, "ước thấp" | K | N2 tr. 3–4: "two stages. On August 12, 2016… victim impact testimony and expert testimony on the psychological impact"; "On February 2, 2017… case agent… testified"; tr. 14: "39 additional victims beyond the 13 listed in the PSR"; "he concluded the total calculated loss of around $1.7 million was an underestimate" | Gán "ước thấp" cho điều tra viên — đúng tầng. Không nêu tên điều tra viên (tr. 4, 14 có tên) — đạt |
| 31 | Nhịp 10 — các mức tăng nặng, 2.054.972,66 USD | K | N2 tr. 4: "four-level leadership… two-level… acting on behalf of a government agency… four-level substantial financial hardship… two-level vulnerable victim… 16-level enhancement for an intended loss of $2,054,972.66… two-level… outside of the United States" | Lưu ý: tr. 14–15 toà phúc thẩm lại mô tả mức 16 bậc theo **thiệt hại thực tế** $1,669,050.98. Khi viết lời, nếu nêu số 2.054.972,66 thì gắn rõ "intended loss" theo tr. 4, hoặc không nêu số này để tránh mâu thuẫn trên hình |
| 32 | Nhịp 10 — 324 tháng, bồi hoàn 1.707.260,98 → 1.669.050,98 | K | N2 tr. 5: "324 months' imprisonment and ordered restitution in the amount of $1,707,260.98… later amended the judgment to $1,669,050.98" | — |
| 33 | Nhịp 11 (●C) | K | N2 tr. 1 "DECIDED APRIL 16, 2018"; tr. 18 "we AFFIRM"; tr. 8: "chose the women… specifically targeting women they believed would be susceptible to their deceitful tactics. Many of these women had been divorced, abandoned, widowed, or ignored by the men in their lives"; "most of the targeted women were middle-aged rather than elderly" | Chỉ dùng câu khái quát — đạt; các ca cụ thể cùng trang không dùng — đạt |
| 34 | Nhịp 11b — trục xuất, > 200.000 USD từ 4 bất động sản (◐D) | K | N1: "When Sunmola has completed his 27-year prison term, he will be removed to his native home of Nigeria"; "Over $200,000 in proceeds from the sale of Sunmola's four properties in South Africa has already been turned over to the District Court and will be proportionally disbursed to the individual identified victims" | — |
| 35 | Nhịp 11b — "số 220.000 ●C" | **MH** (tầng) | N2 tr. 4: "**The Government advised the judge** that the clerk of the court had possession of $220,000 liquidated assets"; tr. 15–16 tranh chấp về việc đã trừ khoản này hay chưa, toà nói "We fail to find any discussion in the record…" | Đây là lời công tố báo với thẩm phán, toà chỉ ghi lại — không phải sự việc toà xác định. Sửa: gắn "lời công tố được toà ghi lại" (như cách tệp làm với "ước thấp" ở nhịp 10); EN: *"the government told the judge the court clerk held about $220,000 in liquidated assets."* Hoặc chỉ dùng số ◐D của N1 |
| 36 | Nhịp 12 | K | Tham chiếu §4 | — |
| 37 | L1 | **MH** | N2 tr. 11–12 (tuyển đồng phạm, đặt hàng, nhận hàng/tiền, "directed everyone else on what to tell the victims") | (a) Khái quát thành luật chung "Lừa tình quy mô lớn **là** một tổ chức" từ một vụ; (b) "chia việc" và "nhiều người theo **cùng một kịch bản**" không có trong nguồn (suy ra). Sửa: "**Trong vụ này**, toà mô tả một tổ chức: người cầm đầu tuyển người, nhận tiền và hàng, và chỉ đạo người khác nói gì với nạn nhân — nên 'người yêu' trên màn hình có thể không chỉ là một người." |
| 38 | L2 | **MH** (nhẹ) | N2 tr. 8: "Many of these women **had been** divorced, abandoned, widowed, or ignored…"; "most… middle-aged rather than elderly" | Chữ "**vừa** trải qua" mạnh hơn nguồn (câu khái quát không có "recently"; chữ "recent/recently" chỉ ở các ca cụ thể cùng trang — chính là tổ hợp nhận diện bị cấm). Sửa: bỏ "vừa"; câu khái quát "Kẻ gian chọn người theo hoàn cảnh" nên dẫn thêm N6 ("the elderly, women, and those who have lost a spouse are often targeted") để không khái quát từ một vụ |
| 39 | L3 | K | N2 tr. 4 (một lần vượt khung vì "psychological injury to a victim"); tr. 14 ("unable to reach all of these individuals… an underestimate") | Ghi rõ "toà sơ thẩm" thay "toà"; vế "báo cáo giúp cơ quan thấy đúng quy mô" là lời khuyên của kênh, không gắn nguồn — chấp nhận |
| 40 | D1 | **MH** | N2 tr. 10 (lính/đại tá ở nước ngoài); N6: "claims to be a U.S. service member serving overseas" | (a) "**Không gặp được**" không có trong N1/N2/N6 (N6 chỉ có "especially if you have never met in person" ở dấu hiệu xin tiền); (b) "kỹ sư hợp đồng chính phủ" là từ N1 ("an engineer working on a large government contract in South Africa") nhưng ô không dẫn N1 và nhịp H2/4 không có vai này. Sửa: "**Nói đang làm nhiệm vụ / làm việc ở nước ngoài**" (N2 tr. 10; N6), nếu giữ "kỹ sư" thì dẫn N1 ◐D |
| 41 | D2 | K | N2 tr. 2 ("money and merchandise… electronics"), tr. 10 ("computer equipment"); N6 "Asks for money, goods, or any similar type of financial assistance" | "điện thoại" chỉ có ở N1 ("cell phones") — bổ sung N1 vào ô nguồn |
| 42 | D3 (◐D) | K | N1 ("driver, or a co-worker, or a hotel manager") | — |
| 43 | D4 | K | N1 ("phony emergencies… increasingly large amounts"; "abruptly end the relationship"); N6: "Reports a sudden personal crisis and pressures you to provide financial assistance. Be especially wary if the demands become increasingly aggressive." | — |
| 44 | D5 | **MH** | N2 tr. 2 ("pictures of men in U.S. military uniforms"); N1 (ảnh lấy cắp); N6 "Most cyber criminals do not use their own photographs" | "Ảnh '**quá chuẩn**'" không có ở nguồn nào — nguồn nói ảnh là của **người khác**. Sửa: "Ảnh hồ sơ có thể là của người khác (vụ này: ảnh quân phục lấy cắp của đàn ông thật) — tìm ngược ảnh" |
| 45 | P — "Never send money…" | K | N6: "Never send money to someone you meet online, especially by wire transfer." | "hay hàng" lấy từ dấu hiệu N6 ("Asks for money, goods… especially if you have never met in person") — chấp nhận |
| 46 | P — "kể với một người tin cậy trước khi gửi" | **KKĐ** | Không có trong N6/N7/N8 đã mở; trang FTC consumer (có thể có ý này) HTTP 403 theo §7 tệp | Hoặc bỏ, hoặc ghi rõ đây là lời khuyên chung của kênh (không gắn FBI/FTC) |
| 47 | P — tìm ngược ảnh hồ sơ | K | N6: "A reverse image search can determine if a profile picture is being used elsewhere on the internet" | — |
| 48 | P — nơi báo cáo IC3, FTC | K | N7 trang chủ IC3 ("File A Complaint"); N6 "Report the activity to the Internet Crime Complaint Center"; N8 tiêu đề "ReportFraud.ftc.gov" | — |
| 49 | Thẻ tổng kết 1) "A large romance scheme is an organization, not one lonely stranger." | **MH** | Như dòng 37 | Khái quát thành luật chung. Sửa: *"A romance scheme can be an organization, not one lonely stranger."* |
| 50 | Thẻ 2) "Scammers pick targets by life circumstances: loss, divorce, loneliness." | K | N2 tr. 8 (chọn mục tiêu; ly hôn, goá, bị bỏ rơi; "seeking companionship"); N6 ("those who have lost a spouse are often targeted") | Chữ "Scammers" là danh từ chung, không gắn Sunmola — không phạm 8d |
| 51 | Thẻ 3) "The real damage is bigger than the dollar figure." | K | N2 tr. 4, 14 | — |
| 52 | Thẻ — Red flags | **MH** | Như dòng 40, 44 | "can't meet because of a 'mission' overseas" và "a profile photo that's too perfect" mạnh hơn nguồn. Sửa: *"claims to be on a 'mission' overseas · … · a profile photo that may belong to someone else"*; ba mục còn lại K |
| 53 | Thẻ — "Never send money… Report it." | K | N6, N7, N8 | — |
| 54 | Ký hiệu tầng (đầu tệp): nhận tội 8 tội ngày thứ ba, không thoả thuận, 324 tháng, giữ nguyên 16/04/2018 | K | N2 tr. 1, 3, 5, 18 | — |
| 55 | §0 — ý nghĩ tự sát (N1, N2), váy cưới (N1) | K | N1 ("Two victims told the court they had seriously contemplated suicide"; "A few had even purchased wedding dresses"); N2 tr. 2 (trong câu trích lời bị cáo) | Quyết định không dùng — đúng §5 |
| 56 | §0 — N1 nêu một tên giả | K | N1 có một tên giả trong đoạn về khiếu nại 2012 (không chép) | — |
| 57 | §5 (a) Trung tâm ● | K | N2 tr. 1, 3, 5, 18; tên đệm "Ilumsa" từ N1 | — |
| 58 | §5 dòng "§5 tình dục" — nạn nhân người lớn, không dấu hiệu vị thành niên | K | Như mục 4 dưới đây | — |
| 59 | §7 bảng nguồn mới (N1, N2, N6–N8) | K | Đã mở lại như §2 trên: N1 1 kết quả; SHA N2 khớp; N6 tiêu đề, số I-080519-PSA, ngày 05/8/2019 khớp; N7, N8 HTTP 200 | — |

## 4. §5 / nhánh ảnh riêng tư / nhận diện nạn nhân / hướng dẫn làm

**Nhánh đe doạ phát tán ảnh riêng tư — đếm số chỗ nhắc trong tệp.**
- **Nội dung tới người xem (lời, hình, thẻ): 1 chỗ** — nhịp 6 (dòng 45), câu *"With some of the women, it went further: he threatened to expose private images."* — mức khái niệm, không mô tả ảnh, không dựng cảnh, chỉ thẻ chữ tối. Không xuất hiện ở logline, móc câu, cú treo, bài học, dấu hiệu D1–D5, nguyên tắc P, thẻ tổng kết. **Đạt.**
- **Ghi chú quy tắc nội bộ (không phát lên hình/lời): 5 chỗ** — dòng 9 (§0), dòng 76 (thẻ tổng kết không nhắc), dòng 89 (§5 rà), dòng 105 (§6 "nhịp 6 chỉ thẻ chữ"), dòng 123 (§8 không dùng ảnh trang tr. 2); cộng ghi chú trong ngoặc ở chính ô nhịp 6. Cách tính: các chỗ này là chỉ dẫn cho người soạn, không phải câu nói ra, nên không tính vào "một câu"; chúng chỉ nhắc *rằng có* nhánh này, không chép chi tiết. Ô nguồn nhịp 6 có trích ngắn một cụm của N2 tr. 2 về đe doạ đăng ảnh — chấp nhận ở tài liệu nội bộ, không mô tả hành vi.
- **Liên quan gián tiếp:** tên tội danh "interstate extortion / tống tiền liên bang" ở nhịp 8 và §5(d). Đây là tên tội trong cáo trạng (N2 tr. 3), không mô tả nhánh ảnh; tệp đã chặn việc nối Count Eight với nhánh ảnh (đúng, vì N2 không nói Count Eight dựa trên hành vi nào). Chấp nhận.

**Nhận diện nạn nhân.** Không tên; không trích lời nạn nhân (N1 có một câu — tệp không dùng); không số tiền từng người; H3 đã bỏ phần "specifically in Georgia and Illinois" của N2 tr. 2; nhịp 11 và L2 chỉ dùng câu khái quát tr. 8, không dùng các ca cụ thể (tuổi + hoàn cảnh) cùng trang. Rủi ro còn lại, thấp: (a) nhịp 1 "một phụ nữ ở Southern District of Illinois khiếu nại năm 2012" — chỉ có khu tư pháp + năm, không tuổi/hoàn cảnh; giữ được, nhưng **không** ghép người này với bất kỳ chi tiết nào khác (số tiền, tuổi, nhánh ảnh — N1 cho biết nhánh ảnh liên quan phụ nữ ở Illinois); (b) chữ "vừa" ở L2 gần với các ca cụ thể tr. 8 — bỏ (dòng 38).

**Chỉ nạn nhân người lớn.** N2: tr. 2 "middle-aged women"; tr. 8 "most of the targeted women were middle-aged rather than elderly"; các tuổi nêu ở tr. 8 đều là người lớn. Tìm trong N2 và N1 các từ minor/child/juvenile/teen/daughter/girl/school: **không có** (N2 tr. 8 có "47 to 71 years old" nhưng thuộc vụ khác — *Iriri* — được dẫn làm tiền lệ). Không có dấu hiệu vị thành niên. **Đạt.**

**Hướng dẫn làm (phép thử HIEN-CHUONG §1).**
- Móc câu H2 nêu hai vai mạo xưng (lính kẹt ở Nigeria; đại tá ở Nam Phi cần thiết bị máy tính) ở mức khái niệm, trùng các cảnh báo công khai của FBI (N6). Không có lời dụ, không tin nhắn. Đạt — nhưng ở phiên kịch bản **không** mở rộng thành lời thoại/câu chuyện mẫu.
- Nhịp 3, 4b, 5: không mẫu thơ/thư/tin nhắn; không tên dịch vụ chuyển tiền; không cách mua dữ liệu thẻ, cách chọn cửa hàng nhận hàng (tr. 11 có — tệp đúng là bỏ). Mưu "người nhận hàng là tài xế/đồng nghiệp/quản lý khách sạn" là khái niệm để nhận diện, không làm theo được ngay. Đạt.
- Cú treo, L1–L3, D1–D5, P, thẻ tổng kết: đều là dấu hiệu/hiểu biết, không thao tác. Không có trang web, số điện thoại, tên giả, URL của kẻ gian. Đạt.
- H1: chữ trên màn hình mờ không đọc được — đạt.

## 5. Tổng điểm

| K | MH | S | KKĐ | Tổng |
|---|---|---|---|---|
| 47 | 10 | 1 | 1 | 59 (không chấm H1 — cảnh dựng không có sự việc) |

MH: dòng 2, 18, 19, 35, 37, 38, 40, 44, 49, 52. S: dòng 24. KKĐ: dòng 46.

## 6. Danh sách sửa bắt buộc

1. **(S) Nhịp 7** — sửa "hai lần tăng vượt khung vì tổn hại tâm lý" → "hai lần vượt khung: một vì tổn hại tâm lý cho nạn nhân, một vì cố ý gây tổn hại không cần thiết" (N2 tr. 4); bỏ "(được phúc thẩm giữ nguyên)" khỏi phần vượt khung (không bị kháng cáo, tr. 5).
2. **(MH) Logline EN câu 1** — "He told **some of** the women he was an American soldier or Army officer serving overseas."
3. **(MH) Nhịp 5** — "có bằng chứng ông lấy phần lớn hơn" → "công tố đưa bằng chứng cho thấy ông có thể hưởng phần lớn hơn" (tr. 12 "evidence suggesting").
4. **(MH) Nhịp 5** — gian lận thẻ: "nhà điều tra tìm thấy **bằng chứng** gian lận thẻ tín dụng **gây thiệt hại cho** nhiều doanh nghiệp" (tr. 2).
5. **(MH, tầng) Nhịp 11b** — 220.000 USD là "lời công tố báo với thẩm phán, toà ghi lại" (tr. 4), không phải ●C sự việc toà xác định.
6. **(MH) L1 + thẻ tổng kết mục 1** — bỏ khái quát tuyệt đối ("is an organization" → "can be"; "trong vụ này"); bỏ "chia việc", "cùng một kịch bản".
7. **(MH) L2** — bỏ "vừa"; dẫn thêm N6 cho câu khái quát.
8. **(MH) D1 + thẻ red flags** — "không gặp được / can't meet" → "nói đang làm nhiệm vụ ở nước ngoài / claims to be on a mission overseas"; nếu giữ "kỹ sư hợp đồng chính phủ" thì dẫn N1 ◐D.
9. **(MH) D5 + thẻ red flags** — "quá chuẩn / too perfect" → "có thể là ảnh của người khác / may belong to someone else".
10. **(KKĐ) P** — "kể với một người tin cậy" không có nguồn đã mở: bỏ hoặc ghi rõ là lời khuyên chung của kênh, không gắn FBI/FTC.

Khuyến nghị (không bắt buộc): D2 thêm N1 cho "điện thoại"; nhịp 7 câu EN dùng "several more"; nhịp 4 đổi câu 8e lần hai thành bắt buộc; H2 dùng "posed as"; nhịp 10 nếu nêu 2.054.972,66 USD thì ghi rõ "intended loss" (tr. 4) vì tr. 14–15 mô tả mức 16 bậc theo thiệt hại thực tế 1.669.050,98 USD.
