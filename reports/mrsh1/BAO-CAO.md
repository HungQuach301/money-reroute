# BÁO CÁO MR-SH1 — Short dọc 1 từ tập 1 `tap01-1inmm` (1inMM / Horwitz)

> Phiên Claude Code · 02/11/2026 · nhánh `claude/short-doc-1inmm-horwitz-4pnmgb` (từ `main` @ `f144554`). Lệnh `[MR · MR-SH1]`.
> **Chi 0 USD** (trần 0 mọi khoản): không sinh tranh, giọng, nhạc, video mới; không gọi API trả tiền; không thêm dòng `CAPS_PHIEN`. **DỪNG — chờ rà.**

## 0. Tóm tắt
| Hạng mục | Kết quả |
|---|---|
| Bản xem | **`reports/mrsh1/xem/short1.mp4`** (LFS) — 1080×1920, 30 fps, H.264 CRF 18 + AAC 256k, **55,0 s** |
| Lời | Nguyên đoạn P01 (`lab/mr4/tts/P01_l2.mp3`, S004–S011, giữ **S008 KBCB đọc**). **Giữ S011** (vẫn ≤ 59 s). Không câu mới |
| Hình | 11 cảnh tranh cắt dọc (10 tranh + clip K2) · 4 đồ hoạ L2 dọc · 1 crop L3 (N7 tr. 11) · thẻ KBCB · thẻ tên · phụ đề 31 cụm + 2 nửa KBCB · thẻ cuối 3 s |
| Âm | **−14,0 LUFS, đỉnh thật −1,5 dBTP** (đo trên tệp mp4, ebur128); nhạc N1 thấp hơn lời 20 LU khi có lời |
| Kiểm | tờ 0,5 s (110 ô) mắt xem → 1 lỗi sửa; máy đối chiếu chữ **70 chuỗi, 0 cờ**; YuNet trên khung cắt dọc: mọi cờ (ngưỡng 0,3) mắt xem là gáy/bóng lưng/tay/đèn — **không lộ má/tai/mặt** |
| Gói | `docs/tap01-1inmm/phat-hanh/SHORT-1.md` — 3 tiêu đề (kèm ghi chú kiểm S1, S3), mô tả EN 1.154 ký tự, AI use = Yes, Related video = tập 1 |

## 1. Dòng thời gian (giây trong Short)
Giọng P01 đặt ở **0,9 s** (hết 51,98 s). Mốc câu/từ = whisper giọng thật (`reports/mr4/whisper/P01_l2_sochu.json`) + 0,9 s. Cảnh đổi 0,35 s trước tiếng, hoà 0,35 s.

| Giây | Câu | Cảnh | Lớp chồng |
|---|---|---|---|
| 0–1,5 | — | L1 `a07` (bóng lưng dưới đèn) | **chữ móc câu** "25 to 45 percent" (đỏ cam) / "six or twelve months" — chỉ hai cụm có trong lời S005 (lệnh). Không phụ đề trong 1,5 s đầu |
| 0,9–7,2 | S004 NB | `a07` → `b001` (gương phòng thay đồ) → `b067` (phim trường, bóng lưng nhỏ) → `b002` (tay áo vest + đồng hồ cát) | thẻ tên "Zachary Horwitz / aka “Zach Avery” · actor, Los Angeles" (như MR-6) |
| 7,8–16,3 | S005 ●T | **GA** kỳ phiếu: đồng hồ "6 OR 12 MONTHS / typically came due" → hạt chạy → **25–45 %** đếm (điểm nhấn) "PROMISED RETURN" | |
| 16,3–19,7 | S006 ●T | `a09` (kho cuộn phim) → `b070` (dải phim) | |
| 19,7–28,1 | S006–S007 ●T | **GB** "HE TOLD INVESTORS": FILM RIGHTS → STREAMING PLATFORMS → DISTRIBUTION DEALS (hiện theo mốc "licensed", "streaming", "distribution"); dấu **"FAKE — admitted"** đóng đúng mốc "fake" (điểm nhấn), hạt tiền tắt | |
| 28,1–32,6 | S007 (nhãn) / S008 (lời) | **L3** N7 tr. 11 nền ngà, khoanh "purported copies of the distribution agreements were fake" sau 0,5 s, đẩy nhẹ về câu khoanh | thẻ KBCB nửa 1 |
| 32,6–37,6 | S008 KBCB | `b003` (hành lang trống) → `a15` (rạp trống) | thẻ KBCB nửa 2 ("… did business with 1inMM.") |
| 37,6–41,2 | S009 ●T | **GC** "AT LEAST" → **$650,000,000+** đếm (điểm nhấn, hạt hổ phách đổ vào) → "CAME IN" | |
| 41,2–43,5 | S010 ● | `a12` (toà nhà cột) | |
| 43,5–46,6 | S010 ● | **GD** "SENTENCED IN 2022" · 20 ô năm sáng dần · **20 YEARS** đếm (điểm nhấn) · "IN PRISON" | |
| 46,6–52,0 | S011 CHUNG | clip Veo **K2** cắt dọc (bóng lưng nhìn thành phố) | |
| 52,0–55,0 | — | **thẻ cuối 3 s**: "Full case + 5 red flags" / "→ Money Reroute" trên nền K2 mờ | nhạc nâng, tắt dần 1,5 s |

