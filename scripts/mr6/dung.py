#!/usr/bin/env python3
"""MR-6 · Dựng tập 1 theo SHOT2 (0 USD, dựng lại được) → 1080p + 540p, âm −14 LUFS / TP ≤ −1 dBTP.
  python3 scripts/mr6/dung.py [--tu 0 --den 872] [--xem]     # --xem: chỉ 540p nhanh để soát
Đầu vào: reports/mr6/shot2.json (scripts/mr6/shot2.py), reports/mr6/moc_cau.json, docs/tap01-1inmm/loi.json,
tranh lab/mrp1/A + lab/mr6/anh (LFS), clip lab/mr6/veo (K*) + lab/mr4|mr5/veo (V10–V13, chỉnh màu), giọng lab/mr4/tts, nhạc lab/mr5/nhac,
PDF ho-so/1inmm-horwitz. Ra: lab/mr6/dung/tap01_1080p.mp4 (LFS), reports/mr6/xem/tap01_540p.mp4 (LFS), reports/mr6/xem/to1s_*.jpg,
reports/mr6/chu_tren_hinh.json (mọi chuỗi chữ đã vẽ → scripts/mr6/doi_chieu_chu.py).
Song song 4 tiến trình theo khúc thời gian, ghép bằng concat."""
import hashlib, json, math, os, re, subprocess, sys
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
import l2  # noqa: E402
from l2 import fnt, mix, muot, txt, F_SANS, F_SANSB, F_BOLD, F_SERIF, F_SYM, F_MONO, F_MONOB, NGA, XAM, DO, HPA, THAN  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FPS = 25; W, H = 1920, 1080; T_HOA = 0.5
SCR = os.environ.get("MR6_TMP", "/tmp/claude-0/mr6_dung"); os.makedirs(SCR, exist_ok=True)
S2 = json.load(open(os.path.join(ROOT, "reports", "mr6", "shot2.json")))
M = json.load(open(os.path.join(ROOT, "reports", "mr6", "moc_cau.json")))
LOI = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))["cau"]}
TONG = S2["tong_s"]; CANH = S2["canh"]
CS = {k: (v["s"], v["e"]) for k, v in M["cau"].items()}
NGA_L3, MUC = (244, 241, 234), (27, 31, 36)

# ---------------- mốc từ ----------------
TU = M["tu"]
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())


def tw(cid, key, n=0):
    s, e = CS[cid]; k = norm(key); hits = [w["s"] for w in TU if s - 0.25 <= w["s"] <= e + 0.25 and norm(w["w"]).startswith(k)]
    return hits[n] if len(hits) > n else None


# ---------------- nguồn + nhãn tầng (theo loi.json) ----------------
SRC = {"N1": "SEC v. Horwitz, 2:21-cv-02927 (C.D. Cal.), Complaint", "N2": "SEC Press Rel. 2021-58", "N3": "SEC Lit. Rel. 25067",
       "N4": "SEC v. Horwitz, Final Judgment, Dkt. 323 (C.D. Cal. 2024)", "N5": "SEC Lit. Rel. 25973",
       "N6": "U.S. v. Horwitz, 2:21-cr-00214 (C.D. Cal.), Indictment, Dkt. 25", "N7": "U.S. v. Horwitz, 2:21-cr-00214 (C.D. Cal.), Plea Agreement, Dkt. 45",
       "N8": "U.S. v. Horwitz, Judgment, Dkt. 75", "N10": "DOJ USAO C.D. Cal. Press Rel. 21-059", "N11": "DOJ USAO C.D. Cal. Press Rel. 21-207",
       "N12": "DOJ USAO C.D. Cal. Press Rel. 22-027", "N18": "sec.gov", "N19": "FINRA BrokerCheck", "N20": "SEC IAPD", "N21": "FTC ReportFraud",
       "N22": "U.S. v. Horwitz, Gov’t Sentencing Position, Dkt. 58"}
NHAN = {"●": ("● CONVICTED", DO), "●T": ("● CONVICTED · admitted in plea", DO), "◐": ("◐ ALLEGED", HPA)}


