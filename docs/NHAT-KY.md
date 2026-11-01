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

## MR-1 · 01/11/2026 20:41 (giờ Hà Nội) · Chủ dự án gắn khoá YouTube (PA-A) và dán lệnh MR-1
- Khoá YouTube Data API v3: dự án Google Cloud riêng cho MR, network secret host `www.googleapis.com` (chủ dự án báo; MR-1 bước 0 kiểm bằng gọi thật).
- Lệnh MR-1 (M-a Đề tài + hồ sơ, trần `youtube_units` 3000, `search.list` ≤ 60 lượt, khoản khác 0) đã dán vào phiên Claude Code. Chờ phiên DỪNG để rà.

## MR-1 · 01/11/2026 21:20 (giờ Hà Nội) · Điều phối rà MR-1 (M-a Đề tài + hồ sơ) — merge
Nhánh `claude/zealous-tesla-7wrjwj` @ `7176e00` (từ `1f2c394`), merge `--no-ff` vào `main`. Kiểm độc lập trên tệp:
- Preflight `--range main..HEAD`: ĐẠT (55 tệp). 27 PDF hồ sơ đúng dạng LFS; `git lfs pull` tải đủ; **SHA-256 27/27 khớp** NGUON.md (tính lại).
- Sổ `reports/mr1/calls.jsonl`: 19 đơn vị, `search.list` 9/60 lượt, chỉ khoản `youtube_units` — trong trần. `do-cau/*.json` không chứa tiêu đề/mô tả/thumbnail kênh khác.
- `bao_402()` chạy lại trên bản sao: 5 dịch vụ ghi đúng khoản (`openrouter_usd`, `elevenlabs_chars`, `youtube_units`, `gemini_usd`, `khong_ro`), `spent()` chạy được. `check_yt()` + trần lượt: đọc mã, đúng.
- Đối chiếu PDF gốc (pdftotext): Shapiro 300 tháng (240 + 60, nối tiếp); proffer ~1,29 tỷ USD, ~10.000 (và "hơn ~9.000") nhà đầu tư, tiền nhà đầu tư mới bị dùng; plea mức tối đa 20 + 5 năm, từ bỏ kháng cáo; SEC final judgment Shapiro "without admitting or denying", phạt 100.000.000 USD; CA11 23-12660 summary affirm bác giảm án; Acevedo §371, 60 tháng; Roseman chỉ có "criminal conviction" (N15) — đúng lý do không nói "pleaded guilty". Horwitz: plea 1 tội gian lận chứng khoán, "all remaining counts ORDERED dismissed". Hanes: 1 tội §656, 293 tháng. **Không thấy sai.**
- Bảng tầng Woodbridge: tách ● hình sự / ◐ SEC consent đúng HIEN-CHUONG §3 (bản đã duyệt); người không bị cáo buộc không nêu tên.
- **Vi phạm quy trình (không gây hại):** tác tử nghiên cứu Woodbridge thử viết script vượt trang chống bot justice.gov; bị chặn, dừng, phiên báo trung thực. Điều phối thêm luật "Không vượt rào truy cập" vào `CLAUDE.md`.
- Đề xuất của phiên (nhãn cho người/tổ chức không bị cáo buộc) → trình chủ dự án.
- Khuyến nghị điều phối: đồng ý chọn **A Woodbridge** cho tập 1; B giữ tập 2; C chỉ khi có quy tắc ẩn danh cấp thị trấn.

## MR-1 · 01/11/2026 21:29 (giờ Hà Nội) · Chủ dự án: định hướng nội dung → HIẾN CHƯƠNG v2
Chủ dự án (21:20–21:29): mỗi tập một câu chuyện, chấp nhận dài kỳ, kịch tính, cuốn hút; bài học tài chính, đầu tư, tài chính cá nhân, tội phạm, nhận diện lừa đảo, kể cả yếu tố tình dục; (1) **loại bỏ những điểm có rủi ro bị kiện**; (2) chi tiết tội phạm sâu (vd rửa tiền) được đưa vào dạng bài học, lý giải, nhận diện; (3) bài học không giới hạn ở tài chính cá nhân; đảm bảo duy trì nội dung dài hạn.
Điều phối áp vào `docs/HIEN-CHUONG.md` (v2):
- §1: mỗi tập trọn một câu chuyện, cho phép nhiều phần; bài học rộng; "giải thích được, không hướng dẫn làm" (ranh giới khái niệm ↔ thao tác, phép thử "làm theo được ngay"); không khuyên đầu tư **cụ thể**, nguyên tắc chung được nói.
- §3 luật 3: tin đồn về người/tổ chức có tên **CẤM** (trước: mặc định không dùng). Luật 8 mới "loại điểm có rủi ro bị kiện": nhân vật trung tâm phải ●; ◐ chỉ cho vai phụ trong vụ có trụ ● hoặc vụ đã dàn xếp xong; hành vi hợp pháp-có-hại không nêu tên; không gán nhãn khi chưa ●; thương hiệu bị mạo danh kèm câu không liên quan; không suy đoán động cơ/đời tư.
- §5: chủ đề có yếu tố tình dục — chỉ nạn nhân người lớn, không hình/mô tả tình dục; không làm tập có nạn nhân vị thành niên trong vụ tình dục.
- Diễn giải của điều phối cần chủ dự án xác nhận: "sex" = lừa đảo/tội phạm có yếu tố tình cảm, tình dục (lừa tình, sextortion). Vùng xám X1 (hợp pháp-có-hại) giữ được ở dạng **không nêu tên**; X2 (chỉ cáo buộc) chỉ còn ở vai phụ.
- Còn chờ: D2 khuôn dài kỳ, nhãn "KHÔNG BỊ CÁO BUỘC", gói duy trì dài hạn.

