# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/common/quet_v8.py (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa)
"""[K-MỚI · K-V8] Quét lỗi Veo TOÀN PHIM, dùng chung mọi tập (CONG-THUC-LOAT §1.9 V8). 0 USD API — chỉ ffmpeg + OpenCV (+ YOLO CPU cho cột 5).
Vào : <phim.mp4> + <dung.json> (mục "doan": [{id, f0, n, kind?}], khung 24p theo bản dựng; "kind" = "ket" và id trong "giu_cho" bị bỏ qua).
Ra  : <ra>.json (mỗi khe: số đo, đoạn nghi theo cột, giây đầu–cuối) + <ra>-to/<khe>_c<cột>_<mm.ss>.jpg (tờ ảnh mỗi đoạn nghi: 8 ô 0,25 s quanh đỉnh,
      khoanh vùng nghi) + <ra>-to/TONG.jpg (mỗi đoạn nghi một ô đỉnh).
Cột (đo trên khung 640×360, bỏ vùng chữ: ô năm dưới trái, nhãn sự kiện trên trái):
  c1 MƯA VỆT DÀI  : vệt mảnh sáng gần thẳng đứng (±12°), dài > 8 % chiều cao khung, MỚI so với khung lân cận đã bù dịch máy (vật tĩnh như cột đá bị trừ),
                    màu trắng/xám (S ≤ 70, V ≥ 110 — loại cột đá, giàn giáo, vệt bụi cam khi máy tiến), ≥ 6 vệt/khung trong ≥ 6 khung liên tiếp.
  c2 BỤI/KHÓI BÙNG: mảng "mờ" (ít vân; không phải trời xanh, không phải mây/sương trắng-xám sáng) MỚI so với neo đầu khe; khối liền lớn nhất có
                    trọng tâm dưới đường trời (xuất phát từ mặt đất/công trình) tăng ≥ 8 % diện tích khung trong 1 s và giữ mức tăng đó ≥ 1 s.
  c3 VÁCH/NÚI BIẾN DẠNG: đường trời liền mạch (mỗi cột ảnh: điểm đổi bậc "độ trời" = sáng + xanh + ít vân, nối bằng quy hoạch động) so với neo đầu
                    và neo cuối sau khi khớp affine (bù lia, nghiêng, zoom); lệch TRUNG VỊ > 3 % chiều cao khung (lệnh: 2 % — hiệu chỉnh lên 3 %, xem
                    BAO-CAO) với CẢ HAI neo, giữ ≥ 12 khung. Chỉ tính cột ảnh có bậc trời–đất rõ ở cả hai neo; khe mà hai neo đã lệch nhau > 3 %
                    (máy đi vào cảnh khác, mây che neo) ghi "không áp dụng".
  c4 MÀN PHỦ KÍN  : năng lượng chi tiết (|Laplace| trung bình) < 50 % VÀ độ lệch chuẩn độ sáng < 70 % so với cả hai neo, độ sáng trung bình vẫn
                    ≥ 60 % neo sáng hơn (loại trời tối dần), kéo dài > 1 s.
  c5 NGƯỜI/VẬT TRÔI, MỜ DẦN: YOLOv8s (người + thú lớn COCO, ảnh 960×540) mỗi --buoc khung, nối vệt theo IoU. Nghi "hiện/mất tại chỗ": vệt bắt
                    đầu/kết thúc giữa khe (≥ 1 s từ hai đầu khe), ô không bị mép khung cắt, 1 s trước/sau KHÔNG có phát hiện nào (độ tin ≥ 0,15)
                    quanh chỗ đó; ≥ 3 vệt như vậy trong 0,5 s và tương phản ô người (so nền quanh) đổi dần, trung vị nhóm ≥ 20 % trong 0,5 s cạnh
                    mép vệt (người hiện/mờ như bóng ma, không bước vào/ra). Nghi "trôi": vệt dịch ≥ 1,5 px/khung mà ô người gần như không đổi
                    hình (tương quan ≥ 0,97). Kèm dấu "dãn khung" (đỉnh chu kỳ 3 hoặc 5 khung trong MAE ≥ 4× nền ⇒ khe bị nội suy 1,5× / 1,25×,
                    nguồn của nhoè/trôi theo V2; chu kỳ 4 không dùng — có cả ở clip Veo không dãn).
Cờ máy chỉ DẪN MẮT: mọi đoạn nghi phải xem tờ ảnh trước khi kết luận. Hiệu chỉnh và tỉ lệ bắt/báo nhầm: reports/kv8/BAO-CAO.md.
  /opt/cine/bin/python scripts/common/quet_v8.py <phim.mp4> <dung.json> --ra reports/<mốc>/do/quet_v8 [--cot 1,2,3,4,5] [--khe A3,C1] [--buoc 4]
"""
import argparse, hashlib, json, os, subprocess, sys
import cv2, numpy as np

