#!/usr/bin/env python3
"""MR-6 · Mở lại N2, N3, N18 (sec.gov) bằng UA khai báo của kênh + kiểm trạng thái vụ ngày dựng (0 USD, GET).
  MR_UA="<UA khai báo do lệnh cấp>" python3 scripts/mr6/mo_nguon.py → docs/tap01-1inmm/kiem/mr6_nguon.json
UA CHỈ đọc từ biến môi trường và chỉ gửi trong header; KHÔNG ghi vào tệp/repo (CLAUDE.md). Không vượt rào: 403/chặn → ghi "chưa mở được".
Kiểm câu then chốt của từng nguồn bằng chuỗi con (không suy nội dung khi không mở được)."""
import hashlib, html, json, os, re, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = os.environ["MR_UA"]
MUC = [
 ("N2", "https://www.sec.gov/newsroom/press-releases/2021-58", ["Emergency Asset Freeze", "690 Million", "Horwitz"]),
 ("N3", "https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25067", ["one in a million", "HBO or Netflix", "April 5, 2021"]),
 ("N18", "https://www.sec.gov/submit-tip-or-complaint", ["Tip", "Complaint"]),
 ("N15a", "https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present", ["Horwitz"]),
 ("N15b", "https://www.justice.gov/pardon/pardons-granted-president-joseph-biden-2021-2025", ["Horwitz"]),
 ("N15c", "https://www.justice.gov/pardon/commutations-granted-president-joseph-biden-2021-2025", ["Horwitz"]),
]
out = {"ngay_kiem_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ua": "UA khai báo của kênh (không ghi vào repo)", "ket_qua": []}
for ma, url, cau in MUC:
    rec = {"ma": ma, "url": url}
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"}), timeout=60)
        b = r.read(); t = html.unescape(re.sub(r"<[^>]+>", " ", b.decode("utf-8", "replace"))); t = re.sub(r"\s+", " ", t)
        rec.update(http=r.status, bytes=len(b), sha256=hashlib.sha256(b).hexdigest()[:16],
                   tieu_de=(re.search(r"<title>(.*?)</title>", b.decode("utf-8", "replace"), re.S) or [None, ""])[1].strip()[:150],
                   co_cau={c: (c.lower() in t.lower()) for c in cau})
        for m in ("updated", "Updated"):
            k = t.find(m)
            if k >= 0: rec["dong_cap_nhat"] = t[k:k + 60]; break
    except urllib.error.HTTPError as e:
        rec.update(http=e.code, ket_luan="chưa mở được (không vượt)")
    except Exception as e:
        rec.update(http=None, loi=str(e)[:120], ket_luan="chưa mở được")
    out["ket_qua"].append(rec); print(json.dumps(rec, ensure_ascii=False)[:300]); time.sleep(1.5)
json.dump(out, open(os.path.join(ROOT, "docs", "tap01-1inmm", "kiem", "mr6_nguon.json"), "w"), ensure_ascii=False, indent=1)
