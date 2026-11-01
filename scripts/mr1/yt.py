"""[MR-1] Gọi YouTube Data API v3 qua proxy (khoá do proxy tiêm — KHÔNG gửi, KHÔNG in khoá).
Mỗi lượt: budget.check_yt() TRƯỚC, budget.charge("youtube_units", đơn giá) SAU (kể cả lượt lỗi: bảng Quota costs
ghi "All API requests, including invalid requests, incur a quota cost of at least one point"). 402 → budget.bao_402("youtube").
  MR_PHIEN=mr1 python3 scripts/mr1/yt.py videos.list 'part=id&id=jNQXAC9IVRw'
In: HTTP + JSON phản hồi (đã rút gọn). Chỉ lưu số và id; không lưu tiêu đề/mô tả/thumbnail kênh khác."""
import json, os, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cp"))
import budget

def goi(method, query):
    budget.check_yt(method)
    res, meth = method.split(".")
    url = f"https://www.googleapis.com/youtube/v3/{res}?{query}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url), timeout=60) as r:
            code, body = r.status, r.read()
    except urllib.error.HTTPError as e:
        code, body = e.code, e.read()
    budget.charge("youtube_units", budget.YT_DON_GIA[method], {"method": method, "http": code, "query": query[:300]})
    if code == 402: budget.bao_402("youtube", body[:200])
    try: j = json.loads(body)
    except Exception: j = {"raw": body[:300].decode("utf-8", "replace")}
    return code, j

if __name__ == "__main__":
    c, j = goi(sys.argv[1], sys.argv[2])
    print(c); print(json.dumps(j, ensure_ascii=False)[:1500])
