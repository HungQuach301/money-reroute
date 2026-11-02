# BÁO CÁO MR-P3 — Thử nghiệm toàn diện độ sinh động (~2 phút tập 1, ba mức M1/M2/M3)

> Phiên Claude Code · 02/11/2026 · nhánh `ccr-61933171-f4wlwf` (từ `main` @ `33ce227`). Lệnh `[MR · MR-P3]`. Giờ trong báo cáo là **UTC** (Hà Nội = UTC + 7).
> Trần: `openrouter_usd` 5,00 · `elevenlabs_chars` 3.000 ký tự tính · khác 0 · mốc báo 80 %. **Chi thật: OpenRouter 2,94 USD (59 %), ElevenLabs 759 ký tự (25 %)** — khớp khoá MR và số dư tài khoản. Không 402. Lời, giọng, L2, L3, nhãn, thẻ **không đổi**. **DỪNG — chờ rà.**

## 0. Tóm tắt cho chủ dự án
| Hạng mục | Kết quả |
|---|---|
| Bản xem 540p (116,05 s mỗi bản) | `reports/mrp3/xem/goc.mp4` · `M1.mp4` · `M2.mp4` · `M3.mp4` · **ghép 2×2 `ghep_2x2.mp4`** (âm của M2) · đối chứng đo `P1.mp4`, `P2.mp4` · tờ 1 s `to1s_{goc,M1,M2,M3}.jpg` · nghe so tiếng động `so_sanh_tieng_dong.mp4` · so 720p/1080p `so_720_1080.jpg` |
| Đoạn thử | P00–P01 trọn (0–71,93 s bản đăng, có nhân vật đại diện) + P15 S067–S068 "lull" (492,88–510,48) + P16 S073 hạn 9/4 (543,60–552,52) + P17 S078–S080 nộp đơn → phong toả → bắt (589,92–607,52). Bỏ S069–S072, S074–S077, S081 để vừa ~2 phút (§9.1) |
| % thời lượng tranh có chuyển động thật (vượt đối chứng phẳng) | **goc ≈ 20 %** (theo dựng: chỉ K2, K3) · **M1 54 %** · **M2 58 %** · **M3 61 %** (§5) |
| Độ phủ clip theo dựng (trên 78 s tranh) | M1 27 % (4 clip: 2 mới + K2, K3) · M2 42 % (8 clip) · M3 63 % (15 clip) |
| Chi đoạn thử theo mức | M1 **0,40 USD** · M2 **1,20 USD + 660 ký tự** · M3 **2,20 USD + 660 ký tự** · thử riêng (nhân vật, 720p so sánh, tiếng động EL) 0,74 USD + 99 ký tự |
| Lượt clip | **16/17 đạt lượt 1**, 0 lượt 2; 1 bị lọc (Cb: khung cuối có người, 0 USD) |
| Nhân vật chuyển động (mục 5) | **(c) hoạt hoạ bằng mã thắng** (nhất quán tuyệt đối ref_nv, 0 USD); (d) Kling giữ đúng nhân vật nhưng diễn quá lời, 0,42 USD/3 s; (a) Veo chữ→video ra người khác; (b) bị lọc |
| 720p phóng lên vs 1080p | Trên tranh vẽ: **720p phóng lên không thua mắt thường**, giữ nét cọ sát tranh gốc hơn; 1080p thêm hạt lốm đốm + đốm trắng, vẽ lại tiền cảnh (§7) — rẻ hơn 40 % |
| Khuyến nghị | **M2 làm khuôn tập 2+** với clip **720p**, nhân vật bằng cách (c), nhạc theo hồi; M3 chỉ cho 1–2 đoạn cao trào. Luật đề xuất: `reports/mrp3/PHONG-CACH-HINH-v2-DE-XUAT.md` |

