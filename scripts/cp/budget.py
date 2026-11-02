# NGUỒN: HungQuach301/lost-places-lab @ ae22e370700d6dc254974588b824802d3edb2406 — scripts/cp/budget.py
# (chép ở MR-0, 01/11/2026). ĐÃ SỬA: bảng trần LP (cp, m2a … mc2) thay bằng bảng trần phiên MR; biến LP_PHIEN → MR_PHIEN;
# thêm khoản openrouter_usd vào bảng trần; Gemini402 → Quy402 dùng chung mọi dịch vụ (Gemini402 giữ làm bí danh).
# MR-1 (01/11/2026): thêm dòng trần mr1; bao_402() ghi đúng khoản của từng dịch vụ (KHOAN_DICH_VU); thêm YT_DON_GIA,
# TRAN_LUOT_PHIEN, luot(), check_yt() cho YouTube Data.
# MR-K1 (01/11/2026): thêm dòng trần mrk1 (youtube_units 2000) + TRAN_LUOT_PHIEN mrk1 (search.list 50) theo lệnh [MR · MR-K1] bước 0.
# MR-5 (02/11/2026): thêm dòng trần mr5 + mốc báo 80 % theo lệnh [MR · MR-5] bước 0.
# MR-P1 (02/11/2026): thêm dòng trần mrp1 + mốc báo 80 % theo lệnh [MR · MR-P1] bước 0 (thử phong cách minh hoạ).
# MR-4 (01/11/2026): thêm dòng trần mr4 + mốc báo 80 % + chặn phụ ký tự gửi (TRAN_GUI_PHIEN, gui(), check_gui()) theo lệnh [MR · MR-4] bước 0.
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
    "mr1": {"youtube_units": 3000},  # MR-1 (lệnh điều phối [MR · MR-1] 01/11/2026): youtube_units 3000, search.list ≤ 60 lượt (TRAN_LUOT); mọi khoản khác 0.
    "mrk1": {"youtube_units": 2000},  # MR-K1 kho đề tài (lệnh điều phối [MR · MR-K1] 01/11/2026, bước 0): youtube_units 2000, search.list ≤ 50 lượt; mọi khoản khác 0.
    "mr4": {"openrouter_usd": 1.60, "elevenlabs_chars": 8000},  # MR-4 M-c phần 1 (lệnh [MR · MR-4] 01/11/2026, bước 0): openrouter 1,60 USD; elevenlabs 8.000 ký tự TÍNH (chặn phụ ≤ 16.000 ký tự gửi, TRAN_GUI_PHIEN); khác 0.
    "mrp1": {"openrouter_usd": 2.00},  # MR-P1 thử phong cách minh hoạ (lệnh [MR · MR-P1] 02/11/2026, bước 0): openrouter 2,00 USD (ảnh); khác 0.
    "mr5": {"openrouter_usd": 8.30, "elevenlabs_chars": 6000},  # MR-5 M-c phần 2 (lệnh [MR · MR-5] 02/11/2026, bước 0): openrouter 8,30 USD (14 khe Veo); elevenlabs 6.000 ký tự TÍNH (nhạc); khác 0.
}
CAPS = {k: float(CAPS_PHIEN.get(PHIEN, {}).get(k, 0.0)) for k in KHOAN}
# Mốc báo theo phiên: chạm mốc (đã ghi + đang chờ) mà còn > 20 % việc → DỪNG SINH, báo điều phối. Dạng {"mr1": {"openrouter_usd": 8.0}}.
DUNG_BAO_PHIEN = {"mr4": {"openrouter_usd": 1.28, "elevenlabs_chars": 6400},  # mr4: 80 % trần (lệnh [MR · MR-4] bước 0)
                  "mr5": {"openrouter_usd": 6.64, "elevenlabs_chars": 4800},  # mr5: 80 % trần (lệnh [MR · MR-5] bước 0)
                  "mrp1": {"openrouter_usd": 1.60}}  # mrp1: 80 % trần (lệnh [MR · MR-P1] bước 0)  # mr5: 80 % trần (lệnh [MR · MR-5] bước 0)
