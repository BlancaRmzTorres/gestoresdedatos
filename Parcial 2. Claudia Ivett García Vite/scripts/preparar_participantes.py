import csv
from pathlib import Path
from collections import Counter

# Ubicación del proyecto y de los archivos
PROYECTO = Path(__file__).resolve().parent.parent

ARCHIVO_ORIGINAL = (
    PROYECTO / "datos" / "originales" / "participants.txt"
)

CARPETA_PROCESADOS = PROYECTO / "datos" / "procesados"

ARCHIVO_LIMPIO = CARPETA_PROCESADOS / "participantes_limpios.tsv"
ARCHIVO_INFORME = CARPETA_PROCESADOS / "informe_limpieza_participantes.txt"


def limpiar_participantes():
    CARPETA_PROCESADOS.mkdir(parents=True, exist_ok=True)

    if not ARCHIVO_ORIGINAL.exists():
        print(f"No se encontró el archivo: {ARCHIVO_ORIGINAL}")
        return

    validos = []
    incidencias = []
    identificadores_vistos = set()
    filas_leidas = 0

    with open(
        ARCHIVO_ORIGINAL,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:
        lector = csv.DictReader(archivo, delimiter="\t")

        columnas = lector.fieldnames or []

        if not {"participant_id", "sex"}.issubset(columnas):
            print(
                "Error: el archivo debe contener "
                "las columnas participant_id y sex."
            )
            return

        for numero_fila, fila in enumerate(lector, start=2):
            filas_leidas += 1

            participante = (fila.get("participant_id") or "").strip()
            sexo = (fila.get("sex") or "").strip().lower()

            errores = []

            if not participante:
                errores.append("Identificador vacío")
            elif not (
                participante.startswith("sub-")
                and participante[4:].isdigit()
            ):
                errores.append("Formato de identificador inválido")

            if sexo not in {"m", "f"}:
                errores.append("Valor de sexo no reconocido")

            if participante in identificadores_vistos:
                errores.append("Identificador duplicado")

            if errores:
                incidencias.append(
                    f"Fila {numero_fila}: "
                    f"{participante or '(sin ID)'} - "
                    f"{'; '.join(errores)}"
                )
                continue

            identificadores_vistos.add(participante)

            validos.append({
                "participant_id": participante,
                "sex": sexo
            })

    # Guardar los registros válidos en formato TSV
    with open(
        ARCHIVO_LIMPIO,
        "w",
        encoding="utf-8",
        newline=""
    ) as archivo:
        campos = ["participant_id", "sex"]
        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos,
            delimiter="\t"
        )
        escritor.writeheader()
        escritor.writerows(validos)

    # Crear informe de limpieza
    conteo_sexo = Counter(registro["sex"] for registro in validos)

    with open(ARCHIVO_INFORME, "w", encoding="utf-8") as archivo:
        archivo.write("INFORME DE LIMPIEZA DE PARTICIPANTES\n")
        archivo.write("=" * 40 + "\n")
        archivo.write(f"Filas revisadas: {filas_leidas}\n")
        archivo.write(f"Registros válidos: {len(validos)}\n")
        archivo.write(f"Registros con incidencias: {len(incidencias)}\n")
        archivo.write(f"Sexo m: {conteo_sexo.get('m', 0)}\n")
        archivo.write(f"Sexo f: {conteo_sexo.get('f', 0)}\n")
        archivo.write("\nDETALLE DE INCIDENCIAS\n")

        if incidencias:
            for incidencia in incidencias:
                archivo.write(incidencia + "\n")
        else:
            archivo.write("No se detectaron incidencias.\n")

    print("Preparación terminada.")
    print(f"Filas revisadas: {filas_leidas}")
    print(f"Registros válidos: {len(validos)}")
    print(f"Registros con incidencias: {len(incidencias)}")
    print(f"Archivo limpio: {ARCHIVO_LIMPIO}")
    print(f"Informe: {ARCHIVO_INFORME}")


if __name__ == "__main__":
    limpiar_participantes()