"""Consultas de comprobacion con salida determinista y timeout de conexion."""
from __future__ import annotations
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config import COL_INDICADORES, MONGO_DB, MONGO_URI
from analisis.consultas import pipeline_conteos_por_tamano, pipeline_promedio_dominios_por_tamano


def main():
    try:
        with MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000) as cliente:
            cliente.admin.command("ping")
            col = cliente[MONGO_DB][COL_INDICADORES]
            n = col.count_documents({})
            if n == 0:
                raise SystemExit("La coleccion esta vacia; ejecuta 05_cargar_mongodb.py.")
            print(f"Coleccion: {MONGO_DB}.{COL_INDICADORES} | Documentos: {n}")
            print("\n1) Primeros cinco documentos por identificador")
            for doc in col.find({}, {"_id": 1, "territorio": 1, "indicadores": 1}).sort("_id", 1).limit(5):
                print(doc)
            print("\n2) Dominios de Aguascalientes (CVE_ENT = 01)")
            for doc in col.find({"territorio.cve_ent": "01"}).sort("territorio.tamloc", 1):
                print(doc["territorio"], doc["indicadores"])
            print("\n3) Mayor participacion economica")
            for doc in col.find({"indicadores.participacion_economica_pct": {"$ne": None}},
                                {"territorio": 1, "indicadores.participacion_economica_pct": 1}
                               ).sort([("indicadores.participacion_economica_pct", -1), ("_id", 1)]).limit(5):
                print(doc)
            print("\n4) Agregación $group + $sum: cobertura por tamaño de localidad")
            for r in col.aggregate(pipeline_conteos_por_tamano(), maxTimeMS=15000):
                print(r)
            print("\n5) Agregación $group + $avg: MEDIA NO PONDERADA ENTRE DOMINIOS de escolaridad")
            for r in col.aggregate(pipeline_promedio_dominios_por_tamano("escolaridad_promedio"), maxTimeMS=15000):
                print(r)
            print("AVISO: $avg entre dominios NO equivale a promedio poblacional ponderado.")
    except PyMongoError as exc:
        raise SystemExit(f"Error en consultas MongoDB: {exc}") from exc


if __name__ == "__main__":
    main()
