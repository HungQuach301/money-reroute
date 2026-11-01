# PHƯƠNG ÁN GU — Tập 1 · `tap01-1inmm` (tiêu đề, thumbnail, giọng, bảng màu/chữ)

> MR-3 · 01/11/2026 · NHÁP G1 — **chủ dự án chọn** (QUY-TRINH §1: gu là quyết định của chủ dự án). Không sinh mẫu giọng, không sinh ảnh (0 USD).

## 1. Tiêu đề (≤ 60 ký tự, đếm máy)

| # | Tiêu đề | Ký tự | Tầng / căn cứ | Ghi chú |
|---|---|---|---|---|
| **T1 (đề xuất)** | How an Actor Raised $650 Million on Fake Film Deals | 51 | ●T: "at least $650 million" (N7 tr. 12); hợp đồng "fake" (N7 tr. 10–11); "actor" (N2, N3) | Không tên thương hiệu, không nhãn "scammer"; Horwitz là ● |
| T2 | The Film Deals Were Fake. The $650 Million Was Real. | 52 | như T1 | Móc tò mò, không tên người |
| T3 | 25% in Six Months: Red Flags in a $650M Film Scheme | 51 | ●T: 25–45 %, 6–12 tháng (N7 tr. 10); "scheme to defraud" (N7 tr. 9) | Hướng bài học. "25%" là mức thấp của dải thừa nhận |

Không dùng trong tiêu đề: "HBO", "Netflix" (tiêu đề không chứa được câu "not accused" — luật 8e); "Ponzi" (chữ của DOJ, không phải tội danh — luật 8d); "con man/scammer/Hollywood fraud".

## 2. Thumbnail (chữ/sơ đồ; không mặt, không logo, không tài liệu toà dựng lại)

| # | Ý | Bố cục | Chữ | Tránh |
|---|---|---|---|---|
| **TN1 (đề xuất, đi với T1/T2)** | "Dải phim rỗng" | Dải phim 35 mm phẳng (vector) chạy ngang; các ô phim **trống**, ô giữa đóng dấu đỏ "FAKE"; góc phải số lớn | "$650M" (lớn) · "FAKE FILM DEALS" (nhỏ hơn) | Không poster phim thật, không tên phim, không logo streaming, không màu nhận diện thương hiệu (đỏ-đen kiểu nền tảng) |
| TN2 (đi với T3) | "Tháp ly" | Sơ đồ phẳng tháp ly: đỉnh "NEW MONEY" chảy xuống các tầng; tầng đáy trống, mũi tên đỏ | "25–45% IN 6 MONTHS?" | Không ảnh thật, không người; sơ đồ là minh hoạ khái niệm (không ghi "Ponzi" lên hình gắn với Horwitz) |

Hai ý đều là đồ hoạ tự vẽ (0 USD, dựng ở M-d), không cần ảnh AI.

## 3. Giọng đọc ElevenLabs (mô tả — chưa sinh mẫu)

Điều kiện chung: giọng **tổng hợp** (Voice Design hoặc giọng thư viện **không** mang tên/nhái người nổi tiếng), **không** giống giọng bị cáo, nạn nhân, quan chức trong vụ (HIEN-CHUONG §4); en-US General American; thử trên cùng đoạn S004–S010 (~700 ký tự) ở M-c, tính vào trần.

| # | Mô tả | Nhịp | Thông số khởi điểm (thử ở M-c) | Hợp với |
|---|---|---|---|---|
| **G1 (đề xuất)** | Nam, 35–50 tuổi, trầm-ấm, điềm tĩnh kiểu phóng sự điều tra; không kịch hoá, nhấn nhẹ ở số liệu | ~140 từ/phút (tập ≈ 16 phút) | stability ~0,55 · similarity ~0,75 · style thấp (≤ 0,2) | Bảng màu B1 "Hồ sơ"; kênh lâu dài, nhiều chủ đề nặng |
| G2 | Nữ, 30–45 tuổi, giọng trung, rõ, kiểu người giải thích (explainer) thân thiện; hơi nhanh, sáng hơn ở phần bài học | ~150 từ/phút (tập ≈ 15 phút) | stability ~0,45 · similarity ~0,75 · style ~0,25 | Bảng màu B2 "Đêm"; tăng cảm giác "bài học" |

Phát âm cần cài (cả hai giọng): `SEC` → "S-E-C", `FBI`, `HBO` đánh vần; `FINRA` → "FIN-rah"; `one-in-M-M`; "Scarsi" (thử nghe, sửa bằng từ điển phát âm nếu lệch).

## 4. Bảng màu / chữ kênh (font Google Fonts, giấy phép OFL)

| | **B1 "Hồ sơ" (đề xuất)** | B2 "Đêm" |
|---|---|---|
| Nền | giấy ngà `#F4F1EA` | xanh đêm `#0E1726` |
| Chữ chính | mực `#1B1F24` | `#E8ECF2` |
| Dòng tiền / nhấn | xanh két `#2B7A78` | hổ phách `#F2A541` |
| Cảnh báo / "FAKE" / dấu hiệu | đỏ cam `#D9480F` | đỏ `#E5484D` |
| Phụ / lưới sơ đồ | xám `#8A8F98` | xám thép `#7A8BA6` |
| Nhãn tầng | `● CONVICTED` đỏ cam · `◐ ALLEGED` hổ phách `#B7791F` · `ILLUSTRATIVE` xám — chữ trắng trên ô màu | `● CONVICTED` đỏ · `◐ ALLEGED` hổ phách · `ILLUSTRATIVE` xám thép |
| Tiêu đề | IBM Plex Serif SemiBold | Archivo Black |
| Thân, sơ đồ | Inter | Source Sans 3 |
| Dòng nguồn, số vụ | IBM Plex Mono (≥ 22 px ở 1080p) | JetBrains Mono (≥ 22 px) |
| Cảm giác | tài liệu, thư viện luật, bình tĩnh — hợp ảnh trang hồ sơ (TL) | phim tài liệu tội phạm, tương phản cao — hợp cảnh Veo tối |

Kiểm ở M-d: tương phản WCAG ≥ 4,5:1 cho chữ thân và dòng nguồn (chưa đo); công cụ `scripts/common/ban_do.py`, `mau_look.py` còn thiếu tệp phụ thuộc (báo cáo MR-0 §4) → chốt look sau khi có.
