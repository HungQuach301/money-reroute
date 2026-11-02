#!/bin/bash
# MR-5 · Một lượt Veo (TRẢ TIỀN) rồi đẩy LFS ngay (≤ 10 phút sau khi sinh): veo.py → preflight (chạy riêng, mã thoát 0) → commit → push.
#   bash scripts/mr5/chay_khe.sh V01 1
set -u
cd "$(dirname "$0")/../.." || exit 2
KHE=$1; L=$2; B=ccr-af44ed0c-12rbdy
MR_PHIEN=mr5 python3 scripts/mr5/veo.py "$KHE" "$L"; rc=$?
[ $rc -ne 0 ] && { echo "veo.py rc=$rc — DỪNG"; exit $rc; }
git add lab/mr5/veo/ reports/mr5/
bash tools/preflight.sh; p=$?
[ $p -ne 0 ] && { echo "PREFLIGHT TRƯỢT — chưa commit"; exit 3; }
git commit -q -m "MR-5: Veo ${KHE} lượt ${L} (LFS)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019Gns8ZZCRCFLbgBr9oe5qS" || exit 4
for d in 2 4 8 16; do git push -q -u origin $B && break; sleep $d; done
echo "đẩy xong $(date -u +%H:%M:%S)"
