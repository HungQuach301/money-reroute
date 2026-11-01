# KIỂM LỜI ĐỘC LẬP — VÒNG 2 · Tập 2 (`tap02-irs-callcenter-patel`)

- **Thời điểm:** 01/11/2026, 23:28–23:45 UTC.
- **Phạm vi:** chấm lại 7 câu đã sửa sau vòng 1 (S007, S037, S043, S046, S049, S059, S063) bằng nguồn tự mở; sau đó lướt toàn bộ 71 câu của `loi.json` và dòng HGLOBAL trong `SHOT.md`.
- **Đã đọc:** `docs/HIEN-CHUONG.md` (§1, §3 luật 1–8, §4, §5), `docs/tap02-irs-callcenter-patel/NGUON.md`, `loi.json`, `SHOT.md`. **Không đọc** `docs/dan-truyen/*`, `docs/kho-de-tai/*`, `reports/*`, `kiem/*` khác (chấm độc lập).
- **Không** sửa `loi.json`, không commit, không gọi API trả tiền. Mọi request dùng curl mặc định, không có thông tin cá nhân, không đổi user-agent. Tệp tải về để ở thư mục tạm riêng (`mktemp -d`), đọc bằng `python3 -I`.

## 1. Nguồn đã mở thực sự

| Mã | Đường mở | HTTP | Ghi chú |
|---|---|---|---|
| N1 | Tệp repo `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` | — (tệp cục bộ) | SHA-256 `04fb7cb3c4cfda5b444a66c9415878635346dfb1f6c3333e5acf41867a7b2bdf` — khớp NGUON. Render `pdftoppm -r 80 -gray` và xem ảnh các trang 1, 3, 4, 6, 7 ("Page x of 81"). |
| N2 | `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=Dozens of Individuals Indicted in Multimillion-Dollar Indian Call Center Scam Targeting U.S. Victims` → bản `/archives/opa/pr/dozens-individuals-indicted-multimillion-dollar-indian-call-center-scam-targeting-us-victims` | 200 | API trả 2 bản (usao-sdtx và OPA); chỉ dùng bản OPA. Số 16-1257, ngày 27/10/2016. 18 thẻ `<p>` không rỗng. |
| N3 | API, tiêu đề "24 Defendants Sentenced in Multimillion Dollar India-Based Call Center Scam Targeting U.S. Victims" → `/archives/opa/pr/24-defendants-sentenced-…` | 200 | Số 18-961, ngày 20/07/2018. Có 19 `<p>`, trong đó 18 `<li>` nằm sau đ.12 và 3 `<li>` sau đ.13. |
| N4 | API, tiêu đề đầy đủ "Indian National Pleads Guilty to Owning, Funding, and Operating India-Based Call Centers That Scammed U.S. Victims Out of Millions of Dollars" → **200 nhưng `results: []`**; gọi lại với "Indian National Pleads Guilty to Owning" → 1 kết quả `/archives/opa/pr/indian-national-pleads-guilty-owning-funding-and-operating-india-based-call-centers-scammed` | 200 | Số 20-19, ngày 09/01/2020. 16 `<p>` (khớp NGUON). **Ghi chú tái lập:** tra tiêu đề đầy đủ không ra kết quả; NGUON nên ghi chuỗi tra ngắn. |
| N5 | API, tiêu đề "Owner and Operator of India-Based Call Centers Sentenced to Prison for Scamming U.S. Victims out of Millions of Dollars" → `/archives/opa/pr/owner-and-operator-…-out-millions` | 200 | Số 20-1294, ngày 30/11/2020. 17 `<p>` (khớp NGUON). |
| N9 | `https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door` (curl mặc định) | 200 | Đọc mục "The IRS initiates most contacts…" và "Note that the IRS does not:". |

N6, N7, N8, N10, N11: không mở lại ở vòng này (không câu nào trong 7 câu chấm, và lượt lướt không thấy câu đáng ngờ, dựa vào các nguồn này).

## 2. Bảng chấm 7 câu đã sửa

