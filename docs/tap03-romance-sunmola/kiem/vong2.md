# KIỂM LỜI ĐỘC LẬP — VÒNG 2 · Tập 3 "Prince Charming" / Sunmola

- **Thời điểm:** 01/11/2026, 23:31–23:40 UTC.
- **Người chấm:** tác tử kiểm lời độc lập (vòng 2). Không đọc `docs/dan-truyen/*`, `docs/kho-de-tai/*`, `reports/*`, `kiem/vong1.md`.
- **Tài liệu chấm:** `docs/tap03-romance-sunmola/loi.json` (79 câu, 79 id khác nhau), `docs/tap03-romance-sunmola/SHOT.md`. Đối chiếu `docs/HIEN-CHUONG.md` §1, §3 (luật 1–8), §4, §5 và `NGUON.md`.
- **Luật đã giữ:** không vượt rào, curl mặc định (không UA tuỳ chỉnh, không thông tin cá nhân), không gọi API trả tiền, không sửa `loi.json`, không commit. Tệp tải về để trong thư mục tạm riêng (mktemp -d trong scratchpad); Python đọc tệp chạy `-I`.

## 1. Nguồn đã mở

| Mã | Đường | Kết quả | SHA-256 |
|---|---|---|---|
| N2 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf`, `pdftotext -layout -f N -l N`, N = 1…18 | đọc đủ 18 trang; số trang in đầu trang trùng số trang PDF | `cc362fa04d95dd71c5af59f50a3f2e6ab4b0393a9c65f54754e7ab710959953b` (khớp NGUON.md) |
| N1 | `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=Prince Charming` (API chính thức, curl mặc định) | HTTP 200, 1 kết quả, url `…/usao-sdil/pr/prince-charming-behind-bars-nigerian-romance-scammer-nets-27-year-prison-sentence`, date 1486036800 (02/02/2017) | phản hồi `51add97e…f75ba` (khác SHA tệp repo — phản hồi API có thể đổi trường phụ; nội dung body dùng để chấm khớp các câu dẫn) |
| N6 | `https://www.ic3.gov/PSA/2019/PSA190805` (curl mặc định) | HTTP 200; Alert I-080519-PSA, 05/08/2019 | `90837bed…af978b3` (khác SHA NGUON.md `b40f7ca1…` — trang HTML động; các câu trích N6 trong lời đều tìm thấy nguyên văn) |
| N3, N7, N8 | — | **không mở lại** ở vòng này (ngoài phạm vi 8 câu) | — |

## 2. Bảng chấm 8 câu được giao

