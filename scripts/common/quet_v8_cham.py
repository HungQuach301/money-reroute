# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/common/quet_v8_cham.py (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa)
"""[K-MỚI · K-V8] Chấm bộ quét V8 (scripts/common/quet_v8.py) trên LỖI THẬT ĐÃ BIẾT (nguồn: NHAT-KY R-139, R-140, R-141).
Bắt = có ít nhất một đoạn nghi (cột bất kỳ) chồng cửa sổ lỗi ± 1 s; ghi thêm cột nào bắt. Báo nhầm = đoạn nghi không chồng lỗi nào đã biết
(kể cả "lỗi khác đã biết") — số này là TRẦN báo nhầm; phiếu mắt `mat.json` (khe, cột, giây, kết luận "lỗi…" / "nghi lỗi…" / "báo nhầm…") tách ra.
  python3 scripts/common/quet_v8_cham.py <kq_pe2.json> <kq_pe3.json> <kq_mc1.json> [--mat reports/kv8/mat.json] --ra reports/kv8/cham.json"""
import argparse, json

# (phim, khe, giây đầu, giây cuối, cột kỳ vọng, mô tả, nhóm) — nhóm "chinh" = 9 lỗi lệnh K-V8; "cung_clip" = cùng clip có trong PE-2; "khac" = lỗi khác đã biết
LOI = [
    ("pe3", "A3", 35.2, 36.8, {4, 2, 1}, "màn vệt nâu dọc phủ kín khung", "chinh"),
    ("pe3", "C1", 247.8, 249.4, {1, 2}, "mưa vệt + bụi nâu bùng khắp thung lũng", "chinh"),
    ("pe3", "D2", 314.0, 316.0, {3, 2}, "vách đá biến dạng thành cột nhọn + vệt cam bùng", "chinh"),
    ("pe3", "D5b", 349.5, 351.0, {1}, "mưa vệt dài", "chinh"),
    ("mc1", "A2b", 43.0, 45.0, {1}, "mưa vệt dọc", "chinh"),
    ("mc1", "A7", 169.0, 171.0, {1}, "mưa vệt dọc", "chinh"),
    ("pe2", "CA4", 106.5, 107.3, {5}, "người, lạc đà hiện mờ dần", "chinh"),
    ("pe2", "B1", 162.0, 168.0, {5}, "đoàn lạc đà nhoè (khe dãn 1,25×)", "chinh"),
    ("pe2", "B4", 190.0, 194.0, {2}, "bụi bùng như nổ từ Qasr al-Bint", "chinh"),
    ("pe2", "C1", 247.8, 249.4, {1, 2}, "cùng clip PE-2 C1", "cung_clip"),
    ("pe2", "D2", 314.0, 316.0, {3, 2}, "cùng clip PE-2 D2", "cung_clip"),
    ("pe2", "D5b", 349.5, 351.0, {1}, "cùng clip PE-2 D5b", "cung_clip"),
    ("pe3", "A7", 108.4, 115.9, set(), "bông tuyết to sát máy (nhẹ, R-141)", "khac"),
    ("pe2", "A7", 108.4, 115.9, set(), "bông tuyết (cùng clip? PE-2 Omni)", "khac"),
    ("mc1", "H1", 0.0, 6.0, set(), "nhoè 1,0–1,5 s (R-141)", "khac"),
    ("mc1", "TT1", 88.5, 94.5, set(), "đoàn llama gần như đứng (R-141)", "khac"),
    ("mc1", "CW2", 65.0, 67.0, set(), "sợi dây thẳng đứng treo từ mép trên 1:06 (R-141)", "khac"),
] + [("pe2", k, None, None, {5}, "khe Omni PE-1 dãn 1,5× — người trôi (R-139)", "khac") for k in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9")] + [
    ("pe2", "C2", 253.6, 261.0, set(), "vá ảnh tĩnh do 402 (R-139)", "khac"),
    ("pe2", "C3", 267.0, 274.5, set(), "vá ảnh tĩnh do 402 (R-139)", "khac"),
    ("pe2", "C4", 268.0, 270.5, set(), "4:29 khung khoá K1_446 hỏng, màu bệt (R-139)", "khac"),
]


