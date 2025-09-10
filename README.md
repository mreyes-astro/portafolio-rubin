# Portafolio Rubin 🔭

Repositorio personal para experimentos y proyectos basados en los **Data Previews** del [Vera C. Rubin Observatory](https://www.lsst.org/).

[![DOI (versión)](https://zenodo.org/badge/DOI/10.5281/zenodo.17017865.svg)](https://doi.org/10.5281/zenodo.17017865)
[![DOI (concepto)](https://zenodo.org/badge/DOI/10.5281/zenodo.17017864.svg)](https://doi.org/10.5281/zenodo.17017864)

> Autor: **Marcelo Reyes** · [mreyesb@gmail.com](mailto:mreyesb@gmail.com)

---

## Estado (2025-09-09)

**RN-A (DP1 · 47 Tuc · Astrometry)**  
- **Release actual:** v1.0.5-rnA — corrige el wording SRD de v1.0.4 y añade *sanity r²*, descomposición **core/tail**, **RMS robusto 1%** e **influence curve**.  
  • GitHub release: https://github.com/mreyes-astro/portafolio-rubin/releases/tag/v1.0.5-rnA  
  • Paquete reproducible: `release/rnA_v1.0.5/`  
  • Manuscrito (EN, v9): `docs/RN-A_en/Reyes_2025_RubinDP1_47Tuc_RN-A_v9_EN.pdf`

- **Release anterior:** v1.0.4-rnA — **Erratum**: se retira la frase “consistente con el SRD con amplio margen”.  
  • Erratum visible en la página de la release v1.0.4.  


Próximos:
- **RN-B (DP1 · 47 Tuc · Fotometría R(g))**: borrador en `docs/RN-B_R_of_g_47tuc.md` (con `data/.../rnB_metrics.json` placeholder).
- Otros proyectos DP0/DP1: en preparación.

---

## Estructura

```text
portafolio-rubin/
├─ notebooks/
│  └─ 47tuc/
│     ├─ rnA_per_coordinate_metrics.ipynb  # RMS por coordenada (+ CIs, P68 CI)
│     ├─ rnA_radius_robustness.ipynb       # Robustez vs radio (0.4–2.0″)
│     ├─ rnA_outliers_analysis.ipynb       # CSV > P95 (cola)
│     ├─ rnA_astrometry_47tuc.ipynb      # Notebook reproducible (RN-A)
│     ├─ dp1_47tuc_prep.ipynb            # Utilidades/preparación DP1
│     └─ figs/rnA_hist_sep.png           # Figura RN-A
├─ data/
│  └─ 47tuc_dp1/
│     ├─ rnA_matched_minimal.parquet     # Derivado mínimo (publicado)
│     └─ rnA_metrics.json                # Métricas + IC-95% (publicado)
├─ docs/
│  ├─ RN-A_astrometry_47tuc.md           # Texto RN-A (RNAAS-ready)
│  ├─ RN-A_release_notes.md              # Notas de release (método, hashes)
│  └─ RN-B_R_of_g_47tuc.md               # Borrador RN-B
├─ release/
│  └─ rnA_v1.0/                          # Paquete listo para Zenodo (v1.0.4-rnA)
├─ scripts/
│  └─ rna_bootstrap_ci.py                # Script para IC por bootstrap
├─ requirements.txt · environment.yml    # Reproducibilidad local
├─ CITATION.cff · .zenodo.json           # Metadatos de citación / Zenodo
└─ README.md
```

---

## Reproducibilidad rápida (local)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Recalcular métricas e IC-95 % desde el parquet derivado
python scripts/rna_bootstrap_ci.py \
  --parquet data/47tuc_dp1/rnA_matched_minimal.parquet \
  --out     data/47tuc_dp1/rnA_metrics.json \
  --B 5000 --seed 47
```

> Alternativa: los mismos artefactos están en `release/rnA_v1.0/` (idénticos a los de la release GitHub/Zenodo).

---

## Resumen científico (RN-A)

- **Muestra:** 47 Tuc (DP1, ComCam) × **Gaia DR3**  
- **Emparejamiento:** radio 2″ + **deduplicación 1:1** simétrica (nearest Rubin↔Gaia)  
- **Métricas:** **N = 1 113**, **P50 = 0.051″**, **P68 = 0.053″**, **P95 = 0.116″**  
- **Bootstrap:** B = 5000, seed = 47; IC-95 % para P50 y P95  
- **Control:** *offset-match* (+60″ en RA) ⇒ **0** pares ≤ 2″ (plano)  
- **Conclusión:** Reportamos percentiles radiales y el RMS por coordenada (Δα⋆, Δδ) con IC-95 %. Dado que el SRD (LPM-17) está definido por coordenada, no realizamos una verificación directa de cumplimiento aquí; proveemos estos números como referencia cuantitativa para este campo.

---

**Resumen cuantitativo (47 Tuc, DP1·ComCam, N=1113):**  
P50 = 0.0510″ [0.0507, 0.0514]; P68 = 0.0533″ [0.0530, 0.0538]; P95 = 0.1158″ [0.0978, 0.1707].  
RMS(Δα⋆) ≈ 131 mas [97.7, 162.3]; RMS(Δδ) ≈ 147 mas [104.3, 185.4].  
P50 ≈ 0.25 px a 0.2″/px (ComCam).  
Submuestras por radio r∈{0.4, 0.8, 1.0, 1.2, 1.5, 2.0}″: P50/P68 estables; P95 crece con r (cola).


## Cola y robustez (sanity)

- **Identidad (sanity):** `mean(r^2) = mean((Δα⋆)^2) + mean((Δδ)^2)` — coincide a precisión de máquina con el parquet publicado.

- **Descomposición núcleo/cola en el cuantil radial q95:**
  - `q95 = 0.11583″` (≈ `0.116″`)
  - `n_core = 1057`, `n_tail = 56` ⇒ `w_core = 1057/1113 ≈ 0.9497`
  - `E[r^2]_core = 0.002439 arcsec^2`
  - `E[r^2]_tail = 0.723691 arcsec^2`
  - **Mezcla:** `w_core·E[r^2]_core + (1−w_core)·E[r^2]_tail ≈ 0.03873 arcsec^2 ≃ mean(r^2)`

- **Métricas robustas (recorte 1% por r, q01–q99):**
  - `RMS_trim,1% (Δα⋆) = 78.27 mas`
  - `RMS_trim,1% (Δδ)  = 58.57 mas`

**Lectura correcta.** La cola (~5% de los pares) es pequeña pero muy pesada en `r^2`. Esto explica que el **RMS clásico por eje (131–147 mas)** supere los percentiles del núcleo (P50/P68 ≈ `0.051/0.053″`). La **curva de influencia** (RMS vs fracción incluida por cuantil de `r`) es plana hasta ~0.95 y se eleva al añadir el 5% final.

**Artefactos añadidos (repo):**
- `data/47tuc_dp1/rnA_influence_curve.csv` — tabla de la curva de influencia (RMS vs fracción incluida).
- `notebooks/47tuc/figs/rnA_influence_curve.png` — figura de la curva de influencia.
- `notebooks/47tuc/rnA_r2_sanity_and_influence.ipynb` — notebook: identidad de `mean(r^2)`, core/tail, RMS 1% y figura.

---


**Manuscrito (EN, v9):** `docs/RN-A_en/Reyes_2025_RubinDP1_47Tuc_RN-A_v9_EN.pdf`


## Recursos DP1 (enlaces vigentes)

- **Cross-match (tutorial):** https://dp1.lsst.io/tutorials/notebook/306/notebook-306-3.html  
- **Monster Reference Catalog:** https://dp1.lsst.io/tutorials/notebook/204/notebook-204-2.html  
- **Astrometric calibration (visita):** https://dp1.lsst.io/tutorials/notebook/204/notebook-204-3.html

---

## Buenas prácticas

- Derivados **inmutables** (Parquet/JSON) con **SHA256** en notas de release.
- **CITATION.cff** + badges DOI (versión y concepto).
- **Licenciamiento dual**: código MIT; datos/figuras derivados recomendados **CC-BY-4.0** en el paquete de release/Zenodo.
- Scripts/notebooks con **semilla** fijada y parámetros documentados (bootstrap).

---

## Citar

Reyes, M. (2025). **RN-A — Astrometry in 47 Tuc with Rubin DP1 (ComCam)** (v1.0.4-rnA). Zenodo. https://doi.org/10.5281/zenodo.17017865  
> Para citar “todas las versiones” usa el Concept DOI: https://doi.org/10.5281/zenodo.17017864

---

## Contacto

- **Email**: [mreyesb@gmail.com](mailto:mreyesb@gmail.com)  
- **GitHub**: [@mreyes-astro](https://github.com/mreyes-astro)

¡Pull requests y sugerencias son bienvenidos!