def nguon(cid):
    c = LOI.get(cid)
    if not c: return None
    if c["tang"] == "KBCB": return "Source: SEC Lit. Rel. 25067; SEC Complaint ¶78; Indictment, Dkt. 25, p. 1"
    if cid in ("S027", "S028", "S094"): return "Illustrative math based on a sample note in the SEC complaint (¶25)"
    if c["tang"] in ("MH", "CHUNG") and cid not in ("S103", "S104"): return None
    gom = {}  # gộp trang theo tài liệu để dòng nguồn không tràn
    for n in c["nguon"]:
        m = re.match(r"(N\d+)\s*(.*)", n); k, rest = m.group(1), m.group(2)
        if k not in SRC: continue
        g = gom.setdefault(k, [])
        pg = re.search(r"tr\. ([\d–]+)", rest); para = re.search(r"¶(\d+)", rest)
        if k == "N1" and para: g.append("¶" + para.group(1))
        elif pg and k != "N1": g.append(pg.group(1))
    out = []
    for k, g in gom.items():
        g = list(dict.fromkeys(g)); s = SRC[k]
        if g: s += (" " if k == "N1" else (", pp. " if (len(g) > 1 or "–" in g[0]) else ", p. ")) + ", ".join(g)
        out.append(s)
    out = out[:3]
    # gộp tiền tố vụ hình sự lặp lại để dòng nguồn ngắn (kiểm pháp lý lần 2, phát hiện 7)
    TT = "U.S. v. Horwitz, 2:21-cr-00214 (C.D. Cal.), "
    hs = [o for o in out if o.startswith("U.S. v. Horwitz")]
    if len(hs) > 1:
        gop = TT.rstrip(", ") + ": " + "; ".join(o.replace(TT, "").replace("U.S. v. Horwitz, ", "") for o in hs)
        out = [gop] + [o for o in out if o not in hs]
    return ("Source: " + "; ".join(out)) if out else None


def nhan_tang(cid):
    c = LOI.get(cid)
    if not c: return None
    if cid in ("S087", "S088", "S089"): return ("◐ ALLEGED · consent judgment, no findings of fact", HPA)
    if cid in ("S090", "S091", "S092"): return ("◐ ALLEGED · prosecutors’ words", HPA)
    return NHAN.get(c["tang"])


def huy_hieu(d, x, y, text, mau, s=30):
    f = fnt(F_SANSB, s); ky, chu = (text[0], text[1:]) if text[0] in "●◐" else ("", text)
    fk = fnt(F_SYM, s); wk = d.textlength(ky, font=fk) if ky else 0; w = wk + d.textlength(chu, font=f)
    d.rounded_rectangle((x, y, x + w + 32, y + s + 20), radius=8, fill=mau + (240,))
    l2.CHU.add(text)
    if ky: d.text((x + 16, y + 7), ky, font=fk, fill="white")
    d.text((x + 16 + wk, y + 8), chu, font=f, fill="white")


