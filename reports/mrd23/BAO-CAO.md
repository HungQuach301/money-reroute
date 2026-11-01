# BÁO CÁO MR-D23 — Dàn truyện tập 2 (`irs-callcenter-patel`) và tập 3 (`romance-sunmola`)

> Phiên Claude Code, 01/11/2026. Nhánh `ccr-f54cf043-76wk5p` từ `main` @ `0ba8782`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD** — không gọi API trả tiền, không sinh giọng/hình, không 402. Chỉ đọc hồ sơ công khai: 2 PDF trong repo (SHA-256 khớp kho §8), API thông cáo chính thức của DOJ, trang công khai IRS / IC3 / FTC / TIGTA. Không merge, không xoá nhánh, không force-push.
> **UA khai báo cho sec.gov: không dùng tới** — cả hai vụ không có nguồn sec.gov. Địa chỉ liên hệ không xuất hiện trong request, tệp, commit hay lệnh cho tác tử con.
> Preflight chạy riêng trước mỗi commit và `--range origin/main..HEAD` trước mỗi lần đẩy; chỉ commit/đẩy khi mã thoát = 0.

## 1. Sản phẩm
| Tệp | Nội dung |
|---|---|
| `docs/dan-truyen/irs-callcenter-patel.md` | Logline VI/EN; móc câu 30 s (H1–H6, mỗi câu một tầng); bảng 18 nhịp (sự việc, nguồn + trang/đoạn, tầng, hình, rà luật 8); khuôn tập + cú treo; bài học L1–L3 + 5 dấu hiệu + nguyên tắc + **thẻ tổng kết cuối tập**; rà luật 8/luật 5; ước chi; nguồn mới mở; việc trước khi chốt lời |
| `docs/dan-truyen/romance-sunmola.md` | Như trên, bảng 15 nhịp; thêm §0 giới hạn riêng (§5 tình dục, nhận diện nạn nhân) |
| `docs/dan-truyen/kiem/irs-callcenter-patel-vong{1,2,3}.md`, `romance-sunmola-vong{1,2,3}.md`, `vong4-hai-vu.md`, `vong5-dong-sua.md` | Biên bản kiểm độc lập |

Quy ước tầng riêng trong hai tệp: Patel **●T** = điều Patel thừa nhận **theo thông cáo DOJ** (plea agreement chưa mở được → lời luôn "According to the Justice Department…"), **●N** = nhóm 24 bị cáo ở Mỹ đã kết án (không tên). Sunmola **●C** = điều toà phúc thẩm mô tả/giữ nguyên (N2), **◐D** = lời DOJ trong thông cáo ("prosecutors said…").

