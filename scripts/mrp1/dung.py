#!/usr/bin/env python3
"""MR-P1 · Dựng bản xem 540p P00–P03 tập 1 cho một biến thể phong cách (0 USD, dựng lại được).
  python3 scripts/mrp1/dung.py A      → reports/mrp1/xem/A.mp4 + reports/mrp1/xem/A_to1s.jpg + reports/mrp1/xem/A_khung.json
Cần (LFS): lab/mrp1/<bt>/*.png, lab/mr4/tts/{P00,P01_l2,P02,P03}.mp3, lab/mr5/nhac/N1_mo.mp3,
           ho-so/1inmm-horwitz/{doj-plea-agreement-2021,sec-complaint-2021}.pdf
Dòng thời gian = giọng thật đã duyệt (reports/mr4/xem/tap01_giong_ghep.json: P00 0,00 · P01 19,45 · P02 72,28 · P03 92,14),
mốc cảnh theo từ (reports/mr4/whisper/*.json). Thẻ KBCB S019 giữ 6 s không lời sau P03 (SHOT hàng 12).
Hình: tranh AI tĩnh + chuyển động máy chậm (đẩy/kéo/lia, có làm mượt) + hoà cảnh 0,5 s. Thẻ chữ bảng màu B1 "Hồ sơ".
Bằng chứng thật: ảnh trang PDF (pdftoppm 200 dpi), cắt đúng dòng, chỉ thêm khung khoanh + dòng nguồn — không vẽ lại chữ.
Phông: IBM Plex (B1) không có trong máy, tải từ github bị 403 (không vượt) → thay Liberation Serif Bold / Inter / JetBrains Mono."""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BT = sys.argv[1]; FPS = 25; W, H = 960, 540; T = 0.5
XEM = os.path.join(ROOT, "reports", "mrp1", "xem"); os.makedirs(XEM, exist_ok=True)
TMP = os.environ.get("TMPDIR", "/tmp")
NGA, MUC, KET, DO, XAM, HP = "#F4F1EA", "#1B1F24", "#2B7A78", "#D9480F", "#8A8F98", "#B7791F"
F_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"; F_SANSB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
F_SYM = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf"; F_MONOB = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-SemiBold.ttf"
fnt = lambda f, s: ImageFont.truetype(f, s)

# ---------- nguồn ảnh ----------
CHON = {"a14": "a14_l2"}  # a14 lượt 1 lộ mép má/tai → dùng lượt 2 (bóng thuần)
CAT = {  # cắt khung loại phần không dùng (0 USD): khách nền có mặt (a17), nhân vật lọt vào (a14 l2, a16 B)
    "A": {"a14": (0, 0, 860, 484), "a17": (300, 80, 1376, 685)},
    "B": {"a14": (140, 0, 940, 450), "a17": (0, 60, 1100, 679), "a16": (150, 100, 950, 550)}}


def tranh(tid):
    im = Image.open(os.path.join(ROOT, "lab", "mrp1", BT, CHON.get(tid, tid + "_l1") + ".png")).convert("RGB")
    if tid in CAT[BT]: im = im.crop(CAT[BT][tid])
    return im.resize((1920, 1080), Image.LANCZOS)


# ---------- thẻ chữ B1 (vẽ 1920×1080) ----------
def giay():
    im = Image.new("RGB", (1920, 1080), NGA)
    rng = np.random.default_rng(7); n = rng.normal(0, 5, (1080, 1920, 1)).astype(np.int16)
    a = np.clip(np.asarray(im).astype(np.int16) + n, 0, 255).astype(np.uint8)
    return Image.fromarray(a)


def wrap(d, text, f, wmax):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= wmax: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out


