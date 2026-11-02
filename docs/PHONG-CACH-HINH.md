# PHONG CÁCH HÌNH — Money Reroute v1

> Chủ dự án duyệt 02/11/2026 10:20 (giờ Hà Nội), sau thử MR-P1: **PA-A1** (tranh A + tách màu theo vai trò), **mật độ giữa**, clip Veo tả thực chỉ làm điểm nhấn. Bổ sung của chủ dự án: **mọi phần quy trình, dòng tiền, con số phải trực quan, sinh động, có điểm nhấn** (đồ hoạ động), không để sơ đồ hộp tĩnh.
> Khi khác `docs/HIEN-CHUONG.md` (§4 người thật, §5 cấm), hiến chương thắng. Tờ phong cách chi tiết + tiền tố lời sinh: `reports/mrp1/A/PHONG-CACH.md` (dùng làm gốc, áp các sửa dưới đây).

## 1. Ba lớp hình (mỗi lớp một vai, người xem nhận ra ngay)
| Lớp | Dùng cho | Nhìn thế nào |
|---|---|---|
| **L1 Kể chuyện** | cảnh dựng, không khí, nhân vật đại diện | Tranh A: vẽ số bán hiện thực, tông tối teal–hổ phách, nét cọ + hạt phim; rõ là tranh, không giống ảnh. Nhãn "ILLUSTRATIVE" lần đầu mỗi đoạn |
| **L2 Đồ hoạ giải thích** | quy trình, dòng tiền, con số, so sánh, phép tính, mốc thời gian | **Đồ hoạ động trên nền tối** (than `#14181D`, lưới mờ), cùng tông L1; màu nhấn theo §3. Chi tiết §2 |
| **L3 Hồ sơ thật** | trang toà án/cơ quan, câu trích nguyên văn, dòng nguồn, nhãn ●/◐ | **Nền ngà B1 `#F4F1EA`** — chỉ lớp này dùng nền ngà. Trang hồ sơ giữ nguyên dạng (crop trang được phép), khoanh câu, không vẽ lại |
Thẻ tiêu đề, thẻ "không liên quan" (KBCB), thẻ bài học: **nền tối, chữ ngà, chồng lên tranh** (thanh dưới hoặc khối bên), không chiếm cả màn hình; giữ 3–4 s (KBCB ≤ 4 s, có thể chồng lên cảnh kế tiếp).

## 2. Đồ hoạ giải thích (L2) — bắt buộc trực quan, sinh động, có điểm nhấn
Mỗi đồ hoạ trả lời **một câu hỏi** của lời và dẫn mắt tới **một điểm nhấn**. Làm bằng mã (0 USD), dựng lại được.
1. **Hiện dần theo lời:** từng bước/ô xuất hiện đúng lúc giọng đọc tới từ đó (mốc whisper); không hiện cả sơ đồ một lúc.
2. **Dòng tiền chuyển động:** tiền là **hạt/dòng chảy** chạy dọc đường nối (độ dày = số tiền); chỗ tiền "đi sai" đổi màu đỏ cam, có nhịp đập nhẹ. Vòng Ponzi = dòng tiền **quay về** người cũ thấy rõ.
3. **Biểu tượng thay chữ:** mỗi ô có icon vẽ đơn giản, cùng nét (nhà đầu tư, công ty, cuộn phim, nền tảng, ngân hàng, toà án…); chữ trong ô ≤ 3 từ. Icon tự vẽ bằng mã hoặc sinh 1 lần thành bộ (không logo, không thương hiệu).
4. **Con số đếm lên:** số tiền/phần trăm/năm tù chạy số từ 0 tới giá trị, dừng có nhấn (phóng nhẹ + vạch sáng); số lớn so với vật quen (vd thanh dài, chồng tiền) khi hồ sơ cho phép.
5. **Phép tính hoạt hoạ:** ví dụ lãi kỳ ngắn → lãi năm: thanh 35 % nhân đôi/nhân luỹ tiến thành ~82 %, hai cột so sánh "nghe như" vs "thực ra".
6. **Mốc thời gian:** trục ngang có điểm mốc bật sáng lần lượt; đồng hồ đếm ngược khi lời cần (vd tới 9/4).
7. **"Lời hứa" vs "Thực tế":** cùng sơ đồ chia đôi; nửa thực tế hiện sau, các ô rỗng/đứt/đánh dấu "FAKE — admitted" đúng tầng.
8. **Một điểm nhấn mỗi đồ hoạ:** màu đỏ cam chỉ cho đúng một chỗ (điểm sai/điểm then chốt); phần còn lại trung tính.
9. **Nhãn tầng + nguồn** luôn ở góc dưới (lớp tĩnh), theo `loi.json`; không chữ nào ngoài lời đã duyệt, số liệu hồ sơ, nhãn và nguồn.
10. Chuyển động mượt (easing), ≤ 1 hiệu ứng nổi bật mỗi 2 s; không nhấp nháy gắt (an toàn thị giác).

