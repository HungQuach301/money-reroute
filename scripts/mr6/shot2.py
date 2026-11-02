#!/usr/bin/env python3
"""MR-6 · BẢNG SHOT 2 (dữ liệu) — mỗi câu 1–3 cảnh, lớp L1 tranh / L2 đồ hoạ động / L3 hồ sơ thật, theo PHONG-CACH-HINH v1.
  python3 scripts/mr6/shot2.py   → docs/tap01-1inmm/SHOT2.md + reports/mr6/shot2.json (dòng thời gian tính máy)
Mốc = whisper giọng thật (reports/mr6/moc_cau.json). Khoảng của câu = [đầu câu, đầu câu kế); cảnh chia theo trọng số.
Mã cảnh:  aNN = tranh MR-P1 (A) dùng lại · bNNN = tranh MR-6 · "x:2" = lần dùng 2 (khung cắt/chuyển động khác) ·
          G.. = đồ hoạ động L2 (scripts/mr6/l2.py) · T.. = crop trang hồ sơ thật L3 · K1–K5 = Veo ảnh→video MR-6 ·
          V10–V13 = clip Veo tả thực MR-4/MR-5 (chỉnh màu teal–hổ phách) · "*n" = trọng số thời lượng.
Lớp chồng (OV) = thẻ nền tối chồng lên tranh (KBCB ≤ 4 s, tiêu đề, tên, bài học), nhãn tầng + nguồn tự động theo loi.json."""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# ---------------- cảnh theo câu ----------------
SC = {
 "S001": ["a01*1.3", "b064"], "S002": ["a03", "b065", "a04"], "S003": ["a05", "b066*1.3"],
 "S004": ["a07", "b001", "b067"], "S005": ["b002", "G01*2"], "S006": ["a09", "b070", "a10"],
 "S007": ["T01*2"], "S008": ["b003", "a15", "b074"], "S009": ["G02*1"], "S010": ["G02*1", "a12"],
 "S011": ["K2*2"],
 "S012": ["a14", "b004", "b005"], "S013": ["b006", "b068"], "S014": ["a16", "b071"],
 "S015": ["a17", "b072", "G03*1.5"], "S016": ["G03*2.5", "a19"], "S017": ["G03*1"],
 "S018": ["b073", "T02*2"], "S019": ["a18"],
 "S020": ["b007", "G04*1.5"], "S021": ["b008", "b076"], "S022": ["G04*1"], "S023": ["G04*1.5", "a08"],
 "S024": ["T03*2"],
 "S025": ["b009", "b077"], "S026": ["G05*1"], "S027": ["G05*2"], "S028": ["G05*1"],
 "S029": ["b010", "b080", "b011", "b079"],
 "S030": ["b012", "G06*2"], "S031": ["b082", "T04*1.6"], "S032": ["b013", "T05*1.4"], "S033": ["b014"],
 "S034": ["b015", "b084", "G07*1"], "S035": ["G07*1.5", "b085"], "S036": ["G07*2"], "S037": ["b016"],
 "S038": ["b017", "G07*1"], "S039": ["b018", "b087"],
 "S040": ["b021"], "S041": ["b022", "G08*2"], "S042": ["G08*2", "b089"], "S043": ["G08*1.2", "b090"],
 "S044": ["G08*2", "b083"], "S045": ["b023", "b074:2", "b088"],
 "S046": ["b024", "G09*2"], "S047": ["b025", "G09*2", "b092"], "S048": ["G09*1.4"], "S049": ["b026", "b093"],
 "S050": ["b028", "G10*1"], "S051": ["G10*3", "T06*1.6"], "S052": ["V10*1.2", "b029", "b030"],
 "S053": ["b031", "b027", "G11*1.4"], "S054": ["G11*1", "b032"], "S055": ["G11*1.6", "b099"], "S056": ["G11*1", "V11*1.2"],
 "S057": ["b033", "b075"],
 "S058": ["G12*1.5"], "S059": ["V12*1.6"], "S060": ["G12*2"], "S061": ["b034", "b060", "G12*1.2"],
 "S062": ["b035", "b102", "b036"], "S063": ["V13*1.3", "G13*1"],
 "S064": ["b037", "b038"], "S065": ["G13*1.6"], "S066": ["b039", "b104"],
 "S067": ["T07*1.6", "b040"], "S068": ["K3*2"], "S069": ["b041", "b042", "G14*2", "b109"],
 "S070": ["b043", "b110"], "S071": ["b044", "b111"], "S072": ["b045"],
 "S073": ["T08*1.4", "G15*1.4"], "S074": ["b046", "b047", "b114"], "S075": ["T09*1.4", "b113"],
 "S077": ["b048", "b049", "b115", "b108"], "S076": ["b050"],
 "S078": ["b051", "G15*1.4"], "S079": ["b052", "G15*1"], "S080": ["G15*1"], "S081": ["b053*1.6", "G15*1.4"],
 "S082": ["b116", "G16*1"], "S083": ["b054", "T10*1.6", "b055"], "S084": ["b120", "G16*1.6", "b056"],
 "S085": ["G16*1.4", "b124"], "S086": ["b123", "G16*1"],
 "S087": ["b057", "b126", "G17*1.6"], "S088": ["b124:2", "G17*1"], "S089": ["T11*1.4", "G17*1.2"],
 "S090": ["b058", "T12*1.2"], "S091": ["b059", "b129", "T13*1.2"], "S092": ["T14*1.2", "b130"],
 "S093": ["b131", "G18*1.4"], "S094": ["b009:2", "G18*1.4"], "S095": ["b060:2", "b101", "G18*1"], "S096": ["b086", "G18*1.2"],
 "S097": ["b133", "b078"], "S098": ["b134", "a20"], "S099": ["b135", "b024:2"], "S100": ["b019:2", "b016:2"],
 "S101": ["b137", "b041:2"], "S102": ["K5*2", "b132"], "S103": ["b138", "b148"], "S104": ["b140", "b139"], "S105": ["b150"],
 "KET": ["G19*1"], "NGUON": ["G20*1"],
}
# Tranh chưa dùng ở trên được rải làm cảnh chen ở câu dài (> 7 s) — xem CHEN.
CHEN = {"S012": "b142", "S016": "b069", "S027": "b081", "S029": "b143", "S041": "b091", "S047": "b145", "S051": "b094",
        "S053": "b095", "S056": "b098", "S062": "b096", "S064": "b105", "S069": "b112", "S074": "b106", "S077": "b107",
        "S081": "b119", "S083": "b121", "S084": "b122", "S087": "b125", "S088": "b097", "S089": "b117",
        "S092": "b128", "S095": "b144", "S102": "b149", "S104": "b140:2", "S016b": "b118", "S073": "b141", "S086": "b146",
        "S066": "b100", "S070": "b147", "S045": "b103", "S035": "b086:2", "S036": "b019", "S038": "b020", "S004": "b062",
        "S061": "b061", "S002b": "a02", "S011": "b063", "S030": "a11", "S031": "b105", "S043": "b100", "S052b": "b097",
        "S058": "b020", "S065": "b147", "S085": "a13", "S010": "a12:2", "S021": "b076:2", "S032": "a05:2", "S040": "b143:2", "S060": "b101:2",
        "S063": "b036:2", "S078": "b116:2", "S079": "b118:2", "S090": "b058:2", "S093": "b139:2", "S096": "b087:2", "S103": "b138:2"}

