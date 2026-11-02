# TỜ HƯỚNG DẪN PHONG CÁCH — Biến thể B: Minh hoạ phẳng / đồ hoạ theo B1 "Hồ sơ"

> MR-P1 · 02/11/2026 · thử cho tập 1 `tap01-1inmm` P00–P03. Tranh: `lab/mrp1/B/` (LFS). Lời sinh đầy đủ: `reports/mrp1/B/loi_anh.json`. Model `google/gemini-nano-banana-2.1`, 16:9, 1K (1376×768).

## Phong cách
Minh hoạ vector phẳng kiểu biên tập, bảng màu khoá theo B1 (giấy ngà, mực, xanh két, đỏ cam ít, xám ấm), hình khối đơn giản, bóng phẳng, vân giấy nhẹ; người giản lược (mắt chấm, miệng một nét). Liền mạch với thẻ chữ/bằng chứng B1; ít "phim" hơn A.

**Tiền tố phong cách (nguyên văn):**
> ART STYLE (variant B): flat vector editorial illustration with a strictly limited palette — ivory paper #F4F1EA, ink #1B1F24, teal #2B7A78, red-orange #D9480F used sparingly as accent, warm gray #8A8F98. Simple geometric shapes, flat fills, soft flat shadows, subtle paper-grain texture, clean 'case file' documentary look. People simplified with minimal facial features (simple dot eyes, single-line mouth).

Tham chiếu: `lab/mrp1/B/a01_l1.png`.

## Nhân vật (giữ nhất quán — dán nguyên văn vào mọi lời sinh)
- **Nhà đầu tư (nhân vật đại diện, tự nghĩ ra, không giống ai):** phụ nữ ~50 tuổi, tóc xoăn dài ngang vai muối tiêu, kính tròn gọng đồi mồi mảnh, áo len cardigan vàng mù tạt ngoài sơ mi trắng cổ đứng. **Được** có mặt. Không gắn quốc tịch/sắc tộc; không phóng đại nét mặt.
- **Người đàn ông vest tối (đại diện Horwitz — người thật):** chỉ **lưng thẳng, bóng ngược sáng, hoặc tay/tay áo** (khuy măng-sét). **Không** góc 3/4 sau lộ mép má/tai (bài học a14 lượt 1), không nghiêng mặt, không đặc điểm nhận dạng. Nhãn "ILLUSTRATIVE — not the real person" ở cảnh đầu mỗi đoạn.
- Không ai khác có mặt rõ. Khách nền (nhà hàng) → cắt khung bỏ hoặc ghi "restaurant otherwise empty" vào lời.

## Luật hình (hậu tố mọi lời, nguyên văn ở `loi_anh.json` → `hau_to`)
Không chữ/số/logo/biển/giao diện; màn hình, giấy, poster, phong bì để trắng hoặc mờ; không tài liệu, hợp đồng, tiền giấy; không người thật/người nổi tiếng; không biếm hoạ sắc tộc/quốc tịch; 16:9, một khung, không viền. **Mọi chữ thêm ở hậu kỳ** (nhãn, bong bóng tin nhắn chung có nhãn "ILLUSTRATIVE — not a real message", thẻ số liệu có huy hiệu tầng + dòng nguồn).

## Tham chiếu nhất quán
- Tranh đầu `a01` sinh **không** tham chiếu; mọi tranh sau gửi kèm `a01_l1.png` + câu `ref_loi`.
- **Bài học MR-P1:** tham chiếu có nhà đầu tư làm model **chèn nhà đầu tư vào cảnh không có bà** (a14 lượt 2 cả A và B; B a16). Bản sau: dùng **hai** tham chiếu — `ref_nv` (có nhà đầu tư, chỉ cho cảnh có bà) và `ref_canh` (một cảnh trống cùng nét vẽ, cho mọi cảnh khác); cảnh không có bà ghi rõ "the investor woman is NOT in this scene".

## Chuyển động + chuyển cảnh (bộ dựng `scripts/mrp1/dung.py`)
Mỗi tranh tĩnh: đẩy/kéo 1,00 ↔ 1,12–1,18 hoặc lia ngang 12 % khung, có làm mượt (smoothstep); hoà cảnh 0,5 s; thẻ chữ đẩy rất nhẹ (1,00 → 1,04); huy hiệu tầng + dòng nguồn ở lớp tĩnh (không trôi ra ngoài khung). Một tranh có thể dùng 2 lần bằng khung cắt khác (a09, a12, a13).

## Thẻ chữ / bằng chứng
Bảng màu **B1 "Hồ sơ"** cho cả hai biến thể (đã duyệt): giấy `#F4F1EA`, mực `#1B1F24`, xanh két `#2B7A78`, đỏ cam `#D9480F`, xám `#8A8F98`, ◐ hổ phách `#B7791F`. Phông B1 (IBM Plex) **chưa có** trong máy (tải github 403, không vượt) → bản thử dùng Liberation Serif Bold / Inter / JetBrains Mono. Bằng chứng: ảnh trang PDF thật (pdftoppm 200 dpi), cắt đúng dòng, chỉ thêm khung khoanh đỏ cam + nền dạ quang nhạt; không vẽ lại chữ.
