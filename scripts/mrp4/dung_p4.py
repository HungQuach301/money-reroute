#!/usr/bin/env python3
"""MR-P4 · Sửa ÂM + CHUYỂN ĐỘNG MÁY trên đoạn thử MR-P3 (116 s, bản M2) — 0 USD, dựng lại được.
  MRP4_TMP=… python3 scripts/mrp4/dung_p4.py am        # âm mới + âm cũ tái dựng theo lớp, đo từng lớp → reports/mrp4/am_do.json
  MRP4_TMP=… python3 scripts/mrp4/dung_p4.py M2_moi    # hình mới (từ vựng máy + cổng độ sâu + 10 tranh nhiều lớp) + âm mới
  MRP4_TMP=… python3 scripts/mrp4/dung_p4.py xem       # M2_cu (= reports/mrp3/xem/M2.mp4), ghép cạnh nhau, bản loa điện thoại
Giữ nguyên MR-P3 M2: lời, giọng, L2, L3, nhãn, thẻ, clip, nhân vật hoạt hoạ mã, nhạc theo hồi, điểm cắt khớp phách (cùng nguồn phách).
Đổi: (1) máy quay theo scripts/mrp4/may.py (một kiểu/cảnh, neo theo từ, cổng độ sâu HD); (2) 10 tranh phẳng nhất thay bằng tranh nhiều lớp
(lab/mrp4/anh, chọn ở reports/mrp4/anh/chon.json; lớp phủ đặt lại theo tranh mới); (3) chuỗi âm mới (giọng nén + nâng 2–5 kHz + khử xì;
nhạc −12…−15 dB dưới lời, sidechain; tiếng nhấn −6…−10 dB; tiếng nền −22…−28 dB; tổng −14 LUFS, TP ≤ −1 dBTP)."""
import json, math, os, shutil, subprocess, sys, time
import numpy as np, cv2
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP4_TMP", "/tmp/claude-0/mrp4/w"); os.makedirs(TMP, exist_ok=True)
os.environ["MRP3_TMP"] = TMP
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrp3")); sys.path.insert(0, os.path.dirname(__file__))
_argv = sys.argv; sys.argv = sys.argv[:1]
import dung_p3 as P3  # noqa: E402
sys.argv = _argv
import may  # noqa: E402
P, D = P3.P, P3.D
W, H, FPS, T_HOA = P3.W, P3.H, P3.FPS, P3.T_HOA
REP = os.path.join(ROOT, "reports", "mrp4"); XEM = os.path.join(REP, "xem"); os.makedirs(XEM, exist_ok=True)
HD = {k: v["HD"] for k, v in json.load(open(os.path.join(REP, "do_sau.json")))["tranh"].items()}
HD_MOI = {k: v["HD"] for k, v in json.load(open(os.path.join(REP, "do_sau_moi.json")))["tranh"].items()} if os.path.exists(os.path.join(REP, "do_sau_moi.json")) else {}
CHON = json.load(open(os.path.join(REP, "anh", "chon.json")))
VEO = P3.VEO_M2; NV = P3.NV_BIEN["M2"]
# lớp phủ đặt lại theo bố cục tranh mới (cùng loại hiệu ứng như MR-P3, nguồn có trong tranh mới)
HIEU_MOI = {
    "a10": ("den", dict(c=(1568, 351), r=380)),             # ánh TV (góc phải)
    "b118": ("rung", dict(t=0.6)),                          # rung khi khoá (đặt lại theo từ 'freeze')
    "b003": ("quet", dict()),                               # vệt đèn quét qua hành lang
    "b141": ("den", dict(c=(590, 100), r=420)),             # đèn bàn thở nhẹ
    "b116": ("suong", dict(y0=380, y1=760)),                # sương giữa nhà cao tầng
    "b001": ("den", dict(c=(619, 422), r=380)),             # bóng đèn gương chập chờn
    "b070": ("den", dict(c=(500, 440), r=420)),             # đèn sau dải phim
    "a12": ("quet", dict()),                                # nắng dịch qua mặt đá
    "b002": ("cat", dict(x=981, y0=560, y1=655)),           # cát chảy trong đồng hồ cát
    "a09": ("bui", dict(hop=(950, 120, 1300, 760), n=90)),  # bụi trong tia sáng cuối lối đi
}


