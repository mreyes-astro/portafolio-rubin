# Portafolio Rubin 🔭

&#x20;

Repositorio personal para experimentos y proyectos basados en los **Data Previews** del [Vera C. Rubin Observatory](https://www.lsst.org/):

- **DP0.2** – catálogos simulados (DESC DC2)
- **DP1**    – datos reales de **ComCam**

El objetivo es construir un **portafolio reproducible** que demuestre destrezas en ciencia de datos astronómicos, pipeline LSST y buenas prácticas DevOps.

> Autor   : **Marcelo Reyes**  ｜ [*mreyesb@gmail.com*](mailto\:mreyesb@gmail.com)\
> Asistente : **RubinCopilot**\
> Rama activa : `feature/proj-1_47tuc`

---

## 1 · Estructura del repositorio

```text
portafolio-rubin/
├─ notebooks/
│   ├─ 47tuc/                 # Proyecto 1 – 47 Tucanae
│   │   ├─ dp02_benchmark.ipynb
│   │   └─ dp1_47tuc_prep.ipynb
│   └─ README.md             # Guía específica de subproyecto
├─ queries/                  # Scripts ADQL ( *.sql )
├─ docs/                     # Diagramas, PDFs de referencia
├─ data/                     # Salidas Parquet persistentes
├─ .github/workflows/        # CI ( smoke test Papermill )
├─ AUDIT_LOG.md              # Bitácora de entorno/ejecuciones
└─ README.md                 # ← este documento
```

---

## 2 · Requisitos mínimos

| Herramienta            | Versión recomendada          | Notas                                |
| ---------------------- | ---------------------------- | ------------------------------------ |
| Rubin Science Platform | `current` (LSST Stack ≥ v29) | Entorno Jupyter, acceso TAP + Butler |
| Git + GitHub           | ≥ 2.30                       | Flujo CLI en la terminal RSP         |
| Conda/Mamba (⟂)        | opcional                     | Para ejecución local                 |
| Docker (⟂)             | opcional                     | Imágenes reproducibles               |

---

## 3 · Uso rápido

```bash
# 1 · Clona el repo dentro de la RSP
$ git clone https://github.com/mreyes-astro/portafolio-rubin.git
$ cd portafolio-rubin

# 2 · Crea tu rama de trabajo
$ git checkout -b feature/<mi-rama>

# 3 · Abre el notebook de benchmark
# File ▶ Open ▶ notebooks/47tuc/dp02_benchmark.ipynb
```

> **Tip CI**: el workflow `notebook-smoke.yml` ejecuta Papermill con `CI_MODE=1` para verificar que cada notebook corre tras un `git clone`.\
> Consulta `.github/workflows/` si deseas extender las pruebas.

---

## 4 · Mapa de proyectos

| Fase  | Proyecto                                          | Estado 2025‑07‑29 | Tag / Release |
| ----- | ------------------------------------------------- | ----------------- | ------------- |
|  1    | **Benchmark DP0.2** – pipeline fotométrico mínimo | ✅ Completado      | `v1.0-dp02`   |
|  2    | **Validación DP1** – 47 Tuc cross‑match Gaia      | 🚧 En curso       | `v2.x`        |
|  3    | Clasificador de artefactos en alertas             | ⏳ Pendiente       | —             |
|  4    | Asteroides Habs – auditoría de magnitudes         | ⏳                 | —             |

Cada hito genera un *release* con DOI Zenodo y snapshot de datos Parquet.

---

## 5 · Buenas prácticas adoptadas

- **Estructura notebook estándar** (véase `docs/Notebook Markdown Style Guide`).
- **Control de versiones de datos** → Parquet inmutable bajo `data/`.
- **Pruebas CI** → `papermill --kernel LSST` smoke‑test.
- **AUDIT\_LOG.md** → hash de contenedor + métricas clave por ejecución.
- **Citación formal** → DPDD LSE‑163, SRD LPM‑17, papers relevantes.

---

## 6 · Licencia

Código bajo **MIT**.  Documentación bajo **CC‑BY‑4.0** salvo indicación contraria.

---

## 7 · Citar este repositorio

```
Reyes, M. (2025). Portafolio Rubin — proyectos DP0/DP1 (v1.0-dp02) [Computer software].
Zenodo. https://doi.org/10.5281/zenodo.1234567
```

> El DOI se actualizará automáticamente en cada release.

---

## 8 · Contacto

Para dudas, *issues* o colaboración:

- **Email** : [mreyesb@gmail.com](mailto\:mreyesb@gmail.com)
- **GitHub**: [@mreyes-astro](https://github.com/mreyes-astro)
- **Slack**  : `#rubin-dp0-es` / `#stack-club`

¡Pull requests y sugerencias son bienvenidos!

