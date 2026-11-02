# Kiểm độc lập vòng 8 — dàn truyện `theranos-holmes` (tập 4)

> Tác tử kiểm độc lập · 02/11/2026 (UTC) · đối tượng: `docs/dan-truyen/theranos-holmes.md` (bản trong cây làm việc lúc kiểm). Căn cứ luật: `docs/HIEN-CHUONG.md` §3 (luật 1–8), §4, §5; `docs/QUY-TRINH-TAP.md` §6. Có đọc `docs/kho-de-tai/theranos-holmes.md`. **Không** đọc `reports/**`, `docs/dan-truyen/kiem/**` (ngoài tệp này), lịch sử git, `docs/kho-de-tai/kiem/**`. Không gọi API trả tiền, không sửa dàn truyện, không commit.

## Kết luận

**Đạt, còn 1 điểm MH nhẹ cần sửa** (nhãn hình nhịp 7). **0 S.** Các kiểm riêng (1)–(8) đều đạt:
1. Phán quyết Holmes (kết án 4: Count 1, 6–8 · trắng án 4: Count 2, 10–12 · treo 3: Counts 3–5, nhà đầu tư C-1 · Count 9 bị rút) đúng ở §0, H4, nhịp 14, câu nối nhịp 15, logline (logline/H4 không nêu Count 9 — lược, không sai). Không chỗ nào nói hay ám chỉ Holmes bị kết án lừa bệnh nhân.
2. Balwani chỉ theo bản án của ông (N1 tr. 16; N7; N8): 12/12 tội, 07/07/2022, 155 tháng, 3 năm giám sát, 07/12/2022 — khớp.
3. Không tên bệnh nhân, nhà đầu tư, nhân chứng (chỉ nêu Holmes, Balwani, Thẩm phán Davila).
4. Mọi câu "not accused" đúng chủ thể (ngoại lệ "Apart from Theranos, Holmes and Balwani" đúng vì SEC kiện Theranos — N2), đều có "in these cases", có nguồn (N1 tr. 8 "charged Holmes and Balwani"; N4; N2; N1 tr. 14, 16–17), đặt đúng quy tắc §0 (H5; nhịp 2, 3, 4b, 12; Walgreens 2, 3, 7, 9, 16; hãng dược 3, 7; quân đội 3, 8; tổng 10, 18).
5. Luật 8 (a)–(f) đạt.
6. Không hướng dẫn làm theo được (không "null protocol", không cách sửa máy, không mẫu tài liệu).
7. Số trang N1 dẫn đúng (đã mở từng trang bằng `pdftotext -layout`), không dẫn tr. 3–6.
8. "Bảy câu kiểm" nhất quán: 6 câu từ 7 nhóm (A)–(G) ((A)+(F) gộp Kiểm 1; (C) Kiểm 2; (B) Kiểm 3; (G) Kiểm 4; (E) Kiểm 5; (D) Kiểm 6) + Kiểm 7 của kênh — khớp §0, nhịp 3, H5, §3, §6.

## Nguồn đã mở trong vòng này

| Mã | Đường mở | Kết quả |
|---|---|---|
| N1 | tệp repo; SHA-256 `4f591641abf798a74e8e107a9b0f129bd9cbef3b03b10566ba05c02c578e32da` | **khớp**; đọc tr. 1–3, 7–17, 30–33, 52–54 |
| N2, N3 | bản phiên chính đã tải (scratchpad `src/sec/lr-24069.html`, `2018-41.html`) — không tự tải sec.gov | đọc toàn văn; cụm then chốt có trong HTML |
| N4–N8 | API DOJ `press_releases.json?parameters[title]=Theranos&pagesize=50` | 200; 6 kết quả (ngày 15/06/2018, 04/01/2022, 07/07/2022, 18/08/2022, 18/11/2022, 07/12/2022) |
| N9 | curl mặc định | 200; "Updated October 20, 2026"; 0 lần "Holmes", 0 lần "Balwani" |
| N11 | curl mặc định | 200 ("BrokerCheck - Find a broker…") |
| N12 | curl mặc định | 200 ("ReportFraud.ftc.gov") |
| N14 | curl mặc định, JSON | 200; 24965-111 → Bryan, projRelDate 02/22/2030; 24966-111 → Lompoc II, 04/21/2033 |

## Bảng chấm

