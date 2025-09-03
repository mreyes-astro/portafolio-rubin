# -*- coding: utf-8 -*-
from pathlib import Path
import json
import nbformat as nbf

ROOT   = Path.home() / "portafolio-rubin"
NB_DIR = ROOT / "notebooks" / "47tuc"
DATA   = ROOT / "data" / "47tuc_dp1"
REL    = ROOT / "release" / "rnA_v1.0"
NB_DIR.mkdir(parents=True, exist_ok=True)

# -------------- Notebook A: métricas por coordenada + CI y P68 radial con CI --------------
nbA = nbf.v4.new_notebook()
cellsA = []

cellsA += [
    nbf.v4.new_markdown_cell(
        "# RN-A · Métricas por coordenada (Δα⋆, Δδ) con IC-95% + P68 radial\n"
        "Calcula **RMS por coordenada** (mas) con **IC-95% bootstrap (B=5000; seed=47)** y añade **CI para P68 radial**.\n"
        "Actualiza `rnA_metrics.json` en `data/...` (y también en `release/...` si existe)."
    ),
    nbf.v4.new_code_cell(
        "from pathlib import Path\n"
        "import json\n"
        "import numpy as np, pandas as pd\n"
        "from IPython.display import display\n"
        "\n"
        "ROOT = Path.home()/ 'portafolio-rubin'\n"
        "PARQUET = ROOT/'data/47tuc_dp1/rnA_matched_minimal.parquet'\n"
        "JSONP   = ROOT/'data/47tuc_dp1/rnA_metrics.json'\n"
        "JSON_REL= ROOT/'release/rnA_v1.0/rnA_metrics.json'\n"
        "B=5000; SEED=47\n"
        "\n"
        "df = pd.read_parquet(PARQUET)\n"
        "display(df.head())"
    ),
    nbf.v4.new_code_cell(
        "import numpy as np\n"
        "deg2asec = 3600.0\n"
        "dec_mid = 0.5*(df['coord_dec'].to_numpy() + df['dec_gaia'].to_numpy())\n"
        "cosd = np.cos(np.deg2rad(dec_mid))\n"
        "dra_arcsec  = (df['coord_ra'].to_numpy()  - df['ra_gaia'].to_numpy()) * cosd * deg2asec\n"
        "ddec_arcsec = (df['coord_dec'].to_numpy() - df['dec_gaia'].to_numpy()) * deg2asec\n"
        "sep_arcsec  = df['separation_arcsec'].to_numpy()\n"
        "N = len(df)\n"
        "N"
    ),
    nbf.v4.new_code_cell(
        "rng = np.random.default_rng(SEED)\n"
        "def rms(x):\n"
        "    x=np.asarray(x); return float(np.sqrt(np.mean(x**2)))\n"
        "def ci_rms(x, B=B):\n"
        "    x=np.asarray(x); n=len(x)\n"
        "    idx = rng.integers(0, n, size=(B,n))\n"
        "    samples = np.sqrt(np.mean((x[idx])**2, axis=1))\n"
        "    lo, hi = np.quantile(samples, [0.025, 0.975])\n"
        "    return float(lo), float(hi)\n"
        "def ci_percentile(x, q, B=B):\n"
        "    x=np.asarray(x); n=len(x)\n"
        "    idx = rng.integers(0, n, size=(B,n))\n"
        "    samples = np.percentile(x[idx], q, axis=1)\n"
        "    lo, hi = np.quantile(samples, [0.025, 0.975])\n"
        "    return float(lo), float(hi)"
    ),
    nbf.v4.new_code_cell(
        "res = {\n"
        "  'N_pairs': int(N),\n"
        "  'per_coordinate': {\n"
        "     'rms_ra_mas' : rms(dra_arcsec)*1000.0,\n"
        "     'rms_dec_mas': rms(ddec_arcsec)*1000.0,\n"
        "     'rms_ra_ci95_mas'  : [v*1000.0 for v in ci_rms(dra_arcsec)],\n"
        "     'rms_dec_ci95_mas' : [v*1000.0 for v in ci_rms(ddec_arcsec)],\n"
        "     'note': 'Δα⋆ incluye cosδ; unidades mas por coordenada.'\n"
        "  },\n"
        "  'radial': {\n"
        "     'P50_arcsec': float(np.percentile(sep_arcsec, 50)),\n"
        "     'P68_arcsec': float(np.percentile(sep_arcsec, 68)),\n"
        "     'P95_arcsec': float(np.percentile(sep_arcsec, 95)),\n"
        "     'P50_ci95_arcsec': list(ci_percentile(sep_arcsec, 50)),\n"
        "     'P68_ci95_arcsec': list(ci_percentile(sep_arcsec, 68)),\n"
        "     'P95_ci95_arcsec': list(ci_percentile(sep_arcsec, 95)),\n"
        "  }\n"
        "}\n"
        "import pandas as pd\n"
        "summary = pd.DataFrame({\n"
        "  'metric'   : ['rms_ra_mas','rms_dec_mas','P50_arcsec','P68_arcsec','P95_arcsec'],\n"
        "  'value'    : [res['per_coordinate']['rms_ra_mas'], res['per_coordinate']['rms_dec_mas'],\n"
        "                res['radial']['P50_arcsec'],res['radial']['P68_arcsec'],res['radial']['P95_arcsec']],\n"
        "  'ci95_low' : [res['per_coordinate']['rms_ra_ci95_mas'][0],res['per_coordinate']['rms_dec_ci95_mas'][0],\n"
        "                res['radial']['P50_ci95_arcsec'][0],res['radial']['P68_ci95_arcsec'][0],res['radial']['P95_ci95_arcsec'][0]],\n"
        "  'ci95_high': [res['per_coordinate']['rms_ra_ci95_mas'][1],res['per_coordinate']['rms_dec_ci95_mas'][1],\n"
        "                res['radial']['P50_ci95_arcsec'][1],res['radial']['P68_ci95_arcsec'][1],res['radial']['P95_ci95_arcsec'][1]],\n"
        "  'units'    : ['mas','mas','arcsec','arcsec','arcsec']\n"
        "})\n"
        "summary"
    ),
    nbf.v4.new_code_cell(
        "def update_json(path):\n"
        "    existing={}\n"
        "    if path.exists():\n"
        "        try:\n"
        "            existing=json.loads(path.read_text())\n"
        "        except Exception as e:\n"
        "            print('WARN: no se pudo leer JSON existente:', e)\n"
        "    existing['N_pairs']=res['N_pairs']\n"
        "    existing['P50_arcsec']=res['radial']['P50_arcsec']\n"
        "    existing['P68_arcsec']=res['radial']['P68_arcsec']\n"
        "    existing['P95_arcsec']=res['radial']['P95_arcsec']\n"
        "    existing['P50_ci95_arcsec']=res['radial']['P50_ci95_arcsec']\n"
        "    existing['P68_ci95_arcsec']=res['radial']['P68_ci95_arcsec']\n"
        "    existing['P95_ci95_arcsec']=res['radial']['P95_ci95_arcsec']\n"
        "    existing['per_coordinate']=res['per_coordinate']\n"
        "    existing.setdefault('units','arcsec')\n"
        "    existing.setdefault('bootstrap_B', 5000)\n"
        "    existing.setdefault('bootstrap_seed', 47)\n"
        "    existing['generator']={'script':'notebooks/47tuc/rnA_per_coordinate_metrics.ipynb','version':'v1.1-rnA'}\n"
        "    path.write_text(json.dumps(existing, indent=2))\n"
        "    return existing\n"
        "\n"
        "JSONP = Path(JSONP); JSON_REL = Path(JSON_REL)\n"
        "updated = update_json(JSONP)\n"
        "if JSON_REL.exists():\n"
        "    update_json(JSON_REL)\n"
        "from IPython.display import display\n"
        "display(updated)"
    ),
]
nbA['cells'] = cellsA
nbA.metadata['kernelspec'] = {'name':'python3','display_name':'Python 3'}
nbA.metadata['language_info'] = {'name':'python'}
(NB_DIR / "rnA_per_coordinate_metrics.ipynb").write_text(nbf.writes(nbA), encoding="utf-8")

