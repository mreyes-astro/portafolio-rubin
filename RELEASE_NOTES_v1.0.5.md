# RN-A v1.0.5 — r² sanity + core/tail + robust RMS + influence curve (EN v9)

**What's new**
- In-plane sanity identity: `mean(r^2) = mean(Δα⋆^2) + mean(Δδ^2)` (matches to machine precision).
- Core/tail decomposition at `q95` in `r^2`; the ~5% tail dominates `E[r^2]` and explains the larger per-axis RMS.
- 1% trimmed (robust) per-axis RMS, complementing the classical RMS.
- Influence curve (RMS vs included fraction by quantile of `r`): flat up to ~0.95 and rises with the last 5%.
- EN manuscript **v9** aligned with README/JSON (no SRD-compliance claim; SRD is per-coordinate).

**Assets**
- CITATION.cff  
- LICENSE-CC-BY-4.0.txt  
- README_DEPOSIT.md  
- rnA_astrometry_47tuc.ipynb  
- rnA_hist_sep.png  
- rnA_matched_minimal.parquet  
- `data/47tuc_dp1/rnA_metrics.json` (updated)  
- `data/47tuc_dp1/rnA_influence_curve.csv`  
- `notebooks/47tuc/figs/rnA_influence_curve.png`  
- `notebooks/47tuc/rnA_r2_sanity_and_influence.ipynb`  
- `docs/RN-A_en/Reyes_2025_RubinDP1_47Tuc_RN-A_v9_EN.pdf`  
- SHA256SUMS.txt

**Erratum note**
v1.0.4 description said “consistent with SRD by a wide margin”. This is outdated. RN-A reports **radial percentiles** and **per-coordinate RMS** for transparency; since **LPM-17 SRD** defines requirements **per coordinate**, we do **not** claim SRD compliance here. See EN v9 and README.

**Reproducibility**
All code/notebooks/derived tables and figures included; bootstrap seed and parameters documented.
