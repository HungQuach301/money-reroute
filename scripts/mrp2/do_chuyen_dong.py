#!/usr/bin/env python3
"""MR-P2 · Đo "tỷ lệ thời lượng có chuyển động thật trong khung" (0 USD).
  python3 scripts/mrp2/do_chuyen_dong.py goc A B C
Định nghĩa (bản 2 — bản 1 dùng luồng quang Farneback − affine KHÔNG hiệu chỉnh được: bản gốc chỉ trượt/phóng vẫn ra 71 %):
khung t (thu 480×270, xám) so với khung t − 0,4 s CÙNG cảnh, ngoài cửa sổ hoà cảnh. Khớp MỘT homography (ORB + RANSAC 1 px) —
mọi chuyển động của một ảnh phẳng (trượt, phóng, lia, nghiêng = "ảnh tĩnh trượt") được giải thích hết. Phần dư = |khung t − khung cũ
đã khớp| (làm mờ 5 px), bỏ dải nhãn/nguồn dưới. (Bản 3, dùng:) luồng quang DIS giữa t − 0,4 s và t → khớp MỘT homography vào luồng (RANSAC 0,5 px) → phần dư từng điểm
(px, ở 480 px). Khung "có chuyển động thật" khi phân vị 90 phần dư > 0,5 px. GIỚI HẠN: thẻ chữ/nhãn đứng yên trên ảnh trượt
và nhiễu luồng cũng tạo dư → luôn đọc kèm đối chứng P (cùng máy quay A trên tranh phẳng = ảnh tĩnh trượt thuần): phần VƯỢT P
mới là chuyển động thật. Bảng ghi cả p90/p98 × 3 ngưỡng.
Báo theo lớp (L1 tranh / L2 đồ hoạ) theo shot2.json. Ra: reports/mrp2/do_chuyen_dong.json."""
import json, os, sys
import numpy as np, cv2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FPS = 25
CFG = json.load(open(os.path.join(os.path.dirname(__file__), "canh.json")))
DOAN = [(round(a * FPS - 0.5) / FPS, round(b * FPS) / FPS) for a, b in CFG["doan"]]
CANH = json.load(open(os.path.join(ROOT, "reports", "mr6", "shot2.json")))["canh"]


def t_goc(tau):
    for a, b in DOAN:
        if tau < b - a: return a + tau
        tau -= b - a
    return DOAN[-1][1]


def lop_luc(t):
    i = max(j for j, c in enumerate(CANH) if c["s"] <= t + 1e-6); c = CANH[i]
    hoa = t < c["s"] + 0.5 and c["s"] > 0
    return c["lop"], c["ma"].split(":")[0], hoa


BUOC = 10  # so khung t với t − 0,4 s
DIS = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)


def do(f):
    cap = cv2.VideoCapture(f); fr = []
    while True:
        ok, x = cap.read()
        if not ok: break
        fr.append(cv2.cvtColor(cv2.resize(x, (480, 270), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY))
    X, Y = np.meshgrid(np.arange(480, dtype=np.float32), np.arange(270, dtype=np.float32))
    vung = np.zeros((270, 480), bool); vung[14:208, 14:466] = True  # bỏ dải nhãn/nguồn dưới + mép
    gy, gx = np.mgrid[14:208:6, 14:466:6]
    out = []
    for n in range(BUOC, len(fr)):
        tau = n / FPS; t = t_goc(tau); lp, ma, hoa = lop_luc(t); _, ma0, hoa0 = lop_luc(t_goc((n - BUOC) / FPS))
        if ma0 != ma or hoa or hoa0: continue  # cùng cảnh, ngoài hoà cảnh
        fl = DIS.calc(fr[n - BUOC], fr[n], None)
        A = np.stack([gx.ravel(), gy.ravel()], 1).astype(np.float32); B = A + fl[gy.ravel(), gx.ravel()]
        Hm, _ = cv2.findHomography(A, B, cv2.RANSAC, 0.5)
        if Hm is None: Hm = np.eye(3)
        den = Hm[2, 0] * X + Hm[2, 1] * Y + Hm[2, 2]
        hx = (Hm[0, 0] * X + Hm[0, 1] * Y + Hm[0, 2]) / den - X; hy = (Hm[1, 0] * X + Hm[1, 1] * Y + Hm[1, 2]) / den - Y
        du = np.hypot(fl[..., 0] - hx, fl[..., 1] - hy)[vung]
        out.append({"tau": round(tau, 2), "lop": lp, "ma": ma, "p90": round(float(np.percentile(du, 90)), 3), "p98": round(float(np.percentile(du, 98)), 3)})
    return out


NG = ("p90", 0.5)  # ngưỡng: phân vị 90 phần dư > 0,5 px (ở 480 px) — báo kèm đối chứng P làm mức nền


def tom(rows, loc):
    r = [x for x in rows if loc(x)]
    if not r: return None
    o = {"giay": round(len(r) / FPS, 1)}
    for k in ("p90", "p98"):
        o[f"{k}_tb"] = round(float(np.mean([x[k] for x in r])), 3)
        for q in (0.5, 1.0, 1.5):
            o[f"pct_{k}>{q}"] = round(100 * len([x for x in r if x[k] > q]) / len(r), 1)
    o["co_chuyen_dong_that_pct"] = o[f"pct_{NG[0]}>{NG[1]}"]
    return o




VUOT = 0.25  # px: khung X "có chuyển động thật" khi p90(X) > p90(P cùng khung) + 0,25 px


def main():
    p = os.path.join(ROOT, "reports", "mrp2", "do_chuyen_dong.json")
    kq = {}; rows = {}
    for b in ["P"] + [x for x in sys.argv[1:] if x != "P"]:
        rows[b] = do(os.path.join(ROOT, "reports", "mrp2", "xem", f"{b}.mp4"))
    P = {x["tau"]: x["p90"] for x in rows["P"]}
    for b, rr in rows.items():
        for x in rr: x["vuot_P"] = (x["p90"] - P.get(x["tau"], 0)) > VUOT
        def t2(loc):
            r = [x for x in rr if loc(x)]
            if not r: return None
            o = tom(r, lambda x: True); o["vuot_P_pct"] = round(100 * len([x for x in r if x["vuot_P"]]) / len(r), 1); return o
        kq[b] = {"ca_doan_tru_hoa_canh": t2(lambda x: True), "L1": t2(lambda x: x["lop"].startswith("L1")), "L2": t2(lambda x: x["lop"] == "L2"),
                 "theo_tranh": {m: t2(lambda x, m=m: x["ma"] == m) for m in CFG["l1"]}}
        print(b, "L1 vượt P %", kq[b]["L1"]["vuot_P_pct"], "| cả đoạn", kq[b]["ca_doan_tru_hoa_canh"]["vuot_P_pct"])
    kq["_dinh_nghia"] = __doc__.split("\n", 2)[2].strip()
    kq["_chi_so_chinh"] = ("vuot_P_pct = % thời lượng (ngoài hoà cảnh) mà phân vị 90 phần dư luồng sau khớp homography vượt khung cùng thời điểm "
                           "của đối chứng P quá 0,25 px. 'goc' có camera khác P nên chỉ số này không áp cho goc; L1 của goc trong đoạn này toàn "
                           "tranh tĩnh trượt (SHOT2) → chuyển động thật = 0 % theo dựng.")
    json.dump(kq, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
