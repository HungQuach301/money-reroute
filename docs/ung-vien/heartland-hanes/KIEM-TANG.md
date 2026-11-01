# Kiểm tầng pháp lý độc lập — `heartland-hanes`

- **Người kiểm:** tác tử độc lập MR-1 (không đọc `reports/**`, `RUI-RO.md`, phần tóm tắt `NGUON.md`; chỉ dùng CLAUDE.md, HIEN-CHUONG §3, `TANG.md`, bảng nguồn `NGUON.md`).
- **Ngày kiểm:** 01/11/2026.
- **Thang chấm:** **K** = khớp · **MH** = mạnh hơn nguồn · **S** = sai · **KKĐ** = không kiểm được · k/a = không áp dụng (không tính).

## Nguồn đã mở

| Mã | Tệp / URL | Trang đã đọc | Kiểm |
|---|---|---|---|
| N1 | `ho-so/heartland-hanes/information.pdf` | tr. 1–5 | SHA-256 `dd29eed7…1e83196` khớp NGUON |
| N2 | `plea-agreement.pdf` | tr. 1–13 | `3c91e808…c502e` khớp |
| N3 | `second-amended-judgment.pdf` | tr. 1–8 | `94490f50…e7999d` khớp |
| N4 | `govt-sentencing-memo.pdf` | tr. 1–6, 13 | `8ed6793f…06fabd` khớp |
| N5 | `restitution-memo.pdf` | tr. 1–6 | `52c51970…7bfd3aac` khớp |
| N6 | `frb-oig-material-loss-review.pdf` | tr. PDF 8, 12–13, 19 | `74fbd1ad…1248ba` khớp |
| N7 | `frb-prohibition-order.pdf` | tr. 1–5 | `56a62962…cc6b646` khớp |
| N9 | `frb-oig-sentencing-statement.pdf` | 1 tr. | `bd6f9bd6…324238` khớp |
| N17 | `defense-sentencing-memo.pdf` (Doc. 26), `bill-of-particulars.pdf` | Doc. 26 tr. 5–6 | `85d25d38…8f808`, `85f8c8a5…6f80` khớp |
| Doc. 15 | RECAP `gov.uscourts.ksd.151122.15.0.pdf` (Petition to Enter Plea and Order Entering Plea) | tr. 1, 7 | HTTP 200; SHA-256 `0309f427ae512d091bc22cae6ff98e5236cef5dac20b87bb768933134133d161` |
| Doc. 32 | RECAP `gov.uscourts.ksd.151122.32.0.pdf` (Amended Judgment) | tr. 1, 6 | HTTP 200; SHA-256 `48f8cb5a7392b4c8a0ad3c59b3975935081fd3a6218b86397e005deac037ebd4` |
| N8 | federalreserve.gov/newsevents/pressreleases/enforcement20241121a.htm | toàn văn | HTTP 200 |
| N10 | fdicoig.gov/…/former-ceo-failed-bank-sentenced-prison | toàn văn | HTTP 200 |
| N14 | justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present | toàn văn, tìm "Hanes", "Heartland" | HTTP 200, trang ghi "Updated October 20, 2026"; 0 kết quả |
| N15 | justice.gov/pardon/commutations-… và pardons-granted-president-joseph-biden-2021-2025 (+ các PDF lệnh ân giảm liên kết trên trang) | toàn văn | HTTP 200; 0 kết quả "Hanes". Một số PDF trả 502 từ proxy (không thử lại) |
| N16 | BOP Inmate Locator (POST `/PublicInfo/execute/inmateloc`, số 02016-511) | kết quả JSON | HANES, SHAN · FMC Fort Worth · projRelDate 06/11/2044 · không có actRelDate |
| N13 | courtlistener.com/docket/68221157/… | — | **chưa mở được**: HTTP 403 (CloudFront "Request blocked"), WebFetch cũng 403. RECAP Doc. 30, 66, 68: 404 |

## Bảng chấm từng ô

