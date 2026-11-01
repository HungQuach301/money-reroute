# BÁO CÁO MR-K1 — Kho đề tài (QUY-TRINH 0.2 §4b)

> Phiên `[MR · MR-K1]`, 01/11/2026. Nhánh `claude/kho-de-tai-mr-k1-5pplwo`. Gốc nhánh là `187fa36`, commit điều phối phát lệnh MR-3 + MR-K1, nằm ngay sau `6296c0e`. Lệnh ghi "từ main @ 6296c0e"; `187fa36` chỉ thêm 4 dòng NHAT-KY, nên phiên không đổi gốc.
> **Chi thật: 0 USD.** Chỉ dùng hạn mức YouTube Data: **55/2000 đơn vị**, gồm **28/50 lượt `search.list`** và 27 `videos.list`. Cả 55 lượt trả HTTP 200, không có 402. Sổ: `reports/mrk1/calls.jsonl`.
> Phiên không merge, không xoá nhánh, không force-push. **DỪNG ở cuối mốc, chờ rà.**

## 1. Đã làm theo lệnh
| Bước | Kết quả | Tệp |
|---|---|---|
| 0 | Thêm dòng trần `"mrk1": {"youtube_units": 2000}` và `TRAN_LUOT_PHIEN "mrk1": {"search.list": 50}`, có ghi căn cứ lệnh. `budget.py` in đúng trần | `scripts/cp/budget.py` |
| 1 | **14 vụ** chia đều 6 trụ, trụ nào cũng có ≥ 2 vụ (bảng §2). Đã loại Woodbridge, 1inMM, Heartland | `docs/kho-de-tai/<vụ>.md` |
| 2 | Cả 14 nhân vật trung tâm đều ●. 13/14 vụ có ≥ 1 PDF sơ cấp của toà/DOJ (tổng 22 PDF) trong `ho-so/<vụ>/`, đẩy LFS, SHA-256 ghi ở §8 từng tệp. **Ngoại lệ là Rimasauskas** (§4.1) | `ho-so/*/` |
| 3 | Mỗi tệp vụ có 8 mục theo khuôn: tóm tắt có nguồn và trang · bảng tầng gọn (có cột loại phán quyết, kháng cáo/ân xá, ngày kiểm) · bước ngoặt · bài học và dấu hiệu · rủi ro (người không bị cáo buộc, nạn nhân dễ nhận diện, chi tiết cơ chế phải tránh, lỗ hổng nguồn) · đánh giá · đo cầu YouTube (chỉ số và id) · nguồn | 14 tệp |
| 4 | Bảng xếp hạng 5 tiêu chí kèm cầu YouTube, và gợi ý thứ tự 14 tập xoay trụ | `docs/kho-de-tai/KHO.md` |
| 5 | **Kiểm tầng độc lập trên cả 14 bảng tầng.** Có 5 tác tử kiểm, mỗi tác tử chỉ đọc §2 và §8 rồi mở lại nguồn đúng trang. Phiên đã áp các điểm sửa vào bảng tầng, mỗi chỗ ghi "sửa theo kiem" | `docs/kho-de-tai/kiem/*.md` |
| — | Công cụ đo cầu (dùng lại `scripts/mr1/yt.py`) và công cụ điền §7. Số đo thô chỉ lưu id, ngày, lượt xem; không lưu tiêu đề, mô tả hay thumbnail kênh khác | `scripts/mrk1/`, `reports/mrk1/do-cau/` |

