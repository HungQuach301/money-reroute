# BÁO CÁO MR-2 — M-b bước 1: Dàn truyện hai vụ (Woodbridge, 1inMM)

> Phiên Claude Code, 01/11/2026. Nhánh `ccr-287dabd9-ibz780` từ `main` @ `489f18a`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD** — không gọi API trả tiền, không sinh giọng/hình, không 402. Chỉ đọc hồ sơ công khai (PDF trong repo qua `git lfs pull`, sec.gov, API thông cáo chính thức của DOJ). Không merge, không xoá nhánh, không force-push.
> Phân công: phiên soạn hai dàn truyện; **5 lượt tác tử kiểm độc lập** (vòng 1 và vòng 2 mỗi vụ một tác tử mới; vòng 3 một tác tử cho các dòng sửa sau vòng 2). Tác tử kiểm không đọc `reports/**`, `TANG/RUI-RO/KIEM-TANG.md` hay kết quả vòng trước; chỉ đọc HIEN-CHUONG, tệp dàn truyện, bảng mã nguồn NGUON và PDF/HTML gốc.

## 1. Sản phẩm
| Tệp | Nội dung |
|---|---|
| `docs/dan-truyen/woodbridge-shapiro.md` | Logline VI/EN, móc câu 30 s (H1–H6, mỗi câu một tầng), bảng 27 nhịp (sự việc, nguồn + trang, tầng, hình, rà luật 8), khuôn tập, bài học, rà luật 8, ước chi, việc trước khi chốt lời |
| `docs/dan-truyen/1inmm-horwitz.md` | như trên, bảng 21 nhịp |
| `docs/dan-truyen/kiem/*-vong1.md`, `*-vong2.md`, `vong3-dong-sua.md` | Kết quả kiểm độc lập |

Quy ước tầng dùng trong dàn truyện: ● kết án · **●T** sự việc bị cáo **thừa nhận** trong factual proffer / factual basis (nói thẳng, kèm "In his plea, … admitted") · ◐ cáo buộc, dàn xếp, consent, lời công tố · TT thủ tục · NB nhận dạng · MH cảnh minh hoạ ILLUSTRATIVE · KBCB = KHÔNG BỊ CÁO BUỘC (không nêu tên, không nhãn trên hình).

## 2. Tóm tắt từng vụ (theo yêu cầu 1–6 của lệnh)
| | **A. Woodbridge — Robert H. Shapiro** | **B. 1inMM — Zachary Horwitz** |
|---|---|---|
| Logline (EN nháp) | *For five years, the interest checks arrived every month. The man behind them would later admit in federal court where the money really came from.* | *He sold investors a front-row seat to the streaming boom. In his plea agreement, he admitted the deals behind it were fake. HBO and Netflix were not accused of any wrongdoing.* |
| Trụ móc câu | ~10.000 nhà đầu tư, ~1,29 tỷ USD, "safe"; ít nhất 5 bang ra lệnh dừng mà vẫn bán; 25 năm tù (●T/●: N9, N10) | Diễn viên "Zach Avery"; lợi nhuận 25–45 %/kỳ 6–12 tháng; hợp đồng phân phối giả; ≥ 650 triệu USD; 20 năm tù (●T/●: N7, N8, N12) |
| Bước ngoặt có hồ sơ | (1) người vay là công ty của chính Shapiro (N9 tr. 5–6); (2) 5 lệnh cease-and-desist bị phớt lờ (N9 tr. 7); (3) quyết định phá sản nhưng vẫn thu tiền (N9 tr. 7) | (1) tài sản bảo đảm rỗng + hợp đồng giả (N7 tr. 10–11); (2) vỡ nợ toàn bộ từ ~12/2019 (N7 tr. 12); (3) SEC phong toả, FBI bắt 06/04/2021 (N2, N3, N10) |
| Khuôn | **1 tập ~20 phút.** Đã xét 2 phần: Phần 2 thiếu bài học riêng có nguồn (tỷ lệ thu hồi Liquidation Trust chưa xác minh) → không đạt 0b | **1 tập ~16 phút.** Phần 2 giả định không có bài học khác nhịp "ru ngủ" → không đạt 0b |
| Cú treo giữa tập | "And when the end came, the money kept coming in." (●T, N9 tr. 7) | Ba câu, tách lời DOJ ("more than five years", N12) với điều thừa nhận (N7 tr. 12) |
| Bài học hiểu biết | L1 Ponzi ở mức khái niệm; L2 "thế chấp hạng nhất" vô nghĩa khi người vay là bên liên quan; L3 lệnh của bang là tín hiệu công khai + phân biệt vụ dân sự dàn xếp / hình sự kết án | L1 đổi lợi nhuận kỳ ngắn ra lãi năm (35 %/6 tháng ≈ 82 %/năm nếu tái đầu tư); L2 Ponzi sống nhờ "thành tích" + ru ngủ; L3 tiền qua nhiều tầng — biết mình ký với ai |
| Dấu hiệu nhận diện | 5, mỗi cái gắn nhịp | 5, mỗi cái gắn nhịp |
| Phép thử "làm theo được ngay?" | Không — không cấu trúc trust/LLC, không kỹ thuật trốn thuế, không Form D/Rule 506 | Không — không cách làm giả tài liệu, không cấu trúc kỳ phiếu sao chép được, không chia tầng né đăng ký |
| Ước chi sơ bộ (đơn giá QUY-TRINH §6, **chưa đo trên MR**) | **≈ 9,9 – 21,4 USD** + ≈ 10.400 – 16.900 ký tự ElevenLabs | **≈ 7,9 – 17,0 USD** + ≈ 8.800 – 13.600 ký tự ElevenLabs |

