# KIỂM LỜI ĐỘC LẬP (K-lời) — Tập 3 `tap03-romance-sunmola` — Vòng 1

- **Thời điểm chấm:** 2026-11-01 23:25–23:28 UTC (02/11/2026 sáng giờ Hà Nội).
- **Đối tượng:** `docs/tap03-romance-sunmola/loi.json` (bản "MR-K23 nháp G1", 79 câu S001–S079). Không sửa loi.json, không commit.
- **Căn cứ:** `docs/HIEN-CHUONG.md` (§1, §3 luật 1–8, §4, §5), `docs/tap03-romance-sunmola/NGUON.md`, trường `quy_uoc` của loi.json. Không đọc dàn truyện, kho đề tài, báo cáo (chấm độc lập).
- **Cách làm:** thư mục tạm riêng (`mktemp -d`), curl mặc định (không đổi user-agent, không gửi thông tin cá nhân), python chạy `-I`. Không gọi API trả tiền.

## Nguồn đã mở thực sự

| Mã | Nguồn | Cách mở | Kết quả |
|---|---|---|---|
| N1 | `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=Prince Charming` | curl mặc định, `-G --data-urlencode`, 23:25:35 UTC | HTTP 200, 10 069 byte, 1 kết quả (tiêu đề "Prince Charming" Behind Bars…, URL usao-sdil khớp NGUON.md). SHA-256 phản hồi `51add97e…bf75ba` (khác tệp repo do siêu dữ liệu API), **nội dung `body` trùng từng dòng** với `ho-so/romance-sunmola/doj-api-sdil-2017-02-02.json` (SHA tệp repo `09ef97f8…6f9680` khớp NGUON.md) |
| N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` | `sha256sum` (= `cc362fa0…59953b`, khớp NGUON.md); `pdftotext -layout`, đọc đủ 18 trang; trang xác định theo số in đầu trang ("2 No. 17-1299"…) | đọc được toàn văn |
| N3 | `https://www.bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&nameFirst=olayinka&nameLast=sunmola` | curl mặc định, 23:25:51 UTC | HTTP 200, 397 byte, 1 bản ghi: SUNMOLA OLAYINKA ILUMSA, #11507-025, FCI Oakdale I, `projRelDate` 09/20/2037, `actRelDate` trống, tuổi 43 (khớp "33" năm 2017 ở N1). SHA `733fcbb3…5df4` (khác NGUON.md vì trường `FormToken` thay đổi; dữ liệu tù nhân trùng) |
| N6 | `https://www.ic3.gov/PSA/2019/PSA190805` | curl mặc định, 23:25:52 UTC | HTTP 200, 10 493 byte, PSA I-080519-PSA, 05/08/2019 |
| N7 | `https://www.ic3.gov/` | curl mặc định | HTTP 200, 53 005 byte ("central hub for reporting cyber-enabled crime. It is run by the FBI"; "File A Complaint") |
| N8 | `https://reportfraud.ftc.gov/` | curl mặc định | HTTP 200, 5 398 byte, `<title>ReportFraud.ftc.gov` (trang khung JS; SHA `874400…387c` khớp NGUON.md) |

**Chưa mở được / không mở:** N4, N5 (không dùng trong lời → không mở lại). Cáo trạng, judgment, docket 3:13-cr-30272 của S.D. Ill. — chưa mở được (không thuộc lệnh; lời không dựa vào). consumer.ftc.gov, fbi.gov "Romance Scams" — không mở (lời không dùng).

## Bảng chấm 79 câu

Ký hiệu nguồn: N2 tr. n = trang in của opinion; N1 = thông cáo DOJ 02/02/2017 (dẫn bằng chữ đầu câu).

