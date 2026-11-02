# Kiểm độc lập vòng 7 — dàn truyện `theranos-holmes` (tập 4)

> Đối tượng: `docs/dan-truyen/theranos-holmes.md` (bản trên đĩa, 141 dòng). Kiểm ngày 02/11/2026, tác tử kiểm độc lập.
> Đã đọc trước: `docs/HIEN-CHUONG.md` §3 (luật 1–8). **Không** đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài tệp này), `docs/kho-de-tai/kiem/**`, lịch sử git.
> Ký hiệu: **K** = khớp nguồn/tầng · **MH** = mơ hồ / thiếu nguồn-trang / mạnh hơn nguồn một chút, nên sửa · **S** = sai · **KKĐ** = không kiểm được trong phạm vi lệnh.
> Không sửa dàn truyện, không commit. Chi 0 USD; không gọi API trả tiền; không tải sec.gov.

## Nguồn đã mở

| Mã | Đường mở | Kết quả |
|---|---|---|
| N1 | `ho-so/theranos-holmes/ca9-opinion-2025-02-24-22-10312.pdf` | SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` **khớp**; 54 trang; số trang in = số trang PDF (kiểm tr. 2, 7–17, 31, 32, 53, 54). Đọc `pdftotext -layout -f P -l P`: tr. 1, 2, 7–17, 31, 32, 53, 54 |
| N2 | bản phiên chính `scratchpad/src/sec/lr-24069.html` | đọc toàn văn phần nội dung |
| N3 | bản phiên chính `scratchpad/src/sec/2018-41.html` | đọc toàn văn phần nội dung |
| N4–N8 | `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=Theranos&pagesize=50` | 02/11/2026, HTTP 200, 6 kết quả (khớp §7); đọc toàn văn N4, N5, N6, N7, N8 |

## Kết luận

Dàn truyện **đạt về chất** ở cả bốn nhóm điểm được giao: không câu nào nâng tầng; phán quyết đối với Holmes được tách đúng bốn phần; Theranos, Inc. không bị đặt vào câu "not accused"; cấu trúc "bảy câu kiểm = sáu câu từ bảy nhóm + một câu của kênh" nhất quán ở mọi chỗ. **Không có S.** Có **5 MH** (một trong đó lặp ở 5 vị trí), đều sửa được bằng chữ, không đổi cấu trúc tập.

**Tổng đếm: 35 dòng kiểm — 26 K · 9 MH (= 5 lỗi MH riêng: MH-1 lặp ở 5 dòng; MH-2…MH-5 mỗi lỗi 1 dòng) · 0 S · 0 KKĐ trong bảng; ngoài bảng 1 KKĐ (trạng thái BOP/ân xá, ngoài phạm vi nguồn).**

## Phần A — bảng chấm

### A1. Câu "not accused of wrongdoing" (chủ thể, nguồn, vị trí theo quy tắc §0)

Căn cứ chung: N4 — đại bồi thẩm truy tố **chỉ** Holmes và Balwani ("A federal grand jury has indicted Elizabeth A. Holmes and Ramesh 'Sunny' Balwani"); N1 tr. 8 — cáo trạng "charged Holmes and Balwani (collectively, 'Defendants')"; N2/N3 — SEC kiện **Theranos Inc.**, Holmes, Balwani ("charged Silicon Valley-based private company Theranos Inc., its founder and CEO Elizabeth Holmes, and its former President…"); "Theranos and Holmes neither admitted nor denied the allegations".

| # | Vị trí | Câu / điểm | Đối chiếu | Kết quả |
|---|---|---|---|---|
| 1 | Logline VI/EN | Không chứa câu "not accused" | Logline là tóm tắt nội bộ, không phải lời đọc; §0 không đặt câu kèm ở logline | K (nếu logline được dùng làm mô tả video thì nêu nhà đầu tư mà không câu kèm — ghi chú, không tính lỗi) |
| 2 | H5 | "The investors in this story were not accused of wrongdoing; the court treated twelve of them as victims." | Vế 2: N1 tr. 16 ("the twelve investors … were 'victims' under the … MVRA") — K. Vế 1: nguồn chỉ chứng minh không bị cáo buộc **trong các vụ này** (N4 hình sự; N2 SEC). Câu không có "in these cases" → phạm vi tuyệt đối, mạnh hơn nguồn; ô nguồn chỉ ghi N4, thiếu N2 | **MH-1** |
| 3 | Nhịp 2 (Walgreens) | "Walgreens was not accused of wrongdoing in these cases; the court later treated it as a victim owed restitution." | N1 tr. 17 ("$54.5 million for two other victims, Safeway and Walgreens"); N4; N2 | K |
| 4 | Nhịp 2 (nhà đầu tư) | Như H5 | Như dòng 2 | MH-1 (lặp) |
| 5 | Nhịp 3 (câu gộp) | "These were the indictment's allegations against Holmes and Balwani; the investors, Walgreens, the drug companies and the U.S. military were not accused of wrongdoing in these cases." | Chủ thể bị cáo buộc đúng (cáo trạng chỉ Holmes, Balwani — N1 tr. 8; N4); không liệt kê Theranos vào nhóm "not accused" — đúng vì Theranos bị SEC kiện (N2) | K |
| 6 | Nhịp 4b | Như H5 | Như dòng 2 | MH-1 (lặp) |
| 7 | Nhịp 7 (hãng dược) | "The drug companies were not accused of wrongdoing in these cases; their representatives testified they did not authorize their logos on these reports." | N1 tr. 14 ("neither independently validated … nor authorized the use of their company logo"); N4; N2 | K |
| 8 | Nhịp 7 (Walgreens) | Câu mẫu Walgreens | N1 tr. 17; N4; N2 | K |
| 9 | Nhịp 8 | "The U.S. military was not accused of wrongdoing in these cases." | N4; N2 | K |
| 10 | Nhịp 9 | Câu mẫu Walgreens | N1 tr. 17; N4; N2 | K |
| 11 | Nhịp 10 | "Apart from Theranos, Holmes and Balwani, none of the other companies, investors, board members, military officers or prominent backers was accused of wrongdoing in these cases." | Loại trừ đúng cả Theranos (bị SEC kiện — N2) lẫn Holmes, Balwani (Balwani là thành viên HĐQT — N4/N8; Holmes là chủ tịch — N6, nên "other … board members" đúng). Ghi chú ô ("chỉ Holmes, Balwani bị truy tố (N4), SEC chỉ kiện Theranos, Holmes, Balwani (N2)") khớp | K |
| 12 | Nhịp 12 | Như H5 (lần nêu đầu Hồi 3) | Như dòng 2 | MH-1 (lặp) |
| 13 | Nhịp 16 | "Safeway and Walgreens were not accused of wrongdoing in these cases; the court treated them as victims." | N1 tr. 17; N4; N2 | K |
| 14 | Nhịp 18 | "Apart from Theranos, Holmes and Balwani, none of the companies, the U.S. military, the investors or the board members mentioned in this story was accused of wrongdoing in these cases." | Như dòng 11 | K |
| 15 | §0 (danh sách + quy tắc vị trí) | Walgreens/Safeway/hãng dược/quân đội: mỗi đoạn; nhà đầu tư: lần đầu mỗi hồi (H5; nhịp 2 + 3; 4b; 12) và nhịp 10, 18 | Rà vị trí: Hồi 1 — nhịp 1 không nêu nhà đầu tư, nhịp 2 là lần đầu ✓; Hồi 2 — nhịp 4 không nêu nhà đầu tư, 4b lần đầu ✓; Hồi 3 — nhịp 11 không nêu, nhịp 12 lần đầu ✓. Walgreens có câu kèm ở 2, 3, 7, 9, 16; quân đội ở 3, 8, 10 ("military officers"), 18; hãng dược ở 3, 7, 10, 18 ✓ | K |
| 16 | §5(e) | Danh sách câu mẫu | Khớp nguyên văn với các nhịp; câu mẫu nhà đầu tư mang cùng lỗi phạm vi như H5 | MH-1 (lặp) |
| 17 | §5(b) | "Theranos, Inc. (dàn xếp SEC không thừa nhận; không bị truy tố hình sự — N2, N4)" | N2/N3 ("Theranos and Holmes neither admitted nor denied"); N4 chỉ truy tố hai cá nhân | K |

### A2. Tách bạch phán quyết đối với Holmes

Căn cứ: N1 tr. 15 ("the government dismissed Count 9. The jury acquitted Holmes on the patient-related counts: conspiracy (Count 2) and wire fraud (Counts 10–12). The jury convicted Holmes of four investor-related counts … (Count 1), … (Counts 6–8). The jury hung on … C-1 investors (Counts 3–5)"); N1 tr. 8 (Counts 9–12 = "wire fraud counts involving patients"); N5/N6/N7/N8 ("One count of wire fraud relating to a Theranos patient was dismissed during the trial").

| # | Vị trí | Điểm | Đối chiếu | Kết quả |
|---|---|---|---|---|
| 18 | §0 | kết án 4 (Count 1, 6–8) / trắng án 4 (Count 2, 10–12) / treo 3 (Counts 3–5, C-1) / Count 9 rút | N1 tr. 15; N5 | K |
| 19 | Logline VI | "kết án bà 4 tội lừa nhà đầu tư, tuyên trắng án 4 tội liên quan bệnh nhân, không thống nhất được ở 3 tội" | N1 tr. 15 | K (xem MH-2 cho bản EN) |
| 20 | Logline EN + H4 | "…acquitted her on four patient counts, and deadlocked on three more." / "On four counts involving patients, the same jury acquitted her. On three more, it could not reach a verdict." | Số đúng. Nhưng "three more" đứng ngay sau "four patient counts" → người nghe dễ hiểu là **ba tội bệnh nhân nữa**; thực tế là ba tội **nhà đầu tư** C-1 (N1 tr. 15). §0 yêu cầu tách bạch, không để ám chỉ | **MH-2** |
| 21 | Nhịp 14 | Thẻ 12 ô bốn mảnh; Counts 6–8 "chuyển khoản tổng hơn 140 triệu USD" | N1 tr. 15; N5 ("wire transfers totaling more than $140 million"); N6 | K |
| 22 | Nhịp 15 — câu nối | "At her separate trial, Holmes was acquitted of the patient conspiracy count and three patient wire-fraud counts; one other patient count was dismissed." | Nội dung đúng. Ô nguồn ghi **chỉ** "(N1 tr. 15)", nhưng tr. 15 không nói Count 9 và Counts 10–12 là tội **bệnh nhân** — điều đó nằm ở N1 tr. 8 ("four wire fraud counts involving patients (Counts 9 to 12)") hoặc N5/N7/N8 ("One count of wire fraud relating to a Theranos patient was dismissed") | **MH-3** |

### A3. Cấu trúc "bảy câu kiểm"

Căn cứ: N1 tr. 10–11 liệt kê đúng bảy nhóm (A)–(G). Ánh xạ trong tệp: Kiểm 1 = (A)+(F) (nhịp 4–4b), Kiểm 2 = (C) (nhịp 5), Kiểm 3 = (B) (nhịp 6), Kiểm 4 = (G) (nhịp 7), Kiểm 5 = (E) (nhịp 8), Kiểm 6 = (D) (nhịp 9), Kiểm 7 = K (nhịp 10). Đủ 7 nhóm, 6 câu, 1 câu kênh.

| # | Vị trí | Đối chiếu | Kết quả |
|---|---|---|---|
| 23 | §0 "Góc riêng" | "sáu câu dựng từ bảy nhóm … (A) và (F) gộp trong Kiểm 1 … cộng một câu của kênh (Kiểm 7 …, nhãn K)" — nhất quán; riêng cụm "phân loại của chính cáo trạng" xem MH-4 | K (cấu trúc) |
| 24 | H5 | Thẻ "7 checks", không "7 claims" — nhất quán | K |
| 25 | Nhịp 3 | Bảy nhóm (A)–(G) đúng thứ tự và nội dung N1 tr. 10–11; "sáu câu … ((A)+(F) gộp ở Kiểm 1); Kiểm 7 là câu của kênh"; thẻ ghi "6 from the indictment's categories + 1 lesson" | K (cấu trúc) |
| 26 | Nhịp 4 | "(nhóm (A) + (F))" | K |
| 27 | Nhịp 10 | "câu của kênh, K — không phải nhóm của cáo trạng" | K |
| 28 | §3 | "sáu câu dựng từ bảy nhóm lời khai sai theo cáo trạng + một câu của kênh" | K |
| 29 | §6 | "sáu thẻ … + một thẻ câu của kênh" | K |

### A4. Nhịp 3 (cụm "alleged…"), D(4), §7 "Dùng cho", §8 ảnh tr. 15

| # | Vị trí | Đối chiếu | Kết quả |
|---|---|---|---|
| 30 | Nhịp 3 — "The indictment grouped the alleged false and misleading statements into seven categories" | "alleged … false and misleading" đúng tầng ◐ và đúng nguồn ("made materially false and misleading statements"). Nhưng N1 tr. 10–11 viết: "The Indictment alleged that … Holmes and Balwani made materially false and misleading statements to the investors, **which generally fell in the following categories**". Câu không cho biết chính cáo trạng **xếp nhóm** hay đây là tóm tắt của toà; và chữ "generally" bị bỏ. "grouped … into seven categories" và §0 "phân loại của chính cáo trạng" mạnh hơn nguồn đã mở (cáo trạng chưa mở) | **MH-4** |
| 31 | §4 D(4) | "200 triệu USD doanh thu từ Bộ Quốc phòng trong khi thiết bị chưa từng ra thực địa (N1 tr. 13)". (i) Câu "investor-victim Grossman testified that, prior to his investment," bắt đầu ở **tr. 12**, phần "$200 million in revenue from the Department of Defense" ở tr. 13 → trang đúng là **tr. 12–13** (nhịp 8 đã ghi đúng 12–13). (ii) Viết như sự việc, thiếu chủ thể lời khai: 200 triệu là điều **một nhà đầu tư khai đã được Holmes và Balwani nói**; "chưa từng ra thực địa" là lời khai của **một vị tướng** (tầng ●C, phải nói "testified") | **MH-5** |
| 32 | §7 N2 "Dùng cho: 12; câu kèm (nhịp 2, 3, 7, 8, 9, 10, 16, 18)" | Rà toàn tệp: N2 có ở nhịp 2, 3, 7, 8, 9, 10, 12, 16, 18 (+ §5(b)) — **khớp**. (Nếu sửa MH-1 thì thêm H5, 4b vào danh sách) | K |
| 33 | §7 N3 "H2, 2b, 12, L1, L3" | N3 có ở H2, 2b, 12, L1, L3, ghi chú §2 (quan chức SEC) — khớp; nội dung: "Silicon Valley-based" ✓, câu Peikin "no exemption … non-public, development-stage, or the subject of exuberant media attention" ✓, câu Choi "Innovators who seek to revolutionize…" nguyên văn ✓, 500.000 USD / 10 năm / 18,9 triệu cổ phần / voting control / "subject to court approval" ✓ | K |
| 34 | §7 N4–N8 "H3, H4, H5, 6b, 9, 10, 13–16; N4 cho câu kèm"; "6 kết quả" | API trả 6 kết quả ✓. N6 ở H3 ("was able to induce dozens of investors…") ✓, H4 (ngày) ✓, 6b ("zero revenue in 2012 and 2013 … over $100 million … nearly $1 billion") ✓, 9 ("from a few dozen to 900 … stagnating") ✓, 10 ("In its memorandum filed for the sentencing hearing" … "more than $4 billion" … bìa tạp chí) ✓, 16 (3 năm giám sát, "No fine", "ordered to surrender on April 27, 2023") ✓; N5 ở H4, 6b, 13 (28/07/2020), 14 ✓; N4 ở 13 ✓ và câu kèm ✓; N7/N8 ở 15 (07/07/2022 "guilty on all counts"; 155 tháng, 3 năm) ✓ | K |
| 35 | §8 ảnh tr. 15 | Tr. 15 thực tế: trên cùng là phần cuối "D. Scheme to Defraud Patients" (lời khai bệnh nhân: HIV, thai kỳ), rồi "Procedural History" + đoạn lý do tách phiên ("Balwani's abuse in their personal relationship"), rồi "A. Holmes's Conviction and Sentence". Hướng dẫn cắt (chỉ giữ đoạn A) đúng vị trí, loại đúng hai phần cấm (8f, luật 5); đoạn A không có tên người ngoài Holmes | K |

### Ngoài bảng — KKĐ

| # | Vị trí | Lý do |
|---|---|---|
| — | Nhịp 17, §8: trạng thái BOP (N14), trang ân xá (N9) | Ngoài phạm vi nguồn được giao; không mở lại. Không tính vào tổng (ghi để điều phối biết) — **KKĐ: 1** |

## Phần B — đọc lướt toàn tệp

Đã đối chiếu thêm (không tính vào bảng đếm vì ngoài danh sách A; đều **K**): H1 (tr. 7 nguyên văn "[O]ne tiny drop changes everything." + "vision"), H2 (tr. 7), H3 (N6, ●D có chủ thể), nhịp 1 (tr. 8–9), 2 (tr. 10), 2b (N3), 4 (tr. 10–11: 300/12, "general chemistry tests", sửa máy, QC — lời khai "at both trials"), 5 (tr. 12), 6 (tr. 12: 57/92 triệu, 15 triệu, 2 triệu/tuần, 1.944.948, 230 triệu), 7 (tr. 14, tr. 8 nguyên văn), 8 (tr. 12–13, trích ghi âm nguyên văn, chú thích 2 "phiên Holmes"), 9 (tr. 13–14), 10 (tr. 7), 11 (tr. 7–8, 11, 31 "early 2016, when the Report was received", 32 "voided all patient tests run on the Edison"), 12 (N2/N3), 13 (tr. 8, 15; N4 14/06/2018; N5 28/07/2020), 15 (tr. 15–16), 16 (tr. 15–17: 120 triệu, 135 tháng, 452 / 397 / 54,5 triệu, 05/2023), 17 (tr. 2, 8, 53–54: "in its entirety", trích nhà đầu tư nguyên văn), cú treo §3 (N6; tr. 11), §5(a)(d) (tr. 7–8 "half-truths and outright lies", "nothing more than a mirage"), L1–L3, thẻ tổng kết.

**Không phát hiện thêm câu mạnh hơn nguồn/tầng hay tự mâu thuẫn** ngoài 5 MH nêu trên. Ghi chú nhỏ (không tính lỗi): D(2), D(3) cũng viết dạng sự việc không chủ thể lời khai như D(4); nếu §4 D được đọc thành lời ở nhịp 18 thì nên áp cùng cách sửa MH-5 ("employees testified…", "an investor testified…").

## Sửa đề xuất (cho MH)

| Mã | Vị trí | Sửa đề xuất |
|---|---|---|
| MH-1 | H5, nhịp 2, 4b, 12, §5(e) | Đổi câu mẫu nhà đầu tư thành: *"The investors in this story were not accused of wrongdoing in these cases; the court treated twelve of them as victims."* Ô nguồn: N1 tr. 16; N4; **N2**. Thêm H5, 4b vào cột "Dùng cho" của N2 (§7) |
| MH-2 | Logline EN, H4 (và logline VI cho đồng bộ) | Logline EN: *"…acquitted her on four patient counts, and deadlocked on three other investor counts."* H4: *"…On three other investor counts, it could not reach a verdict."* Logline VI: "…không thống nhất được ở 3 tội lừa nhà đầu tư khác" |
| MH-3 | Nhịp 15, ô "Câu nối bắt buộc" | Nguồn đổi thành "(N1 tr. 8, 15; N5)" — tr. 8 xác định Counts 9–12 là tội bệnh nhân; N5 "One count of wire fraud relating to a Theranos patient was dismissed during the trial" |
| MH-4 | Nhịp 3 (câu EN + mô tả VI), §0 "Góc riêng" | EN: *"According to the appeals court, the indictment alleged false and misleading statements to investors that generally fell into seven categories."* VI nhịp 3: "theo toà phúc thẩm, các lời khai sai mà cáo trạng cáo buộc nhìn chung thuộc bảy nhóm". §0: "bảy nhóm theo cách toà phúc thẩm tóm tắt cáo buộc của cáo trạng (N1 tr. 10–11)" thay cho "phân loại của chính cáo trạng". Thẻ nhịp 3 có thể giữ "6 from the indictment's categories" → nên đổi "6 from the categories of alleged statements" |
| MH-5 | §4 D(4) | "(4) **Hợp đồng chính phủ/quân đội không kiểm được** — một nhà đầu tư khai được nói Theranos đã có 200 triệu USD doanh thu từ Bộ Quốc phòng, trong khi một vị tướng khai thiết bị chưa từng được quân đội đưa ra thực địa (N1 tr. 12–13, ●C) — nhịp 8" |
