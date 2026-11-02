#!/usr/bin/env python3
"""MR-6 · Đồ hoạ động L2 (PHONG-CACH-HINH v1 §2) — vẽ bằng mã, 0 USD, dựng lại được. Dùng bởi scripts/mr6/dung.py.
Luật: nền than #14181D + lưới mờ; hiện dần theo MỐC TỪ của giọng (reports/mr6/moc_cau.json); tiền = hạt chạy dọc đường nối;
một điểm nhấn đỏ cam #D9480F mỗi đồ hoạ; số đếm lên rồi dừng có nhấn; ≤ 1 hiệu ứng nổi bật / 2 s; chuyển động có easing.
Nhãn tầng + nguồn do dung.py vẽ ở lớp tĩnh góc dưới (không vẽ ở đây). Mọi chữ đi qua txt() để ghi sổ đối chiếu (CHU)."""
import math, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1920, 1080
THAN, TEAL, HP, NGA, XAM, DO, HPA = (20, 24, 29), (43, 122, 120), (192, 138, 62), (244, 241, 234), (138, 143, 152), (217, 72, 15), (183, 121, 31)
F_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"; F_SANSB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
F_BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; F_SYM = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf"; F_MONOB = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-SemiBold.ttf"
_F = {}
CHU = set()  # mọi chuỗi chữ đã vẽ (đối chiếu với loi.json + nguồn + nhãn: scripts/mr6/doi_chieu_chu.py)


def fnt(f, s):
    k = (f, s)
    if k not in _F: _F[k] = ImageFont.truetype(f, s)
    return _F[k]


def muot(u): u = min(max(u, 0.0), 1.0); return u * u * (3 - 2 * u)
def ap(t, t0, d=0.5): return muot((t - t0) / d) if t0 is not None else 0.0
def mix(c, a, bg=THAN): return tuple(int(bg[i] + (c[i] - bg[i]) * a) for i in range(3))


def txt(d, xy, s, f, col, a=1.0, anchor="la", bg=THAN):
    if a <= 0.01: return
    CHU.add(s); d.text(xy, s, font=f, fill=mix(col, a, bg), anchor=anchor)


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


# ---------------- icon (nét đơn, cùng kiểu) ----------------
def icon(d, kind, cx, cy, s, col, a=1.0, w=5):
    c = mix(col, a)
    if a <= 0.01: return
    if kind == "nguoi":
        for dx in (-0.32, 0.32, 0):
            r = s * 0.16; x = cx + dx * s; y = cy - s * 0.12 + (0.06 * s if dx else 0)
            d.ellipse((x - r, y - r - s * 0.12, x + r, y + r - s * 0.12), outline=c, width=w)
            d.arc((x - r * 1.9, y + r * 0.6, x + r * 1.9, y + r * 4.2), 180, 360, fill=c, width=w)
    elif kind == "mot_nguoi":
        r = s * 0.2; d.ellipse((cx - r, cy - s * 0.42 - r, cx + r, cy - s * 0.42 + r), outline=c, width=w)
        d.arc((cx - s * 0.38, cy - s * 0.12, cx + s * 0.38, cy + s * 0.6), 180, 360, fill=c, width=w)
    elif kind == "cty":
        d.rectangle((cx - s * 0.35, cy - s * 0.45, cx + s * 0.35, cy + s * 0.45), outline=c, width=w)
        for i in range(3):
            for j in range(2):
                x = cx - s * 0.2 + j * s * 0.28; y = cy - s * 0.3 + i * s * 0.25
                d.rectangle((x, y, x + s * 0.12, y + s * 0.12), fill=c)
    elif kind == "phim":
        d.ellipse((cx - s * 0.42, cy - s * 0.42, cx + s * 0.42, cy + s * 0.42), outline=c, width=w)
        for k in range(5):
            an = k * 2 * math.pi / 5; x = cx + math.cos(an) * s * 0.22; y = cy + math.sin(an) * s * 0.22
            d.ellipse((x - s * 0.08, y - s * 0.08, x + s * 0.08, y + s * 0.08), outline=c, width=max(2, w - 2))
    elif kind == "manhinh":
        d.rounded_rectangle((cx - s * 0.48, cy - s * 0.32, cx + s * 0.48, cy + s * 0.26), radius=8, outline=c, width=w)
        d.polygon([(cx - s * 0.1, cy - s * 0.14), (cx - s * 0.1, cy + s * 0.08), (cx + s * 0.12, cy - s * 0.03)], fill=c)
        d.line((cx - s * 0.2, cy + s * 0.4, cx + s * 0.2, cy + s * 0.4), fill=c, width=w)
    elif kind == "xu":
        for k in range(3):
            y = cy + s * 0.2 - k * s * 0.18; d.ellipse((cx - s * 0.36, y - s * 0.12, cx + s * 0.36, y + s * 0.12), outline=c, width=w)
    elif kind == "giay":
        d.polygon([(cx - s * 0.3, cy - s * 0.42), (cx + s * 0.14, cy - s * 0.42), (cx + s * 0.3, cy - s * 0.26), (cx + s * 0.3, cy + s * 0.42),
                   (cx - s * 0.3, cy + s * 0.42)], outline=c, width=w)
        for k in range(4): d.line((cx - s * 0.18, cy - s * 0.18 + k * s * 0.13, cx + s * 0.18, cy - s * 0.18 + k * s * 0.13), fill=c, width=max(2, w - 2))
    elif kind == "dongho":
        d.ellipse((cx - s * 0.42, cy - s * 0.42, cx + s * 0.42, cy + s * 0.42), outline=c, width=w)
        d.line((cx, cy, cx, cy - s * 0.28), fill=c, width=w); d.line((cx, cy, cx + s * 0.2, cy + s * 0.08), fill=c, width=w)
    elif kind == "nha":
        d.polygon([(cx - s * 0.42, cy - s * 0.05), (cx, cy - s * 0.42), (cx + s * 0.42, cy - s * 0.05)], outline=c, width=w)
        d.rectangle((cx - s * 0.3, cy - s * 0.05, cx + s * 0.3, cy + s * 0.4), outline=c, width=w)
        d.rectangle((cx - s * 0.08, cy + s * 0.12, cx + s * 0.08, cy + s * 0.4), fill=c)
    elif kind == "toa":
        d.polygon([(cx - s * 0.45, cy - s * 0.2), (cx, cy - s * 0.45), (cx + s * 0.45, cy - s * 0.2)], outline=c, width=w)
        for k in range(4): x = cx - s * 0.3 + k * s * 0.2; d.line((x, cy - s * 0.12, x, cy + s * 0.3), fill=c, width=w)
        d.line((cx - s * 0.45, cy + s * 0.38, cx + s * 0.45, cy + s * 0.38), fill=c, width=w)
    elif kind == "thu":
        d.rectangle((cx - s * 0.42, cy - s * 0.28, cx + s * 0.42, cy + s * 0.28), outline=c, width=w)
        d.line((cx - s * 0.42, cy - s * 0.28, cx, cy + s * 0.05, cx + s * 0.42, cy - s * 0.28), fill=c, width=w)
    elif kind == "may_bay":
        d.line((cx - s * 0.45, cy, cx + s * 0.45, cy), fill=c, width=w + 2)
        d.polygon([(cx - s * 0.05, cy), (cx - s * 0.25, cy - s * 0.35), (cx + s * 0.05, cy)], fill=c)
        d.polygon([(cx - s * 0.05, cy), (cx - s * 0.25, cy + s * 0.35), (cx + s * 0.05, cy)], fill=c)