DUNG_BAO = DUNG_BAO_PHIEN.get(PHIEN, {})
# Trần SỐ LƯỢT theo phương thức (ngoài trần đơn vị). charge(..., {"method": "search.list"}) được đếm. Căn cứ: lệnh MR-1.
TRAN_LUOT_PHIEN = {"mr1": {"search.list": 60}, "mrk1": {"search.list": 50}}  # mrk1: lệnh [MR · MR-K1] 01/11/2026
TRAN_LUOT = TRAN_LUOT_PHIEN.get(PHIEN, {})
# Đơn giá YouTube Data API v3 (đơn vị/lượt) — bảng "Quota costs", developers.google.com/youtube/v3/determine_quota_cost
# (trang "Last updated 2026-10-15 UTC", mở 01/11/2026 MR-1). search.list có hạn mức riêng 100 lượt/ngày, mỗi lượt 1;
# các phương thức còn lại chung 10.000 đơn vị/ngày. youtube_units = tổng đơn giá × số lượt (kể cả lượt lỗi: "at least one point").
YT_DON_GIA = {"search.list": 1, "videos.list": 1, "channels.list": 1}

# Chặn phụ theo ĐƠN VỊ GỬI (khác đơn vị tính tiền). Sổ ghi meta "gui" (vd ký tự gửi TTS). Căn cứ: lệnh MR-4 (≤ 16.000 ký tự gửi).
TRAN_GUI_PHIEN = {"mr4": {"elevenlabs_chars": 16000}}
TRAN_GUI = TRAN_GUI_PHIEN.get(PHIEN, {})

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

def luot(method):
    """Số lượt đã ghi của một phương thức (đọc meta "method" trong sổ)."""
    n = 0
    if os.path.exists(LOG):
        for l in open(LOG):
            if l.strip() and json.loads(l).get("method") == method: n += 1
    return n

def check_yt(method, so_luot=1):
    """Kiểm trần youtube_units theo đơn giá + trần số lượt của phương thức (nếu có). Gọi TRƯỚC mỗi lệnh YouTube Data."""
    if method not in YT_DON_GIA: raise BudgetStop(f"{method}: chưa có đơn giá YouTube trong YT_DON_GIA")
    check("youtube_units", YT_DON_GIA[method] * so_luot)
    if method in TRAN_LUOT and luot(method) + so_luot > TRAN_LUOT[method]:
        raise BudgetStop(f"{method}: đã {luot(method)} + {so_luot} lượt > trần {TRAN_LUOT[method]} lượt ở phiên {PHIEN}")

def gui(kind):
    """Tổng đơn vị GỬI đã ghi của một khoản (meta "gui" trong sổ)."""
    n = 0.0
    if os.path.exists(LOG):
        for l in open(LOG):
            if l.strip():
                d = json.loads(l)
                if d.get("kind") == kind: n += float(d.get("gui", 0))
    return n

def check_gui(kind, so_gui):
    """MR-4: kiểm chặn phụ đơn vị gửi (TRAN_GUI) — gọi cùng check() trước mỗi lượt."""
    if kind in TRAN_GUI and gui(kind) + so_gui > TRAN_GUI[kind]:
        raise BudgetStop(f"{kind}: đã gửi {gui(kind):.0f} + {so_gui} > chặn phụ {TRAN_GUI[kind]} ở phiên {PHIEN}")

def charge(kind, amount, meta):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        with open(LOG, "a") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "kind": kind, "amount": round(amount, 6), **meta}, ensure_ascii=False) + "\n")

# Dịch vụ → khoản của chính dịch vụ đó (MR-1 sửa lỗi MR-0: 402 của ElevenLabs/YouTube bị ghi vào gemini_usd).
# Dịch vụ lạ → "khong_ro" (vẫn ghi sổ, vẫn DỪNG; amount 0 nên không ảnh hưởng tổng chi).
KHOAN_DICH_VU = {"gemini": "gemini_usd", "openrouter": "openrouter_usd", "elevenlabs": "elevenlabs_chars",
                 "claude": "claude_usd", "youtube": "youtube_units", "openai": "openai_usd"}

def bao_402(dich_vu, chi_tiet=""):
    """Gọi ngay khi nhận HTTP 402 từ bất kỳ dịch vụ nào: ghi sổ (amount 0) rồi raise Quy402 → phiên DỪNG."""
    charge(KHOAN_DICH_VU.get(dich_vu, "khong_ro"), 0.0,
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
                      "caps": CAPS, "dung_bao": DUNG_BAO,
                      "gui": {k: gui(k) for k in TRAN_GUI}, "tran_gui": TRAN_GUI}, ensure_ascii=False))
