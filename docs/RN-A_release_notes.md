# RN-A — Alineación astrométrica DP1 en 47 Tuc (Rubin×Gaia)

**Resumen.** Cross-match 1:1 Rubin DP1 (ComCam) × Gaia DR3 en 47 Tuc, radio 2″.  
**Métricas:** N=1113; P50=0.051″; P68=0.053″; P95=0.116″ (cumple SRD A22).

**Artefactos (derivados):**
- `data/47tuc_dp1/rnA_matched_minimal.parquet`
- `data/47tuc_dp1/rnA_metrics.json`
- Figura: `notebooks/47tuc/figs/rnA_hist_sep.png`
- Notebook: `notebooks/47tuc/rnA_astrometry_47tuc.ipynb`

**Método breve.** TAP Rubin/DP1 + Gaia DR3, radio 2″, deduplicación 1:1 simétrica; offset-match plano; PM-propagation bias <0.02″.

**Agradecimientos:** Rubin DP1/RSP, Gaia DR3.
