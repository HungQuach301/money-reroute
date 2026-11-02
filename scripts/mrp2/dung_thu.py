#!/usr/bin/env python3
"""MR-P2 · Dựng đoạn thử ~60 s tập 1 (P05 S025–S029 + P08 S040–S042) theo 4 cách — 0 USD, dựng lại được.
  python3 scripts/mrp2/dung_thu.py goc|A|B|C [--to]       # --to: thêm tờ 1 s
  goc = cắt từ bản đã đăng (lab/mr6/dung/tap01_1080p.mp4, LFS)
  A   = 2.5D: mỗi tranh L1 tách 3 lớp theo độ sâu (scripts/mrp2/sau.py), mỗi lớp cong theo độ sâu từng điểm ảnh, máy di chuyển → thị sai
  B   = A + đúng 1 lớp chuyển động phủ/cảnh (bụi, cát chảy, đèn, hơi nước, đèn quét, lấy nét chuyển, rung, ổ khoá lắc)
        + chuyển cảnh khớp hình (3 cặp) + rung tay rất nhẹ
  P   = đối chứng cho thước đo: máy quay của A trên tranh phẳng (độ sâu hằng) = ảnh tĩnh trượt thuần, cùng thẻ chữ/nhãn
  C   = B, nhưng 5 cảnh thay bằng clip Veo ảnh→video 4 s (lab/mrp2/veo, LFS)
L2/L3/nhãn/thẻ chồng/giọng/nhạc: GIỮ NGUYÊN bản đăng — gọi thẳng scripts/mr6/dung.py (ve_canh, nhan_lop, ov_luc); âm cắt từ bản đăng.
Ra: reports/mrp2/xem/<bien>.mp4 (540p, LFS), reports/mrp2/xem/to1s_<bien>.jpg, reports/mrp2/dung_<bien>.json (thời gian dựng);
bản 1080p ở $MRP2_TMP (không đẩy — dựng lại được)."""
import json, math, os, subprocess, sys, time, zlib
import numpy as np, cv2
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP2_TMP", "/tmp/claude-0/mrp2"); os.makedirs(TMP, exist_ok=True)
os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))
import dung as D  # noqa: E402
from l2 import muot  # noqa: E402

W, H, FPS, T_HOA = D.W, D.H, D.FPS, D.T_HOA
CFG = json.load(open(os.path.join(os.path.dirname(__file__), "canh.json")))
# Đoạn theo khung (25 fps): 169,28–209,56 và 281,28–300,96 (dòng thời gian bản đăng)
DOAN = [(round(a * FPS - 0.5) / FPS, round(b * FPS) / FPS) for a, b in CFG["doan"]]
SAU = os.path.join(TMP, "sau")
XEM = os.path.join(ROOT, "reports", "mrp2", "xem")
GOC_1080 = os.path.join(ROOT, "lab", "mr6", "dung", "tap01_1080p.mp4")

