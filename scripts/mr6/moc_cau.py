#!/usr/bin/env python3
"""MR-6 · Mốc từng câu + từng từ theo whisper GIỌNG THẬT đã duyệt (0 USD).
  python3 scripts/mr6/moc_cau.py   → reports/mr6/moc_cau.json
Dòng thời gian phim = reports/mr4/xem/tap01_giong_ghep.json (giọng đã duyệt, nghỉ 1,5 s giữa đoạn) + chèn KHE KHÔNG LỜI 4 s
cho 4 thẻ KBCB chỉ chữ (S019 sau P03, S033 sau P06, S072 sau P15, S076 giữa P16 — đặt sau P16 vì lời P16 liền mạch;
PHONG-CACH-HINH §1: KBCB ≤ 4 s). Căn câu: so khớp token chuẩn hoá của câu (lời gửi TTS, scripts/mr4/tts.py phat_am)
với từ whisper bản "sochu" (số chép bằng chữ) bằng difflib; mốc câu = từ đầu/cuối khớp."""
import difflib, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr4"))
from tts import doan_text  # noqa: E402

KHE_KBCB = {"P03": ("S019", 4.0), "P06": ("S033", 4.0), "P15": ("S072", 4.0), "P16": ("S076", 4.0)}
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())


def tok(s):
    return [t for t in (norm(x) for x in re.split(r"[\s\-–—]+", s)) if t]


def main():
    g = json.load(open(os.path.join(ROOT, "reports", "mr4", "xem", "tap01_giong_ghep.json")))
    txt = doan_text(); off = 0.0; cau = {}; doan = []; tu_all = []
    for x in g["doan"]:
        p = x["doan"]; base = os.path.basename(x["tep"])[:-4]
        wf = os.path.join(ROOT, "reports", "mr4", "whisper", base + "_sochu.json")
        if not os.path.exists(wf): wf = wf.replace("_sochu", "")
        W = json.load(open(wf))["words"]
        t0 = x["bat_dau"] + off
        wt = []  # (token, s, e, chữ gốc)
        for w in W:
            for t in tok(w["w"]): wt.append((t, w["s"] + t0, w["e"] + t0, w["w"]))
        tu_all += [{"w": w["w"], "s": round(w["s"] + t0, 3), "e": round(w["e"] + t0, 3), "doan": p} for w in W]
        ref = []; owner = []
        for cid, s in txt[p]:
            for t in tok(s): ref.append(t); owner.append(cid)
        sm = difflib.SequenceMatcher(None, ref, [a[0] for a in wt], autojunk=False)
        m = {}
        for a, b, n in sm.get_matching_blocks():
            for k in range(n): m[a + k] = b + k
        for cid, _ in txt[p]:
            idx = [i for i, o in enumerate(owner) if o == cid and i in m]
            s = wt[m[idx[0]]][1]; e = wt[m[idx[-1]]][2]
            cau[cid] = {"doan": p, "s": round(s, 3), "e": round(e, 3), "khop": round(len(idx) / owner.count(cid), 3)}
        d = {"doan": p, "tep": x["tep"], "s": round(t0, 3), "e": round(t0 + x["dai"], 3)}
        doan.append(d)
        if p in KHE_KBCB:
            cid, dur = KHE_KBCB[p]; ks = t0 + x["dai"] + 0.75
            cau[cid] = {"doan": p, "s": round(ks, 3), "e": round(ks + dur, 3), "khop": None, "khong_loi": True}
            off += dur + 0.5
    # câu thiếu (không đọc) đã thêm; sắp theo id
    end = doan[-1]["e"]
    out = {"_ghi_chu": __doc__.strip().splitlines()[0], "tong_loi_s": round(end, 3), "khe_kbcb": KHE_KBCB, "doan": doan,
           "cau": dict(sorted(cau.items())), "tu": tu_all}
    os.makedirs(os.path.join(ROOT, "reports", "mr6"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "reports", "mr6", "moc_cau.json"), "w"), ensure_ascii=False, indent=0)
    low = {k: v["khop"] for k, v in cau.items() if v["khop"] is not None and v["khop"] < 0.8}
    print("tổng lời", round(end, 1), "s; câu", len(cau), "; khớp < 0,8:", low)


if __name__ == "__main__":
    main()
