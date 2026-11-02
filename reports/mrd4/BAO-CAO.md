# BÁO CÁO MR-D4 — Dàn truyện tập 4 (`theranos-holmes`)

> Phiên Claude Code, 01–02/11/2026. Nhánh `claude/theranos-holmes-tap-4-fmz9li`. Lệnh ghi "từ main @ d485da0"; khi phiên mở, `main` đã ở `11b69dc` (commit điều phối sau d485da0, chỉ thêm 5 dòng NHAT-KY mục MR-5) → nhánh tạo từ `11b69dc`; không ảnh hưởng tệp của mốc này.
> Trần theo lệnh: **0 mọi khoản**. **Chi thật: 0 USD** — không gọi API trả tiền, không sinh giọng/hình, không 402.
> **UA khai báo cho sec.gov:** chỉ dùng trong header của các lệnh curl tới sec.gov (N2, N3, N10, N15) và investor.gov; **không** ghi vào tệp, báo cáo, commit hay lệnh cho tác tử con. Tác tử kiểm **không** nhận UA và **không** tự tải sec.gov — họ đối chiếu N2/N3 trên bản HTML phiên chính đã tải (scratchpad, ngoài repo). Quét repo: 0 dòng chứa địa chỉ liên hệ.
> Preflight chạy riêng (không qua pipe) trước mỗi commit và `--range origin/main..HEAD` trước mỗi lần đẩy; chỉ commit/đẩy khi mã thoát = 0 — 13 commit, tất cả ĐẠT. Không merge, không xoá nhánh, không force-push.

## 1. Sản phẩm
| Tệp | Nội dung |
|---|---|
| `docs/dan-truyen/theranos-holmes.md` | Ký hiệu tầng; §0 giới hạn riêng của vụ; logline VI/EN; móc câu 30 s (H1–H5); bảng 24 dòng nhịp (0–18, kể cả nhịp con 2b, 4b, 6b) có nguồn + trang + tầng + hình + rà luật 8; khuôn tập (0b) + cú treo; bài học L1–L3 + 5 dấu hiệu + nguyên tắc + thẻ tổng kết cuối tập; rà luật 8/luật 5; ước chi theo đơn giá đo thật; nguồn; việc trước khi chốt lời |
| `docs/dan-truyen/kiem/theranos-holmes-vong{1..12}.md` | 12 biên bản kiểm độc lập |

## 2. Tóm tắt dàn truyện
- **Nhân vật trung tâm:** Elizabeth Holmes — **●** (N1 tr. 15–16, 54; N5; N6). Theranos, Inc. ◐ (dàn xếp SEC không thừa nhận). Balwani ● theo bản án riêng.
- **Logline EN (nháp):** *A private company promised a lab in a drop of blood, and investors put in hundreds of millions of dollars. In 2022, a federal jury convicted its founder on four investor-fraud counts, acquitted her on four patient counts, and deadlocked on three other investor counts. This is the case, claim by claim, as a lesson in due diligence.*
- **Góc riêng "bài học thẩm định":** Hồi 2 là **bảy câu kiểm** — sáu câu dựng từ bảy nhóm lời khai sai mà toà phúc thẩm tóm tắt từ cáo trạng (N1 tr. 10–11; (A)+(F) gộp ở Kiểm 1) + một câu của kênh ("Danh tiếng có phải bằng chứng?"). Cấu trúc dựng từ hồ sơ; **không** xem hay dùng cấu trúc, lời, hình của video sẵn có.
- **Bước ngoặt có hồ sơ:** khung bảy nhóm (nhịp 3); Holmes thừa nhận tự gắn logo hãng dược lên báo cáo, các hãng khai không thẩm định/không cho phép (nhịp 7, N1 tr. 14); thanh tra CMS cuối 2015 → "immediate jeopardy" (nhịp 11); SEC 03/2018 (◐); phán quyết bốn mảnh 03/01/2022.
- **Khuôn:** **1 tập ~17 phút.** P2 (sụp – xử – phúc thẩm) có bước ngoặt nhưng bài học riêng mỏng, phụ thuộc P1 → **không đạt 0b**.
- **Bài học:** L1 cổ phần tư nhân có thể không có đường thoát (toà sơ thẩm xác định nạn nhân không bán được, phúc thẩm giữ — N1 tr. 52–53); L2 "uy tín vay mượn" không phải thẩm định; L3 "cho tôi xem" khác "kể cho tôi nghe" (kèm câu quan chức SEC 2018, N3). **5 dấu hiệu:** bảo chứng không xác nhận được với bên bảo chứng · trình diễn do người bán điều khiển · dự báo vênh xa số thực · doanh thu/quan hệ với chính phủ, quân đội không kiểm được · quan hệ "đang mở rộng" mà đối tác không xác nhận. Nơi kiểm/báo cáo: BrokerCheck, IAPD, SEC Tips, FTC ReportFraud. Thẻ tổng kết EN ở cuối §4.

