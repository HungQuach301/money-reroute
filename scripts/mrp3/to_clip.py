#!/usr/bin/env python3
"""MR-P3 · Tờ 0,5 s cho clip (V8 mắt xem): mỗi clip một hàng 9 ô (0–4 s) 384×216. 0 USD.
  python3 scripts/mrp3/to_clip.py <ra.jpg> <clip.mp4> …"""
import sys, cv2, numpy as np
rows = []
for f in sys.argv[2:]:
    cap = cv2.VideoCapture(f); fps = cap.get(cv2.CAP_PROP_FPS) or 24; n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); r = []
    for k in range(9):
        cap.set(cv2.CAP_PROP_POS_FRAMES, min(int(k * 0.5 * fps), n - 1)); ok, x = cap.read()
        x = cv2.resize(x, (384, 216)) if ok else np.zeros((216, 384, 3), np.uint8)
        cv2.putText(x, f"{k*0.5:.1f}s", (4, 210), 0, 0.5, (0, 255, 255), 1); r.append(x)
    h = np.hstack(r); cv2.putText(h, f.split("/")[-1], (4, 18), 0, 0.55, (0, 255, 255), 2); rows.append(h)
cv2.imwrite(sys.argv[1], np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 82])
