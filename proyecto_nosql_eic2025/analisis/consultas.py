"""Consultas NoSQL reutilizables. Nunca estimar TGF con el promedio de HNV."""
from __future__ import annotations

from typing import Iterable

METRICAS = {
    "escolaridad_promedio": "Escolaridad promedio (años)",
    "participacion_economica_pct": "Participación económica (%)",
    "mujeres_unidas_pct": "Mujeres unidas (%)",
    "autoadscripcion_indigena_pct": "Autoadscripción indígena (%)",
    "habla_lengua_indigena_pct": "Habla lengua indígena (%)",
    "promedio_hijos_nacidos_vivos": "Promedio de hijos nacidos vivos",
}

DESCRIPCIONES_TAMLOC_4 = {
    "1": "Menos de 2 500 habitantes",
    "2": "2 500 a 14 999 habitantes",
    "3": "15 000 a 49 999 habitantes",
    "4": "50 000 y más habitantes",
}


def filtro_territorial(entidades: Iterable[str] = (), tamanos: Iterable[str] = ()) -> dict:
    """Devuelve filtro $match explícito; sin valores = sin restricción."""
    match = {}
    ents = [str(e) for e in entidades]
    tams = [str(t) for t in tamanos]
    if ents:
        match["territorio.cve_ent"] = {"$in": ents}
    if tams:
        match["territorio.tamloc"] = {"$in": tams}
    return match


def pipeline_dominios(entidades=(), tamanos=(), limite=200) -> list[dict]:
    """Filtra, proyecta y ordena dominios; solo campos autorizados para interfaz."""
    if not 1 <= limite <= 10000:
        raise ValueError("El límite debe estar entre 1 y 10000.")
    filtro = filtro_territorial(entidades, tamanos)
    return [
        {"$match": filtro},
        {"$project": {
            "_id": 1,
            "cve_ent": "$territorio.cve_ent",
            "tamloc": "$territorio.tamloc",
            "tamloc_descripcion": "$territorio.tamloc_descripcion",
            "registros_microdato": "$conteos.registros_microdato",
            "poblacion_ponderada": "$conteos.poblacion_ponderada",
            **{campo: f"$indicadores.{campo}" for campo in METRICAS},
        }},
        {"$sort": {"cve_ent": 1, "tamloc": 1}},
        {"$limit": limite},
    ]


def pipeline_conteos_por_tamano(entidades=(), tamanos=()) -> list[dict]:
    """Agregación de dominios y tamaños muestrales, NO tasas ni promedios."""
    return [
        {"$match": filtro_territorial(entidades, tamanos)},
        {"$group": {
            "_id": "$territorio.tamloc",
            "dominios": {"$sum": 1},
            "registros_microdato": {"$sum": "$conteos.registros_microdato"},
            "poblacion_ponderada": {"$sum": "$conteos.poblacion_ponderada"},
        }},
        {"$sort": {"_id": 1}},
    ]


def pipeline_extremos(metrica: str, entidades=(), tamanos=()) -> list[dict]:
    """Rango descriptivo entre dominios; no prueba de significancia estadística."""
    if metrica not in METRICAS:
        raise ValueError(f"Métrica no permitida: {metrica}")
    ruta = f"$indicadores.{metrica}"
    return [
        {"$match": filtro_territorial(entidades, tamanos)},
        {"$match": {f"indicadores.{metrica}": {"$type": "number"}}},
        {"$group": {"_id": None, "min": {"$min": ruta}, "max": {"$max": ruta},
                    "dominios_validos": {"$sum": 1}}},
        {"$project": {"_id": 0, "min": 1, "max": 1, "dominios_validos": 1,
                       "amplitud": {"$subtract": ["$max", "$min"]}}},
    ]


def pipeline_promedio_dominios_por_tamano(metrica: str, entidades=(), tamanos=()) -> list[dict]:
    """Media aritmética NO ponderada de indicadores de DOMINIOS (evidencia $avg).

    Una observación = dominio entidad x tamaño de localidad, NO persona. Esta
    media no es una tasa/proporción poblacional ni sustituye la estimación con
    microdatos, numeradores, denominadores y factores de expansión.
    """
    if metrica not in METRICAS:
        raise ValueError(f"Métrica no permitida: {metrica}")
    return [
        {"$match": filtro_territorial(entidades, tamanos)},
        {"$match": {f"indicadores.{metrica}": {"$type": "number"}}},
        {"$group": {
            "_id": "$territorio.tamloc",
            "dominios_validos": {"$sum": 1},
            "media_no_ponderada_de_dominios": {"$avg": f"$indicadores.{metrica}"},
            "min": {"$min": f"$indicadores.{metrica}"},
            "max": {"$max": f"$indicadores.{metrica}"},
        }},
        {"$sort": {"_id": 1}},
    ]
