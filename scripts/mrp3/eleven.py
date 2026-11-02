#!/usr/bin/env python3
"""MR-P3 · ElevenLabs Sound Effects + Eleven Music (TRẢ TIỀN — ký tự TÍNH, qua budget.py, trần mrp3 elevenlabs_chars 3.000).
  MR_PHIEN=mrp3 python3 scripts/mrp3/eleven.py sfx <khoá>      # một tiếng động theo SFX[khoá]
  MR_PHIEN=mrp3 python3 scripts/mrp3/eleven.py nhac <khoá>     # một bản nhạc theo NHAC[khoá] (composition plan theo hồi)
Đo chi THẬT = chênh character_count của /v1/user/subscription trước/sau (ghi cả hai số). 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả. Ra: lab/mrp3/am/<khoá>.mp3 (LFS, tệp tốn tiền) + reports/mrp3/am/eleven_luot.jsonl."""
import json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp"))
import budget  # noqa: E402
API = "https://api.elevenlabs.io"; HDR = {"xi-api-key": "dummy-proxy-injects", "Content-Type": "application/json"}
OUT = os.path.join(ROOT, "lab", "mrp3", "am"); SO = os.path.join(ROOT, "reports", "mrp3", "am", "eleven_luot.jsonl")
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
# Tiếng động thử (so với CC0 cùng vai)
SFX = {
    "e_rung_dt": {"text": "A smartphone vibrating twice on a wooden kitchen table, close, quiet room.", "duration_seconds": 2.0, "prompt_influence": 0.5},
    "e_va_cham": {"text": "Deep cinematic low impact hit with a soft sub-bass boom and a long dark tail, no music, no voice.", "duration_seconds": 3.0, "prompt_influence": 0.5},
    "e_dong_ho": {"text": "A single old wall clock ticking steadily, dry, close, tense quiet room.", "duration_seconds": 4.0, "prompt_influence": 0.5},
}
# Nhạc theo hồi cho P15–P17 của đoạn thử (ru ngủ → đếm ngược → dồn → lật ở cảnh bắt). Không lời, không giọng.
NHAC = {
    "m_p15_17": {"composition_plan": {
        "positive_global_styles": ["dark cinematic documentary underscore", "minimal", "piano and low strings", "subtle synth pulse", "true crime"],
        "negative_global_styles": ["vocals", "lyrics", "choir", "upbeat", "pop", "rock drums", "EDM drop"],
        "sections": [
            {"section_name": "Lull", "positive_local_styles": ["soft warm felt piano", "slow", "deceptively calm", "gentle pad"], "negative_local_styles": ["percussion"], "duration_ms": 17500, "lines": []},
            {"section_name": "Countdown", "positive_local_styles": ["ticking muted pulse", "clock-like staccato", "uneasy", "rising tension", "low strings ostinato"], "negative_local_styles": ["melody resolution"], "duration_ms": 9000, "lines": []},
            {"section_name": "Closing in", "positive_local_styles": ["building", "driving low strings", "heavier pulse", "crescendo", "urgent"], "negative_local_styles": ["release"], "duration_ms": 13000, "lines": []},
            {"section_name": "Aftermath", "positive_local_styles": ["sudden stop then sparse low drone", "single distant piano note", "empty"], "negative_local_styles": ["drums", "melody"], "duration_ms": 8500, "lines": []}]}},
}


def sub():
    r = json.load(urllib.request.urlopen(urllib.request.Request(API + "/v1/user/subscription", headers=HDR), timeout=60))
    return {"character_count": r["character_count"], "character_limit": r["character_limit"]}


def post(path, body):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(), method="POST", headers=HDR)
    try:
        return urllib.request.urlopen(req, timeout=300).read()
    except urllib.error.HTTPError as e:
        msg = e.read()[:400].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("elevenlabs", msg)
        raise SystemExit(f"HTTP {e.code}: {msg}")


def main(loai, k):
    if os.environ.get("MR_PHIEN") != "mrp3": raise SystemExit("đặt MR_PHIEN=mrp3")
    dst = os.path.join(OUT, k + ".mp3")
    if os.path.exists(dst): raise SystemExit(f"{dst} đã có — không gửi lại")
    if loai == "sfx": body = SFX[k]; est = 100 * body["duration_seconds"] / 2 + 100; path = "/v1/sound-generation?output_format=mp3_44100_128"
    else:
        body = dict(NHAC[k]); body["model_id"] = "music_v1"
        ms = sum(s["duration_ms"] for s in body["composition_plan"]["sections"]); est = 900 * ms / 60000; path = "/v1/music?output_format=mp3_44100_128"
    budget.check("elevenlabs_chars", est)
    if budget.canh_bao("elevenlabs_chars"): raise SystemExit("đã chạm mốc báo 80 % — DỪNG SINH")
    s0 = sub(); t0 = now(); b = post(path, body); t1 = now()
    os.makedirs(OUT, exist_ok=True); open(dst, "wb").write(b)
    s1 = s0  # số dư cập nhật trễ (đo MR-P3: 4 s chưa đổi, ~25 s đã đổi) → đợi tới khi đổi, tối đa 90 s
    for _ in range(18):
        time.sleep(5); s1 = sub()
        if s1["character_count"] != s0["character_count"]: time.sleep(5); s1 = sub(); break
    tinh = s1["character_count"] - s0["character_count"]
    budget.charge("elevenlabs_chars", tinh, {"loai": loai, "khoa": k, "uoc": round(est), "bat_dau": t0, "xong": t1, "nguon_so": "chênh character_count /v1/user/subscription"})
    rec = {"loai": loai, "khoa": k, "body": body, "bat_dau": t0, "xong": t1, "truoc": s0, "sau": s1, "ky_tu_tinh": tinh, "byte": len(b), "tep": os.path.relpath(dst, ROOT)}
    os.makedirs(os.path.dirname(SO), exist_ok=True)
    with open(SO, "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(k, "ký tự tính", tinh, "ước", round(est))
    if budget.canh_bao("elevenlabs_chars"): print("CẢNH BÁO: chạm mốc báo 80 % elevenlabs_chars — DỪNG SINH")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