| id | Kết quả | Tầng đúng? | Làm theo được ngay? | Trích nguyên văn nguồn + mã/trang | Đề xuất sửa |
|---|---|---|---|---|---|
| S007 | **KHỚP** | Có. CHUNG ở dạng câu hỏi; tiền đề ngầm ("call from India", tiền tới tay người ở Mỹ "almost immediately") khớp phần Patel thừa nhận ở S035. | Không | N4 đ.5: "Upon payment, the call centers would immediately turn to a network of “runners” based in the United States to liquidate and launder the fraudulently obtained funds." N3 đ.14: "…to liquidate and launder the extorted funds as quickly as possible…" | Không bắt buộc. "almost immediately" đã mềm hơn nguồn. |
| S037 | **KHỚP** | Có (◐, hai lần "according to the indictment" / "the indictment described") | Không. Câu chỉ nêu khái niệm, đã bỏ vế "or leaving a record of the transaction". | N2 đ.10: "The co-conspirators allegedly used “hawalas,” in which money is transferred internationally outside of the formal banking system, to direct the extorted funds to accounts belonging to U.S.-based individuals." N1 tr. 6 ¶2(g): "A hawala is an underground banking system based on trust through which money can be made available internationally without actually moving it or leaving a record of the transaction." | Không |
| S043 | **KHỚP** | Có (●N, theo nhóm, không nêu tên) | Không | N3 đ.1: "Twenty-one members … were sentenced this week to terms of imprisonment up to 20 years. Three other conspirators were sentenced earlier this year…" Danh sách `<li>` sau đ.12: "Nilesh Pandya … three years probation"; sau đ.13: Raman Patel "received a probationary sentence"; Dipakkumar Patel "Northern District of Georgia, Atlanta Division"; Raman Patel "District of Arizona, Phoenix Division". N3 đ.8: "240 months". N4 đ.11: "A total of 24 domestic defendants … have previously been convicted and sentenced … up to 20 years in the Southern District of Texas, District of Arizona and Northern District of Georgia." Ngày N3 (API `date`): 20/07/2018. | Không |
| S046 | **KHỚP** | Có (◐, chủ thể "the Justice Department said", mốc "As of July 2018") | Không | N3 đ.15: "The indictment in this case also charged 32 India-based conspirators and five India-based call centers … These defendants have yet to be arraigned in this case. An indictment is merely an allegation and the defendants are presumed innocent until proven guilty…" N2 đ.1: "32 individuals and five call centers in India were charged". | Tuỳ chọn: "and they were presumed innocent" → "and, it said, they were presumed innocent until proven guilty" (bám sát nguồn hơn, tránh hiểu thì quá khứ là "nay không còn"). Không bắt buộc. |
| S049 | **KHỚP** | Có (TT, có chủ thể DOJ) | Không | N4 đ.9: "Singapore authorities apprehended Patel at the request of the United States pursuant to a provisional arrest warrant in September 2018, after Patel flew there from India." (N5 đ.11 cùng câu) | Không |
| S059 | **KHỚP** | Có (●T: vế sự việc vụ có chủ thể "according to the Justice Department"; vế khung rửa tiền tự đánh dấu "In our terms") | Không. Nêu loại phương thức thanh toán ở mức dấu hiệu, không thao tác. | N4 đ.5 (phần "According to admissions that he made as part of his plea"): "Upon payment, the call centers would immediately turn to a network of “runners” based in the United States to liquidate and launder the fraudulently obtained funds." N9: "Note that the IRS does not: Call to demand immediate payment using a specific payment method such as a prepaid debit card, gift card or wire transfer." (Thẻ quà tặng trong vụ: N3 đ.14 "…Apple iTunes or other gift cards that victims purchased" — không nêu thương hiệu trong lời, đúng.) | Tuỳ chọn cho đồng bộ với S035: "…according to the Justice Department, Patel admitted that once a victim paid…". Không bắt buộc. |
| S063 | **KHỚP** | Có (◐ "the indictment described"; vế IRS là CHUNG có chủ thể IRS) | Không | N1 tr. 3 ¶1(a): "…would be arrested and fined if they did not pay their alleged back taxes immediately."; ¶1(b): "…they would be deported unless they paid a fine immediately for alleged issues with their USCIS paperwork." N9: "Demand that you pay taxes without the opportunity to question or appeal the amount they say you owe." | Không |

**Tổng 7 câu:** 7 KHỚP · 0 MẠNH HƠN · 0 SAI · 0 KHÔNG CẦN NGUỒN.

## 3. Kết quả lượt lướt 71 câu

Các câu tự đối chiếu thêm với nguồn đã mở ở mục 1 (không đưa vào bảng chấm vì đều khớp): S002, S004, S006, S009, S010, S012–S015, S017–S020, S025, S027–S036, S038–S040, S044, S045, S047, S048, S050–S056, S058, S060–S062, S064–S066, S069. Không câu nào sai số, sai ngày hay sai tầng.