## 1. Bước 0 + mục 1 — trần, số dư, danh mục video
- `scripts/cp/budget.py`: thêm `"mrp3": {"openrouter_usd": 5.00, "elevenlabs_chars": 3000}` + mốc báo `{"openrouter_usd": 4.00, "elevenlabs_chars": 2400}`.
- Số dư **trước** (16:37:24): OpenRouter credits 155 / usage 142,96616 → **còn 12,03 USD**; khoá MR 19,3113955. ElevenLabs đã dùng 26.068 / 157.382. Trần 5,00 ≤ số dư − 20 % (9,63) → đạt BAI-HOC #6.
- Số dư **sau** (17:35:22): usage 145,90616 → **còn 9,09 USD**; khoá MR 22,2513955 (**+2,94 = sổ phiên**); tài khoản +2,94 → **0 chi ngoài khoá MR** trong cửa sổ phiên. ElevenLabs 26.827 (**+759 = sổ phiên**).
- **Danh mục video** (GET `https://openrouter.ai/api/v1/videos/models`, 16:36 UTC, miễn phí) → `reports/mrp3/danh_muc_video.json`: **31 mô hình**. Tóm tắt các mô hình có khung đầu (giá danh mục, không tiếng):

| Mô hình | Độ phân giải | Độ dài (s) | Khung | Giá |
|---|---|---|---|---|
| google/veo-3.1-lite | 720p, 1080p | 4, 6, 8 | đầu + cuối | 0,03 / 0,05 USD/s |
| google/veo-3.1-fast | 720p, 1080p, 4K | 4, 6, 8 | đầu + cuối | 0,08 / 0,10 / 0,25 USD/s |
| google/veo-3.1 | 720p, 1080p, 4K | 4, 6, 8 | đầu + cuối | 0,20 / 0,40 (4K) USD/s |
| kwaivgi/kling-v3.0-std / -pro | 720p | 3–15 | đầu + cuối | 0,084 / 0,112 USD/s |
| kwaivgi/kling-video-o1 | 720p | 5, 10 | đầu + cuối | 0,112 USD/s |
| alibaba/wan-3.0 / -prime | 480p–1080p | 2–30 | đầu + cuối | 0,05–0,20 / 0,068–0,28 USD/s |
| alibaba/wan-2.7 · wan-2.6 | 720p, 1080p | 2–10 · 5, 10 | đầu(+cuối) · đầu | 0,10 · 0,10–0,15 USD/s |
| alibaba/happyhorse-1.0 / 1.1 | 720p, 1080p | 3–15 | đầu | 0,0988–0,1694 USD/s |
| bytedance/seedance-2.0 / -fast / -mini / 2.5 / 1-5-pro | 480p–1080p (4K) | 4–30 | đầu + cuối | theo token video (0,0000012–0,0000107 USD/token) |
| minimax/hailuo-3 / -3-max / -2.3 | 480p–2K | 5–15 · 6, 10 | đầu(+cuối) | 0,05–0,13 USD/s |
| x-ai/grok-imagine-video / -1.5 / -1.5-lite | 480p–1080p | 1–15 | đầu | 0,02–0,25 USD/s + phí ảnh vào |
| runway/gen-4.5 | 720p | 2–10 | đầu | 0,12 USD/s |
| black-forest-labs/flux-3-video | 720p–4K | 5–20 | đầu + cuối | 0,17–0,41 USD/s |
| tbc/mischief-1 · heygen-video-1 | 480p–720p · 480p–2K | 3, 5 · 5–15 | đầu | 0,005–0,01 · 0,02–0,10 USD/s |
(Không khung/khác: heygen/avatar-iv, flux-video-edit, flux-video-upscale, runway/aleph-2 — sửa/phóng video, không dùng cho việc này.)
- **Chọn 1 mô hình khác Veo để thử: `kwaivgi/kling-v3.0-std`** — lý do: việc Veo không làm được là **khung đầu có người** (bài học MR-6 K1/K3); Kling có khung đầu + cuối, 3 s tối thiểu (khớp cảnh ~2,5 s), giá danh mục thấp nhất trong nhóm "chuyển động nhân vật" tầm trung, có `negative_prompt`. **Giá thật lệch danh mục:** `usage.cost` = **0,42 USD cho 3 s 720p** (danh mục 0,084 × 3 = 0,252) — ghi để điều phối biết.