def node(d, cx, cy, ic, label, a, col=NGA, w=300, h=230, acc=False, sub=None, dash=False):
    if a <= 0.01: return
    oy = (1 - a) * 24; c = mix(DO if acc else col, a)
    box = (cx - w / 2, cy - h / 2 + oy, cx + w / 2, cy + h / 2 + oy)
    if dash: dashed_rect(d, box, c, 4)
    else: d.rounded_rectangle(box, radius=18, outline=c, width=4, fill=mix((30, 36, 43), a))
    if ic: icon(d, ic, cx, cy - h * 0.16 + oy, h * 0.42, DO if acc else col, a)
    f = fnt(F_SANSB, 30 if len(label) < 18 else 25)
    ys = cy + h * 0.2 + oy if ic else cy - 20 * (label.count("\n")) + oy
    for i, ln in enumerate(label.split("\n")):
        txt(d, (cx, ys + i * 34), ln, f, DO if acc else NGA, a, "mm")
    if sub: txt(d, (cx, cy + h / 2 + 30 + oy), sub, fnt(F_SANS, 24), XAM, a, "mm")


def dashed_rect(d, box, c, w, dl=18):
    x0, y0, x1, y1 = box
    for (a, b) in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        dashed(d, [a, b], c, w, dl)


def dashed(d, pts, c, w, dl=18, prog=1.0):
    segs = poly_cut(pts, prog)
    for (x0, y0), (x1, y1) in zip(segs, segs[1:]):
        L = math.hypot(x1 - x0, y1 - y0); n = max(1, int(L // dl))
        for k in range(0, n, 2):
            u0, u1 = k / n, min((k + 1) / n, 1)
            d.line((x0 + (x1 - x0) * u0, y0 + (y1 - y0) * u0, x0 + (x1 - x0) * u1, y0 + (y1 - y0) * u1), fill=c, width=w)


def poly_len(p): return sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(p, p[1:]))


def poly_at(p, u):
    L = poly_len(p) * u
    for a, b in zip(p, p[1:]):
        l = math.hypot(b[0] - a[0], b[1] - a[1])
        if L <= l and l > 0: return (a[0] + (b[0] - a[0]) * L / l, a[1] + (b[1] - a[1]) * L / l)
        L -= l
    return p[-1]


def poly_cut(p, u):
    if u >= 1: return p
    L = poly_len(p) * u; out = [p[0]]
    for a, b in zip(p, p[1:]):
        l = math.hypot(b[0] - a[0], b[1] - a[1])
        if L <= l:
            out.append((a[0] + (b[0] - a[0]) * L / max(l, 1e-6), a[1] + (b[1] - a[1]) * L / max(l, 1e-6))); return out
        out.append(b); L -= l
    return out


def arrow(d, pts, col, a, prog=1.0, w=5, dash=False, head=True):
    if a <= 0.01 or prog <= 0.01: return
    c = mix(col, a); seg = poly_cut(pts, prog)
    if dash: dashed(d, pts, c, w, prog=prog)
    else: d.line(seg, fill=c, width=w, joint="curve")
    if head and prog > 0.97:
        (x0, y0), (x1, y1) = pts[-2], pts[-1]; an = math.atan2(y1 - y0, x1 - x0); L = 22
        d.polygon([(x1, y1), (x1 - L * math.cos(an - 0.45), y1 - L * math.sin(an - 0.45)), (x1 - L * math.cos(an + 0.45), y1 - L * math.sin(an + 0.45))], fill=c)


def hat(d, pts, t, col, a, n=7, v=0.28, r=7, pulse=False):
    """Hạt tiền chạy dọc đường nối (t = giây toàn cục)."""
    if a <= 0.01: return
    rr = r * (1 + (0.25 * math.sin(t * 6) if pulse else 0))
    for k in range(n):
        u = (t * v + k / n) % 1.0; x, y = poly_at(pts, u)
        fade = min(u / 0.1, (1 - u) / 0.1, 1.0)
        d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=mix(col, a * fade))


def dem(t, t0, v, d=1.6):
    """Số đếm lên 0 → v (easing ra), dừng ở v."""
    if t0 is None or t < t0: return 0
    u = min((t - t0) / d, 1.0); return v * (1 - (1 - u) ** 3)


def nhan(t, t0):
    """Hệ số phóng nhẹ khi số dừng (một lần, ~0,5 s)."""
    if t0 is None: return 1.0
    u = (t - t0); return 1.0 + 0.08 * math.exp(-((u - 0.25) / 0.18) ** 2)


def tieu(d, s, t, t0, sub=None):
    a = ap(t, t0, 0.6); txt(d, (120, 96), s, fnt(F_SERIF, 54), NGA, a)
    d.line((120, 168, 120 + 160 * a, 168), fill=mix(DO, a), width=5)
    if sub: txt(d, (120, 190), sub, fnt(F_SANS, 28), XAM, a)


def so_lon(d, xy, s, t, t0, col=NGA, size=150, anchor="mm"):
    k = nhan(t, t0); f = fnt(F_BOLD, int(size * k)); txt(d, xy, s, f, col, ap(t, t0 - 0.3 if t0 else None, 0.3), anchor)