def huy_hieu(d, x, y, text, mau, s=34):
    """Huy hiệu tầng. Ký hiệu ●/◐ vẽ bằng DejaVu (Inter không có ◐)."""
    f = fnt(F_SANSB, s); ky, chu = (text[0], text[1:]) if text[0] in "●◐" else ("", text)
    fk = fnt(F_SYM, s); wk = d.textlength(ky, font=fk) if ky else 0; w = wk + d.textlength(chu, font=f)
    d.rounded_rectangle((x, y, x + w + 36, y + s + 22), radius=8, fill=mau)
    if ky: d.text((x + 18, y + 8), ky, font=fk, fill="white")
    d.text((x + 18 + wk, y + 9), chu, font=f, fill="white")
    return w + 36


def nguon(d, text, y=1010, mau=MUC, x=80):
    d.text((x, y), text, font=fnt(F_MONO, 24), fill=mau)


def lop_moi():
    """Lớp tĩnh (không theo chuyển động máy) cho huy hiệu tầng, dòng nguồn, tiêu đề bằng chứng — luôn đọc được trọn."""
    o = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); return o, ImageDraw.Draw(o)


def the_kbcb(text, src):
    im = giay(); d = ImageDraw.Draw(im)
    d.rectangle((80, 120, 92, 760), fill=KET)
    f = fnt(F_SERIF, 64); y = 170
    for ln in wrap(d, text, f, 1600): d.text((130, y), ln, font=f, fill=MUC); y += 86
    o, od = lop_moi(); nguon(od, src); return im, o


def the_hop(tieu_de, hop, badge, src, buoc=None):
    """Sơ đồ hộp nối mũi tên. hop = list (chữ, màu); buoc = số hộp hiện (sơ đồ lộ dần)."""
    im = giay(); d = ImageDraw.Draw(im)
    d.text((80, 80), tieu_de, font=fnt(F_SERIF, 60), fill=MUC)
    n = len(hop); k = n if buoc is None else buoc; bw, gap = (1760 - (n - 1) * 70) // n, 70; y0, y1 = 380, 640
    for i, (t, mau) in enumerate(hop[:k]):
        x0 = 80 + i * (bw + gap)
        d.rounded_rectangle((x0, y0, x0 + bw, y1), radius=18, outline=mau, width=6, fill="#FBF9F4")
        f = fnt(F_SANSB, 40 if n <= 3 else 32); yy = (y0 + y1) // 2 - 26 * len(wrap(d, t, f, bw - 40))
        for ln in wrap(d, t, f, bw - 40):
            d.text((x0 + bw / 2, yy), ln, font=f, fill=MUC, anchor="ma"); yy += 52
        if i < k - 1 and i < n - 1:
            ax = x0 + bw + 8; d.line((ax, 510, ax + gap - 16, 510), fill=XAM, width=6)
            d.polygon([(ax + gap - 16, 496), (ax + gap - 2, 510), (ax + gap - 16, 524)], fill=XAM)
    o, od = lop_moi(); huy_hieu(od, 80, 900, badge[0], badge[1]); nguon(od, src); return im, o


def the_vong(buoc, src):
    """P03 'lời chào mời' (Plea pp. 9–10): Investors → 1inMM → film rights → streaming platforms (outside U.S.) → profits → back to investors."""
    hop = [("INVESTORS", KET), ("1inMM", MUC), ("FILM RIGHTS", MUC), ("STREAMING PLATFORMS (outside the U.S.)", MUC), ("PROFITS → PAID BACK", KET)]
    im, o = the_hop("The pitch, as he described it", hop[: {1: 3, 2: 4, 3: 5}[buoc]] if buoc < 3 else hop,
                    ("● CONVICTED · admitted in plea", DO), src)
    if buoc == 3:
        d = ImageDraw.Draw(im); bw = (1760 - 4 * 70) // 5
        xa, xb = 80 + bw / 2, 80 + 4 * (bw + 70) + bw / 2
        d.line((xb, 650, xb, 760), fill=KET, width=6); d.line((xb, 760, xa, 760), fill=KET, width=6); d.line((xa, 760, xa, 660), fill=KET, width=6)
        d.polygon([(xa - 14, 672), (xa, 648), (xa + 14, 672)], fill=KET)
    return im, o


