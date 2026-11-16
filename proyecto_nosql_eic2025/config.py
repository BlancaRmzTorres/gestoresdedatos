"""Configuración común del proyecto EIC 2025 -> MongoDB."""
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DATOS_DIR = BASE_DIR / "datos"
SALIDAS_DIR = BASE_DIR / "salidas"
SALIDAS_DIR.mkdir(exist_ok=True)

# Microdatos opcionales: el modo demo solo requiere el JSON incluido.
ARCHIVO_PREDETERMINADO = DATOS_DIR / "personas00.csv"

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

# Puerto configurable: debe coincidir con MONGO_PORT usado por Docker Compose.
MONGO_PORT = os.environ.get("MONGO_PORT", "27018")
MONGO_URI = os.environ.get("MONGO_URI", f"mongodb://127.0.0.1:{MONGO_PORT}/")
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
