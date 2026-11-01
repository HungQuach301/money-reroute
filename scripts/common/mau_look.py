# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/common/mau_look.py (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa)
"""[K-MỚI] Look màu cố định (R-119): chuyển Lab affine theo lab/mau/look-A.json — 0 USD.
  python3 scripts/common/mau_look.py do <video.mp4> [--mau 40]   → in mean/std nguồn gộp (Lab) của N khung rải đều
  python3 scripts/common/mau_look.py ap <anh_vao> <anh_ra> --nguon "m0,m1,m2,s0,s1,s2" [--k 0.6]
Trong bộ dựng: gọi ap_khung(bgr, nguon_mean, nguon_std, k) trên khung TRƯỚC khi vẽ chữ. Khe đêm/bão: k = k_dem_bao."""
import json, os, sys, subprocess, numpy as np, cv2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CFG = json.load(open(os.path.join(ROOT, "lab", "mau", "look-A.json")))
MD, SD = np.array(CFG["mean_dich"], np.float32), np.array(CFG["std_dich"], np.float32)

def ap_khung(bgr, mn, sn, k=CFG["k_mac_dinh"]):
    L = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    T = (L - mn) / sn * SD + MD
    return cv2.cvtColor(np.clip(L * (1 - k) + T * k, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

def do(video, n=40):
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video]))
    P = []
    for i in range(n):
        t = dur * (i + 0.5) / n
        b = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", video, "-frames:v", "1", "-vf", "scale=480:270", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"])
        f = np.frombuffer(b, np.uint8).reshape(270, 480, 3)
        P.append(cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32).reshape(-1, 3))
    P = np.concatenate(P); return P.mean(0), P.std(0)

if __name__ == "__main__":
    if sys.argv[1] == "do":
        n = int(sys.argv[sys.argv.index("--mau") + 1]) if "--mau" in sys.argv else 40
        m, s = do(sys.argv[2], n); print(",".join(f"{v:.3f}" for v in list(m) + list(s)))
    else:
        v = [float(x) for x in sys.argv[sys.argv.index("--nguon") + 1].split(",")]
        k = float(sys.argv[sys.argv.index("--k") + 1]) if "--k" in sys.argv else CFG["k_mac_dinh"]
        cv2.imwrite(sys.argv[3], ap_khung(cv2.imread(sys.argv[2]), np.array(v[:3], np.float32), np.array(v[3:], np.float32), k))
