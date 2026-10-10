"""Convierte la base analítica en documentos JSON listos para MongoDB."""
from __future__ import annotations

import json
import math
from pathlib import Path

import pandas as pd

from config import SALIDAS_DIR


def valor(v):
    if pd.isna(v):
        return None
    if isinstance(v, float) and math.isfinite(v):
        return round(float(v), 4)
    if hasattr(v, "item"):
        return v.item()
    return v


def main():
    entrada = SALIDAS_DIR / "indicadores_territoriales.csv"
    df = pd.read_csv(entrada, dtype={"CVE_ENT": "string", "TAMLOC": "string"})

    docs = []
    for _, r in df.iterrows():
        docs.append({
            "_id": f"{r['CVE_ENT']}_{r['TAMLOC']}",
            "fuente": {
                "institucion": "INEGI",
                "programa": "Encuesta Intercensal 2025",
                "tabla_origen": "PERSONAS",
                "periodo": 2025,
            },
            "territorio": {
                "cve_ent": str(r["CVE_ENT"]),
                "tamloc": str(r["TAMLOC"]),
                "tamloc_descripcion": r["tamloc_descripcion"],
            },
            "universo": {
                "sexo": "Mujer",
                "edad_min": 15,
                "edad_max": 49,
            },
            "conteos": {
                "registros_microdato": int(r["registros"]),
                "poblacion_ponderada": valor(r["poblacion_ponderada"]),
            },
            "indicadores": {
                "escolaridad_promedio": valor(r["escolaridad_promedio"]),
                "participacion_economica_pct": valor(r["participacion_economica_pct"]),
                "mujeres_unidas_pct": valor(r["mujeres_unidas_pct"]),
                "autoadscripcion_indigena_pct": valor(r["autoadscripcion_indigena_pct"]),
                "habla_lengua_indigena_pct": valor(r["habla_lengua_indigena_pct"]),
                "promedio_hijos_nacidos_vivos": valor(r["promedio_hijos_nacidos_vivos"]),
            },
            "notas": {
                "tasa_global_fecundidad": "Pendiente de método específico. El promedio de hijos nacidos vivos no se interpreta como TGF."
            }
        })

    salida = SALIDAS_DIR / "indicadores_territoriales.json"
    with salida.open("w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)

    print(f"Documentos generados: {len(docs)}")
    print(f"JSON: {salida}")


if __name__ == "__main__":
    main()