## 2. M1 — 2.5D + 1 lớp phủ/cảnh + ~1 clip/30 s + tiếng động + cắt khớp phách + chữ động
- **2.5D**: `scripts/mrp3/sau.py` gọi lại `scripts/mrp2/sau.py` (Depth Anything V2 Small, Apache-2.0, ONNX `onnx-community/depth-anything-v2-small` @ `4472b73`, sha256 `afb6a5c2…df10c` khớp MR-P2; trọng số không vào repo). 28 tranh, **7,6 s/tranh** (`reports/mrp3/lop_do.json`). Máy quay mặc định tự động (`cam_mac_dinh`): trượt 30 px (cảnh có người 22 px, theo đề xuất MR-P2 §7.8), phóng 1,06 → 1,11.
- **Lớp phủ**: đúng 1/cảnh, từ nguồn có trong tranh (`HIEU` trong `scripts/mrp3/dung_p3.py`): hơi trà/cốc ×4, màn hình điện thoại sáng ×3, mưa trượt trên kính ×2 (mới), bụi trong tia sáng ×6, đèn chập chờn ≤ ±5,5 % < 3 Hz ×6, sương trôi ×2 (mới), cát chảy, vệt sáng quét ×2, rung khi khoá ×2. Không thêm người/chữ/vật.
- **Clip Veo 4 s** (≈ 1/30 s): V01 a03 (mưa trên kính bếp trống, S002) + V02 b040 (hồ đêm, sương, S067 "lull") + **K2, K3 của bản đăng** → 4 clip / 116 s.
- **Cắt khớp phách**: phách tìm từ nhạc của chính bản (thông lượng phổ → tự tương quan 70–160 BPM theo cửa sổ 12 s → pha); chỉ dời ranh **giữa hai cảnh tranh/clip kề nhau** tới phách gần nhất trong ±0,30 s (mỗi cảnh ≥ 1 s); ranh có L2/L3 giữ nguyên vì gắn giọng. M1: 147 phách, **12 điểm cắt dời** (−0,20 … +0,19 s) — đều ở P00–P01 phần có N1; 40–72 s không nhạc (như bản đăng) nên không dời. Ghi ở `dung_M1.json`.
- **Chữ động câu trích**: hai câu nguyên văn đã duyệt trong `loi.json` "chu" — S067 “to lull the investors into believing their funds were safely invested” (N7 tr. 11, ●T) và S073 “a release of funds by April 9th (at the latest)” (N1 ¶76, ◐). Từng từ hiện đúng mốc whisper của giọng, nhấn đỏ cam "lull"/"April", vạch trái màu theo tầng (đỏ cam ● / hổ phách ◐), dòng nguồn + nhãn tầng giữ nguyên lớp tĩnh của bản đăng. Đã kiểm lại nguyên văn trong PDF (`pdftotext`): khớp.
- **Tiếng động CC0** (§6): 13 tệp BigSoundBank, đặt theo mốc từ whisper (vd tiếng búa ở "sentenced", khoá ở "freeze", va chạm ở "arrested").
- Âm: giọng đã duyệt đặt theo `moc_cau.json` + nhạc bản đăng cắt đoạn + tiếng động; loudnorm hai lượt → **−14,0 LUFS, đỉnh −1,5 dBFS** (cả M1, M2, M3; goc −14,1 LUFS là âm bản đăng cắt ra).

## 3. M2 — M1 + clip phủ ~1/3 + nhân vật chuyển động + nhạc theo hồi
- Thêm 4 clip 1080p: V03 b066 (kho hồ sơ, tia sáng), V04 a15 (rạp trống, chùm máy chiếu), V05 b051 (phòng xử, tia nắng), V06 b052 (**cửa két đóng** đúng câu S079 "asset freeze"). Phủ **42 %** thời lượng tranh (32,7 / 78,0 s, gồm K2, K3).
- **Nhân vật**: cách (c) cho a01 (S001, 3 s) và a04 (S002, 1,6 s) — chớp mắt, nghiêng đầu ≤ 1,4°, thở ≤ 2 px; máy phẳng nhẹ (§5 của tờ đề xuất).
- **Nhạc theo hồi** (`nhac_hoi()` trong `dung_p3.py`):
  - P00–P01: N1 (móc) → **dừng cứng + va chạm ElevenLabs ở chữ "real"** (cú lật S003 "the case behind it is real") → N2 lớp đầu vào sau 0,8 s, mức −23 → −18 dB dưới P01.
  - P15–P17: **Eleven Music `m_p15_17`** 48 s, 4 hồi theo kế hoạch bố cục: Lull 17,5 s (piano dạ) khớp S067–S068 · Countdown 9 s (nhịp tích tắc) khớp S073 · Closing in 13 s (dây trầm dồn) khớp S078–S079 · **cắt cứng đúng đầu S080** "FBI agents arrested" + va chạm → lặng 1,2 s → đuôi Aftermath rất nhỏ. 660 ký tự.
  - Cắt khớp phách theo nhạc mới: 169 phách, 13 điểm cắt dời.
