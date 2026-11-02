#!/usr/bin/env python3
"""MR-SH1 · Short dọc 1 từ tập 1 `tap01-1inmm` (0 USD — không sinh tranh/giọng mới; dựng lại được).
  python3 scripts/mrsh1/short1.py            → reports/mrsh1/xem/short1.mp4 (1080×1920, 30 fps, LFS)
                                              + reports/mrsh1/chu_tren_hinh.json (sổ chữ đã vẽ, kèm loại → doi_chieu.py)
                                              + reports/mrsh1/do_am.json
  python3 scripts/mrsh1/short1.py --khung 12.3 → chỉ xuất 1 khung PNG vào thư mục tạm (soát nhanh)
Lời = nguyên đoạn P01 (lab/mr4/tts/P01_l2.mp3, S004–S011, đã duyệt), mốc từ = whisper giọng thật (reports/mr4/whisper/P01_l2_sochu.json).
Hình: tranh MR-6 / MR-P1 cắt dọc 9:16 (432×768 từ 1376×768), clip Veo K2 cắt dọc, đồ hoạ L2 dựng lại cho khung dọc (dùng hàm vẽ
của scripts/mr6/l2.py), L3 = crop N7 tr. 11 (ảnh trang PDF thật, nền ngà, khoanh câu). Nhãn tầng + nguồn lấy từ scripts/mr6/dung.py
(nhan_tang, nguon — theo loi.json). Vùng an toàn Shorts: không đặt chữ ở 15 % dưới (y > 1632) và 10 % phải (x > 972).
Âm: giọng + nhạc N1 (−20 dB dưới lời), loudnorm hai lượt → −14 LUFS, TP ≤ −1 dBTP."""
import hashlib, json, math, os, re, subprocess, sys
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCR = os.environ.get("MRSH1_TMP", "/tmp/claude-0/mrsh1_dung"); os.makedirs(SCR, exist_ok=True)
os.environ.setdefault("MR6_TMP", os.path.join(SCR, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))
import l2  # noqa: E402
from l2 import fnt, muot, ap, mix, icon, arrow, hat, dem, nhan, dashed, F_SANS, F_SANSB, F_BOLD, F_SERIF, F_SYM, F_MONO, F_MONOB, NGA, XAM, DO, HP, TEAL, THAN  # noqa: E402
import dung  # noqa: E402  (chỉ dùng nhan_tang, nguon, tu_trang, tim_cum)

W, H, FPS = 1080, 1920, 30
OFF = 0.9            # giọng bắt đầu ở 0,9 s (chữ móc câu 0–1,5 s)
T_HOA = 0.35
SAFE_X, SAFE_Y = 972, 1632   # 10 % phải, 15 % dưới
CX = 510             # trục giữa vùng chữ (lệch trái để tránh 10 % phải)
LOI = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))["cau"]}
MC = json.load(open(os.path.join(ROOT, "reports", "mr6", "moc_cau.json")))
P01_S = [d for d in MC["doan"] if d["doan"] == "P01"][0]["s"]
CAUS = ["S004", "S005", "S006", "S007", "S008", "S009", "S010", "S011"]
CS = {c: (MC["cau"][c]["s"] - P01_S + OFF, MC["cau"][c]["e"] - P01_S + OFF) for c in CAUS}
WH = json.load(open(os.path.join(ROOT, "reports", "mr4", "whisper", "P01_l2_sochu.json")))["words"]
TU = [{"w": w["w"], "s": w["s"] + OFF, "e": w["e"] + OFF} for w in WH]
GIONG_HET = TU[-1]["e"]
T_CUOI = 52.0; TONG = 55.0   # thẻ cuối 3 s
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
# moc_cau MR-6 căn S008 (khớp 0,793) từ "and" thứ hai — từ đầu thật là "HBO" lần 2 trong whisper → chỉnh mốc đầu S008
CS["S008"] = ([w["s"] for w in TU if norm(w["w"]) == "hbo"][1], CS["S008"][1])


def tw(cid, key, n=0):
    s, e = CS[cid]; k = norm(key)
    hits = [w["s"] for w in TU if s - 0.25 <= w["s"] <= e + 0.25 and norm(w["w"]).startswith(k)]
    return hits[n] if len(hits) > n else None


# ---------------- sổ chữ (mọi chuỗi vẽ lên hình, kèm loại) ----------------
CHU = set()


def reg(s, loai): CHU.add((s, loai))


def ve(d, xy, s, f, col, loai, anchor="la", stroke=0, sc=(0, 0, 0), a=1.0, bg=THAN, ghi=True):
    if a <= 0.01: return
    if ghi: reg(s, loai)
    d.text(xy, s, font=f, fill=mix(col, a, bg) if bg is not None else col, anchor=anchor, stroke_width=stroke, stroke_fill=sc)


