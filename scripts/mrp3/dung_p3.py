#!/usr/bin/env python3
"""MR-P3 · Dựng đoạn thử ~116 s tập 1 (P00–P01 + P15 S067–S068 + P16 S073 + P17 S078–S080) theo 3 mức sinh động — 0 USD, dựng lại được.
  MRP3_TMP=… python3 scripts/mrp3/dung_p3.py goc|M1|M2|M3|P1|P2 [--to]
  goc = cắt từ bản đăng (lab/mr6/dung/tap01_1080p.mp4, LFS), hình + âm
  M1  = 2.5D (scripts/mrp2: 3 lớp theo độ sâu, cong theo độ sâu từng điểm ảnh) + đúng 1 lớp phủ/cảnh + clip Veo 4 s ≈ 1/30 s
        (V01 a03, V02 b040 mới + K2, K3 của bản đăng) + tiếng động CC0 + điểm cắt L1→L1 khớp phách nhạc gốc + chữ động câu trích (S067, S073)
  M2  = M1 + clip 4 s phủ ≈ 1/3 thời lượng tranh (thêm V03–V06) + nhân vật đại diện chuyển động (cách (c): hoạt hoạ cắt ghép bằng mã,
        a01 + a04) + nhạc theo hồi (P00–P01: N1/N2 đã duyệt cắt theo hồi, lặng + va chạm ở cú lật S003; P15–P17: Eleven Music
        m_p15_17 4 hồi, dừng ở cảnh bắt S080) — điểm cắt khớp phách nhạc mới
  M3  = M2 + clip phủ ≈ 2/3 thời lượng tranh (thêm V07–V13; trộn 1080p và 720p phóng lên Lanczos)
  P1/P2 = đối chứng thước đo: cùng dòng thời gian/máy quay của M1 / M2–M3 trên tranh PHẲNG (ảnh tĩnh trượt thuần), cùng thẻ/nhãn, không clip
Lời, giọng, L2, L3, nhãn tầng/nguồn, thẻ chồng: GIỮ NGUYÊN bản đăng (gọi scripts/mr6/dung.py). Giọng = các đoạn TTS đã duyệt đặt
theo reports/mr6/moc_cau.json (như bản đăng). Ra: reports/mrp3/xem/<bien>.mp4 (540p, LFS), reports/mrp3/dung_<bien>.json,
reports/mrp3/dong_thoi_gian_<bien>.json; 1080p ở $MRP3_TMP (không đẩy — dựng lại được)."""
import json, math, os, re, subprocess, sys, time, zlib
import numpy as np, cv2
from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP3_TMP", "/tmp/claude-0/mrp3"); os.makedirs(TMP, exist_ok=True)
os.environ["MRP2_TMP"] = TMP; os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrp2")); sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))
_argv = sys.argv; sys.argv = sys.argv[:1]
import dung_thu as P  # noqa: E402  (2.5D + lớp phủ của MR-P2)
sys.argv = _argv
D = P.D
import l2  # noqa: E402
from l2 import fnt, muot, F_SERIF, F_MONO, NGA, DO, HPA  # noqa: E402

W, H, FPS, T_HOA = D.W, D.H, D.FPS, D.T_HOA
CFG = json.load(open(os.path.join(os.path.dirname(__file__), "doan.json")))
DOAN = [(round(a * FPS) / FPS, round(b * FPS) / FPS) for a, b in CFG["doan"]]
XEM = os.path.join(ROOT, "reports", "mrp3", "xem"); REP = os.path.join(ROOT, "reports", "mrp3")
GOC_1080 = os.path.join(ROOT, "lab", "mr6", "dung", "tap01_1080p.mp4")
CC0 = os.path.join(TMP, "cc0"); AM = os.path.join(ROOT, "lab", "mrp3", "am")
TONG_RA = sum(b - a for a, b in DOAN)


def t_ra(t):
    """giờ bản đăng → giờ bản thử (None nếu ngoài đoạn)."""
    o = 0.0
    for a, b in DOAN:
        if a - 1e-6 <= t <= b + 1e-6: return o + t - a
        o += b - a
    return None


def t_goc(tau):
    for a, b in DOAN:
        if tau < b - a: return a + tau
        tau -= b - a
    return DOAN[-1][1]


# ---------------- máy quay + lớp phủ theo tranh (toạ độ khung 1920×1080 của tranh) ----------------
def cam_mac_dinh(ma, nguoi):
    h = zlib.crc32(ma.encode()); s = 1 if h % 2 else -1; tr = 22 if nguoi else 30
    z0 = 1.30 if ma in ("b116", "b118") else 1.06  # b116:2, b118:2 — bản đăng dùng khung cắt sâu (MV2)
    if h % 3 == 0: T = ((0, s * tr * 0.7), (0, -s * tr * 0.7))
    else: T = ((s * tr, 0), (-s * tr, 0))
    return dict(L=((960 - s * 30, 545), (960 + s * 30, 535)), Z=(z0, z0 + 0.05), K=(0.0, 0.05), T=T)


