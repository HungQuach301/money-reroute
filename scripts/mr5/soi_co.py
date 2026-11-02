#!/usr/bin/env python3
"""MR-5 · Tờ soi cờ mặt YuNet (0 USD): cắt vùng bị cờ (toạ độ 960×540 → ×2, nới 60 %) ở tối đa 12 thời điểm rải đều,
ghép thành một tờ để mắt xác nhận báo nhầm/thật.  python3 scripts/mr5/soi_co.py V02_l1  → reports/mr5/veo/V02_l1_co.jpg"""
import json, os, subprocess, sys
import cv2, numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ten = sys.argv[1]; RA = os.path.join(ROOT, "reports", "mr5", "veo")
q = json.load(open(os.path.join(RA, ten + "_qc.json"))); hits = q["mat_yunet"]
if not hits: print(ten, "0 cờ"); sys.exit(0)
step = max(1, len(hits) // 12); chon = hits[::step][:12]; o = []
for h in chon:
    b = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{h['t']:.3f}", "-i", os.path.join(ROOT, q["tep"]), "-frames:v", "1",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True, check=True).stdout
    f = cv2.imdecode(np.frombuffer(b, np.uint8), cv2.IMREAD_COLOR)
    x, y, w, hh = [v * 2 for v in h["o"]]; cx, cy = x + w / 2, y + hh / 2; s = max(w, hh) * 1.6 + 40
    x0, y0 = int(max(0, cx - s / 2)), int(max(0, cy - s / 2)); x1, y1 = int(min(1920, cx + s / 2)), int(min(1080, cy + s / 2))
    c = cv2.resize(f[y0:y1, x0:x1], (240, 240))
    cv2.putText(c, f"{h['t']:.2f}s {h['diem']:.2f}", (4, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2); o.append(c)
while len(o) % 6: o.append(np.zeros_like(o[0]))
cv2.imwrite(os.path.join(RA, ten + "_co.jpg"), np.vstack([np.hstack(o[i:i + 6]) for i in range(0, len(o), 6)]), [cv2.IMWRITE_JPEG_QUALITY, 85])
print(ten, len(hits), "cờ →", ten + "_co.jpg")