Ghi chú mốc: `moc_cau.json` MR-6 căn S008 lệch (khớp 0,793, mốc đầu rơi vào "and" thứ hai, trễ 0,56 s) → Short lấy mốc đầu S008 = từ "HBO" lần 2 trong whisper (ghi trong `short1.py`).

## 2. Hình — chi tiết theo lệnh
- **Tranh cắt dọc:** cửa sổ 432×768 (9:16) trên tranh 1376×768, tâm cắt chọn tay theo chủ thể (`CANH` trong `short1.py`), phóng 2,5× LANCZOS + làm nét nhẹ; chuyển động đẩy/kéo 1,00 ↔ 1,09; dải tối trên/dưới cho chữ. Chỉ dùng tranh đã qua QC MR-6/MR-P1. **Không dùng** tranh nhà đầu tư (b062, b063) để tránh thêm nhân vật có mặt vào 55 s.
- **Luật người thật (kiểm lại sau cắt):** người vest tối xuất hiện ở `a07`, `b067`, `b002` (chỉ tay/tay áo), K2 — đều **lưng/gáy, bóng tối**, không góc 3/4. Mắt xem phóng to vùng đầu từng cảnh (và các khung K2): không má, không tai, không nét mặt. Mọi cảnh có người mang nhãn "ILLUSTRATIVE — not the real person"; cảnh không người mang "ILLUSTRATIVE".
- **L2 dọc** (`scripts/mrsh1/short1.py` — GA, GB, GC, GD; dùng icon/hạt/đếm của `scripts/mr6/l2.py`): nền than + lưới; hiện theo mốc từ; **một điểm nhấn đỏ cam mỗi đồ hoạ** (25–45 % · dấu FAKE · $650,000,000+ · 20 YEARS); gạch tiêu đề đổi sang teal để giữ một điểm đỏ; số trung gian khi đếm không ghi sổ chữ (như MR-6).
- **L3:** ảnh trang PDF thật 220 dpi (`ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf`, SHA-256 khớp NGUON.md), crop dòng 8–15, **không vẽ lại chữ**; vị trí khoanh tìm máy bằng `pdftotext -bbox` (hàm `dung.tim_cum`). Tiêu đề "PLEA AGREEMENT · U.S. v. HORWITZ / Dkt. 45 · page 11" (tách hai dòng từ tiêu đề MR-6). Trang này không thuộc danh sách cấm SHOT.
- **Nhãn + nguồn:** lấy từ `dung.nhan_tang` / `dung.nguon` (sinh từ `loi.json`, cùng bộ MR-6 đã qua kiểm pháp lý lần 2): ●T → "● CONVICTED · admitted in plea" + Plea Agreement, Dkt. 45, p. 9/10/11/12; S010 ● → "● CONVICTED" + Judgment, Dkt. 75, p. 1; DOJ 22-027; S004 NB và S008 KBCB chỉ dòng nguồn; S011 CHUNG không nhãn. Khối nhãn đặt trên vạch 15 % đáy (y ≤ 1632).
- **Phụ đề cháy hình:** Inter Bold 66, trắng viền đen, trục x = 510 (bề rộng ≤ 820 → mép phải ≤ 920 < 972), tâm y ≈ 1330; cụm 2–5 từ đúng thứ tự lời, bật theo mốc từ whisper (khớp **từ chính xác**). Số viết chữ số khi hiện ("25 to 45 percent", "$650 million", "2022", "20 years"), "one-in-M-M" hiện "1inMM" (như thẻ KBCB MR-6). S008 hiện dạng **thẻ KBCB nền tối** (serif, vạch teal) chia hai nửa câu — vừa là phụ đề vừa là thẻ "không liên quan".
- **Vùng an toàn Shorts:** mọi chữ trong x ≤ 972, y ≤ 1632; nhãn ILLUSTRATIVE ở y 150–200.

