#!/bin/bash
# MR-6 · Chạy khe Veo ảnh→video TUẦN TỰ (V7), mỗi clip xong: preflight riêng (mã 0) → commit → đẩy LFS (≤ 10 phút).
#   bash scripts/mr6/chay_veo.sh K1 K2 …   ;   LUOT=2 bash scripts/mr6/chay_veo.sh K3
set -u; cd "$(dirname "$0")/../.." || exit 2; export MR_PHIEN=mr6; LUOT=${LUOT:-1}
for k in "$@"; do
  python3 scripts/mr6/veo.py "$k" "$LUOT" || { echo "LỖI $k — DỪNG"; exit 1; }
  for t in 1 2 3 4 5 6; do
    while [ -f .git/index.lock ]; do sleep 2; done
    git add lab/mr6/veo reports/mr6/veo_luot.jsonl reports/mr6/calls.jsonl && \
    bash tools/preflight.sh > /tmp/claude-0/pfv.log 2>&1 && \
    git commit -q -m "MR-6: clip Veo ảnh→video $k lượt $LUOT (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8Z2YCRYKVxAqpATwFF" && break
    sleep 5
  done
  for i in 1 2 3 4; do git push -q -u origin ccr-93d57c5c-q2ib0q && break; sleep $((2**i)); done
  echo "ĐẨY $k $(date -u +%H:%M:%S)"
done