# -------------- Notebook B: robustez al radio (subsets) --------------
nbB = nbf.v4.new_notebook()
cellsB = []

cellsB += [
    nbf.v4.new_markdown_cell(
        "# RN-A · Robustez al radio de búsqueda (subsets por separación)\n"
        "Calcula N/P50/P68/P95 para cortes de separación `r ∈ {0.4, 0.8, 1.2, 2.0}\"` sobre el parquet ya deduplicado.\n"
        "Añade el bloque `radii_check` al JSON y muestra una tabla.\n"
        "**Nota:** Verifica estabilidad; no estima FDR por *offset grid* (eso requiere catálogos originales)."
    ),
    nbf.v4.new_code_cell(
        "from pathlib import Path\n"
        "import json\n"
        "import numpy as np, pandas as pd\n"
        "from IPython.display import display\n"
        "\n"
        "ROOT = Path.home()/ 'portafolio-rubin'\n"
        "PARQUET = ROOT/'data/47tuc_dp1/rnA_matched_minimal.parquet'\n"
        "JSONP   = ROOT/'data/47tuc_dp1/rnA_metrics.json'\n"
        "JSON_REL= ROOT/'release/rnA_v1.0/rnA_metrics.json'\n"
        "df = pd.read_parquet(PARQUET)\n"
        "sep = df['separation_arcsec'].to_numpy()\n"
        "radii = [0.4, 0.8, 1.2, 2.0]\n"
        "rows = []\n"
        "for r in radii:\n"
        "    m = sep <= r\n"
        "    s = sep[m]\n"
        "    if len(s)==0:\n"
        "        rows.append((r, 0, np.nan, np.nan, np.nan))\n"
        "    else:\n"
        "        rows.append((r, int(m.sum()), float(np.percentile(s,50)), float(np.percentile(s,68)), float(np.percentile(s,95))))\n"
        "tab = pd.DataFrame(rows, columns=['radius_arcsec','N','P50','P68','P95'])\n"
        "display(tab)"
    ),
    nbf.v4.new_code_cell(
        "def merge_radii(path, tab):\n"
        "    try:\n"
        "        data=json.loads(path.read_text())\n"
        "    except Exception:\n"
        "        data={}\n"
        "    data['radii_check']={\n"
        "        'radius_arcsec': tab['radius_arcsec'].tolist(),\n"
        "        'N': tab['N'].tolist(),\n"
        "        'P50_arcsec': tab['P50'].tolist(),\n"
        "        'P68_arcsec': tab['P68'].tolist(),\n"
        "        'P95_arcsec': tab['P95'].tolist(),\n"
        "    }\n"
        "    path.write_text(json.dumps(data, indent=2))\n"
        "    return data\n"
        "\n"
        "JSONP = Path(JSONP); JSON_REL = Path(JSON_REL)\n"
        "updated = merge_radii(JSONP, tab)\n"
        "if JSON_REL.exists():\n"
        "    merge_radii(JSON_REL, tab)\n"
        "display(updated)"
    ),
]
nbB['cells'] = cellsB
nbB.metadata['kernelspec'] = {'name':'python3','display_name':'Python 3'}
nbB.metadata['language_info'] = {'name':'python'}
(NB_DIR / "rnA_radius_robustness.ipynb").write_text(nbf.writes(nbB), encoding="utf-8")

