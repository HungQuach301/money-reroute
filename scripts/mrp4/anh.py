#!/usr/bin/env python3
"""NGUỒN: scripts/mr6/anh.py (repo này, main @ a8741a4) — MR-P4 đổi: phiên mrp4, lời reports/mrp4/anh/loi_anh.json, ra lab/mrp4/anh, sổ reports/mrp4/anh/anh_luot.jsonl. Còn lại nguyên văn.
MR-6 · Sinh MỘT tranh minh hoạ qua OpenRouter (chat/completions, modalities image+text). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mr6 python3 scripts/mr6/anh.py b001 1
Lời: reports/mrp1/<biến thể>/loi_anh.json = {"tien_to": "...", "hau_to": "...", "ref": "a01", "tranh": {"a01": {"luot1": "...", ...}}}.
Tranh có "ref": true → gửi kèm ảnh tham chiếu (tranh "ref" của biến thể) để giữ nhất quán nét vẽ + nhân vật đại diện.
Model: google/gemini-nano-banana-2.1 (tên + giá kiểm bằng GET /api/v1/models, reports/mrp1/gia_model.json) · 16:9 · 1K.
Luật: ≤ 2 lượt/tranh, lượt 2 phải đổi lời; tuần tự; trước mỗi lượt check() trần + /credits còn ≥ ước + 1 USD (quỹ chung).
Chi ghi bằng usage.cost của phản hồi (usage: include); không có → chênh usage khoá. 402 → bao_402 → DỪNG.
Khoá do proxy tiêm; gửi giá trị giả. Không ghi khoá ra tệp."""
import base64, json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402

API = "https://openrouter.ai/api/v1"; HDR = {"Authorization": "Bearer sk-or-dummy-proxy-injects"}
MODEL = "google/gemini-nano-banana-2.1"; UOC = 0.06  # ước trần mỗi lượt (giá đo lượt thử ghi ở BAO-CAO)
SO = os.path.join(ROOT, "reports", "mrp4", "anh", "anh_luot.jsonl")
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def get(u):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=HDR), timeout=60))
    except urllib.error.HTTPError as e:
        if e.code == 402: budget.bao_402("openrouter", e.read()[:200])
        raise


def quy():
    c = get(API + "/credits")["data"]; k = get(API + "/key")["data"]
    return {"total_usage": round(c["total_usage"], 5), "con": round(c["total_credits"] - c["total_usage"], 5), "khoa_usage": k["usage"]}


def main(tid, luot):
    if os.environ.get("MR_PHIEN") != "mrp4": raise SystemExit("đặt MR_PHIEN=mrp4")
    if luot not in (1, 2): raise SystemExit("tối đa 2 lượt/tranh")
    L = json.load(open(os.path.join(ROOT, "reports", "mrp4", "anh", "loi_anh.json"))); T = L["tranh"][tid]
    p = T[f"luot{luot}"]
    if luot == 2 and p == T["luot1"]: raise SystemExit("lượt 2 phải đổi lời")
    out = os.path.join(ROOT, "lab", "mrp4", "anh"); os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, f"{tid}_l{luot}.png")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    budget.check("openrouter_usd", UOC)
    if budget.canh_bao("openrouter_usd"): print("CẢNH BÁO: đã chạm mốc 80 % trần", flush=True)
    q0 = quy()
    if q0["con"] < UOC + 1: raise SystemExit(f"số dư {q0['con']} < ngưỡng — DỪNG")
    text = f"{L['tien_to']}\n\nSCENE: {p}\n\n{L['hau_to']}"
    ref = os.path.join(ROOT, L[T["ref"]])
    b64 = base64.b64encode(open(ref, "rb").read()).decode()
    content = [{"type": "image_url", "image_url": {"url": "data:image/png;base64," + b64}},
               {"type": "text", "text": L["ref_loi_nv" if T["ref"] == "ref_nv" else "ref_loi_canh"] + "\n\n" + text}]
    body = {"model": MODEL, "modalities": ["image", "text"], "messages": [{"role": "user", "content": content}],
            "image_config": {"aspect_ratio": "16:9", "image_size": "1K"}, "usage": {"include": True}}
    t0 = now()
    req = urllib.request.Request(API + "/chat/completions", data=json.dumps(body).encode(), method="POST",
                                 headers={**HDR, "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("openrouter", msg)
        raise SystemExit(f"HTTP {e.code}: {msg}")
    except (ConnectionError, urllib.error.URLError, TimeoutError) as e:  # MR-6: mất kết nối giữa chừng — ghi sự kiện, đối soát khoá cuối phiên
        time.sleep(3); q1 = quy()
        with open(SO, "a") as f:
            f.write(json.dumps({"tranh": tid, "luot": luot, "bat_dau": t0, "xong": now(), "loi": f"{type(e).__name__}: {e}"[:200],
                                "quy_truoc": q0, "quy_sau": q1, "ghi_chu": "không có phản hồi → không ghi sổ chi; đối soát chênh khoá cuối phiên"}, ensure_ascii=False) + "\n")
        raise SystemExit(f"MẤT KẾT NỐI {tid}: {e}")
    t1 = now()
    msg = r["choices"][0]["message"]; imgs = msg.get("images") or []
    rec = {"tranh": tid, "luot": luot, "bat_dau": t0, "xong": t1, "model": r.get("model"), "usage": r.get("usage"),
           "so_anh": len(imgs), "chu_tra_ve": (msg.get("content") or "")[:300], "ref": os.path.relpath(ref, ROOT) if ref else None,
           "quy_truoc": q0, "prompt": p}
    if imgs:
        u = imgs[0]["image_url"]["url"]; open(dst, "wb").write(base64.b64decode(u.split(",", 1)[1]))
        rec["tep"] = os.path.relpath(dst, ROOT)
    time.sleep(3); q1 = quy(); rec["quy_sau"] = q1
    rec["chi_khoa"] = round(q1["khoa_usage"] - q0["khoa_usage"], 5)
    rec["chi_phien_khac"] = round(q1["total_usage"] - q0["total_usage"] - rec["chi_khoa"], 5)
    cost = (r.get("usage") or {}).get("cost")
    amt = float(cost) if cost is not None else rec["chi_khoa"]
    budget.charge("openrouter_usd", amt, {"tranh": tid, "luot": luot, "bat_dau": t0, "xong": t1, "so_anh": len(imgs),
                                          "nguon_so": "usage.cost" if cost is not None else "chênh usage khoá"})
    with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(tid, luot, "ảnh" if imgs else "KHÔNG ẢNH", "cost", amt, "tokens", (r.get("usage") or {}).get("completion_tokens"), flush=True)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
