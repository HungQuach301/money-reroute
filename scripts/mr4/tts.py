#!/usr/bin/env python3
"""MR-4 · TTS lời tập 1 theo đoạn (ElevenLabs eleven_v4, giọng kênh kozBJGqBNTqfBBClLNCL). TRẢ TIỀN — qua budget.py.
  MR_PHIEN=mr4 python3 scripts/mr4/tts.py P00 P01 P02          # thu các đoạn
  MR_PHIEN=mr4 python3 scripts/mr4/tts.py --lai P05 --ly-do "…"  # thu lại (≤ 1 lần/đoạn, tệp P05_l2.mp3)
  MR_PHIEN=mr4 python3 scripts/mr4/tts.py --dem                  # chỉ đếm ký tự gửi (0 USD)
Lời lấy nguyên văn từ docs/tap01-1inmm/loi.json (đóng băng sau G1), chỉ câu "doc" ≠ false, nối bằng dấu cách, áp bảng phát âm
PHAT_AM của scripts/mr3/loi_md.py (SEC → S-E-C, …). Không sửa chữ nào.
Ký tự TÍNH = chênh character_count của /v1/user/subscription trước/sau mỗi lượt (đo thật); header phản hồi ghi kèm để đối chiếu.
Ước trước lượt (check) dùng hệ số xấu nhất 1,0 (bảng /v1/models: eleven_v4 character_cost_multiplier 1.0). 402 → bao_402 → DỪNG.
Khoá API do proxy tiêm; gửi giá trị giả."""
import json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "cp")); sys.path.insert(0, os.path.join(ROOT, "scripts", "mr3"))
import budget  # noqa: E402
from loi_md import tts as phat_am  # noqa: E402

VOICE = "kozBJGqBNTqfBBClLNCL"; MODEL = "eleven_v4"; FMT = "mp3_44100_128"
API = "https://api.elevenlabs.io"; HDR = {"xi-api-key": "dummy-proxy-injects"}
OUT = os.path.join(ROOT, "lab", "mr4", "tts"); SO = os.path.join(ROOT, "reports", "mr4", "tts_luot.jsonl")


def doan_text():
    d = json.load(open(os.path.join(ROOT, "docs", "tap01-1inmm", "loi.json")))
    o = {}
    for c in d["cau"]:
        if c.get("doc", True): o.setdefault(c["doan"], []).append((c["id"], phat_am(c["loi"])))
    return o


def so_du():
    r = urllib.request.urlopen(urllib.request.Request(API + "/v1/user/subscription", headers=HDR), timeout=60)
    j = json.load(r); return j["character_count"], j["character_limit"]


def thu(doan, text, ten, ly_do=""):
    n = len(text)
    budget.check("elevenlabs_chars", n); budget.check_gui("elevenlabs_chars", n)
    c0, lim = so_du()
    body = json.dumps({"text": text, "model_id": MODEL}).encode()
    req = urllib.request.Request(f"{API}/v1/text-to-speech/{VOICE}?output_format={FMT}", data=body, method="POST",
                                 headers={**HDR, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    try:
        r = urllib.request.urlopen(req, timeout=600); audio = r.read(); h = dict(r.headers)
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode("utf-8", "replace")
        if e.code == 402: budget.bao_402("elevenlabs", msg)
        # lượt lỗi khác: vẫn đọc chênh số dư, ghi sổ rồi dừng
        time.sleep(3); c1, _ = so_du()
        budget.charge("elevenlabs_chars", c1 - c0, {"doan": doan, "loi_http": e.code, "gui": n, "chi_tiet": msg})
        raise SystemExit(f"{doan}: HTTP {e.code} {msg}")
    os.makedirs(OUT, exist_ok=True); p = os.path.join(OUT, ten + ".mp3"); open(p, "wb").write(audio)
    # chênh số dư có thể trễ vài giây → đọc lại tới khi đổi (tối đa ~30 s)
    c1 = c0
    for _ in range(10):
        time.sleep(3); c1, _ = so_du()
        if c1 != c0: break
    hdr_cc = {k: v for k, v in h.items() if "character" in k.lower() or k.lower() in ("request-id", "history-item-id")}
    hc = next((int(v) for k, v in h.items() if k.lower() == "character-cost"), None)
    # /subscription có thể trễ (đo MR-4 P00: không đổi sau 30 s) → ký tự tính = max(chênh số dư, header Character-Cost);
    # đối soát tổng bằng chênh /subscription đầu–cuối phiên ở báo cáo.
    tinh = max(c1 - c0, hc or 0)
    meta = {"doan": doan, "tep": os.path.relpath(p, ROOT), "gui": n, "he_so": round(tinh / n, 4) if n else None,
            "header": hdr_cc, "bat_dau": t0, "ly_do": ly_do, "chenh_sub": c1 - c0, "character_cost": hc}
    budget.charge("elevenlabs_chars", tinh, meta)
    os.makedirs(os.path.dirname(SO), exist_ok=True)
    with open(SO, "a") as f: f.write(json.dumps({**meta, "tinh": tinh, "count_truoc": c0, "count_sau": c1}, ensure_ascii=False) + "\n")
    print(json.dumps({"doan": doan, "gui": n, "tinh": tinh, "he_so": meta["he_so"], "header": hdr_cc, "tep": meta["tep"]}, ensure_ascii=False))
    if budget.canh_bao("elevenlabs_chars"): print("CẢNH BÁO: chạm mốc báo 80 % elevenlabs_chars")
    return tinh


if __name__ == "__main__":
    o = doan_text(); a = sys.argv[1:]
    if not a or a[0] == "--dem":
        for k, v in o.items(): print(k, len(" ".join(t for _, t in v)))
        print("tong", sum(len(" ".join(t for _, t in v)) for v in o.values())); sys.exit(0)
    if a[0] == "--lai":
        k = a[1]; ly = a[a.index("--ly-do") + 1] if "--ly-do" in a else ""
        if os.path.exists(os.path.join(OUT, k + "_l2.mp3")): raise SystemExit(f"{k}: đã thu lại 1 lần — không thu lần 3")
        thu(k, " ".join(t for _, t in o[k]), k + "_l2", ly); sys.exit(0)
    for k in a:
        if os.path.exists(os.path.join(OUT, k + ".mp3")): print(k, "đã có, bỏ qua"); continue
        thu(k, " ".join(t for _, t in o[k]), k)