**(a) Câu nói mạnh hơn tầng.** Không phát hiện.
- Mọi câu ◐ đều có chủ thể "according to the indictment / the indictment alleged/described / the Justice Department said". S015 nói thêm "Those figures were allegations at that stage".
- Mọi câu ●T (S002, S004, S028, S034, S035, S047, S053, S059, S062, S064) đều có "according to the Justice Department". S002, S059, S062, S064 không có chữ "admitted" nhưng vẫn qua chủ thể DOJ, đúng quy ước ●T trong `loi.json`.
- S020 và S031 lấy từ đoạn "In his plea, Patel admitted…" (N4 đ.6–7) nhưng được hạ xuống ◐. Như vậy là thận trọng hơn nguồn, chấp nhận được.
- Các câu TT không có chủ thể (S012–S014, S048, S050) đều là sự việc thủ tục, khớp N2 đ.1 và đ.8, N4 đ.9.

**(b) HGLOBAL.**
- `loi.json`: HGLOBAL được nêu 2 lần, trong lời S028 và trong lời + chữ S029. S028 đi liền ngay trước S029, và S029 là đúng nguyên câu ◐ (bản lời viết số bằng chữ, bản chữ viết chữ số), khớp từng chữ với `kiem_rieng.can_loi` / `can_chu`.
- Nguồn đã mở: N1 tr. 1 "[1] HGLOBAL" (bị cáo), N3 đ.15, N5 đ.12.
- Không câu nào suy trạng thái của HGLOBAL sau 7/2018. S029 và S056 chỉ nói về "other India-based defendants" ở mốc 11/2020. S030 ("that call center") không nêu tên lại.
- `SHOT.md`: có đúng 1 dòng chứa HGLOBAL (dòng 30, cảnh 11). Dòng này kèm nguyên câu ◐ "…presumed innocent. As of July 2018 … as of November 2020 …", hiện cùng khung, bật và tắt cùng lúc. **Đạt.**
- Ghi chú (không phải lỗi): trong cảnh 11, nhãn của S028 là "● CONVICTED · admitted in plea, per DOJ" và hiện cạnh ô chữ "HGLOBAL — …". Đề xuất ghi rõ chủ thể trên nhãn, ví dụ "● CONVICTED — Hitesh Patel · admitted in plea, per DOJ", để người xem không đọc nhầm nhãn ● là của HGLOBAL.

**(c) Chi tiết "làm theo được ngay" (HIEN-CHUONG §1).** Không phát hiện.
- Lời không có các thao tác trong N1 tr. 4 ¶2(a): chuyển số thẻ GPR cho người đăng ký, mua lệnh phiếu, nhận tiền bằng giấy tờ giả.
- Lời không có chi tiết "used his Indian cell phone number to access GPR cards through automated telephone systems" (N4 đ.7) hay số lượng 276 thẻ (N2 đ.12).
- Phần hawala (S037–S039) chỉ ở mức khái niệm. Không có số điện thoại, URL kẻ gian hay kịch bản lời dụ.

**(d) Thương hiệu, ứng dụng, thành phố nạn nhân, bị cáo chưa xử, nhãn xúc phạm.**
- Quét regex `cam_them` và `scammer|con artist|fraudster|con man`: **0 kết quả** trong lời và chữ. Riêng chữ "boss" chỉ xuất hiện ở chữ trên hình của S032, có kèm "a co-defendant", hợp lệ.
- Không có San Diego, Hayward, Frisco; không có WhatsApp, iTunes, Western Union, MoneyGram; không có tên 4 cụm call center còn lại; không có tên người chưa xử.
- Cơ quan bị mạo danh (IRS, USCIS, cơ quan thuế Canada và Úc) đều có câu "had nothing to do" hoặc "None of these agencies" trong cùng đoạn: P00 có S003, P01 có S011, P03 có S021, P11 có S067.
- Ghi chú (không phải lỗi): ở P01 và P11, câu miễn liên quan (S011, S067) có `doc: false`, tức chỉ hiện trên hình. Trong khi đó lời P01 (S010) có đọc "posing as IRS agents". Luật 8e chỉ đòi "kèm câu nói rõ" nên chữ trên hình vẫn đạt. Nếu muốn chắc hơn, có thể cho đọc S011 thành lời.

## 4. Tổng

- **7/7 câu chấm KHỚP.** Không câu nào MẠNH HƠN hay SAI.
- Lượt lướt 71 câu: **không vi phạm** ở (a), (b), (c), (d).
- Có 4 đề xuất tuỳ chọn, không chặn:
  1. S046: thêm "until proven guilty".
  2. S059: thêm "Patel admitted" cho đồng bộ với S035.
  3. SHOT cảnh 11: ghi tên Patel trên nhãn ●.
  4. Ghi chú tái lập ở NGUON N4: tra API bằng tiêu đề đầy đủ trả `results: []`; tra với "Indian National Pleads Guilty to Owning" thì ra.