def dau(d, cx, cy, s, a, ang=-8, size=44):
    """Dấu đóng 'FAKE — admitted' (chữ vẽ, xoay nhẹ)."""
    if a <= 0.01: return
    f = fnt(F_BOLD, size); tw = int(d.textlength(s, font=f)) + 40
    o = Image.new("RGBA", (tw, size + 30), (0, 0, 0, 0)); od = ImageDraw.Draw(o)
    od.rounded_rectangle((2, 2, tw - 3, size + 27), radius=8, outline=DO + (int(255 * a),), width=5)
    CHU.add(s); od.text((20, 12), s, font=f, fill=DO + (int(255 * a),))
    sc = 1 + 0.25 * (1 - a); o = o.resize((int(o.width * sc), int(o.height * sc))).rotate(ang, expand=True, resample=Image.BICUBIC)
    d._image.paste(o, (int(cx - o.width / 2), int(cy - o.height / 2)), o)


def cross(d, cx, cy, s, col, a, w=8):
    if a <= 0.01: return
    c = mix(col, a); p = s * a
    d.line((cx - s, cy - s, cx - s + 2 * p, cy - s + 2 * p), fill=c, width=w)
    if a > 0.5: q = (a - 0.5) * 2 * 2 * s; d.line((cx + s, cy - s, cx + s - q, cy - s + q), fill=c, width=w)


# =============== các đồ hoạ (mỗi lớp nhận hàm mốc từ tw(cau, từ, lần)) ===============
class G:
    def __init__(self, tw, cs): self.tw = tw; self.cs = cs  # cs: {cau: (s, e)} mốc giọng


class G01(G):  # S005 kỳ phiếu
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = self.cs["S005"][0]; t6 = tw("S005", "six"); t25 = tw("S005", "twenty"); t45 = tw("S005", "forty")
        tieu(d, "PROMISSORY NOTES", t, t0 - 0.2)
        a = ap(t, t6); icon(d, "dongho", 520, 470, 220, NGA, a); txt(d, (520, 660), "6 or 12 MONTHS", fnt(F_BOLD, 64), NGA, a, "mm")
        txt(d, (520, 720), "typically due", fnt(F_SANS, 30), XAM, a, "mm")
        arrow(d, [(700, 520), (1000, 520)], XAM, ap(t, t25 - 0.4), prog=ap(t, t25 - 0.4, 0.6))
        hat(d, [(700, 520), (1000, 520)], t, HP, ap(t, t25), n=4, v=0.5)
        if t25 and t >= t25 - 0.3:
            lo = dem(t, t25, 25, 0.9); s = f"{lo:.0f}%" if not (t45 and t >= t45) else f"25–{dem(t, t45, 45, 0.9):.0f}%"
            so_lon(d, (1380, 500), s, t, t45 if (t45 and t >= t45) else t25, DO, 170)
            txt(d, (1380, 650), "PROMISED RETURN", fnt(F_SANSB, 40), NGA, ap(t, t25), "mm")
        return im


class G02(G):  # S009–S010 $650M → 20 năm
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t1 = tw("S009", "six"); t2 = tw("S010", "twenty", 1) or tw("S010", "sentenced")
        up = ap(t, t2 - 0.6, 0.7) if t2 else 0; y = 470 - 150 * up; sz = int(170 - 70 * up)
        txt(d, (960, y - 140 + 40 * up), "AT LEAST", fnt(F_SANSB, 40), XAM, ap(t, t1 - 0.4), "mm")
        v = dem(t, t1, 650_000_000, 1.8); s = f"${v:,.0f}" + ("+" if t1 and t > t1 + 1.8 else "")
        if t1 and t >= t1 - 0.3: txt(d, (960, y), s, fnt(F_BOLD, sz), NGA, ap(t, t1 - 0.3, 0.3), "mm")
        txt(d, (960, y + 110 - 30 * up), "CAME IN FROM INVESTORS", fnt(F_SANSB, 36 - int(8 * up)), XAM, ap(t, t1 + 0.6), "mm")
        if t2 and t >= t2 - 0.3:
            n = dem(t, t2, 20, 1.2); so_lon(d, (960, 650), f"{n:.0f} YEARS", t, t2 + 1.2, DO, 180)
            txt(d, (960, 790), "IN PRISON · SENTENCED IN 2022", fnt(F_SANSB, 40), NGA, ap(t, t2 + 0.3), "mm")
        return im


class G03(G):  # S015–S017 lời chào mời
    X = [190, 560, 930, 1300, 1680]; Y = 470
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        T = [tw("S015", "investors"), tw("S015", "one"), tw("S015", "distribution"), tw("S016", "streaming"), tw("S016", "profit")]
        tout = tw("S016", "outside"); tback = tw("S017", "pay") or self.cs["S017"][0]
        tieu(d, "THE PITCH", t, self.cs["S015"][0] - 0.2, "as he described it to investors")
        lab = [("nguoi", "INVESTORS"), ("cty", "1inMM"), ("phim", "FILM RIGHTS"), ("manhinh", "STREAMING\nPLATFORMS"), ("xu", "PROFITS")]
        for i in range(4):
            if T[i + 1] and t > T[i + 1] - 0.5:
                p = [(self.X[i] + 140, self.Y), (self.X[i + 1] - 140, self.Y)]
                arrow(d, p, XAM, 1, prog=ap(t, T[i + 1] - 0.5, 0.5)); hat(d, p, t, HP, ap(t, T[i + 1]), n=4, v=0.45)
        for i, (ic, l) in enumerate(lab):
            node(d, self.X[i], self.Y, ic, l, ap(t, T[i]), w=260, h=230, sub=("outside the U.S." if i == 3 and tout and t > tout else None))
        if t > tback - 0.5:
            p = [(self.X[4], self.Y + 130), (self.X[4], 800), (self.X[0], 800), (self.X[0], self.Y + 130)]
            a = ap(t, tback - 0.5, 0.8); arrow(d, p, DO, 1, prog=a, w=6); hat(d, p, t, DO, ap(t, tback + 0.3), n=8, v=0.3)
            txt(d, (935, 840), "PAID BACK TO INVESTORS", fnt(F_BOLD, 40), DO, ap(t, tback), "mm")
        return im