## 3. Bảng màu
- L1/L2 nền: than `#14181D`, teal `#2B7A78`, hổ phách `#C08A3E`, chữ ngà `#F4F1EA`, xám `#8A8F98`.
- Nhấn duy nhất: **đỏ cam `#D9480F`** (điểm sai, "FAKE", nhãn ● CONVICTED).
- ◐ ALLEGED: hổ phách `#B7791F`.
- L3: B1 nguyên bản (ngà `#F4F1EA`, mực `#1B1F24`).
- Phông: IBM Plex Serif/Sans/Mono khi có đường tải chính thức; chưa có → Liberation Serif / Inter / JetBrains Mono (như MR-P1), ghi trong báo cáo.

## 4. Người và nhân vật (giữ HIEN-CHUONG §4)
- **Người thật trong vụ:** chỉ bóng, lưng thẳng, tay/tay áo; không góc 3/4 lộ má/tai; có thể kèm nhãn tên trên bóng.
- **Nhân vật đại diện** (nạn nhân/nhà đầu tư/người gọi điện): được có mặt cách điệu, tự nghĩ ra, không giống ai, nhất quán trong tập; nhãn ILLUSTRATIVE.
- Không biếm hoạ sắc tộc/quốc tịch/tôn giáo; trang phục và bối cảnh trung tính.
- Không chữ/số/logo/biển/giao diện trong tranh; không tài liệu/hợp đồng/tiền giấy giả.
- Tham chiếu nhất quán: **hai** tham chiếu — `ref_nv` (chỉ cảnh có nhân vật đó) và `ref_canh` (cảnh trống cùng phong cách) — bài học MR-P1.

## 5. Mật độ và chuyển động
- Cảnh tranh trung bình **~2,5 s**; dùng lại một tranh tối đa 2 lần bằng khung cắt khác. L2 giữ đủ thời gian đọc nhưng luôn có chuyển động.
- Tranh tĩnh: đẩy/kéo/lia mượt + hoà cảnh 0,5 s.
- **Cảnh động Veo:** tối đa 4–5 khoảnh khắc lớn mỗi tập, **ảnh → video** từ chính tranh L1 (giữ phong cách); 0,40 USD/clip; luật V1–V8. Clip Veo tả thực tập 1 (MR-4/MR-5): chỉ dùng 3–4 clip vật thể hợp tông (V10, V11, V12/V13), chỉnh màu teal–hổ phách; còn lại không dùng.

## 6. Đơn giá (đo thật)
- Tranh `google/gemini-nano-banana-2.1` 16:9 1K: **0,0389 USD/tranh**, sinh lại ~5 % (MR-P1).
- Veo 3.1 Lite 1080p 8 s: 0,40 USD/clip, ~1,44 lượt/khe (MR-4/MR-5).
- Ước một tập ~15 phút mật độ giữa: ~190 tranh ≈ **7,8 USD** + 4–5 clip ảnh→video ≈ **2,0–3,0 USD**.
