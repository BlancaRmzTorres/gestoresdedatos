"""Consultas preliminares para demostrar que la base NoSQL es funcional."""
from pymongo import MongoClient

from config import COL_INDICADORES, MONGO_DB, MONGO_URI


def main():
    cliente = MongoClient(MONGO_URI)
    col = cliente[MONGO_DB][COL_INDICADORES]

    print("\n1) Primeros documentos")
    for doc in col.find({}, {"_id": 1, "territorio": 1, "indicadores": 1}).limit(5):
        print(doc)

    print("\n2) Dominios de Aguascalientes (CVE_ENT = 01)")
    for doc in col.find({"territorio.cve_ent": "01"}).sort("territorio.tamloc", 1):
        print(doc["territorio"], doc["indicadores"])

    print("\n3) Mayor participación económica")
    for doc in col.find(
        {"indicadores.participacion_economica_pct": {"$ne": None}},
        {"territorio": 1, "indicadores.participacion_economica_pct": 1}
    ).sort("indicadores.participacion_economica_pct", -1).limit(5):
        print(doc)

    cliente.close()


if __name__ == "__main__":
    main()
