# BÀN GIAO ĐIỀU PHỐI — Money Reroute

> Phiên điều phối đọc tệp này **trước tiên**. Cập nhật cuối mỗi lượt rà. Cập nhật lần cuối: quyết định chủ dự án sau rà MR-0, 01/11/2026 20:08 (giờ Hà Nội).

## 1. Trạng thái
- Repo vừa khởi tạo (MR-0). Chưa có đề tài, chưa có tập, chưa chi tiền.
- MR-0 **đã merge** vào `main` (fast-forward `85cc88f`) sau rà (NHAT-KY mục rà MR-0). Nhánh giữ nguyên, không xoá.
- `docs/HIEN-CHUONG.md` **ĐÃ DUYỆT** (PA-A, 01/11/2026 20:08). `docs/QUY-TRINH-TAP.md` vẫn NHÁP 0.1 (duyệt cùng G1 tập 1).

## 2. Quỹ (đọc 01/11/2026 12:36 UTC, MR-0)
| Dịch vụ | Số dư | Ghi chú |
|---|---|---|
| OpenRouter (Veo) | **5,45 USD** (chủ dự án báo 01/11/2026 20:08) | **Chung tài khoản** với lost-places-lab, **khoá riêng** cho MR; V7 song song tính chung; cần nạp trước M-c |
| ElevenLabs | 156.855 ký tự | gói creator, reset 01/12/2026 |
| Gemini | — | không có khoá trong môi trường |
| YouTube Data | hạn mức dự án riêng | đã gắn (PA-A, 01/11 20:41), MR-1 bước 0 kiểm |
| Claude API / OpenAI | — | không có khoá |

## 3. Việc kế tiếp (đề xuất)
1. ~~Điều phối rà MR-0 → merge.~~ Xong.
2. ~~Chủ dự án duyệt HIEN-CHUONG, trả lời §6 MR-0.~~ Xong (PA-A; quỹ chung khoá riêng; cấp khoá YouTube).
3. ~~**MR-1 = M-a**~~ Xong, merge 01/11/2026 21:20 (3 vụ: Woodbridge / 1inMM / Heartland; khuyến nghị A). **Kế tiếp: MR-2 = M-b Kịch bản + ước chi → G1**, chờ chủ dự án chọn vụ + độ dài + quyết nhãn người không bị cáo buộc. (Mô tả MR-1 cũ: (0 USD): 3 vụ ứng viên có hồ sơ SEC/DOJ/FTC/toà án mở được, bảng tầng pháp lý, rủi ro; kèm sửa `bao_402()`, áp bổ sung HIEN-CHUONG đã duyệt, mở và ghi chính sách kiếm tiền YouTube liên quan nội dung AI. Đo cầu đề tài bằng YouTube Data: đã cấp.)
4. Trước phiên tốn tiền đầu tiên: thêm dòng trần vào `scripts/cp/budget.py` `CAPS_PHIEN`; quyết bảng màu/chữ/look của kênh (công cụ `ban_do.py`, `mau_look.py` còn thiếu tệp phụ thuộc — xem báo cáo MR-0 §4).

## 4. Luật nhắc nhanh
Không đoán · trần chi + 402 → DỪNG · LFS ≤ 10 phút · preflight trước commit · không merge/xoá nhánh/force-push ở phiên làm · không mặt người thật · ba tầng pháp lý · báo cáo tiếng Việt · DỪNG cuối mốc.

## 5. Lộ trình đã duyệt (01/11/2026 21:34)
Mốc 1 Hiến chương v2 — xong · Mốc 2 Dàn truyện A+B (MR-2) → chủ dự án chọn vụ · Mốc 3 Kịch bản + G1 tập 1 (MR-3) ‖ Kho đề tài (MR-K1, song song) · Mốc 4 Sản xuất tập 1 (nạp OpenRouter trước) · Mốc 5 Đăng, đo đơn giá thật, chốt QUY-TRINH 1.0.

## 6. Trạng thái sau rà MR-2 (01/11/2026 22:20)
- MR-2 merge squash `68af9a9`. Chờ chủ dự án: chọn vụ tập 1 (điều phối khuyến nghị B 1inMM), xoá nhánh `ccr-287dabd9-ibz780` (có email trong lịch sử), cấp địa chỉ liên hệ của kênh cho UA sec.gov. Kế tiếp: MR-3 kịch bản + G1 ‖ MR-K1 kho đề tài.
