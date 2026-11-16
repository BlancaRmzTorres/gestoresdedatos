
"""
PROYECTO BDPCD
Análisis de accidentes de tránsito terrestre en México durante 2025
mediante datos semiestructurados y tecnologías NoSQL.

Fuente: INEGI - ATUS 2025
Base de datos: bdpcd_atus
Colección: accidentes_2025

Requisitos:
    pip install -r requirements.txt

Configuración:
    La URI de MongoDB debe estar en la variable de entorno MONGODB_URI.

Ejecución:
    python consultas_atus.py
"""

import os
import sys
from pymongo import MongoClient
from pymongo.errors import PyMongoError


# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE", "bdpcd_atus")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION", "accidentes_2025")

if not MONGODB_URI:
    print("ERROR: No se encontró la variable MONGODB_URI.")
    print("Configura la variable de entorno antes de ejecutar.")
    sys.exit(1)


CAMPOS_FALLECIDOS = [
    "CONDMUERTO",
    "PASAMUERTO",
    "PEATMUERTO",
    "CICLMUERTO",
    "OTROMUERTO"
]

CAMPOS_LESIONADOS = [
    "CONDHERIDO",
    "PASAHERIDO",
    "PEATHERIDO",
    "CICLHERIDO",
    "OTROHERIDO"
]

CAMPOS_VICTIMAS = CAMPOS_FALLECIDOS + CAMPOS_LESIONADOS


# ============================================================
# 2. FUNCIONES AUXILIARES
# ============================================================

def encabezado(titulo):
    print("\n" + "=" * 75)
    print(titulo)
    print("=" * 75)


def imprimir_resultados(cursor):
    resultados = list(cursor)

    if not resultados:
        print("No se encontraron resultados.")
        return

    for resultado in resultados:
        print(resultado)


def sumar_campos(campos):
    """
    Genera una expresión MongoDB para sumar un conjunto de campos.
    Los valores nulos o inexistentes se consideran cero.
    """
    return {
        "$add": [
            {"$ifNull": [f"${campo}", 0]}
            for campo in campos
        ]
    }


# ============================================================
# 3. EJECUCIÓN DE LOS ANÁLISIS
# ============================================================

client = None

