# BÁO CÁO MR-0 — Khởi tạo repo Money Reroute

> Phiên Claude Code, 01/11/2026. Nhánh `claude/money-reroute-init-sj5scm` (từ `main` @ `78637c1`). **Chi API: 0 USD**, chỉ đọc số dư bằng GET miễn phí. Không merge, không xoá nhánh, không force-push.

## 1. Đã đọc (chỉ đọc, không sửa repo nguồn)
| Repo @ commit | Tệp |
|---|---|
| `HungQuach301/lost-places-lab` @ `ae22e370700d6dc254974588b824802d3edb2406` (clone nông, chỉ đọc) | `CLAUDE.md`; `docs/QUY-TRINH-TAP.md` (bản 2.2); `docs/BIBLE.md`; `docs/CONG-THUC-LOAT.md` (bản 1.4); `docs/K-LUAT.md` (§1–§2, mục lục); `docs/NHAT-KY.md` R-139 → R-148 |
| `HungQuach301/crux-lab` @ `f3a16ff6a66c0ce21a026fafbf7e1d8b02516712` (clone ẩn danh, chỉ đọc) | `CHARTER.md` (v5); `playbook/quality-framework.md` (§0–§9); `playbook/lessons.md` (A, B, B2–B5, C); `RIGHTS.md` (đầu sổ, §F1–§F5) |

Ghi chú: `K-LUAT.md` (36 KB) và `lessons.md` (63 KB) đọc phần luật chung và mục lục, **không** đọc hết từng ngưỡng K-1.3 / bài học tập 2–7 của crux — các phần đó gắn với hình của kênh khác. `RIGHTS.md` crux (81 KB) đọc phần luật (§F), không đọc từng dòng tài sản.

## 2. Tệp đã tạo
| Tệp | Nội dung |
|---|---|
| `CLAUDE.md` | Luật mọi phiên: không đoán; trần chi + 402 → DỪNG; tệp tốn tiền LFS ≤ 10 phút; preflight trước commit; không merge/xoá nhánh/force-push; không in khoá; không mặt người thật; báo cáo tiếng Việt; DỪNG cuối mốc |
| `docs/HIEN-CHUONG.md` (NHÁP, ~1,5 trang) | Định vị drama bài học tài chính/lừa đảo có hồ sơ công khai; **ba tầng pháp lý ĐÃ KẾT ÁN / BỊ CÁO BUỘC / TIN ĐỒN** (điều kiện nguồn, cách nói, nhãn hình); không mặt người thật; nhân vật minh hoạ nhãn "ILLUSTRATIVE"; chỉ dạy dấu hiệu nhận diện; nguồn SEC/DOJ/FTC/toà án ghi trên hình + mô tả; khai AI; danh sách cấm |
| `docs/QUY-TRINH-TAP.md` (NHÁP) | 6 mốc M-a → M-f; **G1** = đề tài + kịch bản + trần chi; **G2** = bản cuối; kiểm lời + kiểm tầng độc lập; đơn giá tham chiếu (số của lost-places-lab, ghi rõ chưa đo trên MR) |
| `docs/LUAT-VEO.md` | V1–V8 **nguyên văn** từ CONG-THUC-LOAT §1.9 (đã so máy: KHỚP) + ghi chú áp dụng cho MR tách riêng |
| `docs/NHAT-KY.md` | Mục MR-0 |
| `docs/BAN-GIAO-DIEU-PHOI.md` | Trạng thái, quỹ, việc kế tiếp |
| `RIGHTS.md` | Luật quyền chung (hồ sơ chính phủ Mỹ §105 kiểm từng tệp; cấm ảnh người thật) + dòng công cụ chép |
| `COST-LEDGER.csv` | 3 dòng đọc số dư (0 USD) |
| `.gitattributes`, `tools/lfs-allow.txt` | LFS cho `lab/**` (ảnh/clip/âm) và `reports/*/xem/*.mp4`, `reports/*/thumb/*` — hai tệp khớp nhau |

