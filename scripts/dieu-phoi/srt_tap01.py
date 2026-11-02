#!/usr/bin/env python3
"""Điều phối · phụ đề EN tập 1 (0 USD). Chữ = loi.json đã duyệt (G1/G2), số đổi sang chữ số cho dễ đọc;
mốc = reports/mr6/moc_cau.json (whisper giọng thật, dòng thời gian bản dựng MR-6, đã gồm 4 khe KBCB 4 s).
  python3 scripts/dieu-phoi/srt_tap01.py docs/tap01-1inmm/phat-hanh/tap01_en.srt"""
import json, re, sys
L = json.load(open('docs/tap01-1inmm/loi.json'))['cau']
M = json.load(open('reports/mr6/moc_cau.json'))
DOI = [  # cụm số trong lời → chữ số (chỉ đổi cách viết, không đổi nội dung)
 ("two hundred thirty million, three hundred sixty-one thousand, eight hundred eighty-four dollars", "$230,361,884"),
 ("six-hundred-fifty-million-dollar", "$650 million"), ("six hundred fifty million dollars", "$650 million"),
 ("two hundred thirty million dollars", "$230 million"), ("two point three three million dollars", "$2.33 million"),
 ("five point seven million dollars", "$5.7 million"), ("seventy-four point two million dollars", "$74.2 million"),
 ("six-million-dollar", "$6 million"), ("thirty-five thousand dollars", "$35,000"), ("one and a half million", "$1.5 million"),
 ("twenty-five to forty-five percent", "25 to 45 percent"), ("thirty-five to forty-five percent", "35 to 45 percent"),
 ("thirty-five percent", "35 percent"), ("eighty-two percent", "82 percent"), ("seventy percent", "70 percent"),
 ("one point eight two", "1.82"), ("two hundred forty months", "240 months"), ("two hundred fifty", "250"),
 ("twenty twenty-four", "2024"), ("twenty twenty-two", "2022"), ("twenty twenty-one", "2021"), ("twenty nineteen", "2019"),
 ("twenty eighteen", "2018"), ("twenty seventeen", "2017"), ("twenty thirteen", "2013"),
 ("twenty years", "20 years"), ("six or twelve months", "6 or 12 months"), ("six-month", "6-month"),
 ("April ninth", "April 9"), ("April fifth", "April 5"), ("April sixth", "April 6"), ("February fourteenth", "February 14"),
 ("one-in-M-M", "1inMM"), ("I-O-U", "IOU"), ("sec dot gov", "sec.gov"), ("ReportFraud dot F-T-C dot gov", "ReportFraud.ftc.gov"),
]
def hien(t):
    for a, b in DOI: t = t.replace(a, b)
    return t
def tg(x):
    x = max(0, x); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"
def hai_dong(c, n=44):
    if len(c) <= n: return c
    w = c.split(); best = None
    for i in range(1, len(w)):
        a, b = " ".join(w[:i]), " ".join(w[i:])
        if len(a) <= n and len(b) <= n:
            d = abs(len(a) - len(b))
            if best is None or d < best[0]: best = (d, a + "\n" + b)
    return best[1] if best else c
def chia(t, toi_da=70):
    """chia câu thành cụm ≤ 2 dòng × 42 ký tự, ưu tiên ngắt ở dấu câu"""
    w = t.split(); out = []; cur = ""  # hai_dong định nghĩa trước khi gọi
    for x in w:
        if cur and len(cur) + 1 + len(x) > toi_da:
            out.append(cur); cur = x
        else:
            cur = (cur + " " + x).strip()
            if re.search(r"[,;:]$", x) and len(cur) > toi_da * 0.55: out.append(cur); cur = ""
    if cur:
        if out and len(cur) < 18 and len(out[-1]) + 1 + len(cur) <= 88 and hai_dong(out[-1] + ' ' + cur).count(chr(10)) == 1: out[-1] += " " + cur
        else: out.append(cur)
    return out
cues = []
khe = {v[0]: k for k, v in M['khe_kbcb'].items()}
het_doan = {}
for x in L:
    if x.get('doc', True) is False: continue
    mc = M['cau'][x['id']]; het_doan[x['doan']] = max(het_doan.get(x['doan'], 0), mc['e'])
for x in L:
    t = hien(x['loi'])
    if x.get('doc', True) is False:  # thẻ KBCB chỉ chữ: đặt vào khe 4 s sau đoạn
        s = het_doan[x['doan']] + 0.15; ps = chia(x.get('chu') or t); d = 3.8 / len(ps)
        for k, p in enumerate(ps): cues.append((s + k * d, s + (k + 1) * d, p))
        continue
    mc = M['cau'][x['id']]; s, e = mc['s'], mc['e']; parts = chia(t); tot = sum(len(p) for p in parts); cur = s
    for p in parts:
        d = (e - s) * len(p) / tot; cues.append((cur, cur + d, p)); cur += d
cues.sort()
with open(sys.argv[1], 'w') as f:
    for i, (s, e, c) in enumerate(cues, 1):
        f.write(f"{i}\n{tg(s)} --> {tg(min(e, cues[i][0] - 0.01) if i < len(cues) else e)}\n{hai_dong(c)}\n\n")
print(len(cues), "cụm")
