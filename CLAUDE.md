# Money Reroute — hướng dẫn cho mọi phiên [MR]

Kênh YouTube drama bài học tài chính / lừa đảo, dựa trên **hồ sơ công khai** (SEC, DOJ, FTC, toà án). Mọi lệnh mở bằng `[MR · <mã phiên>]` (vd `[MR · MR-1]`).
Repo này độc lập với `lost-places-lab` và `crux-lab`; công cụ chép từ đó ghi nguồn + commit SHA ở đầu tệp.

## Đọc trước khi làm (theo thứ tự)
0. **Phiên điều phối:** `docs/BAN-GIAO-DIEU-PHOI.md` trước tiên (trạng thái, việc kế tiếp).
1. Lệnh của điều phối trong phiên này — **lệnh thắng** khi khác tài liệu, trừ khi lệnh trái `docs/HIEN-CHUONG.md` (khi đó DỪNG, hỏi).
2. `docs/HIEN-CHUONG.md` — định vị, ba tầng pháp lý, luật người thật, khai AI. **Thẩm quyền số một về nội dung.**
3. `docs/QUY-TRINH-TAP.md` — mốc, cổng G1/G2, trần chi.
4. `docs/LUAT-VEO.md` — luật V1–V8 khi dùng video AI (Veo).
5. `docs/NHAT-KY.md` — các mục MR-xx mới nhất (quyết định của chủ dự án, kết quả rà).

## Luật không bao giờ bỏ qua
- **Không đoán.** Mọi câu về người/công ty/vụ việc thật phải có hồ sơ công khai đã mở được (số vụ, ngày, URL, trang). Kiểm bằng nguồn đã mở, repo hoặc chạy thật; số đo thật thắng số tự khai. Câu không có nguồn → không dùng. Không mở được nguồn → ghi "chưa mở được", không suy ra nội dung.
- **Trần chi + 402 → DỪNG.** Mọi lệnh gọi API trả tiền: ước chi + trần cứng qua `scripts/cp/budget.py` (`MR_PHIEN=<mã>`). Phiên không có dòng trần trong bảng = trần 0 = cấm gọi. **HTTP 402 (quỹ cạn) ở bất kỳ dịch vụ nào → DỪNG ngay**, không thử lặp, không vá bằng ảnh tĩnh/đường khác; báo số dư. Chạm ~80 % trần mà còn > 20 % việc → dừng sinh, báo.
- **Tệp tốn tiền** (ảnh AI, clip video AI, âm TTS/nhạc) **đẩy Git LFS ≤ 10 phút sau khi sinh** (mẫu ở `.gitattributes` + `tools/lfs-allow.txt`); giữ `reports/<mốc>/CHECKPOINT.md` mục "Chạy tiếp từ đây". Tệp dựng lại được (0 USD) không đẩy, trừ bản xem.
- **`bash tools/preflight.sh` trước MỌI commit** (và `--range origin/main..HEAD` trước khi đẩy). Trượt → sửa rồi chạy lại; không `--no-verify` trừ khẩn cấp có ghi lý do trong báo cáo.
- **Không merge, không xoá nhánh, không force-push.** Điều phối merge sau khi rà.
- **Không vượt rào truy cập** (thêm sau rà MR-1): trang chống bot, CAPTCHA, tường đăng nhập/trả phí, chặn địa lý → **không** viết script, đổi user-agent, dùng bản lưu/mirror để vượt. Dùng đường chính thức (API của cơ quan, bản sao trên trang cơ quan khác, RECAP) hoặc ghi "chưa mở được". PACER có phí → chỉ khi lệnh có trần.
- **Không in khoá API** ra log, báo cáo, commit. Khoá do proxy tiêm; dùng giá trị giả khi công cụ đòi khoá.
- **Không mặt người thật.** Không ảnh, không chân dung AI, không giọng nhái người thật trong vụ. Nhân vật minh hoạ có nhãn (HIEN-CHUONG §4).
- Vật liệu đối thủ (lời, khung hình, thumbnail, danh sách đề tài của kênh khác) không đưa vào repo.
- Báo cáo **tiếng Việt**, văn phong chuyên nghiệp, ở `reports/<mốc>/BAO-CAO.md`; **DỪNG ở cuối mốc** và chờ rà.