# ---------------- lớp chồng (thẻ nền tối trên tranh) ----------------
KBCB = "HBO and Netflix were not accused of wrongdoing in these cases; according to the SEC, neither company ever did business with 1inMM."
OV = {
 "S001": [("bong", "Payment received", 0.4)], "S002": [("bong", "Delay on the platform side. Funds by next week.", 1.2)],
 "S003": [("tieu_de", "Real cases from the public record", "MONEY REROUTE")],
 "S004": [("ten", "Zachary Horwitz", "aka “Zach Avery” · actor, Los Angeles")],
 "S008": [("kbcb", KBCB)], "S019": [("kbcb", KBCB)], "S033": [("kbcb", KBCB)], "S045": [("kbcb", KBCB)],
 "S072": [("kbcb", KBCB)], "S076": [("kbcb", KBCB)],
 "S012": [("ten", "1inMM Capital, LLC", "founded around 2013 · promoted as a film distribution company · Los Angeles")],
 "S013": [("ten", "1inMM (“one in a million”) Capital, LLC", "according to the SEC")],
 "S014": [("ten", "Sole manager", "according to the indictment")],
 "S029": [("bai", "Where would that much profit come from, every single time?")],
 "S039": [("bai", "Know exactly who is on the other side of your contract.")],
 "S049": [("bai", "If every piece of proof comes from the seller, it is not independent proof.")],
 "S052": [("ten", "A $6 million home · luxury cars · private jet travel", "according to prosecutors")],
 "S057": [("bai", "Treat it as a claim to check, not as proof.")],
 "S061": [("bai", "On-time payments feel like proof. In a Ponzi scheme, they keep it going.")],
 "S070": [("ten", "Messages used identities of actual HBO and Netflix employees", "according to prosecutors")],
 "S071": [("ten", "Identity-theft counts: DISMISSED", "not convicted of those counts")],
 "S077": [("bai", "A reason to slow down, not to send more.")],
 "S102": [("bai", "1 RULE · Verify independently before any money moves.")],
}
# Thẻ bài học / dấu hiệu P21 (chữ đã duyệt ở SHOT.md §3, G1) — vẽ trong G18 (bài học) và lớp chồng "the_p21" (dấu hiệu).
P21 = {"S094": ("LESSON 1", "Convert short-term returns to a yearly rate"), "S095": ("LESSON 2", "Steady payments don't prove it's real"),
       "S096": ("LESSON 3", "Know who's on the other side of your contract"),
       "S097": ("RED FLAG 1", "High, fixed returns on a short clock"), "S098": ("RED FLAG 2", "A famous partner you can't verify"),
       "S099": ("RED FLAG 3", "All the proof comes from the seller"), "S100": ("RED FLAG 4", "Unregistered offer passed through friends"),
       "S101": ("RED FLAG 5", "Missed payments blamed on someone else")}
