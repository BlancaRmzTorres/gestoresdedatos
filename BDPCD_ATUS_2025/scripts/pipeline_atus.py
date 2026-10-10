"""
Pipeline preliminar para preparar ATUS 2025 y cargarlo en MongoDB.
Uso:
  1. Coloca atus_anual_2025.csv en data/raw/
  2. pip install -r requirements.txt
  3. python scripts/pipeline_atus.py
  4. Para cargar en MongoDB define MONGODB_URI en el entorno.
"""
from pathlib import Path
import json
import os
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "raw" / "atus_anual_2025.csv"
OUTPUT_CSV = ROOT / "data" / "processed" / "atus_2025_limpio.csv"
OUTPUT_JSONL = ROOT / "data" / "processed" / "atus_2025.jsonl"

# Campos que representan cantidades o valores numéricos.
NUMERIC_FIELDS = [
    "ANIO", "MES", "ID_HORA", "ID_MINUTO", "ID_DIA", "ID_EDAD",
    "AUTOMOVIL", "CAMPASAJ", "MICROBUS", "PASCAMION", "OMNIBUS",
    "TRANVIA", "CAMIONETA", "CAMION", "TRACTOR", "FERROCARRI",
    "MOTOCICLET", "BICICLETA", "OTROVEHIC", "CONDMUERTO", "CONDHERIDO",
    "PASAMUERTO", "PASAHERIDO", "PEATMUERTO", "PEATHERIDO",
    "CICLMUERTO", "CICLHERIDO", "OTROMUERTO", "OTROHERIDO",
    "NEMUERTO", "NEHERIDO"
]

def main():
    if not INPUT.exists():
        raise FileNotFoundError(
            f"No se encontró {INPUT}. Extrae el ZIP de INEGI y copia "
            "conjunto_de_datos/atus_anual_2025.csv a data/raw/atus_anual_2025.csv."
        )

    # Se leen inicialmente como texto para preservar códigos y ceros a la izquierda.
    df = pd.read_csv(INPUT, dtype=str, encoding="utf-8-sig", low_memory=False)
    rows_originales = len(df)
    columnas_originales = len(df.columns)

    # Limpieza básica de espacios y cadenas vacías.
    for col in df.columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
        df[col] = df[col].replace("", pd.NA)

    # Eliminar registros idénticos, documentando cuántos se retiraron.
    duplicados = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Conversión explícita de variables cuantitativas; códigos categóricos se conservan.
    for col in NUMERIC_FIELDS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # Validación de consistencia temporal para esta entrega.
    anios_inesperados = 0
    if "ANIO" in df.columns:
        anios_inesperados = int((df["ANIO"].notna() & (df["ANIO"] != 2025)).sum())

    # Indicador de calidad: faltantes por columna (no se eliminan filas solo por tener nulos).
    nulos = df.isna().sum().sort_values(ascending=False)
    reporte = {
        "archivo_fuente": INPUT.name,
        "filas_originales": rows_originales,
        "columnas_originales": columnas_originales,
        "filas_despues_de_duplicados": len(df),
        "duplicados_eliminados": duplicados,
        "registros_con_anio_distinto_de_2025": anios_inesperados,
        "nulos_por_columna": {str(k): int(v) for k, v in nulos.items()},
    }

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    # JSON Lines: un documento JSON por registro, formato conveniente para MongoDB.
    with OUTPUT_JSONL.open("w", encoding="utf-8") as f:
        for record in df.astype(object).where(pd.notna(df), None).to_dict(orient="records"):
            f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

    report_path = ROOT / "data" / "processed" / "reporte_calidad.json"
    report_path.write_text(json.dumps(reporte, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=== RESUMEN DEL PROCESAMIENTO ===")
    print(f"Filas originales: {rows_originales:,}")
    print(f"Columnas: {columnas_originales}")
    print(f"Duplicados eliminados: {duplicados:,}")
    print(f"Filas preparadas: {len(df):,}")
    print(f"CSV: {OUTPUT_CSV}")
    print(f"JSONL: {OUTPUT_JSONL}")
    print(f"Reporte: {report_path}")


    # La carga a MongoDB se realiza por lotes.
    uri = os.getenv("MONGODB_URI")

    if uri:
        from pymongo import MongoClient
        from pymongo.errors import PyMongoError

        client = None

        try:
            client = MongoClient(
                uri,
                serverSelectionTimeoutMS=15000,
                connectTimeoutMS=20000,
                socketTimeoutMS=60000,
                retryWrites=True
            )

            client.admin.command("ping")

            db = client[os.getenv("MONGODB_DATABASE", "bdpcd_atus")]
            collection = db[
                os.getenv("MONGODB_COLLECTION", "accidentes_2025")
            ]

            # Convertir los datos preparados a documentos.
            documents = (
                df.astype(object)
                  .where(pd.notna(df), None)
                  .to_dict(orient="records")
            )

            total = len(documents)
            batch_size = 1000

            # IMPORTANTE: reinicia la colección destino antes de cargar.
            # Ejecuta esto solo si la colección es exclusiva del proyecto.
            collection.delete_many({})

            print(f"Iniciando carga de {total:,} documentos...")

            for start in range(0, total, batch_size):
                batch = documents[start:start + batch_size]
                collection.insert_many(batch, ordered=False)

                procesados = min(start + len(batch), total)
                print(f"Insertados: {procesados:,} de {total:,}")

            print("Carga completada correctamente.")
            print(f"Base de datos: {db.name}")
            print(f"Colección: {collection.name}")
            print(f"Documentos cargados: {collection.count_documents({}):,}")

        except PyMongoError as exc:
            print("Error durante la conexión o carga en MongoDB.")
            print(f"Detalle: {exc}")
            print(
                "Si la carga quedó incompleta, puedes volver a ejecutarla: "
                "el programa vacía la colección destino antes de comenzar."
            )

        finally:
            if client is not None:
                client.close()
    else:
        print("MONGODB_URI no está configurada; se omitió la carga.")


if __name__ == "__main__":
    main()
