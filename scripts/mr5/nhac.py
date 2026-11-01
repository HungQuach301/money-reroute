#!/usr/bin/env python3
"""MR-5 · Nhạc tập 1 bằng Eleven Music (POST /v1/music, model music_v1, composition_plan, không lời). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mr5 python3 scripts/mr5/nhac.py N1_mo --uoc 1500    # ước xấu nhất (ký tự tính) cho check() trước lượt
Kế hoạch: reports/mr5/nhac/ke_hoach.json. Ra: lab/mr5/nhac/<tên>.mp3. Sổ lượt: reports/mr5/nhac_luot.jsonl.
Ký tự TÍNH: header phản hồi (character-cost nếu có) + chênh character_count của /v1/user/subscription trước/sau (đọc lại sau 60 s
vì /subscription cập nhật trễ — bài học MR-4). Sổ trần ghi số chênh /subscription nếu đo được, ngược lại header. 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả."""
import json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402
API = "https://api.elevenlabs.io"; HDR = {"xi-api-key": "dummy-proxy-injects"}
KH = os.path.join(ROOT, "reports", "mr5", "nhac", "ke_hoach.json"); OUT = os.path.join(ROOT, "lab", "mr5", "nhac")
SO = os.path.join(ROOT, "reports", "mr5", "nhac_luot.jsonl")
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def dung():
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(API + "/v1/user/subscription", headers=HDR), timeout=60))
    except urllib.error.HTTPError as e:
        if e.code == 402: budget.bao_402("elevenlabs", e.read()[:200])
        return None
    return j["character_count"]


def main(ten, uoc, lai=False):
    if os.environ.get("MR_PHIEN") != "mr5": raise SystemExit("đặt MR_PHIEN=mr5")
    plan = json.load(open(KH))[ten]["composition_plan"]
    dst = os.path.join(OUT, ten + ("_l2" if lai else "") + ".mp3")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    budget.check("elevenlabs_chars", uoc)
    if budget.canh_bao("elevenlabs_chars"): raise SystemExit("đã chạm mốc báo 80 % — DỪNG, báo")
    c0 = dung(); t0 = now()
    body = {"composition_plan": plan, "model_id": "music_v1"}
    req = urllib.request.Request(f"{API}/v1/music?output_format=mp3_44100_192", data=json.dumps(body).encode(), method="POST",
                                 headers={**HDR, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        r = urllib.request.urlopen(req, timeout=900); audio = r.read(); h = dict(r.headers)
    except urllib.error.HTTPError as e:
        msg = e.read()[:400].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("elevenlabs", msg)
        time.sleep(60); c1 = dung()
        budget.charge("elevenlabs_chars", max(0, (c1 or c0) - c0) if c0 is not None else 0,
                      {"nhac": ten, "loi_http": e.code, "chi_tiet": msg, "nguon_so": "chênh /subscription"})
        raise SystemExit(f"{ten}: HTTP {e.code} {msg}")
    os.makedirs(OUT, exist_ok=True); open(dst, "wb").write(audio); t1 = now()
    hdr = {k: v for k, v in h.items() if "cost" in k.lower() or "character" in k.lower() or k.lower() in ("request-id", "song-id")}
    hc = next((int(float(v)) for k, v in h.items() if k.lower() == "character-cost"), None)
    time.sleep(60); c1 = dung()
    chenh = (c1 - c0) if (c0 is not None and c1 is not None) else None
    tinh = chenh if chenh else hc
    if tinh is None: raise SystemExit(f"{ten}: không đo được ký tự tính — tệp đã lưu {dst}; đối soát tay")
    dai_ms = sum(s["duration_ms"] for s in plan["sections"])
    meta = {"nhac": ten, "tep": os.path.relpath(dst, ROOT), "dai_ms_ke_hoach": dai_ms, "bat_dau": t0, "xong": t1,
            "header": hdr, "character_cost_header": hc, "sub_truoc": c0, "sub_sau": c1, "chenh_sub": chenh,
            "nguon_so": "chênh /subscription" if chenh else "header character-cost",
            "ky_tu_moi_phut": round(tinh / (dai_ms / 60000), 1)}
    budget.charge("elevenlabs_chars", tinh, meta)
    with open(SO, "a") as f: f.write(json.dumps({**meta, "tinh": tinh}, ensure_ascii=False) + "\n")
    print(json.dumps({**meta, "tinh": tinh}, ensure_ascii=False))
    if budget.canh_bao("elevenlabs_chars"): print("CẢNH BÁO: chạm mốc báo 80 % elevenlabs_chars")


if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0], float(a[a.index("--uoc") + 1]), "--lai" in a)
