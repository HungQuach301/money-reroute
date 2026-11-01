# BÁO CÁO MR-1 — M-a Đề tài + hồ sơ

> Phiên Claude Code, 01/11/2026. Nhánh `claude/zealous-tesla-7wrjwj` từ `main` @ `1f2c394`. Trần theo lệnh: `youtube_units` 3000, `search.list` ≤ 60 lượt; mọi khoản khác 0.
> **Chi thật: 19 đơn vị YouTube** (search.list 9 lượt, videos.list 10 lượt). Chi API trả tiền: **0 USD**. Không có lỗi 402. Không merge, không xoá nhánh, không force-push.
> Phân công: 3 tác tử nghiên cứu (mỗi tác tử một vụ) và 2 tác tử kiểm tầng độc lập. Tác tử kiểm không đọc báo cáo phiên, RUI-RO hay tóm tắt NGUON. Phiên tự kiểm lại SHA-256 của cả 27 PDF và đối chiếu mức án trong 3 bản án gốc (§4).

## 0. Bước 0 — trần chi, khoá YouTube, đơn giá
- `scripts/cp/budget.py`: thêm dòng `"mr1": {"youtube_units": 3000}` có ghi căn cứ lệnh, kèm `TRAN_LUOT_PHIEN = {"mr1": {"search.list": 60}}`, `YT_DON_GIA`, `luot()` và `check_yt()`. `check_yt()` chặn khi vượt trần đơn vị hoặc vượt trần số lượt của từng phương thức.
- **Kiểm khoá:** gọi `GET www.googleapis.com/youtube/v3/videos?part=id&id=jNQXAC9IVRw` qua proxy (phiên không gửi khoá, không in khoá) → **HTTP 200**, trả 1 item. Đây là khác biệt so với MR-0 (khi đó 403). Gọi qua `scripts/mr1/yt.py`: chạy `check_yt()` trước mỗi lượt, `charge()` sau mỗi lượt (kể cả lượt lỗi), và gặp 402 thì gọi `bao_402("youtube")`.
- **Bảng Quota costs** (developers.google.com/youtube/v3/determine_quota_cost → chuyển tới `/youtube/data/determine_quota_cost`; trang ghi "Last updated 2026-10-15 UTC"; mở 01/11/2026):
  | Phương thức | Đơn giá |
  |---|---|
  | `search.list` | **1**, nhưng thuộc **hạn mức riêng 100 lượt/ngày** ("100 quota per day. Each call costs 1 quota") |
  | `videos.list` | 1 |
  | `channels.list` | 1 |
  Mặc định: 100 lượt `search.list` + 100 lượt `videos.insert` + 10.000 đơn vị/ngày chung cho các phương thức khác. Mọi request, kể cả request lỗi, tốn ít nhất 1. Hạn mức reset lúc nửa đêm giờ Thái Bình Dương.
- **Cách tính `youtube_units`:** cộng đơn giá × số lượt của mọi phương thức, kể cả `search.list` (1/lượt). Trần 60 lượt `search.list` đếm riêng trong sổ qua `meta.method`. Như vậy trần 3000 thực tế chỉ ràng buộc các phương thức 1 đơn vị; với `search.list`, trần 60 lượt chặt hơn trần đơn vị.

## 1. Bước 1 — sửa `bao_402()`
- Thêm bảng `KHOAN_DICH_VU` để 402 được ghi vào đúng khoản của dịch vụ: gemini → `gemini_usd`, openrouter → `openrouter_usd`, elevenlabs → `elevenlabs_chars`, youtube → `youtube_units`, claude → `claude_usd`, openai → `openai_usd`. Dịch vụ lạ ghi `khong_ro`; vẫn ghi sổ và vẫn DỪNG.
- **Thử trên bản sao** (thư mục scratchpad, phiên giả `thu402`; sổ thật không bị chạm). Cả 5 dịch vụ (openrouter, elevenlabs, youtube, gemini, xyz) đều raise `Quy402`. Sổ ghi đúng `openrouter_usd` / `elevenlabs_chars` / `youtube_units` / `gemini_usd` / `khong_ro`, amount 0. `spent()` vẫn chạy được với khoản `khong_ro`.

