# Kiểm độc lập vòng 5 — các dòng vừa sửa trong hai dàn truyện

> Tác tử kiểm độc lập · 01/11/2026 · chỉ đọc, không sửa tệp được kiểm, không commit.
> Thang chấm: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được (kèm lý do).

## 1. Phạm vi đọc
- `CLAUDE.md`, `docs/HIEN-CHUONG.md` (toàn văn).
- `docs/dan-truyen/irs-callcenter-patel.md` và `docs/dan-truyen/romance-sunmola.md` (toàn văn, đọc lướt toàn bộ để tìm phát hiện thêm).
- §8 (bảng mã nguồn) của `docs/kho-de-tai/irs-callcenter-patel.md` và `docs/kho-de-tai/romance-sunmola.md`.
- Không đọc `reports/**`, `docs/kho-de-tai/kiem/**`, §1–§7 tệp kho, `docs/dan-truyen/kiem/**` (ngoài tệp này), git log/diff.

## 2. Nguồn đã mở (01/11/2026)
| Mã | Tài liệu | Đường mở | Kết quả |
|---|---|---|---|
| Patel N1 | Cáo trạng thay thế, Doc. 6, 4:16-cr-385 (S.D. Tex.) | tệp repo; SHA-256 `04fb7cb3…7b2bdf` **khớp** kho §8; `pdftoppm -r 80 -gray`, xem ảnh tr. 1, 6, 7 | đọc được |
| Patel N2 | DOJ 16-1257 (27/10/2016) | API `justice.gov/api/v1/press_releases.json` (tiêu đề) | HTTP 200 — chỉ dùng để rà lướt đ.1–13 |
| Patel N3 | DOJ 18-961 (20/07/2018) | API DOJ, tiêu đề "24 Defendants Sentenced…" | HTTP 200 |
| Patel N4 | DOJ 20-19 (09/01/2020) | API DOJ, tiêu đề "Indian National Pleads Guilty to Owning, Funding" | HTTP 200 |
| Patel N5 | DOJ 20-1294 (30/11/2020) | API DOJ, tiêu đề "Owner and Operator…", chọn số 20-1294 | HTTP 200 |
| Patel N9 | IRS FS-2017-7 | https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door — curl mặc định | HTTP 200 |
| Sunmola N2 | Opinion 7th Cir. No. 17-1299 | tệp repo; SHA-256 `cc362fa0…59953b` **khớp** kho §8; `pdftotext -layout` (tr. 1–5, 8–12, 14–15, 17) | đọc được |
| Sunmola N1 | DOJ S.D. Ill. "Prince Charming…" (02/02/2017) | API DOJ, `parameters[title]=Prince Charming` | HTTP 200 |
| Sunmola N6 | FBI/IC3 PSA I-080519-PSA | https://www.ic3.gov/PSA/2019/PSA190805 — curl mặc định | HTTP 200 |

Không gặp 403/CAPTCHA; không đổi User-Agent, không mirror, không PACER, không API trả tiền. Tệp tải về nằm trong thư mục tạm riêng dưới `/tmp/claude-0/`; python đọc tệp chạy `-I`. Đánh số đoạn DOJ: đ.n = thẻ `<p>` không rỗng thứ n trong `body`.

## 3. Bảng chấm 12 mục

