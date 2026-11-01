# BÁO CÁO MR-3 — M-b bước 2 → G1: Kịch bản tập 1 "1inmm-horwitz"

> Phiên Claude Code, 01/11/2026. Nhánh `claude/lucid-goldberg-vcpyv1` từ `main` @ `6296c0e`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD** — không gọi API trả tiền, không sinh giọng/hình/nhạc, không 402. Chỉ đọc hồ sơ công khai (PDF trong repo, sec.gov với UA khai báo của kênh, API thông cáo DOJ, RECAP). Địa chỉ liên hệ của kênh chỉ nằm trong header request, **không** có trong tệp, commit hay lệnh lưu cho tác tử con. Không merge, không xoá nhánh, không force-push.
> 4 lượt tác tử kiểm độc lập (mỗi vòng một tác tử mới, không đọc nháp/báo cáo/kết quả vòng trước).

## 1. Sản phẩm (`docs/tap01-1inmm/`)

| Tệp | Nội dung |
|---|---|
| `NGUON.md` | 18 nguồn đã mở ở MR-3 (giữ mã N; **N22 mới** = Dkt. 58), SHA-256 6 PDF khớp; bảng 12 câu trích nguyên văn (8 câu đối chiếu ảnh trang); §3 nguồn **chưa mở được**; §4 kiểm trạng thái vụ |
| `loi.json` | **Nguồn chuẩn của lời**: 102 câu, mỗi câu `tang` + `nguon` (mã + trang) + `chu` (chữ trích trên hình); en-US; số viết bằng chữ |
| `LOI.md` | Dựng máy từ `loi.json` bằng `scripts/mr3/loi_md.py` (kèm kiểm K1–K7, thống kê, bảng phát âm) |
| `kiem/vong1.md`, `kiem/vong2-4.md` | Kết quả kiểm lời độc lập |
| `SHOT.md` | 44 hàng shot, 16 khe Veo (mức giữa) |
| `UOC-CHI.md` | Ước chi 3 mức + đề xuất trần từng khoản M-c/M-d/M-e + số dư OpenRouter cần |
| `PHUONG-AN.md` | 3 tiêu đề, 2 ý thumbnail, 2 phương án giọng, 2 bảng màu/chữ |

Thêm: `ho-so/1inmm-horwitz/doj-sentencing-position-2022.pdf` (Dkt. 58, Git LFS, SHA-256 `3626166d…1575`); `scripts/mr3/loi_md.py`.

## 2. Bước 1 — Nguồn

| Nguồn | Kết quả MR-3 |
|---|---|
| N3 (SEC Lit. Rel. 25067), N2, N5 | **Mở lại được**, HTTP 200, UA khai báo của kênh |
| N10, N11, N12 (DOJ) | **Mở lại được** qua API chính thức `justice.gov/api/v1/press_releases.json` (trang HTML là kiểm tra bot — không vượt). N12: API trả 2 kết quả, chọn 22-027 |
| **Investor.gov (N17)** | **HTTP 403 với UA khai báo → "chưa mở được"**. Không đổi UA. Lời kết không dẫn Investor.gov; dùng N18–N21 (đều mở lại được, HTTP 200) |
| **Dkt. 58 (N22)** | **Đọc được qua RECAP** (`storage.courtlistener.com`, HTTP 200), tr. 6 đối chiếu ảnh trang → **nhịp 13 giữ**. Câu gốc là "defendant was not…" (N12 chép "[Horwitz] was not…"); lời trích phần "…was not a successful businessman or Hollywood insider. He just played one in real life." |
| N9 docket hình sự | HTML **403** (CloudFront), REST API **401** (cần khoá) → chưa mở được; không dùng mục docket nào |
| N15 ân xá | 3 trang DOJ mở lại, 0 kết quả "Horwitz" (trang Trump cập nhật 20/10/2026) |

## 3. Bước 2 — Lời

- **102 câu · 2.049 từ · ≈ 15–16 phút** (13,7–14,6 phút lời ở 150–140 từ/phút + nghỉ/chữ trích/nhạc). **12.511 ký tự gửi TTS/lượt.**
- Tầng: ● 5 · ●T 30 · ◐ 29 · TT 6 · NB 2 · KBCB 6 · MH 2 · CHUNG 22.
- Theo lệnh: **"Beverlywood" bỏ** (máy chặn ở K6; crop N22 tr. 6 bỏ dòng 10 có tên khu); **nhịp 13 giữ** (đọc được Dkt. 58); **cả 6 đoạn có tên HBO/Netflix đều có câu không liên quan** "HBO and Netflix were not accused of any wrongdoing; according to the SEC, neither company ever did business with one-in-M-M." (máy kiểm K4); trích nguyên văn đối chiếu ảnh trang.
- Kết dấu hiệu: 5 dấu hiệu gắn chi tiết vụ + 1 nguyên tắc chung + nguồn chính thức (SEC tip, BrokerCheck, IAPD, ReportFraud). Bài học L1 (đổi lợi nhuận kỳ ngắn ra năm: 1,35² ≈ 1,82), L2 (Ponzi sống nhờ "thành tích" + ru ngủ), L3 (biết mình ký với ai).
- Thêm so với dàn truyện: nhịp **7c** (SEC cáo buộc "đồng đầu tư" giả, ¶52–56, ◐) + câu bài học "claim ≠ proof"; câu nhắc rằng tội trộm danh tính **đã bị bác** (S071, S086).
- **Không nói** (vì nguồn chưa mở): "without admitting or denying"; phán quyết với 1inMM Capital; số tiền thu hồi; kháng cáo.

## 4. Bước 3 — Kiểm lời độc lập