Cả hai mức thấp đều **> 5,45 USD** (số dư OpenRouter chủ dự án báo) → phải nạp trước M-c. Khoản ảnh Gemini chỉ tính được khi có khoá (môi trường chưa có).

## 3. Rà luật 8 và luật 5 (tóm tắt — chi tiết §5 mỗi tệp)
- **(a)** Nhân vật trung tâm đều ●: Shapiro (N10), Horwitz (N8, N11, N12).
- **(b)** ◐ chỉ dùng cho: Woodbridge công ty và vụ SEC (đã khép bằng consent); 1inMM Capital (vụ SEC chưa có phán quyết đã mở → chỉ nói qua lời Horwitz thừa nhận hoặc "the SEC alleged"); các chi tiết từ đơn kiện SEC, lời công tố.
- **(c)** Không nêu tên: đại lý bán hàng Woodbridge (kể cả người bị SEC kiện riêng), nhóm nhà đầu tư trung gian của 1inMM, ngân hàng, công ty kế toán, các bên trong vụ kiện tư.
- **(d)** Không "fraudster / con man / scammer"; chỉ tên tội danh. Chữ "Ponzi" với Horwitz chỉ qua chủ thể DOJ (N7 không có chữ này).
- **(e)** HBO, Netflix: mọi chỗ nêu tên kèm câu viết sẵn "HBO and Netflix were not accused of any wrongdoing; according to the SEC, neither company ever did business with 1inMM." Không logo, không giao diện, không tài liệu dựng lại.
- **(f)** Không suy đoán động cơ, không bình luận đời tư; chi tiêu chỉ theo hồ sơ.
- **KHÔNG BỊ CÁO BUỘC:** người nhà Shapiro, relief defendant công ty, nạn nhân, nhân viên HBO/Netflix bị dùng danh tính, phim/hãng/đại lý trên giấy tờ giả, chủ hiện tại hai bất động sản — không nêu tên, không nhãn trên hình.
- Lời người thật: chỉ trích hồ sơ, hiện bằng chữ, đã đối chiếu ảnh trang (N2 tr. 22, 25; N9 tr. 4, 6, 7; N15 tr. 6; N1 ¶46, ¶76–77; N12).

## 4. Kiểm độc lập (yêu cầu 7)
| Vụ | Vòng 1 (bản nháp) | Vòng 2 (sau sửa vòng 1, toàn tệp) | Vòng 3 (các dòng sửa sau vòng 2) |
|---|---|---|---|
| Woodbridge | 33 dòng: **27 K · 4 MH · 1 S · 1 KKĐ** | 45 dòng: **42 K · 1 MH · 0 S · 2 KKĐ** | 14 dòng: 11 K · 1 MH · 0 S · 2 KKĐ |
| 1inMM | 26 dòng: **21 K · 5 MH · 0 S · 0 KKĐ**; ngoài bảng: logline VI MH, logline EN **S**, §5(d) dẫn nguồn S | 40 dòng: **35 K · 5 MH · 0 S · 0 KKĐ** | 18 dòng: 14 K · 2 MH · 2 S · 0 KKĐ |