class G04(G):  # S020–S023 kỳ phiếu = IOU
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = tw("S020", "promissory"); tiou = tw("S020", "written"); tsec = tw("S021", "securities"); tam = tw("S022", "thirtyfive") or tw("S022", "thirty")
        tdue = tw("S023", "maturity"); tret = tw("S023", "return")
        tieu(d, "PROMISSORY NOTE", t, t0 - 0.2, None)
        txt(d, (120, 190), "a written IOU: a promise to repay a set amount by a set date", fnt(F_SANS, 30), XAM, ap(t, tiou))
        a = ap(t, t0, 0.8); d.rounded_rectangle((150, 300 + 30 * (1 - a), 750, 860 + 30 * (1 - a)), radius=20, outline=mix(HP, a), width=4, fill=mix((30, 36, 43), a))
        icon(d, "giay", 450, 560, 300, HP, a)
        rows = [(tsec, "SECURITIES", "under federal law (admitted)", NGA), (tam, "AMOUNT", "$35,000 – $1.5 million", NGA), (tdue, "DUE", "6 or 12 months", NGA)]
        for i, (tt, k, v, c) in enumerate(rows):
            aa = ap(t, tt); y = 330 + i * 150 + 20 * (1 - aa)
            txt(d, (860, y), k, fnt(F_SANSB, 30), XAM, aa); txt(d, (860, y + 40), v, fnt(F_BOLD, 52), c, aa)
        if tret and t >= tret - 0.3:
            txt(d, (860, 780), "RETURN", fnt(F_SANSB, 30), XAM, ap(t, tret - 0.3))
            lo = dem(t, tret, 25, 0.8); hi = dem(t, tret + 0.8, 45, 0.8)
            so_lon(d, (860, 820), f"+{lo:.0f}–{max(hi, lo):.0f}%", t, tret + 1.6, DO, 96, "la")
        return im


class G05(G):  # S026–S028 phép tính
    def bar(self, d, x, frac, col, a, lab, val, t, tv):
        base = 860; hmax = 560; h = hmax * frac * a
        d.rectangle((x, base - h, x + 230, base), fill=mix(col, 0.85 * a))
        txt(d, (x + 115, base + 40), lab, fnt(F_SANSB, 28), NGA, a, "mm")
        if a > 0.05: txt(d, (x + 115, base - h - 50), val, fnt(F_BOLD, int(64 * nhan(t, tv))), col, a, "mm")

    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t35 = tw("S026", "thirtyfive") or tw("S026", "thirty"); tre = tw("S027", "reinvest"); t182 = tw("S027", "one", 0) ; t82 = tw("S027", "eightytwo") or tw("S027", "eighty")
        t70 = tw("S028", "seventy")
        tieu(d, "OVER THE LIFE OF THE NOTE ≠ PER YEAR", t, self.cs["S026"][0] - 0.4, "illustrative math · one six-month note listed in the SEC complaint")
        d.line((140, 860, 1780, 860), fill=XAM, width=3)
        a = ap(t, t35, 0.9); self.bar(d, 200, 0.35, HP, a, "6-MONTH NOTE", "35%", t, t35 + 0.9)
        if tre and t > tre - 0.3:
            a2 = ap(t, tre, 0.9); self.bar(d, 520, 0.35, HP, a2, "REINVESTED", "35%", t, tre + 0.9)
            txt(d, (450, 600), "×", fnt(F_BOLD, 70), NGA, a2, "mm")
            txt(d, (1250, 265), "1.35 × 1.35 = 1.8225", fnt(F_MONOB, 58), NGA, ap(t, t182 or tre + 1.5), "mm")
        if t82 and t > t82 - 0.4:
            a3 = ap(t, t82 - 0.4, 0.9); self.bar(d, 1080, 0.82, DO, a3, "PER YEAR (reinvested)", "≈ 82%", t, t82 + 0.5)
        if t70 and t > t70 - 0.4:
            a4 = ap(t, t70 - 0.4, 0.9); self.bar(d, 1420, 0.70, TEAL, a4, "PER YEAR (35% × 2)", "70%", t, t70 + 0.5)
        return im


class G06(G):  # S030 counterparties
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw; s0 = self.cs["S030"][0]
        th = tw("S030", "hbo"); tu = tw("S030", "ultimate")
        node(d, 300, 520, "nguoi", "INVESTORS", ap(t, s0)); node(d, 860, 520, "cty", "1inMM", ap(t, s0 + 0.8))
        p1 = [(450, 520), (710, 520)]; arrow(d, p1, XAM, 1, prog=ap(t, s0 + 0.6)); hat(d, p1, t, HP, ap(t, s0 + 1.2), n=4, v=0.5)
        a = ap(t, th - 0.2)
        if a > 0:
            dashed_rect(d, (1180, 330, 1760, 710), mix(DO, a), 5)
            txt(d, (1470, 470), "HBO", fnt(F_BOLD, 64), NGA, a, "mm"); txt(d, (1470, 560), "Netflix", fnt(F_BOLD, 64), NGA, a, "mm")
            txt(d, (1470, 760), "said to be the “ultimate counterparties”", fnt(F_SANSB, 32), DO, ap(t, tu), "mm")
            p2 = [(1010, 520), (1170, 520)]; arrow(d, p2, XAM, a, dash=True)
        tieu(d, "WHO WAS SAID TO BE BEHIND THE DEALS", t, s0 - 0.3, "according to the SEC")
        return im


class G07(G):  # S034–S038 phễu
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t5 = tw("S034", "five"); tsub = tw("S035", "subinvestors") or tw("S035", "sub"); tnc = tw("S035", "direct"); t250 = tw("S036", "two")
        tcont = tw("S036", "contest"); tnc2 = tw("S038", "direct")
        tieu(d, "WHERE THE MONEY CAME FROM", t, self.cs["S034"][0] - 0.3)
        node(d, 960, 300, "cty", "1inMM", ap(t, self.cs["S034"][0]), w=280, h=190)
        gx = [360, 660, 960, 1260, 1560]
        for i, x in enumerate(gx):
            a = ap(t, (t5 or 0) + i * 0.15)
            node(d, x, 560, "nguoi", "GROUP", a, w=200, h=170)
            p = [(x, 470), (960, 400)]; arrow(d, p, XAM, a * 0.8, w=3, head=False); hat(d, p, t + i * 0.3, HP, a, n=3, v=0.4, r=5)
        txt(d, (1700, 560), "5 major groups", fnt(F_SANSB, 30), NGA, ap(t, t5 + 0.8), "lm") if False else None
        txt(d, (960, 680), "AT LEAST 5 MAJOR GROUPS OF PRIVATE INVESTORS", fnt(F_SANSB, 30), NGA, ap(t, t5 + 0.6), "mm")
        if tsub and t > tsub - 0.4:
            a = ap(t, tsub - 0.4, 1.0); import random; rnd = random.Random(3)
            for k in range(140):
                x = 240 + rnd.random() * 1440; y = 790 + rnd.random() * 120
                if rnd.random() < a: d.ellipse((x - 6, y - 6, x + 6, y + 6), fill=mix(NGA, 0.7 * a))
        if t250 and t > t250 - 0.3:
            v = dem(t, t250, 250, 1.2); so_lon(d, (1680, 300), f"{v:.0f}+", t, t250 + 1.2, NGA, 100)
            txt(d, (1680, 380), "SUB-INVESTORS", fnt(F_SANSB, 30), XAM, ap(t, t250), "mm")
            txt(d, (1680, 420), "a figure he reserved the right to contest", fnt(F_SANS, 22), XAM, ap(t, tcont), "mm")
        for tt in (tnc, tnc2):
            if tt and t > tt - 0.4:
                a = ap(t, tt - 0.4, 0.6); p = [(160, 850), (160, 300), (810, 300)]
                arrow(d, p, DO, 1, prog=a, w=5, dash=True); txt(d, (190, 250), "NO DIRECT CONTRACT", fnt(F_BOLD, 38), DO, a)
                cross(d, 160, 575, 26, DO, ap(t, tt + 0.4)); break
        return im


