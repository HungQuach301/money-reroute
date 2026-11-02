#!/usr/bin/env python3
"""NGUỒN: scripts/mrp2/veo.py (repo này, main @ 33ce227) — MR-P3 đổi: nhiều mô hình (Veo 3.1 Lite 720p/1080p, Kling v3.0 Std 720p),
độ dài/độ phân giải/khung đầu/khung cuối theo từng khe, chế độ chữ→video (không khung), phiên mrp3, đường dẫn. Logic sổ/402/V7 giữ nguyên.
Sinh clip qua OpenRouter (POST /api/v1/videos → poll → tải). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mrp3 python3 scripts/mrp3/veo.py V01 1
Cấu hình mỗi khe trong reports/mrp3/veo/loi_veo.json: ma (khung đầu = dung.tranh(ma) đúng khung bản đăng), cuoi (khung cuối), model, res, dur.
Giá (GET /api/v1/videos/models 02/11/2026 16:36 UTC, reports/mrp3/danh_muc_video.json): Veo 3.1 Lite không tiếng 1080p 0,05 USD/s,
720p 0,03 USD/s; Kling v3.0 Std 0,084 USD/s (không tiếng).
V7: ≤ 2 lượt/khe (lượt 2 phải khác lời lượt 1); TUẦN TỰ; trước lượt kiểm /credits còn ≥ giá + 1 USD. 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả."""
import base64, io, json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402
TMP = os.environ.get("MRP3_TMP", "/tmp/claude-0/mrp3"); os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr6"))

API = "https://openrouter.ai/api/v1"; HDR = {"Authorization": "Bearer sk-or-dummy-proxy-injects"}
DON_GIA = {("google/veo-3.1-lite", "1080p"): 0.05, ("google/veo-3.1-lite", "720p"): 0.03, ("kwaivgi/kling-v3.0-std", "720p"): 0.084}
LOI = os.path.join(ROOT, "reports", "mrp3", "veo", "loi_veo.json"); SO = os.path.join(ROOT, "reports", "mrp3", "veo_luot.jsonl")
OUT = os.path.join(ROOT, "lab", "mrp3", "veo")
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


def anh(ma, res):
    import dung  # noqa: E402  (khung đúng bản đăng)
    im = dung.tranh(ma).convert("RGB")
    if res == "720p": im = im.resize((1280, 720), resample=1)
    b = io.BytesIO(); im.save(b, "PNG"); return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()


def main(khe, luot):
    L = json.load(open(LOI)); K = L[khe]; p = K[f"luot{luot}"]
    if luot not in (1, 2): raise SystemExit("V7: tối đa 2 lượt/khe")
    if luot == 2 and p["prompt"] == K["luot1"]["prompt"]: raise SystemExit("V7: lượt 2 phải đổi lời")
    model = K.get("model", "google/veo-3.1-lite"); res = K.get("res", "1080p"); dur = K.get("dur", 4)
    gia = round(DON_GIA[(model, res)] * dur, 4)
    dst = os.path.join(OUT, f"{khe}_{K.get('ma') or 'chu'}_{res}_l{luot}.mp4")
    if os.environ.get("MR_PHIEN") != "mrp3": raise SystemExit("đặt MR_PHIEN=mrp3")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    budget.check("openrouter_usd", gia)
    if budget.canh_bao("openrouter_usd"): raise SystemExit("đã chạm mốc báo 80 % — DỪNG SINH")
    q0 = quy()
    if q0["con"] < gia + 1: raise SystemExit(f"V7: số dư {q0['con']} < ngưỡng — DỪNG")
    prompt = p["prompt"] + " " + L["_chung"]["phong_cach"]
    body = {"model": model, "prompt": prompt, "duration": dur, "resolution": res, "aspect_ratio": "16:9", "generate_audio": False}
    fr = []
    if K.get("ma"): fr.append({"type": "image_url", "image_url": {"url": anh(K["ma"], res)}, "frame_type": "first_frame"})
    if K.get("cuoi"): fr.append({"type": "image_url", "image_url": {"url": anh(K["cuoi"], res)}, "frame_type": "last_frame"})
    if fr: body["frame_images"] = fr
    neg = p.get("negative") or L["_chung"]["negative"]
    if model.startswith("google/"):
        par = {"negativePrompt": neg}
        if K.get("personGeneration"): par["personGeneration"] = K["personGeneration"]
        body["provider"] = {"options": {"google-vertex": {"parameters": par}}}
    else:
        body["negative_prompt"] = neg
    t0 = now()
    req = urllib.request.Request(API + "/videos", data=json.dumps(body).encode(), method="POST", headers={**HDR, "Content-Type": "application/json"})
    try:
        job = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        msg = e.read()[:400].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("openrouter", msg)
        rec = {"khe": khe, "luot": luot, "status": f"http_{e.code}", "error": msg, "bat_dau": t0, "model": model, "res": res}
        with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        raise SystemExit(f"HTTP {e.code}: {msg}")
    jid = job["id"]; print(khe, luot, model, res, "job", jid, t0, flush=True)
    st = job
    for _ in range(160):
        time.sleep(15); st = get(f"{API}/videos/{jid}")
        if st["status"] in ("completed", "failed", "cancelled", "expired"): break
    t1 = now()
    rec = {"khe": khe, "ma": K.get("ma"), "cuoi": K.get("cuoi"), "luot": luot, "job": jid, "bat_dau": t0, "xong": t1, "status": st["status"],
           "usage": st.get("usage"), "error": st.get("error"), "quy_truoc": q0, "model": model, "res": res, "dur": dur,
           "body": {k: v for k, v in body.items() if k not in ("prompt", "frame_images")}, "prompt": prompt}
    if st["status"] == "completed":
        os.makedirs(OUT, exist_ok=True)
        r = urllib.request.urlopen(urllib.request.Request(f"{API}/videos/{jid}/content?index=0", headers=HDR), timeout=300)
        open(dst, "wb").write(r.read()); rec["tep"] = os.path.relpath(dst, ROOT); rec["tai_xong"] = now()
    time.sleep(5); q1 = quy(); rec["quy_sau"] = q1
    rec["chi_khoa"] = round(q1["khoa_usage"] - q0["khoa_usage"], 5)
    rec["chi_tai_khoan"] = round(q1["total_usage"] - q0["total_usage"], 5)
    rec["chi_phien_khac"] = round(rec["chi_tai_khoan"] - rec["chi_khoa"], 5)
    cost = (st.get("usage") or {}).get("cost")
    amt = float(cost) if cost is not None else (gia if st["status"] == "completed" else 0.0)
    budget.charge("openrouter_usd", amt, {"khe": khe, "ma": K.get("ma"), "luot": luot, "job": jid, "status": st["status"], "model": model, "res": res,
                                          "bat_dau": t0, "xong": t1,
                                          "nguon_so": "usage.cost" if cost is not None else (f"đơn giá {gia}" if st["status"] == "completed" else "failed → 0")})
    with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps({k: rec[k] for k in ("khe", "ma", "luot", "status", "usage", "bat_dau", "xong", "chi_khoa", "chi_phien_khac", "error")}, ensure_ascii=False))
    if budget.canh_bao("openrouter_usd"): print("CẢNH BÁO: chạm mốc báo 80 % openrouter_usd — DỪNG SINH")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
