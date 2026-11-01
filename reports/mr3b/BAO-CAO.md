# BÁO CÁO MR-3b — Sửa lời tập 1 "1inmm-horwitz" trước G1

> Phiên Claude Code, 01/11/2026. Nhánh `claude/compassionate-faraday-ll0nya` từ `main` @ `e987477`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD**: không gọi API trả tiền, không sinh giọng, hình hay nhạc, không gặp 402. Mạng chỉ dùng để tác tử kiểm mở nguồn công khai (API thông cáo DOJ, các trang FINRA, IAPD, FTC). `git lfs pull` 6 PDF hồ sơ tập 1 để đọc (SHA-256 khớp NGUON.md). Không merge, không xoá nhánh, không force-push.
> Căn cứ: CLAUDE.md, HIEN-CHUONG v2, NHAT-KY mục MR-3 22:48 và 22:58, `docs/tap01-1inmm/*`.

## 1. Kết quả theo từng việc của lệnh

| # | Việc | Kết quả |
|---|---|---|
| 1 | Câu KBCB HBO/Netflix | **S008 (P01) và S045 (P08) vẫn đọc thành lời.** **S019 (P03), S033 (P06), S072 (P15), S076 (P16)** thêm `"doc": false` và `"chu"` (thẻ chữ, tầng KBCB). Các câu này không thu âm và không tính vào số từ hay ký tự TTS; mỗi thẻ giữ trên hình 6 s, không có lời đè. Máy kiểm **K4 sửa** thành: mọi đoạn có tên HBO/Netflix (trong lời đọc hoặc chữ trên hình) phải có câu KBCB **đọc HOẶC hiện chữ**. Thêm **K8**: câu `doc: false` phải có `chu`, và thẻ KBCB phải có đủ "HBO", "Netflix", "not accused". Đã chạy thử 3 trường hợp hỏng (xoá `chu`, xoá KBCB P15, thẻ thiếu chữ): máy bắt đúng cả 3 |
| 2 | Hồi 2 (P11, P16) | **Lời P11, P16 không đổi chữ nào** (S076 chỉ chuyển sang dạng thẻ theo việc 1). `SHOT.md` §4 thêm **dòng thời gian đếm ngược tới "April 9"**, chỉ dùng ngày có trong hồ sơ đã mở: ~Mar. 12, 2021 (N1 tr. 13 ¶76, "on or about") còn 28 ngày → Apr. 5 SEC nộp đơn còn 4 ngày → Apr. 6 phong toả tài sản và bắt giữ còn 3 ngày, bộ đếm dừng. Ô April 9 để trống: hồ sơ đã mở không nói gì về ngày đó. Thêm **ghi chú nhạc tăng dần P15–P17**: 3 lớp từ −24 lên −18 dB, cắt lặng 1,5 s ở S080, về −26 dB ở P18. Hàng shot 33–36 ghi theo |
| 3 | P21 tổng kết bài học | Viết lại thành 13 câu (S093–S105): mở đầu "3 lessons, 5 red flags, 1 rule"; **(a)** 3 bài học: S094 đổi lãi kỳ ngắn ra lãi năm (kỳ phiếu 6 tháng 35 % ≈ 70 %/năm), S095 trả đều không chứng minh khoản đầu tư có thật, có "Ponzi" gắn chủ thể Justice Department, S096 biết ai ở phía bên kia hợp đồng (nhà đầu tư con không có hợp đồng trực tiếp); **(b)** 5 dấu hiệu S097–S101; **(c)** 1 nguyên tắc S102 "verify independently before any money moves…"; **(d)** nơi kiểm và nơi báo cáo S103 (BrokerCheck, IAPD) và S104 (SEC tip, ReportFraud FTC); câu nguồn S105. Mỗi ý là một câu, gắn chi tiết đã nêu trong tập, không thêm sự việc mới; câu nhắc sự việc giữ đúng tầng (●T ×5, ◐ ×3). `SHOT.md` hàng 40–44 và **§3 thẻ tổng kết B1 (3 + 5 + 1 dòng)** |
| 4 | PHUONG-AN.md | §0 "ĐÃ CHỌN": **T1**, **B1**, **giọng kênh lost-places** `voice_id kozBJGqBNTqfBBClLNCL` (Voice Design, `eleven_v4`, không thử giọng lại; M-c kiểm voice_id bằng GET miễn phí, không được thì DỪNG), **thumbnail do chủ dự án làm** theo `phat-hanh/THUMBNAIL-RULES.txt`, kèm dòng RIGHTS |
| 5 | LOI.md, UOC-CHI.md | `LOI.md` dựng lại bằng máy (có thêm cột "Đọc"). `UOC-CHI.md` tính lại theo ký tự mới, bỏ khoản thử giọng; **trần đề xuất giữ nguyên** vì mọi mức đều giảm (§5 của tệp) |
| 6 | Kiểm lời độc lập | 4 vòng, mỗi vòng một tác tử mới. Kết thúc với **0 sai, 0 mạnh hơn** (§3) |

