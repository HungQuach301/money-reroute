# BÁO CÁO MR-P2 — Thử giảm cảm giác ảnh tĩnh (~60 s tập 1, ba biến thể)

> Phiên Claude Code · 02/11/2026 · nhánh `claude/brave-faraday-vtsny1` (từ `main` @ `19d3a7a`). Lệnh `[MR · MR-P2]`. Giờ trong báo cáo là **UTC** (Hà Nội = UTC + 7).
> Trần: `openrouter_usd` 1,50 · khác 0 · mốc báo 1,20. **Chi thật 1,00 USD** (khớp khoá MR). Không 402. Lời, giọng, nhạc, L2, L3 **không đổi**. **DỪNG — chờ rà.**

## 0. Tóm tắt cho chủ dự án
| Hạng mục | Kết quả |
|---|---|
| Bản xem cạnh nhau (540p, 59,97 s) | `reports/mrp2/xem/goc.mp4` · `A.mp4` · `B.mp4` · `C.mp4` (+ đối chứng đo `P.mp4`) · tờ 1 s `xem/to1s_{goc,A,B,C}.jpg` · tờ QC mép `xem/qc_mep.jpg` |
| Đoạn thử | P05 S025–S029 (169,28–209,56 s bản đăng: "Over the life of the note…" → phép tính 35 % → 82 % → "where would that much profit come from") + P08 S040–S042 (281,28–300,96 s: "On paper, each note had collateral…" → "did not acquire the distribution rights"). 12 tranh L1, 2 đồ hoạ L2 (G05, G08). Hai khúc nối cứng, âm tắt/mở 0,15 s |
| A — 2.5D | Depth Anything V2 Small (ONNX, CPU) tải được; 3 lớp/tranh, vá nền sau lớp trước, mỗi lớp cong theo độ sâu từng điểm ảnh → thị sai. 0 USD |
| B — A + lớp động | Đúng 1 hiệu ứng/cảnh (cát chảy, bụi trong tia sáng ×3, đèn chập chờn ×2, hơi nước, đèn quét, lấy nét chuyển ×2, rung khi ấn dấu, ổ khoá lắc) + 3 chuyển cảnh khớp hình + rung tay ≤ 1,5 px. 0 USD |
| C — B + Veo | 5 clip ảnh→video **4 s** (Veo 3.1 Lite nhận 4 s — danh mục ghi `supported_durations [8, 4, 6]`, **0,20 USD/clip**); **5/5 đạt lượt 1**, 0 lượt 2. 1,00 USD |
| Đo chuyển động thật (L1, ngoài hoà cảnh) | **gốc 0 %** (theo dựng) · **A 51 %** · **B 58 %** · **C 62 %** thời lượng; sàn nhiễu ≈ 8 % (§4) |
| Thời gian dựng 60 s (1080p, 4 tiến trình) | gốc (cắt) 96 s · A 214 s · B 271 s · C 188 s; + độ sâu/tách lớp ≈ 7,6 s/tranh |
| Khuyến nghị | **B làm mặc định cho mọi cảnh L1 + Veo 4 s cho 5–8 khoảnh khắc lớn/tập** (C nhẹ). Luật đề xuất §7 |

## 1. Bước 0 — trần, số dư, giá
- `scripts/cp/budget.py`: thêm `"mrp2": {"openrouter_usd": 1.50}` và mốc báo `"mrp2": {"openrouter_usd": 1.20}`.
- **GET danh mục** `https://openrouter.ai/api/v1/videos/models` (14:57 UTC, miễn phí) → `reports/mrp2/gia_veo.json`: `google/veo-3.1-lite` — `supported_durations: [8, 4, 6]`, `supported_frame_images: [first_frame, last_frame]`, 1080p không tiếng `duration_seconds_without_audio` **0,05 USD/s** → 4 s = **0,20 USD**; 720p 0,03 USD/s (4 s = 0,12). Lượt thật: `usage.cost` = 0,20 mỗi clip — khớp.
- Số dư **trước** (14:57:53): credits 155 / usage 135,76616 → **còn 19,23 USD**; khoá MR 18,3113955. **Sau** (15:29:44): usage 142,96616 → **còn 12,03 USD**; khoá MR 19,3113955.
- **Đối soát:** khoá +1,00 = sổ phiên (`calls.jsonl`, 5 dòng). Tài khoản +7,20 → **6,20 USD chi ngoài khoá MR** trong cửa sổ phiên (14:57–15:29), cột `chi_phien_khac` từng lượt Veo 0,6 / 0,7 / 0 / 0,2 / 0,9 — kênh dùng chung tài khoản (theo xác nhận G2 tập 1 là lost-places). Ghi để chủ dự án đối chiếu.
- Sổ: `COST-LEDGER.csv` (3 dòng MR-P2), `reports/mrp2/veo_luot.jsonl`.