def wrap(d, s, f, wmax):
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= wmax or not cur: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out


# ---------------- cảnh ----------------
# (mã, lớp, câu cho nhãn/nguồn [None = theo thời gian], bắt đầu, tâm x cắt dọc trên ảnh 1376 px, có người thật/bóng người)
def _sc():
    k = lambda c, w, n=0: tw(c, w, n) - 0.35
    L = [("a07", "L1", "S004", 0.0, 660, True),
         ("b001", "L1", "S004", k("S004", "actor"), 500, False),
         ("b067", "L1", "S004", k("S004", "screen"), 860, True),
         ("b002", "L1", "S004", k("S004", "zach", 1), 900, True),
         ("GA", "L2", "S005", CS["S005"][0] - 0.35, None, False),
         ("a09", "L1", "S006", CS["S006"][0] - 0.35, 700, False),
         ("b070", "L1", "S006", k("S006", "would"), 620, False),
         ("GB", "L2", None, k("S006", "licensed"), None, False),
         ("T01", "L3", "S007", tw("S007", "fake") + 0.75, None, False),
         ("b003", "L1", "S008", tw("S008", "according") - 0.35, 690, False),
         ("a15", "L1", "S008", tw("S008", "neither") - 0.35, 420, False),
         ("GC", "L2", "S009", CS["S009"][0] - 0.35, None, False),
         ("a12", "L1", "S010", CS["S010"][0] - 0.35, 1000, False),
         ("GD", "L2", "S010", k("S010", "sentenced"), None, False),
         ("K2", "veo", "S011", CS["S011"][0] - 0.35, 1170, True),
         ("CUOI", "cuoi", None, T_CUOI, None, False)]
    out = []
    for i, (ma, lop, cau, s, cx, ng) in enumerate(L):
        e = L[i + 1][3] if i + 1 < len(L) else TONG
        out.append({"ma": ma, "lop": lop, "cau": cau, "s": round(s, 3), "e": round(e, 3), "cx": cx, "nguoi": ng})
    return out


CANH = _sc()


def cau_luc(t):
    c = CAUS[0]
    for k in CAUS:
        if CS[k][0] - 0.35 <= t: c = k
    return c


# ---------------- L1 tranh cắt dọc ----------------
_TR = {}


def tep_tranh(ma):
    return os.path.join(ROOT, "lab", "mrp1", "A", ma + "_l1.png") if ma.startswith("a") else os.path.join(ROOT, "lab", "mr6", "anh", ma + "_l1.png")


def cat_doc(ma, cx):
    """Cắt 9:16 (432×768) quanh tâm cx từ tranh 1376×768 → 1080×1920."""
    if ma not in _TR:
        im = Image.open(tep_tranh(ma)).convert("RGB"); w = round(im.height * 9 / 16)
        x0 = int(min(max(cx - w / 2, 0), im.width - w)); cr = im.crop((x0, 0, x0 + w, im.height))
        cr = cr.resize((W, H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
        _TR[ma] = cr
    return _TR[ma]


def chuyen(ma):
    h = int(hashlib.md5(ma.encode()).hexdigest()[:6], 16) % 3
    return [((0.5, 0.5, 1.0), (0.5, 0.47, 1.08)), ((0.5, 0.48, 1.08), (0.5, 0.52, 1.0)), ((0.5, 0.55, 1.03), (0.5, 0.45, 1.09))][h]


def khung(im, mv, u):
    (ax, ay, az), (bx, by, bz) = mv; e = muot(u)
    cx, cy, z = ax + (bx - ax) * e, ay + (by - ay) * e, az + (bz - az) * e
    w, h = W / z, H / z; x0 = min(max(cx * W - w / 2, 0), W - w); y0 = min(max(cy * H - h / 2, 0), H - h)
    return im.transform((W, H), Image.EXTENT, (x0, y0, x0 + w, y0 + h), Image.BILINEAR)


_GRAD = None


def toi_tren_duoi(f):
    """Dải tối trên/dưới cho chữ đọc được trên tranh."""
    global _GRAD
    if _GRAD is None:
        g = Image.new("L", (1, H))
        for y in range(H):
            a = 0
            if y < 300: a = int(150 * (1 - y / 300))
            if y > 1050: a = int(200 * min((y - 1050) / 450, 1))
            g.putpixel((0, y), a)
        _GRAD = g.resize((W, H))
    return Image.composite(Image.new("RGB", (W, H), (8, 10, 12)), f, _GRAD)


# ---------------- clip K2 cắt dọc ----------------
def k2_dir():
    d = os.path.join(SCR, "k2")
    if not os.path.isdir(d) or not os.listdir(d):
        os.makedirs(d, exist_ok=True); x0 = 1170 - 304
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(ROOT, "lab", "mr6", "veo", "K2_l1.mp4"),
                        "-vf", f"fps={FPS},crop=608:1080:{x0}:0,scale={W}:{H}:flags=lanczos", "-q:v", "2", os.path.join(d, "%04d.jpg")], check=True)
    return d


