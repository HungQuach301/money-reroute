# Kiểm tầng độc lập — bec-rimasauskas · MR-K1 · 01/11/2026

Phạm vi: chỉ §2 "Bảng tầng gọn" và §8 "Nguồn" của `docs/kho-de-tai/bec-rimasauskas.md`. Nguồn mở lại bằng đường chính thức ngày 01/11/2026.

## Kết luận
**ĐẠT CÓ SỬA.** Nhân vật trung tâm (Evaldas Rimasauskas) đúng tầng ● theo luật 8a: thông cáo DOJ 19-087 và 19-441 xác nhận nhận tội 1 tội wire fraud và mức án. Cần sửa 2 điểm: (1) "Company-2" không được gắn ● vì pháp nhân này không bị truy tố hay kết án; (2) bảng chưa ghi rằng cáo trạng gốc có 5 tội mà bị cáo chỉ nhận 1 tội, nên dễ bị nói thành kết án rửa tiền hoặc trộm danh tính.

## Bảng chấm
| Dòng bảng tầng | Ô | Điểm | Nguồn đã mở + trang/đoạn | Ghi chú / sửa đề xuất |
|---|---|---|---|---|
| Evaldas Rimasauskas | Vai trò "người dàn dựng (theo cáo trạng đã nhận tội)" | K | N4 (19-441): "According to the allegations in the Indictment to which RIMASAUSKAS pled guilty… orchestrated a fraudulent scheme" | — |
| Evaldas Rimasauskas | Tầng ● CONVICTED | K | N3 (19-087) "pled guilty today to wire fraud"; N4 "was sentenced today to 60 months" | Đúng luật 8a. |
| Evaldas Rimasauskas | Loại phán quyết: nhận tội, toà chấp nhận (20/3/2019) | K | N3, ngày API 20/03/2019 | N3 chỉ nói "entered his guilty plea… before U.S. District Judge George B. Daniels", không có chữ "accepted". Việc tuyên án ngày 19/12/2019 (N4) xác nhận plea đã được chấp nhận. Lời thoại nên viết "pleaded guilty in 2019", không viết "the court accepted". |
| Evaldas Rimasauskas | Tội danh: 1 tội wire fraud | K | N3: "pled guilty to one count of wire fraud"; N4: "previously pled guilty to one count of wire fraud" | — |
| Evaldas Rimasauskas | Các tội khác trong cáo trạng | TT | N1 (17-093): "charged with one count of wire fraud and three counts of money laundering… and one count of aggravated identity theft" | Bảng không ghi rằng 4 tội còn lại không được nhận. Các nguồn đã mở không nói số phận của 4 tội này (bác hay rút); ghi "chưa mở được" và **cấm** nói "convicted of money laundering / identity theft". Đề xuất thêm vào cột tội danh: "(cáo trạng có 5 tội; chỉ nhận 1 tội wire fraud)". |
| Evaldas Rimasauskas | Mức án: 60 tháng, 2 năm giám sát, tịch thu 49,74 triệu USD, bồi hoàn 26,48 triệu USD (19/12/2019) | K | N4: "60 months… two years of supervised release, to forfeit $49,738,559.41… restitution in the amount of $26,479,079.24"; ngày API 19/12/2019 | Số tiền chiếm đoạt không thống nhất giữa các nguồn: N1/N3 ghi "over $100 million", N4 ghi "over $120 million". Lời thoại phải gắn năm và nguồn cho từng con số. |
| Evaldas Rimasauskas | Kháng cáo | KKĐ | N7 CourtListener: HTTP 403 (đã thử 1 lần ngày 01/11/2026, không vượt rào) | §8 ghi đúng là "chưa xác minh bằng docket". |
| Evaldas Rimasauskas | Ân xá / giảm án | K | 5 trang Office of the Pardon Attorney đều HTTP 200: Trump 2025–nay (cập nhật 20/10/2026), Trump 2017–2021 pardons (cập nhật 23/10), Trump 2017–2021 commutations, Biden pardons (cập nhật 14/05/2026), Biden commutations (cập nhật 09/07/2025). Đã quét cả 179 PDF danh sách đính kèm. Tìm "Rimasauskas": 0 kết quả | §8/N6 ghi trang Trump 2017–2021 là "chưa mở được (URL đoán 404)". Hai URL sau mở được (200), đề nghị bổ sung: `justice.gov/pardon/pardons-granted-president-donald-j-trump-2017-2021` và `…/commutations-granted-president-donald-j-trump-2017-2021`. Ngoại lệ: 24 PDF ngắn (1–4 tr.) là bản quét không có lớp chữ nên không tìm chuỗi được. |
| Evaldas Rimasauskas | BOP: đã ra tù 18/6/2021 | K | JSON BOP locator: EVALDAS RIMASAUSKAS, 58 tuổi, số 91190-054, Lewisburg, releaseCode R, actRelDate 06/18/2021 | — |
| "Company-2" | Tầng "● (là phần của tội đã nhận)" | M | N1/N3/N4: Company-2 chỉ là công ty do bị cáo lập ra, không phải bị cáo | Một pháp nhân không bị truy tố hay kết án thì không được mang nhãn ●. Sửa thành: "Công cụ trong tội bị cáo đã nhận; không bị truy tố riêng; không nêu tên, không gắn nhãn". Giữ nguyên quy định không nêu tên. |
| "Company-1" (nhà sản xuất phần cứng châu Á) | KHÔNG BỊ CÁO BUỘC, bị mạo danh | K | N3/N4: "neither sent nor authorized by Company-1" | Đúng luật 8e. Các nguồn DOJ đã mở không nêu tên Company-1, nên kịch bản không được nêu tên. |
| Hai công ty internet Mỹ | Nạn nhân, KHÔNG BỊ CÁO BUỘC | K | N1, N3, N4: "a multinational technology company and a multinational online social media company" | DOJ không nêu tên, nên giữ nguyên không nêu tên (luật 5). |
| Ngân hàng ở Latvia/Cyprus | KHÔNG BỊ CÁO BUỘC, không nêu tên | K | N4: "accounts at banks located in Latvia and Cyprus" | — |

