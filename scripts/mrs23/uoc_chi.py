#!/usr/bin/env python3
"""MR-S23 · Dựng UOC-CHI.md (ước chi 3 mức + đề xuất trần MỘT phiên M-c+M-d, BAI-HOC mục 9) từ loi.json + SHOT2 (0 USD).
  python3 scripts/mrs23/shot2.py tap02 && python3 scripts/mrs23/uoc_chi.py tap02
Đơn giá đo thật (docs/BAI-HOC.md tập 1; PHONG-CACH-HINH §6; QUY-TRINH §6):
  tranh Nano Banana 2.1 16:9 1K 0,0389 USD/tranh, sinh lại ~5 % (MR-P1) · Veo 3.1 Lite 1080p 8 s 0,40 USD/clip × 1,44 lượt/khe ·
  TTS eleven_v4 0,4401 ký tự tính / ký tự gửi · nhạc 825 ký tự tính / phút · nhịp 155 từ/phút.
Ba mức: thấp / giữa / cao (xem bảng giả định trong tệp sinh ra)."""
import json, math, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrk23"))
from loi_md import tts  # noqa: E402

TRANH, VEO, LUOT_GIUA, HS, NHAC_KT = 0.0389, 0.40, 1.44, 0.4401, 825
REF = 2                                   # ref_nv + ref_canh (PHONG-CACH-HINH §4)
SINH_LAI = (0.05, 0.05, 0.15)             # tỉ lệ sinh lại tranh (MR-P1 đo 5 %)
TRANH_THEM = (0.0, 0.10, 0.40)            # tranh chen thêm ở M-d (cao: tiến gần mật độ ~190 tranh/tập của PHONG-CACH-HINH §6)
LUOT = (1.0, LUOT_GIUA, 2.0)              # lượt/khe Veo (cao = trần V7)
TTS_THEM = (0.10, 0.30, 1.00)             # thu lại câu
NHAC_PHUT = (3.0, 4.0, 6.0)               # tập 1 dùng 236 s ≈ 3,9 phút


