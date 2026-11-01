#!/usr/bin/env python3
"""MR-5 · Đọc số dư (GET miễn phí): OpenRouter /api/v1/credits + /api/v1/key; ElevenLabs /v1/user/subscription.
  python3 scripts/mr5/so_du.py reports/mr5/so_du_truoc.json
Khoá do proxy tiêm; gửi giá trị giả. Không ghi khoá ra tệp."""
import json, sys, time, urllib.request
def g(u, h): return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=60))
OR = {"Authorization": "Bearer sk-or-dummy-proxy-injects"}; EL = {"xi-api-key": "dummy-proxy-injects"}
c = g("https://openrouter.ai/api/v1/credits", OR)["data"]; k = g("https://openrouter.ai/api/v1/key", OR)["data"]
s = g("https://api.elevenlabs.io/v1/user/subscription", EL)
o = {"t": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
     "openrouter": {"total_credits": c["total_credits"], "total_usage": round(c["total_usage"], 5),
                    "con": round(c["total_credits"] - c["total_usage"], 5), "khoa_usage": k["usage"], "khoa_limit": k.get("limit")},
     "elevenlabs": {"character_count": s["character_count"], "character_limit": s["character_limit"],
                    "con": s["character_limit"] - s["character_count"], "reset_unix": s.get("next_character_count_reset_unix"), "tier": s.get("tier")}}
txt = json.dumps(o, ensure_ascii=False, indent=1); print(txt)
if len(sys.argv) > 1: open(sys.argv[1], "w").write(txt)