## 2. Danh sách vụ (14)
| Trụ | Vụ | Nhân vật trung tâm · tầng · căn cứ | PDF then chốt |
|---|---|---|---|
| Ponzi/đầu tư | stanford-sib | R. Allen Stanford · ● · bồi thẩm 06/3/2012 (13/14 tội), 110 năm; CA5 giữ nguyên 2015; cert bị bác 2016 | judgment S.D. Tex. 2012; opinion CA5 12-20411; final judgment SEC 2025 |
| | petters-pci | Thomas Petters · ● · bồi thẩm 02/12/2009 (20/20 tội), 50 năm; CA8 2011 | opinion CA8 10-1843; lệnh bác §2255 (2013); lệnh bác compassionate release (27/4/2026) |
| Lừa tình & sextortion | romance-sunmola | Olayinka Sunmola · ● · nhận cả 8 tội giữa phiên xử 2016, 324 tháng; CA7 2018 | opinion CA7 17-1299 |
| | romance-alldred | Derek Alldred · ● · nhận tội 21/12/2017, 288 tháng; CA5 2019 | opinion CA5 18-40813 |
| | military-sextortion-wilkins *(dự phòng)* | Wendell Wilkins · ● · nhận tội **rửa tiền**, 66 tháng (2021) | cáo trạng D.S.C. 2:18-cr-1017 |
| Rửa tiền | 1mdb-ng | Roger Ng · ● · bồi thẩm 08/4/2022, 120 tháng; CA2 giữ nguyên 05/12/2025 | opinion CA2 23-6333; cáo trạng S-2; DPA Goldman 2020 |
| | bitfinex-lichtenstein | Ilya Lichtenstein (cùng Heather Morgan) · ● · nhận tội rửa tiền 03/8/2023, 60 tháng. **Không** bị kết án tội hack | memorandum opinion D.D.C. 04/4/2025 (bản GPO) |
| Gian lận doanh nghiệp | theranos-holmes | Elizabeth Holmes · ● · bồi thẩm 03/01/2022 (4 tội; trắng án 4, treo 3), 135 tháng; CA9 2025 | opinion CA9 22-10312 |
| | frank-javice | Charlie Javice · ● · bồi thẩm 28/3/2025, 85 tháng | complaint SEC 23-cv-2795 |
| Mạo danh & công nghệ | irs-callcenter-patel | Hitesh Patel · ● · nhận tội 09/01/2020, 20 năm | cáo trạng thay thế S.D. Tex. 4:16-cr-385 |
| | techsupport-popup-seward | Michael Seward · ● · nhận tội §1349, 113 tháng (2020) | cáo trạng thay thế S.D. Ill.; lệnh §2255 2022 |
| | bec-rimasauskas *(dự phòng)* | Evaldas Rimasauskas · ● · nhận tội wire fraud 20/3/2019, 60 tháng | **không có PDF**; chỉ có JSON thông cáo DOJ (§4.1) |
| Người trong cuộc | galleon-rajaratnam | Raj Rajaratnam · ● · bồi thẩm 11/5/2011 (14 tội), 132 tháng; CA2 2013; cert bị bác 2014 | opinion CA2 11-4416; opinion CA2 Gupta 12-4448 |
| | coinbase-wahi | Ishan Wahi · ● · nhận tội 07/02/2023, 24 tháng | cáo trạng S.D.N.Y. 22-cr-392; final judgment SEC (consent) |

Các vụ thay vụ gợi ý ban đầu trong lệnh giao tác tử: Sunmola và Seward là vụ thêm để mỗi trụ có đủ 2 vụ đạt chuẩn mà không phụ thuộc vào vụ có điều kiện. Lệnh của điều phối không nêu tên vụ cụ thể.

## 3. Kiểm tầng độc lập (bước 5)
- **Kết luận:** 1 vụ ĐẠT (Wahi), 13 vụ ĐẠT CÓ SỬA, **0 vụ KHÔNG ĐẠT**. Cả 14 nhân vật trung tâm đều được tác tử kiểm xác nhận ● theo luật 8a. SHA-256 khớp với mọi tệp, kể cả các tệp được tải lại để so.
- **Các điểm M (nói mạnh hơn nguồn), đã sửa:**
  - Alldred: "≈ 25 nạn nhân" sửa thành "ít nhất 25".
  - Wilkins: bỏ câu "nạn nhân là quân nhân trưởng thành", vì nguồn không ghi tuổi.
  - Petters: việc receiver đưa doanh nghiệp vào phá sản chỉ áp cho Sun Country và Polaroid, không có Fingerhut.
  - Rimasauskas: "Company-2" bị gắn ● dù không bị truy tố; đã bỏ.
  - Patel: chữ "chủ" chỉ là lời đồng phạm; lời nhận tội chỉ thừa nhận "operating and funding".
  - 1MDB: "người quyết định không chính thức" là lời khai của Leissner, không phải kết luận của toà. Khoản phạt của Goldman Malaysia là khoản thoả thuận; toà chấp nhận hay chưa thì chưa xác minh.
