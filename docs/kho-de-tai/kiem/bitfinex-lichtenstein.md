# Kiểm tầng độc lập — bitfinex-lichtenstein · MR-K1 · 01/11/2026

Phạm vi: chỉ §2 "Bảng tầng gọn" và §8 "Nguồn" của `docs/kho-de-tai/bitfinex-lichtenstein.md`. Không đọc §1, §3–§7, `reports/` hay báo cáo của tác tử khác. Nguồn mở lại trực tiếp ngày 01/11/2026: N4 (PDF quét, xem ảnh trang 1–5 bằng `pdftoppm`), DOJ qua API `press_releases.json` và trang vụ, N5 qua RECAP storage (không lưu vào repo), BOP Inmate Locator JSON, trang ân xá DOJ + tệp đính kèm. Không mở sec.gov. Không gọi API trả tiền.

## Kết luận
**ĐẠT CÓ SỬA (nhẹ).** Hai bị cáo đều ở ● đúng nguồn (nhận tội 03/8/2023, judgment 03/12 và 11/12/2024); tội danh khớp N4 tr. 2; ranh giới tội danh được giữ đúng — **không ai bị kết án tội hack/trộm** (N4 tr. 3: hết thời hiệu; tr. 5: "not charged with hacking"). Không có ô nâng tầng. Chỉ cần làm rõ cách diễn đạt "bồi hoàn 0 USD", ghi chú lệch giữa N2 và N4 về tội danh của Morgan, và cập nhật §8 N8 (trang giảm án Biden nay mở được, 0 kết quả).

## Bảng chấm
| Dòng bảng tầng | Ô | Điểm | Nguồn đã mở + trang | Ghi chú / sửa đề xuất |
|---|---|---|---|---|
| Ilya Lichtenstein | Vai trò: "theo DOJ là người hack và đầu não rửa tiền" | K — **giữ ràng buộc** | N1, N2 ("According to court documents, Lichtenstein hacked into Bitfinex's network in 2016"); N3 ("defendant Ilya Lichtenstein hacked into…") | Quy gán cho DOJ là đúng. Lưu ý N1: phần **"admitted" trong plea** chỉ là các kỹ thuật rửa tiền; câu về hack là "according to court documents". Lời thoại phải luôn đi kèm "không bị kết án tội hack" (N4 tr. 3). |
| Ilya Lichtenstein | Tầng ● CONVICTED | K | N4 tr. 2 ("entered a plea of guilty"), tr. 5 (Judgment ECF 195); N2 (tuyên án 14/11/2024) | Nhân vật trung tâm ở ● đúng luật 8a. |
| Ilya Lichtenstein | Nhận tội 03/8/2023; Judgment ghi docket 03/12/2024 | K | N4 tr. 2 ("On August 3, 2023…"), tr. 5 ("Judgments were entered on the docket on December 3, 2024 [Lichtenstein]") | — |
| Ilya Lichtenstein | Âm mưu rửa tiền § 1956(h) | K | N4 tr. 2; N3; N1 | — |
| Ilya Lichtenstein | 60 tháng tù + 3 năm giám sát | K | N2 (bản USAO-DC: "sentenced today … to 60 months in federal prison"; "three years of supervised release"; ngày đăng 14/11/2024) | N4 tr. 4 xác nhận ngày tuyên án 14/11/2024. |
| Ilya Lichtenstein | Không bị kết án tội hack/trộm (hết thời hiệu, N4 tr. 3) | K | N4 tr. 3 ("neither Defendant was convicted of 'intrusion into the network' (i.e., the hacking of Bitfinex) or with the theft of the cryptocurrency, as those offenses were time barred"); tr. 5 ("the Defendants were not charged with hacking") | Ranh giới đúng. Lưu ý tr. 3 ghi đây là **lập luận của Chính phủ** trong Consent Motion (ECF 141 tr. 5), được toà thuật lại. |
| Ilya Lichtenstein | Bồi hoàn: 0 USD (N4 tr. 2) | K — **làm rõ** | N4 tr. 2 ("$0 restitution shall be awarded to Bitfinex; … disposal of the forfeited assets shall proceed solely through a third-party forfeiture ancillary proceeding") | Đề xuất: "Toà quyết định 0 USD bồi hoàn cho Bitfinex; tài sản đã tịch thu được phân xử qua thủ tục ancillary cho bên thứ ba". Tránh hiểu thành "không phải trả gì". |
| Ilya Lichtenstein | Kháng cáo: chưa xác minh | KKĐ (ghi đúng) | Docket không mở được (CourtListener API cần xác thực; PACER cấm) | Giữ "chưa xác minh". |
| Ilya Lichtenstein | Ân xá/giảm án: không có (N8) | K | Trang Trump 2025– (cập nhật 20/10/2026): 0 kết quả; 130/138 tệp có chữ: 0 kết quả "Lichtenstein", 0 kết quả số tù 85167-509; 8 tệp không có chữ đều mang tên người khác; trang Biden pardons (cập nhật 14/5/2026) và commutations (cập nhật 09/7/2025): 0 kết quả | — |
| Ilya Lichtenstein | BOP: đã ra tù 23/01/2026; lý do ra sớm chưa xác minh | K | BOP JSON: ILYA LICHTENSTEIN, 85167-509, releaseCode R, actRelDate 01/23/2026 (cơ sở ghi "Sacramento") | Giữ "lý do chưa xác minh"; không dùng giải thích của báo chí. |
| Heather Rhiannon Morgan | Tầng ● CONVICTED · nhận tội 03/8/2023; Judgment 11/12/2024 | K | N4 tr. 2, tr. 5 ("December 11, 2024 [Morgan]"); N3 (tên đầy đủ "Heather Rhiannon Morgan") | Vai trò "giúp rửa tiền" khớp N1, N3. |
| Heather Rhiannon Morgan | Âm mưu rửa tiền (§§ 371, 1956(a)(1)(B)(i)) + âm mưu lừa gạt Hoa Kỳ (§ 371) | K — **ghi chú** | N4 tr. 2; N3; N1 ("one count of money laundering conspiracy and one count of conspiracy to defraud the United States") | N2 viết "Lichtenstein and Morgan both pleaded guilty to one count of conspiracy to commit money laundering" — **thiếu** tội thứ hai của Morgan. Bảng theo N4 là đúng; không trích câu này của N2 cho Morgan. |
| Heather Rhiannon Morgan | Mức án: chưa mở được hồ sơ sơ cấp | K (ghi đúng) | API DOJ "Morgan Sentenced", "Bitfinex": không có thông cáo tuyên án Morgan; N4 tr. 4 chỉ cho ngày tuyên án 18/11/2024 | Có thể thêm ngày tuyên án 18/11/2024 (N4 tr. 4). |
| Heather Rhiannon Morgan | BOP: ra tù 12/12/2025; không có trong danh sách ân xá | K | BOP JSON: HEATHER MORGAN, 85215-509, R, 12/12/2025; N8 0 kết quả | BOP có **một Heather Morgan khác** (47430-074, ra 2016) — luôn định danh bằng số 85215-509. |
| Bitfinex (iFinex Inc. và BFXNA) | KHÔNG BỊ CÁO BUỘC | K | N4 tr. 1 chú thích 1 ("iFinex Inc. and BFXNA together are referred to as Bitfinex") | Tổ chức bị hại, tên có trong hồ sơ toà; nêu được. |
| Chủ tài khoản Bitfinex 2016 ("có thể hàng nghìn") và người nộp đơn | KHÔNG BỊ CÁO BUỘC, không nêu tên | K | N4 tr. 1 (John Doe, et al., Petitioners/Third-Party Claimants), tr. 3 chú thích 2 ("potentially thousands of [Bitfinex] accountholders") | Chú thích 2 là lời Chính phủ được trích. |
| Sàn, chợ darknet, dịch vụ trộn tiền | Không xếp tầng, không nêu tên | K | N1 (nêu tên ba dịch vụ trộn tiền); N5 tr. 3 ¶7 (nêu tên một chợ darknet; các sàn ẩn danh VCE 1–10) | Cách xử lý "không nêu tên" an toàn với luật 8c. |
| (kiểm TT) | Người có tên trong nguồn đã mở | Không có TT | N5 tr. 1 chỉ nêu tên đặc vụ IRS-CI (quan chức, không bị cáo buộc) | Không cần dòng mới; không nêu tên đặc vụ trong kịch bản. |
| §8 N8 | "trang giảm án Biden: 404 (chưa mở được)" | **S** (nhẹ) / cập nhật | https://www.justice.gov/pardon/commutations-granted-president-joseph-biden-2021-2025 → 200, 0 kết quả; 29 tệp đính kèm | Cập nhật N8: trang này nay mở được, 0 kết quả. Số tệp trang Trump: 138, không phải 116. |

