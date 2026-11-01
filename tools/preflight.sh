#!/bin/bash
# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — tools/preflight.sh (chép nguyên văn ở MR-0, 01/11/2026; chưa sửa — bước tools/k/khoa.py và checks/lock.py tự bỏ qua khi tệp không tồn tại)
# NỀN TẢNG · kiểm trước commit/push (chép từ cine-lab nen-tang@7255aa4, phiên Nền tảng 15/10/2026; chỉnh cho lost-places-lab 22/10/2026:
#   bỏ bước checks/lock.py vì repo này chưa có bộ luật K; thêm set -o pipefail). Mọi phiên chạy trước MỌI commit/đẩy; có thể cài làm git hook.
#   bash tools/preflight.sh                    # tệp đang stage (mặc định)
#   bash tools/preflight.sh --range origin/main..HEAD   # các commit sắp đẩy
#   bash tools/preflight.sh --all              # toàn repo (kiểm định kỳ)
# Kiểm: email / khoá bí mật · tệp > 5 MB ngoài LFS cho phép (tools/lfs-allow.txt) · checks/lock.py --verify · dấu xung đột merge ·
#       tệp giấy phép cho mỗi dòng sổ footage/ảnh ngoài · (báo) ảnh tư liệu chưa có trong RIGHTS/SOURCES. Chi tiết: scripts/common/preflight_scan.py.
# Cài hook (một lần mỗi bản clone; hook không theo git nên mỗi container mới phải cài lại — đặt trong scripts/env/verify.sh hoặc đầu phiên):
#   ln -sf ../../tools/preflight.sh .git/hooks/pre-commit
#   ln -sf ../../tools/preflight.sh .git/hooks/pre-push
# Bỏ qua khẩn cấp (phải ghi lý do trong báo cáo): git commit --no-verify / git push --no-verify.
set -u -o pipefail
REPO=$(cd "$(dirname "$(readlink -f "$0")")/.." && pwd); cd "$REPO" || exit 2
PY=/opt/cine/bin/python; [ -x $PY ] || PY=python3
HOOK=$(basename "$0"); ARGS=("$@")
if [ "$HOOK" = pre-push ]; then   # stdin: <local ref> <local sha> <remote ref> <remote sha>
  ARGS=(); Z=0000000000000000000000000000000000000000
  while read -r lref lsha rref rsha; do [ "$lsha" = $Z ] && continue
    if [ "$rsha" = $Z ]; then base=$(git merge-base "$lsha" origin/main 2>/dev/null || git rev-list --max-parents=0 "$lsha" | tail -1); else base=$rsha; fi
    ARGS=(--range "$base..$lsha"); done
  [ ${#ARGS[@]} -eq 0 ] && exit 0
elif [ "$HOOK" = pre-commit ]; then ARGS=(--staged); fi
[ ${#ARGS[@]} -eq 0 ] && ARGS=(--staged)
rc=0
$PY scripts/common/preflight_scan.py "${ARGS[@]}" || rc=1
if [ -f checks/lock.py ]; then
  if out=$($PY checks/lock.py --verify 2>&1); then echo "lock.py --verify: KHỚP"; else echo "CHẶN lock.py --verify: $out" | head -5; rc=1; fi
fi
if [ -f tools/k/khoa.py ]; then   # R-50: khoá luật phiên K (docs/K-LUAT.md) — chỉ phiên K được đổi tools/k + khoá lại
  if out=$($PY tools/k/khoa.py kiem 2>&1); then echo "khoa K: KHỚP"; else echo "CHẶN khoá K: $out" | head -5; rc=1; fi
fi
[ $rc = 0 ] && echo "PREFLIGHT ĐẠT" || echo "PREFLIGHT TRƯỢT — sửa các mục CHẶN rồi chạy lại"
exit $rc
