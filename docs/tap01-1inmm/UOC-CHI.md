# ƯỚC CHI + ĐỀ XUẤT TRẦN — Tập 1 · `tap01-1inmm`

> MR-3 · 01/11/2026 · NHÁP G1. **MR-3 chi 0 USD** (không gọi API trả tiền).
> **Đơn giá = QUY-TRINH §6, số đo của lost-places-lab, CHƯA đo trên MR** → mọi con số dưới đây là ước; thay bằng số đo thật sau M-c (đọc số dư trước/sau, `COST-LEDGER.csv`).
> Đầu vào đo được trên repo: lời **12.511 ký tự gửi TTS/lượt** (máy đếm từ `loi.json`, sau thay phát âm), **2.049 từ**, ≈ 16 phút; khe Veo theo `SHOT.md` §2 (12 / 16 / 22 khe 8 s).

## 1. Giả định từng mức

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| Veo 3.1 Lite 1080p, clip 8 s = 0,40 USD | 12 khe × 1,1 lượt | 16 khe × 1,2 lượt | 22 khe × 1,5 lượt |
| TTS `eleven_v4` (0,44 ký tự tính / ký tự gửi) | 1 lượt + 10 % thu lại | 1 lượt + 30 % | 2 lượt trọn |
| Thử giọng G1/G2 (2 phương án × ~700 ký tự, đoạn S004–S010) | 1.400 gửi | 1.400 gửi | 1.400 gửi |
| Eleven Music (~825 ký tự/phút) | 3 phút | 4 phút | 6 phút |
| Ảnh AI (NB2.1 Gemini) | 0 — **không có khoá Gemini**; bảng shot không cần ảnh AI tĩnh | 0 | 0 |
| M-d dựng + kiểm | 0 (máy cục bộ) | 0 | 0 |
| M-e sửa ≤ 2 vòng | 0 khe Veo; 1.000 ký tự TTS gửi | 1 khe (0,40 × 2 lượt); 2.000 ký tự | 2 khe (0,80 × 2); 3.000 ký tự |

## 2. Ước chi

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| **Veo (OpenRouter), M-c** | 12 × 0,40 × 1,1 = **5,28 USD** | 16 × 0,40 × 1,2 = **7,68 USD** | 22 × 0,40 × 1,5 = **13,20 USD** |
| Veo, M-e | 0 | 0,80 USD | 1,60 USD |
| **Tổng OpenRouter** | **5,28 USD** | **8,48 USD** | **14,80 USD** |
| TTS ký tự gửi (lời) | 13.762 | 16.264 | 25.022 |
| TTS ký tự gửi (thử giọng) | 1.400 | 1.400 | 1.400 |
| Nhạc ký tự | 2.475 | 3.300 | 4.950 |
| TTS M-e ký tự gửi | 1.000 | 2.000 | 3.000 |
| **ElevenLabs ký tự tính (hệ số 0,44 cho TTS; nhạc tính đủ)** | ≈ 7.110 + 2.475 = **≈ 9.590** | ≈ 8.650 + 3.300 = **≈ 11.950** | ≈ 12.950 + 4.950 = **≈ 17.900** |
| ElevenLabs nếu hệ số thật = 1,0 (chưa đo trên MR) | ≈ 18.640 | ≈ 22.960 | ≈ 34.370 |

Số dư hiện biết (BAN-GIAO §2): OpenRouter **5,45 USD** (chủ dự án báo 01/11/2026 20:08, tài khoản **chung** với lost-places-lab); ElevenLabs **156.855 ký tự** (đọc MR-0, reset 01/12/2026). → OpenRouter **không đủ** cả mức thấp theo V7; ElevenLabs đủ mọi mức.

## 3. Đề xuất trần cứng (dòng `CAPS_PHIEN` cho `scripts/cp/budget.py`, phiên ghi khi có lệnh)

| Mốc | `openrouter_usd` | `elevenlabs_chars` (ký tự **tính**, đọc chênh `/v1/user/subscription`) | Khác | Mốc báo (~80 %) |
|---|---|---|---|---|
| **M-c** (giọng, Veo, nhạc) | **9,50** (mức giữa 7,68 + biên ≈ 24 % cho lượt 2 ngoài ước) | **16.000** (mức giữa M-c ≈ 11.070 ký tự tính; dư cho hệ số chưa đo; chặn phụ: ký tự **gửi** ≤ 24.000) | `gemini_usd` 0, các khoản khác 0 | Veo 7,60 USD · ElevenLabs 12.800 |
| **M-d** (dựng, quét V8, kiểm pháp lý lần 2) | **0** | **0** | 0 | — |
| **M-e** (sửa ≤ 2 vòng, gói phát hành) | **1,60** | **3.000** | 0 | Veo 1,28 · 2.400 |
| **Cả tập** | **11,10 USD** | **19.000 ký tự** | | |

Luật đi kèm (đã có, nhắc lại): V7 ≤ 2 lượt/khe, lượt 2 đổi lời; ≤ 3 lượt song song **tính chung mọi phiên dùng cùng tài khoản**; mỗi lượt kiểm `/credits` ≥ (lượt đang chạy × giá) + 1 USD; **402 → DỪNG**, không vá bằng ảnh tĩnh. Chạm ~80 % trần mà còn > 20 % việc → dừng, báo.

## 4. Số dư OpenRouter cần có trước M-c (V7, quỹ chung)

- V7: số dư ≥ chi ước cả phiên × 1,2 → mức giữa M-c: 7,68 × 1,2 = **9,22 USD**; cộng biên kiểm mỗi lượt (+1 USD) → **≥ 10,3 USD khả dụng cho MR**.
- Quỹ **chung** với lost-places-lab: số dư phải cộng thêm phần các phiên lost-places-lab chạy **cùng lúc** (không thấy được từ repo này) → điều phối/chủ dự án xác nhận không có phiên Veo song song, hoặc cộng phần đó.
- Hiện 5,45 USD → **nạp tối thiểu ≈ 5 USD** (lên ≥ 10,5 USD) cho mức giữa; **khuyến nghị nạp lên ≥ 15 USD** để chịu được mức cao (13,20 × 1,2 = 15,84) hoặc trần M-c 9,50 + M-e 1,60 với biên. Đọc lại `/api/v1/credits` ngay trước M-c.
