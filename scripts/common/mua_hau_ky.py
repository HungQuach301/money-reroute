# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/common/mua_hau_ky.py (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa)
"""[K-MỚI · MC-2] MƯA HẬU KỲ dùng chung (CONG-THUC 1.4 §1.9 V6 bổ sung R-141) — 0 USD. Viết ở MC-2 (PE-4 chưa có trên main lúc viết); PE-4 và các tập sau dùng lại.
Lý do: Veo 3.1 Lite vẽ mưa toàn cảnh time-lapse thành VỆT DÀI dọc (MC-1 A2b/A7, Petra A3/C1/D5b) dù đổi lời → khe mưa toàn cảnh sinh "overcast, wet stone, NO rain
falling", mưa thêm ở đây.
Hai lớp, cùng tất định theo (seed, số khung) → dựng lại ra đúng khung cũ:
  1. HẠT MẢNH: 3 lớp sâu (xa/giữa/gần), mỗi hạt là đoạn ngắn 1 px (dài 5–16 px ở 1080p — ngắn hơn hẳn vệt Veo 60–300 px), nghiêng nhẹ theo gió, độ mờ thấp (α 0,10–0,28),
     làm mềm Gauss 0,6 px, cộng kiểu screen; lớp xa nhỏ và nhạt nhất. Vị trí giải tích: (x0 + vx·t) mod W, (y0 + vy·t) mod H — không trạng thái.
  2. MÀN HƠI NƯỚC: kết cấu nhiễu tần thấp (fbm 4 bậc) trôi ngang chậm, α 0,06–0,20 theo mức, nâng nhẹ vùng tối + giảm bão hoà 6–14 % (không khí ẩm, xa mờ).
Mức: nhe (mưa phùn) · vua · lon (mưa lớn El Niño). Vào/ra mềm 0,6 s ở hai đầu khoảng mưa.
  from mua_hau_ky import Mua; m = Mua("vua", seed=7); fr = m.ap(fr_bgr_uint8, t_giay, he_so=1.0)
  python3 scripts/common/mua_hau_ky.py vao.mp4 ra.mp4 --muc vua [--t0 0 --t1 99] [--seed 7]   (thử trên clip; giữ nguyên số khung)"""
import argparse, subprocess, json
import cv2, numpy as np

MUC = {  # số hạt (ở 1920×1080) theo 3 lớp sâu, α hạt, α màn, giảm bão hoà
    "nhe": dict(n=(1600, 900, 300), a=(0.22, 0.30, 0.38), man=0.14, sat=0.08, toi=0.04),
    "vua": dict(n=(3000, 1700, 600), a=(0.28, 0.38, 0.48), man=0.22, sat=0.12, toi=0.07),
    "lon": dict(n=(5000, 2800, 1000), a=(0.32, 0.45, 0.58), man=0.32, sat=0.16, toi=0.10),
}
# mỗi lớp: (dài px, tốc độ rơi px/s, độ dày) ở 1080p
LOP = ((6, 520, 1), (11, 900, 1), (20, 1500, 1))


