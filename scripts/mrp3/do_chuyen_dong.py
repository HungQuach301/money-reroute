#!/usr/bin/env python3
"""MR-P3 · Đo "% thời lượng tranh có chuyển động thật" (0 USD). NGUỒN thước đo: scripts/mrp2/do_chuyen_dong.py bản 3 (repo này, main @ 33ce227):
luồng quang DIS giữa khung t − 0,4 s và t (480 px) → khớp MỘT homography (RANSAC 0,5 px) → phần dư từng điểm; khung "có chuyển động thật"
khi p90 phần dư VƯỢT khung cùng thời điểm của đối chứng phẳng quá 0,25 px. Đối chứng: P1 cho M1, P2 cho M2 và M3 (cùng dòng thời gian,
cùng máy quay, tranh phẳng, cùng thẻ/nhãn, không clip). goc: theo dựng (SHOT2: chỉ K2, K3 là clip; tranh còn lại tĩnh trượt).
Đổi so với MR-P2: dòng thời gian lấy từ reports/mrp3/dung_<bien>.json (điểm cắt khớp phách khác nhau giữa các mức).
  python3 scripts/mrp3/do_chuyen_dong.py      → reports/mrp3/do_chuyen_dong.json"""
import json, os, sys
import numpy as np, cv2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REP = os.path.join(ROOT, "reports", "mrp3"); FPS = 25; BUOC = 10; VUOT = 0.25
DIS = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)


def tl(bien):
    d = json.load(open(os.path.join(REP, f"dung_{bien}.json")))["dong_thoi_gian"]
    return sorted([x for x in d if x["s_ra"] is not None], key=lambda x: x["s_ra"])


def lop_luc(T, tau):
    k = [x for x in T if x["s_ra"] <= tau + 1e-6]
    if not k: return None, None, True
    c = k[-1]; return c["lop"], c["ma"].split(":")[0], (tau < c["s_ra"] + 0.5 and c["s_ra"] > 0.05)


def doc(f):
    cap = cv2.VideoCapture(f); fr = []
    while True:
        ok, x = cap.read()
        if not ok: break
        fr.append(cv2.cvtColor(cv2.resize(x, (480, 270), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY))
    return fr


def do(f, T):
    fr = doc(f); X, Y = np.meshgrid(np.arange(480, dtype=np.float32), np.arange(270, dtype=np.float32))
    vung = np.zeros((270, 480), bool); vung[14:208, 14:466] = True; gy, gx = np.mgrid[14:208:6, 14:466:6]; out = []
    for n in range(BUOC, len(fr)):
        tau = n / FPS; lp, ma, hoa = lop_luc(T, tau); _, ma0, hoa0 = lop_luc(T, (n - BUOC) / FPS)
        if lp is None or ma0 != ma or hoa or hoa0: continue
        fl = DIS.calc(fr[n - BUOC], fr[n], None)
        A = np.stack([gx.ravel(), gy.ravel()], 1).astype(np.float32); B = A + fl[gy.ravel(), gx.ravel()]
        Hm, _ = cv2.findHomography(A, B, cv2.RANSAC, 0.5)
        if Hm is None: Hm = np.eye(3)
        den = Hm[2, 0] * X + Hm[2, 1] * Y + Hm[2, 2]
        hx = (Hm[0, 0] * X + Hm[0, 1] * Y + Hm[0, 2]) / den - X; hy = (Hm[1, 0] * X + Hm[1, 1] * Y + Hm[1, 2]) / den - Y
        du = np.hypot(fl[..., 0] - hx, fl[..., 1] - hy)[vung]
        out.append({"tau": round(tau, 2), "lop": lp, "ma": ma, "p90": round(float(np.percentile(du, 90)), 3)})
    return out


def main():
    kq = {}
    for bien, dc in (("M1", "P1"), ("M2", "P2"), ("M3", "P2")):
        T = tl(bien); r = do(os.path.join(REP, "xem", f"{bien}.mp4"), T); p = {x["tau"]: x["p90"] for x in do(os.path.join(REP, "xem", f"{dc}.mp4"), tl(dc))}
        for x in r: x["vuot"] = x["p90"] - p.get(x["tau"], 0) > VUOT
        def t2(loc):
            rr = [x for x in r if loc(x)]
            return None if not rr else {"giay_do": round(len(rr) / FPS, 1), "vuot_P_pct": round(100 * sum(x["vuot"] for x in rr) / len(rr), 1)}
        kq[bien] = {"doi_chung": dc, "L1": t2(lambda x: x["lop"].startswith("L1")), "ca_doan": t2(lambda x: True),
                    "theo_tranh": {m: t2(lambda x, m=m: x["ma"] == m) for m in sorted({x["ma"] for x in r if x["lop"].startswith("L1")})}}
        print(bien, kq[bien]["L1"], kq[bien]["ca_doan"], flush=True)
    T = tl("M1"); dur = {}
    for i, x in enumerate(T):
        e = T[i + 1]["s_ra"] if i + 1 < len(T) else json.load(open(os.path.join(REP, "dung_M1.json")))["thoi_luong_s"]
        dur[x["lop"]] = dur.get(x["lop"], 0) + e - x["s_ra"]
    l1 = dur.get("L1", 0) + dur.get("L1-veo", 0)
    kq["goc"] = {"theo_dung": True, "L1_giay": round(l1, 1), "clip_giay": round(dur.get("L1-veo", 0), 1),
                 "vuot_P_pct_uoc": round(100 * dur.get("L1-veo", 0) / l1, 1)}
    kq["_dinh_nghia"] = __doc__.strip()
    json.dump(kq, open(os.path.join(REP, "do_chuyen_dong.json"), "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
