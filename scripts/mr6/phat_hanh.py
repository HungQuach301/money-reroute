#!/usr/bin/env python3
"""MR-6 · Gói phát hành tập 1 (0 USD) → docs/tap01-1inmm/phat-hanh/PHAT-HANH.md (tiêu đề T1, mô tả EN, chương, thẻ, khai AI).
Chương = đầu đoạn theo mốc giọng thật (reports/mr6/moc_cau.json). Nguồn = chỉ nguồn ĐÃ MỞ trong NGUON.md (+ mở lại N2, N3, N18 ở MR-6)."""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
M = json.load(open(os.path.join(ROOT, "reports", "mr6", "moc_cau.json")))
K = json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "kiem", "mr6_nguon.json")))
st = {d["doan"]: d["s"] for d in M["doan"]}
CH = [("P00", "A message that didn't add up"), ("P01", "The case in one minute"), ("P02", "1inMM Capital"), ("P03", "The pitch"),
      ("P04", "What a promissory note is"), ("P05", "The math: per note vs. per year"), ("P06", "Why investors felt safe"),
      ("P07", "Groups and sub-investors"), ("P08", "Collateral on paper"), ("P09", "The paperwork"), ("P10", "Where the money went"),
      ("P11", "\"Investing alongside you\""), ("P12", "How a Ponzi scheme keeps going"), ("P13", "The defaults"),
      ("P15", "The reassurances"), ("P16", "Countdown to April 9"), ("P17", "April 2021"), ("P18", "Guilty plea and sentence"),
      ("P19", "The SEC's civil case"), ("P20", "In prosecutors' words"), ("P21", "Lessons and red flags")]
mmss = lambda s: f"{int(s // 60)}:{int(s % 60):02d}"
chuong = [("0:00" if p == "P00" else mmss(st[p] - 0.35), t) for p, t in CH]
NG = [
 ("SEC v. Zachary J. Horwitz and 1inMM Capital, LLC, No. 2:21-cv-02927 (C.D. Cal.) — Complaint (filed Apr. 5, 2021)", "https://www.sec.gov/files/litigation/complaints/2021/comp-pr2021-58.pdf"),
 ("SEC Press Release 2021-58 (Apr. 6, 2021)", "https://www.sec.gov/newsroom/press-releases/2021-58"),
 ("SEC Litigation Release No. 25067 (Apr. 8, 2021)", "https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25067"),
 ("SEC v. Horwitz — Final Judgment as to Defendant Zachary J. Horwitz, Dkt. 323 (Feb. 14, 2024)", "https://www.sec.gov/files/judg21-cv-02927horwitz.pdf"),
 ("SEC Litigation Release No. 25973 (Apr. 11, 2024)", "https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25973"),
 ("United States v. Zachary Joseph Horwitz, No. 2:21-cr-00214 (C.D. Cal.) — Indictment, Dkt. 25 (May 4, 2021)", "https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.25.0.pdf"),
 ("U.S. v. Horwitz — Plea Agreement, Dkt. 45 (Sept. 1, 2021)", "https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.45.0.pdf"),
 ("U.S. v. Horwitz — Government's Sentencing Position, Dkt. 58 (Jan. 31, 2022)", "https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.58.0.pdf"),
 ("U.S. v. Horwitz — Judgment and Probation/Commitment Order, Dkt. 75 (Feb. 2022)", "https://storage.courtlistener.com/recap/gov.uscourts.cacd.819729/gov.uscourts.cacd.819729.75.0.pdf"),
 ("U.S. Attorney's Office, C.D. Cal. — Press Release 21-059 (Apr. 6, 2021)", "https://www.justice.gov/usao-cdca/pr/beverlywood-man-arrested-allegedly-bilking-investors-falsely-claiming-license-latin"),
 ("U.S. Attorney's Office, C.D. Cal. — Press Release 21-207 (Oct. 4, 2021)", "https://www.justice.gov/usao-cdca/pr/beverlywood-man-pleads-guilty-securities-fraud-admitting-massive-ponzi-falsely-claimed"),
 ("U.S. Attorney's Office, C.D. Cal. — Press Release 22-027 (Feb. 14, 2022)", "https://www.justice.gov/usao-cdca/pr/la-man-sentenced-20-years-federal-prison-650-million-ponzi-scheme-falsely-claimed"),
]
CHECK = [("FINRA BrokerCheck", "https://brokercheck.finra.org/"), ("SEC Investment Adviser Public Disclosure", "https://adviserinfo.sec.gov/"),
         ("SEC — Submit a Tip or Complaint", "https://www.sec.gov/submit-tip-or-complaint"), ("FTC — ReportFraud", "https://reportfraud.ftc.gov/")]
AI = ("Dramatized scenes use AI-generated visuals and illustrative characters, not the real people involved. Narration voice is AI-generated. "
      "Facts are drawn from the public court and agency records listed below.")