Lỗi chính đã sửa:
- **Woodbridge:** trang ngày phá sản (N2 tr. 2 ¶3, không phải tr. 3); "evading payment of federal income taxes" (đúng tên tội); bỏ "tháng 4/2019 bị bắt" → "by April 2019 … had been arrested and charged" (N13); Boca Raton hạ về ◐; dấu hiệu "đại lý không đăng ký" gắn "the SEC alleged"; logline tách mốc bán (đến 12/2017) và mốc án (2019); "tiền hưu" trong logline gắn SEC (◐).
- **1inMM:** logline EN sai ("the one thing that wasn't real" — hợp đồng với đại lý cũng giả) → viết lại; "dùng danh tính nhân viên thật" chuyển sang lời công tố, ghi rõ tội trộm danh tính đã bị bác; số "hơn 250 nhà đầu tư con" ghi kèm bảo lưu quyền tranh cãi của bị cáo (N7 tr. 13–14); "bạn bè" là lời DOJ; "sole manager" hạ về ◐; cú treo tách hai nguồn; nhịp 6 giữ phạm vi "các phim đó"; "travel by private jet"; L1 sửa ví dụ (35 %/6 tháng theo bảng SEC, ≈ 82 %/năm) và bỏ câu tuyệt đối; L3 bỏ suy luận pháp lý chung (gần khuyên pháp lý); 8e viết sẵn câu không liên quan cho nhịp 2b, 4, 9, 9b.
- Không vòng nào thấy câu thành hướng dẫn làm, gán nhãn, hay ám chỉ công ty/đại lý/người nhà/HBO/Netflix có lỗi.

### 4b. Vòng 3
Tác tử mới chấm 32 dòng đã sửa sau vòng 2 (`kiem/vong3-dong-sua.md`): **25 K · 3 MH (nhẹ) · 2 S · 2 KKĐ (một vế)**. Không nâng tầng nặng, không thành hướng dẫn làm, 8e đạt.
- Đã sửa cả 5 mục bắt buộc: 1inMM nhịp 12 dẫn N4 tr. 3 §III (tiền) / §IV (consent) (S); §5(e) — logline EN và H5 thêm đủ vế "according to the SEC, neither company ever did business with 1inMM" (S); L3 thêm "Horwitz hiểu… một phần" (MH); D(4) "không đăng ký" gắn ◐ N1 ¶18 (MH); Woodbridge D(3) tái tục gắn ◐ N2 ¶90, ¶94 (MH). Gợi ý logline VI Woodbridge "nhà đầu tư trên khắp nước Mỹ": đã áp.
- **Các sửa này chưa được chấm lại bởi tác tử** (đều là thêm chủ thể/trang, hạ tầng — không thêm sự việc mới). Điều phối có thể kiểm nhanh khi rà.
- KKĐ vòng 3: sec.gov trả 403 "Request Rate Threshold Exceeded" cho tác tử (không đổi UA). Hai vế bị ảnh hưởng — Woodbridge nhịp 9 (toà ra lệnh tháng 9 và 11/2017, N1) và nhịp 12 ("by April 2019… arrested and charged", N13) — **đã K ở vòng 2**, và phiên đã tự mở N1 (2017-235: "after obtaining court orders in September and November") và N13 (2019-55, ngày 11/04/2019: "separately arrested and charged by criminal authorities, along with Woodbridge owner Robert H. Shapiro") trong phiên này. Vẫn mở lại trước khi chốt lời MR-3.

**Nguồn chưa mở được** (không vượt rào): docket CourtListener của cả hai vụ (403); thông cáo DOJ S.D. Fla. về Woodbridge (trang chống bot; API chính thức chưa thử cho vụ này); bản Consent của Horwitz; Dkt. 58 (nhịp 13 1inMM để "có điều kiện"); judgment Roseman; Investor.gov ở vòng 1 1inMM (403 với UA khai báo).