| Dòng | Điểm | Nguồn + trang | Ghi chú / sửa |
|---|---|---|---|
| Đầu tệp (quy ước trang, ký hiệu tầng) | K | N1 tr. 3 chú thích "*This summary constitutes no part of the opinion of the court"; tr. 15–16; N7; N8 | |
| §0 (1) phán quyết bốn mảnh | K | N1 tr. 15; N5 | |
| §0 (2) Balwani | K | N1 tr. 15–16; N7; N8 ("former romantic partner") | |
| §0 (3) không tên | K | N1 tr. 10, 12, 13 | Danh sách trang nêu tên chưa đủ (tr. 14 tên hãng dược, tr. 30/32 tên nhân chứng) nhưng §5 và §8 đã chặn — không tính điểm |
| §0 (4) câu "not accused" | K | N1 tr. 8, 16–17; N4; N2 | Xem gợi ý G2 (nhịp 10) |
| §0 (5) cơ chế | K | N1 tr. 12 | |
| §0 (6) bảy câu kiểm | K | N1 tr. 10–11 | |
| Logline (VI) | K | N6 ("induce dozens of investors… hundreds of millions"); N1 tr. 15–16, 54 | |
| Logline (EN) | K | N1 tr. 7, 15, 16–17 | "investors put in hundreds of millions" không chủ thể DOJ nhưng được N1 tr. 16–17 đỡ (bồi hoàn 397 triệu = số tiền 12 nạn nhân đã đầu tư). Gợi ý G1 |
| H1 | K | N1 tr. 7 | Trích đúng nguyên văn |
| H2 | K | N1 tr. 7; N3 ("Silicon Valley-based") | |
| H3 | K | N6 ("Evidence showed that Holmes… was able to induce dozens of investors…") | ●D có chủ thể |
| H4 | K | N1 tr. 15; N5; N6 ("On January 3, 2022") | Tách 3 vế đúng |
| H5 + câu kèm | K | N1 tr. 16 (12 nhà đầu tư là "victims"); N4; N2 | |
| Ghi chú sau móc câu | K | — | |
| Nhịp 0 | K | §1 | |
| Nhịp 1 | K | N1 tr. 8 (2003, CEO tới 2018, "claimed goal"), tr. 9 (Edison; Balwani 2009, President/COO) | Không quan hệ riêng — đạt 8f |
| Nhịp 2 + câu kèm | K | N1 tr. 10 (Walgreens thu 2013; C-1 cuối 2013; C-2 2014; "not publicly traded"); tr. 17; tr. 16; N4; N2 | |
| Nhịp 2b | K | N3 (Steven Peikin, Co-Director Enforcement: "…non-public, development-stage, or the subject of exuberant media attention.") | Chủ thể "an SEC enforcement official" đúng chức vụ |
| Nhịp 3 + câu gộp | K | N1 tr. 10–11 ("generally fell in the following categories" (A)–(G)) | ◐ đúng; câu gộp đúng chủ thể |
| Nhịp 4 | K | N1 tr. 10 (300/12; "general chemistry tests"; "various modifications"); tr. 11 (QC; "dismissed… or shifted blame") | |
| Nhịp 4b + câu kèm | K | N1 tr. 12 ("Multiple investors testified…"); tr. 16; N4; N2 | |
| Nhịp 5 | K | N1 tr. 12 | Có người khai; không "null protocol" |
| Nhịp 6 | K | N1 tr. 12 (0 doanh thu 2012–2013; lỗ 57/92 triệu; 15 triệu tiền mặt, 2 triệu/tuần; IRS 1.944.948; lãi 230 triệu) | |
| Nhịp 6b | K | N6 ("Holmes misrepresented to other investors… over $100 million… nearly $1 billion in 2015"); N5 | |
| Nhịp 7 — sự việc | K | N1 tr. 14 ("Holmes admitted that she personally affixed…"; email gửi Walgreens; đại diện các hãng khai); tr. 8 | |
| Nhịp 7 — hình "LOGO ADDED — per trial testimony" | **MH** | N1 tr. 14 | N1 chỉ ghi "Holmes admitted", **không** nói lời thừa nhận đó là lời khai tại phiên xử; N5/N6 nói "evidence showed… provided reports… with logos", không nói ai gắn. Nhãn gán nguồn "trial testimony" mạnh hơn điều đã mở. **Sửa:** "LOGO ADDED — Holmes admitted it, per the appeals court (9th Cir. 2025)" hoặc "LOGO ADDED — per U.S. v. Holmes (9th Cir. 2025)" |
| Nhịp 7 — câu kèm (hãng dược; Walgreens) | K | N1 tr. 14, 17, 8; N4; N2 | Gợi ý G3 (ghi nguồn cho vế "not accused" của hãng dược) |
| Nhịp 8 + lời trích + câu kèm | K | N1 tr. 12–13 (200 triệu từ DoD; vị tướng khai; bản ghi âm 12/2013 — trích đúng nguyên văn); N4; N2 | Không tên vị tướng |
| Nhịp 9 + câu kèm | K | N1 tr. 13–14; N6 ("from a few dozen to 900… stagnating"); tr. 17 | |
| Nhịp 10 + câu kèm | K | N1 tr. 7 ("captivated… high-ranking members of the United States military"); N6 ("In its memorandum filed for the sentencing hearing… more than $4 billion… cover of…"); N4; N2 | Gợi ý G2 |
| Cú treo (2 câu) | K | N6 (bản ghi nhớ tuyên án: "By the end of 2014, her stock… more than $4 billion"); N1 tr. 11 ("unannounced inspection… in late 2015") | |
| Nhịp 11 | K | N1 tr. 7–8 (báo chí cuối 2015), tr. 11 (CMS; "immediate jeopardy"), tr. 30–31 (báo cáo ban hành 01/2016, Theranos nhận đầu 2016), tr. 32 (nhân chứng khai "voided all patient tests run on the Edison") | Gợi ý G4 (định nghĩa ●C) |
| Nhịp 12 + câu kèm | K | N2; N3 (14/03/2018; >700 triệu; 500.000 USD; cấm 10 năm; 18,9 triệu cổ phần; quyền biểu quyết; "subject to court approval"; "neither admitted nor denied"; kiện Balwani tại toà) | ◐ đúng; không "court ordered" |
| Nhịp 13 | K | N4 (truy tố, công bố 15/06/2018); N5 ("initially charged on June 14, 2018"; "July 28, 2020… superseding indictment"); N1 tr. 8 (2,5 năm điều tra), tr. 15 (cuối 2021 / đầu 2022; gần bốn tháng) | |
| Nhịp 14 | K | N1 tr. 15; N5 ("wire transfers totaling more than $140 million"); N6 (03/01/2022) | |
| Nhịp 15 + câu nối | K | N1 tr. 15 (bệnh nhân khai; bằng chứng gắn Balwani), tr. 16; N7 (07/07/2022; 6 + 4 tội); N8 (155 tháng; 3 năm giám sát; "different federal jury") | Câu nối đúng: trắng án Count 2 + 3 tội; 1 tội bị rút |
| Nhịp 16 + câu kèm | K | N6 (18/11/2022; Davila; 135 tháng; 3 năm; "No fine"; "ordered to surrender on April 27, 2023"); N1 tr. 15 (120 triệu), tr. 16–17 (05/2023; liên đới 452 / 397 / 54,5 triệu; Safeway, Walgreens là "victims") | Gợi ý G3 |
| Nhịp 17 + trạng thái | K | N1 tr. 2, 8, 53 (trích nhà đầu tư đúng nguyên văn; "[un]able to liquidate"), 54 ("affirm… restitution order in its entirety"); N14; N9 | Trạng thái vẫn đúng ngày 02/11/2026 |
| Nhịp 18 + câu kèm | K | §4; N1 tr. 8, 16–17; N4; N2 | |
| Ghi chú sau bảng nhịp (MH, lời trích) | K | N1 tr. 7, 9, 13, 53; N3 | |
| §3 Khuôn tập | K | QUY-TRINH §6 (12:55); `docs/dan-truyen/1inmm-horwitz.md` (~16 phút) | |
| L1 | K | N1 tr. 10, 53; N3 | |
| L2 | K | N1 tr. 7, 13–14; N6 | |
| L3 | K | N1 tr. 12; N3 (Jina Choi, Director SF Regional Office — trích đúng nguyên văn) | |
| D1 | K | N1 tr. 14 | |
| D2 | K | N1 tr. 12 | |
| D3 | K | N1 tr. 12 | |
| D4 | K | N1 tr. 12–13 | |
| D5 | K | N1 tr. 13–14 | |
| P | K | N11, N12 (200); N10, N13 KKĐ | Không khuyên sản phẩm/pháp lý |
| Thẻ tổng kết | K | N1 tr. 53 | Đường "sec.gov/tcr" KKĐ (sec.gov) |
| §5 (a) | K | N1 tr. 15–16, 54; N5; N6 | |
| §5 (b) | K | N2; N4 | |
| §5 (c) | K | — | |
| §5 (d) | K | N1 tr. 7 ("mirage"), tr. 8 ("half-truths and outright lies") | |
| §5 (e) | K | như các nhịp | |
| §5 (f) | K | N6 (dinh thự, máy bay), N1 tr. 9, 15 | |
| §5 KBCB | K | N1 tr. 10, 12, 13, 15, 32; N8 | |
| §5 phép thử | K | — | |
| §6 Ước chi | K | QUY-TRINH §6 | Số học khớp: 5,60/9,00/13,20 USD; 2.635 từ × 6,1 ≈ 15.900 × 0,4401 ≈ 7.000; 2.475/3.300/4.125; ≈ 9.500/12.050/14.600; 12.230/2.005 = 6,10; trần 9,00 × 1,15 ≈ 10,35 → 10,40; 12.050 × 1,15 ≈ 13.860 → 14.000 |
| §7 N1 | K | SHA-256 khớp | |
| §7 N2 | KKĐ | — | Nội dung khớp bản phiên chính; phần "đã mở, 200, UA khai báo" phụ thuộc sec.gov |
| §7 N3 | KKĐ | — | như N2 |
| §7 N4–N8 | K | API DOJ (6 kết quả) | |
| §7 N9 | K | curl 200 | |
| §7 N10 | KKĐ | — | sec.gov |
| §7 N11 | K | curl 200 | |
| §7 N12 | K | curl 200 | |
| §7 N13 | KKĐ | — | adviserinfo.sec.gov |
| §7 N14 | K | curl 200 (JSON) | |
| §7 N15 | KKĐ | — | sec.gov; không dùng cho nhịp nào |
| §7 Investor.gov | KKĐ | — | ngoài danh sách được mở trong lệnh; không dùng |
| §8 (1) trạng thái | K | — | |
| §8 (2) judgment / lệnh SEC | K | — | |
| §8 (3) ảnh trang hồ sơ | K | N1 tr. 1, 9, 10, 12–15, 54 | Bố cục tr. 15 khớp mô tả |
| §8 (4) lời Holmes nhịp 8 | K | N1 tr. 13 | |