| # | Chủ thể | Ô | Bảng nói | Chấm | Bằng chứng (trang thực đọc, trích ≤ 25 từ) |
|---|---|---|---|---|---|
| 1 | Shan Hanes (hình sự) | Tầng | ● CONVICTED | **K** | N3 tr. 1: "pleaded guilty to count(s): 1 of a one-count Information… adjudicated guilty" |
| | | Loại phán quyết | Nhận tội theo plea, toà chấp nhận (Petition and Order Entering Plea 23/05/2024) | **K** | Doc. 15 tr. 7: "Therefore, I accept the defendant's guilty plea." Lọc ngày 05/23/24 |
| | | Tội danh + án | §656 và §2, Class B, kết thúc 07/07/2023; 293 tháng; 3 năm giám sát; 100 USD; miễn phạt; bồi hoàn 55.400.023,31 (FDIC 47.105.000); Tether + money judgment 47,1 triệu | **K** | N3 tr. 1 "Embezzlement by a Bank Officer, a Class B Felony 07/07/2023"; tr. 2 "293 months"; tr. 3 "3 years"; tr. 6 "$100 … *$55,400,023.31 … Waived"; tr. 7 "FDIC $47,105,000.00"; tr. 8 "Money judgment in the amount of $47.1 million". Khoản 8.071.037,80 USD: N5 tr. 4 |
| | | Kháng cáo | ¶13 miễn kháng cáo trừ án vượt khung; docket không có notice of appeal; chưa xác minh PACER; Doc. 66 chưa mở | **KKĐ** (phần ¶13 K) | N2 tr. 10–11: "waives the right to appeal the sentence imposed… except to the extent… the Court departs or varies upwards". Phần docket: CourtListener 403, không kiểm được |
| | | Ân xá | Không có tên (Trump 2025–nay, Biden) | **K** | N14 "Updated October 20, 2026", 0 kết quả; N15 0 kết quả |
| | | Đã chết? | Không; BOP FMC Fort Worth, thả 11/06/2044 | **K** | N16: faclName "Fort Worth", faclType "FMC", projRelDate "06/11/2044" |
| | | Nguồn | N1 tr. 2–3; N2 tr. 1–4, 10–11; N3 tr. 1–2, 6–7; N13… | **S** (nhỏ) | Tịch thu (Tether + money judgment) nằm ở N3 **tr. 8**, không thuộc tr. 1–2, 6–7. Các mục N13 không kiểm được |
| 2 | Shan Hanes (Fed Board) | Tầng | ◐ ALLEGED | **K** | N7 tr. 2: "without Hanes admitting or denying any allegation made or implied by the Board" |
| | | Loại phán quyết | Order of Prohibition Issued Upon Consent, §8(e) | **K** | N7 tr. 1, tiêu đề: "Order of Prohibition Issued Upon Consent Pursuant to Section 8(e)" |
| | | Nội dung | Cấm tham gia ngành ngân hàng khi chưa được phép; docket 24-032-E-I | **K** | N7 tr. 3: "without the prior written approval of the Board… prohibited from: participating in any manner…"; tr. 1 "Docket No. 24-032-E-I" |
| | | Kháng cáo | Đã từ bỏ xem xét tư pháp (N7 tr. 2) | **K** | N7 tr. 2: "(c) to obtain judicial review of this Order" (trong danh sách quyền đã từ bỏ) |
| | | Đã chết? | Không | **K** | như dòng 1 |
| | | Nguồn | N7 tr. 1–3; N8 | **K** | N8: "prohibited Shan Hanes from future participation in the banking industry" (21/11/2024). Ghi thêm: lệnh có hiệu lực "18th day… November, 2024" (N7 tr. 5) |
| 3 | Người/nhóm lừa đảo không xác định | Tầng | ◐ (không ai bị truy tố) | **K** | Không có bị cáo khác trên N1/N3; mô tả từ hồ sơ công tố và plea |
| | | Loại phán quyết | Chưa có | **K** | — |
| | | Nội dung | Kiểm soát tài khoản crypto; "true identity … remain unknown" (N4 tr. 3) | **K** | N4 tr. 3: "To date, the true identity of the co-conspirator, or conspirators, remain unknown."; N2 tr. 2 "controlled by unidentified third parties" |
| | | Nguồn | N2 tr. 2; N4 tr. 3; N10 | **K** | N10: "controlled by unidentified third parties" |
| 4 | Heartland Tri-State Bank | Tầng | ○ (nạn nhân) | **S** (nhãn) | Theo HIEN-CHUONG §3, ○ = TIN ĐỒN / UNVERIFIED. Thất bại ngân hàng là sự kiện có hồ sơ (N1 tr. 2, N7 tr. 2), không phải tin đồn. Dùng ○ sẽ ghi sai nhãn trên hình |
| | | Loại phán quyết | Chưa có (không phải bị đơn) | **K** | — |
| | | Nội dung | Thành viên bang; thất bại 28/07/2023; FDIC tiếp quản; ngân hàng khác ở Kansas mua cùng ngày; MLR kiểm soát yếu | **K** | N7 tr. 1 "A State Member Bank"; N1 tr. 2 "on or about July 28, 2023 the [FDIC] was appointed receiver"; N6 tr. 8 "Another bank in Kansas acquired Heartland on July 28, 2023"; N6 tr. 12 "senior bank employees circumvented the bank's wire policy and daily limits" |
| | | Nguồn | N1 tr. 2; N5 tr. 2; N6 tr. 8, 12–13 | **K** | N5 tr. 2 "sold to Dream First Bank" |
| 5 | Elkhart Financial Corporation | Tầng | ○ (nạn nhân) | **S** (nhãn) | Như dòng 4 |
| | | Nội dung | Cổ phần mất toàn bộ giá trị | **K** | N5 tr. 2: "all value of stock in HTSB was wiped out"; N2 tr. 4 "complete loss of equity by bank investors" |
| | | Nguồn | N4; N5 | **K** | N4 tr. 2–3 mô tả công ty mẹ |
| 6 | FDIC | Tầng | ○ (cơ quan) | **S** (nhãn) | Như dòng 4 |
| | | Nội dung | Bồi hoàn 47.105.000 USD (N3 tr. 7) | **K** | N3 tr. 7: "FDIC $47,105,000.00 $47,105,000.00 2"; N5 tr. 3 "$47,105,000" |
| | | Nguồn | N3; N5 tr. 3 | **K** | — |
| 7 | Vụ án bang Morton County | Tầng | ◐ ALLEGED | **K** | Doc. 26 tr. 5: "There is a current case pending in Morton County, Kansas District Court" |
| | | Loại phán quyết | Chưa có / chưa xác minh | **K** | — |
| | | Nội dung | "28 count Complaint", tới 86 tháng; "matter pending" | **K** | Doc. 26 tr. 6: "facing a 28 count Complaint… potential sentence in that case would be 86 months"; N4 tr. 13: "The matter pending in Morton County, Kansas". Lưu ý: 86 tháng là lời **luật sư bào chữa** |
| | | Kháng cáo | chưa xác minh | **K** | — |
| | | Nguồn | N4 tr. 13; N17 Doc. 26 tr. 5–6 | **K** | đúng trang |

