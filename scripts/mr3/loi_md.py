#!/usr/bin/env python3
"""MR-3 · Kiểm máy + dựng LOI.md từ loi.json (0 USD, không gọi mạng).
  python3 scripts/mr3/loi_md.py docs/tap01-1inmm/loi.json docs/tap01-1inmm/LOI.md
Kiểm (trượt → mã thoát 1):
  K1 tầng hợp lệ · K2 câu về người/tổ chức thật (●, ●T, ◐, TT, NB, KBCB) có mã nguồn · K3 không chữ số trong lời (TTS)
  K4 đoạn nào nêu HBO/Netflix có câu KBCB trong cùng đoạn (HIEN-CHUONG §3 luật 8e) · K5 câu ◐ có chủ thể nói/cáo buộc
  K6 không nhãn cấm (luật 8d) và không tên khu "Beverlywood" (rà MR-2) · K7 mã nguồn có trong NGUON.md
Thống kê: số từ, thời lượng ước ở 140 và 150 từ/phút, số ký tự gửi TTS (sau thay phát âm)."""
import json, re, sys, os

TANG = {"●", "●T", "◐", "TT", "NB", "KBCB", "MH", "CHUNG"}
CAN_NGUON = {"●", "●T", "◐", "TT", "NB", "KBCB"}
CHU_THE = re.compile(r"\b(SEC|prosecutors|Prosecutors|Justice Department|indictment|complaint|they wrote|consent judgment|According to|according to|alleged)\b")
CAM = re.compile(r"(?i)\b(fraudster|con ?man|con artist|scammer|monster|crook|thief|Beverlywood)\b")
PHAT_AM = [(r"\bSEC\b", "S-E-C"), (r"\bFBI\b", "F-B-I"), (r"\bHBO\b", "H-B-O"), (r"\bFINRA\b", "FIN-rah")]
TANG_EN = {"●": "● CONVICTED", "●T": "● CONVICTED · admitted in plea", "◐": "◐ ALLEGED", "TT": "", "NB": "", "KBCB": "", "MH": "ILLUSTRATIVE", "CHUNG": ""}


def tts(s):
    for a, b in PHAT_AM:
        s = re.sub(a, b, s)
    return s


def main(src, dst):
    d = json.load(open(src))
    root = os.path.dirname(os.path.abspath(src))
    nguon_md = open(os.path.join(root, "NGUON.md")).read()
    co_ma = set(re.findall(r"^\| (N\d+) \|", nguon_md, re.M))
    loi, ids = [], set()
    doan = {}
    for c in d["cau"]:
        doan.setdefault(c["doan"], []).append(c)
        if c["id"] in ids: loi.append(f"{c['id']}: trùng id")
        ids.add(c["id"])
        if c["tang"] not in TANG: loi.append(f"K1 {c['id']}: tầng lạ {c['tang']}")
        if c["tang"] in CAN_NGUON and not c["nguon"]: loi.append(f"K2 {c['id']}: thiếu nguồn")
        if re.search(r"\d", c["loi"]): loi.append(f"K3 {c['id']}: có chữ số trong lời")
        if c["tang"] == "◐" and not CHU_THE.search(c["loi"]): loi.append(f"K5 {c['id']}: ◐ thiếu chủ thể")
        if CAM.search(c["loi"]) or (c.get("chu") and CAM.search(c["chu"])): loi.append(f"K6 {c['id']}: từ cấm")
        for n in c["nguon"]:
            m = re.match(r"(N\d+)", n)
            if m and m.group(1) not in co_ma: loi.append(f"K7 {c['id']}: {m.group(1)} không có trong NGUON.md")
    for k, cs in doan.items():
        if any(re.search(r"\b(HBO|Netflix)\b", c["loi"]) for c in cs if c["tang"] != "KBCB") and not any(c["tang"] == "KBCB" for c in cs):
            loi.append(f"K4 {k}: nêu HBO/Netflix mà không có câu KBCB")
    tu = sum(len(c["loi"].split()) for c in d["cau"])
    kt = sum(len(tts(c["loi"])) + 1 for c in d["cau"])
    dem = {t: sum(1 for c in d["cau"] if c["tang"] == t) for t in sorted(TANG)}

    L = [f"# LỜI TẬP 1 — 1inMM Capital / Zachary Horwitz (`{d['tap']}`)", "",
         f"> {d['ban']} · ngôn ngữ {d['ngon_ngu']} · ngày chốt lời {d['ngay_chot_loi']} · ngày kiểm trạng thái vụ {d['ngay_kiem_trang_thai']}.",
         "> **Tệp này dựng máy từ `loi.json`** (`python3 scripts/mr3/loi_md.py`); sửa lời ở `loi.json`, không sửa tay tệp này.",
         f"> {d['quy_uoc']}",
         "> Cột **Chữ trên hình** = trích nguyên văn hiện bằng chữ (HIEN-CHUONG §4), đã đối chiếu ảnh trang. Nhãn hình theo tầng: ● → `● CONVICTED`; ◐ → `◐ ALLEGED`; MH → `ILLUSTRATIVE — not a real message/person`; KBCB, CHUNG, TT, NB không nhãn.",
         "", "## Thống kê (máy)", "",
         f"- Số câu: **{len(d['cau'])}** · số từ: **{tu}** · thời lượng lời ước: **{tu/150:.1f}–{tu/140:.1f} phút** (150–140 từ/phút) + khoảng nghỉ/chữ trích/nhạc ≈ 1–1,5 phút → **≈ {tu/150+1:.0f}–{tu/140+1.5:.0f} phút**.",
         f"- Ký tự gửi TTS một lượt (sau thay phát âm): **{kt:,}**.".replace(",", "."),
         "- Số câu theo tầng: " + " · ".join(f"{k} {v}" for k, v in dem.items()) + ".",
         f"- Kiểm máy K1–K7: **{'ĐẠT' if not loi else 'TRƯỢT (' + str(len(loi)) + ')'}**." + ("" if not loi else " " + "; ".join(loi)),
         "", "## Lời", ""]
    nhan_doan = {}
    for k, cs in doan.items():
        nhip = sorted({c["nhip"] for c in cs}, key=lambda x: (len(x), x))
        L += [f"### {k} · nhịp {', '.join(nhip)}", "", "| # | Tầng | Lời (en-US, số bằng chữ) | Nguồn + trang | Chữ trên hình |", "|---|---|---|---|---|"]
        for c in cs:
            L.append(f"| {c['id']} | {c['tang']} | {c['loi']} | {'; '.join(c['nguon']) or '—'} | {c.get('chu') or ''} |")
        L.append("")
    L += ["## Phát âm (áp ở M-c, không đổi lời)", "", "| Chữ trong lời | Gửi TTS |", "|---|---|"]
    L += [f"| `{a.strip(chr(92)+'b')}` | `{b}` |" for a, b in PHAT_AM]
    L += ["| `one-in-M-M` | giữ nguyên (tên công ty viết `1inMM` chỉ ở chữ trên hình) |", ""]
    open(dst, "w").write("\n".join(L))
    print(json.dumps({"cau": len(d["cau"]), "tu": tu, "ky_tu_tts": kt, "loi": loi}, ensure_ascii=False))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
