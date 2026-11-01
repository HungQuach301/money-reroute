# RIGHTS — sổ quyền tài sản Money Reroute

Khuôn: `crux-lab/RIGHTS.md` (§F footage ngoài, §F2 danh sách cấm) và `lost-places-lab/RIGHTS.md`. Mọi tài sản đi vào một tập có một dòng: nguồn, giấy phép (**trích nguyên câu** + link), phạm vi, ghi công, ngày, SHA-256 khi là tệp. Tài sản chưa có giấy phép trích nguyên văn → **chưa được dùng** trong bản phát hành.

## Luật chung (MR-0, chờ chủ dự án duyệt cùng HIEN-CHUONG)
- **Hồ sơ chính phủ Mỹ** (SEC, DOJ, FTC, toà án liên bang): tác phẩm của nhân viên liên bang khi làm nhiệm vụ thuộc phạm vi công cộng (17 U.S.C. §105) — **kiểm từng tệp**: tài liệu do bên thứ ba nộp (vật chứng, ảnh, thư của luật sư) **không** mặc nhiên thuộc §105. Trích có ghi nguồn trên hình + mô tả.
- **Được:** PD có căn cứ, CC0, CC BY (ghi TASL); dữ liệu chính phủ để tự vẽ sơ đồ; tài sản tự sinh bằng mã (một dòng chung).
- **Cấm:** CC NC, ND, BY-SA cho hình/video; quyền không rõ; **ảnh/footage có mặt người thật trong vụ**; logo/giao diện sản phẩm (trừ chữ thuần khi cần nhận diện); đoạn của kênh YouTube/đài tin tức khác; hình AI trình bày như tư liệu.
- **Đầu ra AI** (ảnh, video, giọng, nhạc): ghi model, nhà cung cấp, phiên; khai "AI use" = Yes (HIEN-CHUONG §6).

## Công cụ chép từ repo khác (MR-0, 01/11/2026)
| Tệp trong repo này | Nguồn | Giấy phép | Ghi chú |
|---|---|---|---|
| `scripts/common/{quet_v8,quet_v8_cham,ban_do,mua_hau_ky,mau_look,preflight_scan}.py`, `scripts/cp/budget.py`, `tools/preflight.sh`, khuôn `.gitattributes`/`tools/lfs-allow.txt`, nội dung `docs/LUAT-VEO.md` | `HungQuach301/lost-places-lab` @ `ae22e370700d6dc254974588b824802d3edb2406` | Mã của cùng chủ dự án (repo nội bộ); không có tệp LICENSE trong thư mục chép | Ghi nguồn + SHA ở đầu mỗi tệp. `ban_do.py` khi chạy tải Natural Earth (PD) và Copernicus DEM GLO-30 — **ghi dòng RIGHTS riêng khi một tập dùng** (chưa dùng ở MR-0) |

## Tài sản của tập
_(chưa có — MR-0 không sinh, không tải tài sản nào)_
