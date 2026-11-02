#!/usr/bin/env python3
"""MR-5 · Bản xem (0 USD, dựng lại được): reports/mr5/xem/
  to1s.jpg        tờ 1 s toàn bộ clip ĐÃ CHỌN của tập (V01–V16; V06/V12 từ MR-4): mỗi hàng một khe, cột 0,0 … 8,0 s (khung cuối 7,85 s)
  veo_ghep.mp4    16 clip đã chọn nối theo thứ tự khe, nhãn khe góc trên trái, không âm (720p)
  nhac.mp4        3 bản nhạc nối (N1 → N2 → N3, cách 2 s lặng) trên nền phổ tần — để nghe
Chọn clip: CHON dưới đây (khớp kết luận QC trong reports/mr5/veo/loi_veo.json)."""
import json, os, subprocess, sys
import cv2, numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
XEM = os.path.join(ROOT, "reports", "mr5", "xem"); os.makedirs(XEM, exist_ok=True)
CHON = json.load(open(os.path.join(ROOT, "reports", "mr5", "veo", "chon.json")))["chon"]


def khung(p, t, w=320):
    b = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", p, "-frames:v", "1", "-vf", f"scale={w}:-2",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True, check=True).stdout
    return cv2.imdecode(np.frombuffer(b, np.uint8), cv2.IMREAD_COLOR)


hang = []
for k, tep in CHON.items():
    p = os.path.join(ROOT, tep); o = []
    for i in range(9):
        f = khung(p, min(i, 7.85))
        cv2.rectangle(f, (0, 0), (150 if i == 0 else 48, 24), (0, 0, 0), -1)
        cv2.putText(f, f"{os.path.basename(tep)[:-4]} {i}s" if i == 0 else f"{i}s", (4, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        o.append(f)
    hang.append(np.hstack(o))
cv2.imwrite(os.path.join(XEM, "to1s.jpg"), np.vstack(hang), [cv2.IMWRITE_JPEG_QUALITY, 72])

ds = os.path.join(XEM, "veo_ds.txt"); tmp = []
for k, tep in CHON.items():
    o = os.path.join("/tmp", f"mr5x_{k}.mp4"); tmp.append(o)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(ROOT, tep), "-vf",
                    f"scale=1280:720,drawbox=x=0:y=0:w=230:h=40:color=black@0.6:t=fill,drawtext=text='{os.path.basename(tep)[:-4]}':x=10:y=8:fontsize=26:fontcolor=white",
                    "-an", "-c:v", "libx264", "-crf", "26", "-preset", "veryfast", "-pix_fmt", "yuv420p", o], check=True)
open(ds, "w").write("".join(f"file '{o}'\n" for o in tmp))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", ds, "-c", "copy", os.path.join(XEM, "veo_ghep.mp4")], check=True)
os.remove(ds)

N = [os.path.join(ROOT, "lab", "mr5", "nhac", f"{n}.mp3") for n in ("N1_mo", "N2_tang_dan", "N3_ket")]
fc = "[0:a]apad=pad_dur=2[a0];[1:a]apad=pad_dur=2[a1];[a0][a1][2:a]concat=n=3:v=0:a=1[a];[a]asplit[o][s];[s]showspectrum=s=1280x720:slide=scroll:legend=0[v]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *sum([["-i", n] for n in N], []), "-filter_complex", fc, "-map", "[v]", "-map", "[o]",
                "-c:v", "libx264", "-crf", "30", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "12", "-c:a", "aac", "-b:a", "192k",
                os.path.join(XEM, "nhac.mp4")], check=True)
print("xong", os.listdir(XEM))
