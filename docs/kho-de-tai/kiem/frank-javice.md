# Kiểm tầng độc lập — frank-javice · MR-K1 · 01/11/2026

Phạm vi: chỉ đọc §2 "Bảng tầng gọn" và §8 "Nguồn" của `docs/kho-de-tai/frank-javice.md`; mở lại nguồn ngày 01/11/2026.

## Kết luận
**ĐẠT CÓ SỬA.** Mọi ô kiểm được đều khớp nguồn đúng trang; không có ô nói mạnh hơn nguồn, không có số/ngày sai. Chỉ cần bổ sung trạng thái giam giữ hiện tại theo BOP (Javice không ở trạng thái đang bị BOP giam; Amar đang thụ án) và giữ nguyên các ghi chú "chưa mở được" (số vụ hình sự, kháng cáo 25-2895, mức án Amar).

Kiểm thêm: (a) nhân vật trung tâm Charlie Javice ● CONVICTED (bản án sau xét xử, N1, N4) — đạt luật 8a. (b) Không có cá nhân không bị cáo buộc nào bị nêu tên trong bảng (giám đốc kỹ thuật, "Data Science Professor", bên kiểm định, bên bán dữ liệu đều không tên) — đạt luật 5. (c) SHA-256 khớp. (d) Không có yếu tố tình dục — §5 không áp dụng.

## Bảng chấm
| Dòng bảng tầng | Ô | Điểm | Nguồn đã mở + trang | Ghi chú / sửa đề xuất |
|---|---|---|---|---|
| Charlie Javice (hình sự) | Tầng ● | K | N1 (DOJ API, toàn văn): "convicted of conspiracy, wire fraud, bank fraud, and securities fraud following a six-week jury trial in March 2025" | — |
| Charlie Javice (hình sự) | Loại phán quyết: sau xét xử, bồi thẩm nhất trí | K | N4: "a unanimous jury found Charlie Javice and Olivier Amar guilty" | — |
| Charlie Javice (hình sự) | Tội danh + mức án | K | N1: 85 tháng; 3 năm giám sát; forfeiture $22,360,977.48; restitution $287,501,078.00 "joint and several with AMAR" | — |
| Charlie Javice (hình sự) | Số vụ 1:23-cr-00251-AKH | KKĐ | N1, N4 không ghi số vụ | Bảng đã ghi đúng là "theo báo chí/kết quả tìm kiếm"; không đưa số vụ vào lời thoại cho đến khi mở được hồ sơ sơ cấp. |
| Charlie Javice (hình sự) | Kháng cáo 2d Cir. 25-2895 | KKĐ | Justia/CourtListener 403 (bảng đã ghi); PACER cấm | Giữ "chưa mở được". Không nói "đang kháng cáo" như sự thật đã kiểm. |
| Charlie Javice (hình sự) | Ân xá | K | N5 (cập nhật "October 20, 2026"): 0 kết quả "Javice"; kiểm thêm trang Biden pardons (cập nhật 14/05/2026) và Biden commutations: 0 kết quả | — |
| Charlie Javice (hình sự) | Trạng thái hiện tại | TT (bổ sung) | BOP inmate locator (JSON chính thức, 01/11/2026): CHARLIE JAVICE, Reg. 10518-506, MDC Brooklyn, "released" 04/04/2023, không có ngày dự kiến ra tù | Bảng chưa ghi trạng thái BOP. Theo BOP, bà **không ở trạng thái đang bị BOP giam** tại ngày kiểm; lý do (tại ngoại chờ kháng cáo, chưa trình diện…) **chưa mở được** — không suy ra. Kịch bản không được nói "đang ngồi tù". Đối chiếu bằng tên, cần kiểm lại ngày chốt lời. |
| Charlie Javice (dân sự SEC) | Tầng ◐, chưa có phán quyết | K | N3 (PDF) tr. 1 (relief defendants: hai quỹ tín thác 2021), tr. 3 ¶7 (§17(a), §10(b), Rule 10b-5), tr. 19–21 (ba yêu cầu: §17(a); §10(b)/10b-5; unjust enrichment với relief defendants); N2 (sec.gov, 200) | Có thể ghi thêm yêu cầu thứ ba (unjust enrichment, chỉ với hai quỹ tín thác). Kết cục vụ dân sự: KKĐ (trang tìm Litigation Releases của sec.gov không lọc theo từ khoá). |
| Olivier Amar | Tầng ●, sau xét xử cùng phiên, cùng 4 nhóm tội | K | N1, N4 | — |
| Olivier Amar | Mức án | KKĐ | DOJ API tìm tiêu đề "Olivier Amar"/"Amar": không có thông cáo tuyên án | Giữ "chưa mở được". BOP (01/11/2026): OLIVIER AMAR, Reg. 68105-510, FCI Fort Dix, dự kiến ra tù 01/12/2031 — chứng tỏ đang thụ án, **không** dùng để suy ra số tháng. |
| Olivier Amar | Ân xá | K | N5 + trang Biden: 0 kết quả tên "Olivier Amar" (trang Biden commutations có 1 lần chuỗi "Amar" trong tên "Rosamaria" — không phải ông) | — |
| JPMC | KHÔNG BỊ CÁO BUỘC, bên bị lừa | K | N1 ("fraudulently induce J.P. Morgan Chase"); N3 tr. 2 ¶1 | — |
| Ngân hàng lớn thứ hai | KHÔNG BỊ CÁO BUỘC, không tên | K | N1 ("Two major banks, one of which was JPMC") | — |
| Giám đốc kỹ thuật; nhà khoa học dữ liệu; bên kiểm định; bên bán dữ liệu | KHÔNG BỊ CÁO BUỘC, không tên | K | N1; N3 tr. 2–3 ¶3–4, tr. 12–13 ¶52–58 | Lưu ý N3 gọi người tạo dữ liệu là "Data Science Professor" ở "a local university" — không tên; giữ không nêu. N3 cũng nhắc "Frank Executive" (tr. 3 ¶4) — trong vụ SEC không bị nêu là bị đơn; trong vụ hình sự Amar là đồng bị cáo ●. Không ghép hai tên khi chưa có hồ sơ nói rõ. |
| Sinh viên có dữ liệu bị mua bán | KHÔNG BỊ CÁO BUỘC | K | N1 (mua dữ liệu 4,5 triệu sinh viên, $105.000); N3 tr. 3 ¶4 ($105.000; $75.000) | — |

## SHA-256
| Tệp | Ghi trong §8 | Tính lại | Khớp? |
|---|---|---|---|
| `ho-so/frank-javice/sec-complaint-2023-04-04-23-cv-2795.pdf` (23 tr., pdfinfo) | 337ede5ea3de4ff04651e987be5b281c69a500a828108dee1e2349c1e9237ca8 | 337ede5ea3de4ff04651e987be5b281c69a500a828108dee1e2349c1e9237ca8 | Có |

## Không kiểm được
| URL | Lý do |
|---|---|
| https://dockets.justia.com/docket/circuit-courts/ca2/25-2895 | Không mở lại: §8 ghi 403; luật không vượt rào. Docket chính thức của 2d Cir. chỉ qua PACER (cấm). |
| https://www.courtlistener.com/?q=Javice&type=r&court=nysd | Không mở lại: §8 ghi 403. |
| Thông cáo tuyên án Olivier Amar | DOJ API không trả kết quả theo tiêu đề. |
| Kết cục SEC v. Javice (1:23-cv-02795) | Trang tìm Litigation Releases sec.gov không lọc theo từ khoá; không có litigation release nào được mở. |
