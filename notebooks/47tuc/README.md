# Project 47 Tuc – DP1 Cross‑match  

![CI badge](https://github.com/mreyes-astro/portafolio-rubin/actions/workflows/notebook-smoke.yml/badge.svg)

## Descripción breve
Validación astrométrica y fotométrica en el cúmulo globular **47 Tucanae** usando el **Data Preview 1** (DP1, ComCam real) y un emparejamiento ≤ 2″ con **Gaia DR3**.  El objetivo científico inmediato es el **KPI 1** del *Plan Estratégico v5.1*:

\[ R \;=\; \sigma_{\mathrm{obs}} / \operatorname{median}(\sigma_{\mathrm{rep}}) \;\le\; 1.2 \]  
(en el rango \(g = 22 \pm 0.15\) mag).

---

## Estructura
- **`dp1_47tuc_prep.ipynb`** — extracción DP1 `Object` ⇢ *cross‑match* Gaia, guardado Parquet.
- **`dp1_47tuc_analysis.ipynb`** — cálculo de dispersión fotométrica y *bootstrap* de \(R\).
- **`data/47tuc_dp1/`** — archivos Parquet persistentes (`matched_dp1_gaia.parquet`, etc.).

> El subproyecto hereda la convención de carpetas descrita en el README raíz.

---

## Reproducibilidad rápida
```bash
# 1 · Clona y cambia a la rama de trabajo
$ git clone https://github.com/mreyes-astro/portafolio-rubin.git
$ cd portafolio-rubin
$ git checkout feature/proj-1_47tuc

# 2 · Ejecuta el smoke‑test (requiere kernel LSST)
$ CI_MODE=1 papermill notebooks/47tuc/dp1_47tuc_prep.ipynb out.ipynb
```

En modo **CI_MODE=1** se cargan subconjuntos de datos desde Parquet para que la prueba termine < 60 s.

---

## Métricas principales (2025‑08‑01)

| Muestra        | N     | Mediana Δθ | P95 Δθ |
| -------------- | ----- | ---------- | ------ |
| Rubin–Gaia 1 : 1 | 1 113 | 0.051″     | 0.116″ |

Todos los valores cumplen holgadamente la meta SRD A22 (≤ 0.25″ para el 95 %).

---

## KPIs del proyecto

| Nº | Descripción                                   | Meta  | Estado |
| -- | --------------------------------------------- | ----- | ------ |
| 1  | Pipeline corre sin errores (smoke CI)         | 100 % | ✔️ |
| 2  | \(R \le 1.2\) con IC 95 % ≤ 1.25             | ✔️    | 🟡 en progreso |

Los avances y versiones se registran en `AUDIT_LOG.md`.

---

## Créditos y contacto

Autor: **Marcelo Reyes**  \| Asistente: **RubinCopilot**  
Email: [mreyesb@gmail.com](mailto:mreyesb@gmail.com)  
Slack: `#rubin-dp0-es`, `#stack-club`

---

*Última edición:* 2025‑08‑01