def k2_khung(u_s):
    d = k2_dir(); n = len(os.listdir(d)); k = min(int(u_s * FPS) + 1, n)
    return Image.open(os.path.join(d, f"{k:04d}.jpg")).convert("RGB")


# ---------------- L3: N7 tr. 11, ảnh trang thật, nền ngà ----------------
L3_PDF = os.path.join(ROOT, "ho-so", "1inmm-horwitz", "doj-plea-agreement-2021.pdf"); L3_TR = 11
L3_VUNG = (66, 228, 574, 432)   # điểm PDF: dòng 8–15 của trang (bỏ cột số dòng lề trái)
L3_CUM = "purported copies of the distribution agreements were fake"
L3_TIEU = ["PLEA AGREEMENT · U.S. v. HORWITZ", "Dkt. 45 · page 11"]
NGA_L3, MUC = (244, 241, 234), (27, 31, 36)
_L3 = None


def l3_nen():
    global _L3
    if _L3: return _L3
    o = os.path.join(SCR, "n7_p11")
    if not os.path.exists(o + ".png"):
        subprocess.run(["pdftoppm", "-r", "220", "-f", str(L3_TR), "-l", str(L3_TR), "-png", "-singlefile", L3_PDF, o], check=True)
    pg = Image.open(o + ".png").convert("RGB"); s = 220 / 72.0
    x0, y0, x1, y1 = L3_VUNG; cr = pg.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))
    sc = 1000 / cr.width; cr = cr.resize((int(cr.width * sc), int(cr.height * sc)), Image.LANCZOS)
    im = Image.new("RGB", (W, H), NGA_L3); d = ImageDraw.Draw(im)
    ox, oy = 40, 560
    sh = Image.new("RGBA", (cr.width + 40, cr.height + 40), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((20, 20, cr.width + 20, cr.height + 20), fill=(0, 0, 0, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(12)); im.paste(sh, (ox - 14, oy - 8), sh); im.paste(cr, (ox, oy))
    y = 330
    for i, ln in enumerate(L3_TIEU):
        ve(d, (ox, y), ln, fnt(F_MONOB, 36 if i == 0 else 32), MUC, "l3_tieu", bg=None); y += 52
    d.line((ox, y + 14, ox + 140, y + 14), fill=DO, width=5)
    words = dung.tu_trang(L3_PDF, L3_TR); hop = []
    ws = dung.tim_cum(words, L3_CUM); lines = {}
    for (a, b, c, e, _) in ws: lines.setdefault(round(b), []).append((a, b, c, e))
    for ls in lines.values():
        a = min(v[0] for v in ls); b = min(v[1] for v in ls); c = max(v[2] for v in ls); e = max(v[3] for v in ls)
        hop.append(((a - x0) * s * sc + ox, (b - y0) * s * sc + oy, (c - x0) * s * sc + ox, (e - y0) * s * sc + oy))
    _L3 = (im, hop); return _L3


def l3_khung(t, s0):
    im, hop = l3_nen(); a = muot((t - s0 - 0.5) / 0.5)
    if a > 0:
        o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
        for (x0, y0, x1, y1) in hop:
            d.rounded_rectangle((x0 - 7, y0 - 5, x1 + 7, y1 + 5), radius=7, fill=(242, 165, 65, int(80 * a)), outline=(217, 72, 15, int(255 * a)), width=4)
        im = Image.alpha_composite(im.convert("RGBA"), o).convert("RGB")
    hx = sum((h[0] + h[2]) / 2 for h in hop) / len(hop) / W; hy = sum((h[1] + h[3]) / 2 for h in hop) / len(hop) / H
    return khung(im, ((0.5, 0.5, 1.0), (0.5 + (hx - 0.5) * 0.3, 0.5 + (hy - 0.5) * 0.3, 1.07)), (t - s0) / 4.5)


# ---------------- L2 dọc ----------------
_NEN = None


def nen():
    global _NEN
    if _NEN is None:
        im = Image.new("RGB", (W, H), THAN); d = ImageDraw.Draw(im)
        for x in range(0, W, 80): d.line((x, 0, x, H), fill=(27, 32, 38), width=1)
        for y in range(0, H, 80): d.line((0, y, W, y), fill=(27, 32, 38), width=1)
        v = Image.radial_gradient("L").resize((W, H)).point(lambda p: int(p * 0.55))
        _NEN = Image.composite(Image.new("RGB", (W, H), (8, 10, 12)), im, v)
    return _NEN.copy()


def tieu(d, s, t, t0):
    a = ap(t, t0, 0.5); ve(d, (60, 300), s, fnt(F_SERIF, 60), NGA, "do_hoa", a=a)
    d.line((60, 382, 60 + 160 * a, 382), fill=mix(TEAL, a), width=6)


def so(d, xy, s, t, t_dung, col, size, anchor="mm"):
    """Số lớn; số trung gian (trước lúc dừng) không ghi sổ chữ."""
    k = nhan(t, t_dung); ve(d, xy, s, fnt(F_BOLD, int(size * k)), col, "do_hoa", anchor, ghi=(t_dung is None or t >= t_dung))


def node(d, cx, cy, ic, label, a, w=560, h=230, acc=False):
    if a <= 0.01: return
    oy = (1 - a) * 24; c = mix(DO if acc else NGA, a)
    d.rounded_rectangle((cx - w / 2, cy - h / 2 + oy, cx + w / 2, cy + h / 2 + oy), radius=20, outline=c, width=4, fill=mix((30, 36, 43), a))
    icon(d, ic, cx, cy - 34 + oy, 104, DO if acc else NGA, a)
    ve(d, (cx, cy + 68 + oy), label, fnt(F_SANSB, 42), NGA, "do_hoa", "mm", a=a)


def dau_v(im, cx, cy, s, a, size=60, ang=-8):
    """Dấu đóng 'FAKE — admitted' (đỏ cam — điểm nhấn duy nhất của đồ hoạ)."""
    if a <= 0.01: return
    reg(s, "do_hoa"); f = fnt(F_BOLD, size); tmp = ImageDraw.Draw(im); tw_ = int(tmp.textlength(s, font=f)) + 44
    o = Image.new("RGBA", (tw_, size + 34), (0, 0, 0, 0)); od = ImageDraw.Draw(o)
    od.rounded_rectangle((3, 3, tw_ - 4, size + 30), radius=10, fill=(20, 24, 29, int(215 * a)), outline=DO + (int(255 * a),), width=6)
    od.text((22, 12), s, font=f, fill=DO + (int(255 * a),))
    sc = 1 + 0.25 * (1 - a); o = o.resize((int(o.width * sc), int(o.height * sc))).rotate(ang, expand=True, resample=Image.BICUBIC)
    im.paste(o, (int(cx - o.width / 2), int(cy - o.height / 2)), o)


def GA(t):  # S005: kỳ phiếu 6 hoặc 12 tháng → +25–45 % (đếm), điểm nhấn = 25–45 %
    im = nen(); d = ImageDraw.Draw(im)
    t6 = tw("S005", "six"); t25 = tw("S005", "twenty"); t45 = tw("S005", "forty")
    tieu(d, "PROMISSORY NOTES", t, CS["S005"][0] - 0.2)
    a = ap(t, t6 - 0.3); icon(d, "dongho", CX, 560, 210, NGA, a)
    ve(d, (CX, 740), "6 OR 12 MONTHS", fnt(F_BOLD, 76), NGA, "do_hoa", "mm", a=a)
    ve(d, (CX, 810), "typically came due", fnt(F_SANS, 36), XAM, "do_hoa", "mm", a=a)
    p = [(CX, 860), (CX, 950)]; arrow(d, p, XAM, ap(t, t25 - 0.5), prog=ap(t, t25 - 0.5, 0.5)); hat(d, p, t, HP, ap(t, t25 - 0.2), n=3, v=0.6)
    if t >= t25 - 0.3:
        lo = dem(t, t25, 25, 0.5); hi = 25 + dem(t, t45, 20, 0.4)
        s = f"{lo:.0f}%" if t < t45 else f"25–{hi:.0f}%"
        so(d, (CX, 1060), s, t, t45 + 0.4 if t >= t45 else t25 + 0.5, DO, 180)
        ve(d, (CX, 1175), "PROMISED RETURN", fnt(F_SANSB, 44), NGA, "do_hoa", "mm", a=ap(t, t25))
    return im


def GB(t):  # S006–S007: quyền phim → nền tảng → hợp đồng phân phối → dấu FAKE — admitted
    im = nen(); d = ImageDraw.Draw(im); s0 = [c for c in CANH if c["ma"] == "GB"][0]["s"]
    tst = tw("S006", "streaming"); tdi = tw("S007", "distribution"); tf = tw("S007", "fake")
    tieu(d, "HE TOLD INVESTORS", t, s0)
    node(d, CX, 520, "phim", "FILM RIGHTS", ap(t, s0 + 0.1))
    tat = 1 - ap(t, tf, 0.4)  # dòng tiền tắt khi dấu FAKE đóng
    p1 = [(CX, 645), (CX, 700)]; arrow(d, p1, XAM, ap(t, tst - 0.6), prog=ap(t, tst - 0.6, 0.4))
    node(d, CX, 820, "manhinh", "STREAMING PLATFORMS", ap(t, tst - 0.2))
    p2 = [(CX, 945), (CX, 1000)]; arrow(d, p2, XAM, ap(t, tdi - 0.6), prog=ap(t, tdi - 0.6, 0.4))
    node(d, CX, 1120, "giay", "DISTRIBUTION DEALS", ap(t, tdi - 0.2))
    for p, t_ in ((p1, tst), (p2, tdi)): hat(d, p, t, HP, ap(t, t_) * tat, n=2, v=0.7, r=6)
    dau_v(im, CX + 40, 1085, "FAKE — admitted", ap(t, tf - 0.1, 0.35))
    return im


def GC(t):  # S009: ít nhất $650,000,000+ (đếm), điểm nhấn = con số
    im = nen(); d = ImageDraw.Draw(im); t1 = tw("S009", "six"); tc = tw("S009", "came"); s0 = CS["S009"][0]
    ve(d, (CX, 640), "AT LEAST", fnt(F_SANSB, 50), XAM, "do_hoa", "mm", a=ap(t, s0 - 0.3))
    het = t1 + 1.2; dong = ap(t, s0 - 0.2) * (1 - ap(t, het + 0.3, 0.5))
    for x in (140, 330, 510, 690, 880):
        hat(d, [(x, 380), (CX, 700)], t, HP, dong, n=4, v=0.55, r=7)
    if t >= t1 - 0.3:
        v = dem(t, t1, 650_000_000, 1.2); s = f"${v:,.0f}" + ("+" if t >= het else "")
        so(d, (CX, 800), s, t, het, DO, 116)
    ve(d, (CX, 930), "CAME IN", fnt(F_SANSB, 50), NGA, "do_hoa", "mm", a=ap(t, tc - 0.2))
    return im


def GD(t):  # S010: SENTENCED IN 2022 · 20 YEARS (đếm, 20 ô năm), điểm nhấn = 20 YEARS
    im = nen(); d = ImageDraw.Draw(im); s0 = [c for c in CANH if c["ma"] == "GD"][0]["s"]
    ty = tw("S010", "years"); t20 = ty - 0.3; tp = tw("S010", "prison")
    ve(d, (CX, 470), "SENTENCED IN 2022", fnt(F_BOLD, 54), NGA, "do_hoa", "mm", a=ap(t, s0))
    n = dem(t, t20, 20, 1.2)
    for k in range(20):
        r, c = divmod(k, 5); x = CX - 2 * 132 + c * 132; y = 600 + r * 110
        on = n >= k + 0.999 or (t >= t20 + 1.2)
        d.rounded_rectangle((x - 50, y - 40, x + 50, y + 40), radius=10, outline=mix(XAM, ap(t, s0)), width=3, fill=mix(NGA, 0.85) if on else mix((30, 36, 43), ap(t, s0)))
    if t >= t20 - 0.3:
        so(d, (CX, 1060), f"{n:.0f} YEARS", t, t20 + 1.2, DO, 160)
    ve(d, (CX, 1210), "IN PRISON", fnt(F_SANSB, 50), NGA, "do_hoa", "mm", a=ap(t, tp - 0.2))
    return im


G = {"GA": GA, "GB": GB, "GC": GC, "GD": GD}


# ---------------- lớp chữ ----------------
def nhan_nguon(o, cau, mh):
    """Nhãn ILLUSTRATIVE (trên trái) + nhãn tầng + dòng nguồn (dưới, trên vùng 15 % đáy)."""
    d = ImageDraw.Draw(o)
    if mh:
        f = fnt(F_SANSB, 30); w = d.textlength(mh, font=f); reg(mh, "nhan")
        d.rounded_rectangle((50, 150, 50 + w + 32, 200), radius=9, fill=(110, 116, 125, 230)); d.text((66, 157), mh, font=f, fill="white")
    if not cau: return
    nh = dung.nhan_tang(cau); src = dung.nguon(cau)
    if not (nh or src): return
    f2 = fnt(F_MONO, 24); ls = wrap(d, src, f2, SAFE_X - 70) if src else []
    y1 = SAFE_Y - 14; y0 = y1 - 36 * len(ls) - (70 if nh else 0) - 24
    d.rectangle((0, y0, W, y1 + 6), fill=(14, 17, 21, 200))
    y = y0 + 16
    if nh:
        txt, col = nh; ky, chu = txt[0], txt[1:]; fk = fnt(F_SYM, 30); fc = fnt(F_SANSB, 30); reg(txt, "nhan")
        wk = d.textlength(ky, font=fk); w = wk + d.textlength(chu, font=fc)
        d.rounded_rectangle((50, y, 50 + w + 32, y + 50), radius=8, fill=col + (240,))
        d.text((66, y + 7), ky, font=fk, fill="white"); d.text((66 + wk, y + 8), chu, font=fc, fill="white"); y += 66
    if src:
        reg(src, "nguon")
        for ln in ls: d.text((54, y), ln, font=f2, fill=(214, 210, 200)); y += 36


_NH = {}


def lop_nhan(i, t):
    c = CANH[i]; cau = c["cau"] or cau_luc(t)
    mh = None
    if c["lop"] in ("L1", "veo"): mh = "ILLUSTRATIVE — not the real person" if c["nguoi"] else "ILLUSTRATIVE"
    k = (cau, mh)
    if k not in _NH:
        o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); nhan_nguon(o, cau if c["lop"] != "cuoi" else None, mh); _NH[k] = o
    return _NH[k]


# Phụ đề: cụm chữ của lời đã duyệt, hiện theo mốc whisper. Số viết bằng chữ số khi hiện (bảng đổi trong doi_chieu.py).
PHU_DE = {
    "S004": [("The man at the center of it", "the"), ("was Zachary Horwitz,", "was"), ("an actor in Los Angeles", "an"), ("who used the screen name", "who"), ("Zach Avery.", "zach")],
    "S005": [("His company issued", "his"), ("promissory notes", "promissory"), ("that typically came due", "that"), ("in six or twelve months,", "in"),
             ("with a promised return", "with"), ("of 25 to 45 percent.", "of")],
    "S006": [("The money, he told investors,", "the"), ("would buy film rights", "would"), ("to be licensed", "to"), ("to streaming platforms", ("to", 1)),
             ("such as HBO and Netflix.", "such")],
    "S007": [("In his plea agreement,", "in"), ("he admitted", "he"), ("the distribution deals", "the"), ("were fake.", "were")],
    "S009": [("At least", "at"), ("$650 million", "six"), ("came in.", "came")],
    "S010": [("In 2022,", "in"), ("a federal judge", "a"), ("sentenced him", "sentenced"), ("to 20 years in prison.", "to")],
    "S011": [("This is the story", "this"), ("of how that money", "of"), ("was rerouted,", "was"), ("and the red flags", "and"), ("you can spot next time.", "you")],
}
# S008 (KBCB): thẻ nền tối, cả câu chia hai nửa theo lời (HIEN-CHUONG §3 luật 8e; PHONG-CACH-HINH §1)
KBCB = [("HBO and Netflix were not accused of wrongdoing in these cases;", "hbo"),
        ("according to the SEC, neither company ever did business with 1inMM.", "according")]


def _moc(cid, ds):
    out = []
    for i, (s, key) in enumerate(ds):
        k, n = (key if isinstance(key, tuple) else (key, 0)); c0, c1 = CS[cid]
        hits = [w["s"] for w in TU if c0 - 0.25 <= w["s"] <= c1 + 0.25 and norm(w["w"]) == k]   # khớp TỪ CHÍNH XÁC (tránh "to" ↔ "told")
        a = hits[n] if len(hits) > n else None
        assert a is not None, (cid, s)
        out.append([s, a])
    for i in range(len(out)):
        out[i].append(out[i + 1][1] if i + 1 < len(out) else CS[cid][1] + 0.35)
    return out


PD = [(s, a, b, "phu_de") for cid, ds in PHU_DE.items() for s, a, b in _moc(cid, ds)]
PD += [(s, a, b, "kbcb") for s, a, b in _moc("S008", KBCB)]
PD = [(s, max(a, 1.5), b, k) for s, a, b, k in PD if b > 1.5]   # không phụ đề trong 1,5 s chữ móc câu


def lop_phu_de(f, t):
    d = ImageDraw.Draw(f)
    for s, a, b, k in PD:
        if not (a <= t < b): continue
        if k == "phu_de":
            fo = fnt(F_BOLD, 66); ls = wrap(d, s, fo, 820); reg(s, "phu_de")
            y = 1330 - 40 * (len(ls) - 1)
            for ln in ls:
                d.text((CX, y), ln, font=fo, fill=(255, 255, 255), anchor="mm", stroke_width=7, stroke_fill=(0, 0, 0)); y += 82
        else:
            fo = fnt(F_SERIF, 54); ls = wrap(d, s, fo, 800); reg(s, "kbcb"); h = 70 * len(ls) + 56
            y0 = 1390 - h
            o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(o)
            od.rectangle((40, y0, SAFE_X - 12, y0 + h), fill=(14, 17, 21, 228)); od.rectangle((40, y0, 50, y0 + h), fill=TEAL + (255,))
            f.paste(Image.alpha_composite(f.convert("RGBA"), o).convert("RGB"))
            y = y0 + 28
            for ln in ls: d.text((80, y), ln, font=fo, fill=NGA); y += 70
    return f


def lop_ten(f, t):
    """Thẻ tên S004 (nền tối, như MR-6)."""
    s, e = CS["S004"]; a0, b0 = max(s + 0.6, 1.6), min(s + 4.6, e + 0.2)
    if not (a0 <= t <= b0): return f
    al = min((t - a0) / 0.3, (b0 - t) / 0.3, 1.0)
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    d.rectangle((0, 960, W, 1150), fill=(14, 17, 21, int(215 * al)))
    d.text((54, 978), "Zachary Horwitz", font=fnt(F_SERIF, 70), fill=NGA + (int(255 * al),)); reg("Zachary Horwitz", "ten")
    s2 = "aka “Zach Avery” · actor, Los Angeles"; d.text((56, 1074), s2, font=fnt(F_SANS, 36), fill=(216, 212, 202, int(255 * al))); reg(s2, "ten")
    return Image.alpha_composite(f.convert("RGBA"), o).convert("RGB")


MOC_CAU = ["25 to 45 percent", "six or twelve months"]   # chữ móc câu — chỉ cụm có trong lời đã duyệt (lệnh MR-SH1)


def lop_moc(f, t):
    if t >= 1.5: return f
    al = 1.0 if t < 1.25 else max(0.0, (1.5 - t) / 0.25)
    o = Image.new("RGBA", (W, H), (8, 10, 12, int(120 * al))); d = ImageDraw.Draw(o)
    d.text((CX, 820), MOC_CAU[0], font=fnt(F_BOLD, 100), fill=DO + (int(255 * al),), anchor="mm", stroke_width=6, stroke_fill=(8, 10, 12, int(255 * al)))
    d.text((CX, 950), MOC_CAU[1], font=fnt(F_BOLD, 70), fill=NGA + (int(255 * al),), anchor="mm", stroke_width=5, stroke_fill=(8, 10, 12, int(255 * al)))
    for s in MOC_CAU: reg(s, "moc_cau")
    return Image.alpha_composite(f.convert("RGBA"), o).convert("RGB")


THE_CUOI = ["Full case + 5 red flags", "→ Money Reroute"]   # nguyên văn lệnh: "Full case + 5 red flags → Money Reroute"
_CUOI = None


def the_cuoi(t):
    global _CUOI
    if _CUOI is None:
        bg = k2_khung(99).filter(ImageFilter.GaussianBlur(18)); bg = Image.blend(bg, Image.new("RGB", (W, H), (8, 10, 12)), 0.55)
        d = ImageDraw.Draw(bg)
        d.text((CX, 820), THE_CUOI[0], font=fnt(F_SERIF, 80), fill=NGA, anchor="mm")
        f = fnt(F_BOLD, 84); w1 = d.textlength("→ ", font=f); w2 = d.textlength("Money Reroute", font=f); x = CX - (w1 + w2) / 2
        d.text((x, 960), "→ ", font=f, fill=DO, anchor="lm"); d.text((x + w1, 960), "Money Reroute", font=f, fill=NGA, anchor="lm")
        d.line((CX - 160, 1050, CX + 160, 1050), fill=TEAL, width=6)
        for s in THE_CUOI: reg(s, "the_cuoi")
        _CUOI = bg
    return _CUOI.copy()


# ---------------- lắp khung ----------------
def ve_canh(i, t):
    c = CANH[i]; ma = c["ma"]; u = (t - c["s"]) / (c["e"] - c["s"] + T_HOA)
    if c["lop"] == "L1": f = toi_tren_duoi(khung(cat_doc(ma, c["cx"]), chuyen(ma), u))
    elif c["lop"] == "veo": f = toi_tren_duoi(k2_khung(max(t - c["s"], 0)))
    elif c["lop"] == "L3": f = l3_khung(t, c["s"])
    elif c["lop"] == "L2": f = G[ma](t)
    else: return the_cuoi(t)
    return Image.alpha_composite(f.convert("RGBA"), lop_nhan(i, t)).convert("RGB")


def khung_luc(t):
    i = max(j for j, c in enumerate(CANH) if c["s"] <= t + 1e-6)
    f = ve_canh(i, t)
    if i > 0 and t < CANH[i]["s"] + T_HOA: f = Image.blend(ve_canh(i - 1, t), f, muot((t - CANH[i]["s"]) / T_HOA))
    if t < T_CUOI:
        f = lop_ten(f, t); f = lop_phu_de(f, t); f = lop_moc(f, t)
    if t > TONG - 0.3: f = Image.blend(Image.new("RGB", (W, H)), f, max(TONG - t, 0) / 0.3)
    return f


def khuc(args):
    k, a, b, out = args
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), out], stdin=subprocess.PIPE)
    for n in range(int(round(a * FPS)), int(round(b * FPS))): p.stdin.write(khung_luc(n / FPS).tobytes())
    p.stdin.close(); p.wait()
    json.dump(sorted(CHU), open(out + ".chu.json", "w"), ensure_ascii=False)
    return out


