# Kiểm độc lập vòng 3 — dàn truyện `romance-sunmola`

> Tệp được kiểm: `docs/dan-truyen/romance-sunmola.md` (bản trong cây làm việc ngày 01/11/2026). Tác tử kiểm độc lập, **không sửa** tệp được kiểm, không commit/push. Chi 0 USD (không gọi API trả tiền, không PACER).
> Thang chấm: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được.

## 1. Phạm vi đọc
- Đã đọc: `CLAUDE.md`, `docs/HIEN-CHUONG.md` (toàn văn), tệp được kiểm (toàn văn), `docs/kho-de-tai/romance-sunmola.md` **chỉ §8**.
- **Không** đọc: `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 tệp kho, dàn truyện khác, `docs/dan-truyen/kiem/**` (kể cả vòng 1, vòng 2), git log/diff.

## 2. Nguồn đã mở (01/11/2026)
| Mã | Đường | Kết quả |
|---|---|---|
| N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf`; `pdftotext -layout`, tách theo form-feed; số trang = số in đầu trang (trùng thứ tự PDF; khối thứ 19 rỗng) | SHA-256 `cc362fa04d95dd71c5af59f50a3f2e6ab4b0393a9c65f54754e7ab710959953b` — **khớp** kho §8. Đọc đủ 18 trang |
| N1 | `curl -sS -G https://www.justice.gov/api/v1/press_releases.json --data-urlencode "parameters[title]=Prince Charming"` | HTTP 200, `count` = 1; tiêu đề "'Prince Charming' Behind Bars: Nigerian Romance Scammer Nets 27-Year Prison Sentence"; `body` HTML đọc đủ |
| N6 | https://www.ic3.gov/PSA/2019/PSA190805 (curl mặc định) | HTTP 200; "August 5, 2019 · Alert Number I-080519-PSA" — khớp tên/ngày ở §7 tệp |
| N7 | https://www.ic3.gov/ | HTTP 200; trang chủ IC3 ("File A Complaint") |
| N8 | https://reportfraud.ftc.gov/ | HTTP 200; `<title>ReportFraud.ftc.gov`, mô tả "Protect your community by reporting fraud, scams, and bad business practices" |

Tệp tải về ở `/tmp/claude-0/kiem-sunmola-v3/dl/` (không đưa vào repo); python đọc chạy `-I`. Không gặp 403/CAPTCHA ở các nguồn trên. Hai trang FTC/FBI mà §7 tệp ghi "chưa mở được" **không** được mở lại (tệp không dùng chúng).

## 3. Bảng chấm từng dòng

### 3.1 Đầu tệp, §0
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| 0.1 | Ký hiệu tầng: nhận tội cả 8 tội ngày thứ ba, không thoả thuận, toà chấp nhận, 324 tháng, 7th Cir. giữ nguyên 16/04/2018 | N2 tr. 1 ("Three days into trial, Sunmola pleaded guilty to all eight counts"; "DECIDED APRIL 16, 2018"), tr. 3 ("judge accepted the guilty pleas without a plea agreement"), tr. 5 (324 months), tr. 18 ("we AFFIRM") | K |
| 0.2 | Quy ước: N2 18 tr., số in trùng số PDF | Kiểm trực tiếp | K |
| 0.3 | §0: câu đe doạ của bị cáo ở N2 tr. 2 — không trích | N2 tr. 2 có câu trích của bị cáo trong đoạn đó | K |
| 0.4 | §0: "không bang + tuổi + hoàn cảnh ghép lại (N2 tr. 8 có tổ hợp như vậy)" | N2 tr. 8 có các ca cụ thể **tuổi + hoàn cảnh**, **không có bang**; bang (hai bang) ở tr. 2. Là rào chắn nội bộ, chặt hơn nguồn chứ không nói thêm về người thật | K (ghi chú G1: chính xác hoá ngoặc thành "tr. 8: tuổi + hoàn cảnh; tr. 2: bang") |
| 0.5 | §0: N1 có ý nghĩ tự sát của nạn nhân; chi tiết "váy cưới" ở N1 | N1 đoạn "Even worse than the financial hardships…" ("Two victims told the court they had seriously contemplated suicide"; "A few had even purchased wedding dresses") | K |
| 0.6 | §0: N1 nêu một tên giả | N1 đoạn "The U.S. Postal Inspection Service began investigating…" (một tên giả trong ngoặc kép) | K |

### 3.2 Logline
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| L-VI | "Từ Nam Phi, Olayinka Sunmola lập hồ sơ hẹn hò dưới tên giả, **đóng vai lính hay sĩ quan Mỹ** làm nhiệm vụ ở nước ngoài, chiếm lòng tin của phụ nữ trung niên ở Mỹ rồi xin tiền và đồ điện tử cho 'nhiệm vụ'; bị bắt ở London, nhận cả 8 tội giữa phiên xử, 27 năm tù, phúc thẩm giữ nguyên" | N2 tr. 2: hồ sơ dưới tên giả, cho phụ nữ tin họ là **"successful businessmen"**, "often used pictures of men in U.S. military uniforms"; tr. 10: vai lính/đại tá chỉ **"In some instances… In other instances"**. Các vế còn lại khớp tr. 2, 3, 5, 18; N1 "27-year prison term" | **MH** (khái quát: bỏ "có lúc/với một số phụ nữ" — logline EN thì giữ "some of the women") |
| L-EN1 | "He told some of the women he was an American soldier or Army officer serving overseas." | N2 tr. 10 (soldier "stranded in Nigeria on a mission"; "colonel in the U.S. Army deployed to South Africa") | K |
| L-EN2 | "He was actually running an online romance scheme from South Africa." | N2 tr. 2 ("carried out an international online romance scheme from the Republic of South Africa") | K |
| L-EN3 | "A federal judge sentenced him to 27 years." | N2 tr. 5 (324 months); N1 ("27-year prison term") | K |

### 3.3 Móc câu H1–H6
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| H1 | Cảnh laptop, chữ mờ không đọc được | Không có sự việc; ràng buộc hình đúng §1/§5 (không dựng tin nhắn đọc được) | K (không có sự việc) |
| H2 | Lính Mỹ kẹt ở Nigeria làm nhiệm vụ; đại tá Lục quân ở Nam Phi cần thiết bị máy tính để hoàn thành nhiệm vụ | N2 tr. 10, đúng từng vế ("stranded in Nigeria on a mission"; "colonel in the U.S. Army deployed to South Africa… purchase and ship computer equipment… finish his assignments") | K |
| H3a | "None of it was true" | N2 tr. 10 ("pretended", "held himself out", "clearly misrepresented") | K |
| H3b | "the U.S. Army had nothing to do with it" | Câu không liên quan bắt buộc (8e); N2 tr. 10 xác định đây là mạo xưng | K |
| H3c | "According to the appeals court… running an online romance scheme from South Africa and targeting middle-aged women in the United States" | N2 tr. 2 | K |
| H4 | "Prosecutors said his goal was to make each woman believe he was her 'Prince Charming.'" | N1 đoạn "The U.S. Postal Inspection Service…" ("Sunmola's purpose was to lead each of his victims to believe that he was her 'Prince Charming'") — ◐D, có chủ thể | K |
| H5 | "In 2017, a federal judge sentenced him to 324 months — 27 years" | N2 tr. 4 (phiên thứ hai 02/02/2017), tr. 5 (324 months); N1 (ngày 02/02/2017, "sentenced this morning to serve 324 months") | K |
| H6 | Chữ trích lời thẩm phán, "as quoted by the U.S. Court of Appeals for the Seventh Circuit" | N2 tr. 17 — trùng nguyên văn kể cả "someone" | K |
| H-gc | Ghi chú: N1 khác chữ ("without laying hands…", không "someone") | N1 đoạn "United States District Judge David R. Herndon agreed…" | K |

### 3.4 Bảng nhịp
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| 0 | Móc câu H1–H6 | như 3.3 | K |
| 1 | 2012, một phụ nữ ở S.D. Ill. khiếu nại; USPIS điều tra; một trong hàng chục hồ sơ giả do Sunmola và đồng phạm lập — "according to prosecutors" | N1 đoạn "The U.S. Postal Inspection Service began investigating Sunmola in 2012…" ("dozens of fictitious online profiles Sunmola and his confederates concocted") | K |
| 2a | Toà: từ 3/2008, từ Nam Phi, nhắm phụ nữ trung niên ở Mỹ; hồ sơ tên giả; tự nhận doanh nhân thành đạt; thường dùng ảnh đàn ông mặc quân phục Mỹ | N2 tr. 2 | K |
| 2b | "Theo DOJ, **ảnh** lấy cắp từ tài khoản bị hack của những người đàn ông Mỹ thật" (đặt ngay sau vế ảnh quân phục) | N1: "he used photographs stolen from the hacked online accounts of real American men" — **không** nói đó là ảnh quân phục; N2 tr. 2 nói ảnh quân phục nhưng **không** nói lấy cắp từ ai. Câu ghép khiến "ảnh" đọc như chính ảnh quân phục | **MH** (ghép hai nguồn thành khẳng định không nguồn nào nói) — nhẹ |
| 2c | Dùng mốc 3/2008 của toà; N1 ghi "2007 to 2014" | N2 tr. 2; N1 đoạn "Olayinka Ilumsa Sunmola, 33, of Lagos…" | K |
| 3 | Theo DOJ: thơ, thiệp, hoa, gấu bông, sô-cô-la; tìm hiểu thành phố Mỹ giả là quê | N1 đoạn "The U.S. Postal Inspection Service…" (hai câu cuối đoạn) | K |
| 4 | Toà: sau khi chiếm lòng tin, ông và đồng phạm xin tiền và hàng; phụ nữ gửi đồ điện tử, chuyển tiền vì "khó khăn tài chính" giả; ông khiến nạn nhân tin tiền/thiết bị dùng cho công việc cho chính phủ Mỹ; toà xác định mạo xưng nhân danh quân đội (tăng nặng giữ nguyên) | N2 tr. 2 ("After gaining the women's trust… false claims of financial distress"); tr. 10 ("work for, or on behalf of, the U.S. government"; "clearly misrepresented… on behalf of… the U.S. military"; "did not err in applying this enhancement") | K |
| 4b-1 | Theo DOJ: hàng gửi cho "Ilumsa Sunmola", giới thiệu là tài xế/đồng nghiệp/quản lý khách sạn, thực ra chính là ông | N1 đoạn "…him money or shipping him laptop computers…" ("invariably told to direct their shipments to 'Ilumsa Sunmola'… driver, or a co-worker, or a hotel manager. In fact, it was Sunmola himself…") | K |
| 4b-2 | "Khẩn cấp" nối tiếp, số tiền tăng dần | N1 đoạn "Once he had successfully beguiled his target…" ("phony emergencies, each of which required increasingly large amounts") | K |
| 4b-3 | Tiền cạn hoặc phụ nữ từ chối → cắt đứt đột ngột | N1 ("When the money inevitably ran out, or the women refused to send more, Sunmola would abruptly end the relationship") | K |
| 4b-gc | N2 tr. 14 có tên dịch vụ chuyển tiền | N2 tr. 14 (có hai tên) | K |
| 5a | Toà giữ nguyên: người tổ chức/cầm đầu; tuyển đồng phạm, đặt hàng, nhận hàng và tiền chuyển, chỉ đạo người khác nói gì với nạn nhân | N2 tr. 11–12 | K |
| 5b | "theo toà, công tố đưa bằng chứng cho thấy có thể ông lấy phần lớn hơn ('evidence suggesting')" | N2 tr. 12 ("The Government also presented evidence suggesting that Sunmola commanded a larger share") — đúng tầng, có rào | K |
| 5c | Theo toà, nhà điều tra tìm thấy bằng chứng gian lận thẻ tín dụng **gây thiệt hại** cho nhiều doanh nghiệp | N2 tr. 2 ("discovered evidence of credit card fraud **affecting** various businesses") | K (ghi chú G2: khi viết lời EN giữ "affecting", không viết "costing/causing losses to") |
| 5d | Theo DOJ, một hãng máy tính lỗ hơn 800.000 USD | N1 đoạn "Two victims were present…" ("The loss incurred by one computer manufacturer alone was over $800,000") | K |
| 6 | **Câu duy nhất:** *"With some of the women, it went further: he threatened to expose private images."* — ●C, N2 tr. 2 | N2 tr. 2: "In some instances" chỉ phần bóc lột (vế "it went further" có điểm tựa); nhưng **lời đe doạ đăng ảnh** tòa chỉ nêu với **một** phụ nữ ("threatened to post photos of a third woman"); các trường hợp khác cùng đoạn là hành vi khác, không phải lời đe doạ đăng ảnh. Câu đặt "some of the women" làm chủ ngữ cho "threatened" → số nhiều ở tầng ●C không có nguồn. (N1 — ◐D — có nói ảnh được dùng để tống tiền ít nhất hai phụ nữ, nhưng dòng này dẫn N2 ●C) | **MH** (rộng hơn: số nhiều) — nhẹ |
| 6-gc | N2 không nói Count Eight dựa trên hành vi nào | N2 tr. 3 chỉ liệt kê tội danh/điều luật | K |
| 7a | Theo DOJ: ít nhất 3 phụ nữ phá sản; "several more" mất việc, mất nhà | N1 đoạn "The United States has no way of knowing…" | K |
| 7b | Tăng nặng "khó khăn tài chính nghiêm trọng cho ≥ 5 nạn nhân"; PSR liệt kê 7 người; phúc thẩm giữ nguyên | N2 tr. 6 ("five or more victims"; "listed seven victims"), tr. 7 ("did not clearly err") | K |
| 7c | Hai lần tăng vượt khung theo đề nghị công tố: tổn hại tâm lý; "gratuitous infliction of injury" | N2 tr. 4 | K |
| 7d | Hai lần này không nằm trong các điểm kháng cáo | N2 tr. 2, tr. 5 (danh sách điểm kháng cáo không có departures) | K |
| 8a | 20/11/2013 đại bồi thẩm S.D. Ill. truy tố 8 tội: âm mưu; 3 mail fraud; 3 wire fraud; "tống tiền liên bang" | N2 tr. 3 (Count One; Two–Four; Five–Seven; Count Eight "interstate extortion", 18 U.S.C. § 875(d)) | K (ghi chú G3: "interstate" = liên tiểu bang; lời EN theo §5(d) dùng "interstate extortion" là đúng) |
| 8b | 09/8/2014 bị bắt khi đang đi qua London | N2 tr. 3 ("arrested Sunmola while he was traveling in London") | K |
| 8c | Theo DOJ, sắp lên máy bay London → Johannesburg | N1 đoạn "A federal grand jury sitting in East St. Louis…" | K |
| 8d | 26/02/2015 giao cho Mỹ | N2 tr. 3 | K |
| 9 | Phiên xử mở 29/02/2016; ngày thứ ba nhận cả 8 tội; không thoả thuận; thẩm phán hỏi bảo đảm hiểu biết, tự nguyện; chấp nhận | N2 tr. 1, 3; N1 ("on March 2, 2016, after two full days of trial" — 2016 nhuận, 02/3 là ngày thứ ba) | K |
| 10a | Tuyên án hai giai đoạn: 12/8/2016 (lời khai ảnh hưởng nạn nhân + chuyên gia tổn hại tâm lý); 02/02/2017 (điều tra viên bưu chính) | N2 tr. 3–4 | K |
| 10b | 13 nạn nhân trong PSR + 39 bổ sung; theo lời điều tra viên, ~1,7 triệu USD là ước thấp | N2 tr. 4, 14 ("39 additional victims beyond the 13 listed in the PSR"; "he concluded the total calculated loss of around $1.7 million was an underestimate") — tầng ghi đúng là lời điều tra viên, toà ghi lại | K |
| 10c | Các mức tăng nặng (cầm đầu, mạo xưng cơ quan chính phủ, khó khăn tài chính, nạn nhân dễ tổn thương, intended loss 2.054.972,66 USD, phạm tội ngoài nước Mỹ); thiệt hại thực tế 1.669.050,98 USD ở tr. 14–15 | N2 tr. 4; tr. 14 ("determined an actual loss calculation of $1,669,050.98"), tr. 15 | K |
| 10d | 324 tháng; bồi hoàn 1.707.260,98 USD, sau sửa 1.669.050,98 USD | N2 tr. 5 | K |
| 11a | 16/04/2018 phúc thẩm giữ nguyên toàn bộ | N2 tr. 1, 18 | K |
| 11b | Toà viết ông và đồng phạm **chọn** phụ nữ họ tin dễ bị lừa; nhiều người ly hôn, bị bỏ rơi, goá, hoặc bị người đàn ông trong đời bỏ mặc; phần lớn trung niên chứ không phải người già | N2 tr. 8 (câu khái quát; không dùng các ca cụ thể cùng trang — đúng) | K |
| 11b-1 | Theo DOJ: mãn hạn → trục xuất về Nigeria | N1 đoạn "When Sunmola has completed his 27-year prison term…" ("removed to his native home of Nigeria") | K |
| 11b-2 | Hơn 200.000 USD từ bán 4 bất động sản ở Nam Phi đã nộp toà, chia cho nạn nhân đã xác định | N1 cùng đoạn ("Over $200,000 in proceeds from the sale of Sunmola's four properties…") | K |
| 11b-3 | Số 220.000 ở N2 tr. 4 là lời công tố báo với thẩm phán | N2 tr. 4 ("The Government advised the judge that the clerk of the court had possession of $220,000 liquidated assets") | K |
| 11b-4 | Kho N3: còn thụ án, dự kiến ra 2037 — kiểm lại ngày chốt lời | Kho §8 N3 (projRelDate 09/20/2037). Không mở lại BOP (ngoài danh sách nguồn vòng này); tệp đã ghi phải kiểm lại, không đưa vào lời | K (đối chiếu kho §8) |
| gc-54 | N1 có một câu trích của nạn nhân — không dùng | N1 đoạn "The United States has no way of knowing…" | K |

### 3.5 §3 khuôn tập, cú treo
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| §3 | P2 có bước ngoặt có hồ sơ (nhận tội giữa phiên xử) | N2 tr. 3 | K |
| CT1 | "He was arrested in London in August 2014." | N2 tr. 3 | K |
| CT2 | "In February 2016, his trial began in Illinois." | N2 tr. 3 ("Trial commenced on February 29, 2016"); tr. 1 (S.D. Ill.) | K |
| CT3 | "It would not make it to a verdict." | N2 tr. 1, 3 (nhận tội ngày thứ ba, không có phán quyết) | K |

### 3.6 Bài học, dấu hiệu, nguyên tắc, thẻ tổng kết
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| L1 | Toà mô tả người cầm đầu tuyển đồng phạm, nhận tiền và hàng, chỉ đạo người khác nói gì với nạn nhân; "người yêu" trên màn hình **có thể** không phải một người | N2 tr. 11–12; tr. 2 ("Sunmola and his co-conspirators created profiles") — câu suy rộng có rào "có thể" | K |
| L2a | Toà viết nhóm này chọn phụ nữ họ tin dễ bị lừa; nhiều người ly hôn, goá, bị bỏ rơi; phần lớn trung niên | N2 tr. 8 | K |
| L2b | FBI ghi người goá thường là mục tiêu | N6 ("the elderly, women, and those who have lost a spouse are often targeted") | K |
| L2c | "Cô đơn sau mất mát không phải lỗi của nạn nhân — đó là thứ kẻ gian tìm." | Câu khái quát không gắn tên; điểm tựa N6 (như L2b) và N2 tr. 8 ("seeking companionship through online dating") | K (ghi chú G4: nên gắn nhãn "lời của kênh" như các câu khuyên chung khác) |
| L3a | Toà tăng án vì tổn hại tâm lý | N2 tr. 4 (upward departure for psychological injury) | K |
| L3b | Điều tra viên cho rằng ~1,7 triệu USD là ước thấp vì Sunmola đã tìm cách liên lạc nhiều người mà điều tra viên không liên lạc được hết | N2 tr. 14 | K |
| L3c | "(Lời khuyên chung của kênh, không gắn nguồn:) báo cáo — kể cả khi xấu hổ…" | Tự nhận không gắn nguồn; không bị gắn nguồn sai | K |
| D1 | Nói đang làm nhiệm vụ ở nước ngoài (lính, sĩ quan; theo DOJ có lúc là kỹ sư làm hợp đồng chính phủ) | N2 tr. 10; N1 ("an engineer working on a large government contract in South Africa"); N6 ("claims to be a U.S. service member serving overseas") | K |
| D2 | Xin tiền hoặc hàng (máy tính, điện thoại) cho "công việc" | N2 tr. 2, 10; N1 ("laptop computers, tablets, and cell phones – equipment he told them he needed to complete his government mission"); N6 ("Asks for money, goods…") | K |
| D3 | Gửi cho người thứ ba — tài xế, đồng nghiệp, quản lý khách sạn | N1 (như 4b-1) | K |
| D4 | Khẩn cấp nối tiếp, số tiền tăng dần; ngừng gửi thì người kia biến mất | N1 (như 4b-2, 4b-3); N6 ("Reports a sudden personal crisis…"; "increasingly aggressive") | K |
| D5 | "Ảnh hồ sơ có thể là của người khác (ở vụ này: **thường là ảnh đàn ông mặc quân phục, theo DOJ lấy cắp của đàn ông thật**)" | Cùng lỗi ghép như 2b: N2 tr. 2 ("often used pictures of men in U.S. military uniforms") không nói nguồn ảnh; N1 nói "photographs stolen from the hacked online accounts of real American men" không nói là ảnh quân phục. Vế "kiểm xem ảnh có xuất hiện nơi khác" khớp N6 ("A reverse image search can determine if a profile picture is being used elsewhere") | **MH** (ghép nguồn) — nhẹ |
| P1 | Không gửi tiền hay hàng cho người chỉ quen trên mạng, chưa gặp trực tiếp (FBI) | N6 ("Never send money to someone you meet online, especially by wire transfer"; danh sách dấu hiệu: "Asks for money, goods… especially if you have never met in person") — gộp hai câu cùng tài liệu | K |
| P2 | (lời khuyên chung của kênh) kể với người tin cậy | Tự nhận không gắn nguồn | K |
| P3 | Kiểm ảnh hồ sơ có xuất hiện nơi khác (N6) | N6 | K |
| P4 | Báo cáo: FBI IC3 (N7), FTC ReportFraud (N8) | N7, N8 HTTP 200; N6 cũng khuyên báo IC3 | K |
| TK1 | "A romance scheme can be an organization, not one lonely stranger." | Bài học khái quát từ N2 tr. 11–12 | K |
| TK2 | "In this case, the court said the group chose women it believed would be easy to deceive — many divorced, widowed or abandoned, looking for companionship online." | N2 tr. 8 ("targeting women they believed would be susceptible to their deceitful tactics"; "divorced, abandoned, widowed"; "seeking companionship through online dating") | K |
| TK3 | "The real damage is bigger than the dollar figure." | Bài học khái quát từ N2 tr. 4, 14 | K |
| TK-RF | Năm dấu hiệu rút gọn | như D1–D5 (bản rút gọn trên thẻ **không** chứa vế ghép của D5: "a profile photo that may belong to someone else") | K |
| TK-P | "Never send money to someone you've only met online. Report it." | N6 | K |
| TK-gc | Thẻ không nhắc nhánh ảnh riêng tư | Kiểm trực tiếp | K |

### 3.7 §5 tổng hợp, §7, §8
| # | Dòng | Bằng chứng | Chấm |
|---|---|---|---|
| R-a | Trung tâm ● (N2 tr. 1, 3, 5, 18) | như 0.1 | K |
| R-d | Dùng "pleaded guilty to conspiracy, mail fraud, wire fraud and interstate extortion" | N2 tr. 3 ("openly pleaded guilty to all counts"; danh sách tội) | K |
| R-f | "chọn mục tiêu" là lời toà (N2 tr. 8) | N2 tr. 8 ("chose the women…") | K |
| R-§5 | Nạn nhân người lớn: tr. 2 "middle-aged women", tr. 8 "most of the targeted women were middle-aged rather than elderly"; không có dấu hiệu vị thành niên trong N1, N2 | N2 tr. 2, 8 nguyên văn; đọc toàn văn N1 và N2: không có nạn nhân vị thành niên | K |
| §7 | N6 tên/ngày/số PSA; N7, N8 HTTP 200 | Mở lại: khớp | K |
| §8 | "887 F.3d 830" | Không có reporter trong phạm vi nguồn vòng này; tệp tự ghi chưa đối chiếu và chưa dùng | KKĐ (không phải lỗi tệp) |

## 4. §5 / ảnh riêng tư / nhận diện / hướng dẫn làm
- **Ảnh riêng tư — số lần xuất hiện tới người xem:** đúng **một** câu (nhịp 6), mức khái niệm, không mô tả nội dung ảnh/video, không dựng cảnh (chỉ thẻ chữ tối), không trích câu đe doạ, không lặp ở D, P, L, thẻ tổng kết. Các chỗ khác nhắc tới chỉ là rào chắn nội bộ (§0, §5, §8). Tội danh "interstate extortion" ở nhịp 8–9/§5(d) là tên tội, không nối với nhánh ảnh — đúng ghi chú nhịp 6. **Đạt**, trừ lỗi số nhiều ở câu (MH-3, sửa không làm tăng mức mô tả).
- **Nhạy cảm khác:** không ý nghĩ tự sát, không "váy cưới", không trích lời nạn nhân — **đạt**.
- **Nhận diện nạn nhân:** không tên, không tuổi, không bang gắn với người, không số tiền từng người, không dùng các ca cụ thể N2 tr. 8. Chi tiết duy nhất về một cá nhân là "một phụ nữ ở Southern District of Illinois khiếu nại năm 2012" (N1) — đơn lẻ, không ghép tuổi/hoàn cảnh/số tiền → không nhận diện được. Thẻ tổng kết chỉ dùng câu khái quát của toà. **Đạt.**
- **Chỉ nạn nhân người lớn:** N2 tr. 2, 8; toàn văn N1, N2 không có vị thành niên. **Đạt.**
- **Hướng dẫn làm (HIEN-CHUONG §1):** không mẫu hồ sơ, tin nhắn, thơ; H1 chữ mờ; không tên trang hẹn hò, dịch vụ chuyển tiền; không cách lấy ảnh, mua dữ liệu thẻ, chọn nơi nhận hàng (N2 tr. 11 bị loại đúng). H2 và nhịp 4b mô tả vai giả và sơ đồ "người yêu → người nhận hàng → cùng một người" ở mức khái niệm/dấu hiệu, không phải lời dụ chép dùng được. **Đạt.**
- **Luật 8:** (a) ● đạt; (b) không có ai tên ở ◐; (c) không tên đồng phạm/hãng/trang/dịch vụ; (d) không nhãn ở giọng kể, "Prince Charming" chỉ ở H4 có chủ thể DOJ; (e) câu "the U.S. Army had nothing to do with it" ở H3 và bắt buộc nhắc ở nhịp 4; (f) không suy đoán động cơ ngoài hồ sơ. **Đạt.** Luật 5: người KBCB không tên — **đạt**.

## 5. Tổng điểm
Tính trên các dòng có sự việc ở mục 3 (kể cả ghi chú nguồn trong tệp):

| K | MH | S | KKĐ |
|---|---|---|---|
| 83 | 4 | 0 | 1 |

- MH (cả bốn đều **nhẹ**, không đổi tầng, không chạm người có tên khác ngoài bị cáo):
  - **MH-1** Logline VI: "đóng vai lính hay sĩ quan Mỹ" khái quát — toà chỉ nói "in some instances / in other instances"; hồ sơ hẹn hò theo toà là "successful businessmen".
  - **MH-2** Nhịp 2 vế ◐D: "ảnh lấy cắp…" đặt ngay sau ảnh quân phục → ghép thành "ảnh quân phục lấy cắp của đàn ông thật", không nguồn nào nói vậy.
  - **MH-3** Nhịp 6: "With some of the women… he threatened to expose private images" — ●C N2 tr. 2 chỉ có lời đe doạ đăng ảnh với **một** phụ nữ.
  - **MH-4** D5: cùng lỗi ghép như MH-2.
- S: 0.
- KKĐ: §8 "887 F.3d 830" (không có reporter; tệp đã tự đánh dấu chưa đối chiếu, không dùng) — không phải lỗi.
- **Kết luận vòng 3: còn 0 S nhưng chưa đạt 0 MH (4 MH nhẹ).**

## 6. Sửa bắt buộc
1. **MH-1 (logline VI):** đổi "đóng vai lính hay sĩ quan Mỹ…" → "**với một số phụ nữ**, đóng vai lính hay sĩ quan Mỹ…" (hoặc "có lúc đóng vai…"), khớp logline EN và N2 tr. 10.
2. **MH-2 (nhịp 2):** tách vế DOJ khỏi ảnh quân phục: "Theo DOJ, **ông dùng ảnh lấy cắp** từ tài khoản bị hack của những người đàn ông Mỹ thật" (không gọi đó là ảnh quân phục). Lời EN tương ứng: "Prosecutors said he used photographs stolen from the hacked online accounts of real American men."
3. **MH-3 (nhịp 6), giữ đúng một câu mức khái niệm, không thêm mô tả:** đổi số nhiều thành điều toà nói, vd *"With at least one woman, it went further: he threatened to post private photos."* (●C, N2 tr. 2). Nếu muốn giữ số nhiều thì phải đổi tầng sang ◐D N1 có chủ thể ("prosecutors said…") — không khuyến nghị vì kéo theo mô tả hành vi khác.
4. **MH-4 (D5):** tách hai nguồn: "(ở vụ này: toà nói ông thường dùng ảnh đàn ông mặc quân phục Mỹ; theo DOJ, ông dùng ảnh lấy cắp từ tài khoản bị hack của đàn ông thật)".

Ghi chú không bắt buộc (không tính MH): G1 §0 ngoặc "N2 tr. 8 có tổ hợp như vậy" → "tr. 8: tuổi + hoàn cảnh; bang ở tr. 2"; G2 nhịp 5 giữ "affecting" khi viết lời EN; G3 "tống tiền liên bang" → "tống tiền liên tiểu bang (interstate extortion)"; G4 L2 câu "Cô đơn sau mất mát…" gắn nhãn lời của kênh; đầu tệp ghi "N6–N7 mới mở" trong khi §7 có cả N8.