## 3. Âm
- Giọng P01_l2 (−18,3 LUFS gốc) + N1 (−12,6 LUFS gốc). Khuếch N1 **−25,7 dB** → thấp hơn lời **20 LU** trong lúc có lời; +6 dB trong 0,9 s đầu (chưa có lời), +8 dB ở thẻ cuối, tắt dần 1,5 s. N1 dài 40 s < 55 s → nối N1 với chính nó từ giây 6 (hoà chéo 4 s).
- Loudnorm hai lượt (đích −14 / TP −1,5) → đo trên tệp ra: **WAV −14,0 LUFS / −1,5 dBTP; MP4 (AAC) −14,0 LUFS / −1,5 dBTP** (`reports/mrsh1/do_am.json`). Đạt −14 LUFS, TP ≤ −1 dBTP.

## 4. Kiểm
| Kiểm | Kết quả | Tệp |
|---|---|---|
| Tờ 0,5 s | 110 ô, mắt xem. Lần dựng 1: **17,5–18 s hai cụm phụ đề chồng nhau** (khoá "to" khớp tiền tố "told") → sửa khớp từ chính xác, dựng lại; lần 2 sạch. Các điểm khác: đếm số chạy đúng, dấu FAKE đúng mốc, L3 khoanh đúng câu, thẻ cuối 3 s đủ | `reports/mrsh1/xem/to05s.jpg` |
| Máy đối chiếu chữ | `scripts/mrsh1/kiem.py`: **70 chuỗi, 0 cờ**. Luật: phụ đề/KBCB/chữ móc câu/đồ hoạ/thẻ tên phải là **đoạn liền** của một câu S004–S011 sau bảng đổi số → chữ; 3 chuỗi không liền có bảng riêng kèm cụm bắt buộc ("FAKE — admitted" ← S007; "$650,000,000+" ← S009 "at least … six hundred fifty million dollars"; "SENTENCED IN 2022" ← S010; thẻ tên ← S004); nhãn ∈ tập HIEN-CHUONG; nguồn = đúng `dung.nguon(câu)`; tiêu đề L3 ⊂ tiêu đề MR-6; thẻ cuối = nguyên văn lệnh. Kèm bảng nhãn/nguồn theo cảnh ↔ tầng `loi.json` | `reports/mrsh1/doi_chieu_chu.json`, `chu_tren_hinh.json` |
| Mặt (YuNet 2023mar, ngưỡng 0,3 — thấp hơn 0,6 của MR-6 để bắt rộng) | Quét 10 tranh cắt dọc (mức phóng 1,00 và 1,09), 8 khung K2, 110 khung tờ 0,5 s. Cờ: `a07` (0,63 ở mức phóng — gáy người đứng lưng), `b067` (0,34 — gáy nhỏ), `b002` (0,51 — bàn tay), `b001` (0,48 — khung gương đèn), `b070` (0,35 — ô dải phim mờ), K2 (≤ 0,42 — đèn thành phố / gáy), khung 40,0 s (hạt đồ hoạ). **Mắt xem phóng to từng vùng: không có mặt, má, tai** — đều báo nhầm | `reports/mrsh1/qc_mat.json` |
| Thời lượng / định dạng | 55,0 s ≤ 59 s; 1080×1920; 30 fps | `do_am.json` |

