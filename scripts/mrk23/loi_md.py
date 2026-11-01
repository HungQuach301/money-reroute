#!/usr/bin/env python3
"""MR-K23 · Kiểm máy + dựng LOI.md từ loi.json cho mọi tập (0 USD, không gọi mạng).
Khuôn: scripts/mr3/loi_md.py (MR-3b, tập 1). Tổng quát hoá: luật riêng từng tập đọc từ khoá "kiem_rieng" trong loi.json.
  python3 scripts/mrk23/loi_md.py docs/tap02-irs-callcenter-patel/loi.json docs/tap02-irs-callcenter-patel/LOI.md
Trường câu: id, doan, nhip, tang, loi, nguon[], chu (chữ trên hình | null), doc (mặc định true; false = chỉ thẻ chữ, không thu âm).
Kiểm chung (trượt → mã thoát 1):
  K1 tầng hợp lệ · K2 câu về người/tổ chức thật có mã nguồn · K3 không chữ số trong lời đọc (TTS)
  K5 câu ◐ có chủ thể nói/cáo buộc; câu ●T có chủ thể thừa nhận/DOJ; câu ●C ĐỌC có chủ thể toà (hoặc nối ngay sau câu ●C có chủ thể, cùng đoạn; thẻ chữ doc=false mang dòng nguồn trên hình)
  K6 không nhãn cấm (luật 8d) trong lời và chữ trên hình · K7 mã nguồn có trong NGUON.md · K8 câu doc=false phải có chu
Kiểm riêng ("kiem_rieng"):
  KA "kem_doan": mỗi đoạn có câu khớp "ten" (lời đọc hoặc chu; chỉ xét câu thuộc "tang_xet" nếu có) phải có câu khớp "can"
      (lời đọc hoặc chu). Dùng cho câu "không liên quan" của cơ quan bị mạo danh (luật 8e).
  KB "kem_moi_lan": mỗi đoạn có "ten" trong lời đọc phải có một câu ĐỌC khớp "can_loi"; mỗi chu có "ten" phải tự khớp "can_chu";
      tệp SHOT.md (nếu có) mỗi dòng có "ten" phải khớp "can_shot". (Tập 2: HGLOBAL — quyết định chủ dự án MR-5.)
  KC "dung_mot": đúng MỘT câu trong cả tập (lời + chu) khớp "ten"; câu đó phải doc=false (chỉ thẻ chữ) nếu "chi_the";
      SHOT.md khớp "ten" ≤ 1 dòng. (Tập 3: ảnh riêng tư — K3 MR-D23.)
  KD "cam_them": regex cấm thêm của tập (lời + chu).
Thống kê: số từ, thời lượng ước ở 155 từ/phút (đo thật MR-4) và 145, số ký tự gửi TTS (sau thay phát âm)."""
import json, re, sys, os

TANG = {"●", "●T", "●N", "●C", "◐", "TT", "NB", "KBCB", "MH", "CHUNG"}
CAN_NGUON = {"●", "●T", "●N", "●C", "◐", "TT", "NB", "KBCB"}
CHU_THE = re.compile(r"\b(SEC|[Pp]rosecutors|Justice Department|indictment|complaint|they wrote|consent judgment|[Aa]ccording to|alleged|charged)\b")
CHU_THE_T = re.compile(r"\b(admitted|admit|admissions?|plea|Justice Department)\b")
CHU_THE_C = re.compile(r"\b(court|[Jj]udge|appeals|the court wrote|Seventh Circuit)\b")
CAM = re.compile(r"(?i)\b(fraudster|con ?man|con artist|scammer|scam artist|monster|crook|thief|thieves|swindler|predator)\b")
PHAT_AM = [(r"\bSEC\b", "S-E-C"), (r"\bFBI\b", "F-B-I"), (r"\bIRS\b", "I-R-S"), (r"\bFTC\b", "F-T-C"), (r"\bTIGTA\b", "TIG-tah"),
           (r"\bHGLOBAL\b", "H-Global")]
GIU_CHU = 6  # giây giữ một thẻ chữ không đọc (ước)
WPM = (155, 145)  # 155 = nhịp đọc thật MR-4 (QUY-TRINH §6); 145 = giả định SHOT tập 1


def tts(s):
    for a, b in PHAT_AM:
        s = re.sub(a, b, s)
    return s


