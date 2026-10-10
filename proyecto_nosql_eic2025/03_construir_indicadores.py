"""Construye indicadores ponderados por entidad federativa y tamaño de localidad."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from config import CHUNKSIZE, SALIDAS_DIR, TAMLOC_DESC


def argumentos():
    p = argparse.ArgumentParser()
    p.add_argument("--archivo", type=Path, default=SALIDAS_DIR / "mujeres_15_49.csv")
    p.add_argument("--chunksize", type=int, default=CHUNKSIZE)
    return p.parse_args()


def booleano_a_num(serie: pd.Series) -> pd.Series:
    mapa = {"True": 1.0, "False": 0.0, True: 1.0, False: 0.0}
    return serie.map(mapa)


def main():
    args = argumentos()
    partes = []

    for chunk in pd.read_csv(args.archivo, dtype="string", chunksize=args.chunksize):
        chunk["FACTOR"] = pd.to_numeric(chunk["FACTOR"], errors="coerce")
        chunk["ESCOACUM_NUM"] = pd.to_numeric(chunk["ESCOACUM_NUM"], errors="coerce")
        chunk["HNV_NUM"] = pd.to_numeric(chunk["HNV_NUM"], errors="coerce")
        for col in ["PEA", "UNIDA", "INDIGENA", "HABLA_LENGUA_INDIGENA"]:
            chunk[col + "_N"] = booleano_a_num(chunk[col])

        # Componentes de numerador y denominador para indicadores ponderados.
        chunk["POB_POND"] = chunk["FACTOR"]
        chunk["ESC_NUM"] = chunk["ESCOACUM_NUM"] * chunk["FACTOR"]
        chunk["ESC_DEN"] = chunk["FACTOR"].where(chunk["ESCOACUM_NUM"].notna())
        chunk["HNV_W_NUM"] = chunk["HNV_NUM"] * chunk["FACTOR"]
        chunk["HNV_W_DEN"] = chunk["FACTOR"].where(chunk["HNV_NUM"].notna())

        for col in ["PEA", "UNIDA", "INDIGENA", "HABLA_LENGUA_INDIGENA"]:
            chunk[col + "_NUM"] = chunk[col + "_N"] * chunk["FACTOR"]
            chunk[col + "_DEN"] = chunk["FACTOR"].where(chunk[col + "_N"].notna())

        agg = chunk.groupby(["CVE_ENT", "TAMLOC"], dropna=False).agg(
            registros=("ID_PERSONA", "count"),
            poblacion_ponderada=("POB_POND", "sum"),
            esc_num=("ESC_NUM", "sum"), esc_den=("ESC_DEN", "sum"),
            pea_num=("PEA_NUM", "sum"), pea_den=("PEA_DEN", "sum"),
            unida_num=("UNIDA_NUM", "sum"), unida_den=("UNIDA_DEN", "sum"),
            indigena_num=("INDIGENA_NUM", "sum"), indigena_den=("INDIGENA_DEN", "sum"),
            lengua_num=("HABLA_LENGUA_INDIGENA_NUM", "sum"), lengua_den=("HABLA_LENGUA_INDIGENA_DEN", "sum"),
            hnv_num=("HNV_W_NUM", "sum"), hnv_den=("HNV_W_DEN", "sum"),
        ).reset_index()
        partes.append(agg)

    total = pd.concat(partes, ignore_index=True)
    total = total.groupby(["CVE_ENT", "TAMLOC"], as_index=False).sum(numeric_only=True)

    def razon(num, den, escala=1.0):
        return (total[num] / total[den]).where(total[den] > 0) * escala

    total["tamloc_descripcion"] = total["TAMLOC"].map(TAMLOC_DESC)
    total["escolaridad_promedio"] = razon("esc_num", "esc_den")
    total["participacion_economica_pct"] = razon("pea_num", "pea_den", 100)
    total["mujeres_unidas_pct"] = razon("unida_num", "unida_den", 100)
    total["autoadscripcion_indigena_pct"] = razon("indigena_num", "indigena_den", 100)
    total["habla_lengua_indigena_pct"] = razon("lengua_num", "lengua_den", 100)
    total["promedio_hijos_nacidos_vivos"] = razon("hnv_num", "hnv_den")

    salida_cols = [
        "CVE_ENT", "TAMLOC", "tamloc_descripcion", "registros", "poblacion_ponderada",
        "escolaridad_promedio", "participacion_economica_pct", "mujeres_unidas_pct",
        "autoadscripcion_indigena_pct", "habla_lengua_indigena_pct",
        "promedio_hijos_nacidos_vivos",
    ]
    salida = total[salida_cols].sort_values(["CVE_ENT", "TAMLOC"])
    archivo_salida = SALIDAS_DIR / "indicadores_territoriales.csv"
    salida.to_csv(archivo_salida, index=False, encoding="utf-8-sig", float_format="%.4f")

    print(salida.to_string(index=False))
    print(f"\nIndicadores guardados en: {archivo_salida}")
    print("Nota: promedio de hijos nacidos vivos NO equivale a la TGF.")


if __name__ == "__main__":
    main()
