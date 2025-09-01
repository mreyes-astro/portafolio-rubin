import json, argparse, numpy as np, pandas as pd
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--parquet", default="data/47tuc_dp1/rnA_matched_minimal.parquet")
ap.add_argument("--out",     default="data/47tuc_dp1/rnA_metrics.json")
ap.add_argument("--B",       type=int, default=5000)
ap.add_argument("--seed",    type=int, default=47)
args = ap.parse_args()

df = pd.read_parquet(args.parquet)
df = df.sort_values("separation_arcsec")\
       .drop_duplicates("objectId")\
       .drop_duplicates("source_id")
df = df.query("separation_arcsec <= 2.0")
sep = df["separation_arcsec"].to_numpy()

def pct(x, q): return np.percentile(x, q)
P50, P68, P95 = pct(sep,50), pct(sep,68), pct(sep,95)

rng = np.random.default_rng(args.seed)
B = args.B
boot_P50 = np.empty(B); boot_P95 = np.empty(B)
n = len(sep)
for b in range(B):
    s = sep[rng.integers(0, n, size=n)]
    boot_P50[b] = np.percentile(s, 50)
    boot_P95[b] = np.percentile(s, 95)

def ci(arr, alpha=0.05):
    lo, hi = np.quantile(arr, [alpha/2, 1-alpha/2])
    return float(lo), float(hi)

P50_lo, P50_hi = ci(boot_P50)
P95_lo, P95_hi = ci(boot_P95)

out = Path(args.out)
base = {}
if out.exists():
    base = json.loads(out.read_text())

base.update({
    "N_pairs": int(n),
    "P50_arcsec": float(np.round(P50,3)),
    "P68_arcsec": float(np.round(P68,3)),
    "P95_arcsec": float(np.round(P95,3)),
    "P50_ci95_arcsec": [P50_lo, P50_hi],
    "P95_ci95_arcsec": [P95_lo, P95_hi],
    "bootstrap_B": B,
    "bootstrap_seed": args.seed,
    "method_note": "1:1 dentro de 2″; percentiles sobre separaciones; IC-95% por bootstrap."
})
out.write_text(json.dumps(base, indent=2))
print("Actualizado ->", out)
print(json.dumps(base, indent=2))