## 3. Áp yêu cầu riêng của lệnh
- **Kết án 4 / trắng án 4 / treo 3, không gộp:** §0, logline, H4, nhịp 14 (thẻ 12 ô, nhãn ● chỉ ở 4 ô kết án), câu nối nhịp 15. Count 9 bị công tố rút — nói riêng, không tính là trắng án. Số phận Counts 3–5 sau phiên xử chưa có nguồn → không nói.
- **Balwani chỉ theo bản án của ông:** nhịp 15 (bồi thẩm khác, 12/12 tội, 155 tháng; N1 tr. 16; N7; N8). Phần bệnh nhân chỉ gắn với Balwani; câu nối bắt buộc nói Holmes trắng án các tội bệnh nhân. Không lý do tách phiên, không quan hệ riêng (8f).
- **Bệnh nhân/nhà đầu tư không tên:** cả nhân chứng (vị tướng, kiểm soát viên, đại diện Walgreens/hãng dược). Hãng dược không nêu tên. §8 liệt kê trang hồ sơ không được dùng làm hình.
- **Walgreens, Safeway, hãng dược, quân đội Mỹ, nhà đầu tư, thành viên HĐQT/nhân vật nổi tiếng:** câu không liên quan có giới hạn "in these cases" (nguồn: N1 tr. 8; N4 — cáo trạng chỉ nêu Holmes, Balwani; N2 — SEC chỉ kiện Theranos, Holmes, Balwani; "treated as victims" N1 tr. 16–17). Công ty/tổ chức: mỗi đoạn nêu; nhà đầu tư: lần nêu đầu mỗi hồi + nhịp 10, 18. Câu gộp luôn loại trừ Theranos.

## 4. Kiểm độc lập (tác tử mới mỗi vòng; không đọc báo cáo, biên bản cũ, git; mở nguồn đúng trang)
| Vòng | Phạm vi | Dòng | K | MH | S | KKĐ |
|---|---|---|---|---|---|---|
| 1 | toàn tệp | 87 | 71 | 8 | 4 | 4 |
| 2 | toàn tệp | 84 | 69 | 1 | 6 | 8 |
| 3 | toàn tệp | 81 | 69 | 1 | 5 | 6 |
| 4 | toàn tệp | 80 | 72 | 1 | 4 | 3 |
| 5 | toàn tệp | 87 | 78 | 0 | 3 | 6 |
| 6 | toàn tệp | 85 | 76 | 0 | 3 | 6 |
| 7 | dòng sửa + đọc lướt | 35 | 26 | 9 dòng (5 lỗi) | 0 | 0 |
| 8 | toàn tệp | 77 | 70 | 1 | 0 | 6 |
| 9 | dòng sửa + đọc lướt | 16 | 12 | 2 | 2 | 0 |
| 10 | dòng sửa + đọc lướt | 46 | 42 | 1 | 3 | 0 |
| 11 | dòng sửa (hẹp) | 22 | 19 | 0 | 3 | 0 |
| 12 | dòng sửa (hẹp) | 11 (+1 ngoài phạm vi) | 10 | **0** | 1 (+1) | 0 |

Lỗi đáng kể đã sửa:
- **Chủ thể câu "not accused":** câu gộp từng loại trừ chỉ "Holmes and Balwani" trong khi Theranos bị SEC kiện, và Balwani là thành viên HĐQT (v1, v3, v6) → "Apart from Theranos, Holmes and Balwani…". Câu tuyệt đối ("any wrongdoing", "never authorized the use of their logos") → giới hạn "in these cases", "on these reports" (v1, v7). Thiếu câu kèm ở nhịp 3, 7, 10, 18 và cho nhà đầu tư (v2, v4, v5).
- **Phán quyết:** logline bỏ vế treo (v1); "deadlocked on three more" đặt sau "patient counts" dễ hiểu là ba tội bệnh nhân (v7); câu nối nhịp 15 "four patient counts" trỏ nhầm Counts 9–12 (v5); cột tầng H4 gán ● cho cả vế trắng án/treo (v11).
- **Mạnh hơn nguồn:** "mục tiêu" → "mục tiêu bà tuyên bố" (v2); "bà trình diện 27/04/2023" → "bị lệnh trình diện" (v2); "trực thăng cứu thương" → "medevac" (v3); "300 xét nghiệm… các xét nghiệm khác" → "general chemistry tests" (v4); khung "cáo trạng xếp bảy nhóm" → "theo toà phúc thẩm… generally fell into" (v7); "nhà đầu tư không bán được" → kết luận của toà sơ thẩm về nạn nhân, phúc thẩm giữ (v9, v10); "voided all" từ câu thuật lập luận của Holmes → lời toà tr. 34 "every single patient test result" (v11).
- **Cấu trúc:** "bảy nhóm cáo trạng = bảy câu kiểm" tự mâu thuẫn với Kiểm 7 (câu của kênh) → 6 + 1 (v3, v5, v6). Nhãn ●C/TT cho câu kèm và vế "Silicon Valley" (v10).
- **Trang/nguồn:** ngày 03/01/2022 dẫn nhầm N5 (v1); trích "never validated" gán nhầm N2 (v4); danh sách trang đã đọc (v3, v12).