| id | Kết luận | Tầng đúng? | Làm theo được ngay? | Trích nguyên văn từ nguồn đã mở | Đề xuất sửa |
|---|---|---|---|---|---|
| S001 | KHÔNG CẦN NGUỒN | đúng (MH, không nêu sự việc mới về người thật) | Không | — | Nhớ nhãn ILLUSTRATIVE/DRAMATIZATION trên hình (§4) |
| S002 | KHỚP | đúng (●C, toà mô tả "The record indicates…") | Không | N2 tr. 10: "In some instances, Sunmola pretended to be an American soldier, stranded in Nigeria on a mission and in need of help." | — |
| S003 | KHỚP | đúng (●C) | Không | N2 tr. 10: "Sunmola held himself out as a colonel in the U.S. Army deployed to South Africa, … ship computer equipment to him to help him finish his assignments." | — |
| S004 | KHỚP | đúng (KBCB cho vế quân đội; vế "Neither story was true" là sự việc ●C có nền N2 tr. 10) | Không | N2 tr. 10: "pretended…"; "Sunmola clearly misrepresented to his victims that he was acting on behalf of … the U.S. military." | (tuỳ chọn) tách vế "Neither story was true" thành câu ●C riêng để mỗi câu một tầng (luật 1) |
| S005 | KHỚP | đúng (●C) | Không | N2 tr. 2: "Starting in March 2008, Sunmola carried out an international online romance scheme from the Republic of South Africa, targeting middle-aged women in the United States" | — (đã bỏ đúng tên bang) |
| S006 | KHỚP | đúng (◐, "Prosecutors said") | Không | N1 ("Sunmola's purpose was to lead each of his victims to believe that he was her "Prince Charming,"…") | — |
| S007 | KHỚP | đúng (● bản án) | Không | N2 tr. 1: "sentenced Sunmola to 324 months in jail"; tr. 4–5: phiên tuyên án thứ hai "On February 2, 2017"; N1: "sentenced this morning to serve 324 months". 324/12 = 27 | (tuỳ chọn) thêm "N2 tr. 4" vào nguồn cho năm 2017 để năm không chỉ dựa N1 |
| S008 | KHỚP | chấp nhận (● ); chính xác hơn là ●C vì là lời thẩm phán do toà phúc thẩm trích | Không | N2 tr. 17: "describing it as "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being."" — thẻ chữ trùng nguyên văn | (tuỳ chọn) đổi nhãn ●C |
| S009 | KHÔNG CẦN NGUỒN | đúng (CHUNG) | Không | — | — |
| S010 | KHỚP | đúng (◐) | Không | N1 ("The U.S. Postal Inspection Service began investigating Sunmola in 2012, when a woman in the Southern District of Illinois complained that she had been conned by a man masquerading online as…") | — (đã bỏ tên giả; "after" ≈ "when", không đổi nghĩa) |
| S011 | KHỚP | đúng (◐) | Không | N1 ("The investigation soon revealed that "Dyess" was merely one of the dozens of fictitious online profiles Sunmola and his confederates concocted on dating websites…") | — (đã bỏ tên giả, tên trang) |
| S012 | KHỚP | đúng (◐; "hundreds" chỉ có ở DOJ, đã gắn "Prosecutors said") | Không | N1 ("Evidence presented in court showed that Sunmola was the ringleader of a criminal organization operating in South Africa that targeted hundreds of women across the United States…") | (tuỳ chọn) bỏ "the evidence presented in court showed" để người nghe không hiểu "hundreds" là kết luận của toà (toà chỉ nêu 13 + 39 nạn nhân, N2 tr. 14) |
| S013 | KHỚP | đúng (●C) | Không | N2 tr. 2: "Starting in March 2008 … Sunmola and his co-conspirators created profiles on dating websites under fictitious names" | — (mốc 3/2008 theo toà, đúng) |
| S014 | KHỚP | đúng (●C) | Không | N2 tr. 2: "led women to believe they were successful businessmen. Sunmola often used pictures of men in U.S. military uniforms as part of his online profile." | — (câu không liên quan S017 cùng đoạn P02) |
| S015 | KHỚP | đúng (◐; "Separately" giữ tách khỏi ảnh quân phục của toà) | Không | N1 ("…he used photographs stolen from the hacked online accounts of real American men…") | — |
| S016 | KHỚP | đúng (KBCB, luật 5) | Không | N1 và N2: không nêu tên người đàn ông bị lấy ảnh (đã đọc toàn văn) | — |
| S017 | KHỚP | đúng (KBCB, thẻ chữ, luật 8e) | Không | N2 tr. 10: "misrepresented … the U.S. military" | — |
| S018 | KHỚP | đúng (◐) | Không | N1 ("He also showered the women with poetry, cards, flowers, stuffed animals, and chocolates.") | — |
| S019 | KHỚP | đúng (◐) | Không | N1 ("…researched facts about the American cities he pretended to be from.") | — |
| S020 | KHỚP | đúng (●C) | Không | N2 tr. 2: "After gaining the women's trust, Sunmola and his co-conspirators would ask for money and merchandise." | — |
| S021 | KHỚP | đúng (●C) | Không | N2 tr. 2: "These women would ship electronics and make electronic fund transfers under the false claims of financial distress." | — |
| S022 | KHỚP | đúng (●C) | Không | N2 tr. 10: "Sunmola led the victims to believe the money or equipment they sent overseas would be used … on behalf of, the U.S. government"; "Sunmola clearly misrepresented to his victims that he was acting on behalf of … the U.S. military." | — |
| S023 | KHỚP | đúng (KBCB) | Không | N2 tr. 10 (như S022) | — |
| S024 | KHỚP | đúng (◐) | Không | N1 ("…shipping him laptop computers, tablets, and cell phones – equipment he told them he needed to complete his government mission.") | — |
| S025 | KHỚP | đúng (◐) | Không (khái niệm người nhận trung gian, không địa chỉ, không cách thức) | N1 ("The women were invariably told to direct their shipments to "Ilumsa Sunmola," who was passed off as their lover's driver, or a co-worker, or a hotel manager.") | — ("Ilumsa Sunmola" là tên đệm + họ thật, không phải tên giả của hồ sơ hẹn hò) |
| S026 | KHỚP | đúng (◐) | Không | N1 ("In fact, it was Sunmola himself who was slowly bleeding them dry.") | — |
| S027 | KHỚP | đúng (◐) | Không | N1 ("Once he had successfully beguiled his target, Sunmola began to manufacture phony emergencies, each of which required increasingly large amounts of money…"; "When the money inevitably ran out, or the women refused to send more, Sunmola would abruptly end the relationship.") | — |
| S028 | KHÔNG CẦN NGUỒN | đúng (CHUNG, chuyển đoạn; vế "The court described something bigger" được S029 đỡ) | Không | — | — |
| S029 | KHỚP | đúng (●C, toà giữ nguyên tăng nặng) | Không (đã bỏ đúng phần đặt hàng/cửa hàng/dữ liệu thẻ ở tr. 11–12) | N2 tr. 11–12: "He recruited accomplices, … received the stolen goods and wire transfers, and directed everyone else on what to tell the victims."; "we do not find the application of this enhancement clearly erroneous." | — |
| S030 | KHỚP | đúng (●C, giữ đúng chữ "suggesting" và chủ thể "the government") | Không | N2 tr. 12: "The Government also presented evidence suggesting that Sunmola commanded a larger share of the profits." | — |
| S031 | KHỚP | đúng (●C) | Không | N2 tr. 2: "During the investigation, authorities also discovered evidence of credit card fraud affecting various businesses." | — |
| S032 | KHỚP | đúng (◐) | Không | N1 ("The loss incurred by one computer manufacturer alone was over $800,000.") | — (không nêu tên hãng) |
| S033 | KHỚP | đúng (●C; câu khái niệm duy nhất của nhánh ảnh riêng tư, thẻ chữ, `doc: false`) | Không | N2 tr. 2: "In some instances, Sunmola sexually exploited the victims. … and threatened to post photos of a third woman." | — ("private images" là cách gọi của kênh cho "photos" trong đoạn bóc lột tình dục ở tr. 2; nói nhẹ hơn hồ sơ, không mạnh hơn). Không có câu nào khác khớp mẫu `dung_mot` (đã quét lời + chữ) |
| S034 | KHỚP | đúng (◐) | Không | N1 ("The crime forced at least three women to file for bankruptcy. Several more lost their jobs and their homes…") | — |
| S035 | KHỚP | đúng (●C) | Không | N2 tr. 4: "a four-level substantial financial hardship enhancement"; tr. 6: "five or more victims"; "the PSR, which listed seven victims who suffered substantial financial hardship"; tr. 7: "the district court did not clearly err" | — |
| S036 | KHỚP | đúng (●C, toà phúc thẩm mô tả) | Không | N2 tr. 4: "The judge also granted two upward departures the Government requested, one for psychological injury to a victim and a second for gratuitous infliction of injury to a victim." | — |
| S037 | KHỚP | chấp nhận (CHUNG, diễn giải S036; "the court" = toà tuyên án) | Không | N2 tr. 4 (như S036) | — |
| S038 | KHỚP | đúng (TT) | Không | N2 tr. 3: "On November 20, 2013, a grand jury sitting in the Southern District of Illinois charged Sunmola in an eight-count indictment with conspiracy … (Count One); mail fraud … (Counts Two through Four); wire fraud … (Counts Five through Seven); and interstate extortion … (Count Eight)." 1+3+3+1 = 8 | — (tên tội "interstate extortion" bắt buộc để đúng tội danh; toà không gắn Count Eight với ảnh → không tính là nhắc lại nhánh ảnh) |
| S039 | KHỚP | đúng (TT) | Không | N2 tr. 3: "On August 9, 2014, authorities arrested Sunmola while he was traveling in London" | — |
| S040 | KHỚP | đúng (◐) | Không | N1 ("…as he was about to board a plane from London to Johannesburg, South Africa.") | — |
| S041 | KHỚP | đúng (TT) | Không | N2 tr. 3: "transferred him to the custody of the United States on February 26, 2015." | — |
| S042 | KHỚP | đúng (TT) | Không | N2 tr. 3: "Trial commenced on February 29, 2016."; tr. 1: Southern District of Illinois | — |
| S043 | KHỚP | đúng (●) | Không | N2 tr. 1: "Three days into trial, Sunmola pleaded guilty to all eight counts."; tr. 3: "the judge accepted the guilty pleas without a plea agreement." | — |
| S044 | KHỚP | đúng (●) | Không | N2 tr. 3: "The judge asked Sunmola questions to ensure he knowingly and voluntarily entered the pleas. … the judge accepted the guilty pleas" | — |
| S045 | KHỚP | đúng (TT) | Không | N2 tr. 3: "the sentencing hearing should be held in two stages." | — |
| S046 | KHỚP | đúng (TT) | Không | N2 tr. 3–4: "On August 12, 2016, the Government presented its evidence, including victim impact testimony and expert testimony on the psychological impact of Sunmola's scheme" | — (không tên chuyên gia) |
| S047 | KHỚP | đúng (TT) | Không | N2 tr. 4: "On February 2, 2017 … United States Postal Inspector … testified"; tr. 14: "verified a spreadsheet, attached as an addendum, listing 39 additional victims beyond the 13 listed in the PSR" | — (không tên điều tra viên) |
| S048 | **MẠNH HƠN** (nhẹ) | đúng (●C về lời khai do toà thuật) | Không | N2 tr. 14: "he saw that Sunmola had attempted to contact many other individuals, but he was unable to reach all of these individuals. Thus, he concluded the total calculated loss of around $1.7 million was an underestimate" | Lời "many other people whom the investigator could not reach" hiểu thành *không liên lạc được ai trong số đó*; toà: *không liên lạc được hết*. Sửa: "…because Sunmola had tried to contact many other people, and the investigator could not reach all of them." |
| S049 | KHỚP | đúng (●C) | Không | N2 tr. 4: "a four-level leadership enhancement, a two-level enhancement for acting on behalf of a government agency, a four-level substantial financial hardship enhancement, a two-level vulnerable victim enhancement, a 16-level enhancement for an intended loss of $2,054,972.66, and a two-level enhancement due to Sunmola committing the offense outside of the United States." | — (6 tăng nặng đủ; 2,054,972.66 ≈ 2.05 triệu; thẻ chữ đúng số) |
| S050 | KHỚP | đúng (●) | Không | N2 tr. 5: "the judge sentenced Sunmola to 324 months' imprisonment" | — |
| S051 | KHỚP | đúng (●) | Không | N2 tr. 5: "ordered restitution in the amount of $1,707,260.98. The district court later amended the judgment to $1,669,050.98 to match the amount stated in the PSR." (1.71 / 1.67 triệu làm tròn đúng) | — |
| S052 | KHỚP | đúng (◐) | Không | N1 ("When Sunmola has completed his 27-year prison term, he will be removed to his native home of Nigeria.") | — |
| S053 | KHỚP | đúng (◐) | Không | N1 ("Over $200,000 in proceeds from the sale of Sunmola's four properties in South Africa has already been turned over to the District Court and will be proportionally disbursed to the individual identified victims.") — khớp N2 tr. 4 "$220,000 liquidated assets" | — |
| S054 | KHỚP | đúng (●C) | Không | N2 tr. 1: "DECIDED APRIL 16, 2018"; tr. 18: "For the foregoing reasons, we AFFIRM." | — |
| S055 | KHỚP | đúng (●C) | Không | N2 tr. 1: "appeals the district court's application of four sentencing enhancements, restitution calculation, and application of general deterrence"; tr. 5: liệt kê 4 tăng nặng + "the loss calculation" + "general deterrence"; tr. 15: "C. Restitution" | — |
| S056 | KHỚP | đúng (●C) | Không | N2 tr. 10: "Sunmola argues that he used his false military status to impress his victims, not for the purpose of obtaining a benefit on behalf of the military or other government organization. We disagree." | — |
| S057 | KHỚP | đúng (KBCB, thẻ chữ) | Không | N2 tr. 10 (như S022) | — |
| S058 | KHỚP | đúng (●C) | Không | N2 tr. 15: "Sunmola, amongst numerous arguments, nit-picks at almost every dollar"; tr. 13: "Sunmola "presented no documentary evidence to challenge the information in the PSR,"" | — |
| S059 | KHỚP | đúng (●C) | Không | N2 tr. 17: "The judge mentioned general deterrence in a mere four sentences out of the eight-page transcript from his oral statement. The judge repeatedly emphasized the seriousness of the offense" | — |
| S060 | KHỚP | đúng (●C) | Không | N2 tr. 8: "Sunmola and his co-conspirators chose the women they developed relationships with, specifically targeting women they believed would be susceptible to their deceitful tactics." | — |
| S061 | KHỚP | đúng (●C) | Không | N2 tr. 8: "Many of these women had been divorced, abandoned, widowed, or ignored by the men in their lives."; "most of the targeted women were middle-aged rather than elderly" | — (đã bỏ đúng các tổ hợp tuổi + hoàn cảnh nhận diện được ở tr. 8, §5) |
| S062 | KHỚP | đúng (●C) | Không | N2 tr. 8–9: "These women were seeking companionship through online dating, making them particularly susceptible…" | — |
| S063 | KHỚP (diễn ý) | **sai** — nhãn CHUNG nhưng vế 2 là ý gán cho toà ("according to the court") → phải ●C, hoặc bỏ chủ thể toà | Không | N2 tr. 8: "specifically targeting women they believed would be susceptible"; "Many of these women had been divorced, abandoned, widowed…"; tr. 8–9 "seeking companionship". Toà không dùng chữ "lonely". | Giữ vế 1 ở CHUNG, sửa vế 2 không gán chữ "lonely" cho toà: "Being lonely, or grieving, is not a flaw. In this case, it was the women's circumstances that the court found made them targets." (●C) — hoặc tách thành 2 câu: CHUNG + ●C |
| S064 | KHỚP | đúng (TT, có mốc "As of November 2026") | Không | N3: `"faclName":"Oakdale I","faclType":"FCI"`, `"projRelDate":"09/20/2037","actRelDate":""` | — (kiểm lại ngày đăng, luật 4) |
| S065 | KHÔNG CẦN NGUỒN | đúng (CHUNG) | Không | — (đếm: bài học S066, S067, S069 = 3; dấu hiệu S071, S073–S076 = 5; luật S077 = 1 — khớp) | — |
| S066 | KHỚP | đúng (●C) | Không | N2 tr. 11–12: "He recruited accomplices, … and directed everyone else on what to tell the victims." | — |
| S067 | KHỚP | đúng (●C; vế mở là bài học chung) | Không | N2 tr. 8: "specifically targeting women they believed would be susceptible…"; "divorced, abandoned, widowed"; "most of the targeted women were middle-aged" | — |
| S068 | KHỚP | đúng (CHUNG có nguồn) | Không | N6: "However, the elderly, women, and those who have lost a spouse are often targeted." | — |
| S069 | KHỚP | đúng (●C) | Không | N2 tr. 4: "one for psychological injury to a victim"; tr. 14: "the total calculated loss of around $1.7 million was an underestimate" | — |
| S070 | KHÔNG CẦN NGUỒN | đúng (CHUNG, không hàm ý sự việc mới về người thật) | Không | — | — |
| S071 | KHỚP | đúng (●C + N6) | Không | N2 tr. 10 (soldier / colonel); N6: "Claims to be from the U.S. but is currently living, working, or traveling abroad."; "claims to be a U.S. service member serving overseas" | — (câu không liên quan S072 cùng đoạn) |
| S072 | KHỚP | đúng (KBCB, thẻ chữ) | Không | N2 tr. 10 | — |
| S073 | KHỚP | đúng (●C + N6) | Không | N2 tr. 2: "ask for money and merchandise"; tr. 10: "computer equipment"; N6: "Asks for money, goods, or any similar type of financial assistance" | — |
| S074 | KHỚP | đúng (◐) | Không | N1 ("The women were invariably told to direct their shipments to "Ilumsa Sunmola," who was passed off as their lover's driver, or a co-worker, or a hotel manager. In fact, it was Sunmola himself…") | — |
| S075 | KHỚP | đúng (◐ + N6) | Không | N1 ("…manufacture phony emergencies, each of which required increasingly large amounts of money…"; "When the money inevitably ran out…"); N6: "Reports a sudden personal crisis and pressures you to provide financial assistance." | — |
| S076 | **MẠNH HƠN** (ghép hai nguồn) | sai một phần — nhãn ●C nhưng ý "ảnh của người khác" chỉ có ở N1 (◐, "photographs stolen…") | Không | N2 tr. 2: "Sunmola often used pictures of men in U.S. military uniforms as part of his online profile." (toà không nói ảnh là của ai / lấy cắp); N1: "photographs stolen from the hacked online accounts of real American men"; N6: "Most cyber criminals do not use their own photographs… A reverse image search can determine if a profile picture is being used elsewhere on the internet" | Đặt "a profile photo that may belong to someone else" cạnh "The court said he often used pictures of men in uniform" khiến người nghe hiểu toà xác nhận ảnh quân phục là ảnh lấy của người khác (ghép N2 + N1). Sửa: "Five: a profile photo that may belong to someone else. Prosecutors said he used photographs stolen from real American men's hacked accounts, and the F-B-I suggests a reverse image search to check whether a profile picture is being used elsewhere online." (nhãn ◐ + N6). Nếu cần giữ quân phục: tách thành câu ●C riêng, không nối với "belong to someone else" |
| S077 | KHỚP | đúng (CHUNG có nguồn; vế "We would add" là lời khuyên chung, không khuyên đầu tư) | Không | N6: "Never send money to someone you meet online, especially by wire transfer." (lời trích cắt đúng chữ) | — |
| S078 | KHỚP | đúng (CHUNG) | Không | N7: "The Internet Crime Complaint Center (IC3) is the central hub for reporting cyber-enabled crime. It is run by the FBI"; N6: "Contact IC3 at www.ic3.gov"; N8: `<title>ReportFraud.ftc.gov` | — |
| S079 | KHÔNG CẦN NGUỒN | đúng (CHUNG) | Không | — | — |