# ---------------- máy quay theo tranh (toạ độ khung 1920×1080 của tranh) ----------------
# L: điểm nhìn đầu→cuối; Z: phóng chung; K: "dolly" (phóng thêm theo độ sâu → vật gần nở nhanh hơn); T: trượt ngang/dọc ở độ sâu 1 (px)
CAM = {
    "b009": dict(L=((1230, 540), (1290, 520)), Z=(1.08, 1.12), K=(0.0, 0.07), T=((-26, 0), (26, 0))),
    "b077": dict(L=((1010, 560), (960, 560)), Z=(1.10, 1.10), K=(0.02, 0.04), T=((22, -4), (-22, 4))),  # QC mép: dây cân mảnh → biên độ nhỏ
    "b081": dict(L=((960, 620), (1020, 600)), Z=(1.08, 1.12), K=(0.0, 0.06), T=((30, 0), (-30, 0))),
    "b010": dict(L=((1080, 520), (1060, 520)), Z=(1.08, 1.10), K=(0.0, 0.04), T=((-36, 0), (36, 0))),
    "b080": dict(L=((1000, 560), (1040, 540)), Z=(1.10, 1.13), K=(0.0, 0.03), T=((18, -3), (-18, 3))),  # QC mép: vệt vá cạnh lưng ghế → biên độ nhỏ
    "b011": dict(L=((960, 580), (960, 520)), Z=(1.06, 1.12), K=(0.0, 0.08), T=((0, 22), (0, -22))),
    "b143": dict(L=((900, 560), (980, 540)), Z=(1.08, 1.12), K=(0.0, 0.03), T=((-30, -10), (30, 10))),
    "b079": dict(L=((960, 600), (960, 580)), Z=(1.06, 1.10), K=(0.0, 0.06), T=((-22, 0), (22, 0))),
    "b021": dict(L=((1100, 600), (1180, 620)), Z=(1.08, 1.14), K=(0.0, 0.06), T=((-30, 0), (30, 0))),
    "b022": dict(L=((1200, 560), (1140, 600)), Z=(1.08, 1.12), K=(0.0, 0.04), T=((36, 0), (-36, 0))),
    "b091": dict(L=((960, 600), (960, 620)), Z=(1.08, 1.12), K=(0.0, 0.05), T=((0, -20), (0, 20))),
    "b089": dict(L=((1100, 540), (1140, 560)), Z=(1.08, 1.12), K=(0.0, 0.03), T=((-30, 0), (30, 0))),
}
# B · khớp hình: (tranh trước, neo trước) → (tranh sau, neo sau): neo sau đặt đúng chỗ neo trước đang nằm trên màn hình khi hoà cảnh
KHOP = {"b077": ("b009", (1300, 480), (1020, 520)), "b080": ("b010", (1120, 240), (1120, 300)), "b022": ("b021", (1280, 700), (1140, 600))}
# B · đúng 1 hiệu ứng/cảnh (toạ độ khung tranh)
HIEU_UNG = {
    "b009": ("cat", dict(x=1300, y0=500, y1=688)),                       # cát chảy qua cổ đồng hồ
    "b077": ("bui", dict(hop=(900, 0, 1920, 760), n=55)),                # bụi trong ánh đèn
    "b081": ("net", dict(dau=(0, 5, 3), cuoi=(4, 2, 0))),                # lấy nét chuyển: hàng domino xa → quân gần (σ lớp xa, giữa, gần)
    "b010": ("den", dict(c=(540, 650), r=260)),                          # đèn bàn chập chờn nhẹ
    "b080": ("khoi", dict(x=690, y=770, cao=230)),                       # hơi nước bốc từ cốc
    "b011": ("bui", dict(hop=(700, 40, 1300, 900), n=110)),              # bụi trong cột sáng
    "b143": ("quet", dict()),                                            # vệt sáng quét qua bàn (đèn xe ngoài cửa)
    "b079": ("bui", dict(hop=(600, 0, 1350, 760), n=80)),                # hạt sáng trong tia nắng
    "b021": ("den", dict(c=(1840, 260), r=420)),                         # đèn chập chờn trên hộp két rỗng
    "b022": ("net", dict(dau=(0, 0, 6), cuoi=(5, 3, 0))),                # lấy nét chuyển: kệ sau → hộp phim xích
    "b091": ("rung", dict(t=0.55)),                                      # rung khi con dấu ấn xuống
    "b089": ("lac", dict(p=(1180, 330), a=2.2)),                         # ổ khoá lắc quanh móc
}
# C · cảnh thay bằng clip Veo 4 s (reports/mrp2/veo/chon.json ghi lượt dùng)
VEO = {"b009": "V1", "b011": "V2", "b079": "V3", "b022": "V4", "b089": "V5"}

_L = {}


def lop(ma):
    if ma not in _L:
        r = lambda s, f=cv2.IMREAD_UNCHANGED: cv2.imread(os.path.join(SAU, f"{ma}_{s}.png"), f)
        d = r("depth").astype(np.float32) / 65535
        m1, m2 = r("mask1", 0), r("mask2", 0)
        d8 = (d * 255).astype(np.uint8)
        fill = lambda m: cv2.resize(cv2.inpaint(cv2.resize(d8, (W // 4, H // 4)), cv2.resize(cv2.dilate(m, np.ones((25, 25), np.uint8)), (W // 4, H // 4),
                                                interpolation=cv2.INTER_NEAREST), 5, cv2.INPAINT_TELEA), (W, H)).astype(np.float32) / 255
        l0 = r("l0"); l1 = r("l1"); l2 = r("l2")
        no = lambda x: cv2.dilate(x, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))  # QC mép (sửa 1): điểm mép mờ của lớp trước đi cùng vật
        _L[ma] = dict(d=d, dn=no(d), d0=fill(m1), d1=no(np.minimum(fill(m2), d)), l0=np.dstack([l0, np.full(l0.shape[:2], 255, np.uint8)]), l1=l1, l2=l2)
    return _L[ma]


