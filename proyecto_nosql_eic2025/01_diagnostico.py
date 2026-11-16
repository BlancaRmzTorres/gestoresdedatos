"""Diagnostico inicial; deteccion EXACTA de IDs duplicados en RAM o SQLite."""
from __future__ import annotations

import argparse
import sqlite3
import tempfile
from collections import Counter
from pathlib import Path

import pandas as pd

from config import ARCHIVO_PREDETERMINADO, CHUNKSIZE, SALIDAS_DIR, VARIABLES


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archivo", type=Path, default=ARCHIVO_PREDETERMINADO)
    p.add_argument("--chunksize", type=int, default=CHUNKSIZE)
    p.add_argument("--modo-duplicados", choices=("disco", "memoria"), default="disco")
    args = p.parse_args()
    archivo = args.archivo
    if not archivo.is_file():
        p.error(f"No se encontro: {archivo}")
    if args.chunksize <= 0:
        p.error("--chunksize debe ser mayor que cero")

    total = 0
    nulos = Counter()
    valores = {c: Counter() for c in ("SEXO", "TAMLOC", "CONACT", "SITUA_CONYUGAL")}
    duplicados_id = 0
    ids_vistos = set() if args.modo_duplicados == "memoria" else None

    # El indice SQLite temporal detecta duplicados ENTRE bloques sin llenar la RAM.
    # Se borra automaticamente al finalizar (o producirse un error).
    with tempfile.TemporaryDirectory(prefix="eic2025_ids_") as temporal:
        conexion = None
        try:
            if args.modo_duplicados == "disco":
                conexion = sqlite3.connect(str(Path(temporal) / "ids.sqlite"))
                conexion.execute("CREATE TABLE ids (id TEXT PRIMARY KEY) WITHOUT ROWID")
            for chunk in pd.read_csv(archivo, usecols=VARIABLES, dtype="string",
                                     chunksize=args.chunksize, low_memory=False):
                total += len(chunk)
                chunk = chunk.apply(lambda s: s.str.strip() if s.dtype.name == "string" else s)
                chunk = chunk.replace("", pd.NA)
                nulos.update(chunk.isna().sum().to_dict())
                for col in valores:
                    valores[col].update(chunk[col].fillna("<NULO>").value_counts().to_dict())

                ids = chunk["ID_PERSONA"].dropna().tolist()
                if conexion:
                    resultado = conexion.executemany(
                        "INSERT OR IGNORE INTO ids(id) VALUES (?)", ((v,) for v in ids))
                    duplicados_id += len(ids) - resultado.rowcount
                    conexion.commit()
                else:
                    for ident in ids:
                        if ident in ids_vistos:
                            duplicados_id += 1
                        else:
                            ids_vistos.add(ident)
        finally:
            if conexion:
                conexion.close()

    salida = SALIDAS_DIR / "diagnostico.txt"
    with salida.open("w", encoding="utf-8") as f:
        f.write("DIAGNOSTICO INICIAL - EIC 2025\n")
        f.write("=" * 50 + "\n")
        f.write(f"Archivo: {archivo}\n")
        f.write(f"Registros leidos: {total:,}\n")
        f.write(f"Variables seleccionadas: {len(VARIABLES)}\n")
        f.write(f"Duplicados por ID_PERSONA: {duplicados_id:,}\n\n")
        f.write("NULOS / BLANCOS OBSERVADOS\n")
        for col in VARIABLES:
            f.write(f"{col}: {nulos[col]:,}\n")
        f.write("\nDISTRIBUCIONES DE CONTROL\n")
        for col, conteos in valores.items():
            f.write(f"\n{col}\n")
            for v, n in sorted(conteos.items(), key=lambda x: str(x[0])):
                f.write(f"  {v}: {n:,}\n")

    print(f"Diagnostico terminado. Registros: {total:,}")
    print(f"Duplicados por ID_PERSONA: {duplicados_id:,}")
    print(f"Salida: {salida}")


if __name__ == "__main__":
    main()
