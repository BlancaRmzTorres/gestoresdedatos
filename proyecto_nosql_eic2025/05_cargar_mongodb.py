"""Carga idempotente de 5 tamaños y, cuando está disponible, 4 tamaños."""
from __future__ import annotations
from pymongo import MongoClient, UpdateOne
from pymongo.errors import PyMongoError
from config import COL_INDICADORES, MONGO_DB, MONGO_URI, SALIDAS_DIR
from verificar_documentos import validar_archivo


def cargar(coleccion, archivo):
    documentos, n = validar_archivo(archivo)
    operaciones = [UpdateOne({"_id": doc["_id"]},
                             {"$set": {k: v for k, v in doc.items() if k != "_id"}},
                             upsert=True) for doc in documentos]
    resultado = coleccion.bulk_write(operaciones, ordered=False)
    coleccion.create_index([("territorio.cve_ent", 1), ("territorio.tamloc", 1)])
    coleccion.create_index("indicadores.promedio_hijos_nacidos_vivos")
    ids = [doc["_id"] for doc in documentos]
    # El JSON incluido es la fuente autoritativa para cada colección. Evita
    # mezclar documentos obsoletos cuando cambia la cobertura entre corridas.
    coleccion.delete_many({"_id": {"$nin": ids}})
    coincidentes = coleccion.count_documents({"_id": {"$in": ids}})
    print(f"{coleccion.full_name}: {n} documentos, "
          f"{resultado.upserted_count} insertados, "
          f"{resultado.modified_count} actualizados, {coincidentes} comprobados.")
    if coincidentes != n:
        raise ValueError("Verificación fallida: faltan documentos en MongoDB.")


def main():
    archivos = [(COL_INDICADORES, SALIDAS_DIR / "indicadores_territoriales.json")]
    archivo4 = SALIDAS_DIR / "indicadores_territoriales_4.json"
    if archivo4.exists():
        archivos.append(("indicadores_territoriales_4", archivo4))
    try:
        with MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000) as cli:
            cli.admin.command("ping")
            bd = cli[MONGO_DB]
            for nombre, archivo in archivos:
                cargar(bd[nombre], archivo)
    except (PyMongoError, ValueError, OSError) as exc:
        raise SystemExit(f"Fallo la carga: {exc}") from exc

if __name__ == "__main__":
    main()