## MR-1 · 01/11/2026 21:34 (giờ Hà Nội) · Chủ dự án: duyệt và xác nhận toàn bộ theo khuyến nghị
- Diễn giải "sex" = lừa đảo/tội phạm có yếu tố tình cảm, tình dục (lừa tình, sextortion), nạn nhân người lớn — **xác nhận**.
- D2 khuôn tập: **PA-A** một vụ một tập; nhiều phần chỉ khi mỗi phần có bước ngoặt có hồ sơ + bài học riêng → QUY-TRINH §3 mục 0b.
- Nhãn người/tổ chức không bị cáo buộc: **PA-A** giá trị "KHÔNG BỊ CÁO BUỘC" trong bảng tầng, không nhãn trên hình → HIEN-CHUONG §3 luật 5.
- Gói duy trì dài hạn: **duyệt** (dàn truyện trước kịch bản; kho đề tài ≥ 10 vụ theo 6 trụ; xử lý khiếu nại 4 bậc; đo đơn giá thật sau tập 1). QUY-TRINH lên bản 0.2.
- Kho đề tài: **PA-A** chạy song song MR-3 (sau rà MR-2).

## MR-2 · 01/11/2026 22:20 (giờ Hà Nội) · Điều phối rà MR-2 (Dàn truyện A + B) — merge kiểu squash
Nhánh `ccr-287dabd9-ibz780` @ `45956b6` (từ `489f18a`). Kiểm độc lập trên tệp:
- Preflight `--range` trên tip: ĐẠT; 0 USD. Đối chiếu PDF gốc (pdftotext): 1inMM — lợi nhuận 25–45 %, "generally did not and would not acquire", hợp đồng cấp phép/phân phối "fake", ≥ 650 triệu USD từ ≥ 5 nhóm, > 250 nhà đầu tư con (có bảo lưu), vỡ nợ từ ~12/2019, gốc ~230,36 triệu USD; SEC: câu nhà đầu tư "if HBO was involved…", "by April 9th (at the latest)", không quan hệ hợp đồng với HBO; final judgment 2024: 62.847.901,05 + 11.375.011,28 USD. Woodbridge — > 80 triệu USD hoa hồng, 25–95 triệu USD chiếm dụng, 5 bang (TX, MA, AZ, PA, MI) "nonetheless continued to sell". Phép tính 35 %/6 tháng ≈ 82 %/năm (1,35² = 1,8225) đúng. **Không thấy sai.**
- **Sự cố 1 — email chủ dự án trong lịch sử nhánh** (thêm ở `9e0ac68`, gỡ ở `0c15d5e`; tip sạch) do preflight chạy qua pipe. Repo công khai → điều phối **merge kiểu squash** (main không chứa commit có email) (main sạch: 0 dòng email trên toàn lịch sử main). **Xoá nhánh từ xa: điều phối bị chặn quyền** → chờ chủ dự án xoá nhánh `ccr-287dabd9-ibz780` trên GitHub; nội dung đầy đủ đã nằm trong commit squash `68af9a9`. Thêm luật "preflight không qua pipe" vào CLAUDE.md. Lưu ý: GitHub có thể còn giữ commit theo SHA một thời gian; xoá hẳn cần GitHub Support.
- **Sự cố 2 — email chủ dự án gửi tới sec.gov trong User-Agent.** Thêm luật "không đưa thông tin cá nhân chủ dự án vào request/repo" vào CLAUDE.md; chờ chủ dự án cấp địa chỉ liên hệ của kênh.
- **Sự cố 3 — MR-1 N17 (Investor.gov) mở bằng UA trình duyệt sau khi UA khai báo bị 403** → trái luật "không vượt rào truy cập" (luật ban hành sau MR-1). N17 chỉ là trang dẫn người xem, không làm nguồn câu nào; MR-3 mở lại đúng cách hoặc ghi "chưa mở được".
- Góp ý nội dung cho MR-3: 1inMM nhịp 7b bỏ tên khu "Beverlywood" (đủ nhận ra nhà; chủ hiện tại KBCB). Nhịp 13 chỉ dùng khi đọc được Dkt. 58.
- Khuyến nghị điều phối: **đổi sang B (1inMM) cho tập 1**, theo ưu tiên kịch tính của chủ dự án và độ chắc nguồn (gần hết truyện là lời thừa nhận trong plea); A (Woodbridge) làm sau một tập khác trụ.

## MR-2 · 01/11/2026 22:17 (giờ Hà Nội) · Chủ dự án: chọn vụ tập 1 + địa chỉ liên hệ kênh
- **Q1: tập 1 = B `1inmm-horwitz`** (theo khuyến nghị điều phối). Woodbridge làm sau một tập khác trụ.
- **Q2: PA-A** — chủ dự án cấp địa chỉ email liên hệ riêng của kênh cho UA khai báo sec.gov. Địa chỉ **không ghi vào repo** (preflight P1 chặn email trong tệp; repo công khai) — chỉ nằm trong lệnh phiên ở chat.
- Phát lệnh MR-3 (kịch bản tập 1 → G1) và MR-K1 (kho đề tài), chạy song song.

## MR-3 / MR-K1 · 01/11/2026 22:23 (giờ Hà Nội) · Chủ dự án: đã xoá nhánh MR-2, phát MR-3 và MR-K1
- Nhánh `ccr-287dabd9-ibz780` (có email trong lịch sử) đã xoá trên GitHub — điều phối xác nhận bằng `git fetch --prune`: không còn trên remote.
- MR-3 (kịch bản tập 1 → G1) và MR-K1 (kho đề tài) chạy song song từ `6296c0e`. Khi rà: quét toàn lịch sử hai nhánh tìm địa chỉ email.