def vn(x, nd=2):
    s = f"{x:,.{nd}f}" if nd else f"{round(x):,}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def main(tap):
    sh = json.load(open(os.path.join(ROOT, "reports", "mrs23", f"shot2_{tap}.json")))
    thu = os.path.join(ROOT, "docs", sh["tap"])
    d = json.load(open(os.path.join(thu, "loi.json")))
    doc = [c for c in d["cau"] if c.get("doc", True)]
    gui = sum(len(tts(c["loi"])) + 1 for c in doc); tu = sum(len(c["loi"].split()) for c in doc)
    nt, nv = sh["tranh_moi"], len(sh["veo"])
    so_tranh = [(nt * (1 + a) + REF) for a in TRANH_THEM]
    tranh = [n * (1 + s) * TRANH for n, s in zip(so_tranh, SINH_LAI)]
    veo = [nv * VEO * l for l in LUOT]
    or_ = [a + b for a, b in zip(tranh, veo)]
    gui_m = [gui * (1 + t) for t in TTS_THEM]; tts_t = [g * HS for g in gui_m]
    nhac = [p * NHAC_KT for p in NHAC_PHUT]; el = [a + b for a, b in zip(tts_t, nhac)]
    tran_or = math.ceil(or_[1] * 1.25 * 10) / 10
    tran_el = math.ceil(el[1] * 1.25 / 500) * 500
    tran_gui = math.ceil(gui_m[2] / 1000) * 1000
    L = [f"# ƯỚC CHI + ĐỀ XUẤT TRẦN — `{sh['tap']}` (phong cách PHONG-CACH-HINH v1)", "",
         f"> MR-S23 · 02/11/2026 · **dựng máy** `python3 scripts/mrs23/uoc_chi.py {tap}` từ `loi.json` + `SHOT2.md` (`reports/mrs23/shot2_{tap}.json`). **Thay** bản MR-K23 (bản đó tính Veo tả thực 10 khe, không có tranh). **MR-S23 chi 0 USD.**",
         "> **Đơn giá đo thật** (`docs/BAI-HOC.md` tập 1): tranh Nano Banana 2.1 16:9 1K **0,0389 USD**, sinh lại ~5 %; Veo 3.1 Lite 1080p 8 s **0,40 USD × 1,44 lượt/khe**; TTS `eleven_v4` **0,4401** ký tự tính / ký tự gửi; nhạc **825 ký tự/phút**; nhịp **155 từ/phút**.",
         f"> Đầu vào đo trên repo: **{tu} từ đọc**, **{vn(gui, 0)} ký tự gửi TTS/lượt**; SHOT2: **{nt} tranh mới** + {REF} tham chiếu, **{nv} khoảnh khắc ảnh→clip**, {len(sh['l2'])} đồ hoạ L2 + {len(sh['l3'])} L3 (mã, 0 USD); thời lượng ước {sh['tong_s'] // 60:.0f}:{sh['tong_s'] % 60:02.0f}.", "",
         "## 1. Giả định", "", "| Khoản | Thấp | Giữa | Cao |", "|---|---|---|---|",
         f"| Tranh L1 | {nt} + {REF} ref, sinh lại 5 % | + {TRANH_THEM[1]:.0%} tranh chen ở dựng, sinh lại 5 % | + {TRANH_THEM[2]:.0%} tranh chen (gần mật độ ~190/tập), sinh lại 15 % |".replace(".", ","),
         f"| Veo ảnh→clip | {nv} khe × 1,0 lượt | {nv} × **1,44** lượt (đo tập 1) | {nv} × 2 lượt (trần V7) |",
         "| TTS | 1 lượt + 10 % thu lại | 1 lượt + 30 % | 2 lượt trọn |",
         "| Nhạc | 3 phút | 4 phút (tập 1: 236 s) | 6 phút |",
         "| L2, L3, dựng, phụ đề, kiểm | 0 (mã) | 0 | 0 |", "",
         "## 2. Ước chi", "", "| Khoản | Thấp | Giữa | Cao |", "|---|---|---|---|",
         f"| Tranh (số tranh tính tiền) | {vn(so_tranh[0] * 1.05, 0)} → **{vn(tranh[0])} USD** | {vn(so_tranh[1] * 1.05, 0)} → **{vn(tranh[1])} USD** | {vn(so_tranh[2] * 1.15, 0)} → **{vn(tranh[2])} USD** |",
         f"| Veo | **{vn(veo[0])} USD** | **{vn(veo[1])} USD** | **{vn(veo[2])} USD** |",
         f"| **Tổng OpenRouter** | **{vn(or_[0])} USD** | **{vn(or_[1])} USD** | **{vn(or_[2])} USD** |",
         f"| TTS ký tự gửi | {vn(gui_m[0], 0)} | {vn(gui_m[1], 0)} | {vn(gui_m[2], 0)} |",
         f"| TTS ký tự tính (× 0,4401) | {vn(tts_t[0], 0)} | {vn(tts_t[1], 0)} | {vn(tts_t[2], 0)} |",
         f"| Nhạc ký tự tính | {vn(nhac[0], 0)} | {vn(nhac[1], 0)} | {vn(nhac[2], 0)} |",
         f"| **Tổng ElevenLabs ký tự tính** | **≈ {vn(el[0], 0)}** | **≈ {vn(el[1], 0)}** | **≈ {vn(el[2], 0)}** |", "",
         "So với tập 1 (BAI-HOC): 18,31 USD OpenRouter (gồm 9,20 USD Veo tả thực bị bỏ) và 9.354 ký tự; ước tập sau cùng khuôn ≈ 9–11 USD + 9.000–10.000 ký tự. Số tranh ít hơn tập 1 (166) vì lệnh giới hạn **1–3 cảnh/câu** (tập 1 có câu 4–5 cảnh); nếu điều phối muốn đúng mật độ ~190 tranh, dùng mức cao.", "",
         "## 3. Đề xuất trần — MỘT phiên M-c+M-d (giọng → tranh → đồ hoạ → dựng → kiểm → gói), BAI-HOC mục 9", "",
         "| Khoản | Trần cứng | Mốc báo ~80 % | Chặn phụ | Căn cứ |", "|---|---|---|---|---|",
         f"| `openrouter_usd` | **{vn(tran_or)}** | {vn(tran_or * 0.8)} | Veo ≤ {nv} khe, ≤ 2 lượt/khe | mức giữa {vn(or_[1])} + biên ≈ 25 % |",
         f"| `elevenlabs_chars` (ký tự **tính**) | **{vn(tran_el, 0)}** | {vn(tran_el * 0.8, 0)} | ký tự **gửi** ≤ {vn(tran_gui, 0)} | mức giữa ≈ {vn(el[1], 0)} + biên ≈ 25 % |",
         "| Khoản khác (gemini, claude, openai, youtube) | **0** | — | — | không cần |", "",
         f"Dòng gợi ý cho `scripts/cp/budget.py` (phiên M-c+M-d **thêm khi có lệnh**, không thêm ở MR-S23): `\"<mã phiên>\": {{\"openrouter_usd\": {tran_or:.2f}, \"elevenlabs_chars\": {tran_el}}}` · `DUNG_BAO_PHIEN`: `{{\"openrouter_usd\": {tran_or * 0.8:.2f}, \"elevenlabs_chars\": {round(tran_el * 0.8)}}}` · `TRAN_GUI_PHIEN`: `{{\"elevenlabs_chars\": {tran_gui}}}`.",
         "",
         f"**Điều kiện số dư** (BAI-HOC mục 6): trần phiên ≤ số dư thực − 20 % → cần **≥ {vn(tran_or / 0.8)} USD** OpenRouter khả dụng cho MR (sau khi trừ kế hoạch lost-places, quỹ chung) và ≥ {vn(tran_el / 0.8, 0)} ký tự ElevenLabs (gói reset 01/12/2026). Đọc `/api/v1/credits` và `/v1/user/subscription` trước mỗi lượt. **402 ở bất kỳ dịch vụ nào → DỪNG**, không vá bằng ảnh tĩnh; chạm 80 % mà còn > 20 % việc → dừng sinh, báo.", ""]
    open(os.path.join(thu, "UOC-CHI.md"), "w").write("\n".join(L))
    out = {"tap": sh["tap"], "or": [round(x, 2) for x in or_], "el": [round(x) for x in el], "tran_or": tran_or, "tran_el": tran_el, "tran_gui": tran_gui, "gui": gui}
    print(json.dumps(out)); return out


if __name__ == "__main__":
    main(sys.argv[1])