# ---------------- âm ----------------
def lufs(f, extra=None):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, *(["-af", extra] if extra else ["-af", "ebur128=peak=true"]), "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]); TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r); return I, (float(TP[-1]) if TP else None)


def am(dst):
    giong = os.path.join(ROOT, "lab", "mr4", "tts", "P01_l2.mp3"); n1 = os.path.join(ROOT, "lab", "mr5", "nhac", "N1_mo.mp3")
    Iv, _ = lufs(giong); Im, _ = lufs(n1)
    g = (Iv - 20.0) - Im   # nhạc thấp hơn lời 20 LU trong lúc có lời
    t_het = GIONG_HET
    # N1 dài 40 s < 55 s → nối N1 với chính nó từ giây 6 (hoà 4 s); mức: +6 dB trong chữ móc câu, g khi có lời, +8 dB ở thẻ cuối, tắt dần 1,5 s
    vol = (f"volume='pow(10,({g:.2f}+6*(1-min(max((t-0.4)/0.5,0),1))+8*min(max((t-{t_het + 0.2:.2f})/0.6,0),1))/20)':eval=frame")
    fl = [f"[1:a]aresample=48000,atrim=0:40,asetpts=PTS-STARTPTS[m1]", f"[2:a]aresample=48000,atrim=6:40,asetpts=PTS-STARTPTS[m2]",
          f"[m1][m2]acrossfade=d=4[m]", f"[m]atrim=0:{TONG},{vol},afade=t=out:st={TONG - 1.5}:d=1.5[nh]",
          f"[0:a]aresample=48000,adelay={int(OFF * 1000)}|{int(OFF * 1000)},apad,atrim=0:{TONG}[v]",
          f"[v][nh]amix=inputs=2:normalize=0,atrim=0:{TONG}[mix]"]
    tmp = dst + ".raw.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", giong, "-i", n1, "-i", n1, "-filter_complex", ";".join(fl), "-map", "[mix]",
                    "-ar", "48000", "-c:a", "pcm_s16le", tmp], check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
          f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-c:a", "pcm_s16le", dst], check=True)
    return {"giong_LUFS": Iv, "N1_LUFS": Im, "N1_gain_dB": round(g, 2), "nhac_duoi_loi_LU": 20.0}


