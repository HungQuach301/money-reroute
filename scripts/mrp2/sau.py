#!/usr/bin/env python3
"""MR-P2 · Ước độ sâu + tách 3 lớp + vá nền sau tiền cảnh (0 USD, CPU, dựng lại được).
  python3 scripts/mrp2/sau.py <model.onnx> [ma …]
Mô hình: Depth Anything V2 Small (Apache-2.0), bản ONNX công khai `onnx-community/depth-anything-v2-small`
@ 4472b7362082ad9968fee890ca0f1e5aca36b93d, tệp onnx/model.onnx (sha256 afb6a5c2…df10c). Không đưa trọng số vào repo.
Đầu vào: tranh L1 đúng như bản đã đăng (dung.tranh: cắt khung MR-6 → phủ 1920×1080).
Ra (scratch, không đẩy — dựng lại được): $MRP2_TMP/sau/<ma>_{depth.png, l0.png, l1.png, l2.png, mask1.png, mask2.png}
  l0 = nền xa đã vá toàn bộ chỗ lớp giữa+gần; l1 = lớp giữa (RGBA) đã vá chỗ lớp gần; l2 = lớp gần (RGBA)."""
import json, os, sys, hashlib
import numpy as np, cv2, onnxruntime as ort
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP2_TMP", "/tmp/claude-0/mrp2"); OUT = os.path.join(TMP, "sau"); os.makedirs(OUT, exist_ok=True)
os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))
import dung  # noqa: E402  (chỉ dùng hàm tranh() — cắt khung đúng bản đăng)

MEAN = np.array([0.485, 0.456, 0.406], np.float32); STD = np.array([0.229, 0.224, 0.225], np.float32)
# Cấu hình lớp theo tranh: số lớp (2|3) + ngưỡng tay (None = k-means trên độ sâu). Chỉnh sau QC mắt mép lớp.
CAU_HINH = json.load(open(os.path.join(os.path.dirname(__file__), "lop.json")))


def do_sau(sess, im):
    h, w = im.shape[:2]; H = 518; W = int(round(w * H / h / 14)) * 14
    x = cv2.resize(im, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255.0
    x = ((x - MEAN) / STD).transpose(2, 0, 1)[None]
    d = sess.run(None, {sess.get_inputs()[0].name: x})[0][0]
    d = cv2.resize(d, (w, h), interpolation=cv2.INTER_CUBIC)
    d = (d - np.percentile(d, 1)) / (np.percentile(d, 99) - np.percentile(d, 1) + 1e-6)
    return np.clip(d, 0, 1)  # 1 = gần (độ sâu nghịch đảo tương đối)


def nguong(d, k):
    z = d[::4, ::4].reshape(-1, 1).astype(np.float32)
    _, lab, c = cv2.kmeans(z, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1e-4), 5, cv2.KMEANS_PP_CENTERS)
    c = sorted(c.ravel()); return [(c[i] + c[i + 1]) / 2 for i in range(k - 1)]


def mat_na(d, t):
    m = (d > t).astype(np.uint8) * 255
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    m = cv2.morphologyEx(cv2.morphologyEx(m, cv2.MORPH_OPEN, k), cv2.MORPH_CLOSE, k)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)  # bỏ mảnh vụn < 0,4 % khung
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < 0.004 * m.size: m[lab == i] = 0
    return m