| # | Dòng | Bằng chứng | Chấm | Ghi chú |
|---|---|---|---|---|
| 1 | Patel — Logline (VI) | N4 đ.1 ("between 2013 and 2016"); đ.5 ("call centers in Ahmedabad, India, impersonated officials from the IRS and… USCIS… threatened with arrest, imprisonment, fines or deportation… including by purchasing… (GPR) cards or wiring money… would immediately turn to a network of 'runners'… to liquidate and launder"); đ.6 ("admitted to operating and funding several India-based call centers"); đ.9 (Singapore bắt theo yêu cầu Mỹ, dẫn độ 04/2019); N5 đ.1 (20 năm tù, S.D. Tex.); N1 tr. 1 ("SOUTHERN DISTRICT OF TEXAS / HOUSTON DIVISION") | **K** | Chủ thể "theo DOJ" có ở cả hai vế ●T. Hai điểm nhỏ, không đổi điểm: "nhiều call center" dịch "several" — "một số" sát hơn (cùng chữ ở nhịp 6); "trả bằng thẻ trả trước hoặc chuyển khoản" bỏ chữ "including" của nguồn — nên "trong đó có". |
| 2 | Patel — Logline (EN) + dòng nguồn | N4 đ.5 (IRS impersonation, arrest threat, Ahmedabad); N4 đ.6 ("operating and funding several… call centers from which the fraud schemes were perpetrated"); N5 đ.1 ("sentenced today to 20 years in prison… in the Southern District of Texas") | **K** | Hai câu ●T đều mở "According to the Justice Department". "the calls came from India" khớp đ.5. "U.S. federal prison": N5 đ.1 chỉ ghi "in prison" do thẩm phán liên bang tuyên — "federal" là suy từ toà liên bang, chấp nhận được; nếu muốn sát chữ: "20 years in prison". Dòng nguồn ghi đúng đoạn. |
| 3 | Patel — H4 | N4 đ.5 (call centers in Ahmedabad); N4 đ.6 ("operating and funding several") | **K** | Có chủ thể DOJ; "several of them" giữ đúng mức "several". |
| 4 | Patel — L2, vế "IRS nói rõ…" (N9) | N9: "Note that the IRS does not: Call to demand immediate payment using a specific payment method such as a prepaid debit card, gift card or wire transfer." | **K** | Giữ đủ ba giới hạn: "gọi", "ngay", "phương thức chỉ định". |
| 5 | Patel — P (nguyên tắc chung) | N9 (như mục 4); N3 đ.3 (lời AG Sessions: "…conspired to bilk older Americans, legal immigrants and many others out of their life savings"); N9 mục "Know Who to Contact" nêu TIGTA và FTC | **K** | Các vế "lời khuyên chung của kênh" không bị gắn nguồn sai. "theo DOJ" cho câu của Bộ trưởng Tư pháp trong thông cáo DOJ là đúng chủ thể (sát hơn: "the Attorney General said"). N10/N11 không thuộc phạm vi mở lại vòng này; vai trò báo cáo của TIGTA/FTC có trong N9. |
| 6 | Patel — thẻ tổng kết EN, ý 3 | N9: "The IRS initiates most contacts through regular mail…"; "Generally, the IRS will first mail a bill…"; "does not… Call to demand immediate payment using a specific payment method such as a… gift card"; "does not… Threaten to bring in local police, immigration officers or other law-enforcement to have you arrested **for not paying**." | **MH** | Vế 1–2 khớp ("generally" giữ đúng). Vế 3 "doesn't threaten to have you arrested" bỏ giới hạn "for not paying" của nguồn → thành tuyệt đối hơn N9 (IRS có điều tra viên hình sự; N9 chỉ nói không doạ bắt **vì không trả**). |
| 7 | Patel — nhịp 4b và nhịp 6 (câu ◐ về HGLOBAL) | N1 tr. 1 (HGLOBAL là bị cáo [1]; 5 bị cáo-tổ chức [1]–[5]); N1 tr. 6–7 ¶3 ("five major conglomerates of call centers, all located in Ahmedabad…: HGlobal, Call Mantra, Worldwide Solution, Zoriion Communications, and Sharma BPO… often acted together… sharing call scripts and lists of potential victims, processing payments for each other"); N1 tr. 7 (bảng HGLOBAL: "HITESH PATEL (a.k.a. HITESH HINGLAJ) — Call Center Operator — India"); N3 đ.15 ("32 India-based conspirators and five India-based call centers… have yet to be arraigned… presumed innocent"); N5 đ.12 ("Charges remain pending for other India-based defendants. They are presumed innocent…"); N4 đ.2, đ.6, đ.7 | **K** | Việc xếp HGLOBAL vào "five India-based call centers" của N3 đ.15 có căn cứ: N1 tr. 1 có đúng 5 bị cáo-tổ chức, trùng tên 5 conglomerate ở Ahmedabad tr. 6–7. Mốc 07/2018 và 11/2020 gắn đúng. Lưu ý văn phong pháp lý: "HGLOBAL… **is** presumed innocent" ở thì hiện tại trong khi trạng thái HGLOBAL sau 07/2018 chưa có nguồn — câu sau đã gắn mốc nên chấp nhận; an toàn hơn: "was charged and, as of November 2020, was presumed innocent". Nhịp 6: "nhiều call center" — xem ghi chú mục 1. |
| 8 | Patel — §5(b) | N3 đ.15; N5 đ.12; N4 đ.6 ("including the call center HGLOBAL") | **K** | Không suy trạng thái HGLOBAL sau 07/2018; câu "other India-based defendants, who are presumed innocent" gắn mốc. |
| 9 | Sunmola — P (nguyên tắc chung, N6) | N6 "The FBI advises: Never send money to someone you meet online, especially by wire transfer."; "A reverse image search can determine if a profile picture is being used elsewhere…" | **K** | Hai vế gắn N6 khớp. Hai vế "lời khuyên chung của kênh" không gắn nguồn sai (vế không gửi hàng còn được N6 hỗ trợ: "Asks for money, goods… especially if you have never met in person"). Không nêu thao tác tra ảnh từng bước (N6 có — đúng là không chép). |
| 10 | Sunmola — nhịp 6 (câu duy nhất về ảnh riêng tư) | N2 tr. 2, đoạn mở bằng "In some instances, Sunmola sexually exploited the victims", câu cuối nhóm: "…threatened to post photos of a third woman." | **K** | "at least one woman" và "threatened to expose" khớp, không mạnh hơn (nguồn còn nặng hơn — câu này không kể các hành vi khác cùng đoạn, đúng §5). "private images" là cách gọi khái niệm lấy từ ngữ cảnh đoạn "sexually exploited", không thêm chi tiết. Đúng một câu, thẻ chữ, không lặp ở D/L/thẻ tổng kết; không nối với Count Eight. |
| 11 | Sunmola — nhịp 2 và D(5) | N2 tr. 2 ("Sunmola often used pictures of men in U.S. military uniforms as part of his online profile"); N1 đ.2 ("he used photographs stolen from the hacked online accounts of real American men"); N6 ("Most cyber criminals do not use their own photographs") | **K** | Hai vế tách đúng tầng (●C / ◐D), không ghép "ảnh quân phục lấy cắp". N1 không nói ảnh lấy cắp là ảnh quân phục — ghi chú trong dàn đúng. Nhỏ: N2 tr. 2 ghi "Sunmola **and his co-conspirators** created profiles… led women to believe they were successful businessmen" — nhịp 2 để chủ ngữ ngầm là Sunmola; không đổi điểm, nên thêm "ông và đồng phạm". |
| 12 | Sunmola — Logline (VI) | N2 tr. 2 (Nam Phi, từ 3/2008, phụ nữ trung niên ở Mỹ, tên giả, chiếm lòng tin rồi xin tiền và hàng, đồ điện tử); tr. 10 ("pretended to be an American soldier, stranded in Nigeria on a mission… held himself out as a colonel in the U.S. Army deployed to South Africa… purchase and ship computer equipment… finish his assignments"; tiền/thiết bị cho công việc của chính phủ Mỹ); tr. 3 (bắt ở London 09/8/2014; "Three days into trial… pleaded guilty to all counts"); tr. 1, 5 (324 tháng); tr. 18 / tr. 2 ("we affirm") | **K** | "27 năm" = 324 tháng; "giữa phiên xử" khớp "three days into trial"; câu không liên quan về quân đội có. |

