#!/usr/bin/env python3
"""MR-K23 · Dựng UOC-CHI.md (ước chi 3 mức + đề xuất trần) từ loi.json + số khe Veo của SHOT.md §2 (0 USD, không gọi mạng).
  python3 scripts/mrk23/uoc_chi.py docs/tap02-irs-callcenter-patel 7 10 15
Đơn giá THẬT MR-4 (QUY-TRINH §6): Veo 3.1 Lite 1080p 8 s = 0,40 USD/clip; 1,5 lượt/khe (đo trên 2 khe khó); TTS 0,4401 ký tự
tính / ký tự gửi; nhịp đọc 155 từ/phút. Nhạc ~825 ký tự/phút (tham chiếu lost-places, CHƯA đo trên MR).
Mức thấp dùng 1,2 lượt/khe (khe dễ ~1,0 theo §6, cộng biên); cao = 2 lượt/khe (trần V7)."""
import json, re, sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from loi_md import tts  # noqa: E402

GIA, HS = 0.40, 0.4401
LUOT = (1.2, 1.5, 2.0)
TTS_THEM = (0.10, 0.30, 1.00)       # thu lại: +10 % / +30 % / 2 lượt trọn
NHAC_PHUT = (3, 4, 6); NHAC_KT = 825
ME_VEO = (0.0, 0.80, 1.60); ME_GUI = (1000, 2000, 3000)