Kiểm thêm:
- (a) Nhân vật trung tâm ở ● theo luật 8a: **có** (N4 tr. 2, 5; N2).
- (b) Tên cá nhân không bị cáo buộc: không có trong bảng; chủ tài khoản và người nộp đơn được giữ ẩn danh.
- (c) SHA-256: 1/1 khớp.
- (d) §5 HIEN-CHUONG (yếu tố tình dục): không áp dụng.
- Ranh giới tội danh: đúng — cả hai chỉ bị kết án tội âm mưu rửa tiền (và Morgan thêm âm mưu lừa gạt Hoa Kỳ); **không ai bị kết án tội hack hay trộm**. Mọi câu "hacker" phải quy gán ("DOJ says / according to court documents") và kèm câu này.

## SHA-256
| Tệp | Ghi trong §8 | Tính lại 01/11/2026 | Khớp? |
|---|---|---|---|
| `ho-so/bitfinex-lichtenstein/ddc-memorandum-opinion-restitution-2025.pdf` (20 tr., bản quét, có tem GPO xác thực) | `00bdf7f6f4acf6d425e6c0aae1e7a05f71df677fc2af3009ac46d3a322e35bfd` | `00bdf7f6f4acf6d425e6c0aae1e7a05f71df677fc2af3009ac46d3a322e35bfd` | Có |

## Không kiểm được
| URL | Lý do |
|---|---|
| Docket D.D.C. 1:23-cr-00239 (kháng cáo, mức án Morgan) | CourtListener API: 401/403 cho người dùng ẩn danh → dừng; PACER cấm. |
| Lý do Lichtenstein ra tù sớm | Không có trong nguồn chính thức đã mở; BOP chỉ cho ngày ra. |
