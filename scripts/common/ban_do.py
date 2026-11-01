# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/common/ban_do.py (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa)
"""[K-MỚI · BD-1] ĐOẠN BẢN ĐỒ "NƠI NÀY Ở ĐÂU" — clip 1080p 24p, 10 s, không âm. 0 USD API.
Vào (lab/bd1/dia_diem.json): toạ độ địa điểm + 1 thành phố mốc (Natural Earth populated places) + bản đồ cổ (1 hoặc 2) có điểm khống chế.
  0–2,9 s  bản đồ hiện đại: Natural Earth 1:10m (PD) + bóng địa hình Copernicus DEM GLO-30; phóng châu lục → nước; ghim + tên nước + thành phố mốc + khoảng cách.
  2,9–7,2 s hoà sang bản đồ cổ cùng vùng; ghim CHỈ trên địa danh có ghi trên tờ (toạ độ điểm ảnh ghi trong dia_diem.json, kiểm bằng điểm khống chế).
  6,6–10 s về bản đồ hiện đại, phóng vào vùng, ghim nổi bật (vòng toả).
Màu: bảng màu kênh (scripts/m2c/do_hoa.py) + look A (lab/mau/look-A.json, k 0,6, nguồn đo GỘP trên khung hiện đại của clip) áp TRƯỚC chữ;
bản đồ cổ = tư liệu thật → k = 0. Chữ Cinzel/Cormorant (khuôn tấm chữ scripts/h3/ghep_h3.tam_chu, chép lại để khỏi kéo hang_h3), ≤ 6 từ/dòng (kiểm máy).
Dòng ghi nguồn nhỏ góc dưới phải. Không dùng Google/Apple Maps.
  LP_PHIEN=bd1 python3 scripts/common/ban_do.py nguon                  # tải + cắt bản đồ cổ → lab/bd1/nguon (+ nguon.json SHA), tải NE (ghim commit, SHA)
  LP_PHIEN=bd1 python3 scripts/common/ban_do.py khong_che              # kiểm điểm khống chế (affine bỏ-một) → reports/bd1/do/khong_che.json
  LP_PHIEN=bd1 python3 scripts/common/ban_do.py dem <dd>               # khảm DEM GLO-30 (đọc overview COG qua HTTP) → $BD_CACHE/mos/<dd>_*.npz
  LP_PHIEN=bd1 python3 scripts/common/ban_do.py dung <dd> [--thu t1,t2]  # → lab/bd1/clip/<dd>.mp4 + reports/bd1/to/<dd>_0-5s.jpg
Phụ thuộc: opencv-python-headless, rasterio (GDAL trong wheel), pillow, numpy; ffmpeg."""
import argparse, hashlib, json, math, os, subprocess, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.environ.setdefault("LP_PHIEN", "bd1")
sys.path.insert(0, os.path.join(ROOT, "scripts", "m2c")); sys.path.insert(0, os.path.dirname(__file__))
import do_hoa as G
import mau_look as ML
CACHE = os.environ.get("BD_CACHE", os.path.expanduser("~/.cache/lp-bd1"))
CFG = json.load(open(os.path.join(ROOT, "lab/bd1/dia_diem.json")))
NGUON_DIR = os.path.join(ROOT, "lab/bd1/nguon"); CLIP_DIR = os.path.join(ROOT, "lab/bd1/clip")
REP = os.path.join(ROOT, "reports/bd1")
W, H, FPS, DUR = 1920, 1080, 24, 10.0
NF = int(DUR * FPS)
IV, BR, INK, STONE = G.IVORY, G.BRONZE, G.INK, G.STONE
UA = "LostPlacesLab-research/1.0 (BD-1 map segment; github HungQuach301/lost-places-lab)"