## 2. Biến thể A — 2.5D (0 USD)
**Mô hình:** Depth Anything V2 Small, bản ONNX công khai `onnx-community/depth-anything-v2-small` @ `4472b7362082ad9968fee890ca0f1e5aca36b93d` (`onnx/model.onnx`, 99 MB, sha256 `afb6a5c2…df10c`), giấy phép **Apache-2.0** (thẻ mô hình, cả bản gốc `depth-anything/Depth-Anything-V2-Small`). Tải được ngay → **không cần MiDaS**. Trọng số **không** đưa vào repo (chỉ ở scratch). Chạy `onnxruntime` CPU, đầu vào 518 × 924.
**Cách làm** (`scripts/mrp2/sau.py`, `scripts/mrp2/dung_thu.py`):
1. Ảnh vào = đúng khung bản đăng (`dung.tranh()` của MR-6: cắt khung MR-6 → phủ 1920×1080), nên b021 vẫn đã cắt bỏ bóng người.
2. Độ sâu → 3 lớp bằng k-means trên độ sâu (xa / giữa / gần), làm sạch mảnh < 0,4 % khung, mép mềm 2,5 px. b089: lớp gần = riêng ổ khoá, tách bằng GrabCut gieo hạt từ "độ sâu nổi hơn nền cục bộ" (`scripts/mrp2/lop.json`).
3. Vá nền sau lớp trước: Telea ở ½ độ phân giải + mờ + hạt (khớp nét cọ). Lớp xa vá chỗ giữa+gần; lớp giữa vá chỗ gần.
4. **Mỗi lớp cong theo độ sâu từng điểm ảnh** (không trượt cứng từng tấm): ngưỡng k-means cắt ngang mặt bàn/sàn liền, trượt cứng sẽ rách ở đường cắt; cong theo độ sâu làm hai bên đường cắt đi cùng nhau, chỉ mép vật thật (chênh sâu) mới lộ phần vá. Máy: trượt ngang/dọc 18–40 px ở độ sâu 1 + phóng 1,06–1,14 + "dolly" (vật gần nở nhanh hơn), hệ số thị sai 0,15 + 0,85·độ sâu.
**QC mắt mép lớp** (`scripts/mrp2/qc_mep.py` → `xem/qc_mep.jpg`: mỗi tranh, 2 điểm mép có chênh sâu lớn nhất, cắt 1:1 ở khung đầu và cuối cảnh):

| Vòng | Thấy | Sửa |
|---|---|---|
| 1 | **b077** dây cân nhân đôi, răng cưa ở khung cuối; **b080** vệt trắng kéo dãn cạnh lưng ghế; b009/b011/b021 quầng mảnh ở mép | Điểm mép mờ của lớp trước lấy độ sâu nền nên trôi khác vật → lớp trước dùng **độ sâu nở 31 px** (max-filter) để mép đi cùng vật; b077 giảm trượt 40 → 22 px |
| 2 | Hết răng cưa b077; còn **b077 một vệt dây mờ thứ hai** (dây mảnh không bị lớp vá che hết), **b080 vệt vá cạnh lưng ghế**, **b009 viền mảnh ở vành trên**; b081, b143, b079, b022, b091, b089 sạch | b080 giảm trượt 30 → 18 px. Ba lỗi còn lại chỉ thấy ở 1:1 khung cuối, cỡ 2–6 px ở 1080p; **chưa hết** — ghi ở §8 |

Cảnh có nhân vật đại diện (b010, b080, b091 tay áo vest): tóc/vai tách lớp gọn, không thấy rách mặt; vẫn giữ nhãn ILLUSTRATIVE như bản đăng.

## 3. Biến thể B — A + lớp chuyển động phủ (0 USD, mã)
Đúng **1 hiệu ứng/cảnh**, hợp nội dung, vẽ ở toạ độ tranh rồi đưa lên màn theo cùng máy quay/độ sâu (đi cùng thị sai):