def lop_nhan(cid, nhan_minh_hoa=None):
    """Lớp tĩnh: nhãn tầng + nguồn góc dưới trái; nhãn ILLUSTRATIVE góc trên trái."""
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o); co = False
    src = nguon(cid); nh = nhan_tang(cid)
    if src or nh:
        co = True; d.rectangle((0, 968, W, H), fill=(14, 17, 21, 190))
        x = 60
        if nh: huy_hieu(d, x, 982, nh[0], nh[1]); x += int(d.textlength(nh[0], font=fnt(F_SANSB, 30))) + 60
        if src:
            l2.CHU.add(src); sz = 23
            while sz > 14 and d.textlength(src, font=fnt(F_MONO, sz)) > W - x - 40: sz -= 1
            d.text((x, 994 + (23 - sz) // 2), src, font=fnt(F_MONO, sz), fill=(214, 210, 200))
    if nhan_minh_hoa:
        co = True; f = fnt(F_SANSB, 28); w = d.textlength(nhan_minh_hoa, font=f); l2.CHU.add(nhan_minh_hoa)
        d.rounded_rectangle((56, 50, 56 + w + 30, 96), radius=8, fill=(110, 116, 125, 225)); d.text((71, 57), nhan_minh_hoa, font=f, fill="white")
    return o if co else None


# ---------------- lớp chồng thẻ nền tối ----------------
def wrap(d, s, f, wmax):
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= wmax: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out


def the(ov):
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o); k = ov[0]
    if k == "kbcb":
        f = fnt(F_SERIF, 48); ls = wrap(d, ov[1], f, 1500); h = 70 * len(ls) + 70
        d.rectangle((0, 900 - h - 40, W, 950), fill=(14, 17, 21, 225)); d.rectangle((120, 900 - h - 10, 128, 900 - 30), fill=(43, 122, 120, 255))
        y = 900 - h
        for ln in ls: l2.CHU.add(ln); d.text((160, y), ln, font=f, fill=NGA); y += 70
    elif k in ("ten",):
        f1 = fnt(F_SERIF, 66 if len(ov[1]) < 40 else 50); d.rectangle((0, 760, W, 950), fill=(14, 17, 21, 215))
        l2.CHU.add(ov[1]); d.text((90, 782), ov[1], font=f1, fill=NGA)
        if len(ov) > 2 and ov[2]: l2.CHU.add(ov[2]); d.text((90, 880), ov[2], font=fnt(F_SANS, 34), fill=(216, 212, 202))
    elif k == "bai":
        f = fnt(F_SERIF, 54); ls = wrap(d, ov[1], f, 1100); h = 74 * len(ls) + 60
        d.rectangle((W - 1260, 520 - h // 2, W - 60, 520 + h // 2), fill=(14, 17, 21, 220)); d.rectangle((W - 1260, 520 - h // 2, W - 1250, 520 + h // 2), fill=DO + (255,))
        y = 520 - h // 2 + 30
        for ln in ls: l2.CHU.add(ln); d.text((W - 1220, y), ln, font=f, fill=NGA); y += 74
    elif k == "p21":
        d.rectangle((0, 730, W, 950), fill=(14, 17, 21, 220)); l2.CHU.update([ov[1], ov[2]])
        d.text((90, 752), ov[1], font=fnt(F_BOLD, 40), fill=DO if "FLAG" in ov[1] else (43, 122, 120)); d.text((90, 815), ov[2], font=fnt(F_SERIF, 70), fill=NGA)
    elif k == "tieu_de":
        d.rectangle((0, 380, W, 700), fill=(14, 17, 21, 200)); l2.CHU.update([ov[1], ov[2]])
        d.text((960, 500), ov[1], font=fnt(F_SERIF, 92), fill=NGA, anchor="mm"); d.line((660, 580, 1260, 580), fill=DO, width=6)
        d.text((960, 640), ov[2], font=fnt(F_MONOB, 40), fill=XAM, anchor="mm")
    elif k == "bong":
        f = fnt(F_SANS, 44); ls = wrap(d, ov[1], f, 700); h = 58 * len(ls) + 50; x0, y0 = 1040, 180
        d.rounded_rectangle((x0, y0, x0 + 800, y0 + h), radius=34, fill=(244, 241, 234, 240)); yy = y0 + 25
        for ln in ls: l2.CHU.add(ln); d.text((x0 + 38, yy), ln, font=f, fill=MUC); yy += 58
        s = "ILLUSTRATIVE — not a real message"; l2.CHU.add(s)
        d.text((x0 + 800, y0 + h + 14), s, font=fnt(F_SANSB, 26), fill=(230, 226, 218), anchor="ra")
    return o


def ov_khung(cid):
    """(t_bat_dau, t_ket_thuc, RGBA) các lớp chồng của câu; KBCB ≤ 4 s."""
    s, e = CS[cid]; out = []
    for ov in S2["ov"].get(cid, []):
        k = ov[0]
        if k == "kbcb": a, b = s, min(s + 4.0, e + (0.3 if LOI[cid]["doc"] else 0))
        elif k == "ten": a, b = s + 0.2, min(s + 4.0, e + 0.2)
        elif k == "bong": a, b = s + ov[2], e + 0.3
        elif k == "tieu_de": a, b = s + 0.3, min(s + 4.0, e + 0.6)
        else: a, b = s + 0.4, min(s + 4.0, e + 0.3) if k == "bai" else e + 0.3
        if k == "p21": a, b = s, e + 0.3
        out.append((a, b, the(ov)))
    return out


# ---------------- L1 tranh ----------------
CAT = {"a14": (0, 0, 860, 484), "a17": (300, 80, 1110, 536)}  # a17: MR-6 cắt hẹp thêm — bỏ má/tai người vest tối (kiểm pháp lý lần 2)  # MR-P1 (A): a14 l2 nhân vật lọt; a17 khách nền có mặt
CHON = {"a14": "a14_l2"}
CAT_MR6 = json.load(open(os.path.join(ROOT, "reports", "mr6", "cat_khung.json"))) if os.path.exists(os.path.join(ROOT, "reports", "mr6", "cat_khung.json")) else {}
_TR = {}


def tranh(ma):
    base = ma.split(":")[0]
    if base not in _TR:
        if base.startswith("a"):
            im = Image.open(os.path.join(ROOT, "lab", "mrp1", "A", CHON.get(base, base + "_l1") + ".png")).convert("RGB")
            if base in CAT: im = im.crop(CAT[base])
        else:
            f = os.path.join(ROOT, "lab", "mr6", "anh", (CAT_MR6.get(base, {}).get("tep") or base + "_l1") + ".png")
            if not os.path.exists(f) and os.environ.get("MR6_THU"): f = os.path.join(ROOT, "lab", "mrp1", "A", "a03_l1.png")  # chỉ bản thử
            im = Image.open(f).convert("RGB")
            if CAT_MR6.get(base, {}).get("cat"): im = im.crop(tuple(CAT_MR6[base]["cat"]))
        r = max(W * 1.0 / im.width, H * 1.0 / im.height); im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
        x0, y0 = (im.width - W) // 2, (im.height - H) // 2; _TR[base] = im.crop((x0, y0, x0 + W, y0 + H))
    return _TR[base]


MV = [((0.5, 0.5, 1.0), (0.5, 0.5, 1.12)), ((0.5, 0.5, 1.12), (0.5, 0.5, 1.0)), ((0.45, 0.5, 1.1), (0.55, 0.5, 1.1)),
      ((0.55, 0.5, 1.1), (0.45, 0.5, 1.1)), ((0.5, 0.55, 1.04), (0.5, 0.45, 1.14)), ((0.42, 0.45, 1.15), (0.5, 0.5, 1.04))]
MV2 = [((0.35, 0.45, 1.45), (0.42, 0.45, 1.55)), ((0.65, 0.5, 1.5), (0.58, 0.48, 1.4)), ((0.5, 0.4, 1.4), (0.5, 0.55, 1.5))]


def chuyen(ma, i):
    h = int(hashlib.md5(f"{ma}{i}".encode()).hexdigest()[:6], 16)
    return (MV2 if ma.endswith(":2") else MV)[h % (3 if ma.endswith(":2") else 6)]


def khung(im, mv, u):
    (ax, ay, az), (bx, by, bz) = mv; e = muot(u)
    cx, cy, z = ax + (bx - ax) * e, ay + (by - ay) * e, az + (bz - az) * e
    w, h = W / z, H / z; x0 = min(max(cx * W - w / 2, 0), W - w); y0 = min(max(cy * H - h / 2, 0), H - h)
    return im.transform((W, H), Image.EXTENT, (x0, y0, x0 + w, y0 + h), Image.BILINEAR)


# ---------------- L3 hồ sơ (ảnh trang PDF thật, nền ngà, khoanh câu) ----------------
def tu_trang(pdf, p):
    x = subprocess.run(["pdftotext", "-bbox", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout
    return [(float(a), float(b), float(c), float(e), html_unescape(w)) for a, b, c, e, w in
            re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', x)]


def html_unescape(s): return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'")


def tim_cum(words, cum):
    nm = lambda s: re.sub(r"[^a-z0-9$]", "", s.lower().replace("’", "'"))
    q = [nm(x) for x in cum.split() if nm(x)]; ws = [nm(w[4]) for w in words]
    for i in range(len(ws)):
        j, k = i, 0; idx = []
        while j < len(ws) and k < len(q):
            if not ws[j] or (ws[j].isdigit() and ws[j] != q[k] and len(ws[j]) <= 2): j += 1; continue  # số dòng lề trái của trang toà
            if ws[j] == q[k] or (ws[j].startswith(q[k]) and k == len(q) - 1) or (q[k].startswith(ws[j]) and len(ws[j]) > 2):
                idx.append(j); j += 1; k += 1
            else: break
        if k == len(q): return [words[t] for t in idx]
    raise ValueError(f"không thấy cụm: {cum}")


_L3 = {}


def l3_nen(ma):
    if ma in _L3: return _L3[ma]
    pdf, p, vung, cums, tieu = S2["l3"][ma]; pdf = os.path.join(ROOT, pdf)
    o = os.path.join(SCR, f"trang_{os.path.basename(pdf)[:-4]}_{p}")
    if not os.path.exists(o + ".png"):
        subprocess.run(["pdftoppm", "-r", "220", "-f", str(p), "-l", str(p), "-png", "-singlefile", pdf, o], check=True)
    pg = Image.open(o + ".png").convert("RGB"); s = 220 / 72.0
    x0, y0, x1, y1 = vung; cr = pg.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))
    sc = min(1640 / cr.width, 640 / cr.height); cr = cr.resize((int(cr.width * sc), int(cr.height * sc)), Image.LANCZOS)
    im = Image.new("RGB", (W, H), NGA_L3); d = ImageDraw.Draw(im)
    ox, oy = (W - cr.width) // 2, 190 + (640 - cr.height) // 2
    sh = Image.new("RGBA", (cr.width + 40, cr.height + 40), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((20, 20, cr.width + 20, cr.height + 20), fill=(0, 0, 0, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(12)); im.paste(sh, (ox - 14, oy - 8), sh); im.paste(cr, (ox, oy))
    l2.CHU.add(tieu); d.text((ox, 110), tieu, font=fnt(F_MONOB, 32), fill=MUC)
    d.line((ox, 160, ox + 140, 160), fill=DO, width=5)
    words = tu_trang(pdf, p); hop = []
    for cum in cums:
        ws = tim_cum(words, cum); lines = {}
        for (a, b, c, e, _) in ws: lines.setdefault(round(b), []).append((a, b, c, e))
        for ls in lines.values():
            a = min(v[0] for v in ls); b = min(v[1] for v in ls); c = max(v[2] for v in ls); e = max(v[3] for v in ls)
            hop.append(((a - x0) * s * sc + ox, (b - y0) * s * sc + oy, (c - x0) * s * sc + ox, (e - y0) * s * sc + oy))
    _L3[ma] = (im, hop); return _L3[ma]


def l3_khung(ma, t, s0):
    im, hop = l3_nen(ma); a = muot((t - s0 - 0.7) / 0.6)
    if a <= 0: return im.copy()
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    for (x0, y0, x1, y1) in hop:
        d.rounded_rectangle((x0 - 8, y0 - 6, x1 + 8, y1 + 6), radius=8, fill=(242, 165, 65, int(80 * a)), outline=(217, 72, 15, int(255 * a)), width=5)
    return Image.alpha_composite(im.convert("RGBA"), o).convert("RGB")


# ---------------- clip động ----------------
CLIP = {"K1": "lab/mr6/veo/K1_l1.mp4", "K2": "lab/mr6/veo/K2_l1.mp4", "K3": "lab/mr6/veo/K3_l2.mp4", "K4": "lab/mr6/veo/K4_l1.mp4", "K5": "lab/mr6/veo/K5_l1.mp4",
        "V10": "lab/mr5/veo/V10_l2.mp4", "V11": "lab/mr5/veo/V11_l2.mp4", "V12": "lab/mr4/veo/V12_l1.mp4", "V13": "lab/mr5/veo/V13_l2.mp4"}
DAU = {"V12": 2.0, "K4": 3.0}
# chỉnh màu clip tả thực cũ về teal–hổ phách + hạt (PHONG-CACH-HINH §5)
GRADE = ("eq=contrast=1.06:brightness=-0.04:saturation=0.72,colorbalance=rs=-0.06:gs=0.02:bs=0.07:rh=0.08:gh=0.03:bh=-0.07,"
         "curves=all='0/0.04 0.5/0.46 1/0.93',noise=alls=7:allf=t,gblur=sigma=0.6")
CLIP_CHON = json.load(open(os.path.join(ROOT, "reports", "mr6", "veo", "chon.json"))) if os.path.exists(os.path.join(ROOT, "reports", "mr6", "veo", "chon.json")) else {}


def clip_dir(ma):
    src = CLIP_CHON.get(ma, CLIP[ma]); d = os.path.join(SCR, "clip_" + ma)
    if not os.path.isdir(d) or not os.listdir(d):
        os.makedirs(d, exist_ok=True)
        vf = f"fps={FPS},scale={W}:{H}" + ("," + GRADE if ma.startswith("V") else "") + (",eq=brightness=-0.13:gamma=0.82" if ma == "V11" else "")  # V11 bếp sáng → kéo về tông tối
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(DAU.get(ma, 0)), "-i", os.path.join(ROOT, src), "-vf", vf, "-q:v", "3",
                        os.path.join(d, "%04d.jpg")], check=True)
    return d


def clip_khung(ma, u_s):
    d = clip_dir(ma); n = len(os.listdir(d)); k = min(int(u_s * FPS) + 1, n)
    return Image.open(os.path.join(d, f"{k:04d}.jpg")).convert("RGB")


# ---------------- L2 ----------------
DONG19 = [("3 LESSONS", [S2["p21"][k][1] for k in ("S094", "S095", "S096")], (43, 122, 120)),
          ("5 RED FLAGS", [S2["p21"][k][1] for k in ("S097", "S098", "S099", "S100", "S101")], DO),
          ("1 RULE", ["Verify independently before any money moves."], NGA)]
AI = ["Dramatized scenes use AI-generated visuals and illustrative characters, not the real people involved.",
      "Narration voice is AI-generated. Facts are drawn from the public court and agency records listed below."]  # nguyên văn HIEN-CHUONG §6; đặt TRÊN danh sách
NGUON_DS = ["SEC v. Horwitz, No. 2:21-cv-02927 (C.D. Cal.) — Complaint (Apr. 5, 2021)",
            "SEC Press Release 2021-58 (Apr. 6, 2021) · SEC Litigation Release No. 25067 (Apr. 8, 2021)",
            "SEC v. Horwitz — Final Judgment as to Zachary J. Horwitz, Dkt. 323 (Feb. 14, 2024) · SEC Lit. Rel. No. 25973",
            "U.S. v. Horwitz, No. 2:21-cr-00214 (C.D. Cal.) — Indictment, Dkt. 25 (May 4, 2021)",
            "U.S. v. Horwitz — Plea Agreement, Dkt. 45 (Sept. 1, 2021)",
            "U.S. v. Horwitz — Judgment and Probation/Commitment Order, Dkt. 75 (Feb. 2022)",
            "U.S. v. Horwitz — Government’s Sentencing Position, Dkt. 58 (Jan. 31, 2022)",
            "U.S. Attorney’s Office, C.D. Cal. — Press Releases 21-059, 21-207, 22-027",
            "FINRA BrokerCheck · SEC Investment Adviser Public Disclosure",
            "SEC: Submit a Tip or Complaint · FTC: ReportFraud.ftc.gov",
            "Full links in the video description."]


def tao_g():
    g = {}
    for name in ("G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17"):
        g[name] = getattr(l2, name)(tw, CS)
    g["G18"] = l2.G18(tw, CS, S2["p21"]); g["G19"] = l2.G19(tw, CS, DONG19); g["G20"] = l2.G20(tw, CS, NGUON_DS, AI)
    k = [c for c in CANH if c["ma"].startswith("G19")][0]; g["G19"].t0 = k["s"]
    k = [c for c in CANH if c["ma"].startswith("G20")][0]; g["G20"].t0 = k["s"] + 0.5; g["G20"].t1 = k["e"] - 1.0
    return g


# ---------------- lắp khung ----------------
_G = None; _NHAN = {}; _OV = {}
LOP_NGUOI = None


def co_nguoi(ma):
    global LOP_NGUOI
    if LOP_NGUOI is None:
        A = json.load(open(os.path.join(ROOT, "reports", "mr6", "loi_anh.json")))["tranh"]
        LOP_NGUOI = {k for k, v in A.items() if v["loai"] in ("nv", "man")} | {"a01", "a02", "a04", "a05", "a06", "a07", "a08", "a13", "a14", "a16", "a17", "a18", "a20"}
    return ma.split(":")[0] in LOP_NGUOI


def chuan_bi_nhan():
    """Nhãn ILLUSTRATIVE: cảnh minh hoạ (L1/Veo) đầu tiên của mỗi đoạn."""
    """+ (sửa sau kiểm pháp lý lần 2) cảnh minh hoạ ĐẦU TIÊN CÓ NGƯỜI của mỗi đoạn luôn mang "ILLUSTRATIVE — not the real person" (HIEN-CHUONG §4)."""
    da = set(); da_nguoi = set(); out = {}
    for i, c in enumerate(CANH):
        if not c["lop"].startswith("L1"): continue
        ng = co_nguoi(c["ma"])
        if c["doan"] not in da:
            da.add(c["doan"]); out[i] = "ILLUSTRATIVE — not the real person" if ng else "ILLUSTRATIVE"
            if ng: da_nguoi.add(c["doan"])
        elif ng and c["doan"] not in da_nguoi:
            da_nguoi.add(c["doan"]); out[i] = "ILLUSTRATIVE — not the real person"
    return out


NHAN_MH = chuan_bi_nhan()


def nhan_lop(i):
    if i not in _NHAN: _NHAN[i] = lop_nhan(CANH[i]["cau"], NHAN_MH.get(i))
    return _NHAN[i]


def ve_canh(i, t):
    global _G
    c = CANH[i]; ma = c["ma"]; base = ma.split("*")[0]
    d = c["e"] - c["s"] + T_HOA; u = min(max((t - c["s"]) / d, 0), 1)
    if c["lop"] == "L1": f = khung(tranh(base), chuyen(base, i), u)
    elif c["lop"].startswith("L1-veo"): f = clip_khung(base, max(t - c["s"], 0))
    elif c["lop"] == "L3": f = khung(l3_khung(base, t, c["s"]), ((0.5, 0.5, 1.0), (0.5, 0.5, 1.04)), u)
    else:
        if _G is None: _G = tao_g()
        f = _G[base].draw(t)
    f = f.convert("RGBA")
    o = nhan_lop(i)
    if o is not None: f = Image.alpha_composite(f, o)
    return f


def ov_luc(t):
    """Lớp chồng câu đang hiệu lực (fade 0,3 s)."""
    out = []
    for cid in CS:
        s, e = CS[cid]
        if not (s - 1 <= t <= e + 5): continue
        if cid not in _OV: _OV[cid] = ov_khung(cid)
        for a, b, o in _OV[cid]:
            if a <= t <= b:
                al = min((t - a) / 0.3, (b - t) / 0.3, 1.0); out.append((o, al))
    return out


def khung_luc(t):
    i = max(j for j, c in enumerate(CANH) if c["s"] <= t + 1e-6) if t >= CANH[0]["s"] else 0
    f = ve_canh(i, t)
    if i > 0 and t < CANH[i]["s"] + T_HOA:
        f = Image.blend(ve_canh(i - 1, t), f, muot((t - CANH[i]["s"]) / T_HOA))
    for o, al in ov_luc(t):
        if al < 0.999: o = o.copy(); o.putalpha(o.getchannel("A").point(lambda v: int(v * al)))
        f = Image.alpha_composite(f, o)
    f = f.convert("RGB")
    if t < 0.6: f = Image.blend(Image.new("RGB", (W, H)), f, t / 0.6)
    if t > TONG - 2.0: f = Image.blend(Image.new("RGB", (W, H)), f, max(TONG - t, 0) / 2.0)
    return f


def khuc(args):
    k, a, b, out = args
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "faster", "-crf", "19", "-pix_fmt", "yuv420p", "-r", str(FPS), out], stdin=subprocess.PIPE)
    for n in range(int(round(a * FPS)), int(round(b * FPS))):
        p.stdin.write(khung_luc(n / FPS).tobytes())
    p.stdin.close(); p.wait()
    json.dump(sorted(l2.CHU), open(out + ".chu.json", "w"), ensure_ascii=False)
    return out


# ---------------- âm ----------------
def am(dst):
    ins, fl = [], []
    for i, x in enumerate(M["doan"]):
        ins += ["-i", os.path.join(ROOT, x["tep"])]; ms = int(round(x["s"] * 1000)); fl.append(f"[{i}:a]adelay={ms}|{ms},aresample=48000[v{i}]")
    nv = len(M["doan"]); vin = "".join(f"[v{i}]" for i in range(nv)); fl.append(f"{vin}amix=inputs={nv}:normalize=0,apad,atrim=0:{TONG}[voi]")
    nh = os.path.join(ROOT, "lab", "mr5", "nhac")
    ins += ["-i", os.path.join(nh, "N1_mo.mp3"), "-i", os.path.join(nh, "N2_tang_dan.mp3"), "-i", os.path.join(nh, "N2_tang_dan.mp3"), "-i", os.path.join(nh, "N3_ket.mp3")]
    a1, a2, a3, a4 = nv, nv + 1, nv + 2, nv + 3
    # N1: −20 dB (0,10), tắt dần 34–40 s
    fl.append(f"[{a1}:a]aresample=48000,volume=0.10,afade=t=out:st=34:d=6[n1]")
    # N2: bắt đầu 487,9 s; 0–115,4 s của bản nhạc (lớp 1 → lớp 3) với mức −24 → −18 dB, cắt ở S080 (603,3 s)
    st2 = 487.9; cut = CS["S080"][0]; dur = cut - st2
    fl.append(f"[{a2}:a]aresample=48000,atrim=0:{dur:.3f},volume='0.063+(0.126-0.063)*min(t/{dur:.3f},1)':eval=frame,afade=t=out:st={dur-0.08:.3f}:d=0.08,"
              f"adelay={int(st2*1000)}|{int(st2*1000)}[n2a]")
    st3 = cut + 1.5  # lặng 1,5 s rồi đoạn Aftermath (126–136 s) −26 dB
    fl.append(f"[{a3}:a]aresample=48000,atrim=126:136,asetpts=PTS-STARTPTS,volume=0.05,afade=t=in:d=0.4,afade=t=out:st=8:d=2,"
              f"adelay={int(st3*1000)}|{int(st3*1000)}[n2b]")
    st4 = 812.0
    fl.append(f"[{a4}:a]aresample=48000,volume='if(lt(t,{TONG-st4-60+12:.2f}),0.10,0.22)':eval=frame,afade=t=in:d=2,afade=t=out:st={TONG-st4-3:.2f}:d=3,"
              f"adelay={int(st4*1000)}|{int(st4*1000)}[n3]")
    fl.append(f"[voi][n1][n2a][n2b][n3]amix=inputs=5:normalize=0,atrim=0:{TONG}[mix]")
    tmp = dst + ".raw.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fl), "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s16le", tmp], check=True)
    # loudnorm hai lượt → −14 LUFS, TP −1,5
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
          f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-c:a", "pcm_s16le", dst], check=True)


def do_am(f):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]; TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1]; return float(I), float(TP)