Kiểm thêm:
- (a) Nhân vật trung tâm ở tầng ●: **có**.
- (b) Người không bị cáo buộc bị nêu tên trái luật 5: **không**. Các nguồn có nêu tên công tố viên, thẩm phán và cơ quan, nhưng họ không thuộc diện luật 5 bảo vệ.
- (d) §5: vụ này không có yếu tố tình dục, nên không áp dụng.

## SHA-256
| Tệp | Ghi trong §8 | Tính lại | Khớp? |
|---|---|---|---|
| `ho-so/bec-rimasauskas/doj-api-thong-cao-sdny-2017-2019.json` | `3f6aba56e250225f5e5a09f71816f60c67f2b22d4797c2f4a7e6e24ad1b102a8` | `3f6aba56e250225f5e5a09f71816f60c67f2b22d4797c2f4a7e6e24ad1b102a8` | **Khớp** |

Đối chiếu với API DOJ hiện tại (`justice.gov/api/v1/press_releases.json?parameters[title]=Lithuanian Man`, HTTP 200, ngày 01/11/2026):
- API trả về 4 bản ghi 17-093, 17-263, 19-087, 19-441, khớp số, ngày và URL với N1–N4.
- So từng trường (attachment, body, changed, component, created, date, image, number, teaser, title, topic, url, uuid) giữa tệp lưu và API: **không có trường nào khác**, và không thiếu khoá nào.

## Không kiểm được
| URL | Lý do |
|---|---|
| https://www.courtlistener.com/docket/7383280/united-states-v-rimasauskas/ | HTTP 403. Không vượt rào. Vì vậy không kiểm được kháng cáo và số phận 4 tội còn lại. |
| PACER S.D.N.Y. 1:16-cr-00841 | Có phí, bị cấm. |
| 24 PDF quét trong các trang ân xá | Không có lớp chữ nên không tìm chuỗi được (các tệp này là lệnh/tuyên bố ngắn, không phải danh sách lớn). |
