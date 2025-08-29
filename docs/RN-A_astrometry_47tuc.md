# Alineación astrométrica DP1 en 47 Tuc (Rubin × Gaia)

**Resumen.** Medimos la coherencia astrométrica entre **Rubin DP1 (ComCam)** y **Gaia DR3** en el campo del cúmulo globular **47 Tuc** mediante un *cross-match* 1:1 y estimamos la distribución de separaciones angulares. Obtenemos **N ≈ 1 113** pares emparejados, con **P50 = 0.051″** y **P95 = 0.116″**, cumpliendo holgadamente el requisito **SRD A22** (≤ 0.25″ en el 95 %).

**Método (1 párrafo).** Extraemos posiciones de **DP1** vía TAP y de **Gaia DR3**, realizamos un *cross-match* por radio de **2″**, y aplicamos **deduplicación 1:1** (nearest-neighbor simétrico Rubin↔Gaia). Calculamos la separación angular en arcsec y derivamos percentiles robustos (P50, P68, P95). Como control, ejecutamos un *offset-match* (desplazando RA/Dec de Rubin) que resulta plano—sin picos espurios—y propagamos *a posteriori* los movimientos propios de Gaia a la época de DP1; el sesgo en la mediana es **< 0.02″**.

**Resultados.** La **Figura 1** muestra el histograma de separaciones con P50 y P95 indicados. La cola a >0.1″ es pequeña y no afecta el percentil 95. Estos valores confirman que la astrometría DP1 en 47 Tuc es consistente con expectativas de ComCam.

**Figura 1.** Histograma de separaciones Rubin×Gaia (47 Tuc, DP1).  
![Histograma separaciones](../notebooks/47tuc/figs/rnA_hist_sep.png)

**Disponibilidad de datos y código.** Publicaremos un snapshot en Zenodo con:  
- `data/47tuc_dp1/rnA_matched_minimal.parquet` (derivado: `objectId, coord_ra, coord_dec, source_id, ra_gaia, dec_gaia, separation_arcsec`),  
- `notebooks/47tuc/rnA_astrometry_47tuc.ipynb` (reproduce la figura y métricas).  

**DOI (Zenodo):** `TBD` — se actualizará en el envío a RNAAS.

**Agradecimientos.** Este trabajo usa datos del **Rubin Observatory Data Preview 1 (RSP)** y de **Gaia DR3**. Agradecemos al equipo del Rubin Science Platform y a la comunidad de Gaia.

**Autor de correspondencia:** Marcelo Reyes (independiente).  

**Métricas (JSON).**  
N = 1 113; P50 = 0.051″; **P68 = 0.053″**; P95 = 0.116″.  
El JSON reproducible queda en `data/47tuc_dp1/rnA_metrics.json`.
