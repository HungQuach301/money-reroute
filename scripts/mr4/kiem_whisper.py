#!/usr/bin/env python3
"""MR-4 · Kiểm lời đã thu bằng whisper cục bộ (faster-whisper medium.en, CPU, 0 USD).
  python3 scripts/mr4/kiem_whisper.py P00 P01 …        # mặc định lab/mr4/tts/<P>.mp3 (có <P>_l2.mp3 thì kiểm bản đó với --l2)
  python3 scripts/mr4/kiem_whisper.py --so-chu P00 …   # lượt 2: chặn token chữ số → số chép bằng chữ, so từng từ (ra <P>_sochu.json)
Ghi reports/mr4/whisper/<tệp>.json (bản chép + từ có mốc giờ) và in các đoạn LỆCH giữa lời gửi TTS và bản chép.
Chuẩn hoá hai phía trước khi so: chữ thường, bỏ dấu câu, tách gạch nối, số → chữ (num2words; năm 4 chữ số → kiểu năm),
"$"/"dollars", "and", "the" bỏ; "S-E-C" → "sec"; "1inMM"/"one-in-MM" → "one in m m". Lệch có chứa TỪ QUAN TRỌNG
(tên riêng, số tiền/số, "alleged", "one-in-M-M", "not") được gắn cờ ★ để nghe lại bằng tai — cờ máy chỉ dẫn, người quyết."""
import json, os, re, subprocess, sys, difflib
import numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mr4"))
from tts import doan_text  # noqa: E402
from num2words import num2words  # noqa: E402

KEY = set("""horwitz zachary zach avery scarsi mark c hbo netflix sec fbi doj los angeles latin america alleged alleges allegedly
one m not no never guilty pleaded convicted dismissed zero two three four five six seven eight nine ten eleven twelve thirteen
fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand
million billion percent point first second third fourth fifth sixth seventh eighth ninth tenth fourteenth twelfth
january february march april may june july august september october november december months years""".split())
DROP = {"and", "the", "dollars", "dollar", "a", "an"}


def so_thanh_chu(m):
    t = m.group(0).replace(",", "")
    suf = ""
    if t.endswith("%"): t, suf = t[:-1], " percent"
    o = re.match(r"^(\d+)(st|nd|rd|th)$", t)
    if o: return num2words(int(o.group(1)), to="ordinal")
    try:
        if re.fullmatch(r"(19|20)\d\d", t): return num2words(int(t), to="year") + suf
        return num2words(float(t) if "." in t else int(t)) + suf
    except Exception:
        return t


def chuan(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"\b1\s*-?\s*in\s*-?\s*mm\b|\bone-in-m-m\b|\bone in mm\b|\bone-in-mm\b", " one in m m ", s)
    s = re.sub(r"\bs-e-c\b", "sec", s); s = re.sub(r"\bh-b-o\b", "hbo", s); s = re.sub(r"\bf-b-i\b", "fbi", s)
    s = re.sub(r"\bfin-rah\b", "finra", s)
    s = re.sub(r"\$", " ", s)
    s = re.sub(r"\d[\d,]*(\.\d+)?(st|nd|rd|th|%)?", so_thanh_chu, s)
    s = s.replace("-", " ")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return [w for w in s.split() if w not in DROP]


_M = None


def model():
    global _M
    if _M is None:
        from faster_whisper import WhisperModel
        _M = WhisperModel("medium.en", device="cpu", compute_type="int8")
    return _M


_SUP = None


def chan_so():
    """Token id có chữ số/%/$ — chặn để whisper chép số bằng CHỮ (lượt --so-chu: kiểm số tiền, ngày, thứ tự đúng từng từ)."""
    global _SUP
    if _SUP is None:
        tk = model().hf_tokenizer
        _SUP = [-1] + [i for i in range(tk.get_vocab_size()) if any(ch in (tk.id_to_token(i) or "") for ch in "0123456789%$")]
    return _SUP


def chep(path, so_chu=False):
    a = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                                     capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
    kw = {"suppress_tokens": chan_so()} if so_chu else {}
    segs, info = model().transcribe(a, beam_size=5, word_timestamps=True, language="en", **kw)
    words, text = [], []
    for s in segs:
        text.append(s.text.strip())
        for w in s.words: words.append({"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2), "p": round(w.probability, 3)})
    return {"text": " ".join(text), "words": words, "dur": round(len(a) / 16000, 2)}


def so(ref, hyp):
    r, h = chuan(ref), chuan(hyp)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, r, h, autojunk=False).get_opcodes():
        if op == "equal": continue
        rs, hs = r[max(0, i1 - 3):i2 + 3], h[max(0, j1 - 3):j2 + 3]
        key = bool(KEY & set(r[i1:i2] + h[j1:j2]))
        out.append({"op": op, "ref": " ".join(r[i1:i2]), "hyp": " ".join(h[j1:j2]), "ngu_canh_ref": " ".join(rs),
                    "ngu_canh_hyp": " ".join(hs), "quan_trong": key})
    return out, len(r)


if __name__ == "__main__":
    a = sys.argv[1:]; l2 = "--l2" in a; sc = "--so-chu" in a; a = [x for x in a if x not in ("--l2", "--so-chu")]
    o = doan_text(); od = os.path.join(ROOT, "reports", "mr4", "whisper"); os.makedirs(od, exist_ok=True)
    for k in a:
        ten = k + ("_l2" if l2 else ""); ra = ten + ("_sochu" if sc else "")
        ref = " ".join(t for _, t in o[k])
        c = chep(os.path.join(ROOT, "lab", "mr4", "tts", ten + ".mp3"), sc)
        lech, n = so(ref, c["text"])
        json.dump({"doan": k, "tep": f"lab/mr4/tts/{ten}.mp3", "ref": ref, **c, "lech": lech}, open(os.path.join(od, ra + ".json"), "w"),
                  ensure_ascii=False, indent=1)
        print(f"== {ra}: {c['dur']} s · {n} từ · lệch {len(lech)} (★ {sum(x['quan_trong'] for x in lech)})")
        for x in lech:
            print(f"  {'★' if x['quan_trong'] else ' '} {x['op']}: REF «{x['ref']}» | HYP «{x['hyp']}»   [{x['ngu_canh_ref']}] ~ [{x['ngu_canh_hyp']}]")
