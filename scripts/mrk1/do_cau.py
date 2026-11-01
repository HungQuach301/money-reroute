"""[MR-K1] Đo cầu đề tài trên YouTube cho kho đề tài. Khuôn: scripts/mr1/do_cau.py (MR-1), đổi: truy vấn đọc từ
scripts/mrk1/truy_van.json; chạy được cho một số vụ chọn; ghi reports/mrk1/do-cau/<vu>.json.
Mỗi truy vấn: 1 search.list (type=video, maxResults=50, order=relevance) + 1 videos.list (part=statistics,snippet).
Trần qua scripts/cp/budget.py (MR_PHIEN=mrk1: youtube_units 2000, search.list ≤ 50 lượt) — check_yt() trước, charge() sau, 402 → DỪNG.
Tiêu đề chỉ dùng TRONG BỘ NHỚ để đánh dấu "khop" (tiêu đề chứa ít nhất một từ khoá), KHÔNG lưu. Lưu: id video, id kênh, ngày đăng, lượt xem, khop.
  MR_PHIEN=mrk1 python3 scripts/mrk1/do_cau.py stanford-sib petters-pci     # các vụ chọn
  MR_PHIEN=mrk1 python3 scripts/mrk1/do_cau.py                              # mọi vụ chưa đo"""
import json, os, sys, statistics, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "mr1")); from yt import goi
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "reports", "mrk1", "do-cau"); os.makedirs(OUT, exist_ok=True)
assert os.environ.get("MR_PHIEN") == "mrk1", "đặt MR_PHIEN=mrk1"
TV = json.load(open(os.path.join(HERE, "truy_van.json")))
HOM_NAY = datetime.datetime.now(datetime.timezone.utc)
chon = sys.argv[1:] or [v for v in TV if not os.path.exists(os.path.join(OUT, v + ".json"))]
for vu in chon:
    kq = {"vu": vu, "ngay_do": HOM_NAY.date().isoformat(), "truy_van": []}
    for q, khoa in TV[vu]:
        c1, s = goi("search.list", "part=snippet&type=video&maxResults=50&order=relevance&q=" + urllib.parse.quote(q))
        ids = [it["id"]["videoId"] for it in s.get("items", []) if it.get("id", {}).get("videoId")]
        c2, v = goi("videos.list", "part=statistics,snippet&id=" + ",".join(ids)) if ids else (None, {"items": []})
        rows = []
        for it in v.get("items", []):
            td = it["snippet"]["title"].lower()
            rows.append({"id": it["id"], "kenh": it["snippet"]["channelId"], "ngay": it["snippet"]["publishedAt"][:10],
                         "xem": int(it.get("statistics", {}).get("viewCount", 0)), "khop": any(k in td for k in khoa)})
        m = [r for r in rows if r["khop"]]
        def tuoi(r): return (HOM_NAY - datetime.datetime.fromisoformat(r["ngay"] + "T00:00:00+00:00")).days
        top = sorted(m, key=lambda r: -r["xem"])[:3]
        tom = {"q": q, "khoa": khoa, "http": [c1, c2], "so_tra_ve": len(rows), "so_khop_tieu_de": len(m),
               "tong_xem_khop": sum(r["xem"] for r in m), "trung_vi_xem_khop": int(statistics.median([r["xem"] for r in m])) if m else 0,
               "max_xem_khop": max([r["xem"] for r in m], default=0), "so_kenh_khop": len({r["kenh"] for r in m}),
               "khop_12_thang": sum(1 for r in m if tuoi(r) <= 365), "khop_moi_nhat": max([r["ngay"] for r in m], default=None),
               "khop_100k": sum(1 for r in m if r["xem"] >= 100_000), "top3_id": [r["id"] for r in top], "videos": rows}
        kq["truy_van"].append(tom)
        print(vu, json.dumps({k: x for k, x in tom.items() if k != "videos"}, ensure_ascii=False))
    json.dump(kq, open(os.path.join(OUT, vu + ".json"), "w"), ensure_ascii=False, indent=1)
