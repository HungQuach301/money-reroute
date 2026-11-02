# ƯỚC CHI + ĐỀ XUẤT TRẦN — `tap03-romance-sunmola` (phong cách PHONG-CACH-HINH v1)

> MR-S23 · 02/11/2026 · **dựng máy** `python3 scripts/mrs23/uoc_chi.py tap03` từ `loi.json` + `SHOT2.md` (`reports/mrs23/shot2_tap03.json`). **Thay** bản MR-K23 (bản đó tính Veo tả thực 10 khe, không có tranh). **MR-S23 chi 0 USD.**
> **Đơn giá đo thật** (`docs/BAI-HOC.md` tập 1): tranh Nano Banana 2.1 16:9 1K **0,0389 USD**, sinh lại ~5 %; Veo 3.1 Lite 1080p 8 s **0,40 USD × 1,44 lượt/khe**; TTS `eleven_v4` **0,4401** ký tự tính / ký tự gửi; nhạc **825 ký tự/phút**; nhịp **155 từ/phút**.
> Đầu vào đo trên repo: **1735 từ đọc**, **10.752 ký tự gửi TTS/lượt**; SHOT2: **144 tranh mới** + 2 tham chiếu, **5 khoảnh khắc ảnh→clip**, 17 đồ hoạ L2 + 5 L3 (mã, 0 USD); thời lượng ước 12:21.

## 1. Giả định

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| Tranh L1 | 144 + 2 ref, sinh lại 5 % | + 10% tranh chen ở dựng, sinh lại 5 % | + 40% tranh chen (gần mật độ ~190/tập), sinh lại 15 % |
| Veo ảnh→clip | 5 khe × 1,0 lượt | 5 × **1,44** lượt (đo tập 1) | 5 × 2 lượt (trần V7) |
| TTS | 1 lượt + 10 % thu lại | 1 lượt + 30 % | 2 lượt trọn |
| Nhạc | 3 phút | 4 phút (tập 1: 236 s) | 6 phút |
| L2, L3, dựng, phụ đề, kiểm | 0 (mã) | 0 | 0 |

## 2. Ước chi

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| Tranh (số tranh tính tiền) | 153 → **5,96 USD** | 168 → **6,55 USD** | 234 → **9,11 USD** |
| Veo | **2,00 USD** | **2,88 USD** | **4,00 USD** |
| **Tổng OpenRouter** | **7,96 USD** | **9,43 USD** | **13,11 USD** |
| TTS ký tự gửi | 11.827 | 13.978 | 21.504 |
| TTS ký tự tính (× 0,4401) | 5.205 | 6.152 | 9.464 |
| Nhạc ký tự tính | 2.475 | 3.300 | 4.950 |
| **Tổng ElevenLabs ký tự tính** | **≈ 7.680** | **≈ 9.452** | **≈ 14.414** |

So với tập 1 (BAI-HOC): 18,31 USD OpenRouter (gồm 9,20 USD Veo tả thực bị bỏ) và 9.354 ký tự; ước tập sau cùng khuôn ≈ 9–11 USD + 9.000–10.000 ký tự. Số tranh ít hơn tập 1 (166) vì lệnh giới hạn **1–3 cảnh/câu** (tập 1 có câu 4–5 cảnh); nếu điều phối muốn đúng mật độ ~190 tranh, dùng mức cao.

## 3. Đề xuất trần — MỘT phiên M-c+M-d (giọng → tranh → đồ hoạ → dựng → kiểm → gói), BAI-HOC mục 9

| Khoản | Trần cứng | Mốc báo ~80 % | Chặn phụ | Căn cứ |
|---|---|---|---|---|
| `openrouter_usd` | **11,80** | 9,44 | Veo ≤ 5 khe, ≤ 2 lượt/khe | mức giữa 9,43 + biên ≈ 25 % |
| `elevenlabs_chars` (ký tự **tính**) | **12.000** | 9.600 | ký tự **gửi** ≤ 22.000 | mức giữa ≈ 9.452 + biên ≈ 25 % |
| Khoản khác (gemini, claude, openai, youtube) | **0** | — | — | không cần |

Dòng gợi ý cho `scripts/cp/budget.py` (phiên M-c+M-d **thêm khi có lệnh**, không thêm ở MR-S23): `"<mã phiên>": {"openrouter_usd": 11.80, "elevenlabs_chars": 12000}` · `DUNG_BAO_PHIEN`: `{"openrouter_usd": 9.44, "elevenlabs_chars": 9600}` · `TRAN_GUI_PHIEN`: `{"elevenlabs_chars": 22000}`.

**Điều kiện số dư** (BAI-HOC mục 6): trần phiên ≤ số dư thực − 20 % → cần **≥ 14,75 USD** OpenRouter khả dụng cho MR (sau khi trừ kế hoạch lost-places, quỹ chung) và ≥ 15.000 ký tự ElevenLabs (gói reset 01/12/2026). Đọc `/api/v1/credits` và `/v1/user/subscription` trước mỗi lượt. **402 ở bất kỳ dịch vụ nào → DỪNG**, không vá bằng ảnh tĩnh; chạm 80 % mà còn > 20 % việc → dừng sinh, báo.