**Trạng thái cuối:** vòng toàn tệp gần nhất (v8) **0 S**, 1 MH đã sửa; các vòng hẹp sau đó không còn MH (v11, v12: **0 MH**). **Hai dòng S cuối của vòng 12** (nhãn ◐ gán nhầm "the Indictment" của N1 cho cả cáo trạng 2018/2020; danh sách trang N1 ở §7 thiếu tr. 34, 52) đã sửa theo đúng đề xuất, phiên tự đối chiếu với N1 tr. 8 và N4/N5 — **chưa có tác tử chấm lại hai dòng này**; điều phối có thể kiểm nhanh. Không vòng nào thấy: Holmes bị nói là kết án lừa bệnh nhân, tên nạn nhân/nhân chứng, hướng dẫn làm theo được, sai số tiền/ngày/mức án.
KKĐ còn lại (không phải lỗi): tác tử không tự mở sec.gov (N2, N3, N10, N13, N15) theo lệnh — nội dung N2/N3 đối chiếu trên bản phiên chính tải; phiên chính đã mở N10, N13 (HTTP 200). Investor.gov 403 → không dùng.

## 5. Nguồn đã mở ở MR-D4 (01/11/2026)
- **N1** opinion 9th Cir. (LFS; `git lfs pull` — SHA-256 `4f591641…32da` khớp kho §8; 54 tr.; số trang in = số trang PDF).
- **N2, N3** sec.gov (HTTP 200, UA khai báo, chuyển hướng tới đường dẫn mới); **N15** complaint SEC v. Theranos & Holmes (200, SHA-256 `3ce565f8…6826`) — mở nhưng **không dùng**, không lưu vào repo.
- **N4–N8** + 1 thông cáo 2022 (không dùng): API chính thức DOJ, 6 kết quả.
- **Trạng thái (luật 4):** N9 trang ân xá Trump 2025– (cập nhật 20/10/2026): 0 kết quả Holmes/Balwani; N14 BOP: Holmes dự kiến ra 22/02/2030, Balwani 21/04/2033.
- **N10** sec.gov/tcr, **N11** BrokerCheck, **N12** ReportFraud, **N13** IAPD: HTTP 200.
- **Chưa mở được (không vượt rào, không dùng):** 4 trang investor.gov (403, cả với UA khai báo; không đổi UA, không bản lưu). Judgment N.D. Cal., lệnh chấp thuận dàn xếp SEC, kết cục SEC v. Balwani, certiorari: cần PACER/docket — chưa mở.

## 6. Ước chi (đơn giá đo thật QUY-TRINH §6, MR-4)
| | Thấp | Giữa | Cao |
|---|---|---|---|
| Veo 3.1 Lite 1080p (14/18/22 khe × 0,40 USD × 1,0/1,25/1,5 lượt) | 5,60 USD | 9,00 USD | 13,20 USD |
| ElevenLabs ký tự tính (TTS ~2.600 từ × 6,1 × 0,4401, thu lại 0/25/50 % + nhạc 3/4/5 phút × ~825 — nhạc **chưa đo** trên MR) | ≈ 9.500 | ≈ 12.050 | ≈ 14.600 |
Đề xuất trần G1: OpenRouter **≈ 10,40 USD**, ElevenLabs **≈ 14.000** ký tự tính. Ảnh NB2.1: không có khoá Gemini → không tính.

## 7. Cần chủ dự án / điều phối quyết
1. Duyệt dàn truyện (QUY-TRINH §3 mục 0) và khuôn **1 tập ~17 phút**.
2. Góc "bảy câu kiểm" (6 từ hồ sơ + 1 của kênh) — giữ hay đổi.
3. Nêu tên Walgreens/Safeway (theo hồ sơ, kèm câu không liên quan) và **không** nêu tên hãng dược — xác nhận.
4. Trần đề xuất §6 (quyết ở G1).
5. Trước khi chốt lời: kiểm lại trạng thái ngày chốt lời/ngày đăng; Counts 3–5, certiorari, lệnh chấp thuận dàn xếp SEC vẫn chưa có nguồn (PACER đang hoãn — K5).

**DỪNG** — chờ điều phối rà.