GX, GY = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
PF = lambda d: 0.15 + 0.85 * d  # hệ số thị sai theo độ sâu (1 = gần)


def cam_luc(ma, u, i, bien):
    c = CAM[ma]; e = muot(u); lerp = lambda a, b: a + (b - a) * e
    (L0, L1) = c["L"]
    if bien in ("B", "C") and ma in KHOP and i > 0 and D.CANH[i - 1]["ma"].split(":")[0] == KHOP[ma][0] \
            and not (bien == "C" and KHOP[ma][0] in VEO):
        tr, A_tr, A_sau = KHOP[ma]; cp = CAM[tr]
        Pa = (np.array(A_tr) - np.array(cp["L"][1])) * cp["Z"][1]  # vị trí neo trước trên màn (so với tâm) ở cuối cảnh trước
        L0 = tuple(np.array(A_sau) - Pa / c["Z"][0])
    Z = lerp(*c["Z"]); K = lerp(*c["K"])
    Lx, Ly = lerp(L0[0], L1[0]), lerp(L0[1], L1[1])
    Tx, Ty = lerp(c["T"][0][0], c["T"][1][0]), lerp(c["T"][0][1], c["T"][1][1])
    if bien in ("B", "C"):  # rung tay rất nhẹ (≤ 1,5 px), tần số thấp
        tt = u * 3.0 + i
        Tx += 1.2 * math.sin(2.1 * tt) + 0.6 * math.sin(5.3 * tt); Ty += 1.0 * math.sin(1.7 * tt + 1) + 0.5 * math.sin(4.1 * tt)
    m = max(abs(Tx), abs(Ty)) / Z + 6
    Lx = min(max(Lx, W / (2 * Z) + m), W - W / (2 * Z) - m); Ly = min(max(Ly, H / (2 * Z) + m), H - H / (2 * Z) - m)
    return dict(L=(Lx, Ly), Z=Z, K=K, T=(Tx, Ty))


def warp(img, dep, cam):
    (Lx, Ly), Z, K, (Tx, Ty) = cam["L"], cam["Z"], cam["K"], cam["T"]
    Lx, Ly, Z, K, Tx, Ty = (np.float32(v) for v in (Lx, Ly, Z, K, Tx, Ty))
    sx = Lx + (GX - W / 2) / Z; sy = Ly + (GY - H / 2) / Z
    f = PF(cv2.remap(dep, sx, sy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE))
    sc = Z * (1 + K * f)
    mx = Lx + (GX - W / 2 - Tx * f) / sc; my = Ly + (GY - H / 2 - Ty * f) / sc
    return cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def len_man(cam, x, y, d):
    """Toạ độ khung tranh → toạ độ màn (độ sâu d)."""
    (Lx, Ly), Z, K, (Tx, Ty) = cam["L"], cam["Z"], cam["K"], cam["T"]; f = PF(d)
    sc = Z * (1 + K * f); return W / 2 + (x - Lx) * sc + Tx * f, H / 2 + (y - Ly) * sc + Ty * f


def tron(dst, src):
    a = src[..., 3:4].astype(np.float32) / 255
    return dst * (1 - a) + src[..., :3].astype(np.float32) * a


def mo(img, s):
    return img if s < 0.3 else cv2.GaussianBlur(img, (0, 0), s)


def nhieu(t, k=0):
    return (math.sin(1.3 * t + k) * 0.5 + math.sin(2.9 * t + 2 * k) * 0.3 + math.sin(0.7 * t + 3 * k) * 0.2)