- **Sửa trong phiên:** bản dựng M2 đầu có **1,5 s lặng tuyệt đối** (18–19,5 s) vì N1 dừng ở đầu S003; đã sửa (N1 chạy tới chữ "real", N2 vào sau 0,8 s) và dựng lại M2, P2, M3. Còn ~1 s rất nhỏ (−60 dB) giữa câu cuối P00 và đầu P01 — là khoảng thở có chủ ý; chủ dự án nghe quyết.

## 4. M3 — clip phủ ~2/3, trộn 1080p và 720p phóng lên
- Thêm 7 clip: 1080p V09 b116 (thành phố, mây trôi), V12 b141 (đèn bàn, điện thoại úp); **720p** V07 b001 (bóng đèn gương), V08 a09 (kho phim), V10 b003 (hành lang), V11 a12 (toà án, mây), V13 b070 (dải phim). 720p phóng lên 1920×1080 bằng Lanczos trong bộ dựng.
- Phủ **63 %** (49,1 / 78,0 s). 15 clip trên 116 s.
- Thời gian dựng **giảm** (223 s so với 371 s của M2) vì ít cảnh phải tính 2.5D.

## 5. Bảng đo
**Thước đo** (`scripts/mrp3/do_chuyen_dong.py`, bản 3 của MR-P2): luồng DIS t − 0,4 s → t, khớp một homography, phần dư p90; khung "có chuyển động thật" khi vượt khung cùng thời điểm của **đối chứng phẳng cùng dòng thời gian** (P1 cho M1; P2 cho M2, M3 — vì điểm cắt khớp phách khác nhau) quá 0,25 px. Đo 52 s tranh (ngoài cửa sổ hoà cảnh).

| | goc | M1 | M2 | M3 |
|---|---|---|---|---|
| % thời lượng tranh có chuyển động thật | **≈ 20 %** (theo dựng: K2 + K3 = 15,8 / 78 s) | **54,1 %** | **58,3 %** | **61,0 %** |
| Cả đoạn (gồm L2/L3) | — | 35,8 % | 39,7 % | 41,7 % |
| Độ phủ clip theo dựng (tranh) | 20 % | 27 % | 42 % | 63 % |
| Clip trong 116 s (mới + cũ) | 0 + 2 | 2 + 2 | 6 + 2 | 13 + 2 |
| Nhân vật chuyển động | 0 | 0 | 4,8 s (a01, a04) | 4,8 s |
| Tiếng động | 0 | 17 điểm CC0 | 13 CC0 + 4 EL | như M2 |
| Nhạc | bản đăng | bản đăng | theo hồi (N1/N2 + Eleven Music) | như M2 |
| **Chi đoạn thử** | 0 | **0,40 USD** | **1,20 USD + 660 ký tự** | **2,20 USD + 660 ký tự** |
| Thời gian dựng 1080p (4 tiến trình, 4 CPU) | 61 s (cắt) | 326 s | 371 s | 223 s |
| Lượt clip đạt lượt 1 | — | 2/2 | 6/6 | 13/13 |

**Đọc kèm (quan trọng):** thước đo **đếm thấp chuyển động nhỏ trong khung**: mưa trượt trên kính (a03 V01: 4,8 %), chập chờn đèn (đổi độ sáng, không phải dịch chuyển — b001 V07: 0 %), chớp mắt/nghiêng đầu nhân vật (a01 8,8 %, a04 14,3 %), hồ sương (b040 34 %). Vì vậy bước nhảy M1 → M3 trên thước đo (54 → 61 %) **nhỏ hơn nhiều** so với độ phủ clip (27 → 63 %); cảm giác "sống" phải chấm bằng mắt trên `ghep_2x2.mp4`. Một số cảnh 2.5D của M1 có số đo **cao hơn** chính cảnh đó khi thay bằng clip Veo nhẹ (b001 36 % → 0 %, a15 19 % → 9 %): Veo "nhẹ" chủ yếu đổi ánh sáng. Theo tranh: `reports/mrp3/do_chuyen_dong.json`.
**Phiên chỉ xem được khung/tờ, chưa xem phát liên tục và chưa nghe được âm** — đánh giá nhịp/âm cần chủ dự án.

