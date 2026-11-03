#!/usr/bin/env python3
"""MR-P4 · Từ vựng chuyển động máy theo nhịp lời + cổng độ sâu (0 USD). Dùng bởi scripts/mrp4/dung_p4.py.

KIỂU (mỗi cảnh đúng một kiểu, có LÝ DO + TỪ NEO; chuyển động bắt đầu ở từ neo, có gia tốc/giảm tốc, hoặc đứng yên — KHÔNG trôi nhẹ đều):
  day  đẩy vào chi tiết     phóng +15…25 % về điểm neo, dolly theo độ sâu (vật gần nở nhanh hơn)
  keo  kéo ra lộ cảnh       ngược đẩy: bắt đầu chặt (+20 %) → toàn cảnh; dùng ở CÚ LẬT
  lia  lia theo dòng tiền   máy dịch ngang 12–16 % khung theo hướng tiền đi, lớp gần trượt nhanh hơn (thị sai)
  dung máy đứng yên         câu nặng (bản án, thừa nhận, câu pháp lý); chỉ lớp chuyển động trong khung chạy
  cat  cắt vào              đứng yên rồi CẮT CỨNG vào khung chặt (+20 %) đúng từ neo — thay cho đẩy khi tranh dưới ngưỡng độ sâu
  giat giật nhanh           chuyển cảnh khi CHUYỂN HỒI: lia giật 0,32 s + nhoè chuyển động + tiếng vút (thay hoà cảnh 0,5 s)
CỔNG ĐỘ SÂU (chỉ số HD của scripts/mrp4/sau.py):
  HD < 45      → không trượt/không 2.5D: chỉ "dung" hoặc "cat" (day/keo/lia tự hạ thành cat/dung, ghi lại)
  45 ≤ HD < 60 → day/keo/cat được, dolly 2.5D nhẹ (K ≤ 0,03); KHÔNG lia
  HD ≥ 60      → mọi kiểu; dolly K ≤ 0,07, lia có thị sai
Clip ảnh→video và cảnh nhân vật hoạt hoạ mã: máy 2D (không 2.5D) — kiểu chỉ là phóng/khung, chuyển động thật nằm trong khung."""
import math

NGUONG_HD = 45.0
NGUONG_LIA = 60.0
CX, CY = 960.0, 540.0


def ease(x):
    x = min(max(x, 0.0), 1.0)
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


# Bảng cảnh M2 mới. Khoá = mã cảnh trong dòng thời gian (CANH["ma"]). neo = (câu, từ) theo whisper; diem = điểm neo trên tranh 1920×1080.
# huong lia: +1 = máy đi sang phải. A = biên độ phóng.
KIEU = {
    "a01":    dict(k="day", neo=("S001", "phone"), diem=(980, 520), A=0.20, ly_do="lời gọi vào điện thoại đang sáng — đẩy vào tay + màn hình"),
    "b064":   dict(k="lia", neo=("S001", "schedule"), diem=(880, 760), huong=1, ly_do="khoản trả 'đúng hẹn' đi vào máy — lia theo dòng tiền tới điện thoại"),
    "a03":    dict(k="clip", ly_do="clip V01 (mưa trên kính) — chuyển động trong khung"),
    "b065":   dict(k="day", neo=("S002", "delay"), diem=(1110, 730), A=0.22, ly_do="'delay' — đẩy vào tin nhắn trên màn hình"),
    "a02":    dict(k="dung", neo=("S002", "side"), ly_do="cảnh 1,3 s: tay + màn hình — để mắt đọc, không thêm chuyển động"),
    "a04":    dict(k="day", neo=("S002", "next"), diem=(1030, 420), A=0.18, ly_do="'next week' — đẩy vào nét lo trên mặt nhân vật"),
    "a05":    dict(k="dung", neo=("S003", "reconstruction"), ly_do="câu khẳng định nặng 'is a reconstruction' — máy đứng yên để lời rơi"),
    "b066":   dict(k="keo", neo=("S003", "real"), diem=(960, 520), A=0.22, ly_do="CÚ LẬT 'the case … is real' — kéo ra lộ kho hồ sơ công khai (trên clip V03)"),
    "a07":    dict(k="dung", neo=("S004", "man"), vao="giat", huong=1, ly_do="CHUYỂN HỒI sang nhân vật chính — giật vào, rồi đứng yên trên bóng lưng"),
    "b001":   dict(k="day", neo=("S004", "horwitz"), diem=(619, 422), A=0.16, ly_do="tên người — đẩy vào gương phòng hoá trang (vai diễn)"),
    "b067":   dict(k="lia", neo=("S004", "actor"), huong=-1, ly_do="'an actor in Los Angeles' — lia qua trường quay"),
    "b062":   dict(k="dung", neo=("S004", "screen"), ly_do="cảnh 1,4 s nhà đầu tư — đứng yên, giữ nhịp dồn của chuỗi 5 cảnh"),
    "b002":   dict(k="day", neo=("S004", "avery"), diem=(981, 560), A=0.18, ly_do="'Zach Avery' — đẩy vào đồng hồ cát trên tay (thời hạn kỳ phiếu)"),
    "a09":    dict(k="lia", neo=("S006", "money"), huong=1, ly_do="'the money … would buy film rights' — lia theo dòng tiền dọc kho phim"),
    "b070":   dict(k="day", neo=("S006", "rights"), diem=(600, 440), A=0.20, ly_do="'film rights' — đẩy vào dải phim"),
    "a10":    dict(k="lia", neo=("S006", "such"), huong=1, ly_do="'licensed to streaming platforms' — lia theo dòng tiền tới màn hình TV"),
    "b003":   dict(k="dung", neo=("S008", "not"), ly_do="câu pháp lý KBCB 'were not accused' — máy đứng yên"),
    "a15":    dict(k="clip", ly_do="clip V04 (chùm máy chiếu) — chuyển động trong khung"),
    "b074":   dict(k="dung", neo=("S008", "neither"), ly_do="câu pháp lý KBCB 'neither company…' — máy đứng yên"),
    "a12":    dict(k="dung", neo=("S010", "years"), ly_do="BẢN ÁN 'twenty years in prison' — máy đứng yên"),
    "b063":   dict(k="keo", neo=("S011", "story"), diem=(1100, 450), A=0.20, ly_do="'This is the story' — kéo ra mở toàn cảnh căn bếp (mở chuyện)"),
    "b040":   dict(k="clip", ly_do="clip V02 (hồ sương, 'lull') — chuyển động trong khung"),
    "b141":   dict(k="day", neo=("S073", "april"), diem=(1080, 800), A=0.22, ly_do="hạn 'April ninth' — đẩy vào điện thoại úp (chờ tiền)"),
    "b051":   dict(k="clip", vao="giat", huong=1, ly_do="CHUYỂN HỒI 'Closing in' (nộp đơn khẩn) — giật vào clip V05 phòng xử"),
    "b116:2": dict(k="day", neo=("S078", "horwitz"), diem=(1250, 520), A=0.18, ly_do="'emergency case against Horwitz' — đẩy vào thành phố lúc rạng sáng"),
    "b052":   dict(k="clip", ly_do="clip V06 (cửa két đóng) — chuyển động trong khung"),
    "b118:2": dict(k="dung", neo=("S079", "freeze"), rung=True, ly_do="lệnh phong toả 'asset freeze' (câu nặng) — đứng yên, rung đúng chữ 'freeze'"),
    "b053":   dict(k="dung", neo=None, ly_do="khoảng lặng sau cảnh bắt (không lời trong đoạn thử) — đứng yên"),
}
TEN = {"day": "đẩy vào chi tiết", "keo": "kéo ra lộ cảnh", "lia": "lia theo dòng tiền", "dung": "máy đứng yên", "cat": "cắt vào",
       "clip": "clip (chuyển động trong khung)", "giat": "giật nhanh"}


