#!/usr/bin/env python3
"""MR-S23 · BẢNG SHOT 2 (tiền kỳ) theo PHONG-CACH-HINH v1 — khuôn docs/tap01-1inmm/SHOT2.md (scripts/mr6/shot2.py, MR-6).
  python3 scripts/mrs23/shot2.py tap02    → docs/tap02-irs-callcenter-patel/SHOT2.md + reports/mrs23/shot2_tap02.json
  python3 scripts/mrs23/shot2.py tap03    → docs/tap03-romance-sunmola/SHOT2.md   + reports/mrs23/shot2_tap03.json
0 USD, không gọi mạng. Dữ liệu cảnh ở scripts/mrs23/du_lieu_tap02.py / du_lieu_tap03.py.

Khác tập 1: chưa có giọng thật → mốc là ƯỚC từ loi.json (155 từ/phút, đo thật MR-4; nghỉ NGHI s đầu mỗi đoạn; thẻ chữ
không đọc giữ GIU_THE s; thẻ tối riêng giữ GIU_TOI s). Ở M-c/M-d thay bằng mốc whisper (scripts/mr6/moc_cau.py) như tập 1.

Mã cảnh trong dữ liệu:
  "E: mô tả"   tranh L1 mới, cảnh trống / vật (không người)
  "N1: mô tả"  tranh L1 mới có nhân vật đại diện N1 (N2…) — tự nghĩ ra, cố định trong tập, nhãn ILLUSTRATIVE
  "R: mô tả"   tranh L1 mới có NGƯỜI THẬT trong vụ — chỉ bóng / lưng / tay (máy kiểm từ khoá)
  "E#ten: …"   đặt tên gọi cho tranh để dùng lại / làm khung đầu Veo ("tu": "ten")
  "@ten"       dùng lại tranh đã có (lần 2; tối đa 2 lần mỗi tranh — PHONG-CACH-HINH §5)
  "G01" L2 đồ hoạ động · "T01" L3 crop trang hồ sơ · "Q01" L3 thẻ trích nguyên văn nền ngà · "K1" Veo ảnh→clip · "TOI" thẻ tối chỉ chữ
  hậu tố "*1.5" = trọng số thời lượng trong câu.
Máy kiểm (trượt → mã thoát 1): mỗi câu 1–3 cảnh; mã tồn tại; ≥ 6 L2 có câu hỏi + một điểm nhấn; ≤ 5 Veo, khung đầu = tranh
"E" (không người); tranh dùng ≤ 2 lần; cảnh tranh ≥ 1,5 s; tranh "R" có từ khoá bóng/lưng/tay; từ cấm biếm hoạ / mặt; regex cấm của tập
(kiem_rieng.cam_them, KB can_shot, KC ≤ 1 dòng) quét cả tệp SHOT2.md; câu riêng (CHI_TOI) chỉ thẻ tối."""
import importlib, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))
WPM, NGHI, GIU_THE, GIU_TOI, KET_GIU, NGUON_S = 155, 1.5, 4.0, 6.0, 8.0, 20.0
R_OK = re.compile(r"(?i)silhouette|from behind|seen from the back|hands?\b|sleeve|shadow")
CAM_HINH = re.compile(r"(?i)\b(turban|sari|bindi|dashiki|tribal|caricature|accent|exaggerated features|uniform|insignia|logo|seal|badge|flag)\b")
CAM_MAT = re.compile(r"(?i)\b(face|portrait|close-up of (his|her) face)\b")


def mmss(t):
    t = int(round(t)); return f"{t // 60}:{t % 60:02d}"


def tach(s):
    m = re.match(r"^(.*?)\*([\d.]+)$", s.strip())
    return (m.group(1).strip(), float(m.group(2))) if m else (s.strip(), 1.0)


