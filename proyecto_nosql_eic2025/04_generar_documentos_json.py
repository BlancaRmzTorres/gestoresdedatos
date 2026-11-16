"""Genera documentos MongoDB desde tablas territoriales de 5 y, si existen, 4 tamaños."""
from __future__ import annotations

import json
import math
from pathlib import Path
import pandas as pd
from config import SALIDAS_DIR

COMPONENTES = ["esc_num", "esc_den", "pea_num", "pea_den", "unida_num", "unida_den",
               "indigena_num", "indigena_den", "lengua_num", "lengua_den", "hnv_num", "hnv_den"]

def valor(v):
    if pd.isna(v):
        return None
    if isinstance(v, float) and math.isfinite(v):
        return round(float(v), 6)
    if hasattr(v, "item"):
        return v.item()
    return v


def convertir(entrada: Path, salida: Path, agrupacion: int):
    df = pd.read_csv(entrada, dtype={"CVE_ENT": "string", "TAMLOC": "string"})
    docs = []
    for _, r in df.iterrows():
        doc = {
            "_id": f"{r['CVE_ENT']}_{r['TAMLOC']}",
            "fuente": {
                "institucion": "INEGI", "programa": "Encuesta Intercensal 2025",
                "tabla_origen": "PERSONAS", "periodo": 2025, "categorias_tamloc": agrupacion,
            },
            "territorio": {
                "cve_ent": str(r["CVE_ENT"]), "tamloc": str(r["TAMLOC"]),
                "tamloc_descripcion": r["tamloc_descripcion"],
            },
            "universo": {"sexo": "Mujer", "edad_min": 15, "edad_max": 49},
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
            "notas": {"tasa_global_fecundidad":
                      "Pendiente de metodo especifico. Promedio HNV no es TGF."},
        }
        if all(c in df.columns for c in COMPONENTES):
            doc["componentes"] = {c: valor(r[c]) for c in COMPONENTES}
        docs.append(doc)
    with salida.open("w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)
    print(f"Documentos ({agrupacion} tamaños): {len(docs)} -> {salida}")


def main():
    entrada5 = SALIDAS_DIR / "indicadores_territoriales.csv"
    if not entrada5.exists():
        raise SystemExit(f"No existe {entrada5}")
    convertir(entrada5, SALIDAS_DIR / "indicadores_territoriales.json", 5)
    entrada4 = SALIDAS_DIR / "indicadores_territoriales_4.csv"
    if entrada4.exists():
        convertir(entrada4, SALIDAS_DIR / "indicadores_territoriales_4.json", 4)
    else:
        print("No se creo la coleccion 4 tamaños: exige procesamiento completo de microdatos.")

if __name__ == "__main__":
    main()
