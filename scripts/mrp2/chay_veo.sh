#!/bin/bash
# MR-P2 · Chạy khe Veo ảnh→video TUẦN TỰ (V7), mỗi clip xong: preflight riêng (mã 0) → commit → đẩy LFS (≤ 10 phút).
#   bash scripts/mrp2/chay_veo.sh V1 V2 …   ;   LUOT=2 bash scripts/mrp2/chay_veo.sh V3
set -u; cd "$(dirname "$0")/../.." || exit 2; export MR_PHIEN=mrp2; LUOT=${LUOT:-1}; NH=claude/brave-faraday-vtsny1
for k in "$@"; do
  python3 scripts/mrp2/veo.py "$k" "$LUOT" || { echo "LỖI $k — DỪNG"; exit 1; }
  for t in 1 2 3 4 5 6; do
    while [ -f .git/index.lock ]; do sleep 2; done
    git add lab/mrp2/veo reports/mrp2/veo_luot.jsonl reports/mrp2/calls.jsonl || { sleep 5; continue; }
    bash tools/preflight.sh > "${MRP2_TMP:-/tmp}/pfv.log" 2>&1; rc=$?
    if [ $rc -ne 0 ]; then echo "PREFLIGHT TRƯỢT ($k) — không commit"; cat "${MRP2_TMP:-/tmp}/pfv.log" | tail -5; exit 1; fi
    git commit -q -m "MR-P2: clip Veo ảnh→video $k lượt $LUOT (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8cgFeso3QP7uSSWBEY" && break
    sleep 5
  done
  for i in 1 2 3 4; do git push -q -u origin $NH && break; sleep $((2**i)); done
  echo "ĐẨY $k $(date -u +%H:%M:%S)"
done
