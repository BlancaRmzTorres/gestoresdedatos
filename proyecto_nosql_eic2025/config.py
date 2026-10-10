"""Configuración común del proyecto EIC 2025 -> MongoDB."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATOS_DIR = BASE_DIR / "datos"
SALIDAS_DIR = BASE_DIR / "salidas"
SALIDAS_DIR.mkdir(exist_ok=True)

# Archivo de prueba incluido en el paquete. Para trabajar con la base completa,
# pasa --archivo "C:/ruta/personas00M.csv" al ejecutar los scripts.
ARCHIVO_PREDETERMINADO = DATOS_DIR / "personas00M_muestra.csv"

# Leer en bloques evita cargar el archivo completo en memoria.
CHUNKSIZE = 250_000

VARIABLES = [
    "ID_PERSONA",
    "ID_VIV",
    "CVE_ENT",
    "CVE_MUN",
    "TAMLOC",
    "FACTOR",
    "SEXO",
    "EDAD",
    "NIVACAD",
    "ESCOACUM",
    "CONACT",
    "SITUA_CONYUGAL",
    "PERTE_INDIGENA",
    "HLENGUA",
    "HIJOS_NAC_VIVOS",
    "FECHA_NAC_M",
    "FECHA_NAC_A",
]

# Variables que deben conservar ceros a la izquierda.
COLUMNAS_TEXTO = [
    "ID_PERSONA", "ID_VIV", "CVE_ENT", "CVE_MUN", "TAMLOC", "SEXO",
    "NIVACAD", "CONACT", "SITUA_CONYUGAL", "PERTE_INDIGENA", "HLENGUA",
    "FECHA_NAC_M", "FECHA_NAC_A",
]

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "eic2025_nosql"
COL_PERSONAS = "personas_procesadas"
COL_INDICADORES = "indicadores_territoriales"

TAMLOC_DESC = {
    "1": "Menos de 2 500 habitantes",
    "2": "De 2 500 a 14 999 habitantes",
    "3": "De 15 000 a 49 999 habitantes",
    "4": "De 50 000 a 99 999 habitantes",
    "5": "100 000 y más habitantes",
}