def splat(fr, pts, mau):
    """pts: list (x, y, r, a) toạ độ màn → cộng sáng mềm."""
    lay = np.zeros((H // 2, W // 2), np.float32)
    for x, y, r, a in pts:
        if 0 <= x < W and 0 <= y < H: cv2.circle(lay, (int(x / 2), int(y / 2)), max(1, int(r / 2)), float(a), -1, cv2.LINE_AA)
    lay = cv2.resize(cv2.GaussianBlur(lay, (0, 0), 1.0), (W, H))[..., None]
    return fr + lay * np.array(mau, np.float32)[None, None, :]


def hieu_ung(fr, ma, cam, tau, dur, Ld):
    ten, p = HIEU_UNG[ma]; rng = np.random.default_rng(zlib.crc32(ma.encode()))
    if ten == "bui":
        x0, y0, x1, y1 = p["hop"]; n = p["n"]
        lum = cv2.GaussianBlur(cv2.cvtColor(Ld["l0"][..., :3], cv2.COLOR_BGR2GRAY), (0, 0), 25).astype(np.float32) / 255
        px = rng.uniform(x0, x1, n); py = rng.uniform(y0, y1, n); vx = rng.uniform(-10, 14, n); vy = rng.uniform(-6, 10, n)
        r = rng.uniform(2.0, 5.0, n); ph = rng.uniform(0, 6.28, n); dd = rng.uniform(0.35, 0.8, n)
        pts = []
        for k in range(n):
            x = x0 + (px[k] + vx[k] * tau - x0) % (x1 - x0); y = y0 + (py[k] + vy[k] * tau - y0) % (y1 - y0)
            sang = lum[int(min(y, H - 1)), int(min(x, W - 1))]
            a = 160 * max(sang - 0.12, 0) * (0.6 + 0.4 * math.sin(1.7 * tau + ph[k]))
            sx, sy = len_man(cam, x, y, dd[k]); pts.append((sx, sy, r[k] * cam["Z"], a))
        return splat(fr, pts, (0.75, 0.88, 1.0))  # BGR ấm
    if ten == "cat":
        dcat = float(Ld["d"][int((p["y0"] + p["y1"]) / 2), p["x"]])
        pts = []
        for k in range(60):  # hạt rơi 260 px/s, lệch nhẹ
            y = p["y0"] + ((k * 13.7 + tau * 260) % (p["y1"] - p["y0"]))
            x = p["x"] + rng.normal(0, 1.2)
            sx, sy = len_man(cam, x, y, dcat); pts.append((sx, sy, 2.4 * cam["Z"], 70))
        for k in range(14):  # dòng chảy liền
            y = p["y0"] + k * (p["y1"] - p["y0"]) / 14
            sx, sy = len_man(cam, p["x"], y, dcat); pts.append((sx, sy, 2.0 * cam["Z"], 55))
        return splat(fr, pts, (0.55, 0.75, 0.9))
    if ten == "den":
        cx, cy = p["c"]; d = float(Ld["d"][min(cy, H - 1), min(cx, W - 1)]); sx, sy = len_man(cam, cx, cy, d)
        k = 0.055 * nhieu(tau * 2.2, 1.0)  # ≤ ±5,5 %, < 3 Hz (an toàn thị giác)
        g = np.exp(-(((GX - sx) ** 2 + (GY - sy) ** 2) / (2 * (p["r"] * cam["Z"]) ** 2)))[..., None]
        return fr * (1 + k * g) + g * (18 + 14 * k / 0.055) * np.array((0.55, 0.8, 1.0), np.float32)
    if ten == "khoi":
        lay = np.zeros((H // 2, W // 2), np.float32); dk = float(Ld["d"][p["y"], p["x"]])
        for w in range(5):
            pha = w * 1.3; pts = []
            for j in range(40):
                h = j / 39 * p["cao"]; x = p["x"] - 14 + w * 7 + 16 * (h / p["cao"]) * math.sin(0.035 * h - 2.2 * tau + pha)
                sx, sy = len_man(cam, x, p["y"] - h, dk); pts.append((int(sx / 2), int(sy / 2)))
            al = 0.5 + 0.5 * math.sin(1.1 * tau + pha)
            for j in range(len(pts) - 1):
                fa = (1 - j / len(pts)) * al * 22
                cv2.line(lay, pts[j], pts[j + 1], float(fa), 5, cv2.LINE_AA)
        lay = cv2.resize(cv2.GaussianBlur(lay, (0, 0), 5), (W, H))[..., None]
        return fr + lay * np.array((0.85, 0.88, 0.9), np.float32)
    if ten == "quet":
        u = tau / dur; xc = -500 + u * (W + 1000)
        band = np.exp(-((GX + 0.45 * GY - xc) ** 2) / (2 * 170.0 ** 2))[..., None]
        return fr * (1 + 0.10 * band) + band * 10 * np.array((0.6, 0.85, 1.0), np.float32)
    return fr


_VEO = {}


def veo_khung(ma, tau):
    khe = VEO[ma]
    if khe not in _VEO:
        chon = json.load(open(os.path.join(ROOT, "reports", "mrp2", "veo", "chon.json")))
        cap = cv2.VideoCapture(os.path.join(ROOT, chon[khe])); fr = []
        while True:
            ok, f = cap.read()
            if not ok: break
            fr.append(cv2.resize(f, (W, H), interpolation=cv2.INTER_AREA) if f.shape[1] != W else f)
        _VEO[khe] = (fr, cap.get(cv2.CAP_PROP_FPS) or 24)
    fr, fps = _VEO[khe]
    return fr[min(int(tau * fps), len(fr) - 1)].astype(np.float32)


def ve_l1(i, t, bien):
    c = D.CANH[i]; ma = c["ma"].split(":")[0]
    d = c["e"] - c["s"] + T_HOA; u = min(max((t - c["s"]) / d, 0), 1); tau = max(t - c["s"], 0)
    if bien == "C" and ma in VEO:
        fr = veo_khung(ma, tau)
    else:
        Ld = lop(ma); cam = cam_luc(ma, u, i, bien)
        if bien == "P":  # đối chứng đo: cùng máy quay A, độ sâu phẳng → đúng "ảnh tĩnh trượt"
            Ld = dict(Ld); Ld.update({k: np.full_like(Ld["d"], 0.5) for k in ("d", "dn", "d0", "d1")})
        ten = HIEU_UNG[ma][0] if bien in ("B", "C") else None
        sig = (0, 0, 0)
        if ten == "net": a, b = HIEU_UNG[ma][1]["dau"], HIEU_UNG[ma][1]["cuoi"]; e = muot(min(max((u - 0.15) / 0.5, 0), 1)); sig = [x + (y - x) * e for x, y in zip(a, b)]
        if ten == "rung":
            k = tau - HIEU_UNG[ma][1]["t"]
            if k > 0: cam["T"] = (cam["T"][0], cam["T"][1] + 7 * math.exp(-k / 0.12) * math.cos(k * 40)); cam["Z"] *= 1 + 0.006 * math.exp(-k / 0.2)
        l2img = Ld["l2"]; l2dep = Ld["dn"]
        if ten == "lac":
            px, py = HIEU_UNG[ma][1]["p"]; ang = HIEU_UNG[ma][1]["a"] * math.exp(-tau / 2.6) * math.sin(2 * math.pi * tau / 1.5 + 0.6)
            M = cv2.getRotationMatrix2D((px, py), ang, 1.0)
            l2img = cv2.warpAffine(l2img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
        fr = warp(Ld["l0"], Ld["d0"], cam)[..., :3].astype(np.float32)
        fr = mo(fr, sig[0])
        fr = tron(fr, mo(warp(Ld["l1"], Ld["d1"], cam), sig[1]))
        fr = tron(fr, mo(warp(l2img, l2dep, cam), sig[2]))
        if ten in ("bui", "cat", "den", "khoi", "quet"): fr = hieu_ung(fr, ma, cam, tau, d, Ld)
    fr = np.clip(fr, 0, 255).astype(np.uint8)
    return Image.fromarray(fr[..., ::-1]).convert("RGBA")


def ve_canh(i, t, bien):
    c = D.CANH[i]
    if c["lop"] != "L1": return D.ve_canh(i, t)
    f = ve_l1(i, t, bien); o = D.nhan_lop(i)
    return Image.alpha_composite(f, o) if o is not None else f


def khung(t, bien, t_dau):
    """Như D.khung_luc, nhưng không hoà với cảnh ngoài đoạn thử (cảnh đầu đoạn vào thẳng)."""
    i = max(j for j, c in enumerate(D.CANH) if c["s"] <= max(t, t_dau + 0.05) + 1e-6)  # khung đầu đoạn (lệch ≤ 0,02 s) thuộc cảnh đầu đoạn
    f = ve_canh(i, t, bien)
    if D.CANH[i]["s"] > t_dau + 0.1 and t < D.CANH[i]["s"] + T_HOA:
        f = Image.blend(ve_canh(i - 1, t, bien), f, muot((t - D.CANH[i]["s"]) / T_HOA))
    for o, al in D.ov_luc(t):
        if al < 0.999: o = o.copy(); o.putalpha(o.getchannel("A").point(lambda v: int(v * al)))
        f = Image.alpha_composite(f, o)
    return f.convert("RGB")


def am(dst):
    """Âm = cắt từ bản đăng (giọng + nhạc giữ nguyên), nối 2 đoạn với tắt/mở 0,15 s."""
    fl = []; n = len(DOAN)
    for k, (a, b) in enumerate(DOAN):
        fl.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={b - a - 0.15:.3f}:d=0.15[a{k}]")
    fl.append("".join(f"[a{k}]" for k in range(n)) + f"concat=n={n}:v=0:a=1[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", GOC_1080, "-filter_complex", ";".join(fl), "-map", "[a]", "-c:a", "pcm_s16le", dst], check=True)


def khuc(args):
    bien, a, b, k, out = args
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "faster", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for n in range(int(round(a * FPS)), int(round(b * FPS))):
        p.stdin.write(khung(n / FPS, bien, DOAN[k][0]).tobytes())
    p.stdin.close(); p.wait(); return out


def to1s(f, dst, cot=10):
    tmp = os.path.join(TMP, "to"); os.makedirs(tmp, exist_ok=True)
    for x in os.listdir(tmp): os.remove(os.path.join(tmp, x))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", "fps=1,scale=320:180", os.path.join(tmp, "%03d.png")], check=True)
    fs = sorted(os.listdir(tmp)); r = math.ceil(len(fs) / cot); sh = Image.new("RGB", (320 * cot, 200 * r), (20, 20, 20))
    from PIL import ImageDraw
    dr = ImageDraw.Draw(sh)
    for k, x in enumerate(fs):
        sh.paste(Image.open(os.path.join(tmp, x)), ((k % cot) * 320, (k // cot) * 200)); dr.text(((k % cot) * 320 + 4, (k // cot) * 200 + 182), f"{k}s", fill=(255, 255, 0))
    sh.save(dst, quality=82)


def main():
    bien = sys.argv[1]; os.makedirs(XEM, exist_ok=True); t0 = time.time()
    wav = os.path.join(TMP, "am.wav"); am(wav)
    f1080 = os.path.join(TMP, f"{bien}_1080p.mp4")
    if bien == "goc":
        fl = [f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{k}]" for k, (a, b) in enumerate(DOAN)]
        fl.append("".join(f"[v{k}]" for k in range(len(DOAN))) + f"concat=n={len(DOAN)}:v=1:a=0[v]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", GOC_1080, "-i", wav, "-filter_complex", ";".join(fl), "-map", "[v]", "-map", "1:a",
                        "-c:v", "libx264", "-preset", "faster", "-crf", "19", "-c:a", "aac", "-b:a", "192k", f1080], check=True)
    else:
        from multiprocessing import Pool
        jobs = []
        for k, (a, b) in enumerate(DOAN):  # mỗi đoạn chia 2 khúc → 4 tiến trình
            m = round((a + b) / 2 * FPS) / FPS
            jobs += [(bien, a, m, k, os.path.join(TMP, f"{bien}_{k}a.mp4")), (bien, m, b, k, os.path.join(TMP, f"{bien}_{k}b.mp4"))]
        with Pool(4) as p: outs = p.map(khuc, jobs)
        lst = os.path.join(TMP, f"{bien}_ds.txt"); open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
        vid = os.path.join(TMP, f"{bien}_hinh.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", f1080], check=True)
    t_dung = time.time() - t0
    out = os.path.join(XEM, f"{bien}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f1080, "-vf", "scale=960:540", "-c:v", "libx264", "-preset", "medium", "-crf", "23",
                    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
    if "--to" in sys.argv: to1s(out, os.path.join(XEM, f"to1s_{bien}.jpg"))
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout)
    json.dump({"bien": bien, "giay_dung_1080p": round(t_dung, 1), "thoi_luong_s": round(dur, 2), "doan": DOAN, "tien_trinh": 4, "cpu": os.cpu_count()},
              open(os.path.join(ROOT, "reports", "mrp2", f"dung_{bien}.json"), "w"), indent=1)
    print(bien, "xong", round(t_dung, 1), "s dựng;", dur, "s")


if __name__ == "__main__":
    main()
