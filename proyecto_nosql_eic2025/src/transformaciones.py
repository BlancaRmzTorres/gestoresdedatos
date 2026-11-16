"""Reglas de limpieza y transformación basadas en el diccionario EIC 2025."""
from __future__ import annotations

import pandas as pd


EMPLEADOS = {"10", "13", "14", "15", "16", "17", "18", "19", "20"}
BUSCA_TRABAJO = {"30"}
PEA = EMPLEADOS | BUSCA_TRABAJO
NO_PEA = {"40", "50", "60", "70", "80"}
UNIDAS = {"01", "06", "07", "08"}


def normalizar_texto(df: pd.DataFrame) -> pd.DataFrame:
    """Quita espacios y convierte cadenas vacías a NA sin alterar códigos."""
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].str.strip().replace("", pd.NA)
    return df


def preparar_chunk(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia un bloque de microdatos y crea variables derivadas.

    Importante: los blancos por pase se conservan como NA; no se imputan.
    """
    df = normalizar_texto(df.copy())

    # Conversiones numéricas. Los códigos especiales se transforman a NA.
    df["FACTOR"] = pd.to_numeric(df["FACTOR"], errors="coerce")

    df["EDAD_NUM"] = pd.to_numeric(df["EDAD"], errors="coerce")
    df.loc[df["EDAD_NUM"] == 999, "EDAD_NUM"] = pd.NA

    df["ESCOACUM_NUM"] = pd.to_numeric(df["ESCOACUM"], errors="coerce")
    df.loc[df["ESCOACUM_NUM"] == 99, "ESCOACUM_NUM"] = pd.NA

    df["HNV_NUM"] = pd.to_numeric(df["HIJOS_NAC_VIVOS"], errors="coerce")
    df.loc[df["HNV_NUM"].isin([98, 99]), "HNV_NUM"] = pd.NA

    # Indicadores booleanos derivados. NA significa que no existe información
    # válida para construir el indicador en ese registro.
    conact_valido = df["CONACT"].isin(PEA | NO_PEA)
    df["PEA"] = pd.Series(pd.NA, index=df.index, dtype="boolean")
    df.loc[conact_valido, "PEA"] = df.loc[conact_valido, "CONACT"].isin(PEA)

    sit_valida = df["SITUA_CONYUGAL"].isin({"01","02","03","04","05","06","07","08","09"})
    df["UNIDA"] = pd.Series(pd.NA, index=df.index, dtype="boolean")
    df.loc[sit_valida, "UNIDA"] = df.loc[sit_valida, "SITUA_CONYUGAL"].isin(UNIDAS)

    indig_valida = df["PERTE_INDIGENA"].isin({"1", "3"})
    df["INDIGENA"] = pd.Series(pd.NA, index=df.index, dtype="boolean")
    df.loc[indig_valida, "INDIGENA"] = df.loc[indig_valida, "PERTE_INDIGENA"].eq("1")

    lengua_valida = df["HLENGUA"].isin({"1", "3"})
    df["HABLA_LENGUA_INDIGENA"] = pd.Series(pd.NA, index=df.index, dtype="boolean")
    df.loc[lengua_valida, "HABLA_LENGUA_INDIGENA"] = df.loc[lengua_valida, "HLENGUA"].eq("1")

    df["MUJER_15_49"] = (
        df["SEXO"].eq("3")
        & df["EDAD_NUM"].between(15, 49, inclusive="both")
    )

    bins = [15, 20, 25, 30, 35, 40, 45, 50]
    labels = ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"]
    df["GRUPO_EDAD"] = pd.cut(
        df["EDAD_NUM"], bins=bins, labels=labels, right=False
    ).astype("string")

    return df


def solo_mujeres_15_49(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve la población objetivo del proyecto."""
    return df.loc[df["MUJER_15_49"].fillna(False)].copy()
