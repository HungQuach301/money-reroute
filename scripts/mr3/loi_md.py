#!/usr/bin/env python3
"""MR-3 (sửa MR-3b) · Kiểm máy + dựng LOI.md từ loi.json (0 USD, không gọi mạng).
  python3 scripts/mr3/loi_md.py docs/tap01-1inmm/loi.json docs/tap01-1inmm/LOI.md
MR-3b: trường "doc" (mặc định true). "doc": false = câu KHÔNG đọc thành lời, chỉ hiện chữ ở "chu" (thẻ trên hình); không tính
  vào số từ/ký tự TTS; tính giữ hình GIU_CHU giây mỗi thẻ vào thời lượng ước.
Kiểm (trượt → mã thoát 1):
  K1 tầng hợp lệ · K2 câu về người/tổ chức thật (●, ●T, ◐, TT, NB, KBCB) có mã nguồn · K3 không chữ số trong lời (TTS)
  K4 đoạn nào nêu HBO/Netflix (lời đọc hoặc chữ trên hình) có câu KBCB trong cùng đoạn, đọc HOẶC hiện chữ (HIEN-CHUONG §3 luật 8e) · K5 câu ◐ có chủ thể nói/cáo buộc
  K6 không nhãn cấm (luật 8d) và không tên khu "Beverlywood" (rà MR-2) · K7 mã nguồn có trong NGUON.md
  K8 (MR-3b) câu "doc": false phải có "chu" không rỗng; câu KBCB hiện chữ phải nêu cả HBO và Netflix + "not accused"
Thống kê: số từ, thời lượng ước ở 140 và 150 từ/phút, số ký tự gửi TTS (sau thay phát âm)."""
import json, re, sys, os

