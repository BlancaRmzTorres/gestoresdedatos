"""Selecciona, limpia y filtra mujeres de 15 a 49 años de la EIC 2025."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from config import ARCHIVO_PREDETERMINADO, CHUNKSIZE, SALIDAS_DIR, VARIABLES
from src.transformaciones import preparar_chunk, solo_mujeres_15_49


def argumentos():
    p = argparse.ArgumentParser()
    p.add_argument("--archivo", type=Path, default=ARCHIVO_PREDETERMINADO)
    p.add_argument("--chunksize", type=int, default=CHUNKSIZE)
    return p.parse_args()


def main():
    args = argumentos()
    salida = SALIDAS_DIR / "mujeres_15_49.csv"
    if salida.exists():
        salida.unlink()

    primera = True
    total_entrada = 0
    total_salida = 0

    for chunk in pd.read_csv(
        args.archivo,
        usecols=VARIABLES,
        dtype="string",
        chunksize=args.chunksize,
        low_memory=False,
    ):
        total_entrada += len(chunk)
        limpio = preparar_chunk(chunk)
        mujeres = solo_mujeres_15_49(limpio)
        total_salida += len(mujeres)

        columnas_salida = VARIABLES + [
            "EDAD_NUM", "ESCOACUM_NUM", "HNV_NUM", "PEA", "UNIDA",
            "INDIGENA", "HABLA_LENGUA_INDIGENA", "GRUPO_EDAD"
        ]
        mujeres[columnas_salida].to_csv(
            salida,
            mode="w" if primera else "a",
            header=primera,
            index=False,
            encoding="utf-8-sig",
        )
        primera = False

    print(f"Registros de entrada: {total_entrada:,}")
    print(f"Mujeres de 15 a 49 años: {total_salida:,}")
    print(f"Archivo preparado: {salida}")


if __name__ == "__main__":
    main()