def _fbm(h, w, seed):
    r = np.random.default_rng(seed); out = np.zeros((h, w), np.float32); amp = 1.0; tot = 0.0
    for o in range(4):
        sh = max(2, h // (64 >> o)); sw = max(2, w // (64 >> o))
        n = cv2.resize(r.random((sh, sw)).astype(np.float32), (w, h), interpolation=cv2.INTER_CUBIC)
        out += amp * n; tot += amp; amp *= 0.5
    out /= tot; out = (out - out.min()) / (out.max() - out.min() + 1e-6)
    return cv2.GaussianBlur(out, (0, 0), 6)


class Mua:
    def __init__(self, muc="vua", seed=7, W=1920, H=1080, gio=0.10):
        self.c = MUC[muc]; self.W, self.H = W, H; s = H / 1080.0; self.s = s; r = np.random.default_rng(seed)
        self.lop = []
        for i, (dai, v, day) in enumerate(LOP):
            n = int(self.c["n"][i] * (W * H) / (1920 * 1080))
            self.lop.append(dict(x=r.random(n) * W, y=r.random(n) * H, v=v * s * (0.85 + 0.3 * r.random(n)), dai=dai * s, a=self.c["a"][i], day=day))
        self.gio = gio   # độ nghiêng (dx/dy)
        self.man = _fbm(H // 2, W // 2 + W // 4, seed + 1)   # rộng hơn khung để trôi ngang

    def _nhan(self, dai):
        n = max(3, int(round(dai)) | 1); k = np.zeros((n, n), np.float32); c = n // 2
        cv2.line(k, (int(round(c - c * self.gio)), 0), (int(round(c + c * self.gio)), n - 1), 1.0, 1, cv2.LINE_AA)
        return k / k.max()

    def lop_hat(self, t):
        """Chấm điểm hạt (giải tích theo t) rồi tích chập nhân đoạn ngắn nghiêng — nhanh hơn vẽ từng đường."""
        L = np.zeros((self.H, self.W), np.float32)
        for l in self.lop:
            y = ((l["y"] + l["v"] * t) % self.H).astype(np.int32); x = ((l["x"] + l["v"] * t * self.gio) % self.W).astype(np.int32)
            P = np.zeros_like(L); P[y, x] = 1.0
            if "k" not in l: l["k"] = self._nhan(l["dai"])
            L = np.maximum(L, np.clip(cv2.filter2D(P, -1, l["k"]), 0, 1) * l["a"])
        return cv2.GaussianBlur(L, (0, 0), 0.6 * self.s)

    def lop_man(self, t):
        h, w = self.man.shape; off = int((t * 18) % (w - self.W // 2))
        m = cv2.resize(self.man[:, off:off + self.W // 2], (self.W, self.H), interpolation=cv2.INTER_LINEAR)
        doc = np.linspace(0.75, 1.0, self.H, dtype=np.float32)[:, None]   # dày hơn ở phần trên (xa)
        m = np.clip((m - 0.35) / 0.5, 0, 1) ** 1.3   # tấm màn mưa có cấu trúc (dày/mỏng), không phủ đều
        return np.clip(m * doc, 0, 1) * self.c["man"] + 0.25 * self.c["man"]

    def ap(self, fr, t, he_so=1.0):
        """fr: BGR uint8 (H×W×3); he_so 0..1 (vào/ra mềm)."""
        if he_so <= 0: return fr
        if fr.shape[1] != self.W or fr.shape[0] != self.H: raise ValueError("cỡ khung khác cỡ đã khởi tạo")
        f = fr.astype(np.float32) / 255.0
        hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV).astype(np.float32); hsv[..., 1] *= 1 - self.c["sat"] * he_so
        f = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32) / 255.0
        f = f * (1 - self.c["toi"] * he_so)   # trời mưa tối hơn một chút
        man = (self.lop_man(t) * he_so)[..., None]; xam = np.array([0.80, 0.80, 0.78], np.float32)
        f = f * (1 - man) + xam * man
        h = (self.lop_hat(t) * he_so)[..., None]; mau = np.array([0.93, 0.95, 0.96], np.float32)
        f = 1 - (1 - f) * (1 - h * mau)   # screen
        return np.clip(f * 255 + 0.5, 0, 255).astype(np.uint8)


def he_so(t, t0, t1, mem=0.6):
    if t < t0 or t > t1: return 0.0
    return float(min(1.0, (t - t0) / mem if t0 > 0 else 1.0, (t1 - t) / mem))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("vao"); ap.add_argument("ra"); ap.add_argument("--muc", default="vua"); ap.add_argument("--t0", type=float, default=0)
    ap.add_argument("--t1", type=float, default=1e9); ap.add_argument("--seed", type=int, default=7); a = ap.parse_args()
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate", "-of", "json", a.vao],
                                   capture_output=True, text=True).stdout)["streams"][0]
    W, H = pr["width"], pr["height"]; fps = eval(pr["r_frame_rate"]); m = Mua(a.muc, a.seed, W, H)
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.vao, "-an", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "16",
                            "-pix_fmt", "yuv420p", a.ra], stdin=subprocess.PIPE)
    i = 0
    while True:
        b = dec.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        t = i / fps; fr = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        enc.stdin.write(m.ap(fr, t, he_so(t, a.t0, a.t1)).tobytes()); i += 1
    enc.stdin.close(); enc.wait(); print(a.ra, i, "khung")
