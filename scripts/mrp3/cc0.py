#!/usr/bin/env python3
"""MR-P3 · Tải tiếng động CC0 từ BigSoundBank (0 USD). CHỈ nhận tệp mà TRANG CỦA CHÍNH TỆP ghi "License CC0 (public domain)";
giấy phép khác/không rõ → bỏ, ghi lý do. Ghi nguồn + giấy phép + sha256 từng tệp vào reports/mrp3/am/cc0.json.
Tệp âm ở scratch (dựng lại được từ URL, 0 USD → không đẩy). UA mặc định của urllib; không vượt rào (403/429 → ghi "chưa mở được").
  MRP3_TMP=… python3 scripts/mrp3/cc0.py"""
import hashlib, html, json, os, re, time, urllib.request, urllib.error
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP3_TMP", "/tmp/claude-0/mrp3"); OUT = os.path.join(TMP, "cc0"); os.makedirs(OUT, exist_ok=True)
GOC = "https://www.bigsoundbank.com"
# khoá: dùng cho cảnh nào (đoạn thử)
DS = {
    "rung_dt": ("/mobile-phone-vibrator-1-s0022.html", "S001 điện thoại rung trên bàn"),
    "bao_tin": ("/notification-lasolisa-1-s2063.html", "S001/S002 tiếng báo tin nhắn (bong bóng chữ)"),
    "tu_lanh": ("/fridge-s1157.html", "P00 tiếng nền bếp (tủ lạnh ù)"),
    "mua_kinh": ("/night-after-rain-s0621.html", "P00 tiếng nền đêm sau mưa (a03 mưa trên kính)"),
    "lat_trang": ("/great-page-that-turns-1-s0362.html", "L3 trang hồ sơ hiện ra"),
    "bua": ("/gavel-1-blow-s1588.html", "S010 tuyên án 20 năm"),
    "dong_ho": ("/clock-s0007.html", "S073 đếm ngược tới 9/4"),
    "tim": ("/heartbeat-1-s0243.html", "S073–S079 nhịp tim trầm dưới đếm ngược"),
    "vut": ("/whoosh-2-s0573.html", "chuyển cảnh lớn / thẻ"),
    "khoa": ("/lock-s0191.html", "S079 phong toả tài sản (cửa két khoá)"),
    "no_xa": ("/explosion-far-away-s1023.html", "cú lật S003/S080: nền trầm (lọc thấp, rất nhỏ)"),
    "pho_dem": ("/paris-by-night-s0680.html", "S011 thành phố (K2)"),
    "go_phim": ("/slow-keyboard-s1733.html", "S068 gõ thư trấn an (nền)"),
}


def mo(u, nhi=False):
    r = urllib.request.urlopen(urllib.request.Request(u), timeout=60); b = r.read()
    return b if nhi else b.decode("utf-8", "replace")


def main():
    p = os.path.join(ROOT, "reports", "mrp3", "am", "cc0.json"); os.makedirs(os.path.dirname(p), exist_ok=True)
    kq = {"_ghi_chu": __doc__.strip(), "trang_giay_phep_chung": GOC + "/licenses.html", "tep": {}, "bo": {}}
    for k, (duong, dung) in DS.items():
        u = GOC + duong
        try:
            t = mo(u)
        except urllib.error.HTTPError as e:
            kq["bo"][k] = {"url": u, "ly_do": f"chưa mở được (HTTP {e.code})"}; continue
        s = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S))))
        m = re.search(r"License (CC0 \(public domain\))[^(]{0,40}", s)
        tieu = re.search(r"<title>(.*?)</title>", t, re.S)
        if not m:
            lic = re.search(r"License\s+([^()]{0,80})", s)
            kq["bo"][k] = {"url": u, "ly_do": "trang tệp không ghi CC0", "ghi": lic.group(0) if lic else None}; continue
        mp3 = re.search(r"(/UPLOAD/mp3/\d+\.mp3)", t)
        if not mp3:
            kq["bo"][k] = {"url": u, "ly_do": "không thấy liên kết tải mp3"}; continue
        b = mo(GOC + mp3.group(1), True); f = os.path.join(OUT, k + ".mp3"); open(f, "wb").write(b)
        kq["tep"][k] = {"url_trang": u, "url_tep": GOC + mp3.group(1), "tieu_de": html.unescape(tieu.group(1).strip()) if tieu else None,
                        "giay_phep_tren_trang": m.group(0).strip(), "dung_cho": dung, "sha256": hashlib.sha256(b).hexdigest(),
                        "byte": len(b), "tai_luc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        print(k, "CC0", len(b)); time.sleep(1)
    json.dump(kq, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
