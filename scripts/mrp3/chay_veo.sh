#!/bin/bash
# MR-P3 · Chạy khe clip TUẦN TỰ (V7), mỗi clip xong: preflight riêng (mã 0) → commit → đẩy LFS (≤ 10 phút).
#   bash scripts/mrp3/chay_veo.sh V01 V02 …   ;   LUOT=2 bash scripts/mrp3/chay_veo.sh V03
# NGUỒN: scripts/mrp2/chay_veo.sh (repo này, main @ 33ce227) — đổi phiên, nhánh, đường dẫn; khe lỗi/bị lọc không dừng cả lô.
set -u; cd "$(dirname "$0")/../.." || exit 2; export MR_PHIEN=mrp3; LUOT=${LUOT:-1}; NH=ccr-61933171-f4wlwf
T=${MRP3_TMP:-/tmp/claude-0/mrp3}; mkdir -p "$T"
for k in "$@"; do
  python3 scripts/mrp3/veo.py "$k" "$LUOT"; rc=$?
  [ $rc -eq 3 ] && { echo "402/DỪNG"; exit 3; }
  for t in 1 2 3 4 5 6; do
    while [ -f .git/index.lock ]; do sleep 2; done
    git add lab/mrp3/veo reports/mrp3/veo_luot.jsonl reports/mrp3/calls.jsonl 2>/dev/null
    git diff --cached --quiet && break
    bash tools/preflight.sh > "$T/pfv.log" 2>&1; pf=$?
    if [ $pf -ne 0 ]; then echo "PREFLIGHT TRƯỢT ($k) — không commit"; tail -5 "$T/pfv.log"; exit 1; fi
    git commit -q -m "MR-P3: clip $k lượt $LUOT (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8ZLKmcZB7Jif4vde9Z" && break
    sleep 5
  done
  for i in 1 2 3 4; do git push -q -u origin $NH 2>&1 | tail -2 && break; sleep $((2**i)); done
  echo "ĐẨY $k $(date -u +%H:%M:%S)"
  MR_PHIEN=mrp3 python3 -c "import sys;sys.path.insert(0,'scripts/cp');import budget;sys.exit(4 if budget.canh_bao('openrouter_usd') else 0)" || { echo "MỐC 80 % — DỪNG SINH"; exit 4; }
done
