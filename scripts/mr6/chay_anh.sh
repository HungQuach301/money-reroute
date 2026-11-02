#!/bin/bash
# MR-6 · Sinh tranh tuần tự + đẩy LFS theo lô (≤ 10 phút sau sinh, CLAUDE.md). Mỗi lô: preflight chạy RIÊNG, mã thoát 0 mới commit/đẩy.
#   bash scripts/mr6/chay_anh.sh b001 b002 …     (lượt 1) ;  LUOT=2 bash scripts/mr6/chay_anh.sh b014
# Dừng ngay khi một lượt lỗi (402 → Quy402 → mã ≠ 0) hoặc chạm mốc báo 80 % (in cảnh báo, để phiên quyết).
set -u
cd "$(dirname "$0")/../.." || exit 2
export MR_PHIEN=mr6; LUOT=${LUOT:-1}; lo=0; t_lo=$(date +%s)
day() {
  git add lab/mr6/anh reports/mr6/calls.jsonl reports/mr6/anh_luot.jsonl 2>/dev/null
  bash tools/preflight.sh > /tmp/claude-0/pf.log 2>&1; rc=$?
  if [ $rc -ne 0 ]; then echo "PREFLIGHT TRƯỢT"; tail -5 /tmp/claude-0/pf.log; exit 3; fi
  git commit -q -m "MR-6: tranh L1 lô $(date -u +%H:%M) UTC (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8Z2YCRYKVxAqpATwFF" || true
  for i in 1 2 3 4; do git push -q -u origin ccr-93d57c5c-q2ib0q && break; sleep $((2**i)); done
  echo "ĐẨY $(date -u +%H:%M:%S)"; lo=0; t_lo=$(date +%s)
}
for id in "$@"; do
  python3 scripts/mr6/anh.py "$id" "$LUOT" > /tmp/claude-0/anh_out.txt 2>&1; rc=$?; cat /tmp/claude-0/anh_out.txt | tail -2
  if [ $rc -ne 0 ]; then
    if grep -q "MẤT KẾT NỐI" /tmp/claude-0/anh_out.txt && [ ! -f "lab/mr6/anh/${id}_l$LUOT.png" ]; then
      echo "THỬ LẠI 1 LẦN (mất kết nối) $id"; sleep 5; python3 scripts/mr6/anh.py "$id" "$LUOT" || { echo "LỖI lần 2 ở $id — bỏ qua"; }
    else echo "LỖI ở $id — DỪNG"; day; exit 1; fi
  fi
  lo=$((lo+1))
  if [ $lo -ge 12 ] || [ $(( $(date +%s) - t_lo )) -ge 300 ]; then day; fi
  if python3 -c "import sys;sys.path.insert(0,'scripts/cp');import budget;sys.exit(0 if budget.canh_bao('openrouter_usd') else 1)"; then
    echo "MỐC 80 % — DỪNG SINH, phiên quyết"; day; exit 4; fi
done
[ $lo -gt 0 ] && day
echo XONG
