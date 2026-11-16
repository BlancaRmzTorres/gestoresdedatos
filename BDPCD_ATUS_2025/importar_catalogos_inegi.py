"""
Importa catálogos y geometrías oficiales del INEGI a MongoDB Atlas.
No modifica ni elimina la colección accidentes_2025.

Colecciones creadas/actualizadas:
- catalogo_entidades
- catalogo_municipios

Cada documento geográfico incluye la geometría GeoJSON oficial del INEGI.
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
        raise RuntimeError(f"INEGI devolvió error en {url}: {data['error']}")
    return data

def get_features(data, url):
    features = data.get("features") if isinstance(data, dict) else None
    if not isinstance(features, list):
        raise RuntimeError(f"La respuesta no contiene una colección GeoJSON válida: {url}")
    return features

def normalize_code(value, width):
    if value is None:
        return None
    return str(value).strip().zfill(width)

def props_of(feature):
    return feature.get("properties") or {}

def first_prop(props, *names):
    for name in names:
        if props.get(name) not in (None, ""):
            return props[name]
    return None

def main():
    uri = os.getenv("MONGODB_URI")
    if not uri:
        print("ERROR: configura MONGODB_URI en PowerShell antes de ejecutar.")
        sys.exit(1)

    client = MongoClient(uri, serverSelectionTimeoutMS=20000)
    client.admin.command("ping")
    db = client["bdpcd_atus"]
    col_states = db["catalogo_entidades"]
    col_munis = db["catalogo_municipios"]

    # Consultar las 32 geometrías estatales individualmente.
    state_count = 0
    for n in range(1, 33):
        code = f"{n:02d}"
        url = f"{BASE}/geo/mgee/{code}"
        geo = get_json(url)
        features = get_features(geo, url)
        if not features:
            print(f"AVISO: INEGI no devolvió geometría estatal para {code}")
            continue

        feature = features[0]
        props = props_of(feature)
        cve_ent = normalize_code(first_prop(props, "cve_ent", "CVE_ENT", "cvegeo", "CVEGEO") or code, 2)
        name = first_prop(props, "nomgeo", "NOM_ENT", "nom_ent", "nombre")
        short_name = first_prop(props, "nom_abrev", "NOM_ABREV")

        document = {
            "CVE_ENT": cve_ent,
            "NOM_ENT": name,
            "NOM_ABREV": short_name,
            "geometry": feature.get("geometry"),
            "fuente": "INEGI - Marco Geoestadístico",
        }
        if not document["geometry"]:
            raise RuntimeError(f"Geometría estatal ausente para clave {code}")
        col_states.replace_one({"CVE_ENT": cve_ent}, document, upsert=True)
        state_count += 1
        print(f"Entidad {cve_ent}: {name or 'nombre pendiente'}")

    # Consultar los municipios y polígonos por entidad para evitar respuestas masivas.
    municipality_count = 0
    for n in range(1, 33):
        ent = f"{n:02d}"

        tab_url = f"{BASE}/mgem/{ent}"
        tab_data = get_json(tab_url)
        tab_rows = tab_data.get("datos", []) if isinstance(tab_data, dict) else []
        if not isinstance(tab_rows, list):
            raise RuntimeError(f"Respuesta tabular municipal no válida para entidad {ent}")

        geo_url = f"{BASE}/geo/mgem/{ent}"
        geo_data = get_json(geo_url)
        geo_features = get_features(geo_data, geo_url)

        geometry_by_cvegeo = {}
        for feature in geo_features:
            props = props_of(feature)
            key = normalize_code(first_prop(props, "cvegeo", "CVEGEO"), 5)
            if key and feature.get("geometry"):
                geometry_by_cvegeo[key] = feature["geometry"]

        for row in tab_rows:
            cve_ent = normalize_code(first_prop(row, "cve_ent", "CVE_ENT") or ent, 2)
            cve_mun = normalize_code(first_prop(row, "cve_mun", "CVE_MUN"), 3)
            cvegeo = normalize_code(first_prop(row, "cvegeo", "CVEGEO"), 5)
            if not cvegeo and cve_mun:
                cvegeo = cve_ent + cve_mun
            if not cvegeo:
                print(f"AVISO: municipio sin clave en entidad {ent}: {row}")
                continue

            document = {
                "CVEGEO": cvegeo,
                "CVE_ENT": cve_ent,
                "CVE_MUN": cve_mun,
                "NOM_ENT": first_prop(row, "nom_ent", "NOM_ENT"),
                "NOM_MUN": first_prop(row, "nomgeo", "NOM_MUN", "nom_mun"),
                "CVE_CAB": first_prop(row, "cve_cab", "CVE_CAB"),
                "NOM_CAB": first_prop(row, "nom_cab", "NOM_CAB"),
                "Pob_Total": row.get("pob_total"),
                "Pob_Femenina": row.get("pob_femenina"),
                "Pob_Masculina": row.get("pob_masculina"),
                "Total_Viviendas_Habitadas": row.get("total_viviendas_habitadas"),
                "geometry": geometry_by_cvegeo.get(cvegeo),
                "fuente": "INEGI - Catálogo Único y Marco Geoestadístico",
            }
            col_munis.replace_one({"CVEGEO": cvegeo}, document, upsert=True)
            municipality_count += 1

        print(f"Entidad {ent}: {len(tab_rows)} municipios tabulares; {len(geo_features)} geometrías")

    # Índices para filtros, relaciones y consultas geoespaciales.
    col_states.create_index([("CVE_ENT", ASCENDING)], unique=True)
    col_munis.create_index([("CVEGEO", ASCENDING)], unique=True)
    col_munis.create_index([("CVE_ENT", ASCENDING), ("CVE_MUN", ASCENDING)])
    col_states.create_index([("geometry", "2dsphere")])
    col_munis.create_index([("geometry", "2dsphere")])

    print("\nIMPORTACIÓN TERMINADA")
    print("Colección accidentes_2025: no fue modificada.")
    print("Entidades procesadas:", state_count)
    print("Municipios procesados/actualizados:", municipality_count)
    print("Documentos en catalogo_entidades:", col_states.count_documents({}))
    print("Documentos en catalogo_municipios:", col_munis.count_documents({}))
    print("Municipios sin geometría:", col_munis.count_documents({"geometry": None}))
    print("Base de datos:", db.name)
    client.close()

if __name__ == "__main__":
    try:
        main()
    except (requests.RequestException, PyMongoError, RuntimeError, ValueError) as exc:
        print("\nERROR:", exc)
        sys.exit(1)
