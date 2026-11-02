#!/usr/bin/env python3
"""MR-P3 · Độ sâu + tách 3 lớp + vá cho tranh L1 đoạn thử (0 USD, CPU). Gọi lại hàm của scripts/mrp2/sau.py (Depth Anything V2 Small,
Apache-2.0, onnx-community/depth-anything-v2-small @ 4472b73; trọng số không đưa vào repo).
  MRP3_TMP=… python3 scripts/mrp3/sau.py <model.onnx> [ma …]
Ra: $MRP3_TMP/sau/<ma>_{depth,l0,l1,l2,mask1,mask2}.png (scratch, dựng lại được) + reports/mrp3/lop_do.json."""
import json, os, sys, hashlib, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TMP = os.environ.get("MRP3_TMP", "/tmp/claude-0/mrp3"); os.environ["MRP2_TMP"] = TMP; os.environ.setdefault("MR6_TMP", os.path.join(TMP, "mr6"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "mrp2"))
import sau  # noqa: E402
import onnxruntime as ort  # noqa: E402
LOP = json.load(open(os.path.join(os.path.dirname(__file__), "lop.json"))) if os.path.exists(os.path.join(os.path.dirname(__file__), "lop.json")) else {}
sau.CAU_HINH = LOP


def main():
    mdl = sys.argv[1]; ids = sys.argv[2:] or json.load(open(os.path.join(os.path.dirname(__file__), "doan.json")))["l1"]
    sess = ort.InferenceSession(mdl, providers=["CPUExecutionProvider"])
    p = os.path.join(ROOT, "reports", "mrp3", "lop_do.json")
    out = json.load(open(p)) if os.path.exists(p) else {"tranh": {}}
    out.update({"model": "depth-anything-v2-small (onnx-community, rev 4472b73)", "sha256": hashlib.sha256(open(mdl, "rb").read()).hexdigest()})
    t0 = time.time()
    for ma in ids:
        r = sau.lam(sess, ma); out["tranh"][ma] = r; print(r, flush=True)
    out["giay_moi_tranh"] = round((time.time() - t0) / max(len(ids), 1), 1)
    json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