## Gợi ý văn phong (không tính điểm)
- **G1** Logline EN / H4: "four counts of defrauding investors" gộp cả tội âm mưu (Count 1). H4 đã tách "one conspiracy count and three wire-fraud counts" nên đạt; logline EN có thể viết "four investor-fraud counts" (N1 tr. 15 "four investor-related counts") cho sát tội danh.
- **G2** Nhịp 10 nêu "high-ranking members of the U.S. military"; câu kèm gộp có "military officers" nhưng không có "the U.S. military" như mẫu §5 (e) cho quân đội. Có thể thêm "the U.S. military" vào câu gộp nhịp 10 cho đúng chữ quy tắc §0.
- **G3** Cột nguồn câu kèm: nhịp 7 nên ghi rõ "câu kèm hãng dược: N1 tr. 8, 14; N4; N2"; nhịp 16 nên thêm "N1 tr. 17" vào cột câu kèm (hiện đã có trong cột chính tr. 15–17).
- **G4** Định nghĩa ●C (dòng 8) chỉ nhắc "Factual Background / Procedural History", trong khi nhịp 11 (tr. 30–32) và nhịp 17 (tr. 53) dùng phần phân tích của opinion. Nội dung vẫn là toà thuật lại lời khai/kết luận sơ thẩm — có thể mở rộng định nghĩa cho khớp.

## Không kiểm được
- N2, N3, N10, N13, N15 (sec.gov) và Investor.gov: KKĐ (sec.gov không mở theo lệnh; Investor.gov ngoài danh sách). Nội dung N2/N3 đã kiểm trên bản phiên chính tải.
- Lời khai "đã mở ngày 01/11/2026" của phiên soạn cho các nguồn sec.gov (UA khai báo, HTTP 200): không kiểm lại được.

## Tổng đếm
**77 dòng: K 70 · MH 1 · S 0 · KKĐ 6.**
