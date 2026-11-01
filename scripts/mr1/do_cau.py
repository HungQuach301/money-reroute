"""[MR-1] Đo cầu đề tài trên YouTube (bước 6). Mỗi truy vấn: 1 search.list (type=video, maxResults=50, order=relevance)
+ 1 videos.list (part=statistics,snippet) cho các id trả về. Tiêu đề chỉ dùng TRONG BỘ NHỚ để đánh dấu "khop" (tiêu đề chứa
cụm khoá), KHÔNG lưu. Lưu: id video, id kênh, ngày đăng, lượt xem, khop → reports/mr1/do-cau/<vu>.json.
  MR_PHIEN=mr1 python3 scripts/mr1/do_cau.py            # 3 vụ
  MR_PHIEN=mr1 python3 scripts/mr1/do_cau.py chu-de     # mốc thể loại"""
import json, os, sys, statistics, urllib.parse, datetime
sys.path.insert(0, os.path.dirname(__file__)); from yt import goi
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "reports", "mr1", "do-cau"); os.makedirs(OUT, exist_ok=True)
TRUY_VAN = {
    "heartland-hanes": [("Shan Hanes", ["hanes"]), ("Heartland Tri-State Bank", ["heartland"])],
    "woodbridge-shapiro": [("Woodbridge Ponzi", ["woodbridge"]), ("Robert Shapiro Woodbridge", ["woodbridge", "shapiro"])],
    "1inmm-horwitz": [("Zachary Horwitz", ["horwitz"]), ("1inMM Capital", ["1inmm"])],
}
# Truy vấn chủ đề chung (mốc so sánh cầu của thể loại, không phải của vụ). Chạy: do_cau.py chu-de
CHU_DE = {"chu-de": [("pig butchering scam", ["pig butcher"]), ("Ponzi scheme retirees", ["ponzi"]), ("Hollywood Ponzi scheme", ["ponzi"])]}
if len(sys.argv) > 1 and sys.argv[1] == "chu-de": TRUY_VAN = CHU_DE
HOM_NAY = datetime.datetime(2026, 11, 1, tzinfo=datetime.timezone.utc)
for vu, qs in TRUY_VAN.items():
    kq = {"vu": vu, "ngay_do": HOM_NAY.date().isoformat(), "truy_van": []}
    for q, khoa in qs:
        c1, s = goi("search.list", "part=snippet&type=video&maxResults=50&order=relevance&q=" + urllib.parse.quote(q))
        ids = [it["id"]["videoId"] for it in s.get("items", [])]
        c2, v = goi("videos.list", "part=statistics,snippet&id=" + ",".join(ids)) if ids else (None, {"items": []})
        rows = []
        for it in v.get("items", []):
            tieu_de = it["snippet"]["title"].lower()
            rows.append({"id": it["id"], "kenh": it["snippet"]["channelId"], "ngay": it["snippet"]["publishedAt"][:10],
                         "xem": int(it.get("statistics", {}).get("viewCount", 0)), "khop": any(k in tieu_de for k in khoa)})
        m = [r for r in rows if r["khop"]]
        def tuoi(r): return (HOM_NAY - datetime.datetime.fromisoformat(r["ngay"] + "T00:00:00+00:00")).days
        tom = {"q": q, "http": [c1, c2], "so_tra_ve": len(rows), "so_khop_tieu_de": len(m),
               "tong_xem_khop": sum(r["xem"] for r in m), "trung_vi_xem_khop": int(statistics.median([r["xem"] for r in m])) if m else 0,
               "max_xem_khop": max([r["xem"] for r in m], default=0), "so_kenh_khop": len({r["kenh"] for r in m}),
               "khop_12_thang": sum(1 for r in m if tuoi(r) <= 365), "khop_moi_nhat": max([r["ngay"] for r in m], default=None),
               "khop_cu_nhat": min([r["ngay"] for r in m], default=None),
               "khop_100k": sum(1 for r in m if r["xem"] >= 100_000), "videos": rows}
        kq["truy_van"].append(tom)
        print(vu, json.dumps({k: x for k, x in tom.items() if k != "videos"}, ensure_ascii=False))
    json.dump(kq, open(os.path.join(OUT, vu + ".json"), "w"), ensure_ascii=False, indent=1)