def chu_doc(c):
    """Các chuỗi 'hiện ra' của câu: lời nếu đọc, cộng chữ trên hình."""
    out = []
    if c.get("doc", True): out.append(c["loi"])
    if c.get("chu"): out.append(c["chu"])
    return out


def main(src, dst):
    d = json.load(open(src))
    root = os.path.dirname(os.path.abspath(src))
    nguon_md = open(os.path.join(root, "NGUON.md")).read()
    shot_p = os.path.join(root, "SHOT.md")
    shot = open(shot_p).read().split("\n") if os.path.exists(shot_p) else None
    co_ma = set(re.findall(r"^\| (N\d+) \|", nguon_md, re.M))
    kr = d.get("kiem_rieng", {})
    loi, ids, doan = [], set(), {}
    truoc = None
    for c in d["cau"]:
        doan.setdefault(c["doan"], []).append(c)
        if c["id"] in ids: loi.append(f"{c['id']}: trùng id")
        ids.add(c["id"])
        t = c["tang"]
        if t not in TANG: loi.append(f"K1 {c['id']}: tầng lạ {t}")
        if t in CAN_NGUON and not c["nguon"]: loi.append(f"K2 {c['id']}: thiếu nguồn")
        doc = c.get("doc", True)
        if not doc and not (c.get("chu") or "").strip(): loi.append(f"K8 {c['id']}: doc=false mà thiếu chu")
        if doc and re.search(r"\d", c["loi"]): loi.append(f"K3 {c['id']}: có chữ số trong lời")
        if t == "◐" and not CHU_THE.search(c["loi"]): loi.append(f"K5 {c['id']}: ◐ thiếu chủ thể")
        if t == "●T" and not CHU_THE_T.search(c["loi"]): loi.append(f"K5 {c['id']}: ●T thiếu chủ thể thừa nhận/DOJ")
        if t == "●C" and doc:
            ok = CHU_THE_C.search(c["loi"]) or (truoc and truoc["tang"] == "●C" and truoc["doan"] == c["doan"] and truoc.get("_ok"))
            c["_ok"] = bool(ok)
            if not ok: loi.append(f"K5 {c['id']}: ●C thiếu chủ thể toà")
        for s in [c["loi"], c.get("chu") or ""]:
            if CAM.search(s): loi.append(f"K6 {c['id']}: từ cấm '{CAM.search(s).group(0)}'")
        for pat in kr.get("cam_them", []):
            for s in [c["loi"], c.get("chu") or ""]:
                if re.search(pat, s): loi.append(f"KD {c['id']}: khớp regex cấm của tập /{pat}/")
        for n in c["nguon"]:
            m = re.match(r"(N\d+)", n)
            if m and m.group(1) not in co_ma: loi.append(f"K7 {c['id']}: {m.group(1)} không có trong NGUON.md")
        truoc = c
    # KA — câu đi kèm theo đoạn
    for r in kr.get("kem_doan", []):
        ten, can = re.compile(r["ten"]), re.compile(r["can"])
        tx = set(r.get("tang_xet", TANG))
        for k, cs in doan.items():
            neu = any(ten.search(s) for c in cs if c["tang"] in tx for s in chu_doc(c))
            co = any(can.search(s) for c in cs for s in chu_doc(c))
            if neu and not co: loi.append(f"KA {k}: nêu /{r['ten']}/ mà không có câu /{r['can']}/ ({r.get('mo_ta', '')})")
    # KB — kèm mỗi lần nêu (lời + hình + SHOT)
    for r in kr.get("kem_moi_lan", []):
        ten = re.compile(r["ten"]); cl = re.compile(r["can_loi"]); cc = re.compile(r["can_chu"]); cs_ = re.compile(r["can_shot"])
        for k, cs in doan.items():
            if any(c.get("doc", True) and ten.search(c["loi"]) for c in cs):
                if not any(c.get("doc", True) and cl.search(c["loi"]) for c in cs):
                    loi.append(f"KB {k}: nêu {r['ten']} trong lời mà đoạn không có câu ĐỌC kèm ({r.get('mo_ta', '')})")
            if any(ten.search(s) for c in cs for s in chu_doc(c)) and not any(cl.search(s) or cc.search(s) for c in cs for s in chu_doc(c)):
                loi.append(f"KB {k}: đoạn có {r['ten']} mà không có câu kèm")
            for c in cs:
                if c.get("chu") and ten.search(c["chu"]) and not cc.search(c["chu"]):
                    loi.append(f"KB {c['id']}: chữ trên hình có {r['ten']} mà không kèm câu ◐ trên hình")
        if shot is not None:
            for i, ln in enumerate(shot, 1):
                if ten.search(ln) and not cs_.search(ln):
                    loi.append(f"KB SHOT.md dòng {i}: có {r['ten']} mà không kèm câu ◐")
    # KC — đúng một câu
    for r in kr.get("dung_mot", []):
        ten = re.compile(r["ten"])
        khop = [c for c in d["cau"] if any(ten.search(s) for s in [c["loi"], c.get("chu") or ""])]
        if len(khop) != 1: loi.append(f"KC: /{r['ten']}/ khớp {len(khop)} câu ({', '.join(c['id'] for c in khop)}), phải đúng 1")
        for c in khop:
            if r.get("chi_the") and c.get("doc", True): loi.append(f"KC {c['id']}: phải là thẻ chữ (doc=false)")
        if shot is not None:
            n = sum(1 for ln in shot if ten.search(ln))
            if n > 1: loi.append(f"KC SHOT.md: /{r['ten']}/ xuất hiện {n} dòng, tối đa 1")
    doc_cs = [c for c in d["cau"] if c.get("doc", True)]
    n_chu = len(d["cau"]) - len(doc_cs)
    tu = sum(len(c["loi"].split()) for c in doc_cs)
    kt = sum(len(tts(c["loi"])) + 1 for c in doc_cs)
    giu = n_chu * GIU_CHU / 60
    dem = {t: sum(1 for c in d["cau"] if c["tang"] == t) for t in sorted(TANG)}
    dem = {k: v for k, v in dem.items() if v}

    L = [f"# LỜI {d['tieu_de_md']} (`{d['tap']}`)", "",
         f"> {d['ban']} · ngôn ngữ {d['ngon_ngu']} · ngày chốt lời {d['ngay_chot_loi']} · ngày kiểm trạng thái vụ {d['ngay_kiem_trang_thai']}.",
         "> **Tệp này dựng máy từ `loi.json`** (`python3 scripts/mrk23/loi_md.py`); sửa lời ở `loi.json`, không sửa tay tệp này.",
         f"> {d['quy_uoc']}",
         "> Cột **Chữ trên hình** = trích nguyên văn / thẻ chữ hiện bằng chữ (HIEN-CHUONG §4). Nhãn hình theo tầng: ● → `● CONVICTED`; ●T/●N/●C → `● CONVICTED` kèm chú (admitted per DOJ / co-defendants / per appeals court); ◐ → `◐ ALLEGED`; MH → `ILLUSTRATIVE`; KBCB, CHUNG, TT, NB không nhãn.",
         "", "## Thống kê (máy)", "",
         f"- Số câu: **{len(d['cau'])}** (đọc **{len(doc_cs)}**, chỉ chữ trên hình **{n_chu}**) · số từ đọc: **{tu}** · thời lượng lời: **{tu/WPM[0]:.1f} phút ở {WPM[0]} từ/phút** (nhịp đo thật MR-4; {tu/WPM[1]:.1f} phút ở {WPM[1]}) + thẻ chữ không đọc {n_chu} × {GIU_CHU} s = {giu:.1f} phút → thời lượng tập ước ở `SHOT.md` (thêm nghỉ đoạn, thẻ tổng kết, nguồn/nhạc kết).",
         f"- Ký tự gửi TTS một lượt (sau thay phát âm): **{kt:,}**.".replace(",", "."),
         "- Số câu theo tầng: " + " · ".join(f"{k} {v}" for k, v in dem.items()) + ".",
         f"- Kiểm máy K1–K8 + luật riêng ({', '.join(kr.keys()) or '—'}): **{'ĐẠT' if not loi else 'TRƯỢT (' + str(len(loi)) + ')'}**." + ("" if not loi else " " + "; ".join(loi)),
         "", "## Lời", ""]
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
    for a, b in d.get("phat_am_them", []):
        L.append(f"| `{a}` | {b} |")
    L.append("")
    open(dst, "w").write("\n".join(L))
    print(json.dumps({"cau": len(d["cau"]), "doc": len(doc_cs), "chu_khong_doc": n_chu, "tu": tu, "ky_tu_tts": kt, "loi": loi}, ensure_ascii=False))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