try:

    client = MongoClient(
        MONGODB_URI,
        serverSelectionTimeoutMS=15000,
        connectTimeoutMS=20000,
        socketTimeoutMS=60000
    )

    # Verificar conexión
    client.admin.command("ping")

    db = client[DATABASE_NAME]
    coleccion = db[COLLECTION_NAME]

    encabezado("CONEXIÓN A MONGODB")
    print("Conexión establecida correctamente.")
    print(f"Base de datos: {DATABASE_NAME}")
    print(f"Colección: {COLLECTION_NAME}")

    total_documentos = coleccion.count_documents({})

    # ========================================================
    # 1. TOTAL DE REGISTROS
    # ========================================================

    encabezado("1. TOTAL DE REGISTROS")

    print(f"Total de accidentes registrados: {total_documentos:,}")

    # ========================================================
    # 2. ACCIDENTES POR MES
    # ========================================================

    encabezado("2. ACCIDENTES POR MES")

    pipeline_mes = [
        {
            "$group": {
                "_id": "$MES",
                "total_accidentes": {"$sum": 1}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    for r in coleccion.aggregate(pipeline_mes):
        print(
            f"Mes {r['_id']}: "
            f"{r['total_accidentes']:,} accidentes"
        )

    # ========================================================
    # 3. ACCIDENTES POR ENTIDAD FEDERATIVA
    # ========================================================

    encabezado("3. TOP 10 ENTIDADES FEDERATIVAS")

    pipeline_entidad = [
        {
            "$group": {
                "_id": "$CVE_ENT",
                "total_accidentes": {"$sum": 1}
            }
        },
        {
            "$sort": {"total_accidentes": -1}
        },
        {
            "$limit": 10
        }
    ]

    for r in coleccion.aggregate(pipeline_entidad):
        print(
            f"Entidad {r['_id']}: "
            f"{r['total_accidentes']:,} accidentes"
        )

    # ========================================================
    # 4. ACCIDENTES POR TIPO
    # ========================================================

    encabezado("4. ACCIDENTES POR TIPO")

    pipeline_tipo = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "total_accidentes": {"$sum": 1}
            }
        },
        {
            "$sort": {"total_accidentes": -1}
        }
    ]

    for r in coleccion.aggregate(pipeline_tipo):
        porcentaje = (
            r["total_accidentes"] / total_documentos * 100
            if total_documentos else 0
        )

        print(
            f"Tipo: {r['_id']} | "
            f"Accidentes: {r['total_accidentes']:,} | "
            f"Porcentaje: {porcentaje:.2f}%"
        )

    # ========================================================
    # 5. REGISTROS CON CAMPOS FALTANTES
    # ========================================================

    encabezado("5. DIAGNÓSTICO DE CAMPOS PRINCIPALES")

    campos_revision = [
        "CVE_ENT",
        "MES",
        "TIPACCID",
        "CAUSAACCI"
    ]

    for campo in campos_revision:

        faltantes = coleccion.count_documents({
            "$or": [
                {campo: {"$exists": False}},
                {campo: None},
                {campo: ""}
            ]
        })

        porcentaje = (
            faltantes / total_documentos * 100
            if total_documentos else 0
        )

        print(
            f"{campo}: {faltantes:,} faltantes "
            f"({porcentaje:.2f}%)"
        )

    # ========================================================
    # 6. PRINCIPALES CAUSAS DE LOS ACCIDENTES
    # ========================================================

    encabezado("6. PRINCIPALES CAUSAS DE LOS ACCIDENTES")

    pipeline_causas = [
        {
            "$match": {
                "CAUSAACCI": {
                    "$nin": [None, ""]
                }
            }
        },
        {
            "$group": {
                "_id": "$CAUSAACCI",
                "total": {"$sum": 1}
            }
        },
        {
            "$sort": {"total": -1}
        },
        {
            "$limit": 10
        }
    ]

    for r in coleccion.aggregate(pipeline_causas):
        print(
            f"Causa: {r['_id']} | "
            f"Accidentes: {r['total']:,}"
        )

    # ========================================================
    # 7. PARTICIPACIÓN DE LOS VEHÍCULOS INVOLUCRADOS
    # ========================================================

    encabezado("7. VEHÍCULOS INVOLUCRADOS")

    campos_vehiculos = [
        "AUTOMOVIL",
        "CAMPASAJ",
        "MICROBUS",
        "PASCAMION",
        "OMNIBUS",
        "TRANVIA",
        "CAMIONETA",
        "CAMION",
        "TRACTOR",
        "FERROCARRI",
        "MOTOCICLET",
        "BICICLETA",
        "OTROVEHIC"
    ]

    pipeline_vehiculos = [
        {
            "$group": {
                "_id": None,
                **{
                    campo: {
                        "$sum": {"$ifNull": [f"${campo}", 0]}
                    }
                    for campo in campos_vehiculos
                }
            }
        }
    ]

    resultado_vehiculos = next(
        coleccion.aggregate(pipeline_vehiculos),
        None
    )

    if resultado_vehiculos:

        for campo in campos_vehiculos:
            print(
                f"{campo}: "
                f"{resultado_vehiculos[campo]:,}"
            )

        total_vehiculos = sum(
            resultado_vehiculos[campo]
            for campo in campos_vehiculos
        )

        print(f"\nTotal de registros de vehículos: {total_vehiculos:,}")

    # ========================================================
    # 8. DIAGNÓSTICO DE CAMPOS DE VÍCTIMAS
    # ========================================================

    encabezado("8. DIAGNÓSTICO DE CAMPOS DE VÍCTIMAS")

    for campo in ["NEMUERTO", "NEHERIDO"] + CAMPOS_VICTIMAS:

        existentes = coleccion.count_documents({
            campo: {"$exists": True}
        })

        distintos_cero = coleccion.count_documents({
            campo: {
                "$ne": 0,
                "$exists": True
            }
        })

        print(f"\nCampo: {campo}")
        print(f"Documentos con campo: {existentes:,}")
        print(f"Valores distintos de cero: {distintos_cero:,}")

    # ========================================================
    # 9. TOTAL DE FALLECIDOS POR CATEGORÍA
    # ========================================================

    encabezado("9. TOTAL DE FALLECIDOS POR CATEGORÍA")

    pipeline_fallecidos = [
        {
            "$group": {
                "_id": None,
                **{
                    campo: {
                        "$sum": {"$ifNull": [f"${campo}", 0]}
                    }
                    for campo in CAMPOS_FALLECIDOS
                }
            }
        }
    ]

    resultado_fallecidos = next(
        coleccion.aggregate(pipeline_fallecidos),
        None
    )

    total_fallecidos = 0

    if resultado_fallecidos:

        for campo in CAMPOS_FALLECIDOS:
            valor = resultado_fallecidos[campo]
            total_fallecidos += valor
            print(f"{campo}: {valor:,}")

        print(f"\nTOTAL DE FALLECIDOS: {total_fallecidos:,}")

    # ========================================================
    # 10. TOTAL DE LESIONADOS POR CATEGORÍA
    # ========================================================

    encabezado("10. TOTAL DE LESIONADOS POR CATEGORÍA")

    pipeline_lesionados = [
        {
            "$group": {
                "_id": None,
                **{
                    campo: {
                        "$sum": {"$ifNull": [f"${campo}", 0]}
                    }
                    for campo in CAMPOS_LESIONADOS
                }
            }
        }
    ]

    resultado_lesionados = next(
        coleccion.aggregate(pipeline_lesionados),
        None
    )

    total_lesionados = 0

    if resultado_lesionados:

        for campo in CAMPOS_LESIONADOS:
            valor = resultado_lesionados[campo]
            total_lesionados += valor
            print(f"{campo}: {valor:,}")

        print(f"\nTOTAL DE LESIONADOS: {total_lesionados:,}")

    # ========================================================
    # 11. VÍCTIMAS POR TIPO DE ACCIDENTE
    # ========================================================

    encabezado("11. VÍCTIMAS POR TIPO DE ACCIDENTE")

    pipeline_victimas_tipo = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "fallecidos": {
                    "$sum": sumar_campos(CAMPOS_FALLECIDOS)
                },
                "lesionados": {
                    "$sum": sumar_campos(CAMPOS_LESIONADOS)
                }
            }
        },
        {
            "$sort": {"fallecidos": -1}
        }
    ]

    for r in coleccion.aggregate(pipeline_victimas_tipo):

        print(
            f"Tipo: {r['_id']} | "
            f"Accidentes: {r['accidentes']:,} | "
            f"Fallecidos: {r['fallecidos']:,} | "
            f"Lesionados: {r['lesionados']:,}"
        )

    # ========================================================
    # 12. FALLECIDOS POR CADA 100 ACCIDENTES
    # ========================================================

    encabezado("12. FALLECIDOS POR CADA 100 ACCIDENTES")

    pipeline_tasa = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "fallecidos": {
                    "$sum": sumar_campos(CAMPOS_FALLECIDOS)
                }
            }
        },
        {
            "$project": {
                "_id": 1,
                "accidentes": 1,
                "fallecidos": 1,
                "fallecidos_por_100_accidentes": {
                    "$cond": [
                        {"$gt": ["$accidentes", 0]},
                        {
                            "$multiply": [
                                {
                                    "$divide": [
                                        "$fallecidos",
                                        "$accidentes"
                                    ]
                                },
                                100
                            ]
                        },
                        0
                    ]
                }
            }
        },
        {
            "$sort": {
                "fallecidos_por_100_accidentes": -1
            }
        }
    ]

    for r in coleccion.aggregate(pipeline_tasa):

        print(
            f"Tipo: {r['_id']} | "
            f"Accidentes: {r['accidentes']:,} | "
            f"Fallecidos: {r['fallecidos']:,} | "
            f"Tasa: {r['fallecidos_por_100_accidentes']:.2f}"
        )

    # ========================================================
    # 13. LESIONADOS POR CADA 100 ACCIDENTES
    # ========================================================

    encabezado("13. LESIONADOS POR CADA 100 ACCIDENTES")

    pipeline_tasa_lesionados = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "lesionados": {
                    "$sum": sumar_campos(CAMPOS_LESIONADOS)
                }
            }
        },
        {
            "$project": {
                "_id": 1,
                "accidentes": 1,
                "lesionados": 1,
                "lesionados_por_100_accidentes": {
                    "$cond": [
                        {"$gt": ["$accidentes", 0]},
                        {
                            "$multiply": [
                                {
                                    "$divide": [
                                        "$lesionados",
                                        "$accidentes"
                                    ]
                                },
                                100
                            ]
                        },
                        0
                    ]
                }
            }
        },
        {
            "$sort": {
                "lesionados_por_100_accidentes": -1
            }
        }
    ]

    for r in coleccion.aggregate(pipeline_tasa_lesionados):

        print(
            f"Tipo: {r['_id']} | "
            f"Accidentes: {r['accidentes']:,} | "
            f"Lesionados: {r['lesionados']:,} | "
            f"Tasa: {r['lesionados_por_100_accidentes']:.2f}"
        )

    # ========================================================
    # 14. DISTRIBUCIÓN DE ACCIDENTES POR DÍA DE LA SEMANA
    # ========================================================

    encabezado("14. ACCIDENTES POR DÍA DE LA SEMANA")

    pipeline_dias = [
        {
            "$group": {
                "_id": "$DIASEMANA",
                "total": {"$sum": 1}
            }
        },
        {
            "$sort": {"total": -1}
        }
    ]

    imprimir_resultados(coleccion.aggregate(pipeline_dias))

    # ========================================================
    # 15. DISTRIBUCIÓN DE ACCIDENTES POR ZONA
    # ========================================================

    encabezado("15. ACCIDENTES POR ZONA")

    pipeline_zona = [
        {
            "$group": {
                "_id": {
                    "urbana": "$URBANA",
                    "suburbana": "$SUBURBANA"
                },
                "total": {"$sum": 1}
            }
        },
        {
            "$sort": {"total": -1}
        }
    ]

    imprimir_resultados(coleccion.aggregate(pipeline_zona))

    # ========================================================
    # RESUMEN GENERAL
    # ========================================================

    encabezado("RESUMEN GENERAL DEL ANÁLISIS")

    print(f"Registros analizados: {total_documentos:,}")
    print(f"Total de fallecidos por categorías: {total_fallecidos:,}")
    print(f"Total de lesionados por categorías: {total_lesionados:,}")

    if total_documentos > 0:

        print(
            "Fallecidos por cada 100 accidentes (global): "
            f"{total_fallecidos / total_documentos * 100:.2f}"
        )

        print(
            "Lesionados por cada 100 accidentes (global): "
            f"{total_lesionados / total_documentos * 100:.2f}"
        )

    print("\nAnálisis ejecutado correctamente.")

except PyMongoError as error:

    print("\nERROR DE MONGODB")
    print(f"Detalle: {error}")

except Exception as error:

    print("\nERROR DURANTE EL ANÁLISIS")
    print(f"Detalle: {error}")

finally:

    if client is not None:
        client.close()
        print("\nConexión a MongoDB cerrada.")
