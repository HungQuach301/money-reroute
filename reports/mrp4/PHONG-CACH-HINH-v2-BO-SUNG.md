# ĐỀ XUẤT BỔ SUNG PHONG-CACH-HINH v2 — âm, độ sâu, từ vựng chuyển động, bố cục nhiều lớp (từ MR-P4)

> NHÁP của phiên MR-P4 (03/11/2026), **chưa duyệt**. Bổ sung cho `reports/mrp3/PHONG-CACH-HINH-v2-DE-XUAT.md` (MR-P3): **thay** §5.2 (2.5D "trôi") và §7.4 (mức âm) của tờ đó; **thêm** §5a, §5b, §7a, §9. Khi khác HIEN-CHUONG §4–§5, hiến chương thắng. Căn cứ số đo: `reports/mrp4/BAO-CAO.md`, `reports/mrp4/am_do.json`, `reports/mrp4/do_sau*.json`, `reports/mrp4/dung_M2_moi.json`.

## §5a Luật độ sâu (thay §5.2 của MR-P3)
1. **Đo trước khi cho máy chạy:** mỗi tranh L1 qua `scripts/mrp4/sau.py` → chỉ số **độ sâu hữu dụng HD (0–100)** = 100 · TRẢI · TÁCH · f(GẦN):
   - TRẢI = (p95 − p5)/p95 độ sâu thô (Depth Anything V2 Small); TÁCH = trung vị độ sâu lớp gần − phần còn lại; GẦN = % khung của lớp gần, f = min(GẦN/12 %, 1), giảm khi > 55 %.
2. **Ngưỡng:**
   | HD | Được dùng | Cấm |
   |---|---|---|
   | **< 45** | máy đứng yên + lớp chuyển động trong khung; **cắt vào** (cắt cứng +20 % đúng từ neo) | trượt, 2.5D, đẩy/kéo/lia mượt |
   | **45–60** | đẩy / kéo (phóng + dolly 2.5D nhẹ, K ≤ 0,03), cắt, đứng yên | lia |
   | **≥ 60** | mọi kiểu; dolly K ≤ 0,07; lia có thị sai ±55 px | — |
3. Tranh dưới 45 ở cảnh mà lời cần chuyển động (đẩy/lia) → **tạo lại theo §9** (0,04 USD/tranh) trước khi hạ kiểu máy; ghi HD trước/sau.
4. Cổng chạy tự động trong bộ dựng (`scripts/mrp4/may.py` `cong()`): kiểu vượt cổng tự hạ (đẩy → cắt; kéo/lia → đứng yên hoặc đẩy) và ghi vào `dung_*.json`.
5. Clip ảnh→video và nhân vật hoạt hoạ mã: không 2.5D; máy chỉ phóng/khung 2D.

## §5b Từ vựng chuyển động theo nhịp lời (thay "trôi nhẹ đều")
Mỗi cảnh **đúng một kiểu**, ghi **lý do + từ neo** (từ trong lời, mốc whisper) trong bảng cảnh; chuyển động **bắt đầu ở từ neo − 0,15 s**, có gia tốc/giảm tốc (cubic in-out), hoặc **đứng yên hẳn**. **Cấm trôi nhẹ đều** (trượt 20–30 px + phóng 5 % suốt cảnh).
| Kiểu | Khi nào | Biên độ |
|---|---|---|
| **Đẩy vào chi tiết** | lời gọi tên một vật/chi tiết (điện thoại, tên người, hạn chót) | phóng **15–25 %** về điểm neo; ≥ 0,9 s |
| **Kéo ra lộ cảnh** | **cú lật** (câu đảo chiều: "…is real", "This is the story") | từ +20 % về toàn cảnh |
| **Lia theo dòng tiền** | lời nói tiền đi đâu (trả về, mua, cấp phép); hướng lia = hướng tiền | ≈ 14 % khung + thị sai; chỉ HD ≥ 60 |
| **Máy đứng yên** | câu nặng: **bản án, thừa nhận, câu pháp lý (KBCB), lệnh toà**; cảnh < 1,4 s | 0; chỉ lớp trong khung (bụi, đèn, rung khi khoá đúng từ) |
| **Cắt vào** | thay đẩy khi HD < 45 | cắt cứng +20 % đúng từ neo |
| **Giật nhanh** | **chuyển hồi** (sau cú lật sang nhân vật; sang hồi "dồn") | lia giật 0,32 s (0,14 ra + 0,18 vào) + nhoè + tiếng vút −8 dB; thay hoà cảnh |
Tỉ lệ gợi ý mỗi đoạn ~2 phút: đẩy ~35 %, đứng yên ~30 %, lia ~15 %, kéo ≤ 2 (đúng cú lật), giật ≤ 1/hồi.

