#!/usr/bin/env python3
"""MR-3b · Tính lại cột "Thời điểm ước" của SHOT.md từ loi.json (0 USD, không gọi mạng).
  python3 scripts/mr3/shot_tg.py docs/tap01-1inmm/loi.json docs/tap01-1inmm/SHOT.md [--ghi]
Quy ước (giữ như MR-3): lời đọc 145 từ/phút; 3 s nghỉ đầu mỗi đoạn P; câu "doc": false (chỉ chữ) giữ GIU_CHU s;
cộng GIU_THE s cho thẻ tổng kết sau câu cuối P21 (SHOT §3); hàng "Kết" = danh sách nguồn + nhạc KET s.
Hàng SHOT có cột 2 dạng "P01 S005–S007" / "P01 S008" → ghi lại cột 3. Không --ghi: chỉ in."""
import json, re, sys
WPM, NGHI, GIU_CHU, GIU_THE, KET = 145, 3, 6, 8, 45


def mmss(t):
    t = int(round(t)); return f"{t//60}:{t%60:02d}"


def main(src, shot, ghi):
    d = json.load(open(src)); t = 0; bd, kt, prev = {}, {}, None
    for c in d["cau"]:
        if c["doan"] != prev: t += NGHI; prev = c["doan"]
        bd[c["id"]] = t
        t += len(c["loi"].split()) / WPM * 60 if c.get("doc", True) else GIU_CHU
        kt[c["id"]] = t
    cuoi = d["cau"][-1]["id"]; kt[cuoi] += GIU_THE; t = kt[cuoi]
    L = open(shot).read().split("\n"); out = []
    for ln in L:
        m = re.match(r"^\| (\d+) \| (P\d+ (S\d+)(?:–(S\d+))?[^|]*|Kết) \| ([^|]*) \|", ln)
        if m:
            if m.group(2) == "Kết": tg = f"{mmss(t)}–{mmss(t + KET)}"
            else: tg = f"{mmss(bd[m.group(3)])}–{mmss(kt[m.group(4) or m.group(3)])}"
            ln = ln.replace(f"| {m.group(5)} |", f"| {tg} |", 1)
        out.append(ln)
    tong = t + KET
    print(json.dumps({"loi_va_the_s": round(t), "tong_s": round(tong), "tong": mmss(tong)}))
    if ghi: open(shot, "w").write("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--ghi" in sys.argv)