| id | Kết quả | Tầng đúng? | Làm theo được ngay? | Trích nguồn + trang | Đề xuất sửa |
|---|---|---|---|---|---|
| S003 | **KHỚP** | ●C — đúng (có chủ thể "the court said", "The court found") | Không | N2 tr. 10: "In other instances, Sunmola held himself out as a colonel in the U.S. Army deployed to South Africa, telling his victims he needed them to purchase and ship computer equipment to him to help him finish his assignments." · "Sunmola clearly misrepresented to his victims that he was acting on behalf of, and their contributions were going towards, the U.S. military." | Không bắt buộc. Tuỳ chọn cho sát hơn: "The court found he had misrepresented that he was acting on behalf of the U.S. military." |
| S004 | **KHỚP** | KBCB — đúng; câu không liên quan bắt buộc (luật 8e), đọc thành lời, cùng đoạn P00 với S002–S003 | Không | N2 tr. 10 ("misrepresented … that he was acting on behalf of … the U.S. military") — toà xác định lời tự nhận là sai, đủ đỡ câu tách bạch | — |
| S007 | **KHỚP** | ● — đúng | Không | N2 tr. 4: "On February 2, 2017, the district court held the second half of the sentencing hearing"; tr. 5: "the judge sentenced Sunmola to 324 months' imprisonment"; tr. 1: "sentenced Sunmola to 324 months". N1 (đoạn "Olayinka Ilumsa Sunmola, 33, of Lagos…"): "sentenced this morning to serve 324 months behind bars"; 324/12 = 27 | — |
| S008 | **KHỚP** | ●C — đúng (lời của thẩm phán qua toà phúc thẩm) | Không | N2 tr. 17: "The judge repeatedly emphasized the seriousness of the offense, describing it as "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being."" — chữ trên hình trùng nguyên văn bản N2 (N1 viết "…without laying hands…", không dùng — đúng) | — |
| S012 | **KHỚP** | ◐ — đúng (N1 là lời DOJ; vai lãnh đạo còn được N2 tr. 11–12 giữ nguyên nên không có rủi ro nâng tầng) | Không | N1 (đoạn "Olayinka Ilumsa Sunmola, 33…"): "Evidence presented in court showed that Sunmola was the ringleader of a criminal organization operating in South Africa that targeted hundreds of women across the United States" — lời đã bỏ "including many in the St. Louis area" (đúng cam_them) | Dẫn nguồn trong `nguon` ghi "Evidence presented in court showed…" là chữ đầu **câu** thứ hai của đoạn đầu, không phải chữ đầu đoạn; chấp nhận được theo quy ước "đoạn/câu" |
| S048 | **KHỚP** | ●C — đúng: lời gắn đúng chủ thể ("According to the appeals court, he testified…"), không biến ý kiến điều tra viên thành kết luận của toà | Không | N2 tr. 14: "He further testified that it was his opinion that the list was inconclusive. Through investigating Sunmola's Match.com profile, he saw that Sunmola had attempted to contact many other individuals, but he was unable to reach all of these individuals. Thus, he concluded the total calculated loss of around $1.7 million was an underestimate of the total actual loss amount." — lời đã bỏ tên trang hẹn hò và tên điều tra viên (đúng) | — |
| S063 | **MẠNH HƠN (nhẹ)** | ●C nhưng câu ghép một câu bình luận của kênh (CHUNG: "Being lonely, or grieving, is not a flaw.") với một câu toà; phần toà bị gói thành quan hệ nhân quả tuyệt đối | Không | N2 tr. 8: "Sunmola and his co-conspirators chose the women they developed relationships with, specifically targeting women they believed would be susceptible to their deceitful tactics. Many of these women had been divorced, abandoned, widowed, or ignored…"; tr. 8–9: "…seeking companionship through online dating, making them particularly susceptible…"; tr. 9: "Their prior relationships left these women unusually vulnerable…" | Toà nói **nhóm chọn** phụ nữ họ tin là dễ mắc và hoàn cảnh (của **nhiều** người) khiến họ **dễ tổn thương bất thường**; lời "the women's circumstances were **what made them targets**" quy cho mọi nạn nhân và biến hoàn cảnh thành nguyên nhân duy nhất. Đề xuất: tách hai câu — (CHUNG) "Being lonely, or grieving, is not a flaw." + (●C) "In this case, the court found that the group chose women it believed would be susceptible, and that their circumstances left them unusually vulnerable." |
| S076 | **KHỚP** | ◐ — đúng; không ghép với ảnh quân phục của toà (N2 tr. 2) | Không — lời khuyên tìm ảnh ngược là biện pháp tự bảo vệ của FBI, không phải thao tác lừa | N1 (đoạn "The U.S. Postal Inspection Service began investigating…"): "To further the conceit, he used photographs stolen from the hacked online accounts of real American men"; N6 mục "Tips To Protect Yourself": "Most cyber criminals do not use their own photographs… A reverse image search can determine if a profile picture is being used elsewhere on the internet" | — |

## 3. Lượt lướt toàn bộ 79 câu (lời + `chu`) và SHOT.md

Quét máy (regex `kiem_rieng` của `loi.json` + từ khoá bổ sung) và đọc từng câu; câu nghi ngờ đã mở N2/N1/N6 đúng trang.

### (a) Câu mạnh hơn tầng
- **S063** — như bảng §2.
- Các câu ●C còn lại đã đối chiếu N2 đúng trang, không thấy nâng tầng: S002 (tr. 10 "pretended to be an American soldier, stranded in Nigeria on a mission and in need of help"), S005/S013/S014/S020/S021/S031 (tr. 2), S022 (tr. 10), S029–S030 (tr. 11–12), S035 (tr. 4, 6–7: PSR liệt kê bảy nạn nhân), S036 (tr. 4), S038–S046 (tr. 3–4), S047 (tr. 4, 14), S049–S051 (tr. 4–5, số khớp), S054–S056 (tr. 1, 5, 10, 15–16, 18), S058 (tr. 13 "presented no documentary evidence…", tr. 15 "nit-picks at almost every dollar"), S060–S062 (tr. 8–9), S066–S067 (tr. 8, 11–12), S069 (tr. 4, 14).
- Các câu ◐ đều có "prosecutors said/according to prosecutors" và khớp N1: S006, S010, S011, S015, S018, S019, S024–S027, S032, S034, S040, S052, S053, S074, S075.
- Ghi chú nhỏ (không bắt buộc sửa): **S059** "an eight-page statement" — N2 tr. 17 viết "four sentences out of the eight-page transcript from his oral statement"; sát hơn: "in just four sentences of an eight-page transcript of his oral statement". **S067** mở bằng khái quát "these schemes choose people by their circumstances" — ý kênh rút từ một vụ, đã có N6 đỡ (S068); chấp nhận.
- Không câu nào ghép ảnh quân phục (N2 tr. 2, ●C) với ảnh lấy cắp (N1, ◐): S014 và S015 tách tầng, S015 mở bằng "Separately"; S076 chỉ dùng N1.