| Tranh | Câu | Hiệu ứng |
|---|---|---|
| b009 đồng hồ cát | S025 | cát chảy qua cổ đồng hồ (hạt rơi 260 px/s) |
| b077 cân | S025 | bụi trong ánh đèn (độ sáng hạt theo độ sáng nền → chỉ thấy trong vùng sáng) |
| b081 domino | S027 | lấy nét chuyển: hàng xa → quân gần |
| b010 bếp đêm | S029 | đèn bàn chập chờn ≤ ±5,5 %, < 3 Hz (an toàn thị giác) |
| b080 bếp sáng | S029 | hơi nước bốc từ cốc |
| b011 nhà kho | S029 | bụi trôi trong cột sáng |
| b143 bàn đêm | S029 | vệt sáng quét qua bàn |
| b079 mầm cây | S029 | hạt sáng trong tia nắng |
| b021 két rỗng | S040 | đèn chập chờn |
| b022 hộp phim xích | S041 | lấy nét chuyển: kệ sau → hộp phim |
| b091 con dấu | S041 | rung khi con dấu ấn xuống (0,55 s) |
| b089 ổ khoá | S042 | ổ khoá lắc quanh móc, tắt dần (≤ 2,2°) |

Chuyển cảnh **khớp hình** (neo của cảnh sau đặt đúng chỗ neo cảnh trước trên màn khi hoà 0,5 s): đồng hồ cát → trụ cân; đầu nhân vật b010 → b080; hộp két → hộp phim. Rung tay ≤ 1,5 px, tần số thấp, mọi cảnh L1.
Không thêm chữ, vật, người. Thẻ chữ, nhãn tầng, dòng nguồn giữ nguyên bản đăng.