## 6. Âm thanh — CC0 vs ElevenLabs
**CC0:** chỉ nhận tệp mà **trang của chính tệp** ghi "License CC0 (public domain)" (`scripts/mrp3/cc0.py` kiểm chuỗi này rồi mới tải). **13/13 tệp BigSoundBank đạt**, mỗi tệp có URL trang, URL tệp, tiêu đề, dòng giấy phép, sha256, giờ tải trong `reports/mrp3/am/cc0.json` (rung điện thoại, báo tin, tủ lạnh, đêm sau mưa, lật trang, búa toà, đồng hồ, nhịp tim, vút, khoá, nổ xa, phố đêm, gõ phím). Trang giấy phép chung ghi tiêu đề "Royalty-Free Sound License (CC0-like)" nhưng thân trang ghi "Creative Commons CC0 1.0 Universal" và tệp không đăng ký Content ID — **điều phối xem có chấp nhận nguồn này không**. Tệp CC0 dựng lại được 0 USD → không đẩy repo.
Nguồn khác **chưa mở được, không vượt**: kenney.nl HTTP 403; Wikimedia Commons API HTTP 429 (cả với UA mô tả, không email); Freesound API 403 (cần khoá). Không dùng nguồn giấy phép khác/không rõ.

**ElevenLabs Sound Effects** (đo thật, chênh `character_count`): rung điện thoại 2 s = **22**, va chạm điện ảnh 3 s = **33**, đồng hồ 4 s = **44** ký tự → **≈ 11 ký tự/giây**. Số dư cập nhật trễ ~25 s (lượt đầu đọc ra 0 → đã ghi dòng điều chỉnh +22 trong sổ, sửa `eleven.py` chờ tới khi số dư đổi). **Eleven Music**: 48 s = **660 ký tự** (= 825 ký tự/phút, khớp BAI-HOC).
**So sánh** (nghe: `reports/mrp3/xem/so_sanh_tieng_dong.mp4`, từng cặp CC0 → EL): CC0 đủ cho tiếng đời thường (rung, báo tin, búa, khoá, lật trang, nền phòng/phố); **thiếu tiếng "điện ảnh"** (va chạm trầm, riser) — CC0 chỉ có tiếng nổ thật, phải lọc thấp. EL làm đúng vai va chạm/nhạc cụ, giá rất thấp (~0,4 ký tự/khung hình). Đề xuất: CC0 mặc định, EL cho 3–6 tiếng "nhấn" mỗi tập (≈ 150–300 ký tự).

## 7. 720p phóng lên vs 1080p (cùng lời, cùng khung đầu b040: V02 vs V02b)
`scripts/mrp3/so_720_1080.py` → `reports/mrp3/so_720_1080.json`, tờ 1:1 `reports/mrp3/xem/so_720_1080.jpg` (tranh gốc | 1080p | 720p→1080 Lanczos, 3 vùng × 3 thời điểm).
- **Mắt:** 720p phóng lên **giữ nét cọ và mảng mờ giống tranh gốc**; 1080p có **hạt lốm đốm kiểu nén/dither trên mảng phẳng (sương, trời) và vài đốm trắng**, và ở vùng bờ hồ **vẽ lại cây lau khác tranh gốc** (lệch nội dung). Ở 540p/1080p xem bình thường không thấy 720p mềm hơn.
- **Số:** phương sai Laplace toàn khung: tranh gốc 27 · 1080p 227–313 · 720p→1080 11–12 → chỉ số này **đo hạt nhiễu chứ không đo chi tiết** trên tranh vẽ — không dùng làm tiêu chí.
- **Kết luận:** trên tranh vẽ phong cách kênh, **720p phóng lên đạt**, rẻ hơn 40 % (0,12 so với 0,20 USD/4 s). Giới hạn: 1 cặp so sánh; nên kiểm thêm 1 cặp có cạnh sắc (kiến trúc, chữ cấm vẫn cấm).