## 5. Gói phát hành Short
`docs/tap01-1inmm/phat-hanh/SHORT-1.md`: 3 tiêu đề theo lệnh; mô tả EN (câu S007/S004, S009/S010 như mô tả tập 1 đã duyệt G2; câu KBCB nguyên văn; 3 nguồn chính có liên kết — Plea Agreement Dkt. 45, SEC Lit. Rel. 25067, DOJ 22-027; dòng khai AI HIEN-CHUONG §6 nguyên văn; dòng "education only"); **AI use = Yes**; ghi chú **Related video = tập 1**. URL lấy từ gói tập 1 (đã mở ở MR-3/MR-6); phiên này không mở lại nguồn.

## 6. Lệch / cần điều phối quyết (nói rõ)
1. **Tiêu đề S1** "He Sold Fake Netflix Deals for $650 Million": (a) tên Netflix trong tiêu đề hiện ở bảng tin/tìm kiếm không kèm câu KBCB (luật 8e yêu cầu câu nói rõ không liên quan; THUMBNAIL-RULES tập 1 cấm chữ "Netflix" trên thumbnail); (b) "sold … deals" lệch hồ sơ — thứ bán là kỳ phiếu, hợp đồng phân phối mới là thứ giả (N7 tr. 9–11). Phiên **không** sửa tiêu đề của lệnh, chỉ ghi cảnh báo.
2. **Tiêu đề S3** "45% in 6 Months? …": N7 tr. 10 nói kỳ hạn "typically six or twelve months" và lãi "ranged from 25 to 45 percent" — **không ghép 45 % với 6 tháng**. Đề xuất thay thế: "25–45% Returns? The Red Flag Investors Missed". Phiên khuyến nghị **S2**.
3. Phần L3 (N7 tr. 11) chạy sang 3 s đầu câu KBCB S008 (thẻ KBCB chồng lên, nhãn/nguồn vẫn của S007) — để câu "were fake" có đủ ~4 s đọc trong 55 s. Nếu điều phối muốn tách hẳn, đổi `T01` sang trước mốc "fake" (mất dấu FAKE trên L2) hoặc rút L3 còn ~2 s.
4. Chữ L3 nhỏ trên điện thoại (dòng trang ~20 px cao trên khung 1080 px) — khung khoanh đỏ cam + dòng nguồn + phụ đề "were fake." đã dẫn mắt; không phóng quá bề ngang để không cắt câu.
5. Tranh phóng 2,5× từ ảnh 1K → hơi mềm ở 1080×1920 (chất tranh vẽ + hạt che bớt). Muốn nét hơn cần sinh lại tranh dọc — có phí, ngoài lệnh này.
6. Đếm số: khung đầu của bộ đếm có hiện "0%"/"$0" khoảng 0,3 s trước khi chạy (như MR-6) — giá trị trung gian không ghi sổ chữ.

## 7. Tệp
- Dựng/kiểm: `scripts/mrsh1/short1.py`, `scripts/mrsh1/kiem.py` (dùng lại `scripts/mr6/l2.py`, `scripts/mr6/dung.py`).
- Ra: `reports/mrsh1/xem/short1.mp4` (LFS), `reports/mrsh1/xem/to05s.jpg`, `reports/mrsh1/{chu_tren_hinh,doi_chieu_chu,qc_mat,do_am}.json`, `reports/mrsh1/CHECKPOINT.md`, `docs/tap01-1inmm/phat-hanh/SHORT-1.md`.