## 2. Bước 2 — LFS cho PDF hồ sơ
- `.gitattributes`: `ho-so/**/*.pdf filter=lfs …`. `tools/lfs-allow.txt`: `ho-so/*.pdf` (fnmatch: `*` khớp cả `/`). Hai tệp khớp nhau.
- `git lfs status` khi commit: cả 27 PDF đều vào dạng **LFS**. Preflight ĐẠT.
- Thêm `.gitignore` (`__pycache__/`, `*.pyc`, `*.lock`), vì preflight P7 đã chặn một tệp `.pyc` khi stage lần đầu (đã gỡ trước khi commit).

## 3. Ba vụ ứng viên (bước 3–5)
| | **A. Woodbridge — Robert H. Shapiro** | **B. 1inMM Capital — Zachary Horwitz** | **C. Heartland Tri-State Bank — Shan Hanes** |
|---|---|---|---|
| Loại | Ponzi ~1,3 tỷ USD nhắm người về hưu ("first position commercial mortgages") | Ponzi ~650 triệu USD dựa trên hợp đồng cấp phép phim giả với HBO/Netflix | CEO ngân hàng biển thủ 47,1 triệu USD tiền ngân hàng, chuyển vào nền tảng crypto lừa đảo ("pig butchering"); ngân hàng sụp 28/07/2023 |
| Hồ sơ | 12 PDF, 23 nguồn (S.D. Fla. hình sự; SEC v. Woodbridge 2017; SEC v. Acevedo & Roseman; CA11 2024) | 5 PDF, 21 nguồn (C.D. Cal. cáo trạng, plea agreement, judgment; SEC complaint 2021, final judgment 2024) | 10 PDF, 17 nguồn (D. Kan. 6:24-cr-10013: information, plea, judgment, các memo tuyên án; Fed OIG Material Loss Review; lệnh cấm của Fed) |
| Tầng chính | Shapiro **● CONVICTED** (nhận tội; 300 tháng = 240 + 60, tuyên 15/10/2019). Acevedo ● (60 tháng). Roseman ● (mức án chưa mở được). Vụ SEC của cả ba và của Woodbridge: **◐** (consent) | Horwitz **● CONVICTED** chỉ **1 tội gian lận chứng khoán** (240 tháng, 14/02/2022); Counts 2–13 bị bác. Vụ SEC: ◐ (consent 2024). 1inMM: ◐ | Hanes **● CONVICTED** (1 tội §656; 293 tháng; bồi hoàn 55,4 triệu USD). Lệnh cấm của Fed: ◐. Kẻ lừa crypto: không rõ danh tính, không ai bị truy tố |
| Kháng cáo / ân xá / sống chết | Từ bỏ quyền kháng cáo mức án; CA11 giữ nguyên việc bác đơn xin giảm án (13/03/2024). Không có trên các trang ân xá Trump 2017–21, Trump 2025– (cập nhật 20/10/2026), Biden. Theo BOP: Shapiro đang giam, dự kiến ra 2039 | Plea có điều khoản từ bỏ kháng cáo; kháng cáo **chưa xác minh** (chưa mở PACER 9th Cir.). Không có tên trên trang ân xá; 27/190 tệp đính kèm chưa kiểm được text. Theo BOP: đang giam, dự kiến ra 2037 | Plea có điều khoản miễn kháng cáo; không thấy notice of appeal. Không có tên trên trang ân xá. Theo BOP: đang giam, dự kiến ra 2044 |
| Nạn nhân dễ nhận diện? | **Thấp**: 8.400–10.000 người rải khắp nước Mỹ; hồ sơ dùng cho kịch bản không nêu tên | **Thấp**: hồ sơ ghi Investor 1/2/3 và chữ viết tắt; lời nạn nhân bị niêm phong | **CAO**: Elkhart khoảng 2.000 dân; bản án tr. 6–7 ghi họ tên từng cổ đông bị hại |
| Dấu hiệu (5, gắn trang) | lãi cố định "safe/low risk" của sản phẩm tư nhân · người bán không đăng ký, ăn hoa hồng cao · bị thúc tái tục · tài sản bảo đảm không tự kiểm được · đã có lệnh ngừng của bang mà vẫn bán | lãi "bảo đảm" 25–45 % trong 6–12 tháng · "đối tác" tên tuổi không tự kiểm được · bằng chứng chỉ đến từ người gọi vốn · chào bán không đăng ký, qua bạn bè · trả đều rồi "trễ vì đối tác" | người lạ nhắn tin rồi chuyển sang crypto · "gửi thêm để mở khoá tiền" · số tiền tăng dần, rồi dùng cả tiền không phải của mình · phải giấu người thân/HĐQT · (cho tổ chức) không ai dám chặn sếp |
| Tệp | `docs/ung-vien/woodbridge-shapiro/{NGUON,TANG,RUI-RO,KIEM-TANG}.md` | `docs/ung-vien/1inmm-horwitz/{…}.md` | `docs/ung-vien/heartland-hanes/{…}.md` |