HIEU = {  # đúng 1 hiệu ứng/cảnh, phát ra từ nguồn có trong tranh
    "a01": ("khoi", dict(x=688, y=800, cao=180)),          # hơi trà từ cốc
    "b064": ("den", dict(c=(800, 780), r=320)),            # màn hình điện thoại sáng lên ("phone lighting up")
    "a03": ("mua_kinh", dict(hop=(390, 30, 700, 400))),    # giọt mưa trượt trên kính cửa sổ
    "b065": ("den", dict(c=(1180, 660), r=300)),           # màn hình điện thoại trên bàn ướt
    "a02": ("den", dict(c=(840, 560), r=300)),             # màn hình điện thoại trong tay
    "a04": ("mua_kinh", dict(hop=(400, 90, 650, 340))),    # mưa trên kính phía sau
    "a05": ("khoi", dict(x=665, y=380, cao=150)),          # hơi từ cốc
    "b066": ("bui", dict(hop=(520, 100, 900, 1000), n=90)),  # bụi trong cột sáng giữa kệ
    "a07": ("bui", dict(hop=(700, 0, 1220, 900), n=110)),  # bụi trong đèn rọi
    "b001": ("den", dict(c=(600, 380), r=380)),            # bóng đèn gương chập chờn
    "b067": ("bui", dict(hop=(560, 60, 1320, 800), n=100)),  # bụi/khói mờ trong tia đèn trường quay
    "b062": ("khoi", dict(x=1500, y=860, cao=200)),        # hơi từ cốc
    "b002": ("cat", dict(x=1320, y0=560, y1=760)),         # cát chảy trong đồng hồ cát
    "a09": ("bui", dict(hop=(600, 0, 1300, 800), n=110)),  # bụi trong tia sáng kho phim
    "b070": ("den", dict(c=(880, 440), r=420)),            # đèn sau dải phim
    "a10": ("den", dict(c=(460, 260), r=380)),             # ánh TV
    "b003": ("quet", dict()),                              # vệt đèn quét qua hành lang
    "a15": ("bui", dict(hop=(600, 80, 1700, 520), n=130)),  # bụi trong chùm máy chiếu
    "b074": ("den", dict(c=(960, 240), r=600)),            # màn hình chập chờn
    "a12": ("quet", dict()),                               # nắng dịch qua mặt đá
    "b063": ("khoi", dict(x=700, y=820, cao=180)),         # hơi trà
    "b040": ("suong", dict(y0=520, y1=900)),               # sương trôi trên mặt hồ
    "b141": ("den", dict(c=(240, 40), r=520)),             # đèn bàn thở nhẹ
    "b051": ("bui", dict(hop=(400, 0, 1200, 800), n=110)),  # bụi trong tia nắng phòng xử
    "b116": ("suong", dict(y0=500, y1=1080)),              # sương mù trôi giữa nhà cao tầng
    "b052": ("rung", dict(t=0.9)),                         # rung khi cửa két khoá (khớp tiếng khoá)
    "b118": ("rung", dict(t=0.6)),                         # rung khi khoá bấm
    "b053": ("den", dict(c=(480, 224), r=420)),            # đèn bàn
}
NGUOI = {"a01", "a02", "a04", "a05", "a07", "b062", "b063", "b067", "b002", "b074", "b118"}
for _m in CFG["l1"]:
    P.CAM[_m] = cam_mac_dinh(_m, _m in NGUOI)
    P.HIEU_UNG[_m] = HIEU[_m]
P.KHOP = {}

# ---------------- clip theo mức ----------------
VEO_M1 = {"a03": "V01", "b040": "V02"}
VEO_M2 = {**VEO_M1, "b066": "V03", "a15": "V04", "b051": "V05", "b052": "V06"}
VEO_M3 = {**VEO_M2, "b001": "V07", "a09": "V08", "b116": "V09", "b003": "V10", "a12": "V11", "b141": "V12", "b070": "V13"}
VEO_BIEN = {"M1": VEO_M1, "M2": VEO_M2, "M3": VEO_M3}
NV_BIEN = {"M2": {"a01", "a04"}, "M3": {"a01", "a04"}}
CHON = os.path.join(REP, "veo", "chon.json")


def veo_tep(khe):
    c = json.load(open(CHON)) if os.path.exists(CHON) else {}
    if khe in c: return os.path.join(ROOT, c[khe])
    import glob
    f = sorted(glob.glob(os.path.join(ROOT, "lab", "mrp3", "veo", f"{khe}_*_l*.mp4")))
    return f[-1] if f else None


_V = {}