| Vòng | Phạm vi | K | MH | S | KKĐ | Sửa |
|---|---|---|---|---|---|---|
| 1 | S001–S102 | 99 | 1 (S038 "at all" → nguồn nói "direct") | 1 (S004 thiếu nguồn cho chữ "actor") | 0 | S038 thêm "direct"; S004 thêm N3/N2 |
| 2 | 4 câu đã sửa | 3 | 0 | 1 (S024 gán cho SEC khoảng 25–45 %; SEC ghi 35–45 %) | 0 | viết lại S024 |
| 3 | S024 | 1 về nội dung | — | — | — | thiếu chữ "alleged" (§3) → viết lại |
| 4 | S024 | 1 | 0 | 0 | 0 | — |
| **Cuối** | **102 câu** | **102** | **0** | **0** | **0** | tầng đúng 102/102; "làm theo được ngay?" Không ở mọi câu |

Ghi chú trung thực: vòng 3 tác tử ghi "Có" ở cột "làm theo được ngay?" mà ghi chú không nêu thao tác nào; vòng 4 hỏi lại đúng nghĩa và trả lời "Không".

## 5. Bước 4 — Bảng shot (`SHOT.md`)
44 hàng: sơ đồ tự vẽ, ảnh trang hồ sơ thật (crop, có danh sách trang **cấm** dùng: N8 tr. 1 và 3, N1 bảng ¶25, N7 tr. 12 dòng 23–28, N22 tr. 1), thẻ chữ trích, **16 khe Veo** (V01–V16) mỗi khe ghi luật V2/V3/V4/V6. Không mặt, không giọng người thật; không logo, không giao diện, **không tài liệu/tin nhắn/email dựng lại** — giấy/màn hình trong cảnh đều trắng hoặc mờ, chữ thêm ở hậu kỳ; không dựng cảnh bắt giữ. Mọi cảnh dựng có nhãn ILLUSTRATIVE.

## 6. Bước 5 — Ước chi và trần (`UOC-CHI.md`; đơn giá QUY-TRINH §6 của lost-places-lab, **chưa đo trên MR**)

| | Thấp | Giữa | Cao |
|---|---|---|---|
| OpenRouter (Veo, M-c + M-e) | 5,28 USD | 8,48 USD | 14,80 USD |
| ElevenLabs (ký tự tính, hệ số 0,44) | ≈ 9.590 | ≈ 11.950 | ≈ 17.900 |
| ElevenLabs nếu hệ số = 1,0 | ≈ 18.640 | ≈ 22.960 | ≈ 34.370 |

**Đề xuất trần cứng:** M-c `openrouter_usd` **9,50**, `elevenlabs_chars` **16.000** (gửi ≤ 24.000), khác 0 · M-d **0** · M-e `openrouter_usd` **1,60**, `elevenlabs_chars` **3.000** → cả tập **11,10 USD + 19.000 ký tự**.
**Số dư OpenRouter cần (V7, quỹ chung):** ≥ 10,3 USD khả dụng cho MR ở mức giữa (hiện 5,45 USD → **nạp tối thiểu ≈ 5 USD; khuyến nghị lên ≥ 15 USD**), cộng thêm phần các phiên lost-places-lab chạy song song nếu có. ElevenLabs (156.855 ký tự) đủ mọi mức.

## 7. Bước 6–7 — Gu (`PHUONG-AN.md`)
- Tiêu đề: **T1 "How an Actor Raised $650 Million on Fake Film Deals" (51)** · T2 "The Film Deals Were Fake. The $650 Million Was Real." (52) · T3 "25% in Six Months: Red Flags in a $650M Film Scheme" (51). Không tên HBO/Netflix, không "Ponzi", không nhãn.
- Thumbnail: TN1 dải phim rỗng + dấu "FAKE" + "$650M"; TN2 sơ đồ tháp ly "25–45% IN 6 MONTHS?". Đồ hoạ tự vẽ, 0 USD.
- Giọng: G1 nam trầm điềm tĩnh kiểu phóng sự (~140 từ/phút, đề xuất) · G2 nữ trung, kiểu explainer (~150 từ/phút). Giọng tổng hợp, không nhái người thật; chưa sinh mẫu.
- Bảng màu: B1 "Hồ sơ" (giấy ngà, IBM Plex Serif/Inter/Plex Mono, đề xuất) · B2 "Đêm" (xanh đêm, Archivo Black/Source Sans 3/JetBrains Mono).

## 8. Preflight và commit
`bash tools/preflight.sh` chạy riêng (không pipe) trước commit → ĐẠT, mã thoát 0; `--range origin/main..HEAD` trước khi đẩy → ĐẠT. Không `--no-verify`.

## 9. Cần chủ dự án quyết ở G1
1. (a) Đề tài + bảng tầng (giữ như `docs/ung-vien/1inmm-horwitz/TANG.md`, trạng thái kiểm lại §4 NGUON); (b) lời 102 câu `LOI.md`; (c) trần M-c/M-d/M-e ở §6.
2. Nạp OpenRouter (≥ 5 USD, khuyến nghị lên ≥ 15 USD) và xác nhận không có phiên Veo song song bên lost-places-lab lúc chạy M-c.
3. Chọn tiêu đề (T1/T2/T3), thumbnail (TN1/TN2), giọng (G1/G2), bảng màu (B1/B2).
4. Việc còn mở trước ngày đăng: kiểm lại docket/kháng cáo (N9 bị chặn ở MR-3 — cần đường khác hoặc PACER có trần), danh sách giảm án tập thể, đọc lại trang khai AI của YouTube.

**DỪNG — chờ rà.**