## 5. So sánh hai vụ (yêu cầu 8)
| Tiêu chí | A. Woodbridge | B. 1inMM |
|---|---|---|
| **Sức hút** | Quy mô lớn (1,29 tỷ USD, ~10.000 người), nạn nhân là người Mỹ bình thường, tiền hưu; móc "5 bang ra lệnh dừng mà vẫn bán". Thiếu một "nhân vật" có màu sắc riêng | **Cao hơn**: diễn viên Hollywood, HBO/Netflix, máy bay riêng, câu "He just played one in real life" (nếu đối chiếu được Dkt. 58). Dòng thời gian gọn, ba bước ngoặt rõ |
| **Rủi ro bị kiện** | Thấp ở trung tâm (Shapiro ●). Rủi ro nằm ở **nhiều tên phụ**: người nhà, hàng trăm đại lý (một số bị SEC kiện, kết quả chưa xác minh), relief defendants; nhiều chi tiết cơ chế chỉ có trong đơn kiện SEC (◐) → nhiều chỗ đổi tầng trong một câu chuyện | Thấp ở trung tâm (Horwitz ●), Factual Basis của plea phủ gần hết truyện ở ●T. Rủi ro riêng: **thương hiệu bị mạo danh** (HBO, Netflix) — mọi chỗ nêu phải có câu không liên quan, và hình không được gần logo/giao diện/tài liệu; 1inMM công ty chưa có phán quyết SEC; nhóm trung gian có vụ kiện tư chưa mở |
| **Giá trị bài học** | **Cao hơn và rộng hơn** cho khán giả Mỹ phổ thông: sản phẩm "lãi đều, an toàn", người bán ăn hoa hồng, tái tục, tiền hưu, lệnh của bang tra được | Tốt nhưng hẹp hơn: kỳ phiếu tư nhân qua bạn bè; bài "tự kiểm đối tác qua kênh chính thức" và "đổi lợi nhuận kỳ ngắn ra lãi năm" áp dụng rộng |
| **Chi phí (ước)** | 9,9 – 21,4 USD (tập dài hơn) | **7,9 – 17,0 USD**; ràng buộc hình (không logo/tài liệu giả) có thể kéo về mức thấp |
| **Độ chắc nguồn** | Proffer N9 mạnh; nhưng thông cáo DOJ không mở được, Roseman thiếu án, nhiều số chỉ có ở SEC | Plea N7 + judgment N8 + 3 thông cáo DOJ (qua API) đều mở được; ít chênh tầng hơn |

**Khuyến nghị của phiên:** **B (1inMM) cho tập 1, A (Woodbridge) cho tập sau.** Lý do: móc câu mạnh hơn cho kênh mới; gần như cả truyện đứng trên lời thừa nhận đã được toà chấp nhận (ít điểm đổi tầng → ít rủi ro sai lời ở MR-3); tập ngắn hơn và rẻ hơn khi quỹ OpenRouter đang thấp. Rủi ro HBO/Netflix kiểm soát được bằng câu viết sẵn và luật hình. Woodbridge có giá trị bài học cao hơn, nên làm khi đã có quy trình đo đơn giá thật sau tập 1.
Lưu ý: khuyến nghị này **khác** khuyến nghị A của MR-1/điều phối; quyết định thuộc chủ dự án. Cả hai vụ cùng trụ **Ponzi/đầu tư** — theo QUY-TRINH §4b, nếu kho đề tài (MR-K1) có vụ trụ khác, nên chen một tập khác trụ giữa A và B.

## 6. Sự cố quy trình (báo trung thực)
1. **Commit `9e0ac68` đã đẩy khi preflight TRƯỢT.** Lệnh của phiên nối `bash tools/preflight.sh | tail -1 && git commit …`; `tail` trả mã 0 nên commit và push vẫn chạy dù preflight báo **CHẶN P1 email** trong hai tệp `kiem/*-vong2.md`. Email đó là của chủ dự án, do **phiên** đưa vào lệnh cho tác tử kiểm làm phần liên hệ trong User-Agent gửi sec.gov (chính sách SEC yêu cầu khai UA), và tác tử chép lại vào báo cáo. Đã sửa: gỡ email ở commit sau; vòng 3 dùng UA không có email. **Email vẫn còn trong lịch sử nhánh** ở `9e0ac68` — phiên không force-push (luật). Điều phối/chủ dự án quyết: để nguyên, hoặc điều phối viết lại lịch sử trước khi merge (squash). Từ nay phiên chạy preflight không qua pipe.
2. **Email chủ dự án đã được gửi tới sec.gov trong header User-Agent** (phiên tự gọi 3 thông cáo + các tác tử kiểm vòng 1–2). Đây là gửi thông tin cá nhân tới dịch vụ bên ngoài mà chủ dự án không yêu cầu. Đề xuất: chủ dự án quyết một địa chỉ liên hệ riêng của kênh để khai UA với SEC, ghi vào CLAUDE.md.
3. Tác tử kiểm vòng 1 (1inMM) lưu ý: `NGUON.md` MR-1 ghi N17 (Investor.gov) "HTTP 200 (UA trình duyệt; UA khai báo bị 403)" — có thể trái luật "không đổi user-agent để vượt rào". MR-2 không dùng nội dung N17 làm nguồn cho câu nào; điều phối nên xem lại.

## 7. Chờ chủ dự án
1. Chọn vụ cho tập 1 (phiên khuyến nghị **B 1inMM**; MR-1 khuyến nghị A).
2. Duyệt khuôn 1 tập cho cả hai vụ.
3. Xử lý email trong lịch sử nhánh (§6.1) và địa chỉ liên hệ UA (§6.2).
4. Nạp OpenRouter trước M-c (mức thấp của cả hai vụ > 5,45 USD).

**DỪNG** ở cuối M-b bước 1, chờ rà.
