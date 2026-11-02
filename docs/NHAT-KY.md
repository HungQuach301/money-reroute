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

## MR-3 · 01/11/2026 22:50 (giờ Hà Nội) · Điều phối rà MR-3 (kịch bản tập 1 → G1) — merge
Nhánh `claude/lucid-goldberg-vcpyv1` @ `ca3c7cb` (từ `6296c0e`). Kiểm độc lập trên tệp:
- Preflight `--range`: ĐẠT. Quét toàn lịch sử nhánh: **0 dòng email**. Chi 0 USD.
- PDF mới Dkt. 58 (N22) SHA-256 `3626166d…1575` khớp NGUON. Các chữ trích trên hình trong `loi.json` đối chiếu pdftotext: có trong N7 tr. 11 ("to lull the investors…"), N1 ¶77 ("highly doubtful"), N22 ("portrayed himself as a Hollywood success story", "was not a successful businessman or Hollywood insider. He just played one in real life.", "largest known Ponzi scheme in the history of this District"); "one in a million" từ N3 (HTML, phiên ghi trong NGUON). Không thấy chữ trích sai.
- Quét lời: 0 "Beverlywood", 0 "fraudster/scammer/con man/con artist/monster", 0 "convicted of wire"; 2 câu nhắc trộm danh tính đều nói **đã bị bác, không bị kết tội**. 6 đoạn có HBO/Netflix đều kèm câu KBCB. "Ponzi" chỉ qua chủ thể công tố (S092).
- Ước chi: phép tính 3 mức đúng (5,28 / 7,68 / 13,20 USD Veo M-c; 9,22 × V7). Hệ số TTS 0,44 chưa đo trên MR → trần có chặn phụ ký tự gửi.
- SHOT: không mặt, không logo/giao diện, không tài liệu/tin nhắn dựng lại; danh sách trang hồ sơ cấm crop (SSN, tên người nhận bồi hoàn, email/điện thoại công tố) — đạt.
- Kiểm lời độc lập của phiên: 102/102 K sau 4 vòng; điều phối không thấy câu nào trái HIEN-CHUONG v2.

## MR-3 · 01/11/2026 22:48 (giờ Hà Nội) · Chủ dự án: giọng + thumbnail
- **Giọng:** dùng giọng kênh lost-places-lab (BIBLE lost-places §9: W4 "LP-M0b-vd-1", Voice Design, voice_id `kozBJGqBNTqfBBClLNCL`, TTS `eleven_v4`), **không thử giọng lại**. Phiên M-c kiểm trước: voice_id truy cập được từ tài khoản ElevenLabs của MR (GET miễn phí); không được → DỪNG, báo.
- **Thumbnail:** chủ dự án tự sinh bằng ChatGPT. Áp HIEN-CHUONG §4 (thumbnail theo luật tiêu đề, không mặt người thật, không logo). Tệp đưa vào repo ghi một dòng RIGHTS (công cụ AI, ngày, người tạo).
- Còn chờ: duyệt G1 (a)(b)(c), tiêu đề, bảng màu, nạp OpenRouter.

## MR-3 · 01/11/2026 22:58 (giờ Hà Nội) · Chủ dự án: sửa lời trước G1, tiêu đề, bảng màu, quỹ
- Bài học **tổng kết rõ ở cuối clip** (thêm đoạn tổng kết bài học hiểu biết + dấu hiệu + nguyên tắc, kèm thẻ tổng kết trên hình).
- **Đồng ý 2 sửa điều phối đề xuất:** câu KBCB HBO/Netflix đọc thành lời 2 lần (S008, S045), 4 lần còn lại (S019, S033, S072, S076) chuyển chữ trên hình; Hồi 2 giữ nguyên tầng, tăng kịch tính bằng hình/nhạc (dòng thời gian đếm ngược tới 9/4).
- **Tiêu đề T1** "How an Actor Raised $650 Million on Fake Film Deals". **Bảng màu B1 "Hồ sơ".**
- Gói phát hành có tệp luật thumbnail cho ChatGPT: điều phối tạo `docs/tap01-1inmm/phat-hanh/THUMBNAIL-RULES.txt`.
- **OpenRouter:** chủ dự án nạp thêm 15 USD; tổng ~40 USD **dùng chung** với lost-places-lab (chủ dự án báo; phiên đọc `/credits` trước M-c).
- Phát MR-3b (sửa lời + kiểm lời các câu đổi); G1 chốt sau rà MR-3b.

