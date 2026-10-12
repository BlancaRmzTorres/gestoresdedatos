import csv
from pathlib import Path
from pymongo import MongoClient, ASCENDING

PROYECTO = Path(__file__).resolve().parent.parent

ARCHIVO = (
    PROYECTO
    / "datos"
    / "procesados"
    / "participantes_limpios.tsv"
)

URI = "mongodb://localhost:27017"
BASE_DATOS = "seizeit2"
COLECCION = "participantes"


def cargar_participantes():
    if not ARCHIVO.exists():
        print(f"No se encontró el archivo: {ARCHIVO}")
        return

    cliente = MongoClient(URI, serverSelectionTimeoutMS=5000)

    try:
        cliente.admin.command("ping")

        db = cliente[BASE_DATOS]
        participantes = db[COLECCION]

        participantes.create_index(
            [("participant_id", ASCENDING)],
            unique=True
        )

        nuevos = 0
        actualizados = 0
        revisados = 0

        with open(
            ARCHIVO,
            "r",
            encoding="utf-8",
            newline=""
        ) as archivo:
            lector = csv.DictReader(archivo, delimiter="\t")

            for fila in lector:
                participante = {
                    "participant_id": fila["participant_id"].strip(),
                    "sex": fila["sex"].strip().lower()
                }

                resultado = participantes.update_one(
                    {
                        "participant_id":
                            participante["participant_id"]
                    },
                    {"$set": participante},
                    upsert=True
                )

                revisados += 1

                if resultado.upserted_id is not None:
                    nuevos += 1
                elif resultado.modified_count > 0:
                    actualizados += 1

        print("Carga terminada.")
        print(f"Registros revisados: {revisados}")
        print(f"Participantes nuevos: {nuevos}")
        print(f"Participantes actualizados: {actualizados}")
        print(
            "Total en MongoDB:",
            participantes.count_documents({})
        )

    finally:
        cliente.close()


if __name__ == "__main__":
    cargar_participantes()