## Kiểm theo chủ đề

1. **●C / ◐ và ghép nguồn:** mọi câu "prosecutors said" đều ◐ từ N1; mọi ●C có câu tương ứng trong N2 đúng trang. Một chỗ ghép ngầm: **S076** (ảnh quân phục của toà + "ảnh của người khác" của DOJ). S015 dùng "Separately" — tách đúng. Mốc thời gian dùng 3/2008 (S013), không dùng "2007 to 2014" của N1.
2. **Nhánh ảnh riêng tư:** đúng một câu (S033), thẻ chữ, `doc: false`, khớp N2 tr. 2. Quét toàn bộ `loi` + `chu` bằng mẫu `dung_mot` và các từ gần (exploit, threat, image, nude, video, extort): không câu nào khác gợi lại nhánh này trong bài học, dấu hiệu, tổng kết. Lưu ý duy nhất: S038 nêu tội danh "interstate extortion" (bắt buộc cho đúng tội danh; toà không gắn Count Eight với ảnh) — không tính vi phạm; S036/S069 "psychological injury"/"gratuitous infliction of injury" là thuật ngữ toà, không gợi nhánh ảnh.
3. **§5:** nạn nhân người lớn, không tên, không bang (Georgia/St. Louis đã bỏ), không tổ hợp tuổi + hoàn cảnh (55/66 tuổi đã bỏ), không trích lời nạn nhân, không số tiền từng người (đã bỏ "$90,000" của N1), không tự sát/váy cưới. Không giật gân.
4. **Quân đội Mỹ / tên:** mọi đoạn có từ quân đội (P00, P02, P04, P11, P12) đều có câu "had nothing to do". Không tên giả (Elias Dyess), không Match.com/MoneyGram/Western Union, không tên điều tra viên/chuyên gia/công tố/thẩm phán. Không nhãn "scammer/con man" ở giọng kể (S010 "conned" là lời khiếu nại của nạn nhân do DOJ thuật, ◐).
5. **Số:** đã đối chiếu 324 tháng = 27 năm; 8 tội (1+3+3+1); 20/11/2013; 09/08/2014; 02/2015 (26/02); 29/02/2016; 3 ngày; 12/08/2016; 02/2017; 39 + 13; ~1,7 triệu; 2,054,972.66; 1,707,260.98 → 1,669,050.98; 7 nạn nhân khó khăn ≥ 5; > 800 000; ≥ 3 phá sản; > 200 000 / 4 bất động sản; 16/04/2018; 4 câu / 8 trang; 2037. **Không có số sai.**
6. **CHUNG:** S068, S077, S078 khớp N6/N7/N8 nguyên văn; CHUNG không nguồn (S009, S028, S065, S070, S079) không hàm ý sự việc mới về người thật. S063 là CHUNG chứa ý gán cho toà (xem bảng).
7. **Phép thử §1:** không câu nào làm theo được ngay. Phần thao tác đặt hàng, tìm cửa hàng nhận hàng, dữ liệu thẻ giả (N2 tr. 11–12), tên dịch vụ chuyển tiền đã bị loại; S025/S074 chỉ nêu khái niệm "người nhận trung gian" kèm sự thật đó là chính bị cáo.