mo_ta = ["Zachary Horwitz, an actor in Los Angeles, told investors their money would buy film rights to be licensed to streaming platforms. "
         "In his plea agreement, he admitted the distribution deals were fake. At least $650 million came in; in 2022 a federal judge sentenced him "
         "to 20 years in prison. This is how the money was rerouted — and the red flags you can spot next time.",
         "",
         "HBO and Netflix were not accused of wrongdoing in these cases; according to the SEC, neither company ever did business with 1inMM.",
         "",
         "Allegations from the SEC complaint and statements by prosecutors are labeled as such in the video. Facts admitted in the plea agreement are labeled "
         "\"admitted in plea.\" The SEC's 2024 final judgment was entered with his consent, without findings of fact.",
         "", "CHAPTERS"] + [f"{a} {b}" for a, b in chuong] + ["", "SOURCES (public court and agency records)"] + \
        [f"- {a}: {u}" for a, u in NG] + ["", "CHECK A SELLER / REPORT FRAUD"] + [f"- {a}: {u}" for a, u in CHECK] + \
        ["", AI, "", "This video is for education only. It is not investment or legal advice."]
txt = "\n".join(mo_ta)
TAGS = ["1inMM", "Zachary Horwitz", "Ponzi scheme explained", "promissory notes", "investment fraud", "red flags", "SEC case", "financial literacy",
        "how Ponzi schemes work", "true crime finance", "film financing fraud", "investor protection"]
md = ["# GÓI PHÁT HÀNH — Tập 1 `tap01-1inmm` (MR-6, chờ G2)", "",
      "> Sinh máy: `python3 scripts/mr6/phat_hanh.py`. Lời, tiêu đề, dòng khai AI theo bản đã duyệt (PHUONG-AN T1; HIEN-CHUONG §6). **Chưa đăng** — chủ dự án duyệt ở G2.", "",
      "## 1. Tiêu đề (T1, đã chọn ở G1)", "", "`How an Actor Raised $650 Million on Fake Film Deals` (51 ký tự)", "",
      "## 2. Mô tả (EN — dán nguyên khối)", "", "```", txt, "```", "", f"Độ dài mô tả: {len(txt)} ký tự (giới hạn YouTube 5.000).", "",
      "## 3. Thẻ (tags)", "", "`" + ", ".join(TAGS) + "`" + f" — {len(', '.join(TAGS))} ký tự (giới hạn 500). Không thẻ tên HBO/Netflix (luật 8e), không \"scam/scammer\".", "",
      "## 4. Khai AI (HIEN-CHUONG §6)", "",
      "- YouTube Studio → Attributes → **\"AI use\" = Yes** (giọng đọc AI; cảnh minh hoạ AI; 4 clip vật thể tả thực V10–V13).",
      "- Trang Help đã đọc: https://support.google.com/youtube/answer/14328491 — tiêu đề \"Disclosing use of GenAI content\", HTTP 200, đọc **02/11/2026 03:53 UTC** (MR-6). "
      "Nội dung then chốt: creator phải khai nội dung AI \"that seems realistic\"; trong Studio, mục Attributes, \"AI use\" chọn Yes nếu thuộc diện. "
      "**Đọc lại trước ngày đăng** và ghi ngày đọc mới (luật §6).",
      f"- Dòng khai cố định đã có trong mô tả và cuối phim: \"{AI}\"", "",
      "## 5. Trạng thái vụ ngày dựng (HIEN-CHUONG §3 luật 4)", "",
      f"Kiểm {K['ngay_kiem_utc']} (UA khai báo của kênh, chỉ trong header; tệp `docs/tap01-1inmm/kiem/mr6_nguon.json`):", ""]
for r in K["ket_qua"]:
    md.append(f"- {r['ma']} {r['url']} — HTTP {r.get('http')}; " + (", ".join(f"\"{k}\": {'có' if v else 'không'}" for k, v in (r.get('co_cau') or {}).items()))
              + (f"; trang ghi \"{r['dong_cap_nhat'][:30]}\"" if r.get("dong_cap_nhat") else "") + (f"; {r.get('ket_luan')}" if r.get("ket_luan") else ""))
md += ["", "Kết luận: N2, N3, N18 **đã mở được** bằng UA khai báo (MR-3b ghi 403) — câu then chốt khớp. Ân xá/giảm án: \"Horwitz\" **không có** trên 3 trang DOJ. "
       "Docket CourtListener (N9) vẫn chưa mở được ở MR-3 (403, không vượt) → **không** khẳng định có/không kháng cáo; phim không nói về kháng cáo. Kiểm lại ngày đăng.", "",
       "## 6. Thumbnail", "", "Theo `THUMBNAIL-RULES.txt` (điều phối tạo). Phiên MR-6 không làm thumbnail (lệnh không yêu cầu, trần ảnh dành cho L1).", "",
       "## 7. Tệp", "", "- Bản cuối 1080p: `lab/mr6/dung/tap01_1080p.mp4` (LFS) · bản xem 540p: `reports/mr6/xem/tap01_540p.mp4` (LFS).", ""]
open(os.path.join(ROOT, "docs", "tap01-1inmm", "phat-hanh", "PHAT-HANH.md"), "w").write("\n".join(md)); print("\n".join(f"{a} {b}" for a, b in chuong))