## 8. Mục 5 — Nhân vật đại diện chuyển động (nhân vật tự nghĩ ra, người lớn)
| Cách | Lượt / chi | Lọc? | QC: không giống người thật · nhất quán `ref_nv` (a01) · không chữ | Kết luận |
|---|---|---|---|---|
| (a) Veo chữ→video, không khung, `personGeneration: allow_adult` | 1 · 0,20 USD | Không | Ra **người khác**: tóc bạc trắng, gọng kính khác, cửa sổ núi; nét **gần ảnh chụp** hơn tranh → lệch phong cách, tăng rủi ro "giống người thật"; không chữ | **Không đạt** (nhất quán) |
| (b) Veo khung đầu a03 (bếp trống) + khung cuối a01 (có nhân vật) | 1 · 0 USD | **Bị lọc**: "input image violates Vertex AI's usage guidelines" | — | **Không dùng được** (Veo chặn ảnh có người kể cả ở khung cuối) |
| (c) Hoạt hoạ cắt ghép 2D bằng mã (`nv_khung` trong `dung_p3.py`) | 0 USD | — | Đúng tranh gốc → nhất quán tuyệt đối; chớp mắt (nhắm–mở 0,16 s), nghiêng đầu ≤ 1,4° quanh cổ, thở ≤ 2 px; tờ cận 1:1 không méo mặt/kính | **Đạt — chọn cho M2/M3**. Giới hạn: biên độ nhỏ (thước đo chỉ thấy 9–14 %); cần đo toạ độ mắt/cổ mỗi tranh (~2 phút công/tranh) |
| (d) Kling v3.0 Std, khung đầu a01, 3 s 720p | 1 · **0,42 USD** | Không (nhận khung có người) | Giữ đúng nhân vật, kính, áo, nét tranh; nhưng **diễn quá lời**: "nụ cười tăng nhẹ" thành cười rộng lộ răng; không chữ | **Đạt có lưu ý** — dùng cho 1–3 khoảnh khắc cảm xúc/tập, lời ghi biên độ biểu cảm rất nhỏ; đắt gấp ~3,5 lần Veo Lite 720p |
Không ảnh/chân dung người thật nào được gửi; người thật (vest tối) vẫn chỉ bóng/lưng, không đưa vào bất kỳ lượt sinh nào.

## 9. Lệch so với lệnh / việc chưa đạt (nói rõ)
1. **Đoạn thử 116,05 s** (lệnh ~120 s): P00–P01 trọn, nhưng P15–P17 **không trọn** (P15–P17 dài 125 s): giữ S067–S068, S073, S078–S080; bỏ S069–S072 (thư giả, danh tính nhân viên HBO/Netflix + thẻ KBCB), S074–S077, S081. Không câu giữ lại nào nêu tên HBO/Netflix mà thiếu thẻ KBCB (S006 ↔ thẻ S008 vẫn đủ).
2. **Thước đo đếm thấp chuyển động nhỏ** (mưa, chập chờn, chớp mắt) — khoảng cách M1/M2/M3 trên thước đo nhỏ hơn cảm nhận dự kiến; chưa có thước đo độ sáng cục bộ.
3. **Chưa nghe/xem phát liên tục**: đánh giá âm (cân bằng tiếng động, độ hợp của nhạc Eleven Music) và nhịp cắt khớp phách là theo số đo + tờ khung. Chủ dự án nghe `ghep_2x2.mp4` (âm M2), `M1.mp4`, `so_sanh_tieng_dong.mp4`.
4. **V06** (cửa két): bản lề/viền cửa biến dạng từ ~2,5 s; cảnh chỉ dùng 0–2,5 s → giữ, không lượt 2. **V10**: máy đẩy mạnh hơn lời, đèn trần sáng dần. **V12**: điện thoại có dịch nhẹ theo máy. Quét V8 (`reports/mrp3/veo/quet_v8.json`, cột 1–4): 3 cờ c1 "mưa vệt" ở V03, V05, V08 — mắt xem tờ `quet_v8-to/`: là **tia sáng/cột kệ thẳng đứng**, báo nhầm; 0 cờ c2–c4.
5. **Kling giá thật 0,42 USD/3 s** lệch danh mục (0,252) — dự phóng dùng giá thật.
6. Bộ dựng M2 đầu có lặng tuyệt đối 1,5 s → đã sửa, dựng lại (§3). Lệnh cắt goc đầu tiên hết bộ nhớ (trim nhiều đoạn trên một đầu vào) → đổi sang tua đầu vào từng đoạn.
7. Không làm khớp hình giữa các cảnh như MR-P2 (`KHOP` rỗng) — ưu tiên thời gian cho mục 5–7.
8. Lệnh `pkill -f` một lần tự dừng chính lệnh của phiên (lặp lại bài học MR-P2 §8.7) — không mất tệp; đã chạy lại bằng tiến trình nền.