## 2. Số đo (máy)

| | MR-3 | **MR-3b** |
|---|---|---|
| Số câu (đọc / chỉ chữ) | 102 / 0 | **105 / 101 đọc, 4 chữ** |
| Số từ đọc | 2.049 | **2.005** (P21: 253 → 285) |
| Ký tự gửi TTS/lượt | 12.511 | **12.252** |
| Thời lượng (`scripts/mr3/shot_tg.py`, 145 từ/phút + nghỉ + thẻ + nguồn kết) | ≈ 16 phút | **≈ 16:13**; ở 140 từ/phút ≈ 16,7 phút. **≤ 17 phút: đạt** |
| Tầng | CHUNG 22 · KBCB 6 · ●T 30 · ◐ 29 … | CHUNG 18 · KBCB 6 · MH 2 · NB 2 · TT 6 · ● 5 · ●T 35 · ◐ 31 |
| Kiểm máy | K1–K7 ĐẠT | **K1–K8 ĐẠT** |
| ElevenLabs ký tự tính, mức giữa (hệ số 0,44) | ≈ 11.950 | **≈ 11.190** |
| Veo | 16 khe | 16 khe (không đổi) |

Công cụ mới: `scripts/mr3/shot_tg.py` tính lại cột thời điểm của `SHOT.md` từ `loi.json` (0 USD).

## 3. Kiểm lời độc lập (`docs/tap01-1inmm/kiem/mr3b.md`)

| Vòng | Phạm vi | Phát hiện | Sửa |
|---|---|---|---|
| 1 | KBCB + S093–S105 | KBCB vế "not accused of any wrongdoing" **MH nhẹ**. N2, N3 trả 403 nên vế này chỉ đứng được qua danh sách bị đơn/bị cáo. S099 "the collateral" **MH nhẹ**. S104 vế FTC "investment fraud" và S105 "every fact" **KKĐ**. S094, S101 có góp ý | Cả 6 chỗ KBCB thành "…not accused of wrongdoing **in these cases**…", thêm nguồn đã mở N1 tr. 1, **N1 tr. 13 ¶78**, N6 tr. 1. S094 "a … listed in", "roughly". S099 "collateral papers". S101 bỏ "sudden". S104 tách vế SEC và FTC. S105 "The case facts…" |
| 2 | 6 câu đã sửa | KBCB, S094, S099, S105 **K**. S101 "smooth" không có trong plea. S104 vế SEC **KKĐ** (N18 trả 403) | S101 bỏ "smooth payments" |
| 3 | S101 | "blamed on **a partner**" nghiêng MH: dễ hiểu các nền tảng là đối tác thật (luật 8e) | "blamed on **someone else**"; dòng 5 thẻ tổng kết đổi theo |
| 4 | S101 | **K** | — |

**Cuối cùng: sai 0, mạnh hơn 0.** Mọi câu đổi/mới đúng tầng. Không câu nào "làm theo được ngay". Lưu ý trung thực:
- Vế SEC của S104 dựa N18. Tác tử không mở được N18 (403 với curl thường, vì lệnh này không cấp UA khai báo của kênh). N18 đã mở HTTP 200 ở MR-3 (NGUON.md §1).
- N2, N3 cũng 403 ở MR-3b. NGUON.md §3 đã ghi việc này. **Phải mở lại N2, N3, N18 trước ngày đăng.**
- Gợi ý không bắt buộc ở vòng 4 (thêm vế "which he had not even been in contact with" vào S101) **không áp**, để giữ câu ngắn.
- Câu S008, S045 (đọc) cũng đổi chữ ("in these cases") cho khớp thẻ. Đây là thay đổi lời so với MR-3, đã qua kiểm vòng 2.

## 4. Preflight, commit
`bash tools/preflight.sh` chạy riêng, không qua pipe, trước mỗi commit; `--range origin/main..HEAD` chạy trước mỗi lần đẩy. Tất cả **ĐẠT, mã thoát 0**. Không dùng `--no-verify`. Có 2 commit trung gian, đẩy theo yêu cầu của hook dừng phiên trong lúc chờ kiểm vòng 2–4, cộng commit cuối. (`origin/main` trong bản clone chỉ trỏ `78637c1`, nên range quét 89 tệp; vẫn ĐẠT.)

## 5. Cần điều phối / chủ dự án
1. Rà MR-3b, sau đó chốt **G1**: (a) đề tài + bảng tầng, (b) lời 105 câu `LOI.md`, (c) trần (giữ như MR-3: M-c 9,50 USD + 16.000 ký tự tính; M-e 1,60 USD + 3.000).
2. Duyệt việc S008, S045 đổi chữ ("in these cases").
3. Trước M-c: đọc `/api/v1/credits` (quỹ chung ~40 USD); kiểm voice_id `kozBJGqBNTqfBBClLNCL` (GET miễn phí). Trước ngày đăng: mở lại N2, N3, N18 bằng UA khai báo của kênh; kiểm trạng thái vụ (docket, giảm án).

**DỪNG: chờ rà.**
