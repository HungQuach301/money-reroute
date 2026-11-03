#!/usr/bin/env python3
"""MR-P4 · Tờ so TRƯỚC/SAU cùng khung 1920×1080 (cắt như bản đăng) cho các tranh tạo lại: tranh | độ sâu | lớp gần (cam), kèm chỉ số HD (0 USD).
  MRP4_TMP=… python3 scripts/mrp4/to_truoc_sau.py   → reports/mrp4/xem/truoc_sau.jpg"""
import json, os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); TMP = os.environ.get("MRP4_TMP", "/tmp/claude-0/mrp4/w")
os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6")); sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6")); sys.path.insert(0, os.path.dirname(__file__))
import dung as D  # noqa: E402
R = os.path.join(ROOT, "reports", "mrp4"); C = json.load(open(os.path.join(R, "anh", "chon.json")))
cu = json.load(open(os.path.join(R, "do_sau.json")))["tranh"]; moi = json.load(open(os.path.join(R, "do_sau_moi.json")))["tranh"]


def o(im, sd, ma, w=300, h=169):
    dep = cv2.imread(os.path.join(TMP, sd, f"{ma}_depth.png"), -1).astype(np.float32) / 65535
    dc = Image.fromarray(cv2.applyColorMap((cv2.resize(dep, (w, h)) * 255).astype(np.uint8), cv2.COLORMAP_INFERNO)[..., ::-1])
    m = cv2.resize(cv2.imread(os.path.join(TMP, sd, f"{ma}_mask2.png"), 0), (w, h)); a = np.array(im.resize((w, h))).astype(float)
    a[m > 0] = a[m > 0] * 0.5 + np.array([255, 80, 0]) * 0.5
    return [im.resize((w, h)), dc, Image.fromarray(a.astype(np.uint8))]


def tranh_moi(ma):
    """cắt phủ 1920×1080 giữa khung — như dung.tranh() của bản đăng (và scripts/mrp4/sau.py)."""
    im = Image.open(os.path.join(ROOT, C[ma])).convert("RGB"); W, H = 1920, 1080
    r = max(W / im.width, H / im.height); im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2; return im.crop((x0, y0, x0 + W, y0 + H))


def main():
    ks = sorted(C, key=lambda k: cu[k]["HD"]); w, h = 300, 169
    out = Image.new("RGB", (6 * w + 10, len(ks) * (h + 22)), "black"); d = ImageDraw.Draw(out)
    for n, k in enumerate(ks):
        y = n * (h + 22)
        nm = tranh_moi(k)
        for j, x in enumerate(o(D.tranh(k), "sau", k) + o(nm, "sau_moi", k)):
            out.paste(x, (j * w + (10 if j >= 3 else 0), y + 20))
        d.text((4, y + 4), f"{k} TRUOC  HD {cu[k]['HD']}  tach {cu[k]['tach']}  gan {cu[k]['gan_pt']}%", fill="white")
        d.text((3 * w + 14, y + 4), f"{k} SAU  HD {moi[k]['HD']}  tach {moi[k]['tach']}  gan {moi[k]['gan_pt']}%", fill=(255, 200, 80))
    os.makedirs(os.path.join(R, "xem"), exist_ok=True); out.save(os.path.join(R, "xem", "truoc_sau.jpg"), quality=82); print(out.size)


if __name__ == "__main__":
    main()
