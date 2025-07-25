# portafolio-rubin
Repositorio personal de proyectos basados en los *Data Previews* (DP0.2 – simulación,  
DP1 – datos reales de ComCam) del **Vera C. Rubin Observatory**.  
El objetivo es construir un portafolio reproducible que demuestre habilidades en:

- Acceso a datos con la Rubin Science Platform (RSP)
- Consultas ADQL/TAP y uso de Butler
- Estadística robusta y visualización científica en Python
- Buenas prácticas de control de versiones y documentación

> Autor: **Marcelo Reyes** — mreyesb@gmail.com  
> Rama de trabajo principal: `feature/proj-1_47tuc`  

---

## 📂 Estructura inicial
\`\`\`
portafolio-rubin/
├─ notebooks/            # Jupyter Notebooks (análisis, prototipos, informes)
│   └─ 47tuc/            # Proyecto 1 – Validación fotométrica en 47 Tuc
├─ queries/              # Consultas ADQL almacenadas (*.sql)
├─ docs/                 # Diagramas, esquemas de tablas, PDFs de referencia
├─ AUDIT_LOG.md          # Bitácora de entorno, versiones y checkpoints
└─ README.md             # Este documento
\`\`\`

---

## 🔧 Requisitos y entorno

| Herramienta | Estado | Notas |
|-------------|--------|-------|
| **Rubin Science Platform** | ✔️ usado 100 % | El contenedor incluye `git`, `lsst-scipipe`, `numpy`, `astropy`, etc. |
| **Git + GitHub** | ✔️ | Flujo “solo navegador + terminal RSP”. |
| **Docker local (opcional)** | — | No necesario por ahora; se documentará más adelante. |

---

## 🚀 Uso rápido

\`\`\`bash
# Clonar el repo dentro de la RSP
git clone https://github.com/<tu-usuario>/portafolio-rubin.git
cd portafolio-rubin
git checkout -b feature/proj-1_47tuc   # rama de trabajo

# Abrir el notebook de benchmark DP0.2
# File ▸ Open ▸ notebooks/47tuc/dp02_benchmark.ipynb
\`\`\`

Todos los notebooks verifican automáticamente la versión de contenedor y guardan la huella en `AUDIT_LOG.md`.

---

## 🗺️ Hoja de ruta

| Fase | Proyecto | Estado | Tag/Release |
|------|----------|--------|-------------|
| 1 | **Benchmark DP0.2** — pipeline fotométrico básico | ✅ Completado 15-jul-2025 | `v1.0-dp02` |
| 2 | **Validación DP1** — 47 Tuc | 🚧 en curso | `v2.x` |
| 3 | Clasificador de artefactos en alertas | ⏳ | — |
| 4 | Auditoría de magnitudes absolutas de asteroides | ⏳ | — |

---

## 📜 Licencia

Se publicará bajo licencia **MIT** en el primer *release* (`v1.0-dp02`).  
Consulta el archivo `LICENSE` para los términos completos.

---

## 📝 Cómo citar

> Reyes, M. (2025). *Portafolio Rubin – proyectos DP0/DP1.* Zenodo. https://doi.org/10.xxxx/zenodo.xxxxx  
> (el DOI se añadirá al publicar el primer release).

---

## 🙋‍♂️ Contacto

Abre un **Issue** o escribe a **mreyesb@gmail.com** para comentarios o colaboración.