class G08(G):  # S041–S044 trên giấy vs thực tế
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tc = tw("S041", "collateral"); ts = tw("S041", "sole"); tg = tw("S042", "generally"); td = tw("S043", "distribution"); ta = self.cs["S044"][0]
        tieu(d, "ON PAPER  vs.  IN FACT", t, self.cs["S041"][0] - 0.3)
        d.line((960, 250, 960, 840), fill=XAM, width=2)
        txt(d, (140, 260), "ON PAPER", fnt(F_SANSB, 34), HP, ap(t, self.cs["S041"][0]))
        txt(d, (1020, 260), "IN FACT — admitted", fnt(F_SANSB, 34), DO, ap(t, tg - 0.3))
        L = [(tc, "phim", "Collateral: one or more films"), (ts, "giay", "1inMM: “sole and exclusive owner” of the rights"),
             (ts + 1.2 if ts else None, "manhinh", "Distribution deals with streaming platforms")]
        for i, (tt, ic, s) in enumerate(L):
            a = ap(t, tt); y = 380 + i * 150; icon(d, ic, 190, y, 90, NGA, a); txt(d, (270, y), s, fnt(F_SANSB, 32), NGA, a, "lm")
        R = [(tg, "Rights to listed films: generally NOT acquired"), (td, "Distribution agreements with platforms: NONE")]
        for i, (tt, s) in enumerate(R):
            a = ap(t, tt); y = 380 + (i + (0 if i == 0 else 1)) * 150
            cross(d, 1070, y, 24, DO, a); txt(d, (1120, y), s, fnt(F_SANSB, 32), NGA, a, "lm")
        a = ap(t, ta)
        if a > 0:
            d.rounded_rectangle((140, 860 - 10, 1780, 960), radius=12, outline=mix(HPA, a), width=3)
            txt(d, (170, 905), "◐ The SEC alleges: no business relationships with Netflix or HBO; no distribution agreements signed with them", fnt(F_SANS, 29), NGA, a, "lm")
        return im


class G09(G):  # S046–S048 giấy tờ giả, cùng một nguồn
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tl = tw("S046", "license"); tf1 = tw("S046", "fake"); tdi = tw("S047", "distribution"); tf2 = tw("S047", "fake"); tall = tw("S048", "all")
        tieu(d, "THE PAPERWORK", t, self.cs["S046"][0] - 0.3)
        C = [(380, self.cs["S046"][0], "PROMISSORY\nNOTES", None), (960, tl, "LICENSE\nAGREEMENTS", tf1), (1540, tdi, "DISTRIBUTION\nAGREEMENTS", tf2)]
        for x, ta, lab, tf in C:
            node(d, x, 450, "giay", lab, ap(t, ta), w=380, h=300)
            if tf: dau(d, x, 470, "FAKE — admitted", ap(t, tf - 0.1, 0.35))
        if tall and t > tall - 0.4:
            a = ap(t, tall - 0.4, 0.8); node(d, 960, 860, "mot_nguoi", "ALL FROM HIM", a, w=330, h=170, acc=True)
            for x, *_ in C:
                p = [(960, 775), (x, 615)]; arrow(d, p, DO, a, prog=a, w=4); hat(d, p, t, DO, ap(t, tall + 0.4), n=3, v=0.5, r=6)
        return im


class G10(G):  # S050–S051 tiền đi đâu
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = self.cs["S050"][0]; tnu = tw("S050", "use"); T = [tw("S051", "earlier"), tw("S051", "facade"), tw("S051", "himself"), tw("S051", "lavish")]
        tieu(d, "WHERE THE MONEY WENT", t, t0 - 0.2)
        node(d, 330, 560, "xu", "INVESTOR\nMONEY", ap(t, t0), w=300, h=260)
        a = ap(t, t0 + 0.6); p = [(480, 480), (900, 300), (1250, 300)]; arrow(d, p, XAM, a, dash=True, prog=a)
        txt(d, (1280, 300), "FILM RIGHTS, AS PROMISED", fnt(F_SANSB, 30), XAM, a, "lm")
        if tnu: cross(d, 900, 300, 30, XAM, ap(t, tnu)); txt(d, (1280, 345), "not used as promised (admitted)", fnt(F_SANS, 26), XAM, ap(t, tnu), "lm")
        lab = [("PAYMENTS TO EARLIER INVESTORS", True), ("THE COMPANY’S FACADE", False), ("HIMSELF & HIS ENTITIES", False), ("“LAVISH LIFESTYLE”", False)]
        for i, (tt, (l, acc)) in enumerate(zip(T, lab)):
            if not tt or t < tt - 0.5: continue
            y = 470 + i * 125; a = ap(t, tt - 0.5, 0.6); p = [(485, 560), (720, y), (1150, y)]
            arrow(d, p, DO if acc else HP, 1, prog=a, w=6); hat(d, p, t + i, DO if acc else HP, ap(t, tt), n=5, v=0.35, pulse=acc)
            txt(d, (1180, y), l, fnt(F_BOLD, 36), DO if acc else NGA, a, "lm")
        return im