## 4. Phát hiện thêm khi đọc lướt toàn bộ hai tệp
1. **Patel L3 (MH nhẹ, cùng gốc với mục 6):** "**không** doạ gọi cảnh sát hay nhân viên di trú tới bắt" bỏ vế "vì không trả" ("to have you arrested for not paying", N9). Đề xuất: "không doạ gọi cảnh sát hay nhân viên di trú tới bắt **vì không trả tiền**".
2. Không thấy hướng dẫn làm theo được (HIEN-CHUONG §1): hawala ở nhịp 5 chỉ ở mức khái niệm, có cảnh báo không chép N3 đ.14 / N1 tr. 4–6; Sunmola không nêu dịch vụ chuyển tiền, cách mua dữ liệu thẻ, thao tác tra ảnh.
3. Không thấy lời gọi điện dựng lại (Patel): H1 không lời thoại, H2 tóm tắt ngôi thứ ba; ghi chú cấm dựng cuộc gọi có mặt ở §1, §2, §6.
4. §5 (Sunmola): nhánh ảnh riêng tư đúng một câu khái niệm (nhịp 6), không nhắc lại trong D, L, P hay thẻ tổng kết; không dùng tuổi + hoàn cảnh (tr. 8) hay bang (tr. 2); thẻ tổng kết ý 2 chỉ dùng câu khái quát của toà (N2 tr. 8–9: "divorced, abandoned, widowed… seeking companionship"). Không thấy vi phạm.
5. Rà nhanh các nhịp khác với nguồn đã mở (Patel N2 đ.1, 9–13; N3 đ.1, 3, 8, 9, 11, 15; N4 đ.2, 7–11; N5 đ.1–2, 12; Sunmola N2 tr. 3–5, 11–12, 14–15, 17; N1 đ.2–7, 11): không thấy thêm MH/S thực chất.

## 5. Tổng
**12 mục: K 11 · MH 1 · S 0 · KKĐ 0.** Phát hiện thêm: 1 MH nhẹ (Patel L3, cùng gốc với mục 6).

| Mục | Chấm | Đề xuất sửa |
|---|---|---|
| 6 — Patel thẻ tổng kết ý 3 | MH | "…and doesn't threaten to have you arrested **for not paying**." |
| Thêm — Patel L3 | MH nhẹ | Thêm "vì không trả tiền" sau "tới bắt". |
| (tuỳ chọn, không tính điểm) | — | Patel logline VI/nhịp 6 "nhiều call center" → "một số call center"; logline VI "trả bằng…" → "trả bằng nhiều cách, trong đó có…"; nhịp 4b "is presumed innocent" → gắn mốc 11/2020; Sunmola nhịp 2 thêm "ông và đồng phạm". |