for k in ("S097", "S098", "S099", "S100", "S101"): OV.setdefault(k, []).append(("p21",) + P21[k])

# ---------------- L3: crop trang hồ sơ (điểm PDF; danh sách cấm SHOT.md đầu bảng đã tránh) ----------------
H = "ho-so/1inmm-horwitz/"
L3 = {
 "T01": (H + "doj-plea-agreement-2021.pdf", 11, (38, 232, 574, 430), ["purported copies of the distribution agreements were fake"], "PLEA AGREEMENT · U.S. v. HORWITZ · Dkt. 45 · page 11"),
 "T02": (H + "sec-complaint-2021.pdf", 3, (40, 141, 556, 380), ["primarily from Latin America", "Strategic Partners"], "SEC COMPLAINT · SEC v. HORWITZ · ¶5"),
 "T03": (H + "sec-complaint-2021.pdf", 5, (40, 500, 556, 548), ["over the life of the note"], "SEC COMPLAINT · ¶22"),
 "T04": (H + "sec-complaint-2021.pdf", 9, (40, 356, 556, 450), ["I believed that if HBO was involved, my investment was safe."], "SEC COMPLAINT · ¶46"),
 "T05": (H + "sec-complaint-2021.pdf", 9, (40, 452, 556, 522), ["consistent track record of paying large profits"], "SEC COMPLAINT · ¶47"),
 "T06": (H + "doj-plea-agreement-2021.pdf", 12, (38, 256, 574, 356), ["lavish lifestyle"], "PLEA AGREEMENT · Dkt. 45 · page 12"),
 "T07": (H + "doj-plea-agreement-2021.pdf", 11, (38, 425, 574, 548), ["to lull the investors into believing their funds were safely invested"], "PLEA AGREEMENT · Dkt. 45 · page 11"),
 "T08": (H + "sec-complaint-2021.pdf", 13, (40, 188, 556, 282), ["a release of funds by April 9 th (at the latest)"], "SEC COMPLAINT · ¶76"),
 "T09": (H + "sec-complaint-2021.pdf", 13, (40, 284, 556, 428), ["sharing the financial burden with investors", "(highly doubtful)"], "SEC COMPLAINT · ¶77"),
 "T10": (H + "doj-plea-agreement-2021.pdf", 8, (38, 305, 574, 548), ["is, in fact, guilty", "agree to the statement of facts"], "PLEA AGREEMENT · Dkt. 45 · page 8"),
 "T11": (H + "sec-final-judgment-horwitz-2024.pdf", 3, (40, 258, 556, 452), ["$74,222,912.33", "deemed satisfied by the restitution order"], "FINAL JUDGMENT · SEC v. HORWITZ · Dkt. 323 · §III"),
 "T12": (H + "doj-sentencing-position-2022.pdf", 6, (38, 112, 574, 166), ["portrayed himself as a Hollywood success story."], "GOV’T SENTENCING POSITION · Dkt. 58 · page 6"),
 "T13": (H + "doj-sentencing-position-2022.pdf", 6, (38, 352, 574, 404), ["was not a successful businessman or Hollywood insider.", "He just played one in real life."], "GOV’T SENTENCING POSITION · Dkt. 58 · page 6"),
 "T14": (H + "doj-sentencing-position-2022.pdf", 6, (38, 545, 574, 597), ["the largest known Ponzi scheme in the history of this District."], "GOV’T SENTENCING POSITION · Dkt. 58 · page 6"),
}
# Mô tả ngắn các đồ hoạ L2 (cho SHOT2.md); mã vẽ ở scripts/mr6/l2.py
L2 = {
 "G01": "Kỳ phiếu: đồng hồ \"6 or 12 months\" + % đếm lên 25–45% (nhấn đỏ cam)",
 "G02": "Đếm lên $650,000,000+ (at least) → \"20 YEARS IN PRISON\" đếm 0→20 (nhấn)",
 "G03": "Lời chào mời: INVESTORS → 1inMM → FILM RIGHTS → STREAMING PLATFORMS (outside the U.S.) → PROFITS → quay về; hạt tiền chạy theo lời",
 "G04": "Kỳ phiếu = written IOU: securities (admitted) · $35,000 – $1.5M · 6 or 12 months · +25–45% (đếm, nhấn)",
 "G05": "Phép tính: cột \"over the life of the note\" 35% vs \"per year\" 70% (×2) → 1.35 × 1.35 = 1.82 ≈ 82% (nhấn)",
 "G06": "Investors → 1inMM → \"ultimate counterparties\": HBO · Netflix — as claimed (viền đứt đỏ cam) ◐",
 "G07": "Phễu: 1inMM ← 5 major groups ← 250+ sub-investors (đếm; contested) · vạch đứt \"NO DIRECT CONTRACT\" (nhấn)",
 "G08": "\"On paper\" vs \"in fact\": collateral film(s), sole owner → rights NOT acquired (generally) ✗ · no distribution agreements ✗ · ◐ SEC: no business relationships",
 "G09": "Ba thẻ giấy tờ: notes · license agreements FAKE · distribution agreements FAKE → mọi mũi tên từ một nguồn \"HIM\"",
 "G10": "Tiền đi đâu: nhánh film rights gạch bỏ; 4 dòng hạt: earlier investors (nhấn) · company facade · himself & entities · \"lavish lifestyle\"",
 "G11": "Co-investment ◐: tiền nhà đầu tư khác (nhấn) → \"his\" stake → group notes → $2.33M \"his share\" (Mar. 2018) → home ≈ $5.7M cash",
 "G12": "Vòng Ponzi: newer investors → pool → earlier investors; dòng tiền quay về (nhấn) → buy more notes, raise from others",
 "G13": "Trục: payments on schedule → ~Dec. 2019 defaults begin (nhấn) → ≈ $230 million principal in default (đếm)",
 "G14": "\"Messages from the platforms\" → no communication ✗ → FAKE — admitted",
 "G15": "Đếm ngược: ~Mar. 12, 2021 email \"by April 9th (at the latest)\" ◐ → 28 DAYS · Apr. 5 SEC files → 4 · Apr. 6 freeze → 3 · Apr. 6 arrest: bộ đếm DỪNG · May 4 indictment; ô APRIL 9 viền đỏ cam, xám dần",
 "G16": "Kết cục: Oct. 2021 pleaded guilty (1 count) → Feb. 14, 2022: 240 months = 20 YEARS (đếm) → restitution $230,361,884 (đếm, nhấn) → other counts dismissed",
 "G17": "Vụ SEC ◐: Feb. 2024 final judgment by consent (findings waived) · permanent antifraud bar · ≈ $74.2M deemed satisfied by restitution",
 "G18": "P21: tiêu đề 3 LESSONS · 5 RED FLAGS · 1 RULE; ba thẻ bài học có hình gọi lại (phép tính, vòng, vạch đứt)",
 "G19": "Thẻ tổng kết (nền tối): 3 + 5 + 1 dòng (SHOT.md §3) + nơi kiểm/báo cáo + dòng khai AI; giữ 8 s",
 "G20": "Danh sách nguồn chạy chữ (N1–N22 đã mở) + dòng khai AI",
}
VEO = {"K1": "a01 → bình minh, điện thoại sáng (P00)", "K2": "a06 → thành phố chạng vạng lên đèn (P01)",
       "K3": "a04 → đêm, nhà đầu tư đọc tin, lo (P15)", "K4": "b053 → văn phòng trống, đèn tắt (P17) — LOẠI ở QC (vệt khói/bụi xoáy quanh đèn 2,5–8 s, V5/V8); S081 dùng tranh tĩnh b053",
       "K5": "a13 → bình minh bên cửa sổ, quyết định (P21)",
       "V10": "clip tả thực MR-5 máy bay (P10), chỉnh màu", "V11": "clip tả thực MR-5 chìa khoá (P11), chỉnh màu",
       "V12": "clip tả thực MR-4 tháp ly rót (P12), chỉnh màu", "V13": "clip tả thực MR-5 tháp ly cạn (P13), chỉnh màu"}
