#!/usr/bin/env python3
"""MR-6 · Tìm toạ độ (điểm PDF) các dòng chứa cụm từ trên một trang PDF hồ sơ (pdftotext -bbox-layout, 0 USD).
  python3 scripts/mr6/tim_dong.py <pdf> <trang> "cụm 1" "cụm 2" …   → in dòng (y0,y1,x0,x1) + chữ"""
import re, subprocess, sys
pdf, p = sys.argv[1], sys.argv[2]
x = subprocess.run(["pdftotext", "-bbox-layout", "-f", p, "-l", p, pdf, "-"], capture_output=True, text=True).stdout
for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', x, re.S):
    words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', m.group(5))
    t = " ".join(w[4] for w in words)
    if len(sys.argv) == 3 or any(q.lower() in t.lower() for q in sys.argv[3:]):
        print(f"y {float(m.group(2)):.1f}-{float(m.group(4)):.1f} x {float(m.group(1)):.1f}-{float(m.group(3)):.1f} | {t}")