## 10. Dự phóng chi / tập (~15 phút, khuôn tập 1: ~520 s tranh, 166–190 tranh)
Giá thật phiên này: Veo Lite 4 s **0,20 (1080p) / 0,12 (720p)**; **16/17 lượt 1 đạt** (cảnh không người); mỗi clip dùng TB **2,6–2,8 s** trong đoạn thử. Khuôn hiện tại (PHONG-CACH v1): tranh ≈ 7,8 USD + 4–5 clip ≈ 2,0–3,0 USD ≈ **9–11 USD** + ~9.000–10.000 ký tự.

| | Clip/tập | Clip thêm (USD) 1080p · **720p** | ElevenLabs thêm | Máy (CPU 4 nhân) | Ước tổng OpenRouter/tập |
|---|---|---|---|---|---|
| M1 | ≈ 29 (1/30 s) | +2,8–3,8 · **+0,5–1,5** (so với 4–5 clip đang ước 2,0–3,0) | CC0 0 + EL nhấn ≈ 200 ký tự | độ sâu ≈ 21 phút + dựng ≈ 41 phút | **≈ 11–14** |
| M2 | ≈ 62 (1/3 tranh) | +9,4–10,4 · **+4,4–5,4** | nhạc theo hồi: sửa nhạc đã có 0 · hoặc Eleven Music cả tập ≈ +9.000 ký tự | ≈ 21 + 46 phút; sinh clip ≈ 1,6 phút/clip (≤ 3 song song ≈ 35 phút) | **≈ 15–20** (720p ≈ 15) |
| M3 | ≈ 133 (2/3 tranh) | +23,6–24,6 · **+13,0–14,0** (trộn 50/50 ≈ +18–19) | như M2 | ≈ 21 + 28 phút; sinh ≈ 75 phút (3 song song) | **≈ 24–35** |
Nhân vật (c): 0 USD, ~2 phút công/tranh có nhân vật. Kling cho 1–3 khoảnh khắc: +0,4–1,3 USD.

## 11. Đề xuất PHONG-CACH-HINH v2 (chuyển động, âm thanh, nhịp)
Toàn văn: **`reports/mrp3/PHONG-CACH-HINH-v2-DE-XUAT.md`** (không sửa `docs/` — chờ điều phối/chủ dự án duyệt). Tóm tắt: mặc định **M2-720p** (2.5D + 1 lớp phủ mọi tranh; clip Veo Lite **720p** 4 s phủ ~1/3 thời lượng tranh, khung đầu không người không chữ; nhân vật đại diện bằng hoạt hoạ mã); **âm**: tiếng động CC0 (trang tệp ghi CC0) + EL cho tiếng nhấn, nhạc chia theo hồi, cắt cứng + va chạm ở cú lật; **nhịp**: điểm cắt tranh→tranh khớp phách ±0,3 s, chữ động cho câu trích nguyên văn.

## 12. Cần chủ dự án / điều phối
1. Xem `reports/mrp3/xem/ghep_2x2.mp4` (+ từng bản có âm riêng) — chọn mức (khuyến nghị **M2 với clip 720p**).
2. Nghe `so_sanh_tieng_dong.mp4` và nhạc theo hồi trong `M2.mp4` (83–116 s) — duyệt hướng âm.
3. Quyết nguồn CC0 BigSoundBank (§6) và có cho dùng Kling cho khoảnh khắc nhân vật (§8, giá thật 0,42 USD/3 s) không.
4. Duyệt/sửa `PHONG-CACH-HINH-v2-DE-XUAT.md` → đưa vào `docs/PHONG-CACH-HINH.md` v2 + cập nhật trần tập 2 theo §10.
