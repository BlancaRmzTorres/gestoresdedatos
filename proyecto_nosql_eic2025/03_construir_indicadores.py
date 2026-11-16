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

    if not partes:
        raise SystemExit("El archivo preparado esta vacio; revisa el CSV original y el universo de estudio.")
    total = pd.concat(partes, ignore_index=True)
    if total.empty:
        raise SystemExit("No se encontraron mujeres de 15 a 49 anos con dominios territoriales.")
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

    # Los componentes son sumables entre dominios; las tasas/promedios no lo son.
    componentes = ["esc_num", "esc_den", "pea_num", "pea_den", "unida_num", "unida_den",
                   "indigena_num", "indigena_den", "lengua_num", "lengua_den", "hnv_num", "hnv_den"]
    # Exportar en formato analítico íntegro: permite auditar denominadores más adelante.
    total[salida_cols + componentes].sort_values(["CVE_ENT", "TAMLOC"]).to_csv(
        archivo_salida, index=False, encoding="utf-8-sig", float_format="%.6f")

    # Nuevo producto de tesina: cuatro tamaños; 50 000+ = (4 + 5) combinados
    # SUMANDO componentes, no calculando medias simples de indicadores.
    dominios4 = total[["CVE_ENT", "TAMLOC", "registros", "poblacion_ponderada"] + componentes].copy()
    dominios4["TAMLOC"] = dominios4["TAMLOC"].replace({"5": "4"})
    dominios4 = dominios4.groupby(["CVE_ENT", "TAMLOC"], as_index=False).sum(numeric_only=True)
    descripciones4 = {
        "1": "Menos de 2 500 habitantes", "2": "De 2 500 a 14 999 habitantes",
        "3": "De 15 000 a 49 999 habitantes", "4": "50 000 y mas habitantes",
    }
    dominios4["tamloc_descripcion"] = dominios4["TAMLOC"].map(descripciones4)
    for resultado, num, den, factor_escala in (
        ("escolaridad_promedio", "esc_num", "esc_den", 1),
        ("participacion_economica_pct", "pea_num", "pea_den", 100),
        ("mujeres_unidas_pct", "unida_num", "unida_den", 100),
        ("autoadscripcion_indigena_pct", "indigena_num", "indigena_den", 100),
        ("habla_lengua_indigena_pct", "lengua_num", "lengua_den", 100),
        ("promedio_hijos_nacidos_vivos", "hnv_num", "hnv_den", 1),
    ):
        dominios4[resultado] = ((dominios4[num] / dominios4[den]) * factor_escala).where(dominios4[den] > 0)
    archivo4 = SALIDAS_DIR / "indicadores_territoriales_4.csv"
    dominios4[salida_cols + componentes].sort_values(["CVE_ENT", "TAMLOC"]).to_csv(
        archivo4, index=False, encoding="utf-8-sig", float_format="%.6f")
    print(f"Indicadores cinco tamaños: {archivo_salida} ({len(total)} dominios)")
    print(f"Indicadores cuatro tamaños: {archivo4} ({len(dominios4)} dominios)")
    print("Nota: HNV promedio NO equivale a TGF. Revisar precision muestral antes de inferir.")


if __name__ == "__main__":
    main()
