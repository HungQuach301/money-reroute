#!/usr/bin/env python3
"""NGUỒN: scripts/mr6/veo.py (repo này, main @ 19d3a7a) — MR-P2 đổi: 4 s (0,20 USD), phiên mrp2, khung đầu = dung.tranh(ma) 1920×1080
(đúng khung bản đăng), lời có tiền tố phong cách chung, đường dẫn. Logic sổ/402/V7 giữ nguyên.
Sinh clip Veo 3.1 Lite ảnh→video qua OpenRouter (POST /api/v1/videos → poll → tải). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mrp2 python3 scripts/mrp2/veo.py V1 1
Cấu hình: google/veo-3.1-lite · 1080p · 16:9 · 4 s · generate_audio=false. Giá: duration_seconds_without_audio 0,05 USD/s
(GET /api/v1/videos/models 02/11/2026 14:57 UTC, reports/mrp2/gia_veo.json) → 0,20 USD/clip.
V7: ≤ 2 lượt/khe (lượt 2 phải khác lời lượt 1); TUẦN TỰ; trước lượt kiểm /credits còn ≥ 0,20 + 1 USD. 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả."""
import base64, io, json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402
TMP = os.environ.get("MRP2_TMP", "/tmp/claude-0/mrp2"); os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))

API = "https://openrouter.ai/api/v1"; HDR = {"Authorization": "Bearer sk-or-dummy-proxy-injects"}
MODEL = "google/veo-3.1-lite"; DUR = 4; GIA = 0.20
LOI = os.path.join(ROOT, "reports", "mrp2", "veo", "loi_veo.json"); SO = os.path.join(ROOT, "reports", "mrp2", "veo_luot.jsonl")
OUT = os.path.join(ROOT, "lab", "mrp2", "veo")
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
    L = json.load(open(LOI)); p = L[khe][f"luot{luot}"]; ma = L[khe]["ma"]
    if luot not in (1, 2): raise SystemExit("V7: tối đa 2 lượt/khe")
    if luot == 2 and p["prompt"] == L[khe]["luot1"]["prompt"]: raise SystemExit("V7: lượt 2 phải đổi lời")
    dst = os.path.join(OUT, f"{khe}_{ma}_l{luot}.mp4")
    if os.environ.get("MR_PHIEN") != "mrp2": raise SystemExit("đặt MR_PHIEN=mrp2")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    budget.check("openrouter_usd", GIA)
    q0 = quy()
    if q0["con"] < GIA + 1: raise SystemExit(f"V7: số dư {q0['con']} < ngưỡng — DỪNG")
    import dung  # noqa: E402  (khung đúng bản đăng)
    b = io.BytesIO(); dung.tranh(ma).convert("RGB").save(b, "PNG")
    prompt = p["prompt"] + " " + L["_chung"]["phong_cach"]
    body = {"model": MODEL, "prompt": prompt, "duration": DUR, "resolution": "1080p", "aspect_ratio": "16:9", "generate_audio": False,
            "frame_images": [{"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()},
                              "frame_type": "first_frame"}],
            "provider": {"options": {"google-vertex": {"parameters": {"negativePrompt": p.get("negative") or L["_chung"]["negative"]}}}}}
    t0 = now()
    req = urllib.request.Request(API + "/videos", data=json.dumps(body).encode(), method="POST", headers={**HDR, "Content-Type": "application/json"})
    try:
        job = json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("openrouter", msg)
        raise SystemExit(f"HTTP {e.code}: {msg}")
    jid = job["id"]; print(khe, luot, "job", jid, t0, flush=True)
    st = job
    for _ in range(120):
        time.sleep(15); st = get(f"{API}/videos/{jid}")
        if st["status"] in ("completed", "failed"): break
    t1 = now()
    rec = {"khe": khe, "ma": ma, "luot": luot, "job": jid, "bat_dau": t0, "xong": t1, "status": st["status"], "usage": st.get("usage"),
           "error": st.get("error"), "quy_truoc": q0, "body": {k: v for k, v in body.items() if k not in ("prompt", "frame_images")}, "prompt": prompt}
    if st["status"] == "completed":
        os.makedirs(OUT, exist_ok=True)
        r = urllib.request.urlopen(urllib.request.Request(f"{API}/videos/{jid}/content?index=0", headers=HDR), timeout=300)
        open(dst, "wb").write(r.read()); rec["tep"] = os.path.relpath(dst, ROOT); rec["tai_xong"] = now()
    time.sleep(5); q1 = quy(); rec["quy_sau"] = q1
    rec["chi_khoa"] = round(q1["khoa_usage"] - q0["khoa_usage"], 5)
    rec["chi_tai_khoan"] = round(q1["total_usage"] - q0["total_usage"], 5)
    rec["chi_phien_khac"] = round(rec["chi_tai_khoan"] - rec["chi_khoa"], 5)
    cost = (st.get("usage") or {}).get("cost")
    amt = float(cost) if cost is not None else (GIA if st["status"] == "completed" else 0.0)
    budget.charge("openrouter_usd", amt, {"khe": khe, "ma": ma, "luot": luot, "job": jid, "status": st["status"], "bat_dau": t0, "xong": t1,
                                          "nguon_so": "usage.cost" if cost is not None else ("đơn giá 0,20" if st["status"] == "completed" else "failed → 0")})
    with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps({k: rec[k] for k in ("khe", "ma", "luot", "status", "usage", "bat_dau", "xong", "chi_khoa", "chi_phien_khac", "error")}, ensure_ascii=False))
    if budget.canh_bao("openrouter_usd"): print("CẢNH BÁO: chạm mốc báo 80 % openrouter_usd — DỪNG SINH")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
