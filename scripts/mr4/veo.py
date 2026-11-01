#!/usr/bin/env python3
"""MR-4 · Thử khe Veo 3.1 Lite qua OpenRouter (POST /api/v1/videos → poll → tải). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mr4 python3 scripts/mr4/veo.py V12 1        # lượt 1 của khe V12, lời lấy ở reports/mr4/veo/loi_veo.json
Cấu hình cố định: google/veo-3.1-lite · 1080p · 16:9 · 8 s · generate_audio=false (0,05 USD/s × 8 = 0,40 USD, /api/v1/videos/models
đọc 01/11/2026) · không khung khoá (không có khoá Gemini; V1 "không áp dụng").
V7: ≤ 2 lượt/khe (lượt 2 phải khác lời lượt 1); chạy TUẦN TỰ 1 lượt (quỹ chung với lost-places-lab); trước lượt kiểm
/credits còn ≥ 1,92 USD (chi ước phiên 1,60 × 1,2) và ≥ 0,40 + 1 USD. Ghi giờ bắt đầu/kết thúc + total_usage tài khoản và usage
khoá MR trước/sau mỗi lượt vào reports/mr4/veo_luot.jsonl (phát hiện chi song song của phiên khác). 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả."""
import json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402

API = "https://openrouter.ai/api/v1"; HDR = {"Authorization": "Bearer sk-or-dummy-proxy-injects"}
MODEL = "google/veo-3.1-lite"; GIA = 0.40
LOI = os.path.join(ROOT, "reports", "mr4", "veo", "loi_veo.json"); SO = os.path.join(ROOT, "reports", "mr4", "veo_luot.jsonl")
OUT = os.path.join(ROOT, "lab", "mr4", "veo")
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def get(u):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=HDR), timeout=60))
    except urllib.error.HTTPError as e:
        if e.code == 402: budget.bao_402("openrouter", e.read()[:200])
        raise


def quy():
    c = get(API + "/credits")["data"]; k = get(API + "/key")["data"]
    return {"total_credits": c["total_credits"], "total_usage": round(c["total_usage"], 5),
            "con": round(c["total_credits"] - c["total_usage"], 5), "khoa_usage": k["usage"]}


def main(khe, luot):
    L = json.load(open(LOI)); p = L[khe][f"luot{luot}"]
    if luot == 2 and p["prompt"] == L[khe]["luot1"]["prompt"]: raise SystemExit("V7: lượt 2 phải đổi lời")
    if luot not in (1, 2): raise SystemExit("V7: tối đa 2 lượt/khe")
    dst = os.path.join(OUT, f"{khe}_l{luot}.mp4")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    budget.check("openrouter_usd", GIA)
    q0 = quy()
    if q0["con"] < max(1.60 * 1.2, GIA + 1): raise SystemExit(f"V7: số dư {q0['con']} < ngưỡng — DỪNG")
    body = {"model": MODEL, "prompt": p["prompt"], "duration": 8, "resolution": "1080p", "aspect_ratio": "16:9",
            "generate_audio": False}
    if p.get("negative"):
        body["provider"] = {"options": {"google-vertex": {"parameters": {"negativePrompt": p["negative"]}}}}
    t0 = now()
    req = urllib.request.Request(API + "/videos", data=json.dumps(body).encode(), method="POST",
                                 headers={**HDR, "Content-Type": "application/json"})
    try:
        job = json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("openrouter", msg)
        raise SystemExit(f"HTTP {e.code}: {msg}")
    jid = job["id"]; print(khe, luot, "job", jid, t0, flush=True)
    st = job
    for _ in range(120):  # ≤ 30 phút
        time.sleep(15); st = get(f"{API}/videos/{jid}")
        if st["status"] in ("completed", "failed"): break
    t1 = now()
    rec = {"khe": khe, "luot": luot, "job": jid, "bat_dau": t0, "xong": t1, "status": st["status"], "usage": st.get("usage"),
           "error": st.get("error"), "quy_truoc": q0, "body": {k: v for k, v in body.items() if k != "prompt"}, "prompt": p["prompt"]}
    if st["status"] == "completed":
        os.makedirs(OUT, exist_ok=True)
        r = urllib.request.urlopen(urllib.request.Request(f"{API}/videos/{jid}/content?index=0", headers=HDR), timeout=300)
        open(dst, "wb").write(r.read()); rec["tep"] = os.path.relpath(dst, ROOT); rec["tai_xong"] = now()
    time.sleep(5); q1 = quy(); rec["quy_sau"] = q1
    rec["chi_khoa"] = round(q1["khoa_usage"] - q0["khoa_usage"], 5)
    rec["chi_tai_khoan"] = round(q1["total_usage"] - q0["total_usage"], 5)
    rec["chi_phien_khac"] = round(rec["chi_tai_khoan"] - rec["chi_khoa"], 5)
    cost = (st.get("usage") or {}).get("cost")
    amt = float(cost) if cost is not None else rec["chi_khoa"]
    budget.charge("openrouter_usd", amt, {"khe": khe, "luot": luot, "job": jid, "status": st["status"], "bat_dau": t0, "xong": t1,
                                          "nguon_so": "usage.cost" if cost is not None else "chênh usage khoá"})
    with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps({k: rec[k] for k in ("khe", "luot", "status", "usage", "bat_dau", "xong", "chi_khoa", "chi_phien_khac", "error")},
                     ensure_ascii=False))
    if budget.canh_bao("openrouter_usd"): print("CẢNH BÁO: chạm mốc báo 80 % openrouter_usd")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
