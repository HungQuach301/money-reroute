# BÀN GIAO ĐIỀU PHỐI — Money Reroute

> Phiên điều phối đọc tệp này **trước tiên**. Cập nhật cuối mỗi lượt rà. Cập nhật lần cuối: điều phối rà MR-0, 01/11/2026 19:50 (giờ Hà Nội).

## 1. Trạng thái
- Repo vừa khởi tạo (MR-0). Chưa có đề tài, chưa có tập, chưa chi tiền.
- MR-0 **đã merge** vào `main` (fast-forward `85cc88f`) sau rà (NHAT-KY mục rà MR-0). Nhánh giữ nguyên, không xoá.
- Tài liệu ở trạng thái **NHÁP chờ chủ dự án duyệt**: `docs/HIEN-CHUONG.md`, `docs/QUY-TRINH-TAP.md`.

## 2. Quỹ (đọc 01/11/2026 12:36 UTC, MR-0)
| Dịch vụ | Số dư | Ghi chú |
|---|---|---|
| OpenRouter (Veo) | ≈ 8,15 USD (70 − 61,85) — số phiên tự đọc, điều phối chưa kiểm độc lập | Nhiều khả năng **chung tài khoản** với lost-places-lab → chủ dự án xác nhận trước khi đặt trần |
| ElevenLabs | 156.855 ký tự | gói creator, reset 01/12/2026 |
| Gemini | — | không có khoá trong môi trường |
| YouTube Data | — | không có khoá |
| Claude API / OpenAI | — | không có khoá |

## 3. Việc kế tiếp (đề xuất)
1. ~~Điều phối rà MR-0 → merge.~~ Xong.
2. Chủ dự án duyệt HIEN-CHUONG kèm 6 bổ sung ở NHAT-KY (rà MR-0), trả lời các câu §6 báo cáo MR-0.
3. **MR-1 = M-a Đề tài + hồ sơ** (0 USD): 3 vụ ứng viên có hồ sơ SEC/DOJ/FTC/toà án mở được, bảng tầng pháp lý, rủi ro; kèm sửa `bao_402()`, áp bổ sung HIEN-CHUONG đã duyệt, mở và ghi chính sách kiếm tiền YouTube liên quan nội dung AI. Đo cầu đề tài bằng YouTube Data: chờ chủ dự án quyết cấp khoá.
4. Trước phiên tốn tiền đầu tiên: thêm dòng trần vào `scripts/cp/budget.py` `CAPS_PHIEN`; quyết bảng màu/chữ/look của kênh (công cụ `ban_do.py`, `mau_look.py` còn thiếu tệp phụ thuộc — xem báo cáo MR-0 §4).

## 4. Luật nhắc nhanh
Không đoán · trần chi + 402 → DỪNG · LFS ≤ 10 phút · preflight trước commit · không merge/xoá nhánh/force-push ở phiên làm · không mặt người thật · ba tầng pháp lý · báo cáo tiếng Việt · DỪNG cuối mốc.
