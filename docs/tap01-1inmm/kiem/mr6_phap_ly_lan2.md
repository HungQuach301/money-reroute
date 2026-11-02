# Kiểm pháp lý lần 2 — bản dựng MR-6 (QUY-TRINH §4 mục 5)

> Tác tử độc lập (chỉ đọc, không sửa, không mạng), 02/11/2026 ~04:50–05:00 UTC, trên bản dựng 540p đầu tiên (`reports/mr6/xem/tap01_540p.mp4` trước vòng sửa 1), 233 khung trích theo câu + `reports/mr6/chu_tren_hinh.json` + PDF hồ sơ.
> **Kết luận vòng 1: CHƯA ĐẠT** — 1 CHẶN, 9 NÊN SỬA, 10 GHI CHÚ. Phiên sửa trong **vòng sửa 1** (QUY-TRINH §4 mục 6), dựng lại, kiểm lại (§ cuối).

| # | Mức | Câu | Phát hiện (tóm tắt) | Sửa ở vòng 1 |
|---|---|---|---|---|
| 1 | **CHẶN** | S029, S041, S061, S069, S074/S077 | Nhãn "ILLUSTRATIVE — not the real person" chỉ ở cảnh tranh đầu đoạn; ở P05, P08, P12, P15, P16 cảnh đầu không người → nhân vật xuất hiện lần đầu không có nhãn đó (HIEN-CHUONG §4) | `dung.py chuan_bi_nhan()`: thêm nhãn "not the real person" cho **cảnh có người đầu tiên** mỗi đoạn |
| 2 | Nên sửa | S078–S081 | G15 giữ tiêu đề/mốc trích ¶76 (◐) trong các câu TT không nhãn ◐ | Tiêu đề → "UNTIL APRIL 9"; mốc Mar. 12 ghi "◐ SEC complaint ¶76: email, funds “by April 9th (at the latest)”" cố định trong G15 |
| 3 | Nên sửa | S030 | Ngoặc kép "ultimate counterparties" bỏ chữ "purported" của ¶45 | Bỏ ngoặc kép, dùng đúng lời S030 "said to be the ultimate counterparties" |
| 4 | Nên sửa | S053–S056 | Ngoặc kép "INVESTING ALONGSIDE YOU", "his share" không có trong hồ sơ; ô "HIS MONEY" | Tiêu đề = chữ lời S053 "PERSONALLY INVESTING ALONGSIDE THEM?" + "according to the SEC"; "as his share" (lời S055); ô "MONEY HE PUT IN" (lời S054) |
| 5 | Nên sửa | S043 | "Distribution agreements with platforms: NONE" (tuyệt đối) mạnh hơn thừa nhận | "Distribution agreements for those films: none" (lời S043) |
| 6 | Nên sửa | S036 | Câu bảo lưu "a figure he reserved the right to contest" nhỏ, chỉ ~1 s | Hiện cùng lúc với số 250+, chữ ngà 24 px |
| 7 | Nên sửa | S071, S088 | Dòng nguồn tràn khung; S071 thiếu N8 tr. 4 | Gộp tiền tố vụ hình sự, ≤ 3 tài liệu, tự giảm cỡ chữ cho vừa khung; S071 nay có Indictment pp. 9–10; Plea p. 4; Judgment p. 4 |
| 8 | Nên sửa | S005, S009, S036, S085, S089 | Số trung gian khi đếm trông như số thật; S005 "25–45%" chỉ giữ ~0,2 s | Đếm nhanh (0,4–1,0 s), giữ giá trị cuối; S005 cảnh G01 kéo dài cả câu |
| 9 | Nên sửa | S027 | Ký hiệu "35% × 35%" sai toán | Bỏ "×" giữa hai cột; cột 2 ghi "+35% again", mũi tên "→"; phép đúng 1.35 × 1.35 = 1.8225 giữ |
| 10 | Nên sửa | S015 (a17) | Người vest tối góc sau-nghiêng lộ má/tai | Cắt a17 hẹp thêm (300, 80, 1110, 536) |
| 11–20 | Ghi chú | | ◐ mất glyph (G08) · chữ đè (G11, G15, G18) · "typically" ($35,000–$1.5M) · S052 phần "$6 million home, luxury cars" theo N12 **không xác minh được offline** (N12 không lưu bản) · dáng xe b029 · T14 kèm câu ngoài lời (trang thật, có nhãn) · dòng khai AI "above/below" · thẻ bài học diễn đạt lại · S082 bỏ N8 | ◐ vẽ bằng DejaVu; dàn lại vị trí; thêm "typically"; dòng khai AI đặt **trên** danh sách nguồn, nguyên văn §6 ("listed below"); thẻ bài học S049, S061 dùng **nguyên văn lời**; S082 nay có Judgment p. 1. **S052 đã xác minh** (MR-6, 02/11 ~05:05 UTC, API DOJ `press_releases.json`, HTTP 200, số 22-027): "the purchase of his $6 million Beverlywood residence, luxury cars, and travel by private jet, according to the government’s sentencing memorandum" — thẻ "A $6 million home · luxury cars · private jet travel / according to prosecutors" khớp, không nêu tên khu phố |

## Kiểm lại sau vòng sửa 1
{KIEM_LAI}