# ---------------------------------------------------------------- Natural Earth (PD) — ghim commit + SHA-256 (tải 01/11/2026)
NE_COMMIT = "ca96624a56bd078437bca8184e78163e5039ad19"
NE_SHA = {"ne_10m_land": "1ac90796408bc6ad6911d69448485d3c4dbf2190370080368a09976e1c9f7416",
          "ne_10m_admin_0_countries": "239eec57ac17f100a11e2536cffc56752c318b50ae765b0918ff7aab4ce8f255",
          "ne_10m_admin_0_boundary_lines_land": "74d9c16229c095fde65943a9919e337682f044bcebccb120764f38edf3b70f4a",
          "ne_10m_populated_places_simple": "fd3fa867a320cbd5c5b6bb5bc550afeec2939fb2cef688e508007282a55ac42f",
          "ne_10m_lakes": "2d036f53dedec578001c5c30c2959ee7d4eebc1306900fa4367c49929ec8f2d9",
          "ne_10m_rivers_lake_centerlines": "bb854a900ecbd3b408df46d5e16e3e0f974ba55993f9d8b5c26e855273c0905a"}

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def tai(url, ra, tg=600):
    os.makedirs(os.path.dirname(ra), exist_ok=True)
    rq = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(rq, timeout=tg) as r, open(ra + ".part", "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b: break
            f.write(b)
    os.replace(ra + ".part", ra); return ra

def ne(ten):
    p = os.path.join(CACHE, "ne", ten + ".geojson")
    if not os.path.exists(p): tai(f"https://raw.githubusercontent.com/nvkelso/natural-earth-vector/{NE_COMMIT}/geojson/{ten}.geojson", p)
    if sha(p) != NE_SHA[ten]: raise SystemExit(f"SHA Natural Earth lệch: {ten}")
    return json.load(open(p))

def thanh_pho(ten, nuoc):
    for f in ne("ne_10m_populated_places_simple")["features"]:
        p = f["properties"]
        if p["name"] == ten and p["adm0name"] == nuoc: return (p["latitude"], p["longitude"])
    raise SystemExit(f"không thấy thành phố {ten}/{nuoc} trong Natural Earth")

def khoang_cach(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    return 2 * 6371.0088 * math.asin(math.sqrt(math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))

def huong(tu, den):   # 8 hướng, từ thành phố mốc tới địa điểm (phương vị ban đầu)
    la1, lo1, la2, lo2 = map(math.radians, (tu[0], tu[1], den[0], den[1]))
    y = math.sin(lo2 - lo1) * math.cos(la2); x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(lo2 - lo1)
    b = (math.degrees(math.atan2(y, x)) + 360) % 360
    return ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][int((b + 22.5) // 45) % 8], b

# ---------------------------------------------------------------- bản đồ cổ: tải + cắt (tệp vào repo qua LFS, SHA trong nguon.json)
def nguon():
    os.makedirs(NGUON_DIR, exist_ok=True); tmp = os.path.join(CACHE, "goc"); os.makedirs(tmp, exist_ok=True); man = {}
    for t in NE_SHA: ne(t)
    man["natural_earth"] = {"commit": NE_COMMIT, "sha256": NE_SHA, "giay_phep": "public domain (LICENSE.md: 'All versions of Natural Earth raster + vector map data … are in the public domain.')"}
    for mid, m in CFG["ban_do_co"].items():
        urls = m["tai"] if isinstance(m["tai"], list) else [m["tai"]]
        goc = []
        for i, u in enumerate(urls):
            p = os.path.join(tmp, f"{mid}_{i}" + ".jpg")
            if not os.path.exists(p): tai(u, p); time.sleep(1)
            goc.append(p)
        if len(goc) == 2:   # tờ đôi Guaman Poma: ghép ngang, cắt cùng chiều cao
            a, b = cv2.imread(goc[0]), cv2.imread(goc[1]); h = min(a.shape[0], b.shape[0]); im = np.hstack([a[:h], b[:h]])
        else: im = cv2.imread(goc[0])
        x0, y0, x1, y1 = m["cat"]; c = im[y0:y1, x0:x1]
        ra = os.path.join(NGUON_DIR, f"{mid}.jpg"); cv2.imwrite(ra, c, [cv2.IMWRITE_JPEG_QUALITY, 95])
        man[mid] = {"tai": urls, "muc": m["muc"], "sha256_goc": [sha(p) for p in goc], "kich_thuoc_to": [int(im.shape[1]), int(im.shape[0])],
                    "cat": m["cat"], "tep": os.path.relpath(ra, ROOT), "sha256_tep": sha(ra), "ngay_tai": time.strftime("%Y-%m-%d")}
        print(mid, im.shape, "→", ra, flush=True)
    json.dump(man, open(os.path.join(NGUON_DIR, "nguon.json"), "w"), ensure_ascii=False, indent=1)

def anh_co(mid):
    p = os.path.join(NGUON_DIR, f"{mid}.jpg")
    if not os.path.exists(p): nguon()
    return cv2.imread(p)

# ---------------------------------------------------------------- kiểm điểm khống chế: affine bỏ-một (dự đoán px của mỗi điểm từ các điểm còn lại)
def khong_che():
    out = {}
    for mid, m in CFG["ban_do_co"].items():
        D = {k: v for k, v in m["diem"].items() if v.get("ll")}
        if len(D) < 4: out[mid] = {"ghi_chu": m.get("khong_dang_ky") or f"chỉ {len(D)} điểm có toạ độ — không đủ kiểm bỏ-một (cần ≥ 4)", "diem": m["diem"]}; continue
        ks = list(D); lat0 = np.mean([D[k]["ll"][0] for k in ks]); kx = math.cos(math.radians(lat0))
        X = np.array([[D[k]["ll"][1] * kx, D[k]["ll"][0], 1.0] for k in ks]); P = np.array([D[k]["px"] for k in ks], float)
        A, *_ = np.linalg.lstsq(X, P, rcond=None); res_all = np.linalg.norm(X @ A - P, axis=1)
        loo = {}
        for i, k in enumerate(ks):
            m_ = np.arange(len(ks)) != i; Ai, *_ = np.linalg.lstsq(X[m_], P[m_], rcond=None); e = X[i] @ Ai - P[i]
            loo[k] = {"ghi_tren_to": D[k]["ghi"], "px": D[k]["px"], "du_doan_bo_mot": [round(float(v), 1) for v in X[i] @ Ai], "sai_px": round(float(np.hypot(*e)), 1),
                      "sai_km_tuong_duong": None}
        # đổi sai số px → km bằng thang trung bình của affine
        sc = math.sqrt(abs(np.linalg.det(A[:2, :2]))) / 111.2   # px trên km
        for k in loo: loo[k]["sai_km_tuong_duong"] = round(loo[k]["sai_px"] / sc, 1)
        out[mid] = {"so_diem": len(ks), "thang_px_moi_km": round(sc, 3), "sai_trung_vi_bo_mot_px": round(float(np.median([v["sai_px"] for v in loo.values()])), 1),
                    "sai_khop_tat_ca_px": [round(float(v), 1) for v in res_all], "bo_mot": loo,
                    "ghi_chu": "affine (kinh·cos φ, vĩ) → px trên tờ gốc; sai số lớn = bản đồ cổ méo (Tabula nén Bắc–Nam) hoặc đặt nhầm điểm."}
    os.makedirs(os.path.join(REP, "do"), exist_ok=True)
    json.dump(out, open(os.path.join(REP, "do/khong_che.json"), "w"), ensure_ascii=False, indent=1)
    for mid, v in out.items(): print(mid, v.get("sai_trung_vi_bo_mot_px"), {k: x["sai_px"] for k, x in v.get("bo_mot", {}).items()})

# ---------------------------------------------------------------- DEM Copernicus GLO-30 (AWS Open Data), đọc overview COG qua HTTP
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{n}/{n}.tif"
def ten_o(la, lo):
    return f"Copernicus_DSM_COG_10_{'N' if la >= 0 else 'S'}{abs(la):02d}_00_{'E' if lo >= 0 else 'W'}{abs(lo):03d}_00_DEM"
_TL = None
def co_o(n):
    global _TL
    if _TL is None:
        p = os.path.join(CACHE, "tileList.txt")
        if not os.path.exists(p): tai("https://copernicus-dem-30m.s3.amazonaws.com/tileList.txt", p)
        _TL = set(open(p).read().split())
    return n in _TL

def doc_o(la, lo, n):
    ten = ten_o(la, lo); p = os.path.join(CACHE, "dem", str(n), ten + ".npy")
    if os.path.exists(p): return np.load(p)
    if not co_o(ten): return None
    import rasterio
    from rasterio.enums import Resampling
    for lan in range(4):
        try:
            with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", GDAL_HTTP_USERAGENT=UA, GDAL_HTTP_MAX_RETRY="3"):
                with rasterio.open(DEM_URL.format(n=ten)) as f:
                    a = f.read(1, out_shape=(n, n), resampling=Resampling.average).astype(np.float32)
            break
        except Exception as e:
            if lan == 3: raise
            time.sleep(2 ** (lan + 1))
    os.makedirs(os.path.dirname(p), exist_ok=True); np.save(p, a.astype(np.float16) if n <= 450 else a); return a

def khung_bbox(k, latref):
    lon, lat, h = k; dpp = h / H; w = dpp * W / math.cos(math.radians(latref))
    return lon - w / 2, lon + w / 2, lat - h / 2, lat + h / 2, dpp

def kham(bb, n):
    lo0, lo1, la0, la1 = int(math.floor(bb[0])), int(math.ceil(bb[1])), int(math.floor(bb[2])), int(math.ceil(bb[3]))
    z = np.zeros(((la1 - la0) * n, (lo1 - lo0) * n), np.float32)
    o = [(la, lo) for la in range(la0, la1) for lo in range(lo0, lo1) if co_o(ten_o(la, lo))]
    t0 = time.time()
    with ThreadPoolExecutor(24 if n <= 450 else 8) as ex:
        for (la, lo), a in zip(o, ex.map(lambda q: doc_o(q[0], q[1], n), o)):
            if a is None: continue
            r = (la1 - la - 1) * n; c = (lo - lo0) * n; z[r:r + n, c:c + n] = a
    print(f"  khảm n={n} {lo0}..{lo1} × {la0}..{la1}: {len(o)} ô, {time.time() - t0:.0f} s", flush=True)
    return z, (lo0, la1, n)

def bong(z, gt, ve):
    """hillshade (phương vị 315°, cao 45°) — ô lưới theo mét tại từng vĩ độ."""
    lo0, la1, n = gt; rows = z.shape[0]; lat = la1 - (np.arange(rows) + 0.5) / n
    dy = 110950.0 / n; dx = (111320.0 * np.cos(np.radians(lat)) / n)[:, None]
    gy, gx = np.gradient(z * ve); gx = gx / dx; gy = -gy / dy
    az, alt = math.radians(315), math.radians(45)
    sl = np.arctan(np.hypot(gx, gy)); asp = np.arctan2(-gx, gy)
    hs = np.sin(alt) * np.cos(sl) + np.cos(alt) * np.sin(sl) * np.cos(az - asp)
    return np.clip(hs, 0, 1).astype(np.float32)

LOW, HIGH, SNOW = np.array([104, 132, 162], np.float32), np.array([150, 176, 200], np.float32), np.array([214, 224, 230], np.float32)   # BGR: đất thấp, cao, rất cao (look A ấm)
def mau_dia_hinh(z, hs):
    t = np.clip(z / 3500.0, 0, 1)[..., None]; s = np.clip((z - 4300) / 1200.0, 0, 1)[..., None]
    base = LOW * (1 - t) + HIGH * t; base = base * (1 - s) + SNOW * s
    shade = 0.35 + 0.9 * hs[..., None]          # mặt phẳng (hs = sin 45°) ≈ 0,99
    return np.clip(base * shade, 0, 255).astype(np.uint8)

def dem(dd):
    s = CFG["dia_diem"][dd]; latref = s["toa_do"][0]; K = s["khung"]; os.makedirs(os.path.join(CACHE, "mos"), exist_ok=True)
    bb0 = khung_bbox(K["chau_luc"], latref); bbn = khung_bbox(K["nuoc"], latref); bbc = khung_bbox(K["cuoi"], latref)
    lv = [("L1", 60, bb0, 3.0)]
    need_n = 1 / bbn[4]
    if 60 < 0.85 * need_n:   # khung nước cần mịn hơn 60 điểm/độ → L2 phủ cả khung nước và khung cuối
        lv.append(("L2", 450, (min(bbn[0], bbc[0]), max(bbn[1], bbc[1]), min(bbn[2], bbc[2]), max(bbn[3], bbc[3])), 1.6))
    nc = 1 / bbc[4]
    if not any(l[0] == "L2" for l in lv) and nc > 60 / 0.85: lv.append(("L2", 450, bbc[:4], 1.6))
    if nc > 450 / 0.85:
        n3 = 900 if nc <= 900 / 0.85 else (1800 if nc <= 1800 / 0.85 else 3600)
        lv.append(("L3", n3, bbc[:4], 1.4))
    for ten, n, bb, ve in lv:
        p = os.path.join(CACHE, "mos", f"{dd}_{ten}.npz")
        if os.path.exists(p): continue
        z, gt = kham(bb, n); hs = bong(z, gt, ve)
        dat = (((z > 0.5) | (z < -1.0)) * 255).astype(np.uint8)   # đất theo DEM (biển = 0 / không có ô); trũng dưới mực biển (Jordan, Biển Chết) vẫn là đất, hồ vẽ lại từ NE
        img = np.dstack([mau_dia_hinh(z, hs), dat])
        np.savez(p, img=img, gt=np.array(gt, np.float64))
        print(" ", ten, img.shape, "→", p, flush=True)

class Kham:
    """kim tự tháp ảnh bóng địa hình theo mức; chọn mức thô nhất đủ mịn cho khung, nội suy giữa hai tầng liền kề (khỏi 'nhảy' độ nét)."""
    def __init__(s, dd):
        s.T = []
        for ten in ("L1", "L2", "L3"):
            p = os.path.join(CACHE, "mos", f"{dd}_{ten}.npz")
            if not os.path.exists(p): continue
            a = np.load(p); img = a["img"]; lo0, la1, n = a["gt"]; lo0, la1, n = float(lo0), float(la1), float(n)
            lo1 = lo0 + img.shape[1] / n; la0 = la1 - img.shape[0] / n
            while True:
                s.T.append((n, img, lo0, la1, (lo0, lo1, la0, la1)))
                if img.shape[0] < 400 or n <= 16: break
                img = cv2.pyrDown(img); n = n / 2
        s.T.sort(key=lambda t: t[0])
    def lay(s, lon, lat, bb, dpp):
        need = 1.0 / dpp
        cand = [t for t in s.T if t[4][0] <= bb[0] + 1e-6 and t[4][1] >= bb[1] - 1e-6 and t[4][2] <= bb[2] + 1e-6 and t[4][3] >= bb[3] - 1e-6] or s.T[:1]
        a = next((t for t in cand if t[0] >= need), cand[-1]); b = [t for t in cand if t[0] < a[0]]
        out = s._mau(a, lon, lat)
        if b and a[0] >= need:
            b = b[-1]; u = float(np.clip(math.log2(a[0] / need) / math.log2(a[0] / b[0]), 0, 1))
            if u > 0.01: out = cv2.addWeighted(out, 1 - u, s._mau(b, lon, lat), u, 0)
        return out
    def _mau(s, t, lon, lat):
        n, img, lo0, la1, _ = t
        return cv2.remap(img, ((lon - lo0) * n - 0.5).astype(np.float32), ((la1 - lat) * n - 0.5).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

# ---------------------------------------------------------------- vector Natural Earth trong vùng clip
def _vong(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"]]
    if geom["type"] == "MultiPolygon": return geom["coordinates"]
    return []
def _duong(geom):
    if geom["type"] == "LineString": return [geom["coordinates"]]
    if geom["type"] == "MultiLineString": return geom["coordinates"]
    return []
def _cat(rings, bb, m=2.0):
    out = []
    for r in rings:
        a = np.asarray(r, np.float64)
        if a[:, 0].max() < bb[0] - m or a[:, 0].min() > bb[1] + m or a[:, 1].max() < bb[2] - m or a[:, 1].min() > bb[3] + m: continue
        out.append(a)
    return out

class Vector:
    def __init__(s, bb, iso):
        s.land, s.hole = [], []
        for f in ne("ne_10m_land")["features"]:
            for poly in _vong(f["geometry"]):
                ex = _cat([poly[0]], bb)
                if ex: s.land += ex; s.hole += _cat(poly[1:], bb)
        s.nuoc, s.khac = [], []
        for f in ne("ne_10m_admin_0_countries")["features"]:
            if f["properties"]["ADM0_A3"] == iso:
                for poly in _vong(f["geometry"]): s.nuoc += _cat([poly[0]], bb)
        s.bien = []
        for f in ne("ne_10m_admin_0_boundary_lines_land")["features"]:
            for l in _duong(f["geometry"]): s.bien += _cat([l], bb)
        s.ho = []
        for f in ne("ne_10m_lakes")["features"]:
            if (f["properties"].get("scalerank") or 9) <= 6:
                for poly in _vong(f["geometry"]): s.ho += _cat([poly[0]], bb)
        s.song = []
        for f in ne("ne_10m_rivers_lake_centerlines")["features"]:
            sr = f["properties"].get("scalerank") or 9
            if sr <= 7:
                for l in _duong(f["geometry"]): s.song += [(sr, a) for a in _cat([l], bb)]

SEA = np.array([62, 50, 36], np.float32)      # BGR: mực xanh xám đậm (biển)
LAKE = (92, 78, 58); RIVER = (110, 96, 72)

class May:
    """phép chiếu đẳng chữ nhật cục bộ: x = (kinh − kinh tâm)·cos φ_ref / dpp; φ_ref = vĩ độ địa điểm, cố định cả clip (phóng = co giãn thuần)."""
    def __init__(s, lon, lat, h, latref):
        s.lon, s.lat, s.dpp, s.k = lon, lat, h / H, math.cos(math.radians(latref))
    def px(s, lon, lat):
        return (W / 2 + (np.asarray(lon) - s.lon) * s.k / s.dpp, H / 2 - (np.asarray(lat) - s.lat) / s.dpp)
    def bb(s):
        w = s.dpp * W / s.k; return (s.lon - w / 2, s.lon + w / 2, s.lat - H * s.dpp / 2, s.lat + H * s.dpp / 2)
    def luoi(s):
        xs = (np.arange(W) + 0.5 - W / 2) * s.dpp / s.k + s.lon; ys = s.lat - (np.arange(H) + 0.5 - H / 2) * s.dpp
        return np.broadcast_to(xs[None, :], (H, W)), np.broadcast_to(ys[:, None], (H, W))

SH = 4; SC = float(1 << SH)
def _pts(m, a):
    x, y = m.px(a[:, 0], a[:, 1]); p = np.stack([x, y], 1)
    p = np.clip(p, -4000, 6000)
    return (p * SC).round().astype(np.int32)

def ve_hien_dai(m, V, KH):
    lon, lat = m.luoi(); bb = m.bb()
    r4 = KH.lay(lon, lat, bb, m.dpp); rel = r4[..., :3].astype(np.float32)
    land = np.zeros((H, W), np.uint8)
    if V.land: cv2.fillPoly(land, [_pts(m, a) for a in V.land], 255, cv2.LINE_AA, SH)
    if V.hole: cv2.fillPoly(land, [_pts(m, a) for a in V.hole], 0, cv2.LINE_AA, SH)
    # thang vùng (dpp < 0,003°): bờ NE 1:10m quá thô → chuyển dần sang mặt nạ đất từ DEM GLO-30
    wd = float(np.clip((0.003 - m.dpp) / 0.0015, 0, 1))
    if wd > 0:   # vùng trũng sát bờ (z ≤ 0,5 m) không bị coi là biển: trong lõi đất NE (co 41 px) luôn là đất
        dem_land = np.maximum(r4[..., 3], cv2.erode(land, np.ones((41, 41), np.uint8)))
        land = cv2.addWeighted(land, 1 - wd, dem_land, wd, 0)
    ctry = np.zeros((H, W), np.uint8)
    if V.nuoc: cv2.fillPoly(ctry, [_pts(m, a) for a in V.nuoc], 255, cv2.LINE_AA, SH)
    if wd > 0: ctry = np.maximum(ctry, (cv2.dilate(ctry, np.ones((41, 41), np.uint8)) * (land > 0) * wd).astype(np.uint8))   # bờ DEM nằm ngoài đa giác NE
    a = land.astype(np.float32)[..., None] / 255; c = ctry.astype(np.float32)[..., None] / 255
    gray = rel.mean(2, keepdims=True)
    other = (rel * 0.35 + gray * 0.65) * 0.74              # nước khác: bớt màu, tối hơn (nước đích nổi bằng độ sáng, không bằng sắc)
    landc = other * (1 - c) + rel * c
    # biển: đậm dần ra xa bờ (mờ mặt nạ đất)
    far = cv2.GaussianBlur(land, (0, 0), 18).astype(np.float32)[..., None] / 255
    sea = SEA * (0.85 + 0.25 * far)
    fr = sea * (1 - a) + landc * a
    fr = np.clip(fr, 0, 255).astype(np.uint8)
    if V.ho: cv2.fillPoly(fr, [_pts(m, x) for x in V.ho], LAKE, cv2.LINE_AA, SH)
    # sông NE 1:10m chỉ ở thang châu lục/nước: ở thang vùng (dpp < 0,006°) đường sông khái quát lệch khỏi thung lũng DEM → tắt dần
    a_s = float(np.clip((m.dpp - 0.004) / 0.004, 0, 1))
    if a_s > 0:
        lim = 4 if m.dpp > 0.03 else 6; ov = fr.copy()
        for sr, x in V.song:
            if sr <= lim: cv2.polylines(ov, [_pts(m, x)], False, RIVER, 1 if sr > 4 or m.dpp > 0.02 else 2, cv2.LINE_AA, SH)
        fr = cv2.addWeighted(ov, a_s, fr, 1 - a_s, 0)
    # đường bờ (mực, mảnh) + biên giới (đồng, mảnh); viền đậm cho nước đích
    ov = fr.copy()
    if V.land: cv2.polylines(ov, [_pts(m, x) for x in V.land], True, (40, 34, 28), 2, cv2.LINE_AA, SH)
    if V.bien: cv2.polylines(ov, [_pts(m, x) for x in V.bien], False, STONE[::-1], 2, cv2.LINE_AA, SH)
    fr = cv2.addWeighted(ov, 0.6 * (1 - wd), fr, 1 - 0.6 * (1 - wd), 0)
    if V.nuoc:
        ov = fr.copy(); cv2.polylines(ov, [_pts(m, x) for x in V.nuoc], True, BR[::-1], 3, cv2.LINE_AA, SH)
        fr = cv2.addWeighted(ov, 1 - wd, fr, wd, 0) if wd > 0 else ov
    return fr

# ---------------------------------------------------------------- chữ (khuôn ghep_h3.tam_chu, ngà/đồng/mực, Cinzel/Cormorant) + ghim
def so_tu(t):
    return len([w for w in t.replace("·", " ").split() if w.strip("“”\"'.,")])

_C = {}
def tam_chu(dong, plate_a=215, pad=(22, 14), icon=None):
    """như scripts/h3/ghep_h3.tam_chu (không sửa tệp đó): dòng [(text, kind, size, weight, color)] trên tấm mực bo góc → RGBA."""
    for d in dong:
        if so_tu(d[0]) > 6: raise SystemExit(f"dòng chữ > 6 từ: {d[0]!r}")
    key = (tuple(dong), plate_a, pad, icon)
    if key in _C: return _C[key]
    fs = [G.font(k, sz, wt) for (_, k, sz, wt, _) in dong]; d0 = ImageDraw.Draw(Image.new("L", (1, 1)))
    bbs = [d0.textbbox((0, 0), t, font=f, anchor="ls") for (t, *_), f in zip(dong, fs)]
    ic = icon[1] + 12 if icon else 0
    wmax = max(b[2] - b[0] + (ic if i == len(dong) - 1 else 0) for i, b in enumerate(bbs)); gap = 14
    hs = [max(b[3] - b[1], int(sz * 0.72)) for b, (_, _, sz, _, _) in zip(bbs, dong)]
    Wt, Ht = wmax + 2 * pad[0], sum(hs) + gap * (len(dong) - 1) + 2 * pad[1]
    im = Image.new("RGBA", (Wt + 24, Ht + 24), (0, 0, 0, 0)); o = 12
    ImageDraw.Draw(im).rounded_rectangle([o, o, o + Wt, o + Ht], 10, fill=INK + (plate_a,))
    y = o + pad[1]; layers = []
    for i, ((t, k, sz, wt, col), f, b, hh) in enumerate(zip(dong, fs, bbs, hs)):
        x = o + pad[0] + (ic if (icon and i == len(dong) - 1) else 0)
        mm = Image.new("L", im.size, 0); ImageDraw.Draw(mm).text((x - b[0], y - b[1]), t, font=f, fill=255, anchor="ls"); layers.append((mm, col))
        if icon and i == len(dong) - 1:
            ti = Image.fromarray(G.tier_icon(icon[1], icon[0])); im.alpha_composite(ti, (o + pad[0], int(y + hh / 2 - icon[1] / 2)))
        y += hh + gap
    for mm, col in layers:
        tx = Image.new("RGBA", im.size, tuple(col) + (0,)); tx.putalpha(mm); im = Image.alpha_composite(im, tx)
    r = np.array(im); _C[key] = r; return r

def chu_quang(text, kind, size, weight, col, track=0):
    """chữ có quầng mực mềm, không tấm (nhãn trên bản đồ) → RGBA."""
    if so_tu(text) > 6: raise SystemExit(f"dòng chữ > 6 từ: {text!r}")
    key = ("q", text, kind, size, weight, col, track)
    if key in _C: return _C[key]
    if track: text = (" " * track).join(text)
    f = G.font(kind, size, weight); d0 = ImageDraw.Draw(Image.new("L", (1, 1))); b = d0.textbbox((0, 0), text, font=f, anchor="lt")
    pad = size // 2 + 6; w, h = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).text((pad - b[0], pad - b[1]), text, font=f, fill=255, anchor="lt")
    halo = m.filter(ImageFilter.MaxFilter(max(3, (size // 9) | 1))).filter(ImageFilter.GaussianBlur(max(2, size / 8)))
    im = Image.new("RGBA", (w, h), INK + (0,)); im.putalpha(halo.point(lambda v: min(255, int(v * 0.9))))
    tx = Image.new("RGBA", (w, h), tuple(col) + (0,)); tx.putalpha(m); im = Image.alpha_composite(im, tx)
    r = np.array(im); _C[key] = r; return r

def dan(fr, rgba, x, y, alpha=1.0):
    x, y = int(round(x)), int(round(y)); h, w = rgba.shape[:2]; x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + w), min(H, y + h)
    if x1 <= x0 or y1 <= y0 or alpha <= 0: return
    sub = rgba[y0 - y:y1 - y, x0 - x:x1 - x]; a = sub[..., 3:4].astype(np.float32) / 255 * alpha
    reg = fr[y0:y1, x0:x1].astype(np.float32); fr[y0:y1, x0:x1] = (reg * (1 - a) + sub[..., 2::-1].astype(np.float32) * a).astype(np.uint8)

def mo(t, a, b, f=0.35):
    if t < a or t >= b: return 0.0
    return float(min(1.0, (t - a) / f, (b - t) / f))

def ez(u): u = min(1.0, max(0.0, u)); return u * u * (3 - 2 * u)

_GHIM = None
def ghim_sprite():
    """ghim giọt nước đồng, lõi ngà, viền mực, bóng đổ — vẽ 4× rồi thu nhỏ. Trả (rgba, (dx, dy) của mũi ghim)."""
    global _GHIM
    if _GHIM is not None: return _GHIM
    s = 4; w, h = 56 * s, 76 * s; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx, cy, r = w // 2, 24 * s, 17 * s; tip = (cx, 66 * s)
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([cx - 9 * s, tip[1] - 3 * s, cx + 9 * s, tip[1] + 4 * s], fill=INK + (150,))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(3 * s))); d = ImageDraw.Draw(im)
    d.polygon([(cx - r * 0.82, cy + r * 0.55), (cx + r * 0.82, cy + r * 0.55), tip], fill=INK + (255,))
    d.ellipse([cx - r - 2 * s, cy - r - 2 * s, cx + r + 2 * s, cy + r + 2 * s], fill=INK + (255,))
    d.polygon([(cx - r * 0.72, cy + r * 0.5), (cx + r * 0.72, cy + r * 0.5), (tip[0], tip[1] - 3 * s)], fill=BR + (255,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BR + (255,))
    d.ellipse([cx - r * 0.42, cy - r * 0.42, cx + r * 0.42, cy + r * 0.42], fill=IV + (255,))
    im = im.resize((w // s, h // s), Image.LANCZOS)
    _GHIM = (np.array(im), (w // s // 2, 66)); return _GHIM

def ve_ghim(fr, x, y, a=1.0, roi=0.0):
    sp, (dx, dy) = ghim_sprite(); dan(fr, sp, x - dx, y - dy - roi, a)

def ve_cham(fr, x, y, a=1.0):
    ov = fr.copy(); cv2.circle(ov, (int(x * 16), int(y * 16)), 9 * 16, INK[::-1], -1, cv2.LINE_AA, 4)
    cv2.circle(ov, (int(x * 16), int(y * 16)), 6 * 16, IV[::-1], -1, cv2.LINE_AA, 4); fr[:] = cv2.addWeighted(ov, a, fr, 1 - a, 0)

def ve_vong(fr, x, y, dt):
    """3 vòng đồng toả từ ghim, lặp mỗi 1,65 s (dt = giây kể từ lúc bắt đầu)."""
    ov = fr.copy(); ok = False
    for k in range(3):
        if dt < k * 0.55: continue
        u = ((dt - k * 0.55) % 1.65) / 1.6
        if 0 <= u <= 1:
            r = 14 + 110 * ez(u); a = (1 - u) ** 1.5; ok = True
            o2 = ov.copy(); cv2.circle(o2, (int(x * 16), int(y * 16)), int(r * 16), INK[::-1], 9, cv2.LINE_AA, 4)
            cv2.circle(o2, (int(x * 16), int(y * 16)), int(r * 16), IV[::-1], 5, cv2.LINE_AA, 4); ov = cv2.addWeighted(o2, a * 0.9, ov, 1 - a * 0.9, 0)
    if ok: fr[:] = ov

def ve_net_dut(fr, p0, p1, u=1.0, a=1.0):
    """đường nét đứt ngà (viền mực) từ p0 tới p0 + u·(p1 − p0)."""
    p0 = np.array(p0, float); p1 = np.array(p1, float); L = np.linalg.norm(p1 - p0)
    if L < 4 or u <= 0: return
    d = (p1 - p0) / L; ov = fr.copy(); s = 0.0
    while s < L * u:
        e = min(s + 12, L * u); q0 = p0 + d * s; q1 = p0 + d * e
        cv2.line(ov, tuple((q0 * 16).astype(int)), tuple((q1 * 16).astype(int)), INK[::-1], 6, cv2.LINE_AA, 4)
        cv2.line(ov, tuple((q0 * 16).astype(int)), tuple((q1 * 16).astype(int)), IV[::-1], 3, cv2.LINE_AA, 4); s += 20
    fr[:] = cv2.addWeighted(ov, a, fr, 1 - a, 0)

# ---------------------------------------------------------------- dòng thời gian
def lich(nmap):
    """→ (pha hình theo t): danh sách (t0, t1, nguồn) + mốc hoà. Hiện đại 0–2,9; hoà 2,9–3,5; (2 tờ: tờ 1 tới 4,95, hoà 4,95–5,45); hoà ra 6,6–7,2."""
    if nmap == 1: return [(2.9, 3.5, 6.6, 7.2)]
    return [(2.9, 3.5, 4.95, 5.45), (4.95, 5.45, 6.6, 7.2)]

def _len(t, a, b): return min(1.0, max(0.0, (t - a) / (b - a)))
def trong_so(t, L):
    """→ [(nguồn, trọng số)], tổng = 1; nguồn 'hd' (hiện đại) hoặc chỉ số tờ cổ. Tờ sau hoà ĐÈ lên tờ trước; tờ cuối hoà ra về hiện đại."""
    if len(L) == 1:
        a0, a1, b0, b1 = L[0]; w = _len(t, a0, a1) * (1 - _len(t, b0, b1)); out = [(0, w)]
    else:
        (a0, a1, _, _), (c0, c1, b0, b1) = L
        w1 = _len(t, c0, c1) * (1 - _len(t, b0, b1)); w0 = _len(t, a0, a1) * (1 - _len(t, c0, c1)); out = [(0, w0), (1, w1)]
    s = sum(w for _, w in out)
    return [(i, w) for i, w in out if w > 1e-4] + ([("hd", 1 - s)] if s < 0.9999 else [])

def may_tai(t, s):
    K = s["khung"]; latref = s["toa_do"][0]
    def lerp_k(A, B, u):
        hA, hB = A[2], B[2]; h = math.exp(math.log(hA) + (math.log(hB) - math.log(hA)) * u)
        w = (hA - h) / (hA - hB) if abs(hA - hB) > 1e-9 else u
        return (A[0] + (B[0] - A[0]) * w, A[1] + (B[1] - A[1]) * w, h)
    if t < 2.9: k = lerp_k(K["chau_luc"], K["nuoc"], ez(t / 2.9))
    elif t < 7.0:
        u = (t - 2.9) / 4.1; k = (K["nuoc"][0], K["nuoc"][1], K["nuoc"][2] * (1 - 0.03 * u))
    elif t < 9.3: k = lerp_k((K["nuoc"][0], K["nuoc"][1], K["nuoc"][2] * 0.97), K["cuoi"], ez((t - 7.0) / 2.3))
    else: k = (K["cuoi"][0], K["cuoi"][1], K["cuoi"][2] * (1 - 0.025 * (t - 9.3) / 0.7))
    return May(k[0], k[1], k[2], latref)

# ---------------------------------------------------------------- bản đồ cổ trên màn hình
class ToCo:
    def __init__(s, mid, ghim_id, neo_man, nhan="phai"):
        s.nhan = nhan
        s.id = mid; s.M = CFG["ban_do_co"][mid]; s.im = anh_co(mid); x0, y0 = s.M["cat"][:2]
        g = s.M["diem"][ghim_id]; s.g = g; s.neo = (g["px"][0] - x0, g["px"][1] - y0)   # điểm ảnh ghim trong ảnh đã cắt
        s.s0 = max(s.M["ty_le"], W / s.im.shape[1], H / s.im.shape[0]) * 1.001
        s.neo_man = neo_man
    def bien(s, u):
        """ma trận ảnh cắt → màn hình: tỉ lệ s0·(1 + 0,06u), neo ghim tại neo_man (giới hạn để tờ phủ kín khung)."""
        sc = s.s0 * (1 + 0.06 * u); h, w = s.im.shape[:2]
        tx = s.neo_man[0] - s.neo[0] * sc; ty = s.neo_man[1] - s.neo[1] * sc
        tx = min(0.0, max(W - w * sc, tx)); ty = min(0.0, max(H - h * sc, ty))
        return np.float32([[sc, 0, tx], [0, sc, ty]])
    def khung(s, u):
        M = s.bien(u); fr = cv2.warpAffine(s.im, M, (W, H), flags=cv2.INTER_AREA if M[0, 0] < 1 else cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        x = M[0, 0] * s.neo[0] + M[0, 2]; y = M[1, 1] * s.neo[1] + M[1, 2]; return fr, (x, y)

# ---------------------------------------------------------------- dựng
def dung(dd, thu=None):
    s = CFG["dia_diem"][dd]; latref = s["toa_do"][0]; site = tuple(s["toa_do"])
    city = thanh_pho(s["thanh_pho"]["ne"][0], s["thanh_pho"]["ne"][1])
    km = khoang_cach(city, site); hg, bear = huong(city, site)
    km_txt = f"{km:.0f} km" if km >= 10 else f"{km:.1f} km"
    dong_kc = f"{km_txt} {hg} of {s['thanh_pho']['ten']}"
    KH = Kham(dd)
    if not KH.T: raise SystemExit("chưa có khảm DEM — chạy: ban_do.py dem " + dd)
    bb0 = khung_bbox(s["khung"]["chau_luc"], latref); V = Vector(bb0[:4], s["nuoc_ne"])
    L = lich(len(s["ban_do_co"]))
    # neo màn hình của ghim cổ = vị trí địa danh đó trên bản đồ hiện đại lúc 2,9 s (để hoà "cùng vùng")
    m29 = may_tai(2.9, s); TO = []
    for b in s["ban_do_co"]:
        g = CFG["ban_do_co"][b["id"]]["diem"][b["ghim"]]; ll = g.get("ll") or g["ll_hien_dai"]   # địa danh ĐƯỢC GHI trên tờ, đặt neo ở vị trí thật của nó
        x, y = m29.px(ll[1], ll[0]); TO.append(ToCo(b["id"], b["ghim"], (float(x), float(y)), b.get("nhan", "phai")))
    # ---- look A: nguồn đo GỘP trên khung hiện đại (trước chữ)
    os.makedirs(os.path.join(REP, "do"), exist_ok=True); lf = os.path.join(REP, "do", f"look_{dd}.json")
    if os.path.exists(lf) and not thu: lk = json.load(open(lf)); LM, LS = np.array(lk["mean"], np.float32), np.array(lk["std"], np.float32)
    else:
        P = []
        for t in [0.2, 0.9, 1.6, 2.3, 2.9, 4.5, 7.3, 8.0, 8.7, 9.4, 9.9]:
            f = ve_hien_dai(may_tai(t, s), V, KH); P.append(cv2.cvtColor(cv2.resize(f, (480, 270), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2LAB).astype(np.float32).reshape(-1, 3))
        P = np.concatenate(P); LM, LS = P.mean(0), P.std(0)
        if not thu: json.dump({"mean": LM.tolist(), "std": LS.tolist(), "k": ML.CFG["k_mac_dinh"], "khung_do_s": [0.2, 0.9, 1.6, 2.3, 2.9, 4.5, 7.3, 8.0, 8.7, 9.4, 9.9]}, open(lf, "w"), indent=1)
    K = ML.CFG["k_mac_dinh"]
    hien_cache = {}
    def hien(t):
        key = round(t * FPS)
        if key not in hien_cache:
            m = may_tai(t, s); f = ML.ap_khung(ve_hien_dai(m, V, KH), LM, LS, K); hien_cache.clear(); hien_cache[key] = (f, m)
        return hien_cache[key]
    ghi = []
    TEN = s["ten"]
    def khung_t(t):
        ws = trong_so(t, L); fr = np.zeros((H, W, 3), np.float32); neo_co = {}; m = None
        for src, w in ws:
            if src == "hd": f, m = hien(t)
            else:
                a0, a1, b0, b1 = L[src]; u = min(1.0, max(0.0, (t - a0) / (b1 - a0))); f, p = TO[src].khung(u); neo_co[src] = p
            fr += f.astype(np.float32) * w
        fr = np.clip(fr, 0, 255).astype(np.uint8)
        if m is None: m = may_tai(t, s)
        w_hd = dict((k, v) for k, v in ws).get("hd", 0.0)
        # ---- lớp chữ hiện đại
        if w_hd > 0.02:
            sx, sy = (float(v) for v in m.px(site[1], site[0])); cx, cy = (float(v) for v in m.px(city[1], city[0]))
            cn = s["nhan_nuoc"]; nx, ny = (float(v) for v in m.px(cn[0], cn[1]))
            a_n = max(mo(t, 0.9, 3.15, 0.5), mo(t, 6.7, 10.5, 0.5)) * w_hd
            if a_n > 0:
                r = chu_quang(s["nuoc"].upper(), "cinzel", 64 if t < 7 else 52, "SemiBold", IV, track=1); dan(fr, r, nx - r.shape[1] / 2, ny - r.shape[0] / 2, a_n * 0.92)
            a_c = max(mo(t, 1.7, 3.15), mo(t, 6.8, 10.5)) * w_hd
            a_l = max(mo(t, 2.0, 3.15), mo(t, 7.2, 10.5)) * w_hd
            if a_l > 0:
                u = ez((t - 2.0) / 0.5) if t < 3.2 else ez((t - 7.2) / 0.6)
                ve_net_dut(fr, (cx, cy), (sx, sy), u, a_l)
            if a_c > 0:
                ve_cham(fr, cx, cy, a_c)
                r = chu_quang(s["thanh_pho"]["ten"], "corm", 34, "SemiBold", IV)
                left = cx < sx
                dan(fr, r, (cx - r.shape[1] + 4) if left else (cx - 4), cy - r.shape[0] / 2, a_c)
            a_p = max(mo(t, 1.35, 3.15, 0.25), mo(t, 6.75, 10.5, 0.3)) * w_hd
            if a_p > 0:
                roi = 46 * (1 - ez((t - 1.35) / 0.35)) if t < 1.8 else 0.0
                if t >= 7.3: ve_vong(fr, sx, sy, t - 7.3)
                ve_ghim(fr, sx, sy, a_p, roi)
                r1 = tam_chu([(TEN, "cinzel", 40, "SemiBold", IV), (dong_kc, "corm", 30, "SemiBold", BR)], 205, pad=(18, 10))
                left = not (cx < sx)   # nhãn ghim về phía ngược thành phố
                lx = sx - r1.shape[1] - 34 if left else sx + 30; ly = sy - 40 - r1.shape[0] / 2
                lx = min(W - r1.shape[1] - 40, max(40, lx)); ly = min(H - r1.shape[0] - 110, max(40, ly))
                dan(fr, r1, lx, ly, max(mo(t, 1.6, 3.15), mo(t, 7.1, 10.5)) * w_hd)
            if 0 < t < 10: ghi.append({"t": round(t, 3), "lop": "hien_dai", "ghim_px": [round(float(sx), 1), round(float(sy), 1)], "tp_px": [round(float(cx), 1), round(float(cy), 1)], "dpp": float(m.dpp)})
        # ---- lớp chữ bản đồ cổ
        for i, to in enumerate(TO):
            a0, a1, b0, b1 = L[i]; w = dict((k, v) for k, v in ws).get(i, 0.0)
            if w <= 0.02: continue
            x, y = neo_co[i]; a = mo(t, a0 + 0.35, b1 - 0.25, 0.3) * w
            if a > 0:
                ve_ghim(fr, x, y, a)
                gd = to.g["ghim"]["dong"]
                r = tam_chu([(gd[0], "cinzel", 34, "SemiBold", IV), (gd[1], "corm", 28, "SemiBold", BR)], 205, pad=(16, 10), icon=("K", 22))
                if to.nhan == "duoi":   # dưới ghim, lệch trái — không che chữ địa danh trên tờ
                    lx = x - r.shape[1] * 0.85; ly = y + 100
                else:
                    lx = x + 30 if x + 30 + r.shape[1] < W - 40 else x - 34 - r.shape[1]; ly = y - 40 - r.shape[0] / 2
                lx = min(W - 40 - r.shape[1], max(40, lx)); ly = min(H - r.shape[0] - 110, max(150, ly))
                dan(fr, r, lx, ly, a)
            at = mo(t, a0 + 0.1, b1 - 0.1, 0.4) * w
            if at > 0:
                td = to.M["tieu_de"]; r = tam_chu([(td[0], "cinzel", 34, "SemiBold", IV), (td[1], "corm", 28, "SemiBold", BR)], 215, pad=(18, 12)); dan(fr, r, 52, 44, at)
            ghi.append({"t": round(t, 3), "lop": to.id, "ghim_man_px": [round(float(x), 1), round(float(y), 1)], "ghim_to_px": to.g["px"], "ten_ghi": to.g["ghi"], "w": round(float(w), 3)})
        # ---- dòng ghi nguồn (dưới phải), theo lớp đang trội
        cr = [(s["ghi_cong_hien_dai"], w_hd)] + [(TO[i].M["ghi_cong"], w) for i, w in ws if i != "hd"]
        for txt, w in cr:
            if w > 0.02:
                r = tam_chu([(l, "corm", 23, "SemiBold", IV) for l in txt], 185, pad=(12, 6))
                dan(fr, r, W - 44 - r.shape[1], H - 36 - r.shape[0], w)
        return fr
    # ---- xuất
    ts = [float(x) for x in thu.split(",")] if thu else None
    if ts:
        os.makedirs(os.path.join(REP, "thu"), exist_ok=True)
        for t in ts: cv2.imwrite(os.path.join(REP, "thu", f"{dd}_{t:05.2f}.jpg"), khung_t(t), [cv2.IMWRITE_JPEG_QUALITY, 88])
        return
    os.makedirs(CLIP_DIR, exist_ok=True); ra = os.path.join(CLIP_DIR, f"{dd}.mp4")
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart",
                          "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", ra], stdin=subprocess.PIPE)
    to = {}; t0 = time.time()
    for i in range(NF):
        t = i / FPS; f = khung_t(t); p.stdin.write(f.tobytes())
        if i % 12 == 0: to[i] = cv2.resize(f, (480, 270), interpolation=cv2.INTER_AREA)
        if i % 48 == 0: print(f"  {dd} khung {i}/{NF} {time.time() - t0:.0f} s", flush=True)
    p.stdin.close(); p.wait()
    to_05(dd, to)
    json.dump({"dia_diem": dd, "tep": os.path.relpath(ra, ROOT), "sha256": sha(ra), "khoang_cach_km": round(km, 2), "huong_tu_tp": hg, "phuong_vi_do": round(bear, 1),
               "thanh_pho": {"ten": s["thanh_pho"]["ten"], "ll": city}, "toa_do": site, "lich_ban_do_co": L,
               "ban_do_co": [{"id": t_.id, "ghim": t_.g["ghi"], "px_to_goc": t_.g["px"], "neo_man_2_9s": t_.neo_man} for t_ in TO],
               "look": {"mean": [float(v) for v in LM], "std": [float(v) for v in LS], "k": K}, "lop_chu_mau": ghi[::24]},
              open(os.path.join(REP, "do", f"dung_{dd}.json"), "w"), ensure_ascii=False, indent=1)
    print("→", ra, sha(ra), flush=True)

def to_05(dd, to):
    """tờ 0,5 s: 20 khung (0,0 → 9,5 s) lưới 4 × 5, ghi giây."""
    os.makedirs(os.path.join(REP, "to"), exist_ok=True); ks = sorted(to)
    rows = []
    for r in range(5):
        row = []
        for c in range(4):
            i = ks[r * 4 + c]; im = to[i].copy(); cv2.rectangle(im, (0, 0), (92, 26), (0, 0, 0), -1)
            cv2.putText(im, f"{i / FPS:4.1f}s", (6, 19), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA); row.append(im)
        rows.append(np.hstack(row))
    cv2.imwrite(os.path.join(REP, "to", f"{dd}_0-5s.jpg"), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 85])

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("lenh"); ap.add_argument("dd", nargs="?"); ap.add_argument("--thu")
    a = ap.parse_args()
    if a.lenh == "nguon": nguon()
    elif a.lenh == "khong_che": khong_che()
    elif a.lenh == "dem": dem(a.dd)
    elif a.lenh == "dung": dung(a.dd, a.thu)
    else: raise SystemExit(__doc__)
