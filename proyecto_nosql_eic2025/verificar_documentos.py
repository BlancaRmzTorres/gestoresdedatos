"""Verifica integridad basica de los documentos territoriales antes de cargar MongoDB."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from config import SALIDAS_DIR, TAMLOC_DESC

INDICADORES = (
    "escolaridad_promedio", "participacion_economica_pct", "mujeres_unidas_pct",
    "autoadscripcion_indigena_pct", "habla_lengua_indigena_pct",
    "promedio_hijos_nacidos_vivos",
)


def validar_documentos(documentos: object) -> int:
    if not isinstance(documentos, list) or not documentos:
        raise ValueError("El JSON debe contener una lista no vacia de documentos.")
    vistos = set()
    for i, doc in enumerate(documentos, 1):
        if not isinstance(doc, dict):
            raise ValueError(f"Documento {i}: no es un objeto JSON.")
        for campo in ("_id", "fuente", "territorio", "universo", "conteos", "indicadores"):
            if campo not in doc:
                raise ValueError(f"Documento {i}: falta {campo}.")
        territorio = doc["territorio"]
        if not isinstance(territorio, dict):
            raise ValueError(f"Documento {i}: territorio invalido.")
        ent, tam = territorio.get("cve_ent"), territorio.get("tamloc")
        if not (isinstance(ent, str) and len(ent) == 2 and ent.isdigit() and 1 <= int(ent) <= 32):
            raise ValueError(f"Documento {i}: CVE_ENT invalida: {ent!r}")
        if tam not in TAMLOC_DESC:
            raise ValueError(f"Documento {i}: TAMLOC invalido: {tam!r}")
        if doc["_id"] != f"{ent}_{tam}":
            raise ValueError(f"Documento {i}: _id no coincide con CVE_ENT y TAMLOC.")
        if doc["_id"] in vistos:
            raise ValueError(f"Documento {i}: _id duplicado ({doc['_id']}).")
        vistos.add(doc["_id"])
        for nombre in ("fuente", "universo", "conteos", "indicadores"):
            if not isinstance(doc[nombre], dict):
                raise ValueError(f"Documento {i}: {nombre} no es un subdocumento.")
        registros = doc["conteos"].get("registros_microdato")
        if isinstance(registros, bool) or not isinstance(registros, int) or registros <= 0:
            raise ValueError(f"Documento {i}: registros_microdato invalido.")
        indicadores = doc["indicadores"]
        for nombre in INDICADORES:
            if nombre not in indicadores:
                raise ValueError(f"Documento {i}: falta indicador {nombre}.")
            valor = indicadores[nombre]
            if valor is not None:
                if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not math.isfinite(valor):
                    raise ValueError(f"Documento {i}: indicador {nombre} no es numerico finito.")
                if nombre.endswith("_pct") and not (0 <= valor <= 100):
                    raise ValueError(f"Documento {i}: porcentaje fuera de rango ({nombre}).")
    return len(vistos)


def validar_archivo(archivo: Path) -> tuple[list, int]:
    if not archivo.is_file():
        raise FileNotFoundError(f"No se encontro JSON: {archivo}")
    with archivo.open("r", encoding="utf-8") as f:
        documentos = json.load(f)
    return documentos, validar_documentos(documentos)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archivo", type=Path, default=SALIDAS_DIR / "indicadores_territoriales.json")
    args = p.parse_args()
    try:
        _, n = validar_archivo(args.archivo)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Validacion fallida: {exc}") from exc
    print(f"JSON valido: {n} documentos con identificadores territoriales unicos.")


if __name__ == "__main__":
    main()
