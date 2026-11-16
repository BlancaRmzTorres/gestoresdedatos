"""
Proyecto NoSQL - SeizeIT2
Carga de participantes en MongoDB
"""

from pathlib import Path
from pymongo import MongoClient, UpdateOne
import csv
import json
import re

# =====================================================
# 1. CONFIGURACIÓN
# =====================================================

import os

PROYECTO = Path(__file__).resolve().parent.parent

RUTA_DATOS = Path(
    os.environ.get(
        "SEIZEIT2_DATA_DIR",
        str(PROYECTO / "datos")
    )
)
ARCHIVO_PARTICIPANTES = RUTA_DATOS / "participants.tsv"

MONGO_URI = "mongodb://localhost:27017"
NOMBRE_BASE_DATOS = "SeizeIT2_NoSQL"


# =====================================================
# 2. IDENTIFICAR PARTICIPANTES DISPONIBLES
# =====================================================

def obtener_participantes():

    if not RUTA_DATOS.exists():
        raise FileNotFoundError(f"No existe la carpeta: {RUTA_DATOS}")

    return sorted(
        carpeta.name
        for carpeta in RUTA_DATOS.glob("sub-*")
        if carpeta.is_dir()
    )


# =====================================================
# 3. LEER Y PREPARAR PARTICIPANTES
# =====================================================

def leer_participantes(participantes_disponibles):

    if not ARCHIVO_PARTICIPANTES.exists():
        raise FileNotFoundError(
            f"No se encontró: {ARCHIVO_PARTICIPANTES}"
        )

    registros = []

    with open(
        ARCHIVO_PARTICIPANTES,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:

        lector = csv.DictReader(archivo, delimiter="\t")

        for fila in lector:

            identificador = fila["participant_id"].strip()

            if identificador in participantes_disponibles:

                registros.append({
                    "participant_id": identificador,
                    "sex": fila["sex"].strip().lower()
                })

    return registros

# =====================================================
# 4. IDENTIFICAR Y PREPARAR LAS GRABACIONES
# =====================================================

def obtener_grabaciones(participantes):

    modalidades = ["eeg", "ecg", "emg", "mov"]
    registros = []
    archivos_sin_edf = 0

    for participante in participantes:

        carpeta_participante = RUTA_DATOS / participante

        sesiones = [
            carpeta for carpeta in carpeta_participante.glob("ses-*")
            if carpeta.is_dir()
        ]

        for sesion in sesiones:

            for modalidad in modalidades:

                carpeta_modalidad = sesion / modalidad

                if not carpeta_modalidad.exists():
                    continue

                archivos_json = carpeta_modalidad.glob(
                    f"*_{modalidad}.json"
                )

                for archivo_json in archivos_json:

                    archivo_edf = archivo_json.with_suffix(".edf")

                    if not archivo_edf.exists():
                        archivos_sin_edf += 1
                        continue

                    coincidencia = re.search(
                        r"(run-\d+)",
                        archivo_json.name
                    )

                    if not coincidencia:
                        continue

                    numero_run = coincidencia.group(1)

                    with open(
                        archivo_json,
                        "r",
                        encoding="utf-8"
                    ) as archivo:

                        metadatos = json.load(archivo)

                    prefijo = modalidad.upper()

                    registro = {
                        "participant_id": participante,
                        "session": sesion.name,
                        "run": numero_run,
                        "modality": modalidad,
                        "task": metadatos.get("TaskName"),
                        "sampling_frequency": metadatos.get(
                            "SamplingFrequency"
                        ),
                        "channel_count": metadatos.get(
                            f"{prefijo}ChannelCount"
                        ),
                        "montage": metadatos.get(
                            f"{prefijo}Montage"
                        ),
                        "placement": metadatos.get(
                            f"{prefijo}PlacementScheme"
                        ),
                        "recording_type": metadatos.get(
                            "RecordingType"
                        ),
                        "recording_duration": metadatos.get(
                            "RecordingDuration"
                        ),
                        "edf_path": archivo_edf.relative_to(
                            RUTA_DATOS
                        ).as_posix(),
                        "json_path": archivo_json.relative_to(
                            RUTA_DATOS
                        ).as_posix(),
                        "metadata": metadatos
                    }

                    registros.append(registro)

    print("\nPreparación de grabaciones:")
    print(f"Grabaciones preparadas: {len(registros)}")
    print(f"Archivos JSON sin EDF correspondiente: {archivos_sin_edf}")

    return registros

# =====================================================
# PREPARAR EVENTOS
# =====================================================

def obtener_eventos():

    registros = []

    for ruta in sorted(RUTA_DATOS.rglob("*_events.tsv")):

        participante = next(
            parte for parte in ruta.parts
            if parte.startswith("sub-")
        )

        sesion = next(
            parte for parte in ruta.parts
            if parte.startswith("ses-")
        )

        run = re.search(r"run-\d+", ruta.name).group()

        with open(
            ruta,
            encoding="utf-8-sig",
            newline=""
        ) as archivo:

            lector = csv.DictReader(archivo, delimiter="\t")

            for indice, fila in enumerate(lector):

                registro = {
                    "participant_id": participante,
                    "session": sesion,
                    "run": run,
                    "event_index": indice,
                    "source_file": ruta.relative_to(
                        RUTA_DATOS
                    ).as_posix()
                }

                for campo, valor in fila.items():

                    valor = valor.strip()

                    if valor.lower() in ("n/a", "na", ""):
                        registro[campo] = None

                    elif campo in (
                        "onset",
                        "duration",
                        "recordingDuration"
                    ):
                        registro[campo] = float(valor)

                    else:
                        registro[campo] = valor

                registros.append(registro)

    print(f"\nEventos preparados: {len(registros)}")

    return registros

# =====================================================
# 4. CONECTAR Y CARGAR EN MONGODB
# =====================================================

def cargar_participantes(registros):

    cliente = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000
    )

    try:
        cliente.admin.command("ping")

        base_datos = cliente[NOMBRE_BASE_DATOS]
        coleccion = base_datos["participantes"]

        print("\nBases de datos existentes:")
        print(cliente.list_database_names())

        print("\nColecciones existentes:")
        print(base_datos.list_collection_names())

        print("\nParticipantes almacenados:")
        print(coleccion.count_documents({}))


        operaciones = [
            UpdateOne(
                {"participant_id": registro["participant_id"]},
                {"$set": registro},
                upsert=True
            )
            for registro in registros
        ]

        if operaciones:
            resultado = coleccion.bulk_write(operaciones)

            print("\nCarga de participantes completada.")
            print(f"Registros encontrados: {len(registros)}")
            print(f"Documentos nuevos: {resultado.upserted_count}")
            print(f"Documentos modificados: {resultado.modified_count}")

        print(f"Total de documentos en la colección: {coleccion.count_documents({})}")

    finally:
        cliente.close()

