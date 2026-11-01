# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/cp/budget.py
# (chép ở MR-0, 01/11/2026). ĐÃ SỬA: bảng trần LP (cp, m2a … mc2) thay bằng bảng trần phiên MR; biến LP_PHIEN → MR_PHIEN;
# thêm khoản openrouter_usd vào bảng trần; Gemini402 → Quy402 dùng chung mọi dịch vụ (Gemini402 giữ làm bí danh).
# Phần lõi (sổ calls.jsonl, spent/pending_est/check/charge/canh_bao) giữ nguyên logic gốc.
"""[MR] Trần chi phí CỨNG theo phiên Money Reroute.
Sổ = reports/<phiên>/calls.jsonl (commit). Tổng chi tính lại từ sổ mỗi lần kiểm (không sổ tạm → không lệch khi container mới).
check() chạy TRƯỚC mỗi lệnh/lô với ước chi; charge() ghi chi THẬT từ usage/đối soát của phản hồi.
Lỗi 402 (quỹ trả trước cạn) ở BẤT KỲ dịch vụ nào → raise Quy402: DỪNG ngay, không thử lặp, không vá (CLAUDE.md).
  MR_PHIEN=mr1 python3 scripts/cp/budget.py      # in đã chi / đang chờ / trần của phiên
Thêm phiên mới: điều phối ghi trần trong lệnh → phiên thêm MỘT dòng vào CAPS_PHIEN (và DUNG_BAO nếu lệnh có mốc báo), ghi căn cứ lệnh bên cạnh."""
import json, os, time, fcntl
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PHIEN = os.environ.get("MR_PHIEN", "mr0")
LOG = os.path.join(ROOT, "reports", PHIEN, "calls.jsonl")
LAB = os.path.join(ROOT, "lab", PHIEN); REP = os.path.join(ROOT, "reports", PHIEN)

KHOAN = ("gemini_usd", "openrouter_usd", "elevenlabs_chars", "claude_usd", "youtube_units", "openai_usd")
# Bảng trần theo phiên. Khoản không ghi = 0 = CẤM GỌI. Phiên không có trong bảng = mọi khoản 0.
CAPS_PHIEN = {
    "mr0": {},  # MR-0 (khởi tạo repo, lệnh 01/11/2026): 0 USD API mọi khoản; chỉ đọc số dư (GET miễn phí, không qua check()).
}
CAPS = {k: float(CAPS_PHIEN.get(PHIEN, {}).get(k, 0.0)) for k in KHOAN}
# Mốc báo theo phiên: chạm mốc (đã ghi + đang chờ) mà còn > 20 % việc → DỪNG SINH, báo điều phối. Dạng {"mr1": {"openrouter_usd": 8.0}}.
DUNG_BAO_PHIEN = {}
DUNG_BAO = DUNG_BAO_PHIEN.get(PHIEN, {})

class BudgetStop(RuntimeError): pass
class Quy402(RuntimeError): pass
Gemini402 = Quy402  # bí danh để mã chép từ lost-places-lab chạy được

def spent():
    s = {k: 0.0 for k in CAPS}
    if os.path.exists(LOG):
        for l in open(LOG):
            if l.strip():
                d = json.loads(l); s[d["kind"]] = s.get(d["kind"], 0) + float(d.get("amount", 0))
    return s

def pending_est(kind="gemini_usd"):
    """Ước chi của các lô đã gửi nhưng chưa tải kết quả (lab/<phiên>/batch/*.json, chưa "charged") — tính vào khi kiểm trần.
    Tệp lô ghi "kind" (mặc định gemini_usd như bản gốc)."""
    tot = 0.0; d = os.path.join(LAB, "batch")
    if os.path.isdir(d):
        for f in os.listdir(d):
            if f.endswith(".json"):
                j = json.load(open(os.path.join(d, f)))
                if not j.get("charged") and j.get("kind", "gemini_usd") == kind: tot += j.get("est_usd", 0)
    return tot

def check(kind, est):
    if kind not in CAPS: raise BudgetStop(f"{kind}: khoản lạ, không có trong bảng trần")
    s = spent()
    if CAPS[kind] == 0 and est > 0: raise BudgetStop(f"{kind}: trần 0 ở phiên {PHIEN}, cấm gọi")
    used = s.get(kind, 0) + pending_est(kind)
    if used + est > CAPS[kind]:
        raise BudgetStop(f"{kind}: đã ghi + đang chờ {used:.3f} + ước {est:.3f} > trần {CAPS[kind]}")

def charge(kind, amount, meta):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        with open(LOG, "a") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "kind": kind, "amount": round(amount, 6), **meta}, ensure_ascii=False) + "\n")

def bao_402(dich_vu, chi_tiet=""):
    """Gọi ngay khi nhận HTTP 402 từ bất kỳ dịch vụ nào: ghi sổ (amount 0) rồi raise Quy402 → phiên DỪNG."""
    charge("gemini_usd" if dich_vu == "gemini" else f"{dich_vu}_usd" if f"{dich_vu}_usd" in CAPS else "gemini_usd", 0.0,
           {"su_kien": "402", "dich_vu": dich_vu, "chi_tiet": str(chi_tiet)[:200]})
    raise Quy402(f"{dich_vu}: 402 quỹ cạn — DỪNG phiên, không thử lặp, chờ chủ dự án nạp")

def canh_bao(kind=None):
    """→ True nếu có khoản (hoặc khoản `kind`) đã ghi + đang chờ ≥ mốc báo của phiên."""
    s = spent()
    for k, moc in DUNG_BAO.items():
        if (kind is None or k == kind) and s.get(k, 0) + pending_est(k) >= moc: return True
    return False

if __name__ == "__main__":
    print(json.dumps({"phien": PHIEN, "spent": spent(), "pending_est": {k: round(pending_est(k), 4) for k in KHOAN if k.endswith("_usd")},
                      "caps": CAPS, "dung_bao": DUNG_BAO}, ensure_ascii=False))
