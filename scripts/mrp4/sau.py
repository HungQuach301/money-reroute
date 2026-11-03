#!/usr/bin/env python3
"""MR-P4 · Độ sâu + tách 3 lớp + CHỈ SỐ "ĐỘ SÂU HỮU DỤNG" (HD) mỗi tranh L1 đoạn thử (0 USD, CPU, dựng lại được).
Gọi lại scripts/mrp2/sau.py (Depth Anything V2 Small, Apache-2.0, onnx-community/depth-anything-v2-small @ 4472b73,
tệp onnx/model.onnx sha256 afb6a5c2…df10c; trọng số KHÔNG đưa vào repo).
  MRP4_TMP=… python3 scripts/mrp4/sau.py <model.onnx> [--moi] [ma …]
    --moi : đo tranh MỚI (lab/mrp4/anh/<ma>_l*.png đã chọn ở reports/mrp4/anh/chon.json) thay tranh bản đăng
Ra: $MRP4_TMP/sau[_moi]/<ma>_{depth,l0,l1,l2,mask1,mask2}.png (scratch) + reports/mrp4/do_sau[_moi].json.

Chỉ số HD (0–100) = 100 · TRAI · TACH · f(GAN)
  TRAI  độ trải độ sâu trong khung = (p95 − p5) / p95 của độ sâu THÔ (nghịch đảo, chưa chuẩn hoá) — tranh có vật gần và nền xa → gần 1;
        tranh "một mặt phẳng" (bàn nhìn gần, tường, mặt tiền) → nhỏ. Mô hình cho độ sâu tương đối (sai khác tỉ lệ + dịch) → chỉ so giữa tranh.
  TACH  độ tách lớp gần = trung vị độ sâu chuẩn hoá trong lớp gần − trung vị phần còn lại (0–1); dốc đều (sàn, mặt bàn) → nhỏ.
  GAN   diện tích lớp gần (mask2 của sau.py, % khung); f(GAN) = min(GAN/12 %, 1) · (1 nếu GAN ≤ 55 %, giảm tuyến tính về 0,4 ở 85 %)
        — lớp gần quá nhỏ không tạo thị sai thấy được; quá lớn (cả khung là vật gần) cũng như mặt phẳng.
  Kèm MEP = tỉ lệ điểm ảnh có |∇độ sâu chuẩn hoá| > 0,02/px (mép độ sâu rõ) — chỉ ghi, không vào HD."""
import json, os, sys, hashlib, time
import numpy as np, cv2
import onnxruntime as ort
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP4_TMP", "/tmp/claude-0/mrp4/w"); MOI = "--moi" in sys.argv
os.environ["MRP2_TMP"] = TMP; os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrp2"))
import sau  # noqa: E402
sau.CAU_HINH = {}
OUT = os.path.join(TMP, "sau_moi" if MOI else "sau"); os.makedirs(OUT, exist_ok=True); sau.OUT = OUT
MEAN, STD = sau.MEAN, sau.STD


def tranh_moi(ma):
    c = json.load(open(os.path.join(ROOT, "reports", "mrp4", "anh", "chon.json")))
    im = Image.open(os.path.join(ROOT, c[ma])).convert("RGB")
    W, H = 1920, 1080; r = max(W / im.width, H / im.height); im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2; return im.crop((x0, y0, x0 + W, y0 + H))


if MOI: sau.dung.tranh = tranh_moi


def tho(sess, im):
    h, w = im.shape[:2]; HH = 518; WW = int(round(w * HH / h / 14)) * 14
    x = cv2.resize(im, (WW, HH), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255.0
    x = ((x - MEAN) / STD).transpose(2, 0, 1)[None]
    return sess.run(None, {sess.get_inputs()[0].name: x})[0][0]


def chi_so(raw, dn, m2):
    r = raw.astype(np.float64); p5, p95 = np.percentile(r, 5), np.percentile(r, 95)
    trai = float(max(p95 - p5, 0) / (abs(p95) + 1e-6))
    g = (m2 > 0); gan = float(g.mean())
    tach = float(np.median(dn[g]) - np.median(dn[~g])) if 0.005 < gan < 0.995 else 0.0
    f = min(gan / 0.12, 1.0) * (1.0 if gan <= 0.55 else max(0.4, 1 - 0.6 * (gan - 0.55) / 0.30))
    gx = cv2.Sobel(dn.astype(np.float32), cv2.CV_32F, 1, 0, ksize=3) / 8; gy = cv2.Sobel(dn.astype(np.float32), cv2.CV_32F, 0, 1, ksize=3) / 8
    mep = float((np.hypot(gx, gy) > 0.02).mean())
    return dict(HD=round(100 * trai * max(tach, 0) * f, 1), trai=round(trai, 3), tach=round(tach, 3), gan_pt=round(gan * 100, 1), mep_pt=round(mep * 100, 2))


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]; mdl = a[0]
    ids = a[1:] or (list(json.load(open(os.path.join(ROOT, "reports", "mrp4", "anh", "chon.json"))).keys()) if MOI
                    else json.load(open(os.path.join(ROOT, "scripts", "mrp3", "doan.json")))["l1"])
    sess = ort.InferenceSession(mdl, providers=["CPUExecutionProvider"])
    p = os.path.join(ROOT, "reports", "mrp4", "do_sau_moi.json" if MOI else "do_sau.json")
    out = json.load(open(p)) if os.path.exists(p) else {"tranh": {}}
    out.update({"model": "depth-anything-v2-small (onnx-community, rev 4472b73)", "sha256": hashlib.sha256(open(mdl, "rb").read()).hexdigest(),
                "cong_thuc": "HD = 100·TRAI·TACH·f(GAN) — xem docstring scripts/mrp4/sau.py"})
    t0 = time.time()
    for ma in ids:
        r = sau.lam(sess, ma)  # ghi depth/l0/l1/l2/mask (chuẩn hoá) như MR-P2/P3
        im = np.array(sau.dung.tranh(ma).convert("RGB")); raw = cv2.resize(tho(sess, im), (im.shape[1], im.shape[0]), interpolation=cv2.INTER_CUBIC)
        dn = cv2.imread(os.path.join(OUT, f"{ma}_depth.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 65535
        m2 = cv2.imread(os.path.join(OUT, f"{ma}_mask2.png"), 0)
        r.update(chi_so(raw, dn, m2)); out["tranh"][ma] = r; print(r, flush=True)
    out["giay_moi_tranh"] = round((time.time() - t0) / max(len(ids), 1), 1)
    json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
