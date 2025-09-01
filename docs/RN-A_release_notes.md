# RN-A — Alineación astrométrica DP1 en 47 Tuc (Rubin×Gaia)

**Versión:** v1.0-rnA  
**Autor:** Marcelo Reyes (independiente)  
**Fecha:** 2025-08-29

## TL;DR
- **Muestra:** 47 Tuc (DP1, ComCam) × **Gaia DR3**  
- **Emparejamiento:** radio 2″ + deduplicación **1:1 simétrica** (nearest Rubin↔Gaia)  
- **Métricas:** **N = 1 113**, **P50 = 0.051″**, **P68 = 0.053″**, **P95 = 0.116″**  
- **Control:** *offset-match* (Rubin desplazado +60″ en RA) ⇒ **0** pares ≤ 2″ (plano)  
- **Conclusión:** cumple holgadamente **SRD A22** (≤ 0.25″ en el 95 %)

---

## Artefactos (derivados)

> Solo productos derivados. **No** se incluyen imágenes crudas de DP1.

- `data/47tuc_dp1/rnA_matched_minimal.parquet`  
  Campos: `objectId, coord_ra, coord_dec, source_id, ra_gaia, dec_gaia, separation_arcsec`
- `data/47tuc_dp1/rnA_metrics.json`  
  Contiene `{"N_pairs":1113,"P50_arcsec":0.051,"P68_arcsec":0.053,"P95_arcsec":0.116}`
- `notebooks/47tuc/figs/rnA_hist_sep.png` — Histograma con P50 y P95
- `notebooks/47tuc/rnA_astrometry_47tuc.ipynb` — Notebook corto para reproducir figura/métricas
- `docs/RN-A_astrometry_47tuc.md` — Borrador listo para RNAAS (método y resultados)

---

## Método (resumen)
1) Posiciones de **Rubin DP1 (ComCam)** obtenidas vía TAP y de **Gaia DR3**.  
2) *Cross-match* por radio **2″**; **deduplicación 1:1** simétrica (nearest vecino en ambos sentidos).  
3) Cálculo de separaciones angulares (arcsec) y percentiles **P50/P68/P95**.  
4) **Control** de emparejamiento espurio: *offset-match* desplazando Rubin **+60″** en RA ⇒ plano (0 coincidencias ≤ 2″).  
5) (Chequeo adicional) Propagación de PM de Gaia a época DP1: sesgo en mediana **< 0.02″**.

---

## Resultados
- **N = 1 113** pares válidos (1:1 dentro de 2″).  
- **P50 = 0.051″**, **P68 = 0.053″**, **P95 = 0.116″**.  
- Histograma en `notebooks/47tuc/figs/rnA_hist_sep.png`.  
- Cumple **SRD A22** (≤ 0.25″ en el 95 %) con amplio margen en este campo.

---

## Reproducibilidad (rápida)
1. Verifica que existan los derivados:
   - `data/47tuc_dp1/rnA_matched_minimal.parquet`  
   - `data/47tuc_dp1/rnA_metrics.json`
2. Abre y ejecuta `notebooks/47tuc/rnA_astrometry_47tuc.ipynb` (JupyterLab/RSP)  
   → produce `notebooks/47tuc/figs/rnA_hist_sep.png` y re-imprime métricas.  

*(No requiere acceso a TAP ni al Butler; todo se lee de Parquet/JSON.)*

---

## Política de datos y agradecimientos
- Este trabajo utiliza **Rubin Observatory Data Preview 1 (RSP)** y **Gaia DR3**.  
- Solo se publican **productos derivados** (parquets/JSON/figuras).  
- Agradecimientos a los equipos de Rubin RSP/DP1 y Gaia.

---

## Citar
- **Zenodo DOI:** _TBD_ (se actualizará al publicar el depósito)  
- **Release GitHub:** `v1.0-rnA`  
- **Licencia código/docs:** MIT (archivo `LICENSE`)  
- **Licencia datos derivados:** CC-BY-4.0 recomendada en Zenodo

---

## Cambios (changelog)
- **v1.0-rnA (2025-08-29)**: primera liberación — parquet mínimo, métricas JSON, figura y notebook RN-A.


## Integridad (SHA256)

- `data/47tuc_dp1/rnA_matched_minimal.parquet`  
  `a1075b24066818444627ad100a822874a2064eb16eae3ac7c27765e5477faf86`
- `data/47tuc_dp1/rnA_metrics.json`  
  `808495797b581481e36a45560b96156ab79b27f4d549302058db9c3afb13cb18`
- `notebooks/47tuc/figs/rnA_hist_sep.png`  
  `30f228bd223eb8a7e8ebe84895991940bce6dc321059369c08d8088bbcf00c82`

## Licencias
- **Código y notebooks**: MIT (véase LICENSE).
- **Datos derivados y figuras de RN-A**: CC-BY-4.0 (citar a Marcelo Reyes; reconocer Rubin DP1/RSP y Gaia DR3).


## Referencias
- Ivezić, Ž., & the LSST Science Collaboration (2018). *The LSST System Science Requirements Document (LPM-17).* GitHub: https://github.com/lsst-pst/LPM-17