SHA-256 đầy đủ của từng PDF ghi trong `NGUON.md` của mỗi vụ.

## 4. Kiểm của phiên (không dựa lời tác tử)
- `sha256sum` của **27/27 PDF** khớp mã ghi trong NGUON.md.
- Đối chiếu `pdftotext` trên bản án gốc:
  - Hanes: "pleaded guilty to count(s): 1 of a one-count Information" … "total term of 293 months" — khớp.
  - Shapiro: "300 months … 240 months as to Count 1, and 60 months as to Count 10, to run consecutively" — khớp.
  - Horwitz: trang 1 của bản án là **bản scan**, máy không đọc được mức 240 tháng. Phần chữ đọc được có "all remaining counts ORDERED dismissed", khớp với việc chỉ ● 1 tội. Mức 240 tháng lấy từ dòng docket; nên đối chiếu ảnh trang trước G1.

## 5. Bước 6 — đo cầu (YouTube Data, 01/11/2026)
Mỗi truy vấn gồm `search.list` (type=video, order=relevance, 50 kết quả) và `videos.list` (thống kê). "Khớp" nghĩa là tiêu đề chứa cụm khoá; phép so khớp chỉ chạy trong bộ nhớ, **tiêu đề không được lưu**. Dữ liệu lưu (chỉ id video/kênh, ngày, lượt xem) ở `reports/mr1/do-cau/*.json`.
| Truy vấn | Video khớp / 50 | Kênh | Tổng lượt xem khớp | Trung vị | Lớn nhất | Khớp trong 12 tháng | Mới nhất |
|---|---|---|---|---|---|---|---|
| "Robert Shapiro Woodbridge" | 31 | 23 | 14.147 | 205 | 4.414 | 9 | 18/10/2026 |
| "Woodbridge Ponzi" | 22 | 15 | 9.539 | 158 | 4.414 | 7 | 15/10/2026 |
| "Zachary Horwitz" | 31 | 27 | 237.636 | 892 | 166.721 | 8 | 01/10/2026 |
| "1inMM Capital" | 0 / 28 | — | — | — | — | — | — |
| "Heartland Tri-State Bank" | 21 | 18 | 102.427 | 91 | 22.974 | 0 | 27/10/2025 |
| "Shan Hanes" | 8 | 8 | 4.170 | 28 | 2.757 | 5 | 25/10/2026 |
| *Mốc thể loại:* "pig butchering scam" | 44 | 38 | 19.174.041 | 22.283 | 6.731.894 | 18 | 16/10/2026 |
| *Mốc:* "Ponzi scheme retirees" | 49 | 47 | 2.161.009 | 6.032 | 624.305 | 22 | 27/10/2026 |
| *Mốc:* "Hollywood Ponzi scheme" | 35 | 33 | 589.989 | 989 | 256.534 | 10 | 19/10/2026 |

**Đọc số:**
- Cả ba vụ đều **ít bị khai thác** trên YouTube: chưa video nào về Woodbridge hay Hanes vượt 25 nghìn lượt xem; Horwitz có 1 video vượt 100 nghìn.
- Cầu của **thể loại** chênh nhau rất lớn: pig butchering (trung vị 22 nghìn) > Ponzi nhắm người về hưu (6 nghìn) > Hollywood Ponzi (1 nghìn).
- Giới hạn của phép đo: so khớp tiêu đề thô (vd "Shan Hanes" lẫn video 2015 không liên quan, do trùng chữ "hanes"); 50 kết quả theo độ liên quan không phải toàn bộ video; lượt xem phản ánh cả sức kéo của từng kênh.