def tranh_moi(ma):
    im = Image.open(os.path.join(ROOT, CHON[ma])).convert("RGB")
    r = max(W / im.width, H / im.height); im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2; return im.crop((x0, y0, x0 + W, y0 + H))


def nap_tranh_moi():
    """thay tranh + lớp độ sâu + lớp phủ cho 10 tranh tạo lại (chỉ trong bản thử)."""
    goc = P.SAU; P.SAU = os.path.join(TMP, "sau_moi")
    for ma in CHON:
        D._TR[ma] = tranh_moi(ma); P._L.pop(ma, None); P.lop(ma)
        P3.HIEU[ma] = HIEU_MOI[ma]; P.HIEU_UNG[ma] = HIEU_MOI[ma]
    P.SAU = goc


def hd(ma): return HD_MOI.get(ma, HD.get(ma)) if MOI else HD.get(ma)


MOI = False
NHAT_KY = {}


def ke_hoach(i):
    """→ (kiểu thực, spec, ta, te) của cảnh L1 i."""
    c = D.CANH[i]; key = c["ma"]; ma = key.split(":")[0]; spec = may.KIEU.get(key) or may.KIEU.get(ma) or dict(k="dung", neo=None, ly_do="mặc định")
    d = c["e"] - c["s"] + T_HOA
    if ma in VEO or ma in NV: k, gc = (spec["k"], "")
    else: k, gc = may.cong(spec, hd(ma))
    ta = 0.0
    if spec.get("neo"):
        tw = D.tw(*spec["neo"])
        ta = (tw - c["s"] - 0.15) if tw is not None else 0.0
    neo_ngoai = not (0 <= ta <= d - 0.3)
    ta = min(max(ta, 0.0), max(d - 0.9, 0.0))
    if key not in NHAT_KY:
        NHAT_KY[key] = dict(ma=key, kieu=may.TEN[k], kieu_ma=k, vao=may.TEN.get(spec.get("vao"), ""), ly_do=spec["ly_do"],
                            tu_neo=" ".join(spec["neo"]) if spec.get("neo") else "—", neo_giay_trong_canh=round(ta, 2), neo_ngoai_canh=neo_ngoai,
                            bien_do=may.bien_do(k, spec), HD=hd(ma), cong_do_sau=gc)
    return k, spec, ta, d