def the_tieu_de():
    im = giay(); d = ImageDraw.Draw(im)
    d.text((960, 430), "Real cases from the public record", font=fnt(F_SERIF, 92), fill=MUC, anchor="mm")
    d.line((660, 520, 1260, 520), fill=DO, width=6)
    d.text((960, 590), "MONEY REROUTE", font=fnt(F_MONOB, 40), fill=XAM, anchor="mm"); return im, None


def the_chu(dong, phu, src, badge=None):
    im = giay(); d = ImageDraw.Draw(im); y = 330
    f = fnt(F_SERIF, 84)
    for ln in wrap(d, dong, f, 1700): d.text((960, y), ln, font=f, fill=MUC, anchor="ma"); y += 104
    d.text((960, y + 40), phu, font=fnt(F_SANS, 44), fill=XAM, anchor="ma")
    o, od = lop_moi()
    if badge: huy_hieu(od, 80, 900, *badge)
    nguon(od, src); return im, o


# ---------- bằng chứng thật (ảnh trang PDF, không vẽ lại) ----------
def trang(pdf, p, dpi=200):
    o = os.path.join(TMP, f"mrp1_{os.path.basename(pdf)[:-4]}_{p}")
    if not os.path.exists(o + ".png"):
        subprocess.run(["pdftoppm", "-r", str(dpi), "-f", str(p), "-l", str(p), "-png", "-singlefile", pdf, o], check=True)
    return Image.open(o + ".png").convert("RGB"), dpi / 72.0