- **Các điểm S (sai), đã sửa:**
  - Wilkins: Teague được ghi là "nhận tội", nhưng nguồn chỉ nói "was sentenced"; số vụ của Dunbar thiếu nguồn.
  - Sunmola: đồng phạm mang giá trị tầng không có trong hiến chương.
  - Galleon: hai giá trị tầng không hợp lệ ("chưa xác minh", "được tuyên vô tội"). Đã tách thành Kumar/Goel ● (phiên tự mở lại thông cáo DOJ 21/03/2013, HTTP 200), các nguồn tin chưa có kết cục ghi "không nêu tên", và người thân trắng án ghi KHÔNG BỊ CÁO BUỘC (đã trắng án, không nêu tên).
  - Vài lỗi ghi chú nhỏ ở §8 về trang ân xá.
- **Các điểm TT (thiếu), đã bổ sung:**
  - Galleon và Coinbase: dòng dân sự SEC của Gupta, Rajaratnam (vụ thứ hai) và Nikhil Wahi.
  - Stanford: dòng consent SEC của Davis/Lopez và các đơn vị Stanford.
  - Trạng thái BOP của nhiều người.
  - Tên trùng thương hiệu lớn trong cáo trạng IRS: ghi KHÔNG BỊ CÁO BUỘC, không nêu tên.
  - 1MDB: các nhân vật chính trị Malaysia/Abu Dhabi có tên trong opinion: không nêu tên.
- **Phát hiện phải nhớ khi viết lời:**
  - BOP ghi Javice "released 04/04/2023" và không có ngày dự kiến ra tù. Lý do chưa mở được, nên không nói "đang ngồi tù".
  - Lichtenstein, Morgan, Seward và McCormick đã ra tù sớm hơn mức án. Lý do chưa xác minh, không suy đoán.
  - Ngày 27/4/2026 toà bác đơn trả tự do nhân đạo của Petters nhưng ghi "may well be appropriate at a future date". Phải kiểm lại khi chốt lời.

## 4. Lỗ hổng và sai lệch so với lệnh (báo trung thực)
1. **Rimasauskas không có PDF then chốt** (trái bước 2):
   - Tác tử thử 17 đường RECAP đều trả 404. Docket CourtListener trả 403; PACER cấm.
   - Đã lưu bản JSON 4 thông cáo DOJ lấy qua API chính thức (SHA-256 có ghi; tác tử kiểm so từng trường với API ngày 01/11: khớp).
   - Số docket 1:17-cr-00224 trong gợi ý của phiên không thấy ở đâu. Nguồn thứ cấp ghi 1:16-cr-00841 (chưa xác minh).
   - Hồ sơ không nêu tên công ty nào, nên vụ mất móc câu thương hiệu.
   - **Xếp dự phòng.** Trụ mạo danh vẫn đủ 2 vụ có PDF (Patel, Seward).
2. **Wilkins đạt §5 có điều kiện:**
   - Nguồn không ghi tuổi quân nhân bị hại, cũng không ghi tuổi người trong ảnh lấy từ Internet.
   - Yếu tố "vị thành niên" chỉ là lời bịa của kẻ tống tiền.
   - **Xếp dự phòng, chờ chủ dự án quyết.** Trụ lừa tình vẫn đủ 2 vụ (Sunmola, Alldred).
3. **1MDB, nguồn không chính thức:**
   - Lệnh Doc. 274 (Ng được giao trả Malaysia) chỉ đọc được qua bản sao do một hãng luật đăng. Đây không phải vượt rào, nhưng không phải đường chính thức.
   - Đã đánh dấu "nguồn không chính thức, chưa dùng được". Tệp này không lưu vào repo.
4. **govinfo:** một tác tử dùng API govinfo bằng khoá công khai `DEMO_KEY` do GPO cấp cho mọi người (miễn phí, đường chính thức). Ghi lại để điều phối biết.
5. **Gợi ý của phiên bị sai, tác tử đã đính chính:**
   - Năm nhận tội và tuyên án của Patel là 2020, không phải 2018.
   - Số docket của Rimasauskas (xem mục 1).
