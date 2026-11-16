"""
Reconstruye exclusivamente catalogo_entidades y catalogo_municipios
con datos tabulares del INEGI. Elimina esas dos colecciones antes de
reconstruirlas, conforme a la autorización del usuario.

NO elimina ni modifica accidentes_2025.
NO descarga ni almacena geometrías GeoJSON en MongoDB.
"""
import os
import sys
import requests
from pymongo import MongoClient, ASCENDING
from pymongo.errors import PyMongoError

BASE = "https://gaia.inegi.org.mx/wscatgeo/v2"
TIMEOUT = 90
HEADERS = {"User-Agent": "ATUS-2025-Dashboard/1.0"}

def get_json(url):
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, dict) and data.get("error"):
        raise RuntimeError(f"INEGI devolvió error: {data['error']}")
    return data

def first(row, *keys):
    for key in keys:
        value = row.get(key)
        if value not in (None, ""):
            return value
    return None

def code(value, width):
    return str(value).strip().zfill(width) if value is not None else None

def main():
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise RuntimeError("No se encontró MONGODB_URI. Configúrala en PowerShell.")

    client = MongoClient(uri, serverSelectionTimeoutMS=20000)
    client.admin.command("ping")
    db = client["bdpcd_atus"]

    accidents_before = db["accidentes_2025"].count_documents({})
    if accidents_before != 379643:
        print(f"AVISO: accidentes_2025 tiene {accidents_before:,} documentos; se conservará tal cual.")

    # La autorización cubre exclusivamente estas dos colecciones.
    for name in ("catalogo_entidades", "catalogo_municipios"):
        if name in db.list_collection_names():
            db.drop_collection(name)
            print(f"Colección eliminada para reconstrucción: {name}")

    entities = db["catalogo_entidades"]
    municipalities = db["catalogo_municipios"]

    # Catálogo de entidades: se conserva únicamente la información tabular.
    for n in range(1, 33):
        ent = f"{n:02d}"
        url = f"{BASE}/geo/mgee/{ent}"
        data = get_json(url)
        features = data.get("features", [])
        if not features:
            raise RuntimeError(f"INEGI no devolvió la entidad {ent}")

        props = features[0].get("properties") or {}
        cve_ent = code(first(props, "cve_ent", "CVE_ENT", "cvegeo", "CVEGEO") or ent, 2)
        doc = {
            "CVE_ENT": cve_ent,
            "NOM_ENT": first(props, "nomgeo", "NOM_ENT", "nom_ent", "nombre"),
            "NOM_ABREV": first(props, "nom_abrev", "NOM_ABREV"),
            "fuente": "INEGI - Catálogo Único de Claves Geoestadísticas",
        }
        entities.insert_one(doc)
        print(f"Entidad {cve_ent}: {doc['NOM_ENT']}")

    # Catálogo municipal tabular: no se consultan geometrías.
    total_munis = 0
    for n in range(1, 33):
        ent = f"{n:02d}"
        url = f"{BASE}/mgem/{ent}"
        data = get_json(url)
        rows = data.get("datos", [])
        if not isinstance(rows, list):
            raise RuntimeError(f"Respuesta municipal inválida para entidad {ent}")

        docs = []
        for row in rows:
            cve_ent = code(first(row, "cve_ent", "CVE_ENT") or ent, 2)
            cve_mun = code(first(row, "cve_mun", "CVE_MUN"), 3)
            cvegeo = code(first(row, "cvegeo", "CVEGEO"), 5)
            if not cvegeo and cve_mun:
                cvegeo = cve_ent + cve_mun
            if not cvegeo or not cve_mun:
                print(f"AVISO: fila sin clave municipal válida en entidad {ent}: {row}")
                continue

            docs.append({
                "CVEGEO": cvegeo,
                "CVE_ENT": cve_ent,
                "CVE_MUN": cve_mun,
                "NOM_ENT": first(row, "nom_ent", "NOM_ENT"),
                "NOM_MUN": first(row, "nomgeo", "NOM_MUN", "nom_mun"),
                "CVE_CAB": first(row, "cve_cab", "CVE_CAB"),
                "NOM_CAB": first(row, "nom_cab", "NOM_CAB"),
                "Pob_Total": row.get("pob_total"),
                "Pob_Femenina": row.get("pob_femenina"),
                "Pob_Masculina": row.get("pob_masculina"),
                "Total_Viviendas_Habitadas": row.get("total_viviendas_habitadas"),
                "fuente": "INEGI - Catálogo Único de Claves Geoestadísticas",
            })

        if docs:
            municipalities.insert_many(docs, ordered=True)
            total_munis += len(docs)
        print(f"Entidad {ent}: {len(docs)} municipios")

    entities.create_index([("CVE_ENT", ASCENDING)], unique=True)
    municipalities.create_index([("CVEGEO", ASCENDING)], unique=True)
    municipalities.create_index([("CVE_ENT", ASCENDING), ("CVE_MUN", ASCENDING)])

    accidents_after = db["accidentes_2025"].count_documents({})
    print("\nRECONSTRUCCIÓN TERMINADA")
    print("Entidades:", entities.count_documents({}))
    print("Municipios:", municipalities.count_documents({}))
    print("Tamaño de catálogo_entidades:", db.command("collStats", "catalogo_entidades").get("storageSize"), "bytes")
    print("Tamaño de catálogo_municipios:", db.command("collStats", "catalogo_municipios").get("storageSize"), "bytes")
    print("Accidentes antes:", accidents_before)
    print("Accidentes después:", accidents_after)
    print("Colección accidentes_2025 modificada: NO")
    client.close()

if __name__ == "__main__":
    try:
        main()
    except (requests.RequestException, PyMongoError, RuntimeError, ValueError) as exc:
        print("\nERROR:", exc)
        sys.exit(1)