### (b) Nhánh ảnh riêng tư — đúng một lần
- `loi.json`: regex `dung_mot` chỉ trúng **S033** (lời + chu), `doc=false`, thẻ chữ một câu. Đối chiếu N2 tr. 2 ("threatened to post photos of a third woman") — "With at least one woman…" yếu hơn hồ sơ, không mạnh hơn. ●C đúng.
- Không câu nào khác gợi lại: S036/S037 (psychological injury, gratuitous infliction of injury, "not only financial") nói chung về tác hại, không nhắc ảnh; S038 chỉ nêu **tên tội danh** "interstate extortion" (N2 tr. 3) — chấp nhận; S014/S015/S076 "photo/picture" là ảnh đại diện hồ sơ, không phải nhánh này. Bài học, dấu hiệu, thẻ tổng kết (SHOT §3) không nhắc.
- **LỖI trong SHOT.md (dòng 7, khối "Luật áp cho mọi hàng"):** ghi "Nhánh ảnh riêng tư: **chỉ hàng 15**", nhưng thẻ S033 nằm ở **hàng 11** (P06); hàng 15 là phòng xử trống (P09 S043–S044). Đề xuất sửa "chỉ hàng 15" → "chỉ hàng 11". (Nếu máy kiểm KC đọc số hàng từ dòng này thì có thể kiểm sai hàng.)

### (c) HIEN-CHUONG §5 — nạn nhân, tự sát, giật gân
- Không tên/bang/tuổi/hoàn cảnh cá nhân của nạn nhân: không có "Georgia", "St. Louis", "55", "66", ca cụ thể của N2 tr. 8; S010 chỉ "a woman in the Southern District of Illinois" (cấp quận liên bang) — không nhận diện được. S061/S067 chỉ dùng câu khái quát của toà. Không lời nạn nhân (N1 "Retirement should be a happy time…" không dùng).
- Không chi tiết tự sát, váy cưới, "desires to die" (regex `cam_them` 0 trúng; lời thẩm phán N1 đoạn "'Conspiracy,' 'mail and wire fraud'…" không dùng).
- Không giật gân: SHOT hàng 12 và 18 dùng nhân vật tổng hợp quay lưng/ghế trống, nhãn "composite"; nhạc không còi/nức nở.

### (d) Quân đội Mỹ, tên giả, trang hẹn hò, dịch vụ chuyển tiền, điều tra viên, nhãn "scammer"
- Mỗi đoạn có nhắc quân đội đều có câu "had nothing to do": P00 (S002–S003 → S004, đọc), P02 (S014 → S017, thẻ), P04 (S022 → S023, đọc), P11 (S056 → S057, thẻ), P12 (S071 → S072, thẻ). SHOT hàng 2, 6, 8, 17, 21 có thẻ tương ứng. Ghi chú: ở P02, P11, P12 lời đọc nhắc quân đội nhưng câu không liên quan chỉ là thẻ chữ không đọc — thoả luật đoạn; nếu muốn chắc hơn cho người chỉ nghe, có thể cho một trong ba thẻ đọc thành lời (không bắt buộc).
- Không "Elias Dyess", không Match.com/MoneyGram/Western Union, không Latham/Whitty/Herndon/Stump/Reppert/Wasserman, không "boss" (0 trúng). S025 nêu "Ilumsa Sunmola" — là tên thật của bị cáo (đã ●) được dùng làm người nhận hàng theo N1; không phải tên giả mạo xưng, chấp nhận.
- Không "scam(mer)/fraudster/con man/monster" ở giọng kể và trong `chu` (0 trúng; dùng "scheme"). Tiêu đề N1 có chữ "Scammer" không xuất hiện trên hình (S006 chỉ ghi "U.S. Attorney's Office, Southern District of Illinois").

### (e) "Làm theo được ngay"
- Không câu nào cho trình tự thao tác: S029 bỏ chi tiết N2 tr. 11 (đặt hàng, tìm cửa hàng nhận hàng, mua dữ liệu thẻ giả); S024–S025/S074 nêu thủ đoạn ở mức khái niệm (gửi hàng cho "người thứ ba"), không địa chỉ, không kịch bản tin nhắn; SHOT cấm chữ chat/thư đọc được và giao diện. Các câu bảo vệ (S076 tìm ảnh ngược, S077–S078) là hướng dẫn tự vệ — được phép.

## 4. Tổng
- **8 câu được giao:** 7 KHỚP (S003, S004, S007, S008, S012, S048, S076); 1 MẠNH HƠN nhẹ (**S063**). 0 SAI.
- **Lượt lướt 79 câu:** không thêm câu MẠNH HƠN/SAI; 2 ghi chú chữ không bắt buộc (S059, S003 tuỳ chọn). Nhánh ảnh riêng tư đúng một lần (S033, thẻ, doc=false); §5, luật 8d/8e, cấm tên giả/trang hẹn hò/dịch vụ chuyển tiền/điều tra viên: đạt.
- **SHOT.md:** 1 lỗi tham chiếu — dòng 7 "chỉ hàng 15" phải là **hàng 11**.
- Chưa kiểm ở vòng này: N3 (S064), N7/N8 (S078).
