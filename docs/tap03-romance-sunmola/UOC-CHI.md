# ƯỚC CHI + ĐỀ XUẤT TRẦN — `tap03-romance-sunmola`

> MR-K23 · NHÁP G1 · **dựng máy** bằng `python3 scripts/mrk23/uoc_chi.py docs/tap03-romance-sunmola 7 10 15` (đầu vào: `loi.json` + số khe Veo ở `SHOT.md` §2). **MR-K23 chi 0 USD** (không gọi API trả tiền).
> **Đơn giá THẬT đo ở MR-4** (QUY-TRINH §6): Veo 3.1 Lite 1080p clip 8 s **0,40 USD**; **1,5 lượt/khe** (mẫu 2 khe khó); TTS `eleven_v4` **0,4401** ký tự tính / ký tự gửi; nhịp đọc **155 từ/phút**. Nhạc ~825 ký tự/phút = số tham chiếu lost-places, **chưa đo trên MR**.
> Đầu vào đo trên repo: **1741 từ đọc**, **10.766 ký tự gửi TTS/lượt** (sau thay phát âm); khe Veo thấp/giữa/cao = **7 / 10 / 15**.

## 1. Giả định

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| Veo, M-c | 7 khe × 1,2 lượt (khe dễ ~1,0 + biên) | 10 khe × **1,5** lượt (đo MR-4) | 15 khe × 2 lượt (trần V7) |
| TTS (thu lại) | 1 lượt + 10 % | 1 lượt + 30 % | 2 lượt trọn |
| Eleven Music | 3 phút | 4 phút | 6 phút |
| Thử giọng | 0 (giọng kênh, không thử lại) | 0 | 0 |
| Ảnh AI tĩnh | 0 (không có khoá Gemini; bảng shot không cần) | 0 | 0 |
| M-d dựng + kiểm | 0 | 0 | 0 |
| M-e sửa ≤ 2 vòng | 0 khe; 1.000 ký tự gửi | 1 khe × 2 lượt; 2.000 | 2 khe × 2 lượt; 3.000 |

## 2. Ước chi

| Khoản | Thấp | Giữa | Cao |
|---|---|---|---|
| **Veo (OpenRouter), M-c** | 7 × 0,40 × 1,2 = **3,36 USD** | 10 × 0,40 × 1,5 = **6,00 USD** | 15 × 0,40 × 2 = **12,00 USD** |
| Veo, M-e | 0,00 USD | 0,80 USD | 1,60 USD |
| **Tổng OpenRouter** | **3,36 USD** | **6,80 USD** | **13,60 USD** |
| TTS ký tự gửi (M-c) | 11.843 | 13.996 | 21.532 |
| TTS ký tự tính (× 0,4401) | 5.212 | 6.160 | 9.476 |
| Nhạc ký tự | 2.475 | 3.300 | 4.950 |
| M-e TTS ký tự tính | 440 | 880 | 1.320 |
| **Tổng ElevenLabs ký tự tính** | **≈ 8.127** | **≈ 10.340** | **≈ 15.747** |

## 3. Đề xuất trần cứng (dòng `CAPS_PHIEN` cho `scripts/cp/budget.py`, phiên M-c ghi khi có lệnh)

| Mốc | `openrouter_usd` | `elevenlabs_chars` (ký tự **tính**) | Chặn phụ ký tự **gửi** | Mốc báo ~80 % |
|---|---|---|---|---|
| **M-c** (giọng, Veo, nhạc) | **7,50** (mức giữa 6,00 + biên ≈ 25 %) | **12.000** (giữa TTS + nhạc ≈ 9.460 + biên ≈ 25 %) | ≤ 22.000 | Veo 6,00 · ElevenLabs 9.600 |
| **M-d** | **0** | **0** | — | — |
| **M-e** | **1,60** | **2.000** | ≤ 3.000 | 1,28 · 1.600 |
| **Cả tập** | **9,10 USD** | **14.000 ký tự** | | |

Số dư OpenRouter cần trước M-c (V7, quỹ chung với lost-places-lab): ≥ chi ước cả phiên × 1,2 = 6,00 × 1,2 = **7,20 USD** + 1 USD biên kiểm mỗi lượt → **≥ 8,20 USD khả dụng cho MR**, cộng phần các phiên lost-places-lab chạy cùng lúc (không thấy được từ repo này). Đọc lại `/api/v1/credits` ngay trước M-c. Luật đi kèm: V7 ≤ 2 lượt/khe, lượt 2 đổi lời; ≤ 3 lượt song song tính chung mọi phiên cùng tài khoản; **402 → DỪNG**, không vá ảnh tĩnh; chạm ~80 % trần mà còn > 20 % việc → dừng, báo.