def chong(q, phim, l):
    if l[0] != phim or l[1] != q["_khe"]: return False
    if l[2] is None: return True
    a = q["giay"]; b = a + q["dai_s"]
    return a <= l[3] + 1.0 and b >= l[2] - 1.0


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pe2"); ap.add_argument("pe3"); ap.add_argument("mc1")
    ap.add_argument("--mat", default=None); ap.add_argument("--ra", required=True); a = ap.parse_args()
    mat = json.load(open(a.mat)) if a.mat else []
    K = {}
    for phim, p in (("pe2", a.pe2), ("pe3", a.pe3), ("mc1", a.mc1)):
        for path in p.split(","):
            for r in json.load(open(path))["khe"]:
                for q in r["nghi"]:
                    q = dict(q, _khe=r["khe"]); K.setdefault(phim, []).append(q)
    out = {"loi": [], "nghi_ngoai": [], "tong": {}}
    for l in LOI:
        hit = [q for q in K.get(l[0], []) if chong(q, l[0], l)]
        out["loi"].append(dict(phim=l[0], khe=l[1], tu=l[2], den=l[3], mo_ta=l[5], nhom=l[6], bat=bool(hit), cot_bat=sorted({q["cot"] for q in hit}),
                               cot_ky_vong=sorted(l[4]), trung_cot_ky_vong=bool({q["cot"] for q in hit} & l[4]), dau=[(q["cot"], q["tu"]) for q in hit]))
    for phim, qs in K.items():
        for q in qs:
            if any(chong(q, phim, l) for l in LOI): continue
            m = next((x for x in mat if x["phim"] == phim and x["khe"] == q["_khe"] and x["cot"] == q["cot"] and abs(x["giay"] - q["giay"]) < 1.5), None)
            out["nghi_ngoai"].append(dict(phim=phim, khe=q["_khe"], cot=q["cot"], tu=q["tu"], dai_s=q["dai_s"], mo_ta=q["mo_ta"], mat=(m or {}).get("ket_luan"), to=q.get("to")))
    chinh = [x for x in out["loi"] if x["nhom"] == "chinh"]
    ngoai = out["nghi_ngoai"]
    for c in (1, 2, 3, 4, 5):
        n = [x for x in ngoai if x["cot"] == c]
        out["tong"][f"c{c}"] = dict(nghi_ngoai=len(n), mat_xac_nhan_loi=sum(1 for x in n if (x["mat"] or "").startswith("lỗi")),
                                    nghi_loi_moi=sum(1 for x in n if (x["mat"] or "").startswith("nghi lỗi")),
                                    bao_nham=sum(1 for x in n if not (x["mat"] or "").startswith(("lỗi", "nghi lỗi"))),
                                    bat_chinh=sum(1 for x in chinh if c in x["cot_bat"]), ky_vong_chinh=sum(1 for x in chinh if c in x["cot_ky_vong"]))
    out["tong"]["bat_chinh"] = f"{sum(x['bat'] for x in chinh)}/{len(chinh)}"
    out["tong"]["bat_dung_cot"] = f"{sum(x['trung_cot_ky_vong'] for x in chinh)}/{len(chinh)}"
    cc = [x for x in out["loi"] if x["nhom"] == "cung_clip"]; out["tong"]["bat_cung_clip"] = f"{sum(x['bat'] for x in cc)}/{len(cc)}"
    json.dump(out, open(a.ra, "w"), ensure_ascii=False, indent=1)
    for x in out["loi"]: print(("BẮT " if x["bat"] else "LỌT ") + f"{x['phim']} {x['khe']} {x['mo_ta']} cột {x['cot_bat']} (kỳ vọng {x['cot_ky_vong']})")
    print(json.dumps(out["tong"], ensure_ascii=False))


if __name__ == "__main__":
    main()