def va(im, m, gian=21):
    """Vá vùng m (đã nới) bằng Telea ở ½ độ phân giải → phóng lại, phủ hạt nhẹ để khớp nét cọ."""
    mm = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (gian, gian)))
    h, w = im.shape[:2]; s = cv2.resize(im, (w // 2, h // 2), interpolation=cv2.INTER_AREA); ms = cv2.resize(mm, (w // 2, h // 2), interpolation=cv2.INTER_NEAREST)
    f = cv2.inpaint(s, ms, 9, cv2.INPAINT_TELEA); f = cv2.resize(f, (w, h), interpolation=cv2.INTER_CUBIC)
    f = cv2.GaussianBlur(f, (0, 0), 3)
    rng = np.random.default_rng(7); f = np.clip(f.astype(np.int16) + rng.normal(0, 3, f.shape).astype(np.int16), 0, 255).astype(np.uint8)
    a = (cv2.GaussianBlur(mm, (0, 0), 4).astype(np.float32) / 255)[..., None]
    return (im * (1 - a) + f * a).astype(np.uint8)


def grabcut(im_bgr, d, g):
    """Lớp gần = một vật tách bằng GrabCut, hạt giống = chỗ độ sâu nổi hơn nền cục bộ > 0,05 (b089 ổ khoá — để lắc quanh móc)."""
    bg = cv2.GaussianBlur(cv2.morphologyEx(d.astype(np.float32), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (161, 161))), (0, 0), 25)
    x0, y0, x1, y1 = g["hop"]; gc = np.full(d.shape, cv2.GC_BGD, np.uint8); gc[y0:y1, x0:x1] = cv2.GC_PR_BGD
    gc[((d - bg) > 0.05) & (gc == cv2.GC_PR_BGD)] = cv2.GC_PR_FGD
    a, b, c, e = g["chac"]; gc[b:e, a:c] = cv2.GC_FGD
    cv2.grabCut(im_bgr, gc, None, np.zeros((1, 65)), np.zeros((1, 65)), 6, cv2.GC_INIT_WITH_MASK)
    m = np.where((gc == 1) | (gc == 3), 255, 0).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m); m = ((lab == np.argmax(st[1:, 4]) + 1) * 255).astype(np.uint8)
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE); out = np.zeros_like(m); cv2.drawContours(out, cs, -1, 255, -1)
    return out


def alpha(m, mem=2.5):
    return cv2.GaussianBlur(m, (0, 0), mem)


def lam(sess, ma):
    im = np.array(dung.tranh(ma).convert("RGB"))  # 1920×1080, đúng khung bản đăng
    d = do_sau(sess, im)
    ch = CAU_HINH.get(ma, {}); k = ch.get("lop", 3)
    t = ch.get("nguong") or nguong(d, k)
    cv2.imwrite(os.path.join(OUT, f"{ma}_depth.png"), (d * 65535).astype(np.uint16))
    if k == 2:
        m2 = mat_na(d, t[0]); m1 = m2.copy()
    else:
        m1 = mat_na(d, t[0]); m2 = mat_na(d, t[1]); m1 = np.maximum(m1, m2)
    bgr = im[..., ::-1].copy()
    if ch.get("gan_grabcut"): m2 = grabcut(bgr, d, ch["gan_grabcut"]); m1 = np.maximum(m1, m2)
    l0 = va(bgr, m1)
    l1 = va(bgr, m2)
    cv2.imwrite(os.path.join(OUT, f"{ma}_l0.png"), l0)
    cv2.imwrite(os.path.join(OUT, f"{ma}_l1.png"), np.dstack([l1, alpha(m1)]))
    cv2.imwrite(os.path.join(OUT, f"{ma}_l2.png"), np.dstack([bgr, alpha(m2)]))
    cv2.imwrite(os.path.join(OUT, f"{ma}_mask1.png"), m1); cv2.imwrite(os.path.join(OUT, f"{ma}_mask2.png"), m2)
    return {"ma": ma, "lop": k, "nguong": [round(float(x), 3) for x in t], "phan_tram_giua_gan": round(float((m1 > 0).mean()) * 100, 1),
            "phan_tram_gan": round(float((m2 > 0).mean()) * 100, 1)}


def main():
    mdl = sys.argv[1]; ids = sys.argv[2:] or list(json.load(open(os.path.join(os.path.dirname(__file__), "canh.json")))["l1"])
    sha = hashlib.sha256(open(mdl, "rb").read()).hexdigest()
    sess = ort.InferenceSession(mdl, providers=["CPUExecutionProvider"])
    out = {"model": "depth-anything-v2-small (onnx-community, rev 4472b73)", "sha256": sha, "tranh": {}}
    for ma in ids:
        r = lam(sess, ma); out["tranh"][ma] = r; print(r, flush=True)
    p = os.path.join(ROOT, "reports", "mrp2", "lop_do.json")
    old = json.load(open(p)) if os.path.exists(p) else {"tranh": {}}
    old.update({k: v for k, v in out.items() if k != "tranh"}); old["tranh"].update(out["tranh"])
    json.dump(old, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
