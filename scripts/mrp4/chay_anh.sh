#!/bin/bash
# NGUỒN: scripts/mr6/chay_anh.sh (repo này, main @ a8741a4) — MR-P4 đổi: phiên mrp4, nhánh MR-P4, lô 5 tranh. Sinh tuần tự + đẩy LFS ≤ 10 phút.
#   bash scripts/mrp4/chay_anh.sh a10 b118 …   ;  LUOT=2 bash scripts/mrp4/chay_anh.sh b003
set -u
cd "$(dirname "$0")/../.." || exit 2
export MR_PHIEN=mrp4; LUOT=${LUOT:-1}; lo=0; t_lo=$(date +%s); NHANH=claude/friendly-hopper-rmvzyy; S=/tmp/claude-0/mrp4/s; mkdir -p $S
day() {
  git add lab/mrp4/anh reports/mrp4/calls.jsonl reports/mrp4/anh/anh_luot.jsonl 2>/dev/null
  bash tools/preflight.sh > $S/pf.log 2>&1; rc=$?
  if [ $rc -ne 0 ]; then echo "PREFLIGHT TRƯỢT"; tail -5 $S/pf.log; exit 3; fi
  git commit -q -m "MR-P4: tranh nhiều lớp lô $(date -u +%H:%M) UTC (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8bBQJCEEAdo462H3Am" || true
  for i in 1 2 3 4; do git push -q -u origin $NHANH && break; sleep $((2**i)); done
  echo "ĐẨY $(date -u +%H:%M:%S)"; lo=0; t_lo=$(date +%s)
}
for id in "$@"; do
  python3 scripts/mrp4/anh.py "$id" "$LUOT" > $S/anh_out.txt 2>&1; rc=$?; tail -2 $S/anh_out.txt
  if [ $rc -ne 0 ]; then echo "LỖI ở $id — DỪNG"; day; exit 1; fi
  lo=$((lo+1))
  if [ $lo -ge 5 ] || [ $(( $(date +%s) - t_lo )) -ge 300 ]; then day; fi
  if python3 -c "import sys;sys.path.insert(0,'scripts/cp');import budget;sys.exit(0 if budget.canh_bao('openrouter_usd') else 1)"; then
    echo "MỐC 80 % — DỪNG SINH"; day; exit 4; fi
done
[ $lo -gt 0 ] && day
echo XONG