W, H, FPS = 640, 360, 24
NGUONG = dict(
    c1_len=0.08, c1_ridge=7.0, c1_n_vet=6, c1_khung=6, c1_goc=12, c1_sat=70, c1_sang=110,
    c2_tang=8.0, c2_tex=5.0, c2_khung=24, c2_dai=24,
    c3_lech=0.03, c3_neo=0.03, c3_khung=12, c3_bac=0.35, c3_cot_min=0.3,
    c4_lap=0.5, c4_std=0.7, c4_sang=0.6, c4_khung=24,
    c5_conf=0.30, c5_vet_min=3, c5_doi=0.20, c5_dan=4.0, c5_corr=0.97, c5_dich=1.5,
)


def mat_na_chu(w=W, h=H):
    """1 = được đo. Bỏ ô năm dưới trái và nhãn sự kiện trên trái (bố cục chữ chung của kênh, CONG-THUC §3)."""
    m = np.ones((h, w), np.uint8)
    m[int(h * 0.80):, :int(w * 0.30)] = 0
    m[:int(h * 0.085), :int(w * 0.40)] = 0
    return m


def doc_khe(phim, f0, n, w=W, h=H):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{f0 / FPS:.5f}", "-i", phim, "-frames:v", str(n), "-an",
                          "-vf", f"scale={w}:{h}:flags=area", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    b = p.stdout.read(); p.wait()
    return np.frombuffer(b, np.uint8).reshape(-1, h, w, 3)


def ts(f):
    s = f / FPS
    return f"{int(s // 60)}:{s % 60:04.1f}"


def doan_lien(mask, min_len, f0, gop=12):
    """Các đoạn True liên tiếp dài ≥ min_len → [(i0, i1)] chỉ số trong khe; đoạn cách nhau < `gop` khung được gộp trước khi xét độ dài."""
    mask = np.asarray(mask, bool).copy(); idx = np.where(mask)[0]
    for a, b in zip(idx[:-1], idx[1:]):
        if 1 < b - a <= gop: mask[a:b] = True
    out, i, n = [], 0, len(mask)
    while i < n:
        if mask[i]:
            j = i
            while j < n and mask[j]: j += 1
            if j - i >= min_len: out.append((i, j - 1))
            i = j
        else: i += 1
    return out


# ---------- c1 mưa vệt dài ----------
def _nhan_duong(L, goc):
    k = np.zeros((L, L), np.uint8); c = L // 2
    dx = np.tan(np.radians(goc)) * c
    cv2.line(k, (int(round(c - dx)), 0), (int(round(c + dx)), L - 1), 1, 1)
    return k


def _bu_dich(a, b):
    """Dịch b về a (tịnh tiến, tương quan pha)."""
    (dx, dy), _ = cv2.phaseCorrelate(a, b)
    M = np.float32([[1, 0, -dx], [0, 1, -dy]])
    return cv2.warpAffine(b, M, (a.shape[1], a.shape[0]), borderMode=cv2.BORDER_REPLICATE)


def c1_mua(F, G, mn, ng):
    n = len(G); L = int(round(ng["c1_len"] * H))
    nhan = [_nhan_duong(L, g) for g in (-ng["c1_goc"], -6, 0, 6, ng["c1_goc"])]
    hk = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 1))
    so_vet = np.zeros(n); vung = [None] * n
    for t in range(n):
        lan = [G[k] for k in (t - 2, t - 1, t + 1, t + 2) if 0 <= k < n]
        if len(lan) < 2: continue
        bg = np.median(np.stack([_bu_dich(G[t], x) for x in lan]), 0)
        D = np.clip(G[t] - bg, 0, None)
        R = cv2.morphologyEx(D, cv2.MORPH_TOPHAT, hk)       # chỉ giữ cấu trúc hẹp hơn 7 px theo chiều ngang
        B = ((R > ng["c1_ridge"]) & (mn > 0)).astype(np.uint8)
        U = np.zeros_like(B)
        for k in nhan: U |= cv2.morphologyEx(B, cv2.MORPH_OPEN, k)
        nc, lab, st, _ = cv2.connectedComponentsWithStats(U, 8)
        hsv = cv2.cvtColor(F[t], cv2.COLOR_BGR2HSV)
        dai = []
        for i in range(1, nc):
            if st[i, cv2.CC_STAT_HEIGHT] < L: continue
            px = hsv[lab == i]
            if px[:, 1].mean() <= ng["c1_sat"] and px[:, 2].mean() >= ng["c1_sang"]: dai.append(i)   # mưa: trắng/xám, không phải cột đá/giàn cam
        so_vet[t] = len(dai)
        if dai: vung[t] = np.isin(lab, dai)
    co = so_vet >= ng["c1_n_vet"]
    return so_vet, doan_lien(co, ng["c1_khung"], 0), vung