class G11(G):  # S053–S056 co-investment ◐
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = self.cs["S053"][0]; tp = tw("S053", "personally"); tsep = tw("S053", "september"); tk = tw("S054", "taken")
        t233 = tw("S055", "two"); tmar = tw("S055", "march"); t57 = tw("S056", "five"); tco = tw("S056", "combined")
        tieu(d, "“INVESTING ALONGSIDE YOU”", t, t0, "according to the SEC")
        node(d, 560, 420, "mot_nguoi", "HIS STAKE", ap(t, tp), w=280, h=210, sub=("around Sept. 2017" if tsep and t > tsep else None))
        node(d, 1100, 420, "nguoi", "GROUP’S NOTES", ap(t, tp + 0.5 if tp else None), w=300, h=210)
        p = [(705, 420), (945, 420)]; arrow(d, p, XAM, ap(t, tp + 0.5 if tp else None)); hat(d, p, t, HP, ap(t, tp + 0.8 if tp else None), n=3)
        if tk and t > tk - 0.4:
            a = ap(t, tk - 0.4); node(d, 180, 420, "nguoi", "OTHER\nINVESTORS", a, w=250, h=210, acc=True)
            p = [(310, 420), (415, 420)]; arrow(d, p, DO, a); hat(d, p, t, DO, a, n=3, pulse=True)
            txt(d, (360, 560), "taken from other investors", fnt(F_SANSB, 26), DO, ap(t, tk), "mm")
        if t233 and t > t233 - 0.4:
            a = ap(t, t233 - 0.4); p = [(1100, 530), (1100, 700), (760, 700)]; arrow(d, p, HP, a, prog=a); hat(d, p, t, HP, ap(t, t233), n=4)
            v = dem(t, t233, 2.33, 1.0); so_lon(d, (560, 720), f"≈ ${v:.2f}M", t, t233 + 1.0, NGA, 80)
            txt(d, (560, 790), "“his share” · " + ("March 2018" if tmar and t > tmar else ""), fnt(F_SANSB, 28), XAM, a, "mm")
        if t57 and t > t57 - 0.4:
            a = ap(t, t57 - 0.4); node(d, 1560, 760, "nha", "HOME", a, w=280, h=210)
            p = [(760, 760), (1415, 760)]; arrow(d, p, HP, a, prog=a); hat(d, p, t, HP, ap(t, t57), n=4)
            v = dem(t, t57, 5.7, 1.0); so_lon(d, (1560, 930), f"≈ ${v:.1f}M cash", t, t57 + 1.0, NGA, 54)
            if tco: p2 = [(180, 530), (180, 980), (1560, 980), (1560, 870)]; arrow(d, p2, DO, ap(t, tco), prog=ap(t, tco, 1.2), w=3, dash=True)
            txt(d, (870, 1010), "+ other investor funds", fnt(F_SANS, 24), DO, ap(t, tco), "mm")
        return im


class G12(G):  # S058–S061 vòng Ponzi
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = self.cs["S058"][0]; tpz = tw("S058", "ponzi"); tbuy = tw("S060", "buy"); traise = tw("S060", "raise"); t61 = tw("S061", "ontime") or tw("S061", "on")
        tieu(d, "PONZI SCHEME", t, tpz or t0, "paying earlier investors with money from newer ones")
        A, B, C = (330, 560), (960, 560), (1590, 560)
        node(d, *A, "nguoi", "NEWER\nINVESTORS", ap(t, t0)); node(d, *B, "xu", "POOL", ap(t, t0 + 0.5), w=240)
        node(d, *C, "nguoi", "EARLIER\nINVESTORS", ap(t, t0 + 1.0))
        p1 = [(480, 560), (840, 560)]; arrow(d, p1, HP, ap(t, t0 + 0.4)); hat(d, p1, t, HP, ap(t, t0 + 0.6), n=4)
        p2 = [(1080, 560), (1440, 560)]; arrow(d, p2, DO, ap(t, t0 + 1.0), w=7); hat(d, p2, t, DO, ap(t, t0 + 1.2), n=5, pulse=True)
        txt(d, (1260, 500), "PAID ON TIME", fnt(F_BOLD, 30), DO, ap(t, t0 + 1.4), "mm")
        if tbuy and t > tbuy - 0.5:
            a = ap(t, tbuy - 0.5, 0.9); p3 = [(1590, 690), (1590, 860), (330, 860), (330, 690)]
            arrow(d, p3, NGA, 1, prog=a, w=5); hat(d, p3, t, HP, ap(t, tbuy + 0.4), n=8, v=0.25)
            txt(d, (960, 905), "BUY MORE NOTES" + (" · RAISE MONEY FROM OTHERS" if traise and t > traise else ""), fnt(F_BOLD, 34), NGA, a, "mm")
        if t61 and t > t61:
            txt(d, (960, 410), "on-time payments keep it going", fnt(F_SANSB, 32), XAM, ap(t, t61), "mm")
        return im


class G13(G):  # S063, S065 vỡ nợ
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tdec = tw("S063", "december"); t230 = tw("S065", "two"); t0 = self.cs["S063"][0]
        tieu(d, "WHEN THE PAYMENTS STOPPED", t, t0 - 0.2)
        d.line((140, 520, 1780, 520), fill=XAM, width=3)
        for k in range(9):
            x = 200 + k * 110; a = ap(t, t0 + k * 0.12, 0.3)
            d.ellipse((x - 14, 506, x + 14, 534), fill=mix(TEAL, a))
        txt(d, (640, 590), "PAYMENTS ON SCHEDULE", fnt(F_SANSB, 30), TEAL, ap(t, t0 + 0.5), "mm")
        if tdec:
            a = ap(t, tdec - 0.3); x = 1300; d.line((x, 420, x, 620), fill=mix(DO, a), width=6)
            txt(d, (x + 20, 430), "~DEC. 2019", fnt(F_BOLD, 44), DO, a); txt(d, (x + 20, 490), "defaults begin on all outstanding notes", fnt(F_SANS, 28), NGA, a)
            for k in range(4):
                xx = 1400 + k * 95; d.ellipse((xx - 14, 506, xx + 14, 534), outline=mix(XAM, a), width=3)
        if t230 and t > t230 - 0.4:
            v = dem(t, t230, 230, 1.4); so_lon(d, (960, 780), f"≈ ${v:.0f} MILLION", t, t230 + 1.4, NGA, 120)
            txt(d, (960, 870), "PRINCIPAL IN DEFAULT · by the time of the plea", fnt(F_SANSB, 32), XAM, ap(t, t230), "mm")
        return im