def cong(spec, hd):
    """Áp cổng độ sâu → kiểu thực dùng (+ ghi chú)."""
    k = spec["k"]
    if hd is None or k in ("clip", "dung", "cat"): return k, ""
    if hd < NGUONG_HD:
        return ("cat", f"HD {hd} < {NGUONG_HD}: {k} → cắt vào") if k == "day" else ("dung", f"HD {hd} < {NGUONG_HD}: {k} → đứng yên")
    if k == "lia" and hd < NGUONG_LIA: return "day", f"HD {hd} < {NGUONG_LIA}: lia → đẩy"
    return k, ""


def cam(k, spec, hd, tau, ta, te):
    """→ dict(L, Z, K, T) cho scripts/mrp2 warp (toạ độ khung tranh). ta = giây bắt đầu chuyển động (từ neo), te = cuối cảnh."""
    A = spec.get("A", 0.20); P = spec.get("diem", (CX, CY)); kmax = 0.07 if (hd or 0) >= NGUONG_LIA else 0.03
    z0 = 1.03
    if te - ta < 0.9: ta = max(0.0, te - 0.9)
    e = ease((tau - ta) / max(te - ta, 1e-3))
    if k == "dung": return dict(L=(CX, CY), Z=z0, K=0.0, T=(0.0, 0.0))
    if k == "cat":
        if tau < ta: return dict(L=(CX, CY), Z=z0, K=0.0, T=(0.0, 0.0))
        return dict(L=(CX + (P[0] - CX) * 0.55, CY + (P[1] - CY) * 0.55), Z=z0 * 1.20, K=0.0, T=(0.0, 0.0))
    if k in ("day", "keo"):
        if k == "keo": e = 1 - e
        Z = z0 * (1 + A * e)
        return dict(L=(CX + (P[0] - CX) * 0.6 * e, CY + (P[1] - CY) * 0.6 * e), Z=Z, K=kmax * e, T=(0.0, 0.0))
    if k == "lia":
        h = spec.get("huong", 1); Z = 1.17; dx = 115.0; tx = 55.0
        return dict(L=(CX - h * dx + 2 * h * dx * e, CY), Z=Z, K=0.0, T=(h * tx - 2 * h * tx * e, 0.0))
    raise ValueError(k)


def kep(c, W=1920, H=1080):
    """giữ khung nhìn trong tranh (như scripts/mrp2 cam_luc)."""
    (Lx, Ly), Z, (Tx, Ty) = c["L"], c["Z"], c["T"]; m = max(abs(Tx), abs(Ty)) / Z + 6
    Lx = min(max(Lx, W / (2 * Z) + m), W - W / (2 * Z) - m); Ly = min(max(Ly, H / (2 * Z) + m), H - H / (2 * Z) - m)
    c["L"] = (Lx, Ly); return c


def bien_do(k, spec):
    """biên độ ghi bảng."""
    if k in ("day", "keo"): return f"phóng {round(spec.get('A', 0.2) * 100)} %"
    if k == "cat": return "cắt +20 %"
    if k == "lia": return "lia 230 px nguồn ≈ 14 % khung, thị sai ±55 px"
    return "0"


def rung(tau, tr):
    k = tau - tr
    return 0.0 if k <= 0 else 7 * math.exp(-k / 0.12) * math.cos(k * 40)
