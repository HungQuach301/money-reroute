#!/usr/bin/env python3
"""MR-P2 · Tờ QC mép lớp (0 USD): mỗi tranh L1, tìm 2 điểm trên mép lớp có chênh độ sâu lớn nhất, cắt 1:1 (360×240 ở 1080p)
ở khung đầu và khung cuối cảnh của biến thể A (thị sai lớn nhất) → reports/mrp2/xem/qc_mep.jpg. Mắt xem: quầng, rách, kéo dãn, vá lộ."""
import os, sys, json
import numpy as np, cv2
sys.argv = [sys.argv[0]]; sys.path.insert(0, os.path.dirname(__file__))
import dung_thu as P  # noqa: E402
rows = []
for i, c in enumerate(P.D.CANH):
    ma = c["ma"].split(":")[0]
    if c["lop"] != "L1" or ma not in P.CAM: continue
    if not any(a <= c["s"] < b for a, b in P.DOAN): continue
    L = P.lop(ma); d = L["d"]; m = (cv2.imread(os.path.join(P.SAU, f"{ma}_mask1.png"), 0) > 0).astype(np.uint8)
    edge = cv2.morphologyEx(m, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8)) > 0
    gx = np.abs(cv2.Sobel(d, cv2.CV_32F, 1, 0, ksize=7)) + np.abs(cv2.Sobel(d, cv2.CV_32F, 0, 1, ksize=7))
    sc = np.where(edge, gx, 0); sc[:150] = 0; sc[-150:] = 0; sc[:, :220] = 0; sc[:, -220:] = 0
    pts = []
    for _ in range(2):
        y, x = np.unravel_index(np.argmax(sc), sc.shape); pts.append((x, y)); sc[max(0, y - 300):y + 300, max(0, x - 400):x + 400] = 0
    row = []
    for t in (c["s"] + 0.02, c["e"] + P.T_HOA - 0.04):
        f = np.array(P.ve_l1(i, t, "A").convert("RGB"))[..., ::-1]
        cam = P.cam_luc(ma, min(max((t - c["s"]) / (c["e"] - c["s"] + P.T_HOA), 0), 1), i, "A")
        for x, y in pts:
            sx, sy = P.len_man(cam, x, y, float(d[y, x])); sx, sy = int(min(max(sx, 180), 1740)), int(min(max(sy, 120), 960))
            cr = f[sy - 120:sy + 120, sx - 180:sx + 180].copy(); row.append(cr)
    r = np.hstack(row); cv2.putText(r, ma, (6, 22), 0, 0.7, (0, 255, 255), 2); rows.append(r)
out = os.path.join(P.ROOT, "reports", "mrp2", "xem", "qc_mep.jpg")
cv2.imwrite(out, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 80]); print(out, len(rows))
