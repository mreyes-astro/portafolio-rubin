# RN-A (DP1 · 47 Tuc · Astrometry) — v1.0.5

This package contains derived artefacts for RN-A (Rubin DP1 × Gaia DR3; 47 Tuc).

**What’s new in v1.0.5 (vs v1.0.4):**
- Removes the incorrect SRD wording (“consistent … with ample margin”).
- Adds a sanity identity on the plane: `mean(r^2) = mean((Δα⋆)^2) + mean((Δδ)^2)` (matches to machine precision).
- Adds core/tail decomposition at `q95` with heavy-tail quantification and a 1% trimmed (robust) per-axis RMS.
- Adds the influence-curve CSV and figure; includes the EN manuscript (v9) as an asset.

**Artefacts**
- `rnA_matched_minimal.parquet` — minimal derived table.
- `rnA_metrics.json` — radial P50/P68/P95 + CIs; `per_coordinate` (RMS + CIs);
  `radii_check`; generator metadata.
- `rnA_hist_sep.png` — histogram (P50/P68/P95).
- `rnA_influence_curve.csv` — per-axis RMS vs included quantile of `r`.
- `rnA_astrometry_47tuc.ipynb` — main reproducible notebook (RN-A).
- `rnA_r2_sanity_and_influence.ipynb` — sanity (r²), core/tail, robust RMS, and figure.
- `Reyes_2025_RubinDP1_47Tuc_RN-A_v9_EN.pdf` — manuscript (EN v9).
- `LICENSE-CC-BY-4.0.txt`, `CITATION.cff`, `SHA256SUMS.txt`.

**Scope w.r.t. SRD (LPM-17)**
SRD requirements are *per-coordinate*. RN-A reports radial percentiles as a reproducible reference, and provides per-coordinate RMS as quantitative context; no direct SRD compliance claim is made.

For details, see the repository README.