def veo_khung(khe, tau, dur_canh):
    if khe not in _V:
        cap = cv2.VideoCapture(veo_tep(khe)); fr = []
        while True:
            ok, f = cap.read()
            if not ok: break
            fr.append(cv2.resize(f, (W, H), interpolation=cv2.INTER_LANCZOS4) if f.shape[1] != W else f)  # 720p → 1080p Lanczos
        _V[khe] = (fr, cap.get(cv2.CAP_PROP_FPS) or 24)
    fr, fps = _V[khe]; dclip = len(fr) / fps
    giu = max(dur_canh - dclip + 0.05, 0)  # cảnh dài hơn clip: giữ khung đầu (= tranh) rồi chạy clip, không dãn (V2)
    k = 0 if tau < giu else min(int((tau - giu) * fps), len(fr) - 1)
    return fr[k].astype(np.float32)


# ---------------- (c) nhân vật đại diện: hoạt hoạ cắt ghép 2D bằng mã ----------------
NV = {  # mắt (cx, cy, rx, ry), trục cổ, vùng đầu (cx, cy, rx, ry), vùng thân — đo trên tranh 1920×1080 (tờ toạ độ MR-P3)
    "a01": dict(mat=[(1063, 312, 17, 8), (1151, 308, 18, 8)], co=(1150, 470), dau=(1140, 330, 200, 240), than=(1200, 760, 330, 260),
                chop=[0.7, 2.6], nghieng=1.4),
    "a04": dict(mat=[(1072, 312, 17, 8), (1153, 306, 18, 8)], co=(1150, 480), dau=(1145, 330, 200, 240), than=(1180, 760, 330, 260),
                chop=[0.5], nghieng=1.0),
}
GX, GY = P.GX, P.GY


def _mem(cx, cy, rx, ry, s=40):
    m = np.zeros((H, W), np.float32); cv2.ellipse(m, (int(cx), int(cy)), (int(rx), int(ry)), 0, 0, 360, 1.0, -1)
    return cv2.GaussianBlur(m, (0, 0), s)


_NVC = {}


