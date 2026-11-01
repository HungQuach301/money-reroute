"""[MR-K1] Điền §7 "Đo cầu YouTube" của docs/kho-de-tai/<vu>.md từ reports/mrk1/do-cau/<vu>.json (0 USD, không gọi mạng).
Truy vấn đầu của mỗi vụ đo cầu VỤ (tên riêng); truy vấn thứ hai có thể là cầu THỂ LOẠI — đánh dấu theo LOAI dưới đây.
  python3 scripts/mrk1/dien_cau.py"""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(ROOT, "reports", "mrk1", "do-cau")
# "vu" = cụm tìm chứa tên riêng của vụ/nhân vật; "the-loai" = cụm chung (khớp từ khoá rộng, lẫn vụ khác).
THE_LOAI = {"scammer stole 100 million Google Facebook", "IRS scam call center India busted", "Coinbase insider trading case",
            "fake navy pilot romance scam", "prison inmates sextortion military", "sextortion scam service members",
            "nigerian romance scammer sentenced", "tech support scam pop up sentenced", "fake virus warning scam"}
NOTE_RONG = {"Frank startup JPMorgan fraud": "từ khoá \"frank\" rộng", "IRS scam call center India busted": "từ khoá \"irs\" rộng, gồm video quay lén call center",
             "scammer stole 100 million Google Facebook": "từ khoá \"google\"/\"facebook\" rất rộng", "Heather Morgan Razzlekhan": "từ khoá \"morgan\" rộng",
             "fake navy pilot romance scam": "từ khoá \"navy\" rộng", "fake virus warning scam": "từ khoá \"virus\" rộng",
             "Hitesh Patel IRS scam": "từ khoá \"patel\"/\"irs\" rộng"}
for f in sorted(os.listdir(D)):
    vu = f[:-5]; md = os.path.join(ROOT, "docs", "kho-de-tai", vu + ".md")
    if not os.path.exists(md): continue
    j = json.load(open(os.path.join(D, f)))
    L = [f"Đo {j['ngay_do']} bằng `scripts/mrk1/do_cau.py` (YouTube Data API v3: 1 `search.list` maxResults=50 order=relevance + 1 `videos.list`/truy vấn; "
         f"số liệu thô `reports/mrk1/do-cau/{vu}.json`, chỉ id/ngày/lượt xem). \"Khớp\" = tiêu đề chứa ít nhất một từ khoá (tiêu đề không lưu).", "",
         "| Truy vấn | Loại | Từ khoá khớp | Trả về | Khớp | Trung vị xem (khớp) | Max xem | ≥ 100k | Khớp ≤ 12 tháng | Kênh khác nhau | Id top 3 (theo lượt xem) | Ghi chú |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for t in j["truy_van"]:
        loai = "thể loại" if t["q"] in THE_LOAI else "vụ"
        note = NOTE_RONG.get(t["q"], "")
        if t["so_tra_ve"] == 0: note = (note + "; " if note else "") + "search.list trả 0 video"
        L.append(f"| `{t['q']}` | {loai} | {', '.join(t['khoa'])} | {t['so_tra_ve']} | {t['so_khop_tieu_de']} | {t['trung_vi_xem_khop']:,} | {t['max_xem_khop']:,} | "
                 f"{t['khop_100k']} | {t['khop_12_thang']} | {t['so_kenh_khop']} | {', '.join(t.get('top3_id', []))} | {note} |".replace(",", " ").replace("  ", ", "))
    L += ["", "Giới hạn: 50 kết quả theo độ liên quan, không phải toàn bộ; khớp tiêu đề thô; lượt xem phản ánh cả sức kéo của kênh. Không lưu tiêu đề, mô tả, thumbnail của kênh khác."]
    s = open(md).read()
    s2 = re.sub(r"(## 7\. Đo cầu YouTube\n)(.*?)(\n## 8\.)", lambda m: m.group(1) + "\n".join(L) + "\n" + m.group(3), s, flags=re.S)
    open(md, "w").write(s2); print(vu, "điền" if s2 != s else "không đổi")
