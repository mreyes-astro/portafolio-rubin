# Coherencia fotométrica temprana en 47 Tuc con DP1: curva R(g)

**Resumen.** Estimamos la coherencia fotométrica en DP1 (ComCam) para 47 Tuc midiendo  
\(R \equiv \sigma_{\perp, \mathrm{obs}} / \mathrm{median}(\sigma_{\perp, \mathrm{rep}})\) sobre el **residuo perpendicular** a la secuencia del CMD, por bins de magnitud \(g\) (18–22 mag). Reportamos **R(g)** con **IC-95 % (bootstrap)** y demostramos mitigaciones con **piso sistemático de 5–10 mmag** y **de-trending espacial** (gradientes de bajo orden).

---

## Método (resumen)

1) **Membresía** por PM (Gaia DR3) y construcción del CMD (g−r, g).  
2) **Ridgeline** robusta por ventanas de g; residuo **perpendicular** a la secuencia.  
3) \(\sigma_{\perp,\mathrm{obs}}\) (MAD×1.4826) y \(\sigma_{\perp,\mathrm{rep}}\) proyectando errores g/r sobre la normal.  
4) **R(g)** por bins (Δg≈0.3) con **bootstrap** (B≥2000) → banda **IC-95 %**.  
5) Mitigaciones: (i) **piso sistemático** 5–10 mmag en cuadratura; (ii) **de-trending espacial** del residuo ⟂ (grid RA×Dec).

> Productos: `data/47tuc_dp1/rnB_metrics.json` (tabla por bin) y figuras  
> `notebooks/47tuc/figs/rnB_R_of_g.png`, `notebooks/47tuc/figs/rnB_systematics_panel.png`.

---

## Resultados (mensaje clave)

- **R(g)** bruto se eleva hacia \(g\sim19.5\)–21 por **crowding** y gradientes de bajo orden.  
- Tras **piso 5–10 mmag** y **de-trending**, cae a **R≈1.5–2.0** en el régimen intermedio, lo que sugiere que el ruido reportado no domina: los **sistemáticos mmag** explican el exceso principal, con **anchura intrínseca** remanente (poblaciones/binariedad).

---

## Trabajo relacionado (anclaje y sistemáticos)

Estudios recientes en 47 Tuc anclan astrometría/fotometría al marco **Gaia DR3** y corrigen **variaciones de *zero-point*** y **reddening diferencial** a través del FOV, lo que respalda nuestras mitigaciones (piso y de-trending) para recuperar coherencia milimagnitud (ver, p.ej., arXiv:2106.14535).

## Selección de miembros y fondo

A magnitudes débiles, la **decontaminación por PM** y la verificación visual reducen el sesgo del CMD por fuentes de campo/galaxias compactas; esto justifica reportar **IC-95 %** en R(g) y controles por seeing/PSF.

## Anchura intrínseca

47 Tuc muestra **dinámica interna** (rotación/anisotropías) y **poblaciones múltiples**, lo que introduce una anchura física mínima de la secuencia; nuestras mitigaciones separan ese piso intrínseco de los **sistemáticos instrumentales** de bajo orden (p.ej., arXiv:1807.03511).

---

## Datos y código (derivados, DOI)

Publicaremos en Zenodo (DOI) los derivados mínimos:  
- `data/47tuc_dp1/rnB_metrics.json` (tabla de bins con IC-95 % y ejemplo de sistemáticos)  
- notebook `notebooks/47tuc/rnB_photometry_R_of_g.ipynb` (figuras finales)

**Agradecimientos.** Rubin DP1/RSP y Gaia DR3.
