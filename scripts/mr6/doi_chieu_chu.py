#!/usr/bin/env python3
"""MR-6 · Máy đối chiếu MỌI chữ trên hình (reports/mr6/chu_tren_hinh.json — sổ do dung.py ghi khi vẽ) với nguồn cho phép (0 USD).
  python3 scripts/mr6/doi_chieu_chu.py   → reports/mr6/doi_chieu_chu.json + in các chuỗi có từ/số không khớp
Cho phép (PHONG-CACH-HINH §2 luật 9): lời đã duyệt (docs/tap01-1inmm/loi.json: "loi" + "chu"), số liệu/chữ hồ sơ (text các PDF
ho-so/1inmm-horwitz/*.pdf + NGUON.md), chữ thẻ đã duyệt ở G1 (SHOT.md §3, §4), nhãn tầng/minh hoạ/nguồn (HIEN-CHUONG §3–§4, §6).
Từng chuỗi: tách từ (chữ thường) → từ không có trong kho = CỜ; tách số → số không có trong bảng số hồ sơ = CỜ.
Số tính từ hồ sơ (phép tính / đổi đơn vị) liệt kê trong SO_TINH kèm căn cứ. Cờ máy → mắt xét, ghi kết luận vào báo cáo."""
import glob, json, os, re, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
loi = json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))["cau"]
kho = " ".join(c["loi"] + " " + (c["chu"] or "") for c in loi)
pdf = " ".join(subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True).stdout
               for f in glob.glob(os.path.join(ROOT, "ho-so", "1inmm-horwitz", "*.pdf")))
nguon = open(os.path.join(ROOT, "docs", "tap01-1inmm", "NGUON.md")).read()
shot = open(os.path.join(ROOT, "docs", "tap01-1inmm", "SHOT.md")).read()
hc = open(os.path.join(ROOT, "docs", "HIEN-CHUONG.md")).read()
NHAN = ("ILLUSTRATIVE not the real person a real message CONVICTED ALLEGED admitted in plea Source Illustrative math based on sample "
        "SOURCES consent judgment no findings of fact prosecutors words MONEY REROUTE vs per p pp Dkt No Rel Lit Press Gov t USAO DOJ C D Cal "
        "cv cr Final Judgment Complaint Indictment Plea Agreement Sentencing Position Release Litigation page Commitment Order Probation "
        "Attorney s Office FINRA BrokerCheck IAPD FTC ReportFraud links description Full SEC tips Investment Adviser Public Disclosure Submit Tip "
        "Check Report")
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower().replace("’", "'"))
TU = set(norm(w) for w in re.split(r"[\s/·—–\-]+", " ".join([kho, pdf, nguon, shot, hc, NHAN])) if norm(w))
# biến thể hình thái hay gặp (số nhiều / quá khứ) của từ trong kho
def co(w):
    return w in TU or w.rstrip("s") in TU or (w + "s") in TU or w[:-2] in TU or w[:-1] in TU or w[:-3] in TU
SO_HS = set(re.sub(r"[,$]", "", x).rstrip(".") for x in re.findall(r"\$?\d[\d,]*(?:\.\d+)?", pdf + nguon + shot))
SO_TINH = {  # số hiện trên hình nhưng không có nguyên dạng trong hồ sơ — căn cứ
    "650000000": "N7 tr. 12 '$650 million' viết đủ chữ số", "1.8225": "1,35² (S027, N1 ¶25)", "1.82": "S027", "82": "S027 eighty-two",
    "70": "S028 35 % × 2", "1.35": "1 + 35 % (N1 ¶25)", "2.33": "N1 ¶54 ($2.33 million)", "5.7": "N1 ¶56 ($5.7 million)",
    "74.2": "N4 tr. 3 $74,222,912.33 làm tròn", "28": "lịch: 12/3 → 9/4/2021", "4": "lịch 5/4 → 9/4; S034 'five'…", "3": "lịch 6/4 → 9/4; '3 LESSONS' S093",
    "20": "N8 240 tháng = 20 năm", "240": "N8 tr. 1", "230": "N7 tr. 12 $230.36 million làm tròn", "1.5": "N7 tr. 10 $1.5 million",
    "2022": "N8", "2021": "N1/N6/N7", "2024": "N4", "2019": "N7 tr. 12", "2017": "N1 ¶52", "2018": "N1 ¶54", "2013": "N7 tr. 8",
    "5": "N7 tr. 12 five", "250": "N7 tr. 12", "1": "RULE / 1 count", "2": "×2", "6": "6 months", "12": "12 months", "25": "25–45 %",
    "45": "25–45 %", "35": "N1 ¶25", "9": "April 9", "14": "Feb. 14", "353": "", "000": ""}
r = {"chuoi": 0, "co": []}
for s in json.load(open(os.path.join(ROOT, "reports", "mr6", "chu_tren_hinh.json"))):
    r["chuoi"] += 1
    if re.fullmatch(r"\$?[\d,\.]+\+?|\d+%|\+?\d+–\d+%|≈ \$?[\d\.]+.*", s.strip()) and False: pass
    sos = [re.sub(r"[,$+%]", "", x).rstrip(".") for x in re.findall(r"\$?\d[\d,]*(?:\.\d+)?", s)]
    so_la = [x for x in sos if x not in SO_HS and x not in SO_TINH and x.lstrip("0")]
    chu = re.sub(r"\$?\d[\d,]*(?:\.\d+)?%?", " ", s)
    tu_la = [w for w in (norm(x) for x in re.split(r"[\s/·—–\-“”\"(),:;!?.×≈=+]+", chu)) if w and not co(w)]
    if so_la or tu_la: r["co"].append({"chuoi": s, "tu_la": tu_la, "so_la": so_la})
json.dump(r, open(os.path.join(ROOT, "reports", "mr6", "doi_chieu_chu.json"), "w"), ensure_ascii=False, indent=1)
print(r["chuoi"], "chuỗi;", len(r["co"]), "chuỗi có cờ")
for c in r["co"]: print(" -", c["chuoi"][:110], "| từ:", c["tu_la"], "| số:", c["so_la"])