TANG = {"●", "●T", "◐", "TT", "NB", "KBCB", "MH", "CHUNG"}
CAN_NGUON = {"●", "●T", "◐", "TT", "NB", "KBCB"}
CHU_THE = re.compile(r"\b(SEC|prosecutors|Prosecutors|Justice Department|indictment|complaint|they wrote|consent judgment|According to|according to|alleged)\b")
CAM = re.compile(r"(?i)\b(fraudster|con ?man|con artist|scammer|monster|crook|thief|Beverlywood)\b")
PHAT_AM = [(r"\bSEC\b", "S-E-C"), (r"\bFBI\b", "F-B-I"), (r"\bHBO\b", "H-B-O"), (r"\bFINRA\b", "FIN-rah")]
GIU_CHU = 6  # giây giữ một thẻ chữ không đọc (ước)
KBCB_CHU = re.compile(r"(?s)(?=.*\bHBO\b)(?=.*\bNetflix\b)(?=.*not accused)")
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
        doc = c.get("doc", True)
        if not doc and not (c.get("chu") or "").strip(): loi.append(f"K8 {c['id']}: doc=false mà thiếu chu")
        if not doc and c["tang"] == "KBCB" and not KBCB_CHU.search(c.get("chu") or ""): loi.append(f"K8 {c['id']}: thẻ KBCB thiếu HBO/Netflix/not accused")
        if doc and re.search(r"\d", c["loi"]): loi.append(f"K3 {c['id']}: có chữ số trong lời")
        if c["tang"] == "◐" and not CHU_THE.search(c["loi"]): loi.append(f"K5 {c['id']}: ◐ thiếu chủ thể")
        if CAM.search(c["loi"]) or (c.get("chu") and CAM.search(c["chu"])): loi.append(f"K6 {c['id']}: từ cấm")
        for n in c["nguon"]:
            m = re.match(r"(N\d+)", n)
            if m and m.group(1) not in co_ma: loi.append(f"K7 {c['id']}: {m.group(1)} không có trong NGUON.md")
    ten = re.compile(r"\b(HBO|Netflix)\b")
    for k, cs in doan.items():
        neu = any((c.get("doc", True) and ten.search(c["loi"])) or ten.search(c.get("chu") or "") for c in cs if c["tang"] != "KBCB")
        co_kbcb = any(c["tang"] == "KBCB" and (c.get("doc", True) or (c.get("chu") or "").strip()) for c in cs)
        if neu and not co_kbcb:
            loi.append(f"K4 {k}: nêu HBO/Netflix mà không có câu KBCB đọc hoặc hiện chữ")
    doc_cs = [c for c in d["cau"] if c.get("doc", True)]
    n_chu = len(d["cau"]) - len(doc_cs)
    tu = sum(len(c["loi"].split()) for c in doc_cs)
    kt = sum(len(tts(c["loi"])) + 1 for c in doc_cs)
    giu = n_chu * GIU_CHU / 60
    dem = {t: sum(1 for c in d["cau"] if c["tang"] == t) for t in sorted(TANG)}

    L = [f"# LỜI TẬP 1 — 1inMM Capital / Zachary Horwitz (`{d['tap']}`)", "",
         f"> {d['ban']} · ngôn ngữ {d['ngon_ngu']} · ngày chốt lời {d['ngay_chot_loi']} · ngày kiểm trạng thái vụ {d['ngay_kiem_trang_thai']}.",
         "> **Tệp này dựng máy từ `loi.json`** (`python3 scripts/mr3/loi_md.py`); sửa lời ở `loi.json`, không sửa tay tệp này.",
         f"> {d['quy_uoc']}",
         "> Cột **Chữ trên hình** = trích nguyên văn hiện bằng chữ (HIEN-CHUONG §4), đã đối chiếu ảnh trang. Nhãn hình theo tầng: ● → `● CONVICTED`; ◐ → `◐ ALLEGED`; MH → `ILLUSTRATIVE — not a real message/person`; KBCB, CHUNG, TT, NB không nhãn.",
         "", "## Thống kê (máy)", "",
         f"- Số câu: **{len(d['cau'])}** (đọc **{len(doc_cs)}**, chỉ chữ trên hình **{n_chu}**) · số từ đọc: **{tu}** · thời lượng lời ước: **{tu/150:.1f}–{tu/140:.1f} phút** (150–140 từ/phút) + thẻ chữ không đọc {n_chu} × {GIU_CHU} s = {giu:.1f} phút + khoảng nghỉ/chữ trích/nhạc ≈ 1–1,5 phút → **≈ {tu/150+giu+1:.1f}–{tu/140+giu+1.5:.1f} phút**.",
         f"- Ký tự gửi TTS một lượt (sau thay phát âm): **{kt:,}**.".replace(",", "."),
         "- Số câu theo tầng: " + " · ".join(f"{k} {v}" for k, v in dem.items()) + ".",
         f"- Kiểm máy K1–K8: **{'ĐẠT' if not loi else 'TRƯỢT (' + str(len(loi)) + ')'}**." + ("" if not loi else " " + "; ".join(loi)),
         "", "## Lời", ""]
    nhan_doan = {}
    for k, cs in doan.items():
        nhip = sorted({c["nhip"] for c in cs}, key=lambda x: (len(x), x))
        L += [f"### {k} · nhịp {', '.join(nhip)}", "", "| # | Tầng | Đọc | Lời (en-US, số bằng chữ) | Nguồn + trang | Chữ trên hình |", "|---|---|---|---|---|---|"]
        for c in cs:
            dk = "đọc" if c.get("doc", True) else "**chữ, không đọc**"
            lo = c["loi"] if c.get("doc", True) else f"~~{c['loi']}~~ (không thu âm)"
            L.append(f"| {c['id']} | {c['tang']} | {dk} | {lo} | {'; '.join(c['nguon']) or '—'} | {c.get('chu') or ''} |")
        L.append("")
    L += ["## Phát âm (áp ở M-c, không đổi lời)", "", "| Chữ trong lời | Gửi TTS |", "|---|---|"]
    L += [f"| `{a.strip(chr(92)+'b')}` | `{b}` |" for a, b in PHAT_AM]
    L += ["| `one-in-M-M` | giữ nguyên (tên công ty viết `1inMM` chỉ ở chữ trên hình) |", ""]
    open(dst, "w").write("\n".join(L))
    print(json.dumps({"cau": len(d["cau"]), "doc": len(doc_cs), "chu_khong_doc": n_chu, "tu": tu, "ky_tu_tts": kt, "loi": loi}, ensure_ascii=False))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