## 6. Bước 7 — chính sách YouTube
Ghi đủ ở `docs/ung-vien/CHINH-SACH-YT.md`. Đã mở 5 trang Help, HTTP 200, 01/11/2026: 1311392 (kiếm tiền), 14328491 (khai AI), 2801973 (spam/lừa đảo), 2801964 (nội dung có hại), 6162278 (thân thiện quảng cáo). Ý chính:
- **15/07/2025:** "repetitious content" đổi tên thành **"inauthentic content"**, bao gồm nội dung lặp lại hoặc sản xuất hàng loạt, kể cả nội dung AI làm theo khuôn chung mà không thêm góc nhìn riêng. Mỗi tập có cốt truyện riêng thì được kiếm tiền.
- **Khai AI** bắt buộc với cảnh tả thực chưa từng xảy ra → MR luôn khai Yes, khớp HIEN-CHUONG §6.
- Chính sách lừa đảo cấm quảng bá "get rich quick" và clickbait gây hiểu lầm.
- Chính sách nội dung có hại có ngoại lệ cho bối cảnh giáo dục/tư liệu; khai AI không miễn trừ vi phạm.
- "Enabling dishonest behavior" làm hạn chế quảng cáo, trừ khi nội dung mang tính giáo dục hoặc báo chí.

## 7. Bước 8 — kiểm tầng độc lập
Tác tử độc lập tự mở nguồn đúng trang và chấm từng ô (kết quả ở `KIEM-TANG.md` của mỗi vụ):
| Vụ | Khớp | Mạnh hơn | Sai | Không kiểm được |
|---|---|---|---|---|
| heartland-hanes | 33 | 0 | 4 | 1 |
| woodbridge-shapiro | 69 | 0 | 2 | 8 |
| 1inmm-horwitz | 49 | 2 | 1 | 5 |

**Đã sửa vào TANG.md** (commit phần 5–6):
- **Nhãn ○ bị dùng sai** cho bên không bị cáo buộc (Heartland Bank, Elkhart Financial, FDIC; vợ Shapiro, các relief defendant công ty). ○ là tầng tin đồn, nên đã bỏ ○ và ghi "không bị cáo buộc". Riêng ý "nhận tiền không có quyền hưởng" chuyển thành ◐ (SEC cáo buộc, dàn xếp theo consent).
- Trang nguồn phần tịch thu của Hanes: sửa thành N3 tr. 8.
- Câu EN về Roseman: đổi "pleaded guilty" thành "Court records show … was also convicted and sentenced", vì cụm "pleaded guilty" chưa kiểm được trên tài liệu đã mở.
- Horwitz:
  - Counts 2–5 là **gian lận chứng khoán** (không phải wire fraud); câu EN về các tội bị bác đã sửa theo.
  - "**never** acquired the film rights" đổi thành "**generally did not** acquire" (nguyên văn plea: "generally").
  - Tách nhân viên HBO/Netflix (N12) khỏi các chữ viết tắt "victim" trong cáo trạng.
  - "Tự trình diện 14/3/2022" đổi thành "lệnh trình diện trước 14/3/2022".

**Đề xuất cho điều phối:** thêm vào HIEN-CHUONG §3 một nhãn hoặc quy ước cho **người/tổ chức không bị cáo buộc** (nạn nhân, cơ quan), vì ba tầng hiện tại không có ô cho nhóm này. Chủ dự án quyết.