class G14(G):  # S069 thư "từ nền tảng"
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t0 = self.cs["S069"][0]; tcl = tw("S069", "claimed"); tcom = tw("S069", "communication"); tf = tw("S069", "fake")
        tieu(d, "THE REASSURANCES", t, t0 - 0.2)
        node(d, 420, 520, "thu", "EMAILS &\nTEXT MESSAGES", ap(t, t0 + 0.3), w=360, h=260)
        node(d, 1500, 520, "manhinh", "STREAMING\nPLATFORMS", ap(t, tcl), w=360, h=260)
        p = [(1320, 520), (600, 520)]; arrow(d, p, XAM, ap(t, tcl), dash=True, prog=ap(t, tcl, 0.8))
        txt(d, (960, 470), "claimed to come from the platforms", fnt(F_SANSB, 28), XAM, ap(t, tcl), "mm")
        if tcom: cross(d, 960, 530, 30, DO, ap(t, tcom)); txt(d, (960, 610), "no communication with the platforms", fnt(F_SANSB, 30), NGA, ap(t, tcom), "mm")
        if tf: dau(d, 420, 800, "FAKE — admitted", ap(t, tf - 0.1, 0.35))
        return im


class G15(G):  # S073–S081 đếm ngược tới April 9
    def X(self, dd): return 220 + dd * (1480 / 53)

    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tm = tw("S073", "march"); t5 = tw("S078", "fifth") or self.cs["S078"][0]; tfz = tw("S079", "freeze") or self.cs["S079"][0]
        tar = tw("S080", "arrested") or self.cs["S080"][0]; tind = tw("S081", "indicted") or self.cs["S081"][0] + 3
        tieu(d, "COUNTDOWN TO APRIL 9", t, tm - 0.3 if tm else None)
        y = 640; d.line((self.X(0) - 40, y, self.X(53) + 40, y), fill=XAM, width=3)
        stop = t > tar
        ab = ap(t, tm, 0.6) * (0.35 if stop else 1.0)
        bx = self.X(28); dashed_rect(d, (bx - 52, y - 60, bx + 52, y + 60), mix(DO if not stop else XAM, ap(t, tm, 0.6)), 5)
        txt(d, (bx, y), "APRIL 9", fnt(F_BOLD, 24), DO if not stop else XAM, ap(t, tm, 0.6), "mm")
        ev = [(tm, 0, "~MAR. 12, 2021", "email: funds “by April 9th (at the latest)”", HPA, -1),
              (t5, 24, "APR. 5", "SEC files emergency case", NGA, 1), (tfz, 25, "APR. 6", "asset freeze", NGA, -1),
              (tar, 25, "APR. 6", "arrest", DO, 1), (tind, 53, "MAY 4", "indictment", NGA, -1)]
        for tt, dd, lab, s, col, up in ev:
            a = ap(t, tt - 0.2)
            if a <= 0: continue
            x = self.X(dd) + (14 if lab == "APR. 6" and s == "arrest" else 0); d.ellipse((x - 12, y - 12, x + 12, y + 12), fill=mix(col, a))
            yy = y - 160 if up < 0 else y + 110; d.line((x, y + 14 * up, x, yy + (60 if up < 0 else -10)), fill=mix(XAM, a), width=2)
            an = "lm" if dd == 0 else ("rm" if dd == 53 else "mm"); xx = x - 12 if dd == 0 else (x + 12 if dd == 53 else x)
            txt(d, (xx, yy), lab, fnt(F_BOLD, 30), col, a, an); txt(d, (xx, yy + 38), s, fnt(F_SANS, 24), NGA, a, an)
        if tind and t > tind:
            txt(d, (self.X(53), y + 230), "securities fraud · wire fraud · aggravated identity theft", fnt(F_SANS, 22), XAM, ap(t, tind + 0.5), "rm")
        # bộ đếm
        if tm and t > tm - 0.2:
            n = 28 if t < t5 else (4 if t < tfz else 3)
            col = XAM if stop else DO; k = nhan(t, t5 if t < tfz else tfz) if not stop else 1.0
            txt(d, (1700, 120), f"{n} DAYS", fnt(F_BOLD, int(96 * k)), col, ap(t, tm, 0.6), "ra")
            txt(d, (1700, 240), "until April 9" if not stop else "the countdown stopped", fnt(F_SANSB, 30), XAM, ap(t, tm, 0.6), "ra")
        return im


class G16(G):  # S082–S086 kết cục hình sự
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tp = tw("S082", "pleaded") or self.cs["S082"][0]; t240 = tw("S084", "two"); tr = self.cs["S085"][0] + 0.3; tdis = tw("S086", "dismissed")
        tieu(d, "THE CRIMINAL CASE", t, self.cs["S082"][0] - 0.3, "U.S. v. Horwitz · C.D. Cal.")
        rows = [(tp, "OCT. 2021", "pleaded guilty · 1 count of securities fraud"), (t240, "FEB. 14, 2022", "sentenced: 240 months in federal prison"),
                (tr, "RESTITUTION", "ordered by the judge"), (tdis, "OTHER CHARGES", "dismissed on the government’s motion")]
        d.line((170, 280, 170, 280 + 600 * ap(t, tp, 1.5)), fill=XAM, width=3)
        for i, (tt, k, v) in enumerate(rows):
            a = ap(t, tt); y = 300 + i * 165
            d.ellipse((158, y + 8, 182, y + 32), fill=mix(DO if i == 2 else NGA, a))
            txt(d, (220, y), k, fnt(F_BOLD, 40), DO if i == 2 else NGA, a); txt(d, (220, y + 52), v, fnt(F_SANS, 30), XAM, a)
        if t240 and t > t240 - 0.3:
            v = dem(t, t240, 240, 1.2); so_lon(d, (1450, 420), f"{v:.0f} MONTHS", t, t240 + 1.2, NGA, 110)
            txt(d, (1450, 520), "= 20 YEARS", fnt(F_BOLD, 54), NGA, ap(t, t240 + 1.3), "mm")
        if t > tr - 0.3:
            v = dem(t, tr, 230361884, 2.0); so_lon(d, (1450, 720), f"${v:,.0f}", t, tr + 2.0, DO, 96)
            txt(d, (1450, 800), "RESTITUTION", fnt(F_SANSB, 32), XAM, ap(t, tr), "mm")
        return im