def vn(x, nd=2):
    s = f"{x:,.{nd}f}" if nd else f"{round(x):,}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def main(thu_muc, k_thap, k_giua, k_cao):
    d = json.load(open(os.path.join(thu_muc, "loi.json")))
    doc = [c for c in d["cau"] if c.get("doc", True)]
    gui = sum(len(tts(c["loi"])) + 1 for c in doc); tu = sum(len(c["loi"].split()) for c in doc)
    khe = (k_thap, k_giua, k_cao)
    veo = [k * GIA * l for k, l in zip(khe, LUOT)]
    gui_m = [gui * (1 + t) for t in TTS_THEM]
    tinh_tts = [g * HS for g in gui_m]
    nhac = [p * NHAC_KT for p in NHAC_PHUT]
    me_tinh = [g * HS for g in ME_GUI]
    tong_or = [a + b for a, b in zip(veo, ME_VEO)]
    tong_el = [a + b + c for a, b, c in zip(tinh_tts, nhac, me_tinh)]
    # trần: mức giữa + biên ≈ 25 %, làm tròn lên 0,10 USD / 500 ký tự
    tran_veo = math.ceil(veo[1] * 1.25 * 10) / 10
    tran_el = math.ceil((tinh_tts[1] + nhac[1]) * 1.25 / 500) * 500
    tran_gui = math.ceil(gui_m[2] / 1000) * 1000
    tran_me_el = 2000
    L = [f"# ƯỚC CHI + ĐỀ XUẤT TRẦN — `{d['tap']}`", "",
         "> MR-K23 · NHÁP G1 · **dựng máy** bằng `python3 scripts/mrk23/uoc_chi.py " + thu_muc + f" {k_thap} {k_giua} {k_cao}` (đầu vào: `loi.json` + số khe Veo ở `SHOT.md` §2). **MR-K23 chi 0 USD** (không gọi API trả tiền).",
         "> **Đơn giá THẬT đo ở MR-4** (QUY-TRINH §6): Veo 3.1 Lite 1080p clip 8 s **0,40 USD**; **1,5 lượt/khe** (mẫu 2 khe khó); TTS `eleven_v4` **0,4401** ký tự tính / ký tự gửi; nhịp đọc **155 từ/phút**. Nhạc ~825 ký tự/phút = số tham chiếu lost-places, **chưa đo trên MR**.",
         f"> Đầu vào đo trên repo: **{tu} từ đọc**, **{vn(gui, 0)} ký tự gửi TTS/lượt** (sau thay phát âm); khe Veo thấp/giữa/cao = **{k_thap} / {k_giua} / {k_cao}**.", "",
         "## 1. Giả định", "", "| Khoản | Thấp | Giữa | Cao |", "|---|---|---|---|",
         f"| Veo, M-c | {k_thap} khe × 1,2 lượt (khe dễ ~1,0 + biên) | {k_giua} khe × **1,5** lượt (đo MR-4) | {k_cao} khe × 2 lượt (trần V7) |",
         "| TTS (thu lại) | 1 lượt + 10 % | 1 lượt + 30 % | 2 lượt trọn |",
         "| Eleven Music | 3 phút | 4 phút | 6 phút |",
         "| Thử giọng | 0 (giọng kênh, không thử lại) | 0 | 0 |",
         "| Ảnh AI tĩnh | 0 (không có khoá Gemini; bảng shot không cần) | 0 | 0 |",
         "| M-d dựng + kiểm | 0 | 0 | 0 |",
         "| M-e sửa ≤ 2 vòng | 0 khe; 1.000 ký tự gửi | 1 khe × 2 lượt; 2.000 | 2 khe × 2 lượt; 3.000 |", "",
         "## 2. Ước chi", "", "| Khoản | Thấp | Giữa | Cao |", "|---|---|---|---|",
         f"| **Veo (OpenRouter), M-c** | {k_thap} × 0,40 × 1,2 = **{vn(veo[0])} USD** | {k_giua} × 0,40 × 1,5 = **{vn(veo[1])} USD** | {k_cao} × 0,40 × 2 = **{vn(veo[2])} USD** |",
         f"| Veo, M-e | {vn(ME_VEO[0])} USD | {vn(ME_VEO[1])} USD | {vn(ME_VEO[2])} USD |",
         f"| **Tổng OpenRouter** | **{vn(tong_or[0])} USD** | **{vn(tong_or[1])} USD** | **{vn(tong_or[2])} USD** |",
         f"| TTS ký tự gửi (M-c) | {vn(gui_m[0], 0)} | {vn(gui_m[1], 0)} | {vn(gui_m[2], 0)} |",
         f"| TTS ký tự tính (× 0,4401) | {vn(tinh_tts[0], 0)} | {vn(tinh_tts[1], 0)} | {vn(tinh_tts[2], 0)} |",
         f"| Nhạc ký tự | {vn(nhac[0], 0)} | {vn(nhac[1], 0)} | {vn(nhac[2], 0)} |",
         f"| M-e TTS ký tự tính | {vn(me_tinh[0], 0)} | {vn(me_tinh[1], 0)} | {vn(me_tinh[2], 0)} |",
         f"| **Tổng ElevenLabs ký tự tính** | **≈ {vn(tong_el[0], 0)}** | **≈ {vn(tong_el[1], 0)}** | **≈ {vn(tong_el[2], 0)}** |", "",
         "## 3. Đề xuất trần cứng (dòng `CAPS_PHIEN` cho `scripts/cp/budget.py`, phiên M-c ghi khi có lệnh)", "",
         "| Mốc | `openrouter_usd` | `elevenlabs_chars` (ký tự **tính**) | Chặn phụ ký tự **gửi** | Mốc báo ~80 % |", "|---|---|---|---|---|",
         f"| **M-c** (giọng, Veo, nhạc) | **{vn(tran_veo)}** (mức giữa {vn(veo[1])} + biên ≈ 25 %) | **{vn(tran_el, 0)}** (giữa TTS + nhạc ≈ {vn(tinh_tts[1] + nhac[1], 0)} + biên ≈ 25 %) | ≤ {vn(tran_gui, 0)} | Veo {vn(tran_veo * 0.8)} · ElevenLabs {vn(tran_el * 0.8, 0)} |",
         "| **M-d** | **0** | **0** | — | — |",
         f"| **M-e** | **{vn(ME_VEO[2])}** | **{vn(tran_me_el, 0)}** | ≤ 3.000 | {vn(ME_VEO[2] * 0.8)} · {vn(tran_me_el * 0.8, 0)} |",
         f"| **Cả tập** | **{vn(tran_veo + ME_VEO[2])} USD** | **{vn(tran_el + tran_me_el, 0)} ký tự** | | |", "",
         f"Số dư OpenRouter cần trước M-c (V7, quỹ chung với lost-places-lab): ≥ chi ước cả phiên × 1,2 = {vn(veo[1])} × 1,2 = **{vn(veo[1] * 1.2)} USD** + 1 USD biên kiểm mỗi lượt → **≥ {vn(veo[1] * 1.2 + 1)} USD khả dụng cho MR**, cộng phần các phiên lost-places-lab chạy cùng lúc (không thấy được từ repo này). Đọc lại `/api/v1/credits` ngay trước M-c. Luật đi kèm: V7 ≤ 2 lượt/khe, lượt 2 đổi lời; ≤ 3 lượt song song tính chung mọi phiên cùng tài khoản; **402 → DỪNG**, không vá ảnh tĩnh; chạm ~80 % trần mà còn > 20 % việc → dừng, báo.", ""]
    open(os.path.join(thu_muc, "UOC-CHI.md"), "w").write("\n".join(L))
    print(json.dumps({"tu": tu, "gui": gui, "veo": veo, "tong_or": tong_or, "tong_el": [round(x) for x in tong_el], "tran_veo": tran_veo, "tran_el": tran_el, "tran_gui": tran_gui}))


if __name__ == "__main__":
    main(sys.argv[1], *map(int, sys.argv[2:5]))
