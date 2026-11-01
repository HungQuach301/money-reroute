# Kiểm tầng độc lập — techsupport-popup-seward · MR-K1 · 01/11/2026

Phạm vi: chỉ §2 "Bảng tầng gọn" và §8 "Nguồn" của `docs/kho-de-tai/techsupport-popup-seward.md`. Nguồn mở lại bằng đường chính thức ngày 01/11/2026: hai PDF trong `ho-so/`, GovInfo, API DOJ, BOP và các trang ân xá DOJ.

## Kết luận
**ĐẠT CÓ SỬA.** Mọi ô tầng, tội danh và mức án đều khớp nguồn. Nhân vật trung tâm (Michael Austin Seward) ở tầng ●. Không có ô nào nói mạnh hơn nguồn. Cần sửa nhỏ 3 điểm: (1) ngày tuyên án Wasik không thống nhất giữa hai thông cáo DOJ; (2) bản ghi BOP của Lawing hiện ở trạng thái bất thường mà bảng ghi "Không kiểm"; (3) cột nguồn của Lawing cần thêm N6.

## Bảng chấm
| Dòng bảng tầng | Ô | Điểm | Nguồn đã mở + trang/đoạn | Ghi chú / sửa đề xuất |
|---|---|---|---|---|
| Michael Austin Seward | Vai trò: người sáng lập, đồng chủ, CEO Client Care/First Choice, đồng chủ ABC Repair Tech | K | N1 tr. 6 ¶23 "one of the owners of Client Care/First Choice and ABC Repair Tech… CEO"; N6 "Seward was the founder and chief executive officer" | — |
| Michael Austin Seward | Tầng ● CONVICTED | K | N3: "have both pleaded guilty to a federal indictment charging them with conspiracy to commit wire fraud"; N6 tuyên án | Đúng luật 8a. |
| Michael Austin Seward | Loại phán quyết: nhận tội, toà chấp nhận (trước 14/08/2019) | K | N3, ngày API 14/08/2019 | N3 không có chữ "accepted"; việc tuyên án (N6) xác nhận lời nhận tội có hiệu lực. |
| Michael Austin Seward | Tội: §1349; 113 tháng; bồi hoàn > 11,5 triệu USD (10/02/2020) | K | N1 tr. 1, 7 (Count One §1349); N6 ngày API 11/02/2020: "Yesterday… 113 months and 132 months… over $11.5 million in restitution"; N7 tr. 1 xác nhận ngày tuyên án 10/02/2020 | Khoản "over $11.5 million" trong N6 là mức chung cho cả Seward và McCormick. Không viết thành "mỗi người 11,5 triệu" nếu chưa có judgment. |
| Michael Austin Seward | Kháng cáo | KKĐ | — | PACER bị cấm; GovInfo package `USCOURTS-ilsd-3_17-cr-30192` chỉ có 2 văn bản (Doc 272, 273). |
| Michael Austin Seward | Ân xá / giảm án | K | 5 trang Office of the Pardon Attorney (HTTP 200) cùng 179 PDF danh sách đính kèm; tìm "Seward": 0 kết quả | Ngoại lệ: 24 PDF quét ngắn không tìm chuỗi được. |
| Michael Austin Seward | BOP: đã ra 14/11/2023, lý do chưa rõ | K / KKĐ (lý do) | JSON BOP: MICHAEL AUSTIN SEWARD, 39 tuổi, số 18857-104, Miami, releaseCode R, actRelDate 11/14/2023 | Có 2 bản ghi Michael Seward khác (tên đệm D và James) không liên quan. Ngày ra tù sớm so với mức 113 tháng: không được suy đoán lý do (luật 8f). Chỉ nói "BOP records show he was released in November 2023". |
| Kevin James McCormick | ● CONVICTED (tội vẫn đứng); nhận tội 12/08/2019 (hợp tác) | K | N7 tr. 2: "explored a possible cooperation plea agreement… McCormick pled guilty on August 12, 2019"; N7 tr. 6–7: chỉ VACATES sentence, không đi vào grounds 2–3 (tính tự nguyện của plea) | Đúng: chỉ mức án bị huỷ, lời nhận tội không bị huỷ. |
| Kevin James McCormick | 132 tháng (10/02/2020); mức án bị huỷ 27/01/2022 (§2255) | K | N7 tr. 1 và 7: "sentenced him to serve 132 months… VACATES McCormick's sentence imposed on February 10, 2020"; ký ngày 27/01/2022 | Doc 273 (GovInfo `…-1.pdf`, 1 tr., đã đọc): toà giao ông cho US Marshal "pending resentencing". Bảng đã ghi đúng là mức án mới "chưa mở được". Lý do huỷ án là luật sư cũ kém hiệu quả (N7 tr. 5–6), nên không được trình bày như thể McCormick được minh oan. |
| Kevin James McCormick | BOP: đã ra 03/04/2024; không có trong trang ân xá | K | JSON BOP: KEVIN JAMES MCCORMICK, 54 tuổi, số 14130-025, actRelDate 04/03/2024; trang ân xá: 0 kết quả cho "Kevin… McCormick" (2 kết quả "McCormick" khác người: Kimberly Black-McCormick, Richard McCormick) | — |
| Grant Clark Wasik | Vai trò: người bán → trưởng nhóm → quản lý bán hàng → phó chủ tịch | K | N1 tr. 5–6, ¶20–22 | — |
| Grant Clark Wasik | Nhận tội tội 1 (2019); §1349; 125 tháng; bồi hoàn 10.619.430,95 USD (08/10/2019) | K (có ghi chú) | N4: "pled guilty to count one of a 14-count superseding indictment earlier this year… 125 months"; bảng trong N6: "Oct. 8, 2019 Grant Wasik 125 months $10,619,430.95" | **Nguồn mâu thuẫn về ngày tuyên án.** N4 (ngày API 11/10/2019) viết "was sentenced yesterday", tức 10/10/2019, còn bảng trong N6 ghi 08/10/2019. Đề nghị ghi "October 2019" hoặc nêu cả hai nguồn. Ngoài ra N4 ghi "over $10.5 million", N5 ghi "over $10 million", N6 ghi con số chính xác: không mâu thuẫn. |
| Grant Clark Wasik | BOP: dự kiến ra 17/10/2027 | K | JSON BOP: GRANT WASIK, 44 tuổi, số 13842-025, Philadelphia, projRelDate 10/17/2027 | — |
| Michael Cary Lawing | ● CONVICTED; nhận tội felony information 10/2018; 18 tháng, bồi hoàn > 266.000 USD (15/10/2019) | K | N5: "pleaded guilty in October 2018 to a one-count felony information charging him with conspiracy to commit wire fraud… 18 months… over $266,000"; ngày 15/10/2019 chỉ có trong bảng của N6 ("Oct. 15, 2019 Michael Lawing 18 months $266,501.94") | Đề nghị thêm N6 vào cột nguồn vì ngày tuyên án lấy từ N6, không từ N5. |
| Michael Cary Lawing | Kháng cáo / ân xá: "Không kiểm" | TT | JSON BOP: MICHAEL CARY LAWING, 41 tuổi, số 14200-025, faclName "IN TRANSIT", projRelDate "UNKNOWN", không có ngày ra | Trang ân xá: 0 kết quả "Lawing". Bản ghi BOP hiện tại không cho thấy ông đã ra tù sau mức 18 tháng tuyên năm 2019. Nguyên nhân không rõ, và **không được suy đoán**. Đề xuất: hoặc kiểm thêm bằng nguồn chính thức, hoặc kịch bản không nói gì về trạng thái hiện tại của Lawing. |
| 15 nhân viên khác | ● CONVICTED (nhóm); nhận tội; từ quản chế đến 18 tháng tù | K | N6: "17 other employees… have also pleaded guilty" (17 = 15 + Lawing + Wasik); bảng án: cao nhất 18 tháng (Cortez); thấp nhất có 5 năm quản chế (Davidson, Miller), "time served" (McCart, Crowell), "1 day" (Bachman, Aievoli, Swinson) | Dải "từ quản chế đến 18 tháng" nên viết rõ thêm "time served / 1 ngày". Chú ý: N3 (08/2019) ghi Erica Crowell "remains under indictment", còn N6 (02/2020) ghi bà đã nhận tội và bị tuyên án ngày 08/01/2020. Bảng nói theo nhóm theo N6 là đúng. Phải dùng N6, không dùng N3, cho trạng thái của nhóm. |
| Client Care Experts / First Choice; ABC Repair Tech | Không bị truy tố hình sự với tư cách pháp nhân trong N1; bang Florida có vụ dân sự riêng (chưa mở) | K | N1 tr. 1: bị cáo chỉ gồm 3 cá nhân; N3/N6: "Florida Attorney General's Office… bringing its own civil enforcement action against CCE" | N1 ghi "Client Care Experts, Inc.", còn DOJ ghi "LLC". Dùng đúng tên theo từng nguồn. Không gắn nhãn tầng cho công ty. |
| Hai thương hiệu thật (phần mềm quét, chuỗi bán lẻ) | Không bị mạo danh; KHÔNG BỊ CÁO BUỘC | K | N1 tr. 3 ¶11–12 (Webroot System Analyzer), tr. 3–4 ¶13 ("Best Buy pitch") | Đúng luật 8e. Nếu nêu tên thì phải kèm câu nói rõ hai thương hiệu không liên quan. |
| Nạn nhân | > 40.000; ≥ 57 ở S.D. Ill.; trong cáo trạng chỉ ghi tên viết tắt | K | N1 tr. 5 ¶19 "over 40,000 people… At least fifty-seven"; tr. 8–20 (Count 2–14: D.M., S.S., J.H., M.M., J.R.…) | — |
| Các luật sư bào chữa trong N7 | KHÔNG BỊ CÁO BUỘC, không nêu tên | K | N7 tr. 2 và tr. 5–6 nêu tên luật sư cùng các chi tiết về rượu bia và DUI | Rất cần giữ không nêu tên (luật 5 và 8f). Chi tiết đời tư này không được dùng để giật gân. |

