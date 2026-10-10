"""Carga los documentos de indicadores en MongoDB y crea índices."""
from __future__ import annotations

import json
from pymongo import MongoClient, UpdateOne
from pymongo.errors import ServerSelectionTimeoutError

from config import COL_INDICADORES, MONGO_DB, MONGO_URI, SALIDAS_DIR


def main():
    archivo = SALIDAS_DIR / "indicadores_territoriales.json"
    with archivo.open("r", encoding="utf-8") as f:
        documentos = json.load(f)

    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        cliente.admin.command("ping")
    except ServerSelectionTimeoutError as e:
        raise SystemExit(
            "No se pudo conectar a MongoDB. Inicia el servicio o ejecuta: docker compose up -d"
        ) from e

    coleccion = cliente[MONGO_DB][COL_INDICADORES]
    operaciones = [
        UpdateOne({"_id": doc["_id"]}, {"$set": doc}, upsert=True)
        for doc in documentos
    ]
    if operaciones:
        resultado = coleccion.bulk_write(operaciones, ordered=False)
        print(f"Insertados (upsert): {resultado.upserted_count}")
        print(f"Actualizados: {resultado.modified_count}")

    coleccion.create_index([("territorio.cve_ent", 1), ("territorio.tamloc", 1)])
    coleccion.create_index("indicadores.participacion_economica_pct")

    print(f"Base: {MONGO_DB}")
    print(f"Colección: {COL_INDICADORES}")
    print(f"Documentos totales: {coleccion.count_documents({})}")
    cliente.close()


if __name__ == "__main__":
    main()