### Câu "Cách nói EN gợi ý"

| # | Câu | Chấm | Bằng chứng |
|---|---|---|---|
| E1 | Hanes "pleaded guilty… May 2024… embezzlement by a bank officer… In August 2024, a federal judge in Wichita sentenced him to 293 months — about 24 years"; "admitted he lied to bank employees and board members"; nguồn "No. 6:24-cr-10013 (D. Kan. 2024)" | **K** | Doc. 15 lọc 05/23/24; Doc. 32 tr. 1 "Date of Original Judgment: 08/19/2024"; N9 "Wichita, KS"; N2 tr. 3–4 "lied to HTSB employees about the purpose of the transfers. The defendant lied to members of HTSB board of directors" |
| E2 | Trích N1 tr. 3 "embezzled … for the purchase of cryptocurrency intended for the personal benefit"; "His lawyer argued he had fallen victim to a 'pig butchering' scam" | **K** | N1 tr. 3 nguyên văn khớp; Doc. 26 tr. 5 "Mr. Hanes fell victim to a cryptocurrency scam called Pig Butchering" (lời bào chữa, đã gắn "His lawyer argued") |
| E3 | Fed "barred him… in an order he agreed to without admitting or denying" | **K** | N7 tr. 2 |
| E4 | Kẻ lừa đảo "Prosecutors said… unidentified third parties… no one else has been charged" (có rào "As of the latest filings we reviewed") | **K** | N2 tr. 2; N4 tr. 3. Không dùng "convicted"/"fraud" khẳng định cho chủ thể chưa ● |
| E5 | MLR "bank staff approved wires far above the bank's own daily limits" | **K** | N6 tr. 13: "exceeded the $5 million applicable limit by $1.7 million to $5.3 million per sender" |
| E6 | Vụ bang "He also faced state charges in Kansas" + "status not verified" | **K** | Doc. 26 tr. 5–6 |

Không câu EN nào dùng "convicted" hoặc "fraud" khẳng định cho chủ thể chưa ●.

## Tổng

| Khớp | Mạnh hơn | Sai | Không kiểm được |
|---|---|---|---|
| **33** | **0** | **4** (3 nhãn ○ + 1 trang nguồn) | **1** |

## Sửa bắt buộc

1. **Nhãn ○ cho Heartland Bank, Elkhart Financial, FDIC** (dòng 4–6): ○ là nhãn TIN ĐỒN theo §3. Thay bằng ghi chú "không bị cáo buộc — nạn nhân/cơ quan; sự kiện có hồ sơ" và **không** gắn ○ UNVERIFIED trên hình. Nếu cần nhãn hình riêng cho nhóm này, điều phối bổ sung quy ước (HIEN-CHUONG chưa có).
2. **Nguồn dòng 1:** thêm **N3 tr. 8** cho phần tịch thu (địa chỉ Tether + "Money judgment in the amount of $47.1 million").
3. **Doc. 66 "Amended Judgment" 30/07/2025 (và Doc. 67, 68):** chưa ai mở được; có thể đổi án hoặc bồi hoàn. Trước khi chốt lời phải mở (PACER) hoặc ghi rõ số liệu là "theo 2nd Amended Judgment ngày 05/11/2024".
4. **Kháng cáo:** giữ "không thấy kháng cáo" chỉ khi docket được mở lại; lần kiểm này CourtListener trả 403.
5. Nếu nhắc vụ bang: con số 28 tội/86 tháng phải gắn "his lawyers wrote" (Doc. 26 là lời bào chữa).