Kiểm thêm:
- (a) Nhân vật trung tâm ở tầng ●: **có**.
- (b) Người không bị cáo buộc bị nêu tên trái luật 5: **không**. Bảng đã chủ động không nêu tên luật sư.
- (d) §5: vụ này không có yếu tố tình dục, nên không áp dụng. Nạn nhân có người cao tuổi (N1 tr. 7 nêu SCAMS Act với nạn nhân trên 55 tuổi); không được chế giễu nạn nhân.

## SHA-256
| Tệp | Ghi trong §8 | Tính lại | Khớp? |
|---|---|---|---|
| `ho-so/techsupport-popup-seward/cao-trang-thay-the-3-17-cr-30192-doc31-2018-05-23.pdf` | `5cd908ae0fd545d2b654b67a7e1448572e028ac57d5d19b44cbd1f5169c4bf25` | `5cd908ae0fd545d2b654b67a7e1448572e028ac57d5d19b44cbd1f5169c4bf25` | **Khớp** (20 tr.) |
| `ho-so/techsupport-popup-seward/lenh-2255-mccormick-doc272-2022-01-27.pdf` | `1c56073f6441964ddced9edf1a21a23c7f80f84fd01dc17c84d16f52d78997a9` | `1c56073f6441964ddced9edf1a21a23c7f80f84fd01dc17c84d16f52d78997a9` | **Khớp**. Bản tải lại từ GovInfo ngày 01/11/2026 cho cùng giá trị băm. |

Thông cáo N2–N6: API DOJ mở lại HTTP 200. Tiêu đề, URL và ngày khớp §8: 25/05/2018, 14/08/2019, 11/10/2019, 16/10/2019, 11/02/2020.

## Không kiểm được
| URL | Lý do |
|---|---|
| Docket S.D. Ill. 3:17-cr-30192; plea agreement và judgment của Seward; mức án mới của McCormick; kháng cáo 7th Cir. (N10) | PACER có phí, bị cấm. GovInfo chỉ có Doc 272–273. |
| Lý do Seward ra tù 11/2023; trạng thái "IN TRANSIT / UNKNOWN" của Lawing | BOP không ghi lý do. Không suy đoán. |
| Vụ dân sự của bang Florida | Không có trong danh sách nguồn mở; chưa mở. |
| 24 PDF quét trong các trang ân xá | Không có lớp chữ. |