# -------------- Notebook C: outliers (>P95) --------------
nbC = nbf.v4.new_notebook()
cellsC = []

cellsC += [
    nbf.v4.new_markdown_cell(
        "# RN-A · Análisis rápido de outliers (cola > P95)\n"
        "Exporta un CSV con el 5% superior en separación (`separation_arcsec > P95`) para inspección."
    ),
    nbf.v4.new_code_cell(
        "from pathlib import Path\n"
        "import json\n"
        "import numpy as np, pandas as pd\n"
        "from IPython.display import display\n"
        "\n"
        "ROOT = Path.home()/ 'portafolio-rubin'\n"
        "PARQUET = ROOT/'data/47tuc_dp1/rnA_matched_minimal.parquet'\n"
        "JSONP   = ROOT/'data/47tuc_dp1/rnA_metrics.json'\n"
        "OUTCSV  = ROOT/'data/47tuc_dp1/rnA_outliers_gtP95.csv'\n"
        "\n"
        "df = pd.read_parquet(PARQUET)\n"
        "metrics = json.loads(Path(JSONP).read_text())\n"
        "p95 = metrics.get('P95_arcsec') or metrics.get('radial',{}).get('P95_arcsec')\n"
        "if p95 is None:\n"
        "    p95 = float(np.percentile(df['separation_arcsec'],95))\n"
        "    print('P95 tomado del parquet:', p95)\n"
        "mask = df['separation_arcsec'] > p95\n"
        "out = df.loc[mask].copy().sort_values('separation_arcsec', ascending=False)\n"
        "print('Filas outliers:', len(out), 'de', len(df))\n"
        "display(out.head())\n"
        "out.to_csv(OUTCSV, index=False)\n"
        "OUTCSV"
    ),
]
nbC['cells'] = cellsC
nbC.metadata['kernelspec'] = {'name':'python3','display_name':'Python 3'}
nbC.metadata['language_info'] = {'name':'python'}
(NB_DIR / "rnA_outliers_analysis.ipynb").write_text(nbf.writes(nbC), encoding="utf-8")

print('OK: notebooks creados en:', NB_DIR)
for p in ["rnA_per_coordinate_metrics.ipynb","rnA_radius_robustness.ipynb","rnA_outliers_analysis.ipynb"]:
    print(" -", NB_DIR/p)