## 3. Công cụ chép từ lost-places-lab @ `ae22e37`
Mỗi tệp có dòng `# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — <đường dẫn>` ở đầu (sau shebang nếu có).
| Tệp | Sửa? | Kiểm |
|---|---|---|
| `scripts/common/quet_v8.py` | nguyên văn | biên dịch OK; import OK sau khi cài `opencv-python-headless` (cột 5 cần thêm `ultralytics` + `torch` CPU) |
| `scripts/common/quet_v8_cham.py` | nguyên văn | import OK. Bảng lỗi đã biết là của Petra/Machu Picchu — chỉ dùng làm mẫu hiệu chỉnh |
| `scripts/common/mua_hau_ky.py` | nguyên văn | **chạy thật** trên clip thử 2 s 640×360: ra 48 khung = vào 48 khung |
| `scripts/common/mau_look.py` | nguyên văn | **chưa chạy được**: cần `lab/mau/look-A.json` (look màu của kênh gốc) |
| `scripts/common/ban_do.py` | nguyên văn | **chưa chạy được**: cần `scripts/m2c/do_hoa.py` (bảng màu + phông kênh gốc), `lab/bd1/dia_diem.json`, `lab/mau/look-A.json`, `rasterio` |
| `scripts/common/preflight_scan.py` | nguyên văn | **thêm ngoài danh sách lệnh**: `tools/preflight.sh` gọi tệp này, thiếu thì preflight không chạy |
| `scripts/cp/budget.py` | **đã sửa** (ghi ở đầu tệp) | bảng trần LP → `CAPS_PHIEN` theo phiên MR (`mr0` = 0 mọi khoản); `LP_PHIEN` → `MR_PHIEN`; thêm `openrouter_usd`; `Quy402` + `bao_402()` dùng cho mọi dịch vụ. Thử: `check('openrouter_usd', 0.3)` ở `mr0` → chặn đúng "trần 0, cấm gọi" |
| `tools/preflight.sh` | nguyên văn | chạy ĐẠT trước commit (§5). Bước `tools/k/khoa.py`, `checks/lock.py` tự bỏ qua vì repo chưa có |

**Không chép** `look-A.json`, `do_hoa.py`: đó là nhận diện màu/chữ của Timefall Atlas; bảng màu/phông của Money Reroute là quyết định gu của chủ dự án (§6 câu 3).

## 4. Số dư từng khoá (đọc 01/11/2026 12:36 UTC, không in khoá)
| Dịch vụ | Cách đọc | HTTP | Kết quả |
|---|---|---|---|
| **OpenRouter** | `GET /api/v1/credits`, `GET /api/v1/key` | 200 / 200 | Tài khoản: `total_credits` 70, `total_usage` 61,85476 → **còn ≈ 8,15 USD**. Khoá đang tiêm: `limit` 100, `usage` 0 (khoá mới hoặc chưa dùng) — trần khoá 100 cao hơn số dư tài khoản, nên **số dư thật bị chặn bởi tài khoản (8,15)** |
| **ElevenLabs** | `GET /v1/user/subscription` | 200 | gói `creator`, `active`; đã dùng 527 / 157.382 ký tự → **còn 156.855**; reset 01/12/2026 06:57 UTC |
| Gemini | `GET /v1beta/models` không khoá | 403 | "unregistered callers" — **không có khoá** trong môi trường này |
| YouTube Data | `GET /youtube/v3/videos` không khoá | 403 | như trên — **không có khoá** |
| Claude API | `GET /v1/models` | 401 | **không có khoá** |
| OpenAI | — | — | không có khoá, không gọi |

## 5. Preflight
`bash tools/preflight.sh` trên 19 tệp đã stage trước commit: **`preflight: 19 tệp (staged) — ĐẠT` / `PREFLIGHT ĐẠT`**. Chạy lại `--range origin/main..HEAD` trước khi đẩy.

## 6. Câu hỏi cho điều phối / chủ dự án
1. **HIEN-CHUONG**: duyệt nhãn tầng (● CONVICTED / ◐ ALLEGED / ○ UNVERIFIED) và luật "tin đồn về người có tên: mặc định không dùng" (§3.3)? Khuyến nghị: duyệt — giảm rủi ro bôi nhọ nhiều nhất.
2. **Quỹ OpenRouter dùng chung?** 8,15 USD là số của tài khoản; nếu chung với lost-places-lab (Cusco CU-1/CU-2 ước 27 USD), MR cần quỹ riêng hoặc thứ tự ưu tiên trước khi đặt trần.
3. **Nhận diện kênh** (bảng màu, phông, look) — cần để chạy `ban_do.py`/`mau_look.py`; khuyến nghị quyết ở G1 tập 1, không chép của Timefall Atlas.
4. **Khoá YouTube Data / Gemini** cho MR-1 (đo cầu đề tài, ảnh khung khoá) có cần cấp vào môi trường này không?

## 7. Kết thúc
Commit + đẩy nhánh `claude/money-reroute-init-sj5scm`. **DỪNG** — chờ điều phối rà.