## 2. Tóm tắt hai vụ
| | **Tập 2 — Patel (mạo danh IRS/USCIS)** | **Tập 3 — Sunmola (lừa tình)** |
|---|---|---|
| Trụ | Mạo danh & lừa đảo công nghệ | Lừa tình (nạn nhân người lớn) |
| Nhân vật trung tâm | Hitesh Madhubhai Patel — **●** nhận tội 09/01/2020 (toà chấp nhận), 20 năm tù 30/11/2020 (N4, N5) | Olayinka Ilumsa Sunmola — **●** nhận cả 8 tội ngày thứ ba của phiên xử, không thoả thuận; 324 tháng; 7th Cir. AFFIRM 16/04/2018 (N2 tr. 1, 3, 5, 18) |
| Logline EN (nháp) | *According to the Justice Department, callers posing as the IRS threatened people with arrest if they didn't pay — and the calls came from India. The IRS had nothing to do with it. According to the Justice Department, a man admitted operating and funding several of those call centers; he was sentenced to 20 years in U.S. federal prison.* | *He told some of the women he was an American soldier or Army officer serving overseas. He was actually running an online romance scheme from South Africa. A federal judge sentenced him to 27 years.* |
| Móc câu | Điện thoại sáng, không lời; lời doạ tóm tắt ở ngôi thứ ba; câu IRS/USCIS không liên quan; 20 năm tù; câu hỏi "cuộc gọi ở Ấn Độ thành tiền mặt ở Mỹ thế nào" | Hai vai giả (lính mắc kẹt / đại tá); câu quân đội Mỹ không liên quan; "Prince Charming" qua chủ thể DOJ; 324 tháng; lời thẩm phán bằng chữ (bản N2 tr. 17) |
| Bước ngoặt có hồ sơ | (1) dây chuyền có phân công (N1 tr. 4–6); (2) phía Mỹ sụp: 24 bị cáo bị tuyên án ở TX/AZ/GA (N3); (3) bị bắt ở Singapore 9/2018, dẫn độ 4/2019 (N4 đ.9) | (1) lời xin cho "nhiệm vụ" (N2 tr. 10); (2) một tổ chức, Sunmola cầm đầu (N2 tr. 11–12); (3) nhận tội giữa phiên xử (N2 tr. 3) |
| Khuôn | **1 tập ~13 phút.** P2 (chuyến bay → án) không có bài học riêng → không đạt 0b | **1 tập ~15 phút.** P2 (bắt → án → phúc thẩm) bài học riêng quá mỏng → không đạt 0b |
| Bài học hiểu biết | L1 cuộc gọi là mặt tiền của một dây chuyền (trong vụ này); L2 vì sao đòi thẻ/chuyển tiền — rửa tiền ở mức khái niệm (đưa vào → phân lớp, ghi rõ là khung của kênh); L3 IRS thật liên hệ thế nào (IRS FS-2017-7) | L1 lừa tình có thể là một tổ chức; L2 kẻ gian chọn người theo hoàn cảnh (lời toà); L3 thiệt hại lớn hơn con số (tăng nặng tâm lý; ước thấp theo điều tra viên) |
| 5 dấu hiệu | Doạ bắt/trục xuất · đòi trả ngay · đòi phương thức cụ thể (thẻ trả trước, thẻ quà tặng, chuyển tiền) · gọi lại nhiều lần · vay/trợ cấp đòi phí trước | Nói đang làm "nhiệm vụ" ở nước ngoài · xin tiền/đồ điện tử · gửi cho người thứ ba · khẩn cấp nối tiếp · ảnh hồ sơ có thể của người khác |
| Tổng kết cuối tập | Thẻ tổng kết EN: 3 ý + 5 dấu hiệu + "Hang up. Look up the agency yourself. Report it." (TIGTA, FTC) | Thẻ tổng kết EN: 3 ý + 5 dấu hiệu + "Never send money to someone you've only met online. Report it." (IC3, FTC); **không** nhắc nhánh ảnh |
| Ước chi sơ bộ (đơn giá QUY-TRINH §6, **chưa đo trên MR**) | **≈ 6,9 – 14,8 USD** + ≈ 7.500 – 11.600 ký tự ElevenLabs | **≈ 7,9 – 16,1 USD** + ≈ 8.300 – 12.800 ký tự ElevenLabs |

Hai tập liền sau tập 1 (Ponzi) thuộc hai trụ khác nhau và khác trụ tập 1 — đạt QUY-TRINH §4b.

## 3. Áp các yêu cầu riêng của lệnh
**Patel — không dựng lời gọi chép dùng được; thương hiệu/cơ quan bị mạo danh kèm câu không liên quan**
- Không câu thoại của "người gọi", không chữ kịch bản trên màn hình, không số điện thoại; H1 chỉ là điện thoại sáng "Unknown". Lời doạ tóm tắt ở ngôi thứ ba, mức khái niệm.
- IRS, USCIS (H3, logline) và cơ quan thuế Canada/Úc (nhịp 3b) đều kèm câu không liên quan; không logo/con dấu. Không nêu: tên d.b.a. trùng thương hiệu lớn trong cáo trạng (N1 tr. 1), tên thương hiệu thẻ quà tặng (N3 đ.14), tên ứng dụng nhắn tin (N4 đ.6).
- Không nêu tên bị cáo/call center ở Ấn Độ chưa xử, **trừ HGLOBAL** (nằm trong lời nhận tội theo DOJ, N4 đ.6) — mỗi lần nêu kèm câu ◐ gắn mốc (7/2018 chưa ra hầu toà, N3 đ.15; 11/2020 "pending for other India-based defendants", N5 đ.12).
- Bỏ lời đồng bị cáo về "hối lộ" (N4 đ.8 — lời kể, chưa toà nào kết luận). Bỏ thành phố nạn nhân (giữ tuổi + số tiền theo cáo trạng, ◐).
- 24 bị cáo ở Mỹ: chỉ theo nhóm (22 Houston, 1 Atlanta, 1 Phoenix — N3).