KET_GIU = 8.0; KET_TONG = 872.0  # giữ thẻ tổng kết 8 s sau S105, rồi danh sách nguồn tới hết N3


def tach(it):
    w = 1.0
    if "*" in it: it, w = it.split("*"); w = float(w)
    return it, w


def lop(ma):
    if ma.startswith("G"): return "L2"
    if ma.startswith("T"): return "L3"
    if ma.startswith("K"): return "L1-veo"
    if ma.startswith("V"): return "L1-veo-cu"
    return "L1"


def dong_thoi_gian():
    M = json.load(open(os.path.join(ROOT, "reports", "mr6", "moc_cau.json")))
    loi = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))["cau"]}
    cau = sorted(M["cau"].items(), key=lambda kv: kv[1]["s"])
    ds = []
    for i, (cid, m) in enumerate(cau):
        s = 0.0 if i == 0 else m["s"] - 0.35  # cảnh đổi sớm 0,35 s trước tiếng (nhịp dựng)
        e = cau[i + 1][1]["s"] - 0.35 if i + 1 < len(cau) else m["e"] + 0.6
        ds.append((cid, s, e))
    s_ket = ds[-1][2]; ds.append(("KET", s_ket, s_ket + KET_GIU)); ds.append(("NGUON", s_ket + KET_GIU, KET_TONG))
    canh = []; dung = {}
    for cid, s, e in ds:
        items = list(SC[cid])
        for k in (cid, cid + "b"):
            if k in CHEN and (e - s) > 5.5:
                items.insert(len(items) // 2 + (1 if len(items) > 1 else 0), CHEN[k])
        tw = sum(tach(x)[1] for x in items); t = s
        for x in items:
            ma, w = tach(x); d = (e - s) * w / tw
            base = ma.split(":")[0]
            if lop(ma) == "L1": dung[base] = dung.get(base, 0) + 1
            canh.append({"cau": cid, "doan": loi[cid]["doan"] if cid in loi else cid, "ma": ma, "lop": lop(ma),
                         "s": round(t, 3), "e": round(t + d, 3)})
            t += d
    qua = {k: v for k, v in dung.items() if v > 2}
    assert not qua, f"tranh dùng > 2 lần: {qua}"
    return canh, dung, ds


def main():
    canh, dung, ds = dong_thoi_gian()
    loi = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))["cau"]}
    json.dump({"tong_s": KET_TONG, "canh": canh, "ov": OV, "l3": L3, "p21": P21}, open(os.path.join(ROOT, "reports", "mr6", "shot2.json"), "w"),
              ensure_ascii=False, indent=0)
    n = {k: sum(1 for c in canh if c["lop"] == k) for k in ("L1", "L1-veo", "L1-veo-cu", "L2", "L3")}
    tg = {k: round(sum(c["e"] - c["s"] for c in canh if c["lop"] == k), 1) for k in n}
    l1 = [c["e"] - c["s"] for c in canh if c["lop"] == "L1"]
    so_tranh = len(dung); moi = sum(1 for k in dung if k.startswith("b")); cu = sum(1 for k in dung if k.startswith("a"))
    md = ["# BẢNG SHOT 2 — Tập 1 · 1inMM / Horwitz (`tap01-1inmm`) · phong cách PHONG-CACH-HINH v1",
          "",
          "> MR-6 · 02/11/2026. **Thay `SHOT.md`** (giữ làm lịch sử) cho phần hình; lời, giọng, nhạc giữ nguyên (đã duyệt). Bảng **sinh máy** bằng "
          "`python3 scripts/mr6/shot2.py` từ dữ liệu trong tệp đó; mốc = whisper giọng thật (`reports/mr6/moc_cau.json`, `scripts/mr6/moc_cau.py`).",
          f"> Tổng {KET_TONG/60:.0f}:{KET_TONG%60:04.1f} · {len(canh)} cảnh · L1 tranh {n['L1']} cảnh ({tg['L1']} s, TB {sum(l1)/len(l1):.2f} s/cảnh) từ **{so_tranh} tranh** "
          f"({moi} mới MR-6 + {cu} MR-P1) · Veo ảnh→video {n['L1-veo']} cảnh ({tg['L1-veo']} s) · clip tả thực cũ {n['L1-veo-cu']} ({tg['L1-veo-cu']} s) · "
          f"L2 {n['L2']} cảnh ({tg['L2']} s) · L3 {n['L3']} cảnh ({tg['L3']} s).",
          "> Khe không lời 4 s cho 4 thẻ KBCB chỉ chữ (S019, S033, S072, S076) — thẻ nền tối chồng lên tranh (PHONG-CACH-HINH §1). Cảnh đổi 0,35 s trước tiếng.",
          "> Luật áp mọi cảnh: HIEN-CHUONG §4–§5; PHONG-CACH-HINH §1–§5; nhãn tầng + nguồn lớp tĩnh góc dưới theo `loi.json`; nhãn ILLUSTRATIVE ở cảnh tranh đầu mỗi đoạn; "
          "không chữ trên hình ngoài lời đã duyệt, số liệu hồ sơ, nhãn, nguồn (máy đối chiếu: `scripts/mr6/doi_chieu_chu.py`).",
          "> L3 không dùng các trang/dòng cấm của `SHOT.md` (N8 tr. 1, tr. 3; N1 tr. 6 bảng ¶25; N7 tr. 12 dòng 23–28; N22 tr. 1; N22 tr. 6 dòng 10).",
          "", "## 1. Bảng cảnh", "", "| Câu | Tầng | Mốc (s) | Cảnh: lớp · mã · thời lượng | Lớp chồng |", "|---|---|---|---|---|"]
    by = {}
    for c in canh: by.setdefault(c["cau"], []).append(c)
    for cid, s, e in ds:
        cs = by[cid]; tang = loi[cid]["tang"] if cid in loi else "—"
        cell = " · ".join(f"{c['lop']} `{c['ma']}` {c['e']-c['s']:.1f}" for c in cs)
        ov = "; ".join(o[0] + (": " + o[1][:40] if len(o) > 1 and isinstance(o[1], str) else "") for o in OV.get(cid, []))
        md.append(f"| {cid} ({cs[0]['doan']}) | {tang} | {s:.1f}–{e:.1f} | {cell} | {ov} |")
    md += ["", "## 2. Đồ hoạ động L2 (mã, 0 USD — `scripts/mr6/l2.py`)", "", "| Mã | Nội dung (hiện dần theo mốc từ) |", "|---|---|"]
    md += [f"| {k} | {v} |" for k, v in L2.items()]
    md += ["", "## 3. Hồ sơ thật L3 (crop trang, nền ngà, khoanh câu)", "", "| Mã | Tệp · trang | Vùng (điểm PDF) | Khoanh |", "|---|---|---|---|"]
    md += [f"| {k} | `{v[0].split('/')[-1]}` tr. {v[1]} | {v[2]} | {' / '.join(v[3])} |" for k, v in L3.items()]
    md += ["", "## 4. Cảnh động", "", "| Mã | Nguồn |", "|---|---|"] + [f"| {k} | {v} |" for k, v in VEO.items()]
    md += ["", "## 5. Nhạc (theo `SHOT.md` §4, tệp MR-5)",
           "- N1 `N1_mo.mp3` 0:00–0:40, −20 dB dưới lời, tắt dần.",
           "- N2 `N2_tang_dan.mp3` bắt đầu 487,9 s (lớp 1 nhịp tim trước S067; lớp 2 dây vào ≈ S073; lớp 3 trống ≈ S078); **cắt lặng 1,5 s ở S080** (603,3 s), rồi đoạn \"Aftermath\" (nốt piano) từ 604,8 s; mức −24 → −18 dB.",
           f"- N3 `N3_ket.mp3` từ 812,0 s tới hết ({KET_TONG:.0f} s), tắt dần 3 s.", ""]
    open(os.path.join(ROOT, "docs", "tap01-1inmm", "SHOT2.md"), "w").write("\n".join(md))
    print(len(canh), "cảnh", n, tg, "tranh", so_tranh, "mới", moi, "cũ", cu, "TB L1", round(sum(l1) / len(l1), 2))
    chua = [k for k in json.load(open(os.path.join(ROOT, "reports", "mr6", "loi_anh.json")))["tranh"] if k not in dung]
    print("tranh MR-6 chưa dùng:", chua)


if __name__ == "__main__":
    main()