def main():
    a = sys.argv
    tu = float(a[a.index("--tu") + 1]) if "--tu" in a else 0.0; den = float(a[a.index("--den") + 1]) if "--den" in a else TONG
    out_dir = os.path.join(ROOT, "lab", "mr6", "dung"); os.makedirs(out_dir, exist_ok=True)
    xem = os.path.join(ROOT, "reports", "mr6", "xem"); os.makedirs(xem, exist_ok=True)
    for ma in {c["ma"].split("*")[0] for c in CANH if c["lop"].startswith("L1-veo") and tu <= c["e"] and c["s"] <= den}: clip_dir(ma)
    n = 4; ranh = [tu + (den - tu) * k / n for k in range(n + 1)]
    ranh = [round(x * FPS) / FPS for x in ranh]
    jobs = [(k, ranh[k], ranh[k + 1], os.path.join(SCR, f"khuc{k}.mp4")) for k in range(n)]
    with Pool(n) as p: outs = p.map(khuc, jobs)
    chu = set()
    for o in outs: chu |= set(json.load(open(o + ".chu.json")))
    json.dump(sorted(chu), open(os.path.join(ROOT, "reports", "mr6", "chu_tren_hinh.json"), "w"), ensure_ascii=False, indent=0)
    lst = os.path.join(SCR, "ds.txt"); open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
    vid = os.path.join(SCR, "hinh.mp4"); subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid], check=True)
    wav = os.path.join(SCR, "am.wav")
    if tu == 0 and den == TONG:
        am(wav); I, TP = do_am(wav)
        f1080 = os.path.join(out_dir, "tap01_1080p.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", "-movflags", "+faststart", f1080], check=True)
        f540 = os.path.join(xem, "tap01_540p.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f1080, "-vf", "scale=960:540", "-c:v", "libx264", "-preset", "medium", "-crf", "23",
                        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", f540], check=True)
        I2, TP2 = do_am(f1080)
        json.dump({"tong_s": TONG, "fps": FPS, "canh": len(CANH), "am_wav": {"I": I, "TP": TP}, "am_1080p": {"I": I2, "TP": TP2}},
                  open(os.path.join(ROOT, "reports", "mr6", "do_am.json"), "w"), indent=1)
        print("âm", I, TP, "→ 1080p", I2, TP2)
    else:
        os.replace(vid, os.path.join(xem, f"thu_{int(tu)}_{int(den)}.mp4"))
    print("xong")


if __name__ == "__main__":
    main()
