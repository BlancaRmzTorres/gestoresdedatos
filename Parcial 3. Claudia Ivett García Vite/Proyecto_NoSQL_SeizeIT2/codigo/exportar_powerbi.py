from pathlib import Path
import pandas as pd
from pymongo import MongoClient

# 1. Conexión a MongoDB
cliente = MongoClient("mongodb://localhost:27017")
db = cliente["SeizeIT2_NoSQL"]

# 2. Consultar participantes
datos = list(
    db.participantes.find({}, {"_id": 0})
)

# 3. Convertir a DataFrame
df = pd.DataFrame(datos)

# 4. Definir carpeta de salida
carpeta = Path(__file__).resolve().parent.parent / "powerbi"
carpeta.mkdir(parents=True, exist_ok=True)

# 5. Exportar a CSV
archivo = carpeta / "participantes.csv"
df.to_csv(archivo, index=False, encoding="utf-8-sig")

print(f"Participantes exportados: {len(df)}")
print(f"Archivo generado: {archivo}")

# 6. Consultar eventos de crisis epilépticas
eventos = list(
    db.eventos.find(
        {"eventType": {"$regex": "^sz_"}},
        {"_id": 0}
    )
)

# 7. Convertir a DataFrame
df_crisis = pd.DataFrame(eventos)

# 8. Exportar crisis a CSV
archivo_crisis = carpeta / "crisis.csv"

df_crisis.to_csv(
    archivo_crisis,
    index=False,
    encoding="utf-8-sig"
)

print(f"Crisis exportadas: {len(df_crisis)}")
print(f"Archivo generado: {archivo_crisis}")

# 9. Consultar las grabaciones almacenadas en MongoDB
grabaciones = list(
    db.grabaciones.find(
        {},
        {"_id": 0}
    )
)

# 10. Convertir las grabaciones a DataFrame
df_grabaciones = pd.DataFrame(grabaciones)

# 11. Exportar las grabaciones a CSV
archivo_grabaciones = carpeta / "grabaciones.csv"

df_grabaciones.to_csv(
    archivo_grabaciones,
    index=False,
    encoding="utf-8-sig"
)

print(f"Grabaciones exportadas: {len(df_grabaciones)}")
print(f"Archivo generado: {archivo_grabaciones}")

# 12. Recuperar las crisis con inicio y duración válidos
pipeline_crisis = [
    {
        "$match": {
            "eventType": {"$regex": "^sz_"},
            "onset": {"$type": "number"},
            "duration": {"$type": "number"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "participant_id": 1,
            "session": 1,
            "run": 1,
            "onset": 1,
            "duration": 1
        }
    },
    {
        "$sort": {
            "participant_id": 1,
            "session": 1,
            "run": 1,
            "onset": 1
        }
    }
]

df_ventanas = pd.DataFrame(
    list(db["eventos"].aggregate(pipeline_crisis))
)

# 13. Calcular el final de cada crisis
columnas_grupo = ["participant_id", "session", "run"]

df_ventanas["fin_crisis"] = (
    df_ventanas["onset"] + df_ventanas["duration"]
)

# 14. Identificar el final más tardío de las crisis anteriores
df_ventanas["fin_previo"] = (
    df_ventanas.groupby(columnas_grupo)["fin_crisis"]
    .transform(lambda x: x.cummax().shift(1))
)

df_ventanas["inicio_libre"] = (
    df_ventanas["fin_previo"].fillna(0)
)

df_ventanas["tiempo_libre_previo"] = (
    df_ventanas["onset"] - df_ventanas["inicio_libre"]
)

# 15. Identificar ventanas disponibles
df_ventanas["ventana_5_min"] = (
    df_ventanas["tiempo_libre_previo"] >= 300
).astype(int)

df_ventanas["ventana_10_min"] = (
    df_ventanas["tiempo_libre_previo"] >= 600
).astype(int)

df_ventanas["ventana_30_min"] = (
    df_ventanas["tiempo_libre_previo"] >= 1800
).astype(int)

# 16. Exportar resultados
archivo_ventanas = carpeta / "ventanas_preictales.csv"

df_ventanas.to_csv(
    archivo_ventanas,
    index=False,
    encoding="utf-8-sig"
)

print(f"Crisis analizadas para ventanas: {len(df_ventanas)}")
print(f"Ventanas de 5 minutos: {df_ventanas['ventana_5_min'].sum()}")
print(f"Ventanas de 10 minutos: {df_ventanas['ventana_10_min'].sum()}")
print(f"Ventanas de 30 minutos: {df_ventanas['ventana_30_min'].sum()}")
print(f"Archivo generado: {archivo_ventanas}")

# 17. Identificar segmentos con al menos una crisis
# y consultar sus modalidades disponibles

pipeline_modalidades = [
    {
        "$match": {
            "eventType": {"$regex": "^sz_"}
        }
    },
    {
        "$group": {
            "_id": {
                "participant_id": "$participant_id",
                "session": "$session",
                "run": "$run"
            }
        }
    },
    {
        "$lookup": {
            "from": "grabaciones",
            "let": {
                "pid": "$_id.participant_id",
                "ses": "$_id.session",
                "run": "$_id.run"
            },
            "pipeline": [
                {
                    "$match": {
                        "$expr": {
                            "$and": [
                                {"$eq": ["$participant_id", "$$pid"]},
                                {"$eq": ["$session", "$$ses"]},
                                {"$eq": ["$run", "$$run"]}
                            ]
                        }
                    }
                }
            ],
            "as": "grabaciones"
        }
    },
    {
        "$project": {
            "_id": 0,
            "participant_id": "$_id.participant_id",
            "session": "$_id.session",
            "run": "$_id.run",
            "modalidades": "$grabaciones.modality"
        }
    }
]

datos_modalidades = list(
    db["eventos"].aggregate(pipeline_modalidades)
)

df_modalidades = pd.DataFrame(datos_modalidades)

# 18. Crear indicadores por modalidad
for modalidad in ["eeg", "ecg", "emg", "mov"]:
    df_modalidades[modalidad.upper()] = (
        df_modalidades["modalidades"]
        .apply(lambda valores: int(modalidad in valores))
    )

# 19. Identificar segmentos con las cuatro modalidades
df_modalidades["cuatro_modalidades"] = (
    (
        df_modalidades[["EEG", "ECG", "EMG", "MOV"]]
        .sum(axis=1)
    ) == 4
).map({True: "Sí", False: "No"})

# 20. Eliminar la columna de listas para facilitar la importación
df_modalidades = df_modalidades.drop(columns=["modalidades"])

# 21. Exportar a CSV
archivo_modalidades = carpeta / "modalidades_por_segmento.csv"

df_modalidades.to_csv(
    archivo_modalidades,
    index=False,
    encoding="utf-8-sig"
)

# 22. Verificar resultados
print(f"Segmentos con crisis: {len(df_modalidades)}")

print(
    "Segmentos con cuatro modalidades:",
    (df_modalidades["cuatro_modalidades"] == "Sí").sum()
)

print(
    "Segmentos sin cuatro modalidades:",
    (df_modalidades["cuatro_modalidades"] == "No").sum()
)

for modalidad in ["EEG", "ECG", "EMG", "MOV"]:
    print(
        f"Segmentos con {modalidad}:",
        df_modalidades[modalidad].sum()
    )

print(f"Archivo generado: {archivo_modalidades}")

cliente.close()