# ---------- c2 bụi/khói bùng ----------
def _mo(F, G):
    hsv = cv2.cvtColor(F, cv2.COLOR_BGR2HSV)
    m = cv2.blur(G, (7, 7)); s = np.sqrt(np.clip(cv2.blur(G * G, (7, 7)) - m * m, 0, None))
    troi_xanh = (hsv[..., 0] >= 90) & (hsv[..., 0] <= 135) & (hsv[..., 1] > 50)
    may_suong = (hsv[..., 1] < 45) & (hsv[..., 2] > 140)          # mây/sương trắng-xám sáng: thời tiết, không phải bụi/khói bùng
    return (s < NGUONG["c2_tex"]) & ~troi_xanh & ~may_suong & (hsv[..., 2] > 50)


def c2_bui(F, G, mn, ng, troi_y):
    n = len(F); ref = np.zeros(G[0].shape, bool)
    for k in range(min(4, n)): ref |= _mo(F[k], G[k])
    ref = cv2.dilate(ref.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
    duoi = np.zeros_like(ref); y0 = int(np.clip(troi_y, 0, H - 1)); duoi[y0:] = True
    S = mn.sum(); A = np.zeros(n); Ad = np.zeros(n); vung = [None] * n
    for t in range(n):
        new = _mo(F[t], G[t]) & ~ref & (mn > 0)
        new = cv2.morphologyEx(new.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        new = cv2.morphologyEx(new, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
        nc, lab, st, ce = cv2.connectedComponentsWithStats(new, 8)
        # khối liền lớn nhất có trọng tâm dưới đường trời (đám bụi/khói một khối; mái nhà lộ ra khi máy đi là nhiều mảnh rời)
        best = 0
        for i in range(1, nc):
            if ce[i][1] >= y0 and st[i, cv2.CC_STAT_AREA] > best: best = st[i, cv2.CC_STAT_AREA]; bi = i
        A[t] = new.sum() / S * 100; Ad[t] = best / S * 100; vung[t] = (lab == bi) if best else None
    k = ng["c2_khung"]; tang = np.zeros(n)
    for t in range(n - k): tang[t + k] = Ad[t + k] - Ad[:t + 1].min()
    co = tang >= ng["c2_tang"]
    return A, Ad, tang, doan_lien(co, ng["c2_dai"], 0, gop=6), vung


# ---------- c3 đường trời ----------
def _do_troi(F, G):
    lab = cv2.cvtColor(F, cv2.COLOR_BGR2LAB).astype(np.float32)
    m = cv2.blur(G, (5, 5)); s = np.sqrt(np.clip(cv2.blur(G * G, (5, 5)) - m * m, 0, None))
    return (lab[..., 0] / 255.0) + (128 - lab[..., 2]) / 40.0 - s / 12.0     # sáng + xanh (b* âm) − vân


def duong_troi(F, G, mn, w=320, h=180):
    """Đường trời liền mạch: điểm đổi bậc "độ trời" mỗi cột ảnh (trên trời, dưới đất), nối bằng quy hoạch động (|Δy| ≤ 3 px/cột,
    phạt 0,02/px) để mây/chim không làm nhảy. Trả y (theo khung 360) và độ lớn bậc mỗi cột (320 cột)."""
    Fs = cv2.resize(F, (w, h), interpolation=cv2.INTER_AREA); Gs = cv2.resize(G, (w, h), interpolation=cv2.INTER_AREA)
    m = cv2.resize(mn, (w, h), interpolation=cv2.INTER_NEAREST) > 0
    s = cv2.GaussianBlur(_do_troi(Fs, Gs), (5, 5), 0); s = np.where(m, s, 0.0); cm = m.astype(np.float32)
    c = np.cumsum(s, 0); cnt = np.cumsum(cm, 0); tot, totn = c[-1], cnt[-1]
    ylo, yhi = int(0.03 * h), int(0.80 * h); ys = np.arange(ylo, yhi)
    bac = c[ys - 1] / np.maximum(cnt[ys - 1], 1) - (tot - c[ys - 1]) / np.maximum(totn - cnt[ys - 1], 1)
    ny, nx = bac.shape; R = 3; lam = 0.02
    acc = bac[:, 0].copy(); back = np.zeros((ny, nx), np.int16)
    for x in range(1, nx):
        best = np.full(ny, -1e9); arg = np.zeros(ny, np.int16)
        for d in range(-R, R + 1):
            sh = np.full(ny, -1e9)
            if d >= 0: sh[d:] = acc[:ny - d] if d else acc
            else: sh[:d] = acc[-d:]
            sh = sh - lam * abs(d); better = sh > best; best[better] = sh[better]; arg[better] = d
        acc = best + bac[:, x]; back[:, x] = arg
    y = np.zeros(nx, int); y[-1] = int(acc.argmax())
    for x in range(nx - 1, 0, -1): y[x - 1] = y[x] - back[y[x], x]
    return (ys[y] * (H / h)).astype(np.float32), bac[y, np.arange(nx)]


def _khop(yr, yt, hop):
    """Khớp yt ≈ α·yr(x − dx) + β + γ·x (bù lia/nghiêng/zoom), trả phần dư tuyệt đối trên các cột hợp lệ."""
    nx = len(yr); xs = np.arange(nx); best = None
    for dx in range(-24, 25, 2):
        xr = xs - dx; ok = hop & (xr >= 0) & (xr < nx)
        ok[ok] &= hop[xr[ok]]
        if ok.sum() < 0.25 * nx: continue
        A = np.stack([yr[xr[ok]], np.ones(ok.sum()), xs[ok] / nx], 1)
        coef, *_ = np.linalg.lstsq(A, yt[ok], rcond=None)
        res = np.abs(yt[ok] - A @ coef)
        sc = np.percentile(res, 75)
        if best is None or sc < best[0]: best = (sc, res)
    return best[1] if best else None


def c3_troi(F, G, mn, ng):
    n = len(F); nx = 320
    Y = np.zeros((n, nx), np.float32); B = np.zeros((n, nx), np.float32)
    for t in range(n): Y[t], B[t] = duong_troi(F[t], G[t], mn)
    k = min(3, n); y0 = np.median(Y[:k], 0); y1 = np.median(Y[-k:], 0)
    hop = (np.min(B[:k], 0) > ng["c3_bac"]) & (np.min(B[-k:], 0) > ng["c3_bac"])
    if hop.mean() < ng["c3_cot_min"]:
        return None, [], float(hop.mean()), float(np.median(y0))
    r01 = _khop(y0, y1, hop)
    if r01 is None or np.percentile(r01, 75) / H > ng["c3_neo"]:     # hai neo đã khác nhau (máy đi vào cảnh khác) → không áp dụng
        return None, [], float(hop.mean()), float(np.median(y0[hop]))
    lech = np.zeros(n)
    for t in range(n):
        ra = _khop(y0, Y[t], hop); rb = _khop(y1, Y[t], hop)
        va = np.median(ra) if ra is not None else 1e9; vb = np.median(rb) if rb is not None else 1e9
        lech[t] = min(va, vb) / H
    return lech, doan_lien(lech > ng["c3_lech"], ng["c3_khung"], 0, gop=0), float(hop.mean()), float(np.median(y0[hop]))


# ---------- c4 màn phủ kín ----------
def c4_man(G, mn, ng):
    n = len(G); m = mn > 0
    lap = np.array([np.abs(cv2.Laplacian(g, cv2.CV_32F))[m].mean() for g in G])
    sd = np.array([g[m].std() for g in G])
    k = min(6, n)
    l0, l1 = np.median(lap[:k]), np.median(lap[-k:]); s0, s1 = np.median(sd[:k]), np.median(sd[-k:])
    mu = np.array([g[m].mean() for g in G]); m0, m1 = np.median(mu[:k]), np.median(mu[-k:])
    rl = lap / max(min(l0, l1), 1e-3); rs = sd / max(min(s0, s1), 1e-3)
    sang = mu >= ng["c4_sang"] * max(m0, m1)          # màn phủ giữ độ sáng; trời tối dần (chuyển đêm) thì không tính
    co = (rl < ng["c4_lap"]) & (rs < ng["c4_std"]) & sang
    return rl, rs, doan_lien(co, ng["c4_khung"] + 1, 0)


# ---------- c5 người/vật ----------
_YOLO = None
LOP = {0: "nguoi", 16: "cho", 17: "ngua", 18: "cuu", 19: "bo", 15: "meo"}


def yolo():
    global _YOLO
    if _YOLO is None:
        from ultralytics import YOLO
        _YOLO = YOLO(os.environ.get("YOLO_W", "/tmp/yolov8s.pt"))
    return _YOLO


def _tuong_phan(G, b):
    x0, y0, x1, y1 = [int(v) for v in b]
    x0, y0 = max(x0, 0), max(y0, 0); x1, y1 = min(x1, G.shape[1]), min(y1, G.shape[0])
    if x1 - x0 < 2 or y1 - y0 < 2: return 0.0
    o = G[y0:y1, x0:x1]; pad = max(4, (y1 - y0) // 2)
    X0, Y0, X1, Y1 = max(x0 - pad, 0), max(y0 - pad, 0), min(x1 + pad, G.shape[1]), min(y1 + pad, G.shape[0])
    nen = G[Y0:Y1, X0:X1]
    return float(abs(o.mean() - nen.mean()) + o.std())


def _iou(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0])); iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    u = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - ix * iy
    return ix * iy / u if u > 0 else 0


def c5_nguoi(Fhi, ng, buoc):
    """Fhi: khung 960×540. Dò mỗi `buoc` khung; nối vệt theo IoU / tâm gần."""
    M = yolo(); n = len(Fhi); sc = Fhi.shape[2] / W
    Gh = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32) for f in Fhi]
    idx = list(range(0, n, buoc))
    res = M.predict([Fhi[i] for i in idx], imgsz=960, conf=0.15, classes=list(LOP), verbose=False)
    vet = []; tho = {}
    for t, r in zip(idx, res):
        bx = r.boxes.xyxy.cpu().numpy(); cf = r.boxes.conf.cpu().numpy(); cl = r.boxes.cls.cpu().numpy().astype(int)
        tho[t] = [((q[0] + q[2]) / 2, (q[1] + q[3]) / 2) for q in bx]
        dung = [False] * len(bx)
        for v in vet:
            if v["het"] or t - v["t"][-1] > 3 * buoc: v["het"] = True; continue
            best, bj = 0.2, -1
            for j, b in enumerate(bx):
                if dung[j]: continue
                ii = _iou(v["b"][-1], b)
                if ii > best: best, bj = ii, j
            if bj >= 0:
                dung[bj] = True; v["t"].append(t); v["b"].append(bx[bj]); v["c"].append(float(cf[bj]))
                v["tp"].append(_tuong_phan(Gh[t], bx[bj]))
        for j, b in enumerate(bx):
            if not dung[j] and cf[j] >= ng["c5_conf"]:
                vet.append(dict(lop=LOP.get(int(cl[j]), str(cl[j])), t=[t], b=[b], c=[float(cf[j])], tp=[_tuong_phan(Gh[t], b)], het=False))
    nghi = []
    Wh, Hh = Fhi.shape[2], Fhi.shape[1]
    for v in vet:
        if len(v["t"]) < 3 or max(v["c"]) < ng["c5_conf"]: continue
        b0, b1 = v["b"][0], v["b"][-1]
        def o_mep(b): return b[0] < 0.03 * Wh or b[2] > 0.97 * Wh or b[1] < 0.03 * Hh or b[3] > 0.97 * Hh
        if (b0[2] - b0[0]) * (b0[3] - b0[1]) > 0.15 * Wh * Hh: continue          # ô quá lớn (vách đá bị nhận nhầm thành thú)
        # xuất hiện / biến mất "từ không": vệt bắt đầu/kết thúc GIỮA khe, ô đủ cỡ (không bị mép khung cắt), và trong 1 s trước/sau
        # KHÔNG có phát hiện nào (kể cả độ tin thấp 0,15) có tâm trong ô nới 50 % → người không đi vào/ra mà hiện/mờ tại chỗ.
        tt = np.array(v["t"]); tp = np.array(v["tp"])
        for dau in (True, False):
            b = b0 if dau else b1; t_m = tt[0] if dau else tt[-1]
            if t_m < 24 or t_m > n - 25: continue
            sel = (tt <= t_m + 12) if dau else (tt >= t_m - 12)
            dt = np.array([(q[2] - q[0]) * (q[3] - q[1]) for q in np.array(v["b"])[sel]])
            if o_mep(b) and (dt[0] if dau else dt[-1]) < 0.7 * np.median(dt): continue   # đi vào/ra qua mép khung
            ww, hh2 = (b[2] - b[0]) * 0.5, (b[3] - b[1]) * 0.5
            rng = range(t_m - 24, t_m) if dau else range(t_m + 1, t_m + 25)
            co_truoc = any(b[0] - ww <= cx <= b[2] + ww and b[1] - hh2 <= cy <= b[3] + hh2 for k in rng for cx, cy in tho.get(k, []))
            if co_truoc: continue
            gan = tp[sel]; mep = gan[0] if dau else gan[-1]; xa = np.median(gan[-2:] if dau else gan[:2])
            nghi.append(dict(kieu="hiện tại chỗ" if dau else "mất tại chỗ", lop=v["lop"], i=int(t_m), box=[float(x / sc) for x in b],
                             tp_doi=round(float((xa - mep) / max(xa, 1e-3)), 2)))
        # trôi: dịch đều nhưng ô không đổi dạng (không bước chân)
        if len(v["t"]) >= 6:
            cs = []; ds = []
            for a, b2, ta, tb in zip(v["b"][:-1], v["b"][1:], v["t"][:-1], v["t"][1:]):
                ca = ((a[0] + a[2]) / 2, (a[1] + a[3]) / 2); cb = ((b2[0] + b2[2]) / 2, (b2[1] + b2[3]) / 2)
                ds.append(np.hypot(cb[0] - ca[0], cb[1] - ca[1]) / (tb - ta) / sc)
                x0, y0, x1, y1 = [int(q) for q in a]; X0, Y0 = int(b2[0]), int(b2[1])
                pa = Gh[ta][max(y0, 0):y1, max(x0, 0):x1]; pb = Gh[tb][max(Y0, 0):max(Y0, 0) + pa.shape[0], max(X0, 0):max(X0, 0) + pa.shape[1]]
                if pa.size > 20 and pa.shape == pb.shape and pa.std() > 1 and pb.std() > 1: cs.append(float(np.corrcoef(pa.ravel(), pb.ravel())[0, 1]))
            if cs and np.median(ds) >= ng["c5_dich"] and np.median(cs) >= ng["c5_corr"] and (v["b"][0][3] - v["b"][0][1]) / sc >= 14:
                nghi.append(dict(kieu="trôi", lop=v["lop"], i=int(v["t"][len(v["t"]) // 2]), box=[float(x / sc) for x in v["b"][len(v["b"]) // 2]],
                                 dich_px_khung=round(float(np.median(ds)), 2), tuong_quan=round(float(np.median(cs)), 3)))
    # gộp: các nghi mờ/hiện cùng kiểu trong 1 s → một mục, ghi số vệt (≥ 2 vệt đồng loạt là dấu mạnh)
    gop = []
    for q in sorted(nghi, key=lambda q: (q["kieu"], q["i"])):
        if gop and gop[-1]["kieu"] == q["kieu"] and q["i"] - gop[-1]["i"] <= 12 and q["kieu"] != "trôi":
            gop[-1]["so_vet"] += 1; gop[-1]["_doi"].append(q.get("tp_doi", 0)); continue
        q["so_vet"] = 1; q["_doi"] = [q.get("tp_doi", 0)]; gop.append(q)
    for q in gop:
        q["tp_doi_tv"] = round(float(np.median(q.pop("_doi"))), 2); q.pop("tp_doi", None)
    return vet, [q for q in gop if q["kieu"] == "trôi" or (q["so_vet"] >= ng["c5_vet_min"] and q["tp_doi_tv"] >= ng["c5_doi"])]


def dan_khung(G):
    """Dấu nội suy: chu kỳ trong chuỗi MAE khung liên tiếp (3 ⇒ dãn 1,5×; 5 ⇒ dãn 1,25×). Chu kỳ 4 KHÔNG dùng: clip Veo không dãn
    (MC-1) cũng có đỉnh chu kỳ 4 tới 7× nền — dấu riêng của nguồn/mã hoá, không phải nội suy."""
    if len(G) < 40: return None
    d = np.array([np.abs(G[i + 1] - G[i]).mean() for i in range(len(G) - 1)])
    d = d - cv2.blur(d.reshape(1, -1).astype(np.float32), (9, 1)).ravel()
    sp = np.abs(np.fft.rfft(d - d.mean())); fr = np.fft.rfftfreq(len(d))
    out = {}
    for p in (3, 5):
        k = int(np.argmin(np.abs(fr - 1 / p))); nen = np.median(sp[1:]) + 1e-6
        out[p] = round(float(sp[max(k - 1, 1):k + 2].max() / nen), 1)
    return out


# ---------- tờ ảnh ----------
def to_anh(F, i0, i1, f0, nhan, vung=None, box=None):
    """8 ô cách 0,25 s quanh giữa đoạn; viền đỏ = vùng nghi (c1/c2) hoặc ô người (c5, toạ độ 640×360)."""
    pk = (i0 + i1) // 2; idx = sorted(set(int(np.clip(pk + d * 6, 0, len(F) - 1)) for d in range(-4, 4)))
    T = []
    for i in idx:
        t = cv2.resize(F[i], (320, 180), interpolation=cv2.INTER_AREA)
        if vung is not None and vung[i] is not None:
            m = cv2.resize(vung[i].astype(np.uint8), (320, 180), interpolation=cv2.INTER_NEAREST)
            cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); cv2.drawContours(t, cs, -1, (0, 0, 255), 1)
        if box is not None:
            b = [int(v / 2) for v in box]  # 640×360 → ô 320×180
            cv2.rectangle(t, (b[0] - 2, b[1] - 2), (b[2] + 2, b[3] + 2), (0, 0, 255), 2)
        cv2.putText(t, f"{nhan} {ts(f0 + i)}", (4, 14), 0, 0.42, (0, 255, 255), 1)
        T.append(t)
    while len(T) < 8: T.append(np.zeros_like(T[0]))
    return np.vstack([np.hstack(T[:4]), np.hstack(T[4:8])]), F[pk]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phim"); ap.add_argument("dung"); ap.add_argument("--ra", required=True)
    ap.add_argument("--cot", default="1,2,3,4,5"); ap.add_argument("--khe", default="")
    ap.add_argument("--buoc", type=int, default=4); ap.add_argument("--khong-to", action="store_true")
    a = ap.parse_args()
    cot = {int(c) for c in a.cot.split(",")}; chon = set(filter(None, a.khe.split(",")))
    D = json.load(open(a.dung)); giu = set(D.get("giu_cho") or [])
    sha = hashlib.sha256(open(a.phim, "rb").read()).hexdigest()
    sha_khai = (D.get("sha256") or {}).get(os.path.basename(a.phim))
    tod = a.ra + "-to"; os.makedirs(tod, exist_ok=True); os.makedirs(os.path.dirname(a.ra) or ".", exist_ok=True)
    mn = mat_na_chu(); ng = NGUONG
    out = dict(phim=a.phim, sha256=sha, sha256_khop_dung=(sha == sha_khai) if sha_khai else None, dung=a.dung, nguong=ng, cot=sorted(cot), khe=[])
    TONG = []
    for s in D["doan"]:
        if s.get("kind") == "ket" or s["id"] in giu or s["id"] == "KET": continue
        if chon and s["id"] not in chon: continue
        f0, n = s["f0"], s["n"]
        F = doc_khe(a.phim, f0, n)
        if len(F) < 8: continue
        G = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32) for f in F]
        r = dict(khe=s["id"], dau=ts(f0), cuoi=ts(f0 + n - 1), n=len(F), nghi=[])
        def them(c, i0, i1, mo_ta, vung=None, khung=None, **kw):
            if khung is not None: kw["khung_640"] = [round(float(x), 1) for x in khung]
            r["nghi"].append(dict(cot=c, tu=ts(f0 + i0), den=ts(f0 + i1), giay=round((f0 + i0) / FPS, 2), dai_s=round((i1 - i0 + 1) / FPS, 2), mo_ta=mo_ta, **kw))
            if not a.khong_to:
                im, dinh = to_anh(F, i0, i1, f0, f"c{c} {s['id']}", vung, khung)
                p = os.path.join(tod, f"{s['id']}_c{c}_{ts(f0 + i0).replace(':', 'm')}.jpg"); cv2.imwrite(p, im, [cv2.IMWRITE_JPEG_QUALITY, 82])
                r["nghi"][-1]["to"] = os.path.relpath(p, os.path.dirname(os.path.abspath(a.ra)) if False else ".")
                t = cv2.resize(dinh, (320, 180)); cv2.putText(t, f"c{c} {s['id']} {ts(f0 + i0)}", (4, 14), 0, 0.42, (0, 255, 255), 1); TONG.append(t)
        p75, seg3, cot_hop, troi_y = (None, [], 0, H * 0.3)  # p75 = lệch đường trời (phân vị 75 %, /H) sau khớp neo
        if 3 in cot or 2 in cot:
            p75, seg3, cot_hop, troi_y = c3_troi(F, G, mn, ng)
        if 3 in cot:
            r["c3"] = dict(cot_hop=round(float(cot_hop), 2), lech_p75_max=round(float(p75.max()), 4) if p75 is not None else None,
                           ap_dung=p75 is not None)
            for i0, i1 in seg3:
                them(3, i0, i1, f"đường trời lệch trung vị tối đa {p75[i0:i1 + 1].max() * 100:.1f} % H so với nội suy neo đầu–cuối",
                     lech_max=round(float(p75[i0:i1 + 1].max()), 4))  # p75 ở đây là chuỗi lệch trung vị/H
        if 1 in cot:
            sv, seg1, vung1 = c1_mua(F, G, mn, ng)
            r["c1"] = dict(vet_max=int(sv.max()), vet_tb=round(float(sv.mean()), 2))
            for i0, i1 in seg1:
                them(1, i0, i1, f"vệt dọc dài > {ng['c1_len'] * 100:.0f} % H: tối đa {int(sv[i0:i1 + 1].max())} vệt/khung", vung1, vet_max=int(sv[i0:i1 + 1].max()))
        if 2 in cot:
            A, Ad, tang, seg2, vung2 = c2_bui(F, G, mn, ng, troi_y if troi_y else H * 0.3)
            r["c2"] = dict(moi_max=round(float(A.max()), 1), tang_1s_max=round(float(tang.max()), 1))
            for i0, i1 in seg2:
                them(2, i0, i1, f"mảng mờ mới dưới đường trời tăng {tang[i0:i1 + 1].max():.1f} % khung/1 s (tổng {Ad[i1]:.1f} %)", vung2,
                     tang_max=round(float(tang[i0:i1 + 1].max()), 1))
        if 4 in cot:
            rl, rs, seg4 = c4_man(G, mn, ng)
            r["c4"] = dict(lap_min=round(float(rl.min()), 2), std_min=round(float(rs.min()), 2))
            for i0, i1 in seg4:
                them(4, i0, i1, f"chi tiết còn {rl[i0:i1 + 1].min() * 100:.0f} %, tương phản còn {rs[i0:i1 + 1].min() * 100:.0f} % so với neo", lap_min=round(float(rl[i0:i1 + 1].min()), 2))
        if 5 in cot:
            r["dan_khung"] = dan_khung(G)
            Fhi = doc_khe(a.phim, f0, n, 960, 540)
            vet, ng5 = c5_nguoi(Fhi, ng, a.buoc); del Fhi
            r["c5"] = dict(vet=len(vet), vet_dai=sum(len(v["t"]) >= 3 for v in vet))
            dk = r["dan_khung"] or {}
            if dk and max(dk.values()) >= ng["c5_dan"]:
                p = max(dk, key=dk.get)
                them(5, 0, len(F) - 1, f"dãn khung: chu kỳ {p} khung trong MAE (đỉnh {dk[p]}× nền) ⇒ khe nội suy luồng quang, vật chuyển động dễ nhoè/trôi",
                     kieu="dãn khung", chu_ky=p)
            for q in ng5:
                i = q.pop("i"); q["khung"] = q.pop("box"); them(5, max(i - 6, 0), min(i + 6, len(F) - 1), f"{q['kieu']} ({q['lop']})", None, **q)
        out["khe"].append(r)
        print(s["id"], r["dau"], {k: r[k] for k in ("c1", "c2", "c3", "c4", "c5", "dan_khung") if k in r}, [(q["cot"], q["tu"], q["dai_s"]) for q in r["nghi"]], flush=True)
    out["tong_nghi"] = {f"c{c}": sum(1 for r in out["khe"] for q in r["nghi"] if q["cot"] == c) for c in sorted(cot)}
    json.dump(out, open(a.ra + ".json", "w"), ensure_ascii=False, indent=1)
    if TONG and not a.khong_to:
        while len(TONG) % 6: TONG.append(np.zeros_like(TONG[0]))
        cv2.imwrite(os.path.join(tod, "TONG.jpg"), np.vstack([np.hstack(TONG[i:i + 6]) for i in range(0, len(TONG), 6)]), [cv2.IMWRITE_JPEG_QUALITY, 80])
    print("tổng nghi:", out["tong_nghi"])


if __name__ == "__main__":
    main()
