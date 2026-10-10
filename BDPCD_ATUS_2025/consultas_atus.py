import os
from pymongo import MongoClient

uri = os.getenv("MONGODB_URI")

if not uri:
    raise RuntimeError("No se encontró la variable MONGODB_URI.")

client = MongoClient(uri, serverSelectionTimeoutMS=15000)

db = client["bdpcd_atus"]
coleccion = db["accidentes_2025"]

try:
    client.admin.command("ping")

    # ============================================================
    # 1. TOTAL DE REGISTROS
    # ============================================================

    print("\n=== 1. TOTAL DE REGISTROS ===")
    print(coleccion.count_documents({}))

    # ============================================================
    # 2. ACCIDENTES POR MES
    # ============================================================

    print("\n=== 2. ACCIDENTES POR MES ===")

    pipeline_mes = [
        {
            "$group": {
                "_id": "$MES",
                "total": {"$sum": 1}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    for r in coleccion.aggregate(pipeline_mes):
        print(f"Mes {r['_id']}: {r['total']:,} registros")

    # ============================================================
    # 3. ACCIDENTES POR ENTIDAD
    # ============================================================

    print("\n=== 3. ACCIDENTES POR ENTIDAD ===")

    pipeline_entidad = [
        {
            "$group": {
                "_id": "$CVE_ENT",
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

    for r in coleccion.aggregate(pipeline_entidad):
        print(f"Entidad {r['_id']}: {r['total']:,} registros")

    # ============================================================
    # 4. ACCIDENTES POR TIPO
    # ============================================================

    print("\n=== 4. ACCIDENTES POR TIPO ===")

    pipeline_tipo = [
        {
            "$group": {
                "_id": "$TIPACCID",
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

    for r in coleccion.aggregate(pipeline_tipo):
        print(f"Tipo {r['_id']}: {r['total']:,} registros")

    # ============================================================
    # 5. REGISTROS CON CAMPOS FALTANTES
    # ============================================================

    print("\n=== 5. REGISTROS CON CAMPOS FALTANTES ===")

    campos = ["CVE_ENT", "MES", "TIPACCID", "CAUSAACCI"]

    for campo in campos:
        faltantes = coleccion.count_documents({
            "$or": [
                {campo: {"$exists": False}},
                {campo: None},
                {campo: ""}
            ]
        })

        print(f"{campo}: {faltantes:,} registros sin valor")

    # ============================================================
    # 6. PRINCIPALES CAUSAS DE LOS ACCIDENTES
    # ============================================================

    print("\n=== 6. PRINCIPALES CAUSAS DE LOS ACCIDENTES ===")

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

    for resultado in coleccion.aggregate(pipeline_causas):
        print(
            f"Causa: {resultado['_id']} | "
            f"Accidentes: {resultado['total']:,}"
        )

    # ============================================================
    # 7. PERSONAS FALLECIDAS Y LESIONADAS
    # ============================================================

    print("\n=== 7. PERSONAS FALLECIDAS Y LESIONADAS ===")

    pipeline_victimas = [
        {
            "$group": {
                "_id": None,
                "fallecidos": {
                    "$sum": {"$ifNull": ["$NEMUERTO", 0]}
                },
                "lesionados": {
                    "$sum": {"$ifNull": ["$NEHERIDO", 0]}
                },
                "registros": {"$sum": 1}
            }
        }
    ]

    for resultado in coleccion.aggregate(pipeline_victimas):
        print(f"Registros analizados: {resultado['registros']:,}")
        print(f"Fallecidos reportados: {resultado['fallecidos']:,}")
        print(f"Lesionados reportados: {resultado['lesionados']:,}")

    # ============================================================
    # 8. VÍCTIMAS POR TIPO DE ACCIDENTE
    # ============================================================

    print("\n=== 8. VÍCTIMAS POR TIPO DE ACCIDENTE ===")

    pipeline_victimas_tipo = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "fallecidos": {
                    "$sum": {"$ifNull": ["$NEMUERTO", 0]}
                },
                "lesionados": {
                    "$sum": {"$ifNull": ["$NEHERIDO", 0]}
                }
            }
        },
        {
            "$sort": {"fallecidos": -1}
        }
    ]

    for resultado in coleccion.aggregate(pipeline_victimas_tipo):
        print(
            f"Tipo: {resultado['_id']} | "
            f"Accidentes: {resultado['accidentes']:,} | "
            f"Fallecidos: {resultado['fallecidos']:,} | "
            f"Lesionados: {resultado['lesionados']:,}"
        )

    # ============================================================
    # 9. DIAGNÓSTICO DE LOS CAMPOS DE VÍCTIMAS
    # ============================================================

    print("\n=== 9. DIAGNÓSTICO DE LOS CAMPOS DE VÍCTIMAS ===")

    campos = [
        "NEMUERTO",
        "NEHERIDO",
        "CONDMUERTO",
        "CONDHERIDO",
        "PASAMUERTO",
        "PASAHERIDO",
        "PEATMUERTO",
        "PEATHERIDO",
        "CICLMUERTO",
        "CICLHERIDO",
        "OTROMUERTO",
        "OTROHERIDO"
    ]

    for campo in campos:

        print(f"\nCampo: {campo}")

        existentes = coleccion.count_documents({
            campo: {"$exists": True}
        })

        distintos_cero = coleccion.count_documents({
            campo: {"$ne": 0, "$exists": True}
        })

        ejemplos = list(
            coleccion.find(
                {campo: {"$exists": True}},
                {"_id": 0, campo: 1}
            ).limit(5)
        )

        print(f"Documentos con campo: {existentes:,}")
        print(f"Valores distintos de cero: {distintos_cero:,}")
        print(f"Ejemplos: {ejemplos}")

    # ============================================================
    # 10. TIPOS DE DATOS EN MONGODB
    # ============================================================

    print("\n=== 10. TIPOS DE DATOS EN MONGODB ===")

    for campo in ["NEMUERTO", "NEHERIDO", "CAUSAACCI", "TIPACCID"]:

        pipeline_tipos = [
            {
                "$group": {
                    "_id": {"$type": f"${campo}"},
                    "total": {"$sum": 1}
                }
            },
            {
                "$sort": {"total": -1}
            }
        ]

        print(f"\nCampo: {campo}")

        for resultado in coleccion.aggregate(pipeline_tipos):
            print(
                f"Tipo BSON: {resultado['_id']} | "
                f"Registros: {resultado['total']:,}"
            )

    # ============================================================
    # 11. TOTAL DE FALLECIDOS Y LESIONADOS
    # ============================================================

    print("\n=== 11. TOTAL DE FALLECIDOS Y LESIONADOS ===")

    campos_fallecidos = [
        "CONDMUERTO",
        "PASAMUERTO",
        "PEATMUERTO",
        "CICLMUERTO",
        "OTROMUERTO"
    ]

    campos_lesionados = [
        "CONDHERIDO",
        "PASAHERIDO",
        "PEATHERIDO",
        "CICLHERIDO",
        "OTROHERIDO"
    ]

    campos = campos_fallecidos + campos_lesionados

    pipeline = [
        {
            "$group": {
                "_id": None,
                **{
                    campo: {
                        "$sum": {"$ifNull": [f"${campo}", 0]}
                    }
                    for campo in campos
                }
            }
        }
    ]

    documento = next(coleccion.aggregate(pipeline), None)

    if documento:

        print("\nFALLECIDOS POR CATEGORÍA:")

        for campo in campos_fallecidos:
            print(f"{campo}: {documento,}")

        print("\nLESIONADOS POR CATEGORÍA:")

        for campo in campos_lesionados:
            print(f"{campo}: {documento,}")

        total_fallecidos = sum(
            documento[campo]
            for campo in campos_fallecidos
        )

        total_lesionados = sum(
            documento[campo]
            for campo in campos_lesionados
        )

        print(f"\nTotal fallecidos: {total_fallecidos:,}")
        print(f"Total lesionados: {total_lesionados:,}")

    else:
        print("No se obtuvieron resultados.")

    # ============================================================
    # 12. VÍCTIMAS POR TIPO DE ACCIDENTE
    # ============================================================

    print("\n=== 12. VÍCTIMAS POR TIPO DE ACCIDENTE ===")

    pipeline_victimas_tipo = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "fallecidos": {
                    "$sum": {
                        "$add": [
                            {"$ifNull": ["$CONDMUERTO", 0]},
                            {"$ifNull": ["$PASAMUERTO", 0]},
                            {"$ifNull": ["$PEATMUERTO", 0]},
                            {"$ifNull": ["$CICLMUERTO", 0]},
                            {"$ifNull": ["$OTROMUERTO", 0]}
                        ]
                    }
                },
                "lesionados": {
                    "$sum": {
                        "$add": [
                            {"$ifNull": ["$CONDHERIDO", 0]},
                            {"$ifNull": ["$PASAHERIDO", 0]},
                            {"$ifNull": ["$PEATHERIDO", 0]},
                            {"$ifNull": ["$CICLHERIDO", 0]},
                            {"$ifNull": ["$OTROHERIDO", 0]}
                        ]
                    }
                }
            }
        },
        {
            "$sort": {"fallecidos": -1}
        }
    ]

    for resultado in coleccion.aggregate(pipeline_victimas_tipo):
        print(
            f"Tipo: {resultado['_id']} | "
            f"Accidentes: {resultado['accidentes']:,} | "
            f"Fallecidos: {resultado['fallecidos']:,} | "
            f"Lesionados: {resultado['lesionados']:,}"
        )

    # ============================================================
    # 13. FALLECIDOS POR CADA 100 ACCIDENTES
    # ============================================================

    print("\n=== 13. FALLECIDOS POR CADA 100 ACCIDENTES ===")

    pipeline_tasa = [
        {
            "$group": {
                "_id": "$TIPACCID",
                "accidentes": {"$sum": 1},
                "fallecidos": {
                    "$sum": {
                        "$add": [
                            {"$ifNull": ["$CONDMUERTO", 0]},
                            {"$ifNull": ["$PASAMUERTO", 0]},
                            {"$ifNull": ["$PEATMUERTO", 0]},
                            {"$ifNull": ["$CICLMUERTO", 0]},
                            {"$ifNull": ["$OTROMUERTO", 0]}
                        ]
                    }
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

    for resultado in coleccion.aggregate(pipeline_tasa):
        print(
            f"{resultado['_id']} | "
            f"Accidentes: {resultado['accidentes']:,} | "
            f"Fallecidos: {resultado['fallecidos']:,} | "
            f"Por cada 100 accidentes: "
            f"{resultado['fallecidos_por_100_accidentes']:.2f}"
        )

finally:
    client.close()