def main(tap):
    D = importlib.import_module(f"du_lieu_{tap}")
    thu = os.path.join(ROOT, "docs", D.THU_MUC)
    d = json.load(open(os.path.join(thu, "loi.json")))
    kr = d.get("kiem_rieng", {})
    loi, tranh, dung, hang, alias = [], {}, {}, [], {}
    t, prev, n = 0.0, None, 0
    cau_ids = [c["id"] for c in d["cau"]]
    for k in D.SC:
        if k not in cau_ids: loi.append(f"SC có {k} không có trong loi.json")
    for c in d["cau"]:
        if c["doan"] != prev: t += NGHI; prev = c["doan"]
        doc = c.get("doc", True)
        dur = len(c["loi"].split()) / WPM * 60 if doc else (GIU_TOI if c["id"] in D.CHI_TOI else GIU_THE)
        sc = D.SC.get(c["id"])
        if not sc: loi.append(f"{c['id']}: chưa có cảnh"); sc = []
        if not 1 <= len(sc) <= 3: loi.append(f"{c['id']}: {len(sc)} cảnh (phải 1–3)")
        if c["id"] in D.CHI_TOI and sc != ["TOI"]: loi.append(f"{c['id']}: câu riêng phải chỉ thẻ tối (TOI)")
        if "TOI" in sc and c["id"] not in D.CHI_TOI: loi.append(f"{c['id']}: TOI chỉ dành cho câu {D.CHI_TOI}")
        items = [tach(s) for s in sc]; tong_w = sum(w for _, w in items) or 1
        out = []
        for s, w in items:
            ds = dur * w / tong_w
            m = re.match(r"^(E|N\d|R)(?:#(\w+))?:(.*)$", s, re.S)
            if m:
                loai, ten_goi, mo = m.group(1), m.group(2), m.group(3); n += 1; ma = f"{D.TIEN_TO}{n:03d}"
                if ten_goi:
                    if ten_goi in alias: loi.append(f"tên gọi trùng #{ten_goi}")
                    alias[ten_goi] = ma
                tranh[ma] = {"loai": loai, "mo_ta": mo.strip(), "cau": [c["id"]]}; dung[ma] = 1
                if loai != "E" and loai not in ("R",) and loai not in D.NV: loi.append(f"{c['id']}: nhân vật {loai} chưa khai ở NV")
                if loai == "R" and not R_OK.search(mo): loi.append(f"{ma}: người thật phải chỉ bóng/lưng/tay")
                if CAM_HINH.search(mo) and not re.search(r"(?i)no (logo|seal|badge|flag|insignia|uniform)|without (logo|seal|badge|flag|insignia|uniform)|plain|unmarked|blank", mo):
                    loi.append(f"{ma}: từ cấm hình '{CAM_HINH.search(mo).group(0)}'")
                if loai == "R" and CAM_MAT.search(mo) and not re.search(r"(?i)no face|faces? (are )?(not|never) (visible|shown)|face hidden|faces out of frame", mo):
                    loi.append(f"{ma}: người thật không được lộ mặt")
                out.append(("L1", ma, ds))
            elif s.startswith("@"):
                ma = alias.get(s[1:], s[1:])
                if ma not in tranh: loi.append(f"{c['id']}: dùng lại {ma} chưa có"); continue
                dung[ma] += 1; tranh[ma]["cau"].append(c["id"]); out.append(("L1", f"{ma}:{dung[ma]}", ds))
            elif s in D.L2: out.append(("L2", s, ds))
            elif s in D.L3: out.append(("L3", s, ds))
            elif s in D.VEO: out.append(("veo", s, ds))
            elif s == "TOI": out.append(("TOI", "thẻ tối", ds))
            else: loi.append(f"{c['id']}: mã lạ {s}")
        for lp, ma, ds in out:
            if lp == "L1" and ds < 1.5: loi.append(f"{c['id']}: cảnh tranh {ma} chỉ {ds:.1f} s (< 1,5 s)")
        ov = list(D.OV.get(c["id"], []))
        if not doc and c["id"] not in D.CHI_TOI: ov.insert(0, ("kbcb" if c["tang"] == "KBCB" else "the", c.get("chu") or ""))
        hang.append({"id": c["id"], "doan": c["doan"], "tang": c["tang"], "doc": doc, "bd": t, "kt": t + dur, "canh": out, "ov": ov})
        t += dur
    t_loi = t; t += KET_GIU + NGUON_S
    for ma, k in dung.items():
        if k > 2: loi.append(f"{ma}: dùng {k} lần (tối đa 2)")
    # L2 / Veo
    l2_dung = sorted({x[1] for h in hang for x in h["canh"] if x[0] == "L2"})
    for g in D.L2:
        v = D.L2[g]
        if not v.get("hoi") or not v.get("nhan"): loi.append(f"{g}: thiếu câu hỏi hoặc điểm nhấn")
    if len([g for g in l2_dung if D.L2[g].get("dong", True)]) < 6: loi.append("ít hơn 6 đồ hoạ L2 động")
    veo_dung = sorted({x[1] for h in hang for x in h["canh"] if x[0] == "veo"})
    if len(D.VEO) > 5 or len(veo_dung) > 5: loi.append("quá 5 khoảnh khắc Veo")
    for k, v in D.VEO.items():
        src = v["tu"] = alias.get(v["tu"], v["tu"])
        if src not in tranh: loi.append(f"{k}: khung đầu {src} không có"); continue
        if tranh[src]["loai"] != "E": loi.append(f"{k}: khung đầu {src} có người (loại {tranh[src]['loai']}) — LUAT-VEO / BAI-HOC 2")
        if re.search(r"(?i)\b(person|people|man|woman|hand|silhouette|figure)\b", v["chuyen_dong"] + " " + v["neo_cuoi"]) and not re.search(r"(?i)no (person|people)|nobody|empty", v["chuyen_dong"] + v["neo_cuoi"]):
            loi.append(f"{k}: lời chuyển động/neo cuối nhắc người")
    for k in D.L3:
        if k not in {x[1] for h in hang for x in h["canh"]}: loi.append(f"{k}: L3 khai mà không dùng")

    # ---------- SHOT2.md ----------
    n_l1 = sum(1 for h in hang for x in h["canh"] if x[0] == "L1"); s_l1 = sum(x[2] for h in hang for x in h["canh"] if x[0] == "L1")
    dem = lambda lp: (sum(1 for h in hang for x in h["canh"] if x[0] == lp), sum(x[2] for h in hang for x in h["canh"] if x[0] == lp))
    n_l2, s_l2 = dem("L2"); n_l3, s_l3 = dem("L3"); n_v, s_v = dem("veo"); n_toi, s_toi = dem("TOI")
    n_canh = n_l1 + n_l2 + n_l3 + n_v + n_toi
    nv_dem = {k: sum(1 for x in tranh.values() if x["loai"] == k) for k in ["E", "R"] + list(D.NV)}
    L = [f"# BẢNG SHOT 2 — {D.TEN} (`{D.THU_MUC}`) · phong cách PHONG-CACH-HINH v1", "",
         f"> MR-S23 · 02/11/2026 · tiền kỳ (0 USD). **Thay `SHOT.md`** (giữ làm lịch sử) cho phần hình; lời đã duyệt G1 (02/11/2026 10:25) + quyết định KBCB áp ở MR-S23. Bảng **sinh máy** `python3 scripts/mrs23/shot2.py {D.TAP}` từ `scripts/mrs23/du_lieu_{D.TAP}.py` + `loi.json`; khuôn `docs/tap01-1inmm/SHOT2.md`.",
         f"> **Mốc là ƯỚC** (chưa có giọng): {WPM} từ/phút (đo thật MR-4), nghỉ {NGHI} s đầu mỗi đoạn, thẻ chữ không đọc {GIU_THE:g} s, thẻ tối riêng {GIU_TOI:g} s. Ở M-c/M-d thay bằng mốc whisper giọng thật (`scripts/mr6/moc_cau.py`) và chia lại thời lượng cảnh theo trọng số; cảnh tranh dài > 5 s tách thành 2 khung cắt/chuyển động của **cùng** tranh (không thêm tranh).",
         f"> Tổng ước **{mmss(t)}** (lời + thẻ {mmss(t_loi)} · thẻ tổng kết {KET_GIU:g} s · nguồn {NGUON_S:g} s) · **{n_canh} cảnh** · L1 tranh {n_l1} cảnh ({s_l1:.0f} s, TB {s_l1 / max(n_l1, 1):.1f} s) từ **{len(tranh)} tranh mới** (cảnh trống/vật {nv_dem['E']} · người thật bóng/lưng/tay {nv_dem['R']} · " + " · ".join(f"{k} {nv_dem[k]}" for k in D.NV) + f") · L2 {n_l2} cảnh ({s_l2:.0f} s) từ **{len(l2_dung)} đồ hoạ động** · L3 {n_l3} cảnh ({s_l3:.0f} s) · Veo ảnh→clip **{len(veo_dung)}** khoảnh khắc ({s_v:.0f} s)" + (f" · thẻ tối {n_toi} ({s_toi:.0f} s)" if n_toi else "") + ".",
         "> Luật áp mọi cảnh: HIEN-CHUONG §4–§5; PHONG-CACH-HINH §1–§5; LUAT-VEO V1–V8 + BAI-HOC tập 1 mục 2; nhãn tầng + dòng nguồn lớp tĩnh góc dưới theo `loi.json`; nhãn ILLUSTRATIVE ở cảnh tranh đầu mỗi đoạn; không chữ trên hình ngoài lời đã duyệt, số liệu hồ sơ, nhãn, nguồn (M-d đối chiếu máy như `scripts/mr6/doi_chieu_chu.py`).",
         ] + [f"> {x}" for x in D.LUAT_RIENG] + ["",
         "## 0. Nhân vật và người trong hình", "", "| Mã | Ai | Cách vẽ (cố định cả tập) | Được / không |", "|---|---|---|---|"]
    for k, v in D.NV.items(): L.append(f"| {k} | {v[0]} | {v[1]} | {v[2]} |")
    for v in D.NGUOI_THAT: L.append(f"| R | {v[0]} | {v[1]} | {v[2]} |")
    L += ["", "Tham chiếu nhất quán (PHONG-CACH-HINH §4): `ref_nv` = tranh đầu có " + " / ".join(D.NV) + " (chỉ gửi kèm cảnh có nhân vật đó); `ref_canh` = một tranh trống cùng nét (mọi cảnh khác; lời sinh ghi rõ nhân vật KHÔNG có trong cảnh).", "",
          "## 1. Bảng cảnh", "", "| Câu | Tầng | Mốc ước (s) | Cảnh: lớp · mã · thời lượng | Lớp chồng |", "|---|---|---|---|---|"]
    for h in hang:
        cs = " · ".join(f"{lp} `{ma}` {ds:.1f}" for lp, ma, ds in h["canh"])
        ov = " · ".join(f"{k}: {v}" for k, v in h["ov"])
        dk = "" if h["doc"] else " (thẻ, không đọc)"
        L.append(f"| {h['id']} ({h['doan']}){dk} | {h['tang']} | {h['bd']:.1f}–{h['kt']:.1f} | {cs} | {ov} |")
    L += [f"| KET | — | {t_loi:.1f}–{t_loi + KET_GIU:.1f} | {D.KET} | |", f"| NGUON | — | {t_loi + KET_GIU:.1f}–{t:.1f} | {D.NGUON} | |", "",
          f"## 2. Đồ hoạ động L2 ({len(l2_dung)} đồ hoạ; mã, 0 USD — khuôn `scripts/mr6/l2.py`; PHONG-CACH-HINH §2: hiện dần theo mốc từ, hạt tiền, số đếm, một điểm nhấn đỏ cam)", "",
          "| Mã | Câu hỏi đồ hoạ trả lời | Hiện dần (theo lời) | Điểm nhấn duy nhất | Câu | Nhãn tầng |", "|---|---|---|---|---|---|"]
    for g in l2_dung:
        v = D.L2[g]; cs = sorted({h["id"] for h in hang for x in h["canh"] if x[1] == g})
        L.append(f"| {g} | {v['hoi']} | {v['noi_dung']} | {v['nhan']} | {', '.join(cs)} | {v.get('tang', '')} |")
    L += ["", "## 3. Hồ sơ thật L3 (nền ngà B1; crop trang giữ nguyên dạng, khoanh câu; thẻ trích nguyên văn có dòng nguồn)", "",
          "| Mã | Tệp · trang / nguồn | Vùng | Khoanh / chữ | Câu | Ghi chú |", "|---|---|---|---|---|---|"]
    for k, v in D.L3.items():
        cs = sorted({h["id"] for h in hang for x in h["canh"] if x[1] == k})
        L.append(f"| {k} | {v[0]} | {v[1]} | {v[2]} | {', '.join(cs)} | {v[3]} |")
    L += ["", f"Trang/vùng cấm (NGUON.md §4): {D.CAM_L3}", "",
          f"## 4. Khoảnh khắc ảnh→clip (Veo 3.1 Lite, {len(veo_dung)} ≤ 5; khung đầu = tranh L1 KHÔNG người — BAI-HOC tập 1 mục 2)", "",
          "| Mã | Khung đầu (tranh) | Chuyển động (lời Veo khẳng định, mô tả cái có trong khung) | Neo cuối | Câu | Rủi ro / QC |", "|---|---|---|---|---|---|"]
    for k in veo_dung:
        v = D.VEO[k]; cs = sorted({h["id"] for h in hang for x in h["canh"] if x[1] == k})
        L.append(f"| {k} | `{v['tu']}` — {tranh[v['tu']]['mo_ta'][:90]}… | {v['chuyen_dong']} | {v['neo_cuoi']} | {', '.join(cs)} | {v['qc']} |")
    L += ["", "QC mỗi clip (M-c): không người/mặt, không chữ/số/logo mọc ra (V5/V8, bài học tập 1: chữ giả mọc trên vật có chữ), chuyển động không méo; ≤ 2 lượt/khe, lượt 2 đổi lời (V7); hỏng 2 lượt → dùng tranh tĩnh có đẩy/kéo (0 USD, KHÔNG phải vá sau 402 — 402 thì DỪNG).", "",
          f"## 5. Danh sách tranh L1 ({len(tranh)} tranh mới; lời sinh = tiền tố/hậu tố tờ A `reports/mrp1/A/PHONG-CACH.md` + mô tả dưới)", "",
          "| Mã | Loại | Mô tả cảnh (EN, gốc lời sinh) | Dùng ở |", "|---|---|---|---|"]
    for ma, v in tranh.items():
        L.append(f"| {ma} | {v['loai']} | {v['mo_ta']} | {', '.join(v['cau'])} |")
    L += ["", "## 6. Nhạc", ""] + D.NHAC + ["", "## 7. Kiểm máy (scripts/mrs23/shot2.py)", "",
          "- Mỗi câu 1–3 cảnh · mã cảnh tồn tại · ≥ 6 đồ hoạ L2 động có câu hỏi + một điểm nhấn · ≤ 5 Veo, khung đầu tranh loại E · tranh dùng ≤ 2 lần · cảnh tranh ≥ 1,5 s · tranh người thật có từ khoá bóng/lưng/tay, không mặt · từ cấm hình (biếm hoạ, quân phục/phù hiệu/logo/con dấu/cờ) · regex cấm của tập (`kiem_rieng.cam_them`) · KB/KC quét cả tệp này.",
          "- Kết quả: **@@KQ@@**", ""]
    md = "\n".join(L)
    # quét cả tệp: regex cấm của tập, KB, KC
    dong = md.split("\n")
    for pat in kr.get("cam_them", []):
        for i, ln in enumerate(dong, 1):
            if re.search(pat, ln): loi.append(f"SHOT2 dòng {i}: khớp regex cấm /{pat}/")
    for r in kr.get("kem_moi_lan", []):
        for i, ln in enumerate(dong, 1):
            if re.search(r["ten"], ln) and not re.search(r["can_shot"], ln): loi.append(f"SHOT2 dòng {i}: có {r['ten']} mà không kèm câu ◐ (KB)")
    for r in kr.get("dung_mot", []):
        k = [i for i, ln in enumerate(dong, 1) if re.search(r["ten"], ln)]
        if len(k) > 1: loi.append(f"SHOT2: /{r['ten']}/ ở {len(k)} dòng {k} (KC tối đa 1)")
    md = md.replace("@@KQ@@", "ĐẠT (0 lỗi)" if not loi else f"TRƯỢT ({len(loi)}): " + "; ".join(loi))
    open(os.path.join(thu, "SHOT2.md"), "w").write(md)
    tom = {"tap": D.THU_MUC, "tong_s": round(t, 1), "lời_va_the_s": round(t_loi, 1), "canh": n_canh, "tranh_moi": len(tranh),
           "tranh_theo_loai": nv_dem, "l1_canh": n_l1, "l1_tb_s": round(s_l1 / max(n_l1, 1), 2), "l2": l2_dung, "l2_canh": n_l2,
           "l3": list(D.L3), "veo": veo_dung, "loi": loi}
    os.makedirs(os.path.join(ROOT, "reports", "mrs23"), exist_ok=True)
    json.dump(tom, open(os.path.join(ROOT, "reports", "mrs23", f"shot2_{tap}.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in tom.items() if k != "loi"}, ensure_ascii=False)); print("loi:", loi)
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