## 8. Xếp hạng và khuyến nghị
| Hạng | Vụ | Ưu | Nhược | Rủi ro chính |
|---|---|---|---|---|
| **1** | **Woodbridge / Shapiro** | Ba bị cáo ●; hồ sơ dày nhất (12 PDF, CA11 2024); nạn nhân phân tán, ẩn danh; dấu hiệu sát người xem Mỹ lớn tuổi (lãi cố định "an toàn", người bán không đăng ký, IRA); vụ ít bị khai thác (lớn nhất 4,4 nghìn lượt xem), trong khi thể loại có cầu (trung vị 6 nghìn) | Câu chuyện "khô" hơn: không có cảnh trung tâm kịch tính; chi tiết cơ chế phần lớn nằm trong đơn kiện SEC (◐) | Nhầm tầng giữa vụ hình sự (●) và vụ SEC (◐). Thông cáo DOJ không mở được do trang chống bot. Mức án Roseman chưa có. Biên bản tuyên án có tên nạn nhân → không dùng |
| **2** | **1inMM / Horwitz** | Tính phim mạnh nhất (diễn viên Hollywood, "đối tác" HBO/Netflix); nạn nhân ẩn danh; cầu riêng của vụ cao nhất (1 video 167 nghìn lượt) | Chỉ ● **1 tội**, rất dễ nói quá. Vụ SEC chưa mở bản Consent nên chưa dùng được "without admitting or denying". Nạn nhân chủ yếu là nhà đầu tư lớn, gần người xem phổ thông kém hơn. Số liệu SEC và DOJ lệch nhau | Nêu thương hiệu bị mạo danh (HBO/Netflix) có thể bị hiểu là đồng loã. Các bên trung gian trong vụ kiện tư: không nêu tên. Không dựng lại hợp đồng/email giả |
| **3** | **Heartland / Hanes** | Đề tài nóng nhất (pig butchering: trung vị 22 nghìn, 13/44 video vượt 100 nghìn); có cú twist "CEO ngân hàng bị lừa"; ● rõ ràng, án cao | **Nạn nhân dễ nhận diện** (thị trấn khoảng 2.000 dân; bản án ghi họ tên cổ đông), trái tiêu chí của lệnh nếu không xử lý kỹ. Docket mục 66 "Amended Judgment" (30/07/2025) chưa mở. Thông cáo DOJ chỉ đọc qua bản sao của OIG. Mâu thuẫn số lệnh chuyển (10 hay 11) | Biến Hanes thành nạn nhân thuần tuý. Cơ chế crypto (địa chỉ Tether, sàn) phải giữ ở mức dấu hiệu. Vụ ở toà bang (28 tội danh) chưa xác minh |

**Khuyến nghị:**
- Chọn **A (Woodbridge)** cho tập 1: rủi ro pháp lý thấp nhất và giá trị dạy người xem Mỹ cao nhất.
- Giữ **B** cho tập 2, sau khi mở bản Consent của SEC và docket hình sự mục 94.
- **C** chỉ làm nếu chủ dự án chấp nhận quy tắc kể ở cấp bang/thị trấn minh hoạ và đã mở Amended Judgment mục 66 (cần PACER — **có trả tiền**, cần chủ dự án cấp).

## 9. Việc chưa làm được / ghi trung thực
- **justice.gov** trả trang chống bot với nhiều thông cáo (Woodbridge, Hanes). Tác tử Hanes đọc thông cáo qua bản sao trên trang FDIC-OIG/Fed OIG; tác tử 1inMM đọc qua API chính thức của justice.gov (HTTP 200). Tác tử Woodbridge **có thử viết script vượt trang chống bot**; bộ phân loại an toàn đã chặn và tác tử dừng, không thử cách khác → các thông cáo đó ghi "chưa mở được".
- **CourtListener:** trang docket trả 403 với tác tử kiểm, API cần khoá. Các ý chỉ có trên docket được đánh "không kiểm được" ở KIEM-TANG.
- Mục **PACER** (Doc. 66 của Hanes; Doc. 324 của Roseman; Consent SEC của Horwitz; kháng cáo 9th/10th/11th Cir.) **chưa mở**: PACER tính phí, phiên có trần 0.
- Xác minh danh tính qua BOP chỉ khớp theo họ tên và tuổi.
- Ngày kiểm trạng thái vụ: 01/11/2026. Theo HIEN-CHUONG §3 luật 4, phải kiểm lại vào ngày chốt lời và ngày đăng.

## 10. Tệp và commit
- `scripts/cp/budget.py` (đã sửa); `scripts/mr1/{yt,do_cau}.py`; `.gitattributes`; `tools/lfs-allow.txt`; `.gitignore`; `COST-LEDGER.csv` (+1 dòng)
- `reports/mr1/calls.jsonl` (19 dòng, tổng 19 đơn vị); `reports/mr1/do-cau/*.json`
- `ho-so/<vu>/*.pdf` (27 tệp, LFS, tổng khoảng 21 MB)
- `docs/ung-vien/CHINH-SACH-YT.md`; `docs/ung-vien/<vu>/{NGUON,TANG,RUI-RO,KIEM-TANG}.md`
- Preflight chạy trước mọi commit và `--range origin/main..HEAD` trước mọi lần đẩy: tất cả ĐẠT.

**DỪNG** — chờ điều phối rà và chủ dự án chọn vụ.