## MR-3b + MR-K1 · 01/11/2026 23:35 (giờ Hà Nội) · Điều phối rà — merge cả hai
**MR-3b** (`claude/compassionate-faraday-ll0nya` @ `40487cd`): preflight ĐẠT; 0 email trong lịch sử nhánh; 0 USD.
- `loi.json`: 105 câu (101 đọc, 4 chữ), 2.005 từ, ≈ 16:13. Mọi đoạn có tên HBO/Netflix có câu KBCB: đọc ở P01 (S008), P08 (S045); chữ trên hình ở P03, P06, P15, P16. Câu KBCB đổi thành "…not accused of wrongdoing **in these cases**…" (thu hẹp, an toàn hơn — chờ chủ dự án duyệt cùng G1).
- P21 tổng kết: 3 bài học + 5 dấu hiệu + 1 nguyên tắc + nơi kiểm/báo cáo; không sự việc mới; S100 đối chiếu N1 ("registered with the Commission") khớp.
- Còn mở trước ngày đăng: mở lại N2, N3, N18 bằng UA khai báo (403 ở MR-3b).
**MR-K1** (`claude/kho-de-tai-mr-k1-5pplwo` @ `0718006`): preflight ĐẠT; 0 email; YouTube 55/2000 đơn vị, `search.list` 28/50, mọi lượt HTTP 200; `do-cau/*.json` không có tiêu đề/mô tả/thumbnail.
- 14 vụ / 6 trụ; SHA-256 **23/23 khớp** (22 PDF + 1 JSON thông cáo DOJ). Đối chiếu PDF: Stanford "convicted on 13 of 14 counts… 110 years" (CA5); Holmes 135 tháng (CA9); Alldred 288 tháng (CA5). Kiểm tầng độc lập: 0 vụ không đạt; các điểm sửa đã áp.
- Cần chủ dự án quyết: Wilkins (§5 — chưa xác định nạn nhân người lớn), Stanford vụ SEC (summary judgment có tranh chấp: ● hay ◐), Sunmola (mức nói về ảnh riêng tư), thứ tự tập, PACER.

## MR-4 · 01/11/2026 23:29 (giờ Hà Nội) · Chủ dự án: DUYỆT G1 tập 1; PA-A lượt thử; phát MR-4
- **G1 tập 1 `1inmm-horwitz` — DUYỆT** theo khuyến nghị: (a) đề tài + bảng tầng; (b) lời 105 câu (101 đọc) kể cả câu KBCB "…in these cases…"; (c) trần cả tập OpenRouter 11,10 USD + ElevenLabs 19.000 ký tự tính (M-c 9,50 + 16.000; M-d 0; M-e 1,60 + 3.000). **Lời và bảng shot ĐÓNG BĂNG.**
- **PA-A:** MR-4 = giọng toàn lời + thử 2 khe Veo → DỪNG; MR-5 = phần Veo còn lại + nhạc. Chủ dự án đã dán lệnh MR-4.
- Chủ dự án: các tập đăng liên tục, **không chờ số liệu xem tập 1** để định thứ tự → điều phối trình thứ tự chốt + nhịp tiền kỳ song song.

## MR-D23 · 01/11/2026 23:33 (giờ Hà Nội) · Chủ dự án: thứ tự tập, luật đệm, K1–K5; phát MR-D23
- Thứ tự **PA-A**: tập 2–5 chốt cứng Patel (IRS call center) → Sunmola → Theranos → Woodbridge; tập 6–14 dự kiến theo KHO.md §2.
- **Luật đệm** ≥ 2 tập đã qua G1 → QUY-TRINH §4b.
- K1 **loại Wilkins**; K2 Stanford vụ SEC ● JUDGMENT + HIEN-CHUONG §3 (b) "do toà kết luận — sau xét xử hoặc summary judgment có tranh chấp"; K3 Sunmola mức khái niệm; K5 hoãn PACER.
- Chủ dự án đã dán MR-D23 (dàn truyện tập 2 + 3), chạy song song MR-4.

## MR-4 + MR-D23 · 02/11/2026 06:05 (giờ Hà Nội) · Điều phối rà — merge cả hai
**MR-4** (`ccr-aa287726-96bpjx` @ `8a908ac`): preflight ĐẠT; 0 email; LFS tải đủ (25 mp3, 3 mp4, bản xem).
- Sổ `reports/mr4/calls.jsonl`: OpenRouter **1,20 USD** / trần 1,60; ElevenLabs **6.109** ký tự tính / trần 8.000 — khớp đối soát khoá và `/subscription` phiên ghi. Không 402.
- Đơn giá thật ghi QUY-TRINH §6: Veo Lite 1080p 8 s **0,40 USD/clip**; **1,5 lượt/khe** (2 khe khó); TTS **0,4401** ký tự tính/gửi; nhịp **155 từ/phút** (toàn lời 12:55).
- Điều phối xem tờ 0,5 s: **V12_l1** đạt (rót–tràn liên tục, ly không biến dạng, chai nền không chữ đọc được). **V06_l2** đạt: bóng ngược sáng, chỉ gáy/lưng, không nét mặt; neo cuối cửa sổ trống (V3). V06_l1 trượt (lộ mặt) — không dùng.
- Bài học Veo: chỉ dẫn phủ định/vị trí ("no hand", "head outside frame", "to the right") kém tin cậy; **ngược sáng → bóng** là cách giấu mặt hiệu quả → áp cho MR-5.
- **Quỹ chung:** tài khoản OpenRouter chi thêm ≈ 4,00 USD không phải của MR trong 16:28–16:56 UTC. Lịch sử `lost-places-lab` không có commit trong cửa sổ đó (commit cuối 15:37 UTC) → **nguồn chi chưa xác định**; chờ chủ dự án đối chiếu. Lượt Veo của MR chạy tuần tự, mỗi lượt kiểm `/credits` — không bị ảnh hưởng.
- Còn mở: **nghe tai** bản ghép (đặc biệt "Horwitz" ở P19 — whisper chép "Horowitz").
**MR-D23** (`ccr-f54cf043-76wk5p` @ `a38e077`): preflight ĐẠT; 0 email; 0 USD. Kiểm độc lập 5 vòng, 0 sai cuối. Sunmola: đúng một câu khái niệm về ảnh riêng tư, chỉ thẻ chữ, không nhắc lại (K3). Patel: không lời gọi dựng lại, không số điện thoại, cơ quan bị mạo danh kèm câu không liên quan.
- Khuyến nghị điều phối: **bỏ tên HGLOBAL** (tổ chức chỉ bị truy tố, chưa xét xử, trạng thái sau 7/2018 không có nguồn) → nói "one of the call centers he admitted operating and funding".