## §7a Luật âm (thay §7.4 của MR-P3)
Mức đo **tương đối so với độ to giọng** (LUFS tích hợp trên đoạn có lời) — đo bằng `scripts/mrp4/dung_p4.py am` → `am_do.json`.
1. **Giọng:** lọc thấp 70 Hz → nén 3:1 (ngưỡng −22 dB, attack 8 ms, release 120 ms, +3 dB) → −1,5 dB @ 250 Hz → **+4 dB @ 3,2 kHz** (nâng 2–5 kHz) → −3 dB @ 7 kHz → khử xì động (`deesser i 0,4`). Kiểm: dải 2–5 kHz tăng ≥ 4 dB, **đỉnh xì p95 không cao hơn giọng gốc**.
2. **Nhạc dưới lời −12…−15 dB** (đích −13,5), **sidechain** do giọng điều khiển (ngưỡng −32 dBFS, 6:1, attack 25 ms, release 450 ms) → tự hạ khi có lời, **dâng ở khoảng nghỉ** (đo được −7 dB so với giọng). Cú lật: nhạc dừng cứng + va chạm như MR-P3.
3. **Tiếng nhấn −6…−10 dB** (đích −8, đo độ to tức thời 400 ms lớn nhất); hai tiếng nhấn trùng nhau trong 0,5 s → bỏ một.
4. **Tiếng nền −22…−28 dB** (đích −25, tích hợp trên đoạn của nó): tủ lạnh, mưa, phố đêm, đồng hồ, nhịp tim.
5. **Tổng −14 LUFS, đỉnh thật ≤ −1 dBTP** (đặt một hệ số tuyến tính; đỉnh > −1,2 dBTP → limiter ở 192 kHz rồi đo lại bằng `ebur128 peak=true`).
6. **Bản kiểm loa điện thoại** mỗi bản dựng: lọc 300 Hz–8 kHz, mono (`*_loa.mp4`); nghe lời phải rõ trên bản này trước G2.

## §9 Bố cục tranh nhiều lớp (thêm vào tiền tố lời sinh tranh)
Thêm khối sau **ngay sau tiền tố phong cách A** (trước "SCENE:") cho **mọi tranh L1 cảnh vật/không khí** (không bắt buộc ở cận mặt nhân vật đại diện):
```
COMPOSITION — LAYERED DEPTH (mandatory): build the frame in three clearly separated depth planes. FOREGROUND: one dark object very close
to the camera at a frame edge (or framing the view, as if looking past it or through a gap), partly cut off by the frame, softly out of
focus. MIDGROUND: the main subject, sharp. BACKGROUND: a distinct far plane that recedes into haze or darkness. Eye-level or low camera,
never a flat top-down view; no wall or surface filling the whole frame; strong atmospheric perspective between planes.
```
và trong lời từng cảnh ghi rõ ba dòng `FOREGROUND: … MIDGROUND: … BACKGROUND: …` (vật tiền cảnh lấy từ chính bối cảnh: lưng ghế, mép cột, vành cốc, dải phim, khung cửa, xích).
- **Cấm ở tiền cảnh/hậu cảnh:** cửa mở tối có áo/giày treo (đọc như bóng người — lỗi b001 lượt 1), giấy dán tường có vệt giống chữ, bóng người mơ hồ. Cảnh "không ai" → ghi "closed door", "bare walls".
- **QC như MR-6:** YuNet (mặt) + RapidOCR (chữ) + mắt xem 1:1; đo HD sau sinh — đích **≥ 55** (MR-P4: 10/10 đạt, TB 69).
- Tham chiếu: `ref_canh` (a15_l1), tiền tố + hậu tố A nguyên văn (`reports/mrp4/anh/loi_anh.json`).
- Chi: 0,039 USD/tranh; ~1 lượt 2/10 tranh.
