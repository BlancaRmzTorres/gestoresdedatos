"""Diagnóstico inicial de calidad del archivo de personas de la EIC 2025."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import pandas as pd

from config import ARCHIVO_PREDETERMINADO, CHUNKSIZE, SALIDAS_DIR, VARIABLES


def argumentos():
    p = argparse.ArgumentParser()
    p.add_argument("--archivo", type=Path, default=ARCHIVO_PREDETERMINADO)
    p.add_argument("--chunksize", type=int, default=CHUNKSIZE)
    return p.parse_args()


def main():
    args = argumentos()
    archivo = args.archivo
    if not archivo.exists():
        raise FileNotFoundError(f"No se encontró: {archivo}")

    total = 0
    nulos = Counter()
    valores = {c: Counter() for c in ["SEXO", "TAMLOC", "CONACT", "SITUA_CONYUGAL"]}
    ids_vistos = set()
    duplicados_id = 0

    for chunk in pd.read_csv(
        archivo,
        usecols=VARIABLES,
        dtype="string",
        chunksize=args.chunksize,
        low_memory=False,
    ):
        total += len(chunk)
        chunk = chunk.apply(lambda s: s.str.strip() if s.dtype.name == "string" else s)
        chunk = chunk.replace("", pd.NA)
        nulos.update(chunk.isna().sum().to_dict())

        for col in valores:
            valores[col].update(chunk[col].fillna("<NULO>").value_counts().to_dict())

        for ident in chunk["ID_PERSONA"].dropna():
            if ident in ids_vistos:
                duplicados_id += 1
            else:
                ids_vistos.add(ident)

    salida = SALIDAS_DIR / "diagnostico.txt"
    with salida.open("w", encoding="utf-8") as f:
        f.write("DIAGNÓSTICO INICIAL - EIC 2025\n")
        f.write("=" * 50 + "\n")
        f.write(f"Archivo: {archivo}\n")
        f.write(f"Registros leídos: {total:,}\n")
        f.write(f"Variables seleccionadas: {len(VARIABLES)}\n")
        f.write(f"Duplicados por ID_PERSONA: {duplicados_id:,}\n\n")
        f.write("NULOS / BLANCOS OBSERVADOS\n")
        for col in VARIABLES:
            f.write(f"{col}: {nulos[col]:,}\n")
        f.write("\nDISTRIBUCIONES DE CONTROL\n")
        for col, conteos in valores.items():
            f.write(f"\n{col}\n")
            for valor, n in sorted(conteos.items(), key=lambda x: str(x[0])):
                f.write(f"  {valor}: {n:,}\n")

    print(f"Diagnóstico terminado. Registros: {total:,}")
    print(f"Duplicados por ID_PERSONA: {duplicados_id:,}")
    print(f"Salida: {salida}")


if __name__ == "__main__":
    main()