def bang_chung(pdf, p, vung, khoanh, tieu, badge, src):
    """vung = (x0,y0,x1,y1) điểm PDF của đoạn cắt; khoanh = list hộp (điểm PDF) cần khoanh. Trả nền 1920×1080 + vị trí khoanh."""
    pg, s = trang(os.path.join(ROOT, pdf), p)
    x0, y0, x1, y1 = vung; cr = pg.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))
    sc = min(1640 / cr.width, 700 / cr.height); cr = cr.resize((int(cr.width * sc), int(cr.height * sc)), Image.LANCZOS)
    im = Image.new("RGB", (1920, 1080), MUC if BT == "A" else "#E7E2D6"); d = ImageDraw.Draw(im)
    ox, oy = (1920 - cr.width) // 2, 150
    sh = Image.new("RGBA", (cr.width + 40, cr.height + 40), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((20, 20, cr.width + 20, cr.height + 20), fill=(0, 0, 0, 110))
    im.paste(sh.filter(ImageFilter.GaussianBlur(14)), (ox - 12, oy - 6), sh.filter(ImageFilter.GaussianBlur(14)))
    im.paste(cr, (ox, oy))
    hop = [((a - x0) * s * sc + ox, (b - y0) * s * sc + oy, (c - x0) * s * sc + ox, (e - y0) * s * sc + oy) for a, b, c, e in khoanh]
    mau_chu = NGA if BT == "A" else MUC
    o, od = lop_moi(); ft = fnt(F_MONOB, 34)
    od.rectangle((60, 44, 100 + od.textlength(tieu, font=ft), 104), fill=(27, 31, 36, 235)); od.text((80, 56), tieu, font=ft, fill=NGA)
    od.rectangle((60, 896, 1860, 1050), fill=(27, 31, 36, 225) if BT == "A" else (231, 226, 214, 235))
    huy_hieu(od, 80, 910, *badge); nguon(od, src, mau=mau_chu)
    return im, hop, o


def lop_khoanh(hop, a):
    """Lớp khoanh (RGBA 1920×1080) — viền đỏ cam + nền dạ quang nhạt, độ hiện a∈[0,1]."""
    o = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    for (x0, y0, x1, y1) in hop:
        d.rounded_rectangle((x0 - 10, y0 - 8, x1 + 10, y1 + 8), radius=10, fill=(242, 165, 65, int(70 * a)), outline=(217, 72, 15, int(255 * a)), width=5)
    return o


# ---------- lớp chữ trên tranh (1920×1080 RGBA) ----------
def lop(items):
    o = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    for it in items:
        k = it[0]
        if k == "nhan":  # nhãn ILLUSTRATIVE góc trên trái
            f = fnt(F_SANSB, 30); w = d.textlength(it[1], font=f)
            d.rounded_rectangle((60, 54, 60 + w + 32, 104), radius=8, fill=(138, 143, 152, 230)); d.text((76, 62), it[1], font=f, fill="white")
        elif k == "bong":  # bong bóng tin nhắn chung (dựng lại, có nhãn)
            f = fnt(F_SANS, 46); ls = wrap(d, it[1], f, 760); h = 60 * len(ls) + 50
            x0, y0 = it[2], it[3]; d.rounded_rectangle((x0, y0, x0 + 840, y0 + h), radius=36, fill=(244, 241, 234, 245))
            yy = y0 + 25
            for ln in ls: d.text((x0 + 40, yy), ln, font=f, fill=MUC); yy += 60
        elif k == "the":  # thẻ dưới (tên / số liệu) + huy hiệu + nguồn
            tieu, phu, badge, src = it[1:5]
            d.rectangle((0, 700, 1920, 1080), fill=(27, 31, 36, 215))
            d.text((80, 730), tieu, font=fnt(F_SERIF, 76), fill=NGA)
            if phu: d.text((80, 830), phu, font=fnt(F_SANS, 40), fill="#D8D4CA")
            x = 80
            if badge: huy_hieu(d, 1840 - d.textlength(badge[0], font=fnt(F_SANSB, 34)) - 36, 740, *badge)
            d.text((80, 1000), src, font=fnt(F_MONO, 24), fill="#C9C5BB")
    return o


# ---------- danh sách cảnh (giây toàn cục) ----------
SRC_PLEA = "Source: U.S. v. Horwitz, No. 2:21-cr-00214 (C.D. Cal.), Plea Agreement, Dkt. 45"
SRC_IND = "Source: U.S. v. Horwitz, No. 2:21-cr-00214 (C.D. Cal.), Indictment, Dkt. 25, p. 1"
SRC_KBCB = "Source: SEC Lit. Rel. 25067; SEC Press Rel. 2021-58; SEC Complaint ¶78"
KBCB = "HBO and Netflix were not accused of wrongdoing in these cases; according to the SEC, neither company ever did business with 1inMM."
NH = "ILLUSTRATIVE — not the real person"; NM = "ILLUSTRATIVE — not a real message"
# (bắt đầu, loại, nguồn, chuyển động, lớp chữ, ghi chú câu)
# chuyển động: (khung đầu, khung cuối) dạng (cx, cy, zoom) chuẩn hoá — zoom 1 = toàn khung
NHE = ((0.5, 0.5, 1.0), (0.5, 0.5, 1.04))  # thẻ chữ: đẩy rất nhẹ
IN, OUT_, L, R = ((0.5, 0.5, 1.0), (0.5, 0.5, 1.12)), ((0.5, 0.5, 1.12), (0.5, 0.5, 1.0)), ((0.44, 0.5, 1.1), (0.56, 0.5, 1.1)), ((0.56, 0.5, 1.1), (0.44, 0.5, 1.1))
CANH = [
    (0.0, "tranh", "a01", IN, [("nhan", NH)], "P00 S001"),
    (2.3, "tranh", "a02", ((0.5, 0.5, 1.0), (0.55, 0.45, 1.15)), [("nhan", NM), ("bong", "Payment received", 980, 200)], "P00 S001"),
    (5.5, "tranh", "a03", L, [], "P00 S002"),
    (7.7, "tranh", "a04", IN, [("nhan", NM), ("bong", "Delay on the platform side. Funds by next week.", 1000, 160)], "P00 S002"),
    (12.0, "tranh", "a05", ((0.45, 0.5, 1.15), (0.5, 0.5, 1.0)), [], "P00 S003"),
    (14.3, "the", "tieu_de", NHE, [], "P00 S003"),
    (19.3, "tranh", "a06", IN, [("nhan", NH), ("the@1.5", "Zachary Horwitz", "aka “Zach Avery” · actor, Los Angeles", None, SRC_IND)], "P01 S004"),
    (22.3, "tranh", "a07", ((0.5, 0.55, 1.0), (0.5, 0.45, 1.18)), [], "P01 S004"),
    (26.4, "tranh", "a08", R, [], "P01 S005"),
    (29.0, "the", "notes", NHE, [], "P01 S005"),
    (34.9, "tranh", "a09", ((0.5, 0.5, 1.0), (0.5, 0.5, 1.15)), [], "P01 S006"),
    (38.6, "tranh", "a10", L, [], "P01 S006"),
    (42.5, "bang", "tl1", ((0.5, 0.45, 1.0), (0.5, 0.52, 1.1)), [], "P01 S007"),
    (46.8, "the", "kbcb", NHE, [], "P01 S008"),
    (55.6, "tranh", "a11", IN, [("the@0.6", "$650,000,000+", "at least — raised from investors", ("● CONVICTED · admitted in plea", DO), SRC_PLEA + ", p. 12")], "P01 S009"),
    (59.9, "tranh", "a12", ((0.5, 0.6, 1.0), (0.5, 0.45, 1.1)), [], "P01 S010"),
    (62.9, "tranh", "a12", ((0.62, 0.35, 1.6), (0.58, 0.35, 1.75)), [("the@0.2", "20 years in prison", "sentenced in 2022 (240 months)", ("● CONVICTED", DO),
                                                                          "Source: U.S. v. Horwitz, 2:21-cr-00214 (C.D. Cal.), Judgment, Dkt. 75, p. 1; DOJ USAO C.D. Cal. 22-027")], "P01 S010"),
    (65.4, "tranh", "a13", OUT_, [], "P01 S011"),
    (68.2, "tranh", "a13", ((0.35, 0.5, 1.5), (0.4, 0.45, 1.6)), [], "P01 S011"),
    (70.9, "tranh", "a14", IN, [("nhan", NH)], "P02 S012"),
    (74.0, "the", "cty", NHE, [], "P02 S012"),
    (78.0, "tranh", "a15", ((0.4, 0.5, 1.1), (0.6, 0.5, 1.1)), [], "P02 S012"),
    (81.8, "the", "ten", NHE, [], "P02 S013"),
    (86.5, "tranh", "a16", IN, [("the@0.4", "Sole manager", "according to the indictment", ("◐ ALLEGED", HP), SRC_IND)], "P02 S014"),
    (91.9, "tranh", "a17", ((0.5, 0.5, 1.0), (0.4, 0.45, 1.15)), [("nhan", NH)], "P03 S015"),
    (94.0, "tranh", "a18", R, [], "P03 S015"),
    (96.9, "the", "vong1", NHE, [], "P03 S015"),
    (100.3, "tranh", "a20", ((0.5, 0.5, 1.0), (0.45, 0.48, 1.12)), [], "P03 S016"),
    (103.4, "the", "vong2", NHE, [], "P03 S016"),
    (107.6, "tranh", "a19", ((0.5, 0.5, 1.0), (0.5, 0.5, 1.12)), [], "P03 S016"),
    (111.0, "the", "vong3", NHE, [], "P03 S017"),
    (114.2, "tranh", "a09", ((0.3, 0.5, 1.5), (0.4, 0.5, 1.6)), [("the@0.3", "Films mostly from Latin America", "what the company claimed, per the SEC", ("◐ ALLEGED", HP),
                                                                 "Source: SEC v. Horwitz, No. 2:21-cv-02927 (C.D. Cal.), Complaint ¶5")], "P03 S018"),
    (117.3, "bang", "tl2", ((0.5, 0.45, 1.0), (0.5, 0.5, 1.1)), [], "P03 S018"),
    (124.9, "the", "kbcb", NHE, [], "P03 S019 (chữ, không đọc, 6 s)"),
]
KET_T = 132.0


def nen_the(k):
    if k == "tieu_de": return (*the_tieu_de(), None)
    if k == "notes": return the_hop("Promissory notes", [("DUE IN 6 OR 12 MONTHS", MUC), ("PROMISED RETURN 25–45%", DO), ("TO BUY FILM RIGHTS", MUC)],
                                    ("● CONVICTED · admitted in plea", DO), SRC_PLEA + ", pp. 9–10") + (None,)
    if k == "kbcb": return the_kbcb(KBCB, SRC_KBCB) + (None,)
    if k == "cty": return the_chu("1inMM Capital, LLC", "founded around 2013 · promoted as a film distribution company · Los Angeles",
                                  SRC_PLEA + ", p. 8", ("● CONVICTED · admitted in plea", DO)) + (None,)
    if k == "ten": return the_chu("1inMM (“one in a million”) Capital, LLC", "according to the SEC", "Source: SEC Lit. Rel. No. 25067 (Apr. 8, 2021)") + (None,)
    if k.startswith("vong"): return the_vong(int(k[-1]), SRC_PLEA + ", pp. 9–10") + (None,)
    if k == "tl1":
        return bang_chung("ho-so/1inmm-horwitz/doj-plea-agreement-2021.pdf", 11, (38, 232, 574, 430),
                          [(388.8, 381.7, 554.4, 402.1), (72.0, 405.7, 316.8, 426.1)], "PLEA AGREEMENT — U.S. v. HORWITZ · page 11, lines 8–15",
                          ("● CONVICTED · admitted in plea", DO), SRC_PLEA + ", p. 11")
    if k == "tl2":
        return bang_chung("ho-so/1inmm-horwitz/sec-complaint-2021.pdf", 3, (40, 141, 556, 380),
                          [(487.0, 168.7, 538.0, 184.2), (72.0, 192.7, 184.7, 208.2), (401.0, 360.7, 525.4, 376.2)],
                          "SEC COMPLAINT — SEC v. HORWITZ · ¶5, page 3", ("◐ ALLEGED", HP),
                          "Source: SEC v. Horwitz, No. 2:21-cv-02927 (C.D. Cal.), Complaint ¶5, p. 3")
    raise KeyError(k)


def muot(u): return u * u * (3 - 2 * u)


def khung_chuyen(im, mv, u, base=None):
    (ax, ay, az), (bx, by, bz) = mv; e = muot(u)
    cx, cy, z = ax + (bx - ax) * e, ay + (by - ay) * e, az + (bz - az) * e
    w, h = 1920 / z, 1080 / z; x0 = min(max(cx * 1920 - w / 2, 0), 1920 - w); y0 = min(max(cy * 1080 - h / 2, 0), 1080 - h)
    return im.transform((W, H), Image.EXTENT, (x0, y0, x0 + w, y0 + h), Image.BICUBIC)


def chuan_bi():
    out = []
    for i, (s, loai, src, mv, items, ghi) in enumerate(CANH):
        e = CANH[i + 1][0] if i + 1 < len(CANH) else KET_T
        hop = ov = None
        if loai == "tranh": nen = tranh(src)
        elif loai == "bang": nen, hop, ov = nen_the(src)
        else: nen, ov, _ = nen_the(src)
        tinh, dong = [], []
        for it in items:
            if it[0].startswith("the@"): dong.append((float(it[0][4:]), lop([("the",) + tuple(it[1:])]).resize((W, H), Image.LANCZOS)))
            else: tinh.append(it)
        out.append({"s": s, "e": e, "nen": nen, "mv": mv, "tinh": lop(tinh).resize((W, H), Image.LANCZOS) if tinh else None, "dong": dong,
                    "hop": hop, "ov": ov.resize((W, H), Image.LANCZOS) if ov is not None else None, "loai": loai, "src": src, "ghi": ghi})
    return out


def ve(c, t):
    d = c["e"] - c["s"] + T; u = min(max((t - c["s"]) / d, 0), 1)
    nen = c["nen"]
    if c["hop"]:
        a = min(max((t - c["s"] - 1.0) / 0.6, 0), 1)
        if a > 0: nen = Image.alpha_composite(nen.convert("RGBA"), lop_khoanh(c["hop"], a)).convert("RGB")
    f = khung_chuyen(nen, c["mv"], u).convert("RGBA")
    if c["ov"] is not None: f = Image.alpha_composite(f, c["ov"])
    if c["tinh"]: f = Image.alpha_composite(f, c["tinh"])
    for t0, o in c["dong"]:
        a = min(max((t - c["s"] - t0) / 0.3, 0), 1)
        if a > 0:
            oo = o.copy(); oo.putalpha(o.getchannel("A").point(lambda v: int(v * a))); f = Image.alpha_composite(f, oo)
    return f.convert("RGB")


def am(dst):
    g = json.load(open(os.path.join(ROOT, "reports", "mr4", "xem", "tap01_giong_ghep.json")))["doan"][:4]
    ins, fl = [], []
    for i, x in enumerate(g):
        ins += ["-i", os.path.join(ROOT, x["tep"])]; ms = int(round(x["bat_dau"] * 1000)); fl.append(f"[{i}:a]adelay={ms}|{ms}[v{i}]")
    n1 = os.path.join(ROOT, "lab", "mr5", "nhac", "N1_mo.mp3")
    ins += ["-stream_loop", "3", "-i", n1]
    fl.append("[v0][v1][v2][v3]amix=inputs=4:normalize=0[voi]")
    # N1 (40 s) lặp nối tiếp; mức −20 dB dưới lời, nâng lên trong 6 s thẻ KBCB S019 không lời; tắt dần 2 s cuối
    fl.append(f"[4:a]atrim=0:{KET_T},volume='if(between(t,125,131),0.30,0.10)':eval=frame,afade=t=out:st={KET_T - 2}:d=2[nh]")
    fl.append(f"[voi][nh]amix=inputs=2:normalize=0,apad,atrim=0:{KET_T},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fl), "-map", "[a]", "-ar", "48000", "-c:a", "pcm_s16le", dst], check=True)


def main():
    cs = chuan_bi(); wav = os.path.join(TMP, f"mrp1_{BT}.wav"); am(wav)
    dst = os.path.join(XEM, f"{BT}.mp4")
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                          "-shortest", "-movflags", "+faststart", dst], stdin=subprocess.PIPE)
    n = int(KET_T * FPS); mau1s = []
    for k in range(n):
        t = k / FPS; i = max(j for j, c in enumerate(cs) if c["s"] <= t)
        f = ve(cs[i], t)
        if i > 0 and t < cs[i]["s"] + T: f = Image.blend(ve(cs[i - 1], t), f, muot((t - cs[i]["s"]) / T))
        if t < T: f = Image.blend(Image.new("RGB", (W, H)), f, t / T)
        if t > KET_T - 1.0: f = Image.blend(Image.new("RGB", (W, H)), f, max(KET_T - t, 0) / 1.0)
        if k % FPS == 0: mau1s.append((t, f.resize((240, 135))))
        p.stdin.write(f.tobytes())
    p.stdin.close(); p.wait()
    # tờ 1 s: 12 cột, mỗi ô ghi giây
    cot = 12; hang = (len(mau1s) + cot - 1) // cot; to = Image.new("RGB", (cot * 240, hang * 135), "black"); d = ImageDraw.Draw(to)
    for j, (t, im) in enumerate(mau1s):
        x, y = (j % cot) * 240, (j // cot) * 135; to.paste(im, (x, y)); d.rectangle((x, y, x + 46, y + 18), fill="black"); d.text((x + 3, y + 3), f"{int(t)}s", fill="white")
    to.save(os.path.join(XEM, f"{BT}_to1s.jpg"), quality=78)
    json.dump({"bt": BT, "fps": FPS, "kich_thuoc": f"{W}x{H}", "hoa_canh_s": T, "tong_s": KET_T,
               "canh": [{"bat_dau": c["s"], "ket_thuc": c["e"], "loai": c["loai"], "nguon": c["src"], "cau": c["ghi"]} for c in cs]},
              open(os.path.join(XEM, f"{BT}_khung.json"), "w"), ensure_ascii=False, indent=1)
    print("xong", dst)


if __name__ == "__main__":
    main()
