# Portafolio Rubin 🔭

Repositorio personal para experimentos y proyectos basados en los **Data Previews** del [Vera C. Rubin Observatory](https://www.lsst.org/).

[![DOI (versión)](https://zenodo.org/badge/DOI/10.5281/zenodo.17017865.svg)](https://doi.org/10.5281/zenodo.17017865)
[![DOI (concepto)](https://zenodo.org/badge/DOI/10.5281/zenodo.17017864.svg)](https://doi.org/10.5281/zenodo.17017864)

> Autor: **Marcelo Reyes** · [mreyesb@gmail.com](mailto:mreyesb@gmail.com)

---

## Estado (2025-09-01)

- **RN-A (DP1 · 47 Tuc · Astrometría)**: **publicado** como release **v1.0.4-rnA**  
  DOI de la versión: **10.5281/zenodo.17017865** · Concept DOI: **10.5281/zenodo.17017864**  
  Incluye parquet mínimo emparejado Rubin×Gaia, métricas (P50/P68/P95 + IC-95% bootstrap), figura e ipynb reproducible.

Próximos:
- **RN-B (DP1 · 47 Tuc · Fotometría R(g))**: borrador en `docs/RN-B_R_of_g_47tuc.md` (con `data/.../rnB_metrics.json` placeholder).
- Otros proyectos DP0/DP1: en preparación.

---

## Estructura

```text
portafolio-rubin/
├─ notebooks/
│  └─ 47tuc/
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
- **Conclusión:** Reportamos percentiles radiales y el RMS por coordenada (Δα⋆, Δδ) con IC-95 %. Dado que el SRD (LPM-17) está definido por coordenada, no realizamos una verificación directa de cumplimiento aquí; proveemos estos números como referencia cuantitativa. para este campo.

---

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

