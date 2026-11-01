#!/usr/bin/env python3
"""MR-4 · Bản nghe: ghép giọng theo đoạn P00–P21 (bản đã chọn) → reports/mr4/xem/tap01_giong_ghep.mp4 (chỉ âm, AAC 192k, 48 kHz),
nghỉ 1,5 s giữa các đoạn, chuẩn hoá −14 LUFS / TP ≤ −1 dBTP (loudnorm 2 lượt, đích TP −1,5 vì đích −1 đo lại ra −0,90). Kèm reports/mr4/xem/tap01_giong_ghep.json (mốc từng đoạn).
0 USD (ffmpeg cục bộ). Chọn bản: CHON (đoạn → tệp)."""
import json, os, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
T = os.path.join(ROOT, "lab", "mr4", "tts"); X = os.path.join(ROOT, "reports", "mr4", "xem")
CHON = {f"P{i:02d}": f"P{i:02d}" for i in range(22)}
CHON.update({"P01": "P01_l2"})  # P01 bản 2 sạch cả 2 lượt whisper; P17 giữ bản 1 (lượt chặn chữ số sạch, bản 2 lệch cả 2 lượt); P19 giữ bản 1 (bản 2 lệch y hệt)
NGHI = 1.5
dur = lambda p: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
os.makedirs(X, exist_ok=True)
ins, flt, t, moc = [], [], 0.0, []
for k in sorted(CHON):
    p = os.path.join(T, CHON[k] + ".mp3"); d = dur(p)
    moc.append({"doan": k, "tep": f"lab/mr4/tts/{CHON[k]}.mp3", "bat_dau": round(t, 2), "dai": round(d, 2)}); t += d + NGHI
    ins += ["-i", p]
n = len(CHON)
fc = "".join(f"[{i}:a]aresample=48000,apad=pad_dur={NGHI}[a{i}];" for i in range(n)) + "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[c]"
tmp = os.path.join(X, "_tmp.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[c]", "-ac", "1", tmp], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
m = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
      f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
out = os.path.join(X, "tap01_giong_ghep.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-c:a", "aac", "-b:a", "192k", out], check=True)
os.remove(tmp)
r2 = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "loudnorm=I=-14:TP=-1:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
m2 = json.loads(r2[r2.rindex("{"):r2.rindex("}") + 1])
json.dump({"tep": "reports/mr4/xem/tap01_giong_ghep.mp4", "nghi_giua_doan_s": NGHI, "tong_s": round(dur(out), 2),
           "do_sau": {"I": m2["input_i"], "TP": m2["input_tp"], "LRA": m2["input_lra"]}, "doan": moc},
          open(os.path.join(X, "tap01_giong_ghep.json"), "w"), ensure_ascii=False, indent=1)
print(round(dur(out), 2), m2["input_i"], m2["input_tp"])
