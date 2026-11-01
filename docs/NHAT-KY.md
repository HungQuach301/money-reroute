# NHẬT KÝ QUYẾT ĐỊNH — Money Reroute

> Mỗi mục: `## MR-xx · <ngày giờ (giờ Hà Nội)> · <tiêu đề>`. Ghi quyết định của chủ dự án và kết quả rà của điều phối; phiên làm chỉ ghi khi lệnh yêu cầu.
> Bối cảnh khởi nguồn: `lost-places-lab/docs/NHAT-KY.md` R-148 (01/11/2026 18:35): "Money Reroute (kênh drama bài học tài chính/lừa đảo) sẽ có repo GitHub và Claude Project mới riêng, không điều phối từ Project này."

## MR-0 · 01/11/2026 · Khởi tạo repo (phiên Claude Code, 0 USD API)
- Nhánh `claude/money-reroute-init-sj5scm` từ `main` (`78637c1`).
- Tạo: `CLAUDE.md`, `docs/HIEN-CHUONG.md` (NHÁP), `docs/QUY-TRINH-TAP.md` (NHÁP), `docs/LUAT-VEO.md` (V1–V8 nguyên văn từ lost-places-lab CONG-THUC §1.9), `docs/BAN-GIAO-DIEU-PHOI.md`, `RIGHTS.md`, `COST-LEDGER.csv`, công cụ chép từ lost-places-lab @ `ae22e37` (ghi nguồn đầu tệp), `.gitattributes` LFS + `tools/lfs-allow.txt`.
- Số dư (01/11/2026 12:36 UTC): OpenRouter còn ≈ **8,15 USD** (credits 70 − đã dùng 61,85); ElevenLabs còn **156.855** ký tự (527/157.382, reset 01/12/2026); Gemini, YouTube Data, Claude API, OpenAI: **không có khoá** trong môi trường.
- Chờ chủ dự án: duyệt HIEN-CHUONG + QUY-TRINH; các câu hỏi ở `reports/mr0/BAO-CAO.md` §6.

## MR-0 · 01/11/2026 19:50 (giờ Hà Nội) · Điều phối rà MR-0 — merge (fast-forward `85cc88f`)
Kiểm độc lập trên tệp, không dựa báo cáo phiên:
- `preflight --range main..HEAD` và `--all`: ĐẠT. Tác giả commit `noreply@anthropic.com`. 7 tệp Python biên dịch OK, đều có dòng NGUỒN.
- So máy với `lost-places-lab` @ `ae22e37`: 7 tệp công cụ **khớp nguyên văn** (bỏ dòng NGUỒN); `budget.py` khác đúng phần đã khai; 9 dòng luật V1–V8 trong `LUAT-VEO.md` **khớp nguyên văn** `CONG-THUC-LOAT.md`. Câu trích R-148 khớp. Ước Cusco 27,32 USD (R-143) khớp.
- Chạy lại `mua_hau_ky.py` trên clip thử 2 s: 48 khung vào = 48 khung ra (khớp báo cáo).
- `budget.py`: trần 0 chặn đúng ở `mr0` và phiên chưa có dòng (`mr1`). **Lỗi nhỏ:** `bao_402()` ghi khoản `gemini_usd` cho 402 của ElevenLabs/YouTube (số tiền 0, `dich_vu` vẫn đúng) → sửa ở MR-1.
- Trang Help khai AI (support.google.com/youtube/answer/14328491) mở 01/11/2026: tiêu đề "Disclosing use of GenAI content"; Studio → mục Attributes → "AI use" Yes/No — khớp HIEN-CHUONG §6.
- Số dư OpenRouter/ElevenLabs: **chưa kiểm độc lập** (môi trường điều phối không ra được hai dịch vụ này). Sổ `lost-places-lab` ghi chi/nạp OpenRouter cùng giai đoạn → nhiều khả năng **chung tài khoản**; chủ dự án xác nhận.
- Bổ sung đề xuất cho HIEN-CHUONG (chờ chủ dự án): (1) ghi rõ tiếng Anh Mỹ (en-US); (2) tách "phán quyết dân sự sau xét xử" (● JUDGMENT, nói "found liable", không "convicted") khỏi "phán quyết theo thoả thuận không thừa nhận" (◐ ALLEGED + "settled without admitting or denying"); (3) thêm ca DPA/NPA, bị cáo chết trước phán quyết cuối, ân xá/giảm án; (4) luật thumbnail như tiêu đề; (5) §7 đổi "chỉ chủ dự án sửa" → "chỉ chủ dự án quyết định sửa; điều phối/phiên thực hiện"; (6) RIGHTS: hồ sơ tiểu bang/nước ngoài không thuộc §105, kiểm riêng.
- Merge: nội dung còn NHÁP nhưng đã gắn nhãn NHÁP; không có rủi ro phát hành ở mốc này.

## MR-0 · 01/11/2026 20:08 (giờ Hà Nội) · Chủ dự án quyết sau rà MR-0
- **Q1 Hiến chương: duyệt PA-A.** Điều phối áp 6 bổ sung vào `docs/HIEN-CHUONG.md` (en-US; tách ● JUDGMENT sau xét xử khỏi ◐ thoả thuận không thừa nhận, cấm "convicted" cho vụ dân sự; ca DPA/NPA, bị cáo chết, ân xá; cột loại phán quyết bắt buộc; thumbnail theo luật tiêu đề; §7 "chủ dự án quyết định, điều phối/phiên thực hiện") và `RIGHTS.md` (hồ sơ tiểu bang/nước ngoài không thuộc §105). Hiến chương chuyển trạng thái ĐÃ DUYỆT.
- **Q2 Quỹ OpenRouter: dùng chung tài khoản với lost-places-lab; chủ dự án đã tách khoá riêng cho MR.** Số dư tài khoản chủ dự án báo **5,45 USD** (01/11/2026 20:08; điều phối chưa kiểm độc lập). Hệ quả: luật V7 "≤ 3 lượt song song" và đệm `/credits` tính **chung** mọi phiên hai repo; 5,45 USD chưa đủ một tập (tham chiếu Machu Picchu ≈ 25,8 USD OpenRouter) → nạp trước M-c, không chặn M-a/M-b.
- **Q3 Khoá YouTube Data:** chủ dự án cấp trước MR-1; điều phối gửi hướng dẫn trong chat (dự án Google Cloud riêng cho MR, khoá giới hạn chỉ YouTube Data API v3, gắn network secret host `www.googleapis.com` ở môi trường của phiên MR; không dán khoá vào chat/repo). Trang getting-started (mở 01/11/2026): hạn mức mặc định 10.000 đơn vị/ngày/dự án; `search.list` 1 đơn vị nhưng giới hạn riêng 100 lượt/ngày → MR-1 kiểm bảng Quota costs trước khi đặt cách tính `youtube_units`.
- Q4 Nhận diện kênh: quyết ở G1 tập 1.