class G17(G):  # S087–S089 vụ SEC ◐
    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        tf = tw("S087", "final"); tw_ = tw("S087", "waived"); tpb = tw("S088", "permanently"); t74 = tw("S089", "seventyfour") or tw("S089", "seventy"); tde = tw("S089", "deemed")
        tieu(d, "THE SEC’S CIVIL CASE", t, self.cs["S087"][0] - 0.3, "SEC v. Horwitz · final judgment based on his consent")
        rows = [(tf, "FEB. 2024", "final judgment by consent"), (tw_, "WAIVED", "findings of fact · any right to appeal"),
                (tpb, "PERMANENT BAR", "from violating the antifraud provisions")]
        for i, (tt, k, v) in enumerate(rows):
            a = ap(t, tt); y = 300 + i * 160
            txt(d, (140, y), k, fnt(F_BOLD, 40), NGA, a); txt(d, (140, y + 52), v, fnt(F_SANS, 30), XAM, a)
        if t74 and t > t74 - 0.3:
            v = dem(t, t74, 74.2, 1.2); so_lon(d, (1420, 470), f"≈ ${v:.1f} MILLION", t, t74 + 1.2, NGA, 96)
            txt(d, (1420, 560), "disgorgement and interest", fnt(F_SANSB, 32), XAM, ap(t, t74), "mm")
        if tde and t > tde - 0.3:
            a = ap(t, tde - 0.3); arrow(d, [(1420, 610), (1420, 720)], DO, a, prog=a)
            txt(d, (1420, 780), "deemed satisfied by the", fnt(F_SANSB, 34), DO, a, "mm"); txt(d, (1420, 830), "criminal restitution order", fnt(F_SANSB, 34), DO, a, "mm")
        return im


class G18(G):  # P21 tiêu đề + 3 bài học
    def __init__(self, tw, cs, p21):
        super().__init__(tw, cs); self.p21 = p21

    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); tw = self.tw
        t3, t5, t1 = tw("S093", "three"), tw("S093", "five"), tw("S093", "one")
        if t < self.cs["S094"][0] - 0.4:
            txt(d, (960, 300), "WHAT TO TAKE AWAY", fnt(F_SERIF, 64), NGA, ap(t, self.cs["S093"][0]), "mm")
            for i, (tt, s, c) in enumerate([(t3, "3 LESSONS", TEAL), (t5, "5 RED FLAGS", DO), (t1, "1 RULE", NGA)]):
                a = ap(t, tt); txt(d, (420 + i * 540, 560), s, fnt(F_BOLD, 64), c, a, "mm")
            return im
        cid = "S094" if t < self.cs["S095"][0] - 0.4 else ("S095" if t < self.cs["S096"][0] - 0.4 else "S096")
        so, chu = self.p21[cid]; t0 = self.cs[cid][0]
        txt(d, (140, 150), so, fnt(F_BOLD, 40), TEAL, ap(t, t0 - 0.4)); txt(d, (140, 210), chu, fnt(F_SERIF, 58), NGA, ap(t, t0 - 0.2))
        a = ap(t, t0 + 0.3, 0.8)
        if cid == "S094":
            d.rectangle((400, 820 - 260 * a, 640, 820), fill=mix(HP, a)); txt(d, (520, 860), "6 MONTHS", fnt(F_SANSB, 30), NGA, a, "mm")
            txt(d, (520, 520), "35%", fnt(F_BOLD, 60), HP, a, "mm")
            d.rectangle((1100, 820 - 520 * a, 1340, 820), fill=mix(DO, a)); txt(d, (1220, 860), "PER YEAR", fnt(F_SANSB, 30), NGA, a, "mm")
            txt(d, (1220, 250 + 300 * (1 - a) + 20), "≈ 70%", fnt(F_BOLD, 60), DO, ap(t, t0 + 1.0), "mm")
            txt(d, (870, 640), "× 2", fnt(F_BOLD, 72), NGA, ap(t, t0 + 0.8), "mm")
        elif cid == "S095":
            cx, cy, r = 960, 600, 220
            pts = [(cx + r * math.cos(k * math.pi / 30), cy + r * math.sin(k * math.pi / 30)) for k in range(61)]
            d.line(pts, fill=mix(XAM, a), width=4); hat(d, pts, t, DO, a, n=10, v=0.25, r=9)
            txt(d, (cx, cy - 20), "NEW MONEY", fnt(F_SANSB, 34), NGA, a, "mm"); txt(d, (cx, cy + 30), "pays earlier investors", fnt(F_SANS, 28), XAM, a, "mm")
        else:
            node(d, 520, 620, "nguoi", "SUB-INVESTORS", a, w=300, h=220); node(d, 1400, 620, "cty", "1inMM", a, w=300, h=220)
            dashed(d, [(690, 620), (1230, 620)], mix(DO, a), 5); cross(d, 960, 620, 26, DO, ap(t, t0 + 1.0))
            txt(d, (960, 700), "no direct contract", fnt(F_SANSB, 30), DO, ap(t, t0 + 1.0), "mm")
        return im


class G19(G):  # thẻ tổng kết
    def __init__(self, tw, cs, dong): super().__init__(tw, cs); self.dong = dong; self.t0 = None

    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im); t0 = self.t0
        txt(d, (120, 80), "WHAT TO TAKE AWAY", fnt(F_SERIF, 52), NGA, ap(t, t0))
        y = 180
        for i, (nhom, ds, col) in enumerate(self.dong):
            a = ap(t, t0 + 0.3 + i * 0.6); txt(d, (120, y), nhom, fnt(F_BOLD, 32), col, a); y += 50
            for j, s in enumerate(ds):
                txt(d, (150, y), f"{j + 1}. {s}" if len(ds) > 1 else s, fnt(F_SANS, 34), NGA, ap(t, t0 + 0.5 + i * 0.6 + j * 0.1)); y += 50
            y += 18
        a = ap(t, t0 + 2.4)
        txt(d, (120, 960), "Check: brokercheck.finra.org · adviserinfo.sec.gov — Report: sec.gov/submit-tip-or-complaint · reportfraud.ftc.gov", fnt(F_MONO, 24), XAM, a)
        return im


class G20(G):  # danh sách nguồn chạy chữ
    def __init__(self, tw, cs, dong, ai): super().__init__(tw, cs); self.dong = dong; self.ai = ai; self.t0 = None; self.t1 = None

    def draw(self, t):
        im = nen(); d = ImageDraw.Draw(im)
        hcao = 140 + len(self.dong) * 46 + 200; u = (t - self.t0) / max(self.t1 - self.t0, 1)
        y0 = 1080 - (hcao + 1080 * 0.25) * min(max(u, 0), 1) * 1.0 + 0
        txt(d, (960, y0 + 40), "SOURCES", fnt(F_SERIF, 52), NGA, 1, "mm")
        for i, s in enumerate(self.dong):
            y = y0 + 140 + i * 46
            if -60 < y < 1140: txt(d, (960, y), s, fnt(F_SANS, 27), NGA, 1, "mm")
        y = y0 + 140 + len(self.dong) * 46 + 60
        for k, s in enumerate(self.ai):
            if -60 < y + k * 40 < 1140: txt(d, (960, y + k * 40), s, fnt(F_SANS, 26), XAM, 1, "mm")
        return im