def nv_khung(ma, tau):
    c = NV[ma]
    if ma not in _NVC:
        im = np.array(D.tranh(ma).convert("RGB"))[..., ::-1].astype(np.float32)
        nham = im.copy()  # ảnh mắt nhắm: lấp mắt bằng màu da dải ngay trên mắt + đường mi
        for (x, y, rx, ry) in c["mat"]:
            da = np.median(im[y - 3 * ry:y - ry - 2, x - rx:x + rx].reshape(-1, 3), 0)
            m = _mem(x, y + 1, rx + 2, ry + 1, 2.5)[..., None]; nham = nham * (1 - m) + da[None, None, :] * m
            cv2.ellipse(nham, (x, y + ry // 2), (rx, ry // 2 + 1), 0, 15, 165, (40, 45, 55), 2, cv2.LINE_AA)
        _NVC[ma] = (im, nham, _mem(*c["dau"]), _mem(*c["than"], 60))
    im, nham, md, mt = _NVC[ma]
    a = 0.0
    for tb in c["chop"]:
        u = (tau - tb) / 0.16
        if 0 <= u <= 1: a = max(a, 1 - abs(2 * u - 1))  # nhắm–mở 0,16 s
    f = im if a <= 0 else im * (1 - a) + nham * a
    th = math.radians(c["nghieng"] * math.sin(2 * math.pi * tau / 4.2 - 0.6))  # nghiêng đầu chậm quanh cổ
    px, py = c["co"]; dx = GX - px; dy = GY - py
    rx = px + dx * math.cos(th) + dy * math.sin(th) - GX; ry = py - dx * math.sin(th) + dy * math.cos(th) - GY
    tho = 2.0 * math.sin(2 * math.pi * tau / 3.4)  # thở: thân + đầu nâng/hạ ≤ 2 px
    mx = GX + rx * md; my = GY + ry * md + tho * np.maximum(mt, md)
    return cv2.remap(f, mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def nv_cam(img, u):
    """máy phẳng nhẹ cho cảnh nhân vật (PHONG-CACH đề xuất MR-P2 §7.8: biên độ nhỏ)."""
    e = muot(u); z = 1.04 + 0.05 * e; w, h = W / z, H / z; x0 = (W - w) / 2 + 20 * (e - 0.5); y0 = (H - h) / 2
    M = np.float32([[z, 0, -x0 * z], [0, z, -y0 * z]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


# ---------------- lớp phủ thêm (ngoài bộ MR-P2): mưa trên kính, sương trôi ----------------
def hieu_ung_them(fr, ma, cam, tau, Ld):
    ten, p = HIEU[ma]; rng = np.random.default_rng(zlib.crc32(ma.encode()))
    if ten == "mua_kinh":
        x0, y0, x1, y1 = p["hop"]; n = 26; pts = []
        X = rng.uniform(x0, x1, n); V = rng.uniform(25, 70, n); Y0 = rng.uniform(0, 1, n)
        for k in range(n):
            y = y0 + ((Y0[k] * (y1 - y0) + V[k] * tau) % (y1 - y0))
            for j in range(4):
                sx, sy = P.len_man(cam, X[k], y - j * 5, 0.2); pts.append((sx, sy, (2.6 - 0.4 * j) * cam["Z"], 34 - 7 * j))
        return P.splat(fr, pts, (0.85, 0.92, 1.0))
    if ten == "suong":
        y0, y1 = p["y0"], p["y1"]
        if "suong" not in Ld:
            r = np.random.default_rng(3); n = cv2.resize(r.random((12, 40)).astype(np.float32), (W * 2, H), interpolation=cv2.INTER_CUBIC)
            Ld["suong"] = cv2.GaussianBlur(n, (0, 0), 30)
        s = int(tau * 22) % W; band = Ld["suong"][:, s:s + W]
        v = np.clip((GY - y0) / 120, 0, 1) * np.clip((y1 - GY) / 120, 0, 1)
        return fr + (band * v * 26)[..., None] * np.array((0.95, 0.95, 0.9), np.float32)
    return P.hieu_ung(fr, ma, cam, tau, 1.0, Ld)


def ve_l1(i, t, bien):
    c = D.CANH[i]; ma = c["ma"].split(":")[0]
    d = c["e"] - c["s"] + T_HOA; u = min(max((t - c["s"]) / d, 0), 1); tau = max(t - c["s"], 0)
    if bien in VEO_BIEN and ma in VEO_BIEN[bien]:
        fr = veo_khung(VEO_BIEN[bien][ma], tau, d)
    elif bien in NV_BIEN and ma in NV_BIEN[bien]:
        fr = nv_cam(nv_khung(ma, tau), u)
    else:
        b = "P" if bien.startswith("P") else "A"
        Ld = P.lop(ma); cam = P.cam_luc(ma, u, i, b if b == "P" else "B")
        if b == "P":
            Ld = dict(Ld); Ld.update({k: np.full_like(Ld["d"], 0.5) for k in ("d", "dn", "d0", "d1")})
        ten = HIEU[ma][0] if not bien.startswith("P") else None
        sig = (0, 0, 0)
        if ten == "rung":
            k = tau - HIEU[ma][1]["t"]
            if k > 0: cam["T"] = (cam["T"][0], cam["T"][1] + 7 * math.exp(-k / 0.12) * math.cos(k * 40)); cam["Z"] *= 1 + 0.006 * math.exp(-k / 0.2)
        fr = P.warp(Ld["l0"], Ld["d0"], cam)[..., :3].astype(np.float32)
        fr = P.tron(fr, P.warp(Ld["l1"], Ld["d1"], cam))
        fr = P.tron(fr, P.warp(Ld["l2"], Ld["dn"], cam))
        if ten in ("bui", "cat", "den", "khoi", "quet"): fr = P.hieu_ung(fr, ma, cam, tau, d, Ld)
        elif ten in ("mua_kinh", "suong"): fr = hieu_ung_them(fr, ma, cam, tau, Ld)
    fr = np.clip(fr, 0, 255).astype(np.uint8)
    return Image.fromarray(fr[..., ::-1]).convert("RGBA")


# ---------------- chữ động câu trích (nguyên văn loi.json "chu", đã duyệt) ----------------
LOI = D.LOI
TRICH = {"S067": dict(nhan="lull"), "S073": dict(nhan="April")}


def trich_lop(cid, t):
    s, e = D.CS[cid]; cau = LOI[cid]["chu"].strip("“”\""); ws = cau.split()
    # mốc từng từ theo giọng: tìm lần lượt trong whisper
    if not hasattr(trich_lop, "mc"): trich_lop.mc = {}
    if cid not in trich_lop.mc:
        tw = [w for w in D.TU if s - 0.25 <= w["s"] <= e + 0.25]; out = []; j = 0
        for w in ws:
            k = D.norm(w); tt = None
            for jj in range(j, len(tw)):
                if k and D.norm(tw[jj]["w"]).startswith(k[:5]): tt = tw[jj]["s"]; j = jj + 1; break
            out.append(tt)
        last = s
        for n, x in enumerate(out):
            if x is None: out[n] = last + 0.15
            last = out[n]
        trich_lop.mc[cid] = out
    mc = trich_lop.mc[cid]
    o = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(o); f = fnt(F_SERIF, 58)
    # bố cục dòng
    lines, cur = [], []
    for k, w in enumerate(ws):
        tst = " ".join([ws[x] for x in cur] + [w])
        if cur and d.textlength("“" + tst + "”", font=f) > 1180: lines.append(cur); cur = []
        cur.append(k)
    lines.append(cur)
    hh = 78 * len(lines) + 70; y0 = 470 - hh // 2
    d.rectangle((90, y0, 1390, y0 + hh), fill=(14, 17, 21, 205)); d.rectangle((90, y0, 98, y0 + hh), fill=HPA + (255,) if LOI[cid]["tang"] == "◐" else DO + (255,))
    l2.CHU.add("“" + cau + "”")
    y = y0 + 35
    for li, ln in enumerate(lines):
        x = 140
        for k in ln:
            w = ws[k] + (" " if k < len(ws) - 1 else "")
            txtw = ("“" if k == 0 else "") + w + ("”" if k == len(ws) - 1 else "")
            a = muot((t - mc[k] + 0.05) / 0.25)
            if a > 0:
                col = DO if D.norm(ws[k]).startswith(D.norm(TRICH[cid]["nhan"])) else NGA
                dy = int(10 * (1 - a)); d.text((x, y + dy), txtw, font=f, fill=col + (int(255 * a),))
            x += d.textlength(txtw, font=f)
        y += 78
    return o


# ---------------- dòng thời gian (cắt khớp phách) ----------------
def phach(wav):
    """Phách trên dòng thời gian bản thử từ một tệp nhạc (đã đặt đúng giờ bản thử). Thông lượng phổ → tempo tự tương quan theo cửa sổ 12 s → pha."""
    import soundfile as sf
    x, sr = sf.read(wav, always_2d=True); x = x.mean(1)
    hop = 512; n = 2048; win = np.hanning(n)
    fr = np.lib.stride_tricks.sliding_window_view(np.pad(x, (0, n)), n)[::hop] * win
    S = np.log1p(np.abs(np.fft.rfft(fr, axis=1)) * 10); flux = np.maximum(np.diff(S, axis=0), 0).sum(1); flux = np.r_[0, flux]
    rms = np.sqrt((fr ** 2).mean(1)); env = flux - np.convolve(flux, np.ones(16) / 16, "same"); env = np.maximum(env, 0)
    dt = hop / sr; out = []
    for w0 in np.arange(0, len(env) * dt, 12.0):
        a, b = int(w0 / dt), int(min((w0 + 12) / dt, len(env)))
        e = env[a:b]; r = rms[a:b]
        if len(e) < 100 or r.mean() < 0.004: continue  # không nhạc
        ac = np.correlate(e - e.mean(), e - e.mean(), "full")[len(e) - 1:]
        lags = np.arange(len(ac)) * dt; ok = (lags >= 60 / 160) & (lags <= 60 / 70)
        if not ok.any(): continue
        L = np.argmax(np.where(ok, ac, -1e9)); per = L * dt
        best = max(range(L), key=lambda ph: e[ph::L].sum())
        out += [w0 + best * dt + k * per for k in range(int(12 / per) + 1) if w0 + best * dt + k * per < min(w0 + 12, len(env) * dt)]
    return sorted(out)


def lam_dong_thoi_gian(bien, beats):
    """Dời ranh giới GIỮA HAI CẢNH TRANH/CLIP kề nhau (L1→L1) tới phách gần nhất trong ±0,30 s; giữ mọi ranh có L2/L3 (gắn giọng)."""
    doi = []
    if not beats: return doi
    B = np.array(beats)
    for i in range(1, len(D.CANH)):
        a, c = D.CANH[i - 1], D.CANH[i]
        if not (a["lop"].startswith("L1") and c["lop"].startswith("L1")): continue
        tr = t_ra(c["s"])
        if tr is None or t_ra(a["s"]) is None: continue
        k = B[np.argmin(np.abs(B - tr))]
        if abs(k - tr) > 0.30 or abs(k - tr) < 0.02: continue
        ns = c["s"] + (k - tr)
        if ns - a["s"] < 1.0 or c["e"] - ns < 1.0: continue
        doi.append({"canh": c["ma"], "cu": round(c["s"], 3), "moi": round(ns, 3), "lech": round(k - tr, 3)})
        a["e"] = ns; c["s"] = ns
    return doi


# ---------------- khung ----------------
def ve_canh(i, t, bien):
    c = D.CANH[i]
    if c["lop"] == "L1": f = ve_l1(i, t, bien)
    elif c["lop"].startswith("L1-veo") and bien.startswith("P"):  # đối chứng: clip cũ thay bằng khung đầu phẳng (tranh gốc của clip)
        f = D.ve_canh(i, c["s"])
    else: f = D.ve_canh(i, t)
    o = D.nhan_lop(i)
    return Image.alpha_composite(f, o) if o is not None else f


def khung(t, bien, t_dau):
    i = max(j for j, c in enumerate(D.CANH) if c["s"] <= max(t, t_dau + 0.05) + 1e-6)
    f = ve_canh(i, t, bien)
    if D.CANH[i]["s"] > t_dau + 0.1 and t < D.CANH[i]["s"] + T_HOA:
        f = Image.blend(ve_canh(i - 1, t, bien), f, muot((t - D.CANH[i]["s"]) / T_HOA))
    for o, al in D.ov_luc(t):
        if al < 0.999: o = o.copy(); o.putalpha(o.getchannel("A").point(lambda v: int(v * al)))
        f = Image.alpha_composite(f, o)
    if bien in ("M1", "M2", "M3", "P1", "P2"):
        for cid, cf in TRICH.items():
            ma = [c for c in D.CANH if c["cau"] == cid and c["lop"].startswith("L1")][-1]
            if ma["s"] <= t <= ma["e"] + 0.2:
                o = trich_lop(cid, t); al = min((t - ma["s"]) / 0.3, (ma["e"] + 0.2 - t) / 0.3, 1.0)
                if al < 0.999: o.putalpha(o.getchannel("A").point(lambda v: int(v * max(al, 0))))
                f = Image.alpha_composite(f, o)
    return f.convert("RGB")


def khuc(args):
    bien, a, b, k, out = args
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "faster", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for n in range(int(round(a * FPS)), int(round(b * FPS))):
        p.stdin.write(khung(n / FPS, bien, DOAN[k][0]).tobytes())
    p.stdin.close(); p.wait(); return out


# ---------------- âm ----------------
def ff(*a): subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)


def giong_toan_tap(dst):
    """Giọng đã duyệt đặt theo moc_cau (như dung.am của MR-6, chỉ giọng)."""
    if os.path.exists(dst): return
    ins, fl = [], []
    for i, x in enumerate(D.M["doan"]):
        ins += ["-i", os.path.join(ROOT, x["tep"])]; ms = int(round(x["s"] * 1000)); fl.append(f"[{i}:a]aresample=48000,adelay={ms}|{ms}[v{i}]")
    nv = len(D.M["doan"]); fl.append("".join(f"[v{i}]" for i in range(nv)) + f"amix=inputs={nv}:normalize=0,apad,atrim=0:{D.TONG}[o]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[o]", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", dst)


def nhac_goc_toan_tap(dst):
    """Nhạc bản đăng (N1, N2 + lặng ở S080 + Aftermath), không giọng — lấy đúng bộ lọc dung.am của MR-6."""
    if os.path.exists(dst): return
    nh = os.path.join(ROOT, "lab", "mr5", "nhac"); CS = D.CS
    st2 = 487.9; cut = CS["S080"][0]; dur = cut - st2; st3 = cut + 1.5
    fl = ["[0:a]aresample=48000,volume=0.10,afade=t=out:st=34:d=6[n1]",
          f"[1:a]aresample=48000,atrim=0:{dur:.3f},volume='0.063+(0.126-0.063)*min(t/{dur:.3f},1)':eval=frame,afade=t=out:st={dur-0.08:.3f}:d=0.08,adelay={int(st2*1000)}|{int(st2*1000)}[n2a]",
          f"[2:a]aresample=48000,atrim=126:136,asetpts=PTS-STARTPTS,volume=0.05,afade=t=in:d=0.4,afade=t=out:st=8:d=2,adelay={int(st3*1000)}|{int(st3*1000)}[n2b]",
          f"[n1][n2a][n2b]amix=inputs=3:normalize=0,apad,atrim=0:{D.TONG}[o]"]
    ff("-i", os.path.join(nh, "N1_mo.mp3"), "-i", os.path.join(nh, "N2_tang_dan.mp3"), "-i", os.path.join(nh, "N2_tang_dan.mp3"),
       "-filter_complex", ";".join(fl), "-map", "[o]", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", dst)


def cat_doan(src, dst):
    """Cắt các đoạn thử từ tệp dòng thời gian bản đăng, nối, tắt/mở 0,15 s ở chỗ nối."""
    fl = []
    for k, (a, b) in enumerate(DOAN):
        fl.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={b - a - 0.15:.3f}:d=0.15[a{k}]")
    fl.append("".join(f"[a{k}]" for k in range(len(DOAN))) + f"concat=n={len(DOAN)}:v=0:a=1[a]")
    ff("-i", src, "-filter_complex", ";".join(fl), "-map", "[a]", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", dst)


def nhac_hoi(dst):
    """M2/M3 · nhạc chia theo hồi (dòng thời gian bản thử). P00–P01: N1 (móc) → dừng + va chạm ở chữ 'real' (cú lật S003) → N2 lớp đầu dưới P01 (dồn nhẹ tới S010).
    P15–P17: Eleven Music m_p15_17 (Lull 17,5 s · Countdown 9 s · Closing in 13 s · Aftermath), cắt cứng ở S080 rồi lặng 1,2 s, đuôi Aftermath."""
    nh = os.path.join(ROOT, "lab", "mr5", "nhac"); CS = D.CS
    lat = t_ra((D.tw("S003", "real") or CS["S003"][0] + 3.5) - 0.05); p01 = lat + 0.8;  # cú lật ở chữ "real": N1 dừng + va chạm, N2 vào sau 0,8 s (sửa lặng tuyệt đối 18–19,5 s ở bản dựng đầu)
    s2 = t_ra(DOAN[1][0]); s80 = t_ra(CS["S080"][0])
    fl = [f"[0:a]aresample=48000,atrim=0:{lat - 0.05:.3f},volume=0.11,afade=t=out:st={lat - 0.16:.3f}:d=0.1[a]",
          f"[1:a]aresample=48000,atrim=0:{s2 - p01:.3f},asetpts=PTS-STARTPTS,volume='0.07+0.06*min(t/{s2 - p01:.3f},1)':eval=frame,"
          f"afade=t=in:d=1.2,afade=t=out:st={s2 - p01 - 1.5:.3f}:d=1.5,adelay={int(p01*1000)}|{int(p01*1000)}[b]",
          f"[2:a]aresample=48000,atrim=0:{s80 - s2:.3f},asetpts=PTS-STARTPTS,volume=0.16,afade=t=in:d=0.3,afade=t=out:st={s80 - s2 - 0.06:.3f}:d=0.06,"
          f"adelay={int(s2*1000)}|{int(s2*1000)}[c]",
          f"[3:a]aresample=48000,atrim=40:48,asetpts=PTS-STARTPTS,volume=0.08,afade=t=in:d=0.5,afade=t=out:st=5:d=3,"
          f"adelay={int((s80+1.2)*1000)}|{int((s80+1.2)*1000)}[d]",
          f"[a][b][c][d]amix=inputs=4:normalize=0,apad,atrim=0:{TONG_RA}[o]"]
    m3 = os.path.join(AM, "m_p15_17.mp3")
    ff("-i", os.path.join(nh, "N1_mo.mp3"), "-i", os.path.join(nh, "N2_tang_dan.mp3"), "-i", m3, "-i", m3,
       "-filter_complex", ";".join(fl), "-map", "[o]", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", dst)


def sfx_ds(bien):
    """(tệp, giờ BẢN ĐĂNG, mức dB, thời lượng tối đa, lọc) — giờ theo mốc từ whisper/thẻ, đổi sang giờ bản thử lúc trộn."""
    tw, CS = D.tw, D.CS; e = lambda k: os.path.join(AM, k + ".mp3"); c = lambda k: os.path.join(CC0, k + ".mp3")
    hit = e("e_va_cham") if bien in ("M2", "M3") else c("no_xa")
    L = [(c("tu_lanh"), 0.0, -40, 11.8, None), (c("mua_kinh"), 5.3, -36, 6.5, None),
         (c("rung_dt"), 0.5, -22, 1.6, None), (c("bao_tin"), CS["S001"][0] + 0.4, -24, 1.5, None),
         (c("bao_tin"), CS["S002"][0] + 1.2, -26, 1.5, None),
         (hit, (tw("S003", "real") or CS["S003"][0] + 3.5) - 0.05, -20 if bien != "M1" else -24, 3.0, "lowpass=f=900" if bien == "M1" else None),
         (c("vut"), CS["S004"][0] - 0.5, -30, 1.2, None),
         (c("lat_trang"), 42.42, -26, 1.2, None),
         (c("bua"), tw("S010", "sentenced") or CS["S010"][0] + 1.5, -18, 1.5, None),
         (c("pho_dem"), 67.43, -34, 4.5, None),
         (c("lat_trang"), 492.9, -26, 1.2, None),
         (c("rung_dt") if bien == "M1" else e("e_rung_dt"), 503.0, -24, 2.0, None),
         (c("dong_ho") if bien == "M1" else e("e_dong_ho"), 543.7, -28, 8.8, None),
         (c("tim"), 546.9, -30, 5.6, "lowpass=f=300"),
         (c("lat_trang"), tw("S078", "filed") or CS["S078"][0] + 2, -26, 1.2, None),
         (c("khoa"), tw("S079", "freeze") or CS["S079"][0] + 3, -22, 1.5, None),
         (hit, tw("S080", "arrested") or CS["S080"][0] + 2, -18, 4.0, None)]
    return [x for x in L if t_ra(x[1]) is not None]


def am(bien, dst):
    giong = os.path.join(TMP, "giong_toan_tap.wav"); giong_toan_tap(giong)
    gd = os.path.join(TMP, "giong_doan.wav"); cat_doan(giong, gd)
    if bien == "M1":
        ng = os.path.join(TMP, "nhac_goc_toan_tap.wav"); nhac_goc_toan_tap(ng); nh = os.path.join(TMP, "nhac_M1.wav"); cat_doan(ng, nh)
    else:
        nh = os.path.join(TMP, "nhac_hoi.wav"); nhac_hoi(nh)
    sx = sfx_ds(bien); ins = ["-i", gd, "-i", nh]; fl = []
    for k, (f, t, db, dmax, loc) in enumerate(sx):
        ins += ["-i", f]; ms = int(t_ra(t) * 1000)
        fl.append(f"[{k+2}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{dmax},afade=t=out:st={max(dmax-0.3,0):.2f}:d=0.3,"
                  + (loc + "," if loc else "") + f"volume={db}dB,adelay={ms}|{ms}[s{k}]")
    n = len(sx); fl.append("[0:a][1:a]" + "".join(f"[s{k}]" for k in range(n)) + f"amix=inputs={n+2}:normalize=0,atrim=0:{TONG_RA}[m]")
    raw = dst + ".raw.wav"; ff(*ins, "-filter_complex", ";".join(fl), "-map", "[m]", "-ar", "48000", "-c:a", "pcm_s16le", raw)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    ff("-i", raw, "-af", f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
       f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true", "-ar", "48000", "-c:a", "pcm_s16le", dst)
    return nh, [{"tep": os.path.basename(x[0]), "gio_ban_thu": round(t_ra(x[1]), 2), "db": x[2]} for x in sx]


# ---------------- main ----------------
def to1s(f, dst, cot=10):
    P.to1s(f, dst, cot)


def main():
    bien = sys.argv[1]; os.makedirs(XEM, exist_ok=True); t0 = time.time(); info = {"bien": bien}
    f1080 = os.path.join(TMP, f"{bien}_1080p.mp4")
    if bien == "goc":
        ins, fl = [], []
        for k, (a, b) in enumerate(DOAN):  # tua theo đầu vào từng đoạn (trim nhiều đoạn trên một đầu vào làm hết bộ nhớ)
            ins += ["-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", GOC_1080]
            fl.append(f"[{k}:v]setpts=PTS-STARTPTS[v{k}];[{k}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={b-a-0.15:.3f}:d=0.15[a{k}]")
        fl.append("".join(f"[v{k}][a{k}]" for k in range(len(DOAN))) + f"concat=n={len(DOAN)}:v=1:a=1[v][a]")
        ff(*ins, "-filter_complex", ";".join(fl), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "faster", "-crf", "19",
           "-c:a", "aac", "-b:a", "192k", f1080)
    else:
        nhom = "M1" if bien in ("M1", "P1") else "M2"
        wav = os.path.join(TMP, f"am_{nhom}.wav")
        if bien.startswith("M") or not os.path.exists(wav):
            nh, sx = am(nhom, wav); info["tieng_dong"] = sx
        else: nh = os.path.join(TMP, "nhac_M1.wav" if nhom == "M1" else "nhac_hoi.wav")
        beats = phach(nh); info["so_phach"] = len(beats)
        info["doi_diem_cat"] = lam_dong_thoi_gian(bien, beats)
        info["dong_thoi_gian"] = [{"cau": c["cau"], "lop": c["lop"], "ma": c["ma"], "s_ra": round(t_ra(c["s"]), 3) if t_ra(c["s"]) is not None else None,
                                   "s": round(c["s"], 3), "e": round(c["e"], 3)} for c in D.CANH if any(a - 0.01 <= c["s"] < b for a, b in DOAN)
                                  or (c["s"] < DOAN[0][1] and c["e"] > DOAN[0][0])]
        from multiprocessing import Pool
        jobs = []
        for k, (a, b) in enumerate(DOAN):
            nk = max(1, round((b - a) / 15)); ranh = [round((a + (b - a) * j / nk) * FPS) / FPS for j in range(nk + 1)]
            jobs += [(bien, ranh[j], ranh[j + 1], k, os.path.join(TMP, f"{bien}_{k}_{j}.mp4")) for j in range(nk)]
        with Pool(4) as p: outs = p.map(khuc, jobs)
        lst = os.path.join(TMP, f"{bien}_ds.txt"); open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
        vid = os.path.join(TMP, f"{bien}_hinh.mp4"); ff("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid)
        ff("-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", f1080)
    info["giay_dung_1080p"] = round(time.time() - t0, 1)
    out = os.path.join(XEM, f"{bien}.mp4")
    ff("-i", f1080, "-vf", "scale=960:540", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out)
    if "--to" in sys.argv: to1s(out, os.path.join(XEM, f"to1s_{bien}.jpg"))
    info["thoi_luong_s"] = round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out],
                                                     capture_output=True, text=True).stdout), 2)
    info["doan"] = DOAN; info["cpu"] = os.cpu_count(); info["tien_trinh"] = 4
    json.dump(info, open(os.path.join(REP, f"dung_{bien}.json"), "w"), indent=1, ensure_ascii=False)
    print(bien, "xong", info["giay_dung_1080p"], "s dựng;", info["thoi_luong_s"], "s")


if __name__ == "__main__":
    main()