def cam2d(img, Z, L):
    M = np.float32([[Z, 0, W / 2 - L[0] * Z], [0, Z, H / 2 - L[1] * Z]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def ve_l1(i, t, bien):
    c = D.CANH[i]; ma = c["ma"].split(":")[0]; tau = max(t - c["s"], 0)
    k, spec, ta, d = ke_hoach(i)
    if ma in VEO:
        fr = P3.veo_khung(VEO[ma], tau, d)
        if k in ("day", "keo"):
            cm = may.kep(may.cam(k, spec, 100, tau, ta, d)); fr = cam2d(fr, cm["Z"], cm["L"])
    elif ma in NV:
        fr = P3.nv_khung(ma, tau)
        cm = may.kep(may.cam(k, spec, hd(ma), tau, ta, d)); fr = cam2d(fr, cm["Z"], cm["L"])
    else:
        Ld = P.lop(ma); cm = may.kep(may.cam(k, spec, hd(ma), tau, ta, d))
        ten = P3.HIEU[ma][0]
        if ten == "rung" and spec.get("rung"):
            cm["T"] = (cm["T"][0], cm["T"][1] + may.rung(tau, ta + 0.15)); cm["Z"] *= 1 + 0.006 * math.exp(-max(tau - ta - 0.15, 0) / 0.2) * (tau > ta + 0.15)
        fr = P.warp(Ld["l0"], Ld["d0"], cm)[..., :3].astype(np.float32)
        fr = P.tron(fr, P.warp(Ld["l1"], Ld["d1"], cm))
        fr = P.tron(fr, P.warp(Ld["l2"], Ld["dn"], cm))
        if ten in ("bui", "cat", "den", "khoi", "quet"): fr = P.hieu_ung(fr, ma, cm, tau, d, Ld)
        elif ten in ("mua_kinh", "suong"): fr = P3.hieu_ung_them(fr, ma, cm, tau, Ld)
    fr = np.clip(fr, 0, 255).astype(np.uint8)
    return Image.fromarray(fr[..., ::-1]).convert("RGBA")


P3.ve_l1 = ve_l1
GIAT = []  # [(giờ bản thử, hướng)]
G_RA, G_VAO = 0.14, 0.18


def lap_giat():
    GIAT.clear()
    for c in D.CANH:
        sp = may.KIEU.get(c["ma"]) or may.KIEU.get(c["ma"].split(":")[0])
        if sp and sp.get("vao") == "giat" and P3.t_ra(c["s"]) is not None: GIAT.append((P3.t_ra(c["s"]), sp.get("huong", 1)))


def nhoe(img, o, blur):
    a = np.array(img.convert("RGB")); M = np.float32([[1, 0, o], [0, 1, 0]])
    a = cv2.warpAffine(a, M, (W, H), borderMode=cv2.BORDER_REFLECT)
    if blur >= 3: a = cv2.blur(a, (int(blur), 1))
    return Image.fromarray(a).convert("RGBA")


def khung(t, bien, t_dau):
    i = max(j for j, c in enumerate(D.CANH) if c["s"] <= max(t, t_dau + 0.05) + 1e-6)
    f = P3.ve_canh(i, t, bien); tr = P3.t_ra(t) if P3.t_ra(t) is not None else -9
    giat_vao = [g for g in GIAT if g[0] - 0.01 <= tr < g[0] + G_VAO]
    giat_ra = [g for g in GIAT if g[0] - G_RA <= tr < g[0] - 0.01]
    if giat_ra:
        q = (tr - (giat_ra[0][0] - G_RA)) / G_RA; f = nhoe(f, -giat_ra[0][1] * W * 0.45 * q * q, 40 + 300 * q)
    elif giat_vao:
        q = (tr - giat_vao[0][0]) / G_VAO; f = nhoe(f, giat_vao[0][1] * W * 0.45 * (1 - q) ** 2, 300 * (1 - q))
    elif D.CANH[i]["s"] > t_dau + 0.1 and t < D.CANH[i]["s"] + T_HOA and not any(abs(g - (P3.t_ra(D.CANH[i]["s"]) or -9)) < 0.05 for g, _ in GIAT):
        f = Image.blend(P3.ve_canh(i - 1, t, bien), f, P3.muot((t - D.CANH[i]["s"]) / T_HOA))
    for o, al in D.ov_luc(t):
        if al < 0.999: o = o.copy(); o.putalpha(o.getchannel("A").point(lambda v: int(v * al)))
        f = Image.alpha_composite(f, o)
    for cid in P3.TRICH:
        ma = [c for c in D.CANH if c["cau"] == cid and c["lop"].startswith("L1")][-1]
        if ma["s"] <= t <= ma["e"] + 0.2:
            o = P3.trich_lop(cid, t); al = min((t - ma["s"]) / 0.3, (ma["e"] + 0.2 - t) / 0.3, 1.0)
            if al < 0.999: o.putalpha(o.getchannel("A").point(lambda v: int(v * max(al, 0))))
            f = Image.alpha_composite(f, o)
    return f.convert("RGB")


def khuc(args):
    bien, a, b, k, out = args
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "faster", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for n in range(int(round(a * FPS)), int(round(b * FPS))):
        p.stdin.write(khung(n / FPS, bien, P3.DOAN[k][0]).tobytes())
    p.stdin.close(); p.wait(); return out


# ====================================== ÂM ======================================
SR = 48000
ff = P3.ff


def doc(f):
    import soundfile as sf
    x, sr = sf.read(f, always_2d=True, dtype="float32"); assert sr == SR, (f, sr)
    if x.shape[1] == 1: x = np.repeat(x, 2, 1)
    n = int(round(P3.TONG_RA * SR)); return np.pad(x, ((0, max(n - len(x), 0)), (0, 0)))[:n]


def ghi(f, x):
    import soundfile as sf
    sf.write(f, x, SR, subtype="FLOAT")


def db(x): return 20 * math.log10(max(x, 1e-12))


_MET = None


def lufs(x):
    global _MET
    import pyloudnorm as pyln
    if _MET is None: _MET = pyln.Meter(SR)
    if len(x) < int(0.4 * SR): return -99.0
    v = _MET.integrated_loudness(x.astype(np.float64)); return -99.0 if not np.isfinite(v) else float(v)


def mom_max(x, a, b):
    """độ to tức thời (cửa sổ 400 ms, bước 100 ms) lớn nhất trong [a, b] giây."""
    best = -99.0
    for s in np.arange(max(a - 0.1, 0), max(b - 0.4, a) + 1e-6, 0.1):
        i = int(s * SR); best = max(best, lufs(x[i:i + int(0.4 * SR)]))
    return best


def co_loi(v, nguong_db=-42):
    """mặt nạ khung 100 ms có lời (RMS giọng > ngưỡng)."""
    n = int(0.1 * SR); m = len(v) // n; r = np.sqrt((v[:m * n].mean(1).reshape(m, n) ** 2).mean(1) + 1e-12)
    a = 20 * np.log10(r) > nguong_db
    a = np.convolve(a.astype(float), np.ones(3), "same") > 0  # nới 100 ms hai phía
    return np.repeat(a, n)[:len(v)] if len(a) else a


def gom(x, mask):
    return x[:len(mask)][mask]


def dat_sfx(f, t_ban_thu, dmax, loc, dst):
    ms = int(t_ban_thu * 1000)
    ff("-i", f, "-filter_complex", f"[0:a]aresample={SR},aformat=channel_layouts=stereo,atrim=0:{dmax},afade=t=out:st={max(dmax - 0.3, 0):.2f}:d=0.3,"
       + (loc + "," if loc else "") + f"adelay={ms}|{ms},apad,atrim=0:{P3.TONG_RA}[o]", "-map", "[o]", "-ar", str(SR), "-c:a", "pcm_f32le", dst)


NEN = {"tu_lanh", "mua_kinh", "pho_dem", "dong_ho", "e_dong_ho", "tim"}  # tiếng nền (liên tục); còn lại = tiếng nhấn
MT_NHAC, MT_NHAN, MT_NEN = -13.5, -8.0, -25.0  # đích tương đối so với độ to giọng (dB / LU)


def ds_sfx():
    L = P3.sfx_ds("M2"); vut = os.path.join(P3.CC0, "vut.mp3")
    # tiếng vút cũ trùng cú giật (±0,5 s) → bỏ, tiếng vút của cú giật thay chỗ
    L = [x for x in L if not (x[0] == vut and any(abs(P3.t_ra(x[1]) - (g - 0.30)) < 0.5 for g, _ in GIAT))]
    for tw, _h in GIAT: L.append((vut, P3.t_goc(max(tw - 0.30, 0)), -30, 1.0, None))
    return L


GIONG_AF = ("highpass=f=70,acompressor=threshold=-22dB:ratio=3:attack=8:release=120:knee=4:makeup=3dB,equalizer=f=250:t=q:w=1:g=-1.5,"
            "equalizer=f=3200:t=q:w=0.9:g=4,equalizer=f=7000:t=q:w=1:g=-3,deesser=i=0.4:m=0.5:f=0.5:s=o")


def chuoi_giong(src, dst):
    """giọng: lọc thấp 70 Hz → nén nhẹ 3:1 (+3 dB) → giảm đục 250 Hz (−1,5 dB) → nâng 2–5 kHz (+4 dB @ 3,2 kHz, Q 0,9)
    → hạ 7 kHz (−3 dB) bù phần nâng lan sang dải xì → khử xì động (deesser). Chọn sau thử 7 cấu hình (BAO-CAO §3)."""
    ff("-i", src, "-af", GIONG_AF, "-ar", str(SR), "-c:a", "pcm_f32le", dst)


def dinh_xi(x):
    """đỉnh xì: phân vị 95 của tỉ lệ năng lượng dải 5–9 kHz / toàn dải trên khung 20 ms có tiếng (dB) — thấp hơn = ít chói."""
    m = x.mean(1); n = 960; k = len(m) // n; F = np.abs(np.fft.rfft(m[:k * n].reshape(k, n) * np.hanning(n), axis=1)) ** 2; fr = np.fft.rfftfreq(n, 1 / SR)
    s = F[:, (fr >= 5000) & (fr <= 9000)].sum(1); t = F.sum(1); ok = t > np.percentile(t, 40)
    return 10 * math.log10(np.percentile(s[ok] / t[ok], 95))


def xi(x):
    """tỉ lệ năng lượng dải xì 5–9 kHz / toàn dải của giọng (dB)."""
    m = x.mean(1); S = np.abs(np.fft.rfft(m)) ** 2; f = np.fft.rfftfreq(len(m), 1 / SR)
    return db(math.sqrt(S[(f >= 5000) & (f <= 9000)].sum() / S.sum()))


def bang_tan(x, a, b):
    m = x.mean(1); S = np.abs(np.fft.rfft(m)) ** 2; f = np.fft.rfftfreq(len(m), 1 / SR)
    return db(math.sqrt(S[(f >= a) & (f <= b)].sum() / S.sum()))


def master(mix, dst):
    """đưa tổng về −14 LUFS bằng một hệ số tuyến tính; đỉnh thật > −1 dBTP → limiter ở 192 kHz (xấp xỉ đỉnh thật) rồi đo lại."""
    g = -14.0 - lufs(mix); y = mix * 10 ** (g / 20); raw = dst + ".pre.wav"; ghi(raw, y)
    tp = do_ebur(raw)["TP"]; han = False
    if tp > -1.2:
        han = True
        ff("-i", raw, "-af", "aresample=192000,alimiter=limit=0.83:attack=1:release=60:level=false:asc=1,aresample=48000", "-c:a", "pcm_f32le", dst + ".lim.wav")
        y = doc(dst + ".lim.wav"); g2 = -14.0 - lufs(y); y = y * 10 ** (g2 / 20); g += g2
        ghi(raw, y)
    ff("-i", raw, "-c:a", "pcm_s16le", dst)
    return g, han


def do_ebur(f):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"], capture_output=True, text=True).stderr
    s = r[r.rindex("Summary:"):]
    import re
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+)", s).group(1))
    return {"I": g("I"), "LRA": g("LRA"), "TP": g("Peak")}


def am():
    lap_giat_tu_dung()
    gd = os.path.join(TMP, "giong_doan.wav")
    if not os.path.exists(gd): P3.giong_toan_tap(os.path.join(TMP, "giong_toan_tap.wav")); P3.cat_doan(os.path.join(TMP, "giong_toan_tap.wav"), gd)
    nh = os.path.join(TMP, "nhac_hoi.wav")
    if not os.path.exists(nh): P3.nhac_hoi(nh)
    gp = os.path.join(TMP, "giong_xu_ly.wav"); chuoi_giong(gd, gp)
    v0, v = doc(gd), doc(gp); m = doc(nh); mask = co_loi(v0)
    # nhạc: sidechain (giọng điều khiển) → tự hạ khi có lời, dâng lại ở khoảng nghỉ
    nd = os.path.join(TMP, "nhac_duck.wav")
    ff("-i", nh, "-i", gp, "-filter_complex", "[1:a]asplit=1[sc];[0:a][sc]sidechaincompress=threshold=0.025:ratio=6:attack=25:release=450:knee=3:makeup=1[o]",
       "-map", "[o]", "-ar", str(SR), "-c:a", "pcm_f32le", nd)
    md = doc(nd)
    Iv = lufs(gom(v, mask))  # độ to giọng (chỉ đoạn có lời)
    gm = Iv + MT_NHAC - lufs(gom(md, mask)); md = md * 10 ** (gm / 20)
    # tiếng động: từng tiếng một tệp, đo rồi đặt mức theo đích tương đối
    sx = ds_sfx(); stems_nhan = np.zeros_like(v); stems_nen = np.zeros_like(v); ds = []
    for n, (f, t, db_cu, dmax, loc) in enumerate(sx):
        tr = P3.t_ra(t); dst = os.path.join(TMP, f"sfx_{n:02d}.wav"); dat_sfx(f, tr, dmax, loc, dst); x = doc(dst)
        ten = os.path.basename(f)[:-4]; nen = ten in NEN
        a, b = tr, min(tr + dmax, P3.TONG_RA)
        do = lufs(x[int(a * SR):int(b * SR)]) if nen else mom_max(x, a, b)
        g = (Iv + (MT_NEN if nen else MT_NHAN)) - do; x = x * 10 ** (g / 20)
        (stems_nen if nen else stems_nhan)[:] += x
        ds.append(dict(tep=ten, lop="nền" if nen else "nhấn", gio=round(tr, 2), db_cu=db_cu, do_0dB=round(do, 1), g_db=round(g, 1)))
    mix = v + md + stems_nhan + stems_nen
    out = os.path.join(TMP, "am_M2_moi.wav"); G, han = master(mix, out)
    k = 10 ** (G / 20)
    lop = do_lop(v * k, md * k, stems_nhan * k, stems_nen * k, sx, mask, ds)
    # âm cũ (MR-P3 M2) tái dựng theo lớp, cùng mức dB và cùng hệ số loudnorm tuyến tính
    cu = am_cu(v0, m, sx, mask)
    tong = do_ebur(out); r = dict(moi=dict(lop=lop, tong=tong, han_dinh=han, he_so_tong_db=round(G, 2), tieng_dong=ds,
                                           giong_xi_5_9k_db=round(xi(v0), 2), giong_xi_sau_db=round(xi(v), 2),
                                           giong_2_5k_truoc_db=round(bang_tan(v0, 2000, 5000), 2), giong_2_5k_sau_db=round(bang_tan(v, 2000, 5000), 2),
                                           giong_dinh_xi_truoc_db=round(dinh_xi(v0), 2), giong_dinh_xi_sau_db=round(dinh_xi(v), 2),
                                           giong_ngan_han_p10_p50_truoc=ngan_han(v0, mask), giong_ngan_han_p10_p50_sau=ngan_han(v, mask)),
                                  cu=cu, dich=dict(nhac_duoi_loi=MT_NHAC, nhan=MT_NHAN, nen=MT_NEN, tong_LUFS=-14, TP_toi_da=-1.0),
                                  chuoi_giong=GIONG_AF,
                                  sidechain="sidechaincompress ngưỡng 0,025 (−32 dBFS), 6:1, attack 25 ms, release 450 ms, giọng làm tín hiệu điều khiển")
    json.dump(r, open(os.path.join(REP, "am_do.json"), "w"), indent=1, ensure_ascii=False); print(json.dumps(r["moi"]["lop"], ensure_ascii=False, indent=1)); print(tong)


def ngan_han(v, mask):
    """độ to ngắn hạn (3 s, bước 1 s) của giọng: p10 và p50 (LUFS) — khoảng cách nhỏ = chỗ nhỏ được nâng."""
    vals = [lufs(v[int(s * SR):int((s + 3) * SR)]) for s in np.arange(0, P3.TONG_RA - 3, 1.0) if mask[int(s * SR):int((s + 3) * SR)].mean() > 0.6]
    vals = [x for x in vals if x > -70]; return [round(float(np.percentile(vals, 10)), 1), round(float(np.percentile(vals, 50)), 1)]


def do_lop(v, m, nhan, nen, sx, mask, ds):
    Iv = lufs(gom(v, mask)); nghi = ~mask
    r = dict(giong_LUFS=round(Iv, 1), nhac_duoi_loi_LUFS=round(lufs(gom(m, mask)), 1), nhac_khoang_nghi_LUFS=round(lufs(gom(m, nghi)), 1))
    r["nhac_duoi_loi_so_giong_dB"] = round(r["nhac_duoi_loi_LUFS"] - Iv, 1); r["nhac_khoang_nghi_so_giong_dB"] = round(r["nhac_khoang_nghi_LUFS"] - Iv, 1)
    a_nhan, a_nen = [], []
    for (f, t, _db, dmax, _l) in sx:
        ten = os.path.basename(f)[:-4]; tr = P3.t_ra(t); a, b = tr, min(tr + dmax, P3.TONG_RA)
        if ten in NEN: a_nen.append(round(lufs(nen[int(a * SR):int(b * SR)]) - Iv, 1))
        else: a_nhan.append(round(mom_max(nhan, a, b) - Iv, 1))
    r["nhan_so_giong_dB"] = a_nhan; r["nen_so_giong_dB"] = a_nen
    return r


def am_cu(v0, m, sx, mask):
    """MR-P3 M2: giọng thô 0 dB + nhạc theo hồi (mức trong nhac_hoi) + tiếng động theo dB cũ (đủ 17 tiếng của dung_p3.sfx_ds("M2")),
    rồi loudnorm tuyến tính về −14 (như dung_p3.am)."""
    sx = P3.sfx_ds("M2"); nhan = np.zeros_like(v0); nen = np.zeros_like(v0)
    for n, (f, t, dbc, dmax, loc) in enumerate(sx):
        dst = os.path.join(TMP, f"sfxcu_{n:02d}.wav"); dat_sfx(f, P3.t_ra(t), dmax, loc, dst); x = doc(dst) * 10 ** (dbc / 20)
        (nen if os.path.basename(f)[:-4] in NEN else nhan)[:] += x
    mix = v0 + m + nhan + nen; G = -14.0 - lufs(mix); k = 10 ** (G / 20)
    r = do_lop(v0 * k, m * k, nhan * k, nen * k, sx, mask, None)
    r["ghi_chu"] = "tái dựng từng lớp với mức của scripts/mrp3/dung_p3.py (M2) + hệ số loudnorm tuyến tính; tổng đo trên tệp thật reports/mrp3/xem/M2.mp4"
    return r


def lap_giat_tu_dung():
    """dòng thời gian M2 (điểm cắt khớp phách từ cùng nhạc theo hồi) → giờ giật."""
    if getattr(lap_giat_tu_dung, "xong", False): return
    nh = os.path.join(TMP, "nhac_hoi.wav")
    if not os.path.exists(nh): P3.nhac_hoi(nh)
    lap_giat_tu_dung.doi = P3.lam_dong_thoi_gian("M2", P3.phach(nh)); lap_giat(); lap_giat_tu_dung.xong = True


# ====================================== HÌNH ======================================
def dung_hinh(bien):
    global MOI
    MOI = True; nap_tranh_moi(); lap_giat_tu_dung(); t0 = time.time()
    info = dict(bien=bien, doi_diem_cat=lap_giat_tu_dung.doi, giat=[dict(gio=round(g, 2), huong=h) for g, h in GIAT])
    from multiprocessing import Pool
    jobs = []
    for k, (a, b) in enumerate(P3.DOAN):
        nk = max(1, round((b - a) / 15)); ranh = [round((a + (b - a) * j / nk) * FPS) / FPS for j in range(nk + 1)]
        jobs += [(bien, ranh[j], ranh[j + 1], k, os.path.join(TMP, f"{bien}_{k}_{j}.mp4")) for j in range(nk)]
    with Pool(4) as p: outs = p.map(khuc, jobs)
    lst = os.path.join(TMP, f"{bien}_ds.txt"); open(lst, "w").write("".join(f"file '{o}'\n" for o in outs))
    vid = os.path.join(TMP, f"{bien}_hinh.mp4"); ff("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid)
    wav = os.path.join(TMP, "am_M2_moi.wav"); f1080 = os.path.join(TMP, f"{bien}_1080p.mp4")
    ff("-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", f1080)
    out = os.path.join(XEM, f"{bien}.mp4")
    ff("-i", f1080, "-vf", "scale=960:540", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out)
    # bảng kiểu chuyển động: ghi cho mọi cảnh L1 trong đoạn (chạy ke_hoach một lượt ở tiến trình chính)
    for i, c in enumerate(D.CANH):
        if c["lop"] == "L1" and P3.t_ra(c["s"]) is not None: ke_hoach(i); NHAT_KY[c["ma"]]["s_ra"] = round(P3.t_ra(c["s"]), 2)
    info["canh"] = sorted(NHAT_KY.values(), key=lambda x: x.get("s_ra", 0)); info["giay_dung_1080p"] = round(time.time() - t0, 1)
    json.dump(info, open(os.path.join(REP, f"dung_{bien}.json"), "w"), indent=1, ensure_ascii=False); print(bien, "xong", info["giay_dung_1080p"], "s")


def xem():
    cu = os.path.join(XEM, "M2_cu.mp4"); shutil.copyfile(os.path.join(ROOT, "reports", "mrp3", "xem", "M2.mp4"), cu)
    moi = os.path.join(XEM, "M2_moi.mp4")
    fnt = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    lab = lambda s: f"drawtext=fontfile={fnt}:text='{s}':x=16:y=14:fontsize=26:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=8"
    ff("-i", cu, "-i", moi, "-filter_complex", f"[0:v]{lab('M2 cu (MR-P3)')}[a];[1:v]{lab('M2 moi (MR-P4)')}[b];[a][b]hstack=inputs=2[v]",
       "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
       os.path.join(XEM, "ghep_cu_moi.mp4"))
    LOA = "highpass=f=300:poles=2,lowpass=f=8000:poles=2,pan=mono|c0=0.5*c0+0.5*c1"
    r = {}
    for b in ("M2_cu", "M2_moi"):
        src = os.path.join(XEM, f"{b}.mp4"); dst = os.path.join(XEM, f"{b}_loa.mp4")
        ff("-i", src, "-c:v", "copy", "-af", LOA, "-c:a", "aac", "-b:a", "96k", "-ac", "1", "-movflags", "+faststart", dst)
        r[b] = do_ebur(src); r[b + "_loa"] = do_ebur(dst)
    # nghe so liền mạch: 4 đoạn 12 s, cũ → mới, bản loa điện thoại
    ds = [(0, 12), (12, 24), (90, 102), (102, 114)]; fl = []; ins = []
    for n, (a, b) in enumerate(ds):
        for j, s in enumerate(("M2_cu_loa", "M2_moi_loa")):
            ins += ["-ss", str(a), "-t", str(b - a), "-i", os.path.join(XEM, f"{s}.mp4")]
            m = 2 * n + j; tag = "CU" if j == 0 else "MOI"
            fl.append(f"[{m}:v]scale=960:540,{lab(f'{tag} - loa dien thoai - {a}-{b} s')},setsar=1[v{m}];[{m}:a]aformat=channel_layouts=mono,afade=t=in:d=0.05,afade=t=out:st={b - a - 0.1}:d=0.1[a{m}]")
    fl.append("".join(f"[v{m}][a{m}]" for m in range(2 * len(ds))) + f"concat=n={2 * len(ds)}:v=1:a=1[v][a]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "25", "-c:a", "aac", "-b:a", "96k",
       "-movflags", "+faststart", os.path.join(XEM, "nghe_so_loa.mp4"))
    j = json.load(open(os.path.join(REP, "am_do.json"))); j["tep_xem"] = r
    json.dump(j, open(os.path.join(REP, "am_do.json"), "w"), indent=1, ensure_ascii=False); print(json.dumps(r, indent=1))


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "am": am()
    elif m == "xem": xem()
    else: dung_hinh(m)