## MR-5 · 02/11/2026 06:07 (giờ Hà Nội) · Chủ dự án: phát MR-5; giữ tên HGLOBAL; số dư OpenRouter
- MR-5 (14 khe Veo còn lại + nhạc tập 1, trần OpenRouter 8,30 USD + ElevenLabs 6.000 ký tự tính) đã dán.
- **Tập 2 giữ tên HGLOBAL** (chủ dự án quyết, khác khuyến nghị điều phối): mỗi lần nêu (lời và hình) kèm câu ◐ như dàn truyện nhịp 4b — bị truy tố, được coi là vô tội khi chưa bị kết án, gắn mốc 7/2018 và 11/2020; không suy trạng thái sau 7/2018. Kiểm lại trạng thái HGLOBAL ở ngày chốt lời và ngày đăng (luật 4).
- OpenRouter tài khoản chung: **25,65 USD** (chủ dự án báo; khớp số MR-4 đọc sau phiên 25,645 → không có chi mới sau MR-4).

## MR-5 / MR-K23 / MR-D4 · 02/11/2026 06:55 (giờ Hà Nội) · Chủ dự án: duyệt giọng tập 1; ba phiên đang chạy
- **Giọng đọc tập 1 ĐẠT** (chủ dự án nghe bản ghép `reports/mr4/xem/tap01_giong_ghep.mp4`, gồm "Horwitz" ở P19 mốc 10:42) → dùng bản đã chọn ở MR-4 (P01_l2, còn lại bản 1); không thu lại.
- MR-5 (Veo + nhạc tập 1), MR-K23 (kịch bản tập 2 + 3), MR-D4 (dàn truyện tập 4) chạy song song.

## MR-5 + MR-K23 + MR-D4 · 02/11/2026 07:55 (giờ Hà Nội) · Điều phối rà — merge cả ba
Cả ba nhánh: preflight `--range` ĐẠT; 0 dòng email trong lịch sử.
**MR-5** (`ccr-af44ed0c-12rbdy`): sổ `calls.jsonl` OpenRouter **8,00 USD** / trần 8,30; ElevenLabs **3.245** / 6.000; chi phiên khác 0 trong cửa sổ phiên. Điều phối xem tờ 1 s 16 clip chọn (`reports/mr5/xem/to1s.jpg`): không mặt, không chữ đọc được, không logo; người chỉ ở dạng bóng (V06), tay (V07, V14, V16). Ghi chú nhỏ: chữ khắc giả trên chìa (V11) không đọc được ở 1080p → làm mờ ở M-d nếu thấy rõ khi phóng. Clip chọn `reports/mr5/veo/chon.json`. **Tập 1 M-c xong: Veo 9,20 USD (trần 9,50) + ElevenLabs 9.354 ký tự (trần 16.000).** Số dư OpenRouter sau: 17,65 USD. Còn mở: chủ dự án nghe nhạc `reports/mr5/xem/nhac.mp4`.
**MR-K23** (`claude/mr-k23-tap-2-3-3zvw9l`): chạy lại `scripts/mrk23/loi_md.py` hai tập → `loi: []` (K1–K8 + KA–KD đạt). HGLOBAL đọc đúng 1 lần (S028) + câu ◐ ngay sau (S029). Sunmola: đúng 1 câu ảnh riêng tư, thẻ chữ (S033, doc=false). Không từ cấm. Tập 2 ≈ 13:41, tập 3 ≈ 13:12.
**MR-D4** (`claude/theranos-holmes-tap-4-fmz9li`): N1 (CA9) đối chiếu: "convicted Holmes of four investor-related counts", "acquitted Holmes on the patient-related counts", "hung" ba tội nhà đầu tư, 135 tháng — khớp dàn truyện. 12 vòng kiểm độc lập.