**Sunmola — nhánh đe doạ ảnh riêng tư: một câu khái niệm; nạn nhân không nhận diện được**
- Nội dung tới người xem có **đúng một câu** (nhịp 6): *"With at least one woman, it went further: he threatened to expose private images."* — thẻ chữ tối, không cảnh, không minh hoạ; không nối với tội danh; không lặp ở bài học, dấu hiệu, thẻ tổng kết (kiểm vòng 1–5 đếm và xác nhận). Số "ít nhất một" theo N2 tr. 2 (vòng 3 bắt lỗi số nhiều).
- Không tên nạn nhân, không ghép tuổi + hoàn cảnh (N2 tr. 8) + bang (N2 tr. 2), không trích lời nạn nhân, không số tiền từng người, không ý nghĩ tự sát, không chi tiết "váy cưới"; nhân vật minh hoạ là nhân vật tổng hợp không mặt.
- Nạn nhân người lớn: N2 tr. 2, 8 ("middle-aged women"); không có dấu hiệu vị thành niên trong N1, N2.
- Không tên giả bị cáo dùng, không tên trang hẹn hò, dịch vụ chuyển tiền, hãng máy tính; không chi tiết thao tác thẻ tín dụng (N2 tr. 11).

## 4. Kiểm độc lập (tác tử mới mỗi vòng, mở nguồn đúng trang; không đọc báo cáo, kết quả vòng trước, `kiem/**` hay git)
| Vòng | Patel | Sunmola |
|---|---|---|
| 1 (toàn tệp, bản nháp) | 39 dòng: **30 K · 8 MH · 1 S · 0 KKĐ** | 59 dòng: **47 K · 10 MH · 1 S · 1 KKĐ** |
| 2 (toàn tệp) | 53 dòng: 41 K · 11 MH · 1 S · 0 KKĐ | 73 dòng: 68 K · 2 MH · 1 S · 2 KKĐ |
| 3 (toàn tệp) | 40 dòng: 32 K · 8 MH · **0 S** · 0 KKĐ | 88 dòng: 83 K · 4 MH · **0 S** · 1 KKĐ |
| 4 (toàn tệp, một tác tử cho cả hai) | 42 dòng: 40 K · **2 MH** · 0 S · 0 KKĐ | 41 dòng: 40 K · **1 MH** · 0 S · 0 KKĐ |
| 5 (12 dòng sửa + đọc lướt toàn bộ) | 11 K · 1 MH · 0 S (+1 MH cùng gốc phát hiện thêm) | (gộp trong 12 mục) 0 MH · 0 S |

Lỗi đáng kể đã sửa:
- **S (Patel v1):** "24 bị cáo bị tuyên án ở Houston" → 22 Houston / 1 Atlanta / 1 Phoenix (phiên tự mở lại N3 xác nhận). **S (Sunmola v1):** "hai lần vượt khung vì tổn hại tâm lý" → một vì tổn hại tâm lý, một vì cố ý gây tổn hại không cần thiết (N2 tr. 4); hai lần này không nằm trong các điểm kháng cáo. **S (Patel v2):** thẻ tổng kết dùng "the scammers" cho cả nhóm chưa kết án (8d) → bỏ. **S (Sunmola v2):** ghi chú nội bộ dẫn N2 cho ý nghĩ tự sát → sửa dẫn nguồn.
- **Tầng/chủ thể:** mọi câu ●T của Patel thêm "According to the Justice Department"; tách vế cáo trạng ("immediately") khỏi câu ●T; HGLOBAL không suy trạng thái sau 7/2018; Sunmola: "lấy phần lớn hơn" chỉ là bằng chứng "suggesting"; số 220.000 USD (lời công tố được toà ghi) bỏ; ảnh quân phục (toà) tách khỏi ảnh lấy cắp (DOJ).
- **Suy diễn:** ngày bay sang Singapore (nguồn chỉ có tháng bị bắt); "Houston" ở câu tuyên án; bản đồ tới Houston; "hard to trace" ở thẻ tổng kết; khái quát tuyệt đối ở L1/L2; "không gặp được", "ảnh quá chuẩn"; lời khuyên FBI chỉ về tiền (không về hàng); hai câu IRS thiếu giới hạn "immediate" / "for not paying".
- Không vòng nào thấy: lời gọi dựng lại, hướng dẫn làm theo được, nạn nhân nhận diện được, vi phạm §5.

