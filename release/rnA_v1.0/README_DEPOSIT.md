# RN-A — Astrometry in 47 Tuc with Rubin DP1 (ComCam)

Derived products only (no raw DP1 images). Reproducible histogram of Rubin×Gaia separations in 47 Tuc and key percentiles with bootstrap CIs.

**Files**
- rnA_matched_minimal.parquet — minimal matched table (objectId, coord_ra/dec, source_id, ra_gaia/dec_gaia, separation_arcsec)
- rnA_metrics.json — N_pairs, P50/P68/P95 (arcsec), bootstrap CIs, seed, B
- rnA_hist_sep.png — histogram figure
- rnA_astrometry_47tuc.ipynb — self-contained notebook to regenerate metrics/figure
- RN-A_release_notes.md — methods and integrity notes
- CITATION.cff — citation metadata

**License**
Dataset (this deposit): CC-BY-4.0. GitHub code: MIT.