## Tổng

| Kết luận | Số câu |
|---|---|
| KHỚP | 71 |
| MẠNH HƠN | 2 (S048, S076) |
| SAI | 0 |
| KHÔNG CẦN NGUỒN | 6 (S001, S009, S028, S065, S070, S079) |
| **Tổng** | **79** |

- Tầng sai: 2 (S063 — CHUNG chứa ý gán toà; S076 — ●C mang ý của N1).
- "Làm theo được ngay = Có": **0**.

## Đề xuất sửa

**Bắt buộc**
1. **S076** — bỏ ghép N2 + N1: "Five: a profile photo that may belong to someone else. Prosecutors said he used photographs stolen from real American men's hacked accounts, and the F-B-I suggests a reverse image search to check whether a profile picture is being used elsewhere online." → nhãn ◐, nguồn N1 + N6.
2. **S048** — "…because Sunmola had tried to contact many other people, and the investigator could not reach all of them."
3. **S063** — sửa nhãn/lời: "Being lonely, or grieving, is not a flaw. In this case, it was the women's circumstances that the court found made them targets." (●C, N2 tr. 8–9) hoặc tách CHUNG + ●C.

**Tuỳ chọn (không ảnh hưởng kết luận)**
4. S004 — tách "Neither story was true" (●C) khỏi câu KBCB.
5. S008 — đổi nhãn ● → ●C.
6. S007 — thêm "N2 tr. 4" vào nguồn cho năm 2017.
7. S012 — bỏ "the evidence presented in court showed" để "hundreds" không bị nghe như số toà xác nhận.
