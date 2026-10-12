
import json
from pathlib import Path

# Ruta principal del proyecto
PROYECTO = Path(__file__).resolve().parent.parent
CARPETA_DATOS = PROYECTO / "datos" / "originales"

archivos_json = [
    "dataset_description.json",
    "events.json",
    "participants.json"
]

print("REVISIÓN DE METADATOS DE SEIZEIT2")
print("=" * 40)

for nombre in archivos_json:
    ruta = CARPETA_DATOS / nombre

    print(f"\nArchivo: {nombre}")

    if not ruta.exists():
        print("No se encontró el archivo. Revisa su nombre y ubicación.")
        continue

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

        print("Lectura correcta.")

        if isinstance(contenido, dict):
            print("Campos principales:")

            for campo, valor in contenido.items():
                if isinstance(valor, dict):
                    detalle = f"objeto con {len(valor)} campos"
                elif isinstance(valor, list):
                    detalle = f"lista con {len(valor)} elementos"
                else:
                    detalle = repr(valor)
                    if len(detalle) > 120:
                        detalle = detalle[:117] + "..."

                print(f"  - {campo}: {detalle}")

        else:
            print("Tipo de contenido:", type(contenido).__name__)

    except (json.JSONDecodeError, OSError) as error:
        print("No se pudo leer el archivo:", error)

print("\nRevisión terminada.")
