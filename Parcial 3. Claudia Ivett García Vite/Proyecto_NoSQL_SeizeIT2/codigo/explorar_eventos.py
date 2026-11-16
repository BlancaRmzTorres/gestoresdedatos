from pathlib import Path
import os
import csv
from collections import Counter

PROYECTO = Path(__file__).resolve().parent.parent

RUTA_DATOS = Path(
    os.environ.get(
        "SEIZEIT2_DATA_DIR",
        str(PROYECTO / "datos")
    )
)

archivos = list(RUTA_DATOS.rglob("*_events.tsv"))

print("Total de archivos de eventos:", len(archivos))

columnas = set()
valores_por_columna = {}
total_registros = 0

for ruta in archivos:

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:

        lector = csv.DictReader(archivo, delimiter="\t")

        for fila in lector:

            total_registros += 1

            for columna, valor in fila.items():

                columnas.add(columna)

                if columna not in valores_por_columna:
                    valores_por_columna[columna] = Counter()

                valores_por_columna[columna][valor] += 1

print("\nTotal de registros:", total_registros)

print("\nCOLUMNAS Y VALORES ENCONTRADOS")

for columna in sorted(columnas):

    conteo = valores_por_columna[columna]

    print(f"\nColumna: {columna}")
    print(f"Valores diferentes: {len(conteo)}")

    print("Valores más frecuentes:")

    for valor, cantidad in conteo.most_common(10):
        print(f"  {repr(valor)}: {cantidad}")

    faltantes = sum(
        cantidad
        for valor, cantidad in conteo.items()
        if valor is None
        or valor.strip().lower() in ["", "n/a", "na", "null"]
    )

    print(f"Posibles valores faltantes: {faltantes}")

print("\nVALORES FALTANTES POR TIPO DE EVENTO")

resumen = {}

for ruta in archivos:

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:

        lector = csv.DictReader(archivo, delimiter="\t")

        for fila in lector:

            tipo = fila["eventType"]

            if tipo not in resumen:
                resumen[tipo] = {
                    "total": 0,
                    "lateralization_na": 0,
                    "localization_na": 0,
                    "vigilance_na": 0
                }

            resumen[tipo]["total"] += 1

            for campo in [
                "lateralization",
                "localization",
                "vigilance"
            ]:
                if fila[campo].strip().lower() == "n/a":
                    resumen[tipo][f"{campo}_na"] += 1

for tipo, datos in sorted(resumen.items()):
    print(f"\n{tipo}: {datos}")

print("\n========== PRIMEROS 15 REGISTROS ==========\n")

registros_mostrados = 0

for ruta in archivos:

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:

        lector = csv.DictReader(archivo, delimiter="\t")

        for fila in lector:

            print(f"\nArchivo: {ruta.name}")

            for columna, valor in fila.items():
                print(f"  {columna}: {valor}")

            registros_mostrados += 1

            if registros_mostrados >= 15:
                break

    if registros_mostrados >= 15:
        break
import csv

ARCHIVO_SALIDA = (
    Path(__file__).resolve().parent.parent
    / "resultados"
    / "eventos_originales.csv"
)

ARCHIVO_SALIDA.parent.mkdir(parents=True, exist_ok=True)

with open(
    ARCHIVO_SALIDA,
    "w",
    encoding="utf-8-sig",
    newline=""
) as salida:

    escritor = None

    for ruta in sorted(archivos):

        with open(
            ruta,
            encoding="utf-8-sig",
            newline=""
        ) as entrada:

            lector = csv.DictReader(entrada, delimiter="\t")

            if escritor is None:
                columnas = [
                    "archivo_origen",
                    *lector.fieldnames
                ]

                escritor = csv.DictWriter(
                    salida,
                    fieldnames=columnas
                )

                escritor.writeheader()

            for fila in lector:
                escritor.writerow({
                    "archivo_origen": ruta.name,
                    **fila
                })

print(f"\nTabla original generada: {ARCHIVO_SALIDA}")

from collections import defaultdict

resumen_pacientes = defaultdict(lambda: {
    "grabaciones_con_crisis": set(),
    "crisis": 0
})

for ruta in archivos:

    participante = next(
        parte for parte in ruta.parts
        if parte.startswith("sub-")
    )

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:

        lector = csv.DictReader(archivo, delimiter="\t")

        for fila in lector:

            if fila["eventType"].startswith("sz_"):

                resumen_pacientes[participante]["crisis"] += 1
                resumen_pacientes[participante][
                    "grabaciones_con_crisis"
                ].add(ruta.name)

print("\nCRISIS REGISTRADAS POR PARTICIPANTE")

for participante in sorted(
    carpeta.name
    for carpeta in RUTA_DATOS.glob("sub-*")
    if carpeta.is_dir()
):
    datos = resumen_pacientes[participante]

    print(
        f"{participante} | "
        f"Crisis: {datos['crisis']} | "
        f"Runs con crisis: {len(datos['grabaciones_con_crisis'])}"
    )

print(
    "\nParticipantes con crisis registradas:",
    sum(
        datos["crisis"] > 0
        for datos in resumen_pacientes.values()
    )
)