## 4. Biến thể C — B + 5 clip Veo ảnh→video 4 s (1,00 USD)
Khung đầu = tranh L1 đúng khung bản đăng (1920×1080), **không người, không chữ** (BAI-HOC #2). Lời: chuyển động nhẹ đúng nguồn + tiền tố phong cách tranh; negative chặn người/chữ/vật mới/nổ khói (`reports/mrp2/veo/loi_veo.json`). Chạy **tuần tự**, kiểm `/credits` ≥ 0,20 + 1 USD trước mỗi lượt, đẩy LFS ngay sau mỗi clip (`scripts/mrp2/chay_veo.sh`; V1 sinh xong 15:05:16 → đẩy 15:05:28 … V5 15:12:59 → 15:13:10).

| Khe | Tranh | Lượt | Kết quả (tờ 0,5 s mắt + `quet_v8.py` c1–c4) |
|---|---|---|---|
| V1 | b009 đồng hồ cát | 1 | Đạt. Máy tự đẩy/lia rõ hơn lời; cát chảy nhỏ |
| V2 | b011 nhà kho | 1 | Đạt. Bụi trong cột sáng, vải phủ đứng yên |
| V3 | b079 mầm cây | 1 | Đạt. Tia sáng mạnh dần (đổi độ sáng rõ), lá rung nhẹ |
| V4 | b022 hộp phim xích | 1 | Đạt. Ánh sáng "thở" khá mạnh ở 1–2 s; xích/khoá không đổi (cắt 1:1) |
| V5 | b089 ổ khoá | 1 | **Đạt có lưu ý:** ổ khoá lắc rộng hơn lời (~40°, ra khỏi mặt tường ở 1,0–1,5 s), không biến dạng, móc đứng yên. Không chi lượt 2 |

Quét V8 (`reports/mrp2/veo/quet_v8.json`, cột 1–4): **0 cờ**. Cột 5 (người) không chạy — khung không người. Mỗi clip dùng 2,3–2,8 s đầu (+ 0,5 s hoà), không dãn (V2). Chọn: `reports/mrp2/veo/chon.json`.

## 5. Bảng đo
**Thước đo** (`scripts/mrp2/do_chuyen_dong.py` → `reports/mrp2/do_chuyen_dong.json`): luồng quang DIS giữa khung t − 0,4 s và t (480 px) → khớp **một** homography (mọi trượt/phóng/lia của ảnh phẳng được giải thích hết) → phần dư từng điểm. Khung tính là "có chuyển động thật" khi phân vị 90 phần dư **vượt khung cùng thời điểm của đối chứng P quá 0,25 px**. P = cùng máy quay A trên tranh **phẳng** (= ảnh tĩnh trượt thuần) với cùng thẻ chữ/nhãn, nên thẻ chữ và nhiễu luồng bị trừ đi.
Hiệu chỉnh: thước đo v1 (luồng Farneback − affine) và v2 (homography + chênh độ sáng) **trượt hiệu chỉnh** — bản gốc chỉ có ảnh trượt vẫn ra 44–71 % vì thẻ chữ đứng yên trên ảnh trượt và nhiễu nội suy nét cọ. Bản 3 (so với P) dùng được; **sàn nhiễu ≈ 8 %** (đo trên L2, vốn giống hệt nhau giữa các bản).

| | gốc | A | B | C |
|---|---|---|---|---|
| L1: % thời lượng có chuyển động thật (20,7 s đo được, ngoài hoà cảnh) | **0 %** (theo dựng: SHOT2 đoạn này toàn tranh tĩnh trượt; P = 0 %) | **51 %** | **58 %** | **62 %** |
| Cả đoạn (gồm L2) | — | 29 % | 32 % | 30 % |
| Cảnh L1 dùng Veo / có hiệu ứng | 0 / 0 | 0 / 0 | 0 / 12 | 5 / 7 |
| Chi phí đoạn thử | 0 | 0 | 0 | **1,00 USD** (5 × 0,20) |
| Thời gian dựng 60 s ở 1080p (4 tiến trình, 4 CPU) | 96 s (cắt) | 214 s | 271 s | 188 s |
| Độ sâu + tách lớp + vá (một lần/tranh) | — | 91 s / 12 tranh (≈ 7,6 s/tranh) | như A | như A (7 tranh) |

Theo tranh (% vượt P): A thấp ở b081 (0 %, máy chậm), b080 (0 %, sau khi giảm biên độ vì QC mép), b089 (0 %); B kéo các cảnh đó lên nhờ hiệu ứng (b080 44 %, b089 73 %) — trừ b081 (lấy nét chuyển: thước đo không thấy độ mờ đổi). C: b011, b079, b089 ≈ 100 %; b009 49 % (Veo chủ yếu đẩy máy, cát chảy nhỏ). Chi tiết từng tranh trong JSON.
**Đọc kèm mắt:** thước đo chỉ đếm "có/không"; xem `goc.mp4` ↔ `B.mp4` ↔ `C.mp4` để chấm cảm giác — phiên chỉ xem được khung tĩnh/tờ, **chưa xem chạy liên tục**.

## 6. Dự phóng chi / tập (~15 phút, khuôn tập 1: ~166 tranh, 192 cảnh L1 ≈ 520 s)
| | OpenRouter thêm so với khuôn hiện tại | Máy (CPU 4 nhân) | Công phiên |
|---|---|---|---|
| A | **0 USD** | độ sâu ≈ 21 phút (166 × 7,6 s) + dựng ≈ 52 phút (214 s/60 s × 872 s) | cấu hình máy quay mỗi tranh (mặc định tự động + chỉnh tay tranh có vật mảnh) + QC mép 1:1 mỗi tranh |
| B | **0 USD** | ≈ 21 + 66 phút | như A + toạ độ hiệu ứng mỗi tranh (~1 dòng/tranh như `HIEU_UNG`) |
| C nhẹ (5–8 clip 4 s) | **1,00–2,30 USD** (0,20 × 5–8 × 1,00–1,44 lượt/khe) — **thay** 4–5 clip 8 s đang ước 2,0–3,0 USD → tiết kiệm ≈ 0,7–1,0 USD | như B | tờ 0,5 s + quét V8 mỗi clip |
| C dày (1 clip/phút ≈ 15) | 3,00–4,30 USD | như B | như trên |
Tham chiếu: ước tập sau theo BAI-HOC ≈ 9–11 USD OpenRouter. Lượt 1 đạt 5/5 ở MR-P2 (khung đầu không người) — hệ số 1,44 của MR-4/5 có thể là bi quan.

## 7. Đề xuất luật cho `docs/PHONG-CACH-HINH.md` §5 — "Không cảnh nào chỉ là ảnh tĩnh trượt"
1. **Mọi cảnh L1 có ít nhất một nguồn chuyển động trong khung ngoài máy quay:** (a) thị sai 2.5D ≥ 2 lớp theo độ sâu, **và/hoặc** (b) đúng 1 lớp chuyển động phủ hợp nội dung, **hoặc** (c) clip Veo. Mặc định = (a) + (b) (biến thể B).
2. **2.5D:** độ sâu Depth Anything V2 Small (Apache-2.0, CPU); mỗi lớp cong theo độ sâu từng điểm ảnh, mép lớp trước dùng độ sâu nở; trượt ≤ 36 px ở độ sâu 1 (1080p), phóng 1,06–1,14. **Vật mảnh** (dây, chân bàn, tóc rời, gọng kính, xích) gần mép lớp → trượt ≤ 22 px.
3. **QC mép bắt buộc:** tờ `qc_mep` (1:1 khung đầu/cuối tại mép chênh sâu lớn nhất) cho mọi tranh; lỗi nhân đôi/vệt vá/rách → giảm biên độ, hết thì bỏ thị sai cảnh đó (vẫn phải có (b)).
4. **Lớp phủ:** ≤ 1/cảnh; phát ra từ đúng nguồn có trong tranh (V5: hơi nước từ cốc, bụi trong vùng sáng, cát trong đồng hồ); đèn chập chờn ≤ ±6 % độ sáng, < 3 Hz; không thêm vật/chữ/người; không phủ lên mặt nhân vật.
5. **Veo:** 4 s (0,20 USD), khung đầu không người không chữ, 5–8 khoảnh khắc/tập; lời ghi "very slow / slightly" cho vật treo (bài học V5 lắc quá rộng).
6. **Chuyển cảnh:** khi hai tranh kề nhau có vật cùng dáng → khớp hình (neo đặt cùng chỗ trên màn khi hoà); rung tay ≤ 1,5 px được dùng chung.
7. **Đo:** `do_chuyen_dong.py` (so với đối chứng phẳng P) — mục tiêu ≥ 50 % thời lượng L1 mỗi tập có chuyển động thật; kèm tờ 0,5 s mắt xem.
8. Cảnh có nhân vật đại diện: thị sai biên độ nhỏ (≤ 24 px), không Veo.

## 8. Lệch so với lệnh / việc chưa đạt (nói rõ)
1. **QC mép còn 3 lỗi nhỏ** chỉ thấy ở 1:1 khung cuối (b077 vệt dây mờ thứ hai, b080 vệt vá cạnh lưng ghế, b009 viền mảnh vành trên) — có ở A, B, C (C không dùng b009 2.5D). Chưa sửa tiếp (cách sửa: bỏ thị sai riêng vật mảnh, hoặc 2 lớp cho tranh đó).
2. **Thước đo** phải làm lại 2 lần (v1, v2 không hiệu chỉnh được); bản dùng cần đối chứng P (dựng thêm 272 s). Lấy nét chuyển không được thước đo tính.
3. **Đoạn thử** P05 + P08 = 59,97 s, bỏ S020–S024 (P04: định nghĩa kỳ phiếu, G04, trang L3 T03) và S043 để vừa ~60 s; "kỳ phiếu → phép tính" bắt đầu từ S025 "Over the life of the note…".
4. Âm hai khúc nối cứng (tắt/mở 0,15 s), không chỉnh nhạc lại — giọng/nhạc lấy nguyên từ bản đăng.
5. V5 lắc rộng hơn lời — giữ (không vi phạm V1–V8, không biến dạng), không chi lượt 2.
6. Chưa xem phát liên tục; đánh giá cảm giác dựa trên khung/tờ + thước đo.
7. Tiến trình `pkill -f` hai lần tự dừng chính lệnh của phiên (mẫu khớp dòng lệnh) — không ảnh hưởng tệp; đã đổi cách dừng.

## 9. Cần chủ dự án / điều phối
1. Xem `reports/mrp2/xem/{goc,A,B,C}.mp4` cạnh nhau; chọn mặc định (khuyến nghị **B + Veo 4 s 5–8 clip/tập**).
2. Duyệt (hoặc sửa) luật §7 vào `PHONG-CACH-HINH.md` §5; nếu duyệt, cập nhật đơn giá Veo 4 s 0,20 USD ở §6.
3. Đối chiếu **6,20 USD** chi ngoài khoá MR trong cửa sổ 14:57–15:29 UTC (số dư tài khoản sau phiên 12,03 USD).