**Trạng thái cuối:** sau vòng 4 không còn S ở cả hai vụ. 2 MH cuối của vòng 5 (Patel thẻ tổng kết ý 3 và L3) đã sửa bằng cách **thêm nguyên văn giới hạn của nguồn** ("for not paying" / "vì không trả tiền"); phiên đối chiếu lại chuỗi này trong N9 (có). **Hai dòng này chưa được tác tử chấm lại** — điều phối có thể kiểm nhanh. Cùng lượt sửa, áp thêm 2 gợi ý không bắt buộc của vòng 5 ("nhiều" → "một số" call center, sát "several"; câu ◐ HGLOBAL "like every defendant who has not been convicted, it is presumed innocent" thay thì hiện tại trần).
KKĐ còn lại (không dùng làm nguồn câu nào): trích dẫn reporter "887 F.3d 830" (Sunmola §8 — tạm dùng "No. 17-1299 (7th Cir. Apr. 16, 2018)"); hai trang FTC/FBI 403.

## 5. Nguồn đã mở ở MR-D23
- Patel: N1 cáo trạng thay thế (PDF quét, đọc ảnh tr. 1, 3–7; SHA-256 `04fb7cb3…2bdf` khớp); N2–N5 thông cáo DOJ 16-1257, 18-961, 20-19, 20-1294 (API chính thức, HTTP 200); **mới:** N9 IRS FS-2017-7, N10 ReportFraud.ftc.gov, N11 TIGTA (HTTP 200).
- Sunmola: N2 opinion 7th Cir. (SHA-256 `cc362fa0…953b` khớp, 18 tr.); N1 thông cáo DOJ S.D. Ill. (API, HTTP 200); **mới:** N6 IC3 PSA I-080519-PSA, N7 ic3.gov, N8 ReportFraud.ftc.gov (HTTP 200).
- **Chưa mở được (không vượt rào, không dùng):** consumer.ftc.gov (romance scams; government imposter scams) — HTTP 403; fbi.gov romance scams — 403; uscis.gov common scams — 403. Không đổi UA, không bản lưu.
- Vòng 3 Patel: tác tử mở thêm 2 trang ân xá/giảm án Trump 2017–2021 của Pardon Attorney: 0 kết quả "Hitesh/Hinglaj/Patel" liên quan.

## 6. Việc còn mở trước khi viết lời (đã ghi §8 mỗi tệp)
- Luật 4: kiểm lại BOP, kháng cáo, ân xá ngày chốt lời; Patel: trạng thái bị cáo ở Ấn Độ (giữ mốc 7/2018 và 11/2020 nếu không có nguồn mới).
- Patel: tìm plea agreement/judgment qua đường chính thức miễn phí (chưa có); tới khi có, giữ "according to the Justice Department".
- Sunmola: đối chiếu "887 F.3d 830"; cáo trạng/judgment S.D. Ill. chưa mở được (PACER cấm).
- Ảnh trang hồ sơ không được dùng: Patel N1 tr. 1 (d.b.a.) và tr. 7 (bảng tên bị cáo chưa xử), ảnh chụp thông cáo N2 đ.11–12 (có thành phố); Sunmola N2 tr. 2 và tr. 8.
- Phiên kịch bản: N3 đ.14 và N1 tr. 4–6 ¶2(a), (e), (f) của Patel có trình tự thao tác thẻ — không chép sang lời hay hình.

## 7. Cần chủ dự án quyết
1. Duyệt dàn truyện hai vụ (QUY-TRINH §3 mục 0) và khuôn **1 tập** mỗi vụ.
2. Sunmola: câu duy nhất về ảnh riêng tư (nhịp 6) giữ như hiện tại, hay **bỏ hẳn** nhánh này (kho đề tài từng đề xuất phương án bỏ; tập vẫn đủ truyện và bài học không có nó).
3. Patel: chấp nhận nêu tên **HGLOBAL** kèm câu ◐, hay bỏ tên (nói "one of the call centers he admitted operating").
4. Thứ tự tập 2/3 (điều phối đã trình thứ tự chốt riêng).

**DỪNG** — chờ điều phối rà.