# =====================================================
# 5. CARGAR GRABACIONES EN MONGODB
# =====================================================

def cargar_grabaciones(registros):

    cliente = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000
    )

    try:
        cliente.admin.command("ping")

        base_datos = cliente[NOMBRE_BASE_DATOS]
        coleccion = base_datos["grabaciones"]

        # Evitar grabaciones duplicadas
        coleccion.create_index(
            [
                ("participant_id", 1),
                ("session", 1),
                ("run", 1),
                ("modality", 1)
            ],
            unique=True
        )

        operaciones = [
            UpdateOne(
                {
                    "participant_id": registro["participant_id"],
                    "session": registro["session"],
                    "run": registro["run"],
                    "modality": registro["modality"]
                },
                {"$set": registro},
                upsert=True
            )
            for registro in registros
        ]

        if operaciones:
            resultado = coleccion.bulk_write(
                operaciones,
                ordered=False
            )

            print("\nCarga de grabaciones completada.")
            print(f"Registros preparados: {len(registros)}")
            print(f"Documentos nuevos: {resultado.upserted_count}")
            print(f"Documentos modificados: {resultado.modified_count}")

        print(
            "Total de grabaciones en MongoDB:",
            coleccion.count_documents({})
        )

    finally:
        cliente.close()

# =====================================================
# 7. CARGAR EVENTOS EN MONGODB
# =====================================================

def cargar_eventos(registros):

    cliente = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000
    )

    try:
        cliente.admin.command("ping")

        base_datos = cliente[NOMBRE_BASE_DATOS]
        coleccion = base_datos["eventos"]

        # Evitar eventos duplicados
        coleccion.create_index(
            [
                ("participant_id", 1),
                ("session", 1),
                ("run", 1),
                ("event_index", 1)
            ],
            unique=True
        )

        operaciones = [
            UpdateOne(
                {
                    "participant_id": registro["participant_id"],
                    "session": registro["session"],
                    "run": registro["run"],
                    "event_index": registro["event_index"]
                },
                {"$set": registro},
                upsert=True
            )
            for registro in registros
        ]

        if operaciones:
            resultado = coleccion.bulk_write(
                operaciones,
                ordered=False
            )

            print("\nCarga de eventos completada.")
            print(f"Registros preparados: {len(registros)}")
            print(f"Documentos nuevos: {resultado.upserted_count}")
            print(f"Documentos modificados: {resultado.modified_count}")

        print(
            "Total de eventos en MongoDB:",
            coleccion.count_documents({})
        )

    finally:
        cliente.close()

# =====================================================
# 8. VALIDAR RELACIONES ENTRE COLECCIONES
# =====================================================

def validar_relaciones():

    cliente = MongoClient(MONGO_URI)

    try:
        db = cliente[NOMBRE_BASE_DATOS]

        participantes = {
            doc["participant_id"]
            for doc in db["participantes"].find(
                {}, {"participant_id": 1}
            )
        }

        grabaciones = {
            (doc["participant_id"], doc["session"], doc["run"])
            for doc in db["grabaciones"].find(
                {}, {"participant_id": 1, "session": 1, "run": 1}
            )
        }

        sin_participante = 0
        sin_grabacion = 0

        for evento in db["eventos"].find(
            {},
            {"participant_id": 1, "session": 1, "run": 1}
        ):
            if evento["participant_id"] not in participantes:
                sin_participante += 1

            clave = (
                evento["participant_id"],
                evento["session"],
                evento["run"]
            )

            if clave not in grabaciones:
                sin_grabacion += 1

        print("\nVALIDACIÓN DE RELACIONES")
        print(f"Eventos sin participante: {sin_participante}")
        print(f"Eventos sin grabación: {sin_grabacion}")

    finally:
        cliente.close()

# =====================================================
# 6. PROGRAMA PRINCIPAL
# =====================================================

def main():

    participantes = obtener_participantes()
    registros = leer_participantes(participantes)

    print("=" * 50)
    print("PROYECTO NoSQL - SEIZEIT2")
    print("=" * 50)
    print(f"Participantes disponibles: {len(participantes)}")
    print(f"Participantes preparados: {len(registros)}")

    # Cargar participantes
    cargar_participantes(registros)

    # Preparar y cargar grabaciones
    grabaciones = obtener_grabaciones(participantes)
    cargar_grabaciones(grabaciones)
    # Preparar y cargar eventos
    eventos = obtener_eventos()
    cargar_eventos(eventos)

if __name__ == "__main__":
    main()
    validar_relaciones()