6. **Nguồn chưa mở được ở hầu hết các vụ:**
   - Judgment, plea agreement và docket toà quận (PACER cấm; trang docket và search CourtListener trả 403/401).
   - Vì vậy nhiều mức án của người phụ chỉ có trên báo chí, và đều đã ghi "chưa dùng".
   - Kháng cáo của Javice (2d Cir. 25-2895) chỉ thấy qua kết quả tìm kiếm.
7. **Ân xá:** mọi vụ đã tìm trên các trang ân xá của DOJ (Trump 2017–21, Trump 2025–nay cập nhật 20/10/2026, Biden), cả HTML lẫn PDF đính kèm có chữ: 0 kết quả. Một số PDF bản quét (khoảng 24 tệp) không tìm chữ được. Ghi là "chưa xác minh trọn vẹn" cho các danh sách tập thể.
8. **Đo cầu YouTube:**
   - Khớp tiêu đề là khớp thô. Một số từ khoá rộng ("frank", "irs", "navy", "virus", "google/facebook", "morgan") có ghi chú ở §7.
   - Truy vấn tên vụ Sunmola trả 0 video. Seward và Wilkins chưa đo truy vấn tên riêng.

## 5. Tuân thủ
- **Không vượt rào:**
  - Gặp 403/401 (CourtListener, Justia, BoingBoing) thì dừng, ghi "chưa mở được". Không đổi UA, không dùng archive/mirror, không dùng PACER.
  - DOJ đọc qua API chính thức `justice.gov/api/v1/press_releases.json` và các tệp đính kèm chính thức.
- **UA sec.gov:**
  - Chỉ dùng trong cờ `-A` của curl gõ trực tiếp, ở các tác tử cần sec.gov.
  - Quét toàn repo và toàn lịch sử nhánh (`git log -p origin/main..HEAD`): **0 địa chỉ email**. Tác giả và người commit đều là `noreply@anthropic.com`. Scratchpad cũng không có chuỗi UA.
- **Preflight:** chạy riêng trước mọi commit, và chạy `--range origin/main..HEAD` trước mọi lần đẩy. Chỉ commit/đẩy khi mã thoát 0 (gắn bằng `&&`, không qua pipe). Không dùng `--no-verify`.
- **LFS:** 22 PDF mới thuộc `ho-so/**/*.pdf`. Đây là tệp 0 USD nhưng thuộc vùng LFS đã có từ MR-1.
- **Nội dung:**
  - Không lưu ảnh, không mặt người thật.
  - Tệp có ảnh nạn nhân hoặc chi tiết cơ chế (vd Statement of Facts của vụ Bitfinex có tiền tố ví) đã được tác tử **cố ý không lưu**.
  - Người không bị cáo buộc ghi theo nhóm, không nêu tên.

## 6. Đề xuất cho điều phối / chủ dự án
1. **Wilkins (§5):** giữ làm dự phòng hay loại khỏi kho?
2. **Stanford, vụ SEC:** summary judgment có tranh chấp, dựa trên collateral estoppel của bản án hình sự. Xếp ● JUDGMENT hay ◐? (Không ảnh hưởng luật 8, vì trụ của vụ là ● hình sự.) Có nên ghi rõ "summary judgment có tranh chấp" vào HIEN-CHUONG §3?
3. **Sunmola:** nhánh tống tiền bằng ảnh riêng tư của phụ nữ trưởng thành. Nói ở mức khái niệm ("threatened to expose private images") hay bỏ hẳn?
4. **Thứ tự tập** (KHO.md §2): sau 1inMM, gợi ý Patel (mạo danh) → Sunmola (lừa tình) → Theranos (doanh nghiệp) → Woodbridge (Ponzi) → Galleon (người trong cuộc) → 1MDB (rửa tiền) → …
5. **Nâng độ chắc nguồn:** nếu chủ dự án cho trần PACER nhỏ ở một phiên sau, ưu tiên judgment của Javice (kèm docket kháng cáo), Rimasauskas và Patel.

**DỪNG — chờ điều phối rà.**