def main():
    a = sys.argv
    if "--khung" in a:
        t = float(a[a.index("--khung") + 1]); f = os.path.join(SCR, f"khung_{t:.2f}.png"); khung_luc(t).save(f); print(f); return
    xem = os.path.join(ROOT, "reports", "mrsh1", "xem"); os.makedirs(xem, exist_ok=True); k2_dir(); l3_nen()
    n = 4; ranh = [round(TONG * k / n * FPS) / FPS for k in range(n + 1)]
    jobs = [(k, ranh[k], ranh[k + 1], os.path.join(SCR, f"khuc{k}.mp4")) for k in range(n)]
    with Pool(n) as p: outs = p.map(khuc, jobs)
    chu = set()
    for o in outs: chu |= set(tuple(x) for x in json.load(open(o + ".chu.json")))
    json.dump([{"chuoi": s, "loai": k} for s, k in sorted(chu)], open(os.path.join(ROOT, "reports", "mrsh1", "chu_tren_hinh.json"), "w"), ensure_ascii=False, indent=0)
    lst = os.path.join(SCR, "ds.txt"); open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
    vid = os.path.join(SCR, "hinh.mp4"); subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid], check=True)
    wav = os.path.join(SCR, "am.wav"); info = am(wav); I, TP = lufs(wav)
    out = os.path.join(xem, "short1.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-t", str(TONG),
                    "-movflags", "+faststart", out], check=True)
    I2, TP2 = lufs(out)
    info.update({"tong_s": TONG, "fps": FPS, "kich_thuoc": f"{W}x{H}", "giong_bat_dau_s": OFF, "giong_het_s": round(GIONG_HET, 2), "the_cuoi_s": [T_CUOI, TONG],
                 "am_wav": {"I": I, "TP": TP}, "am_mp4": {"I": I2, "TP": TP2}, "canh": CANH})
    json.dump(info, open(os.path.join(ROOT, "reports", "mrsh1", "do_am.json"), "w"), ensure_ascii=False, indent=1)
    print("âm", I, TP, "→ mp4", I2, TP2); print("xong", out)


if __name__ == "__main__":
    main()
