# BDPCD — Análisis de accidentes de tránsito terrestre en México, ATUS 2025

## Descripción
Proyecto de análisis de los registros de Accidentes de Tránsito Terrestre (ATUS) 2025 del INEGI. Integra preparación de datos con Python, almacenamiento documental en MongoDB Atlas, consultas analíticas y un dashboard interactivo en Streamlit con visualización geográfica mediante cartografía GeoJSON del INEGI.

## Componentes
- `app.py`: dashboard interactivo Streamlit.
- `consultas_atus.py`: consultas analíticas sobre MongoDB.
- `scripts/pipeline_atus.py`: preparación, limpieza, validación y exportación de datos. **No ejecutar si no se desea volver a cargar la colección destino**.
- `scripts/descargar_geometrias_inegi.py`: descarga de geometrías GeoJSON a `data/geografia/`; no modifica MongoDB.
- `reconstruir_catalogos_inegi.py`: reconstrucción de catálogos de entidades y municipios. Sustituye esas colecciones; ejecutar únicamente si se autoriza.
- `diccionario_datos.md`: diccionario preliminar de variables.
- `modelo_nosql.md`: diseño del modelo documental.
- `INFORME_TERCERA_ENTREGA.md`: informe de resultados y análisis.
- `EVIDENCIAS.md`: relación de evidencias de la entrega.
- `resultados_consultas_atus.txt`: salida de consultas analíticas.

## Instalación
Requisitos: Python 3.11 o compatible y acceso a MongoDB Atlas.

En PowerShell, desde la raíz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configura la conexión como variable de entorno (no escribas credenciales en el código ni las subas a GitHub):

```powershell
$env:MONGODB_URI = Read-Host "Pega tu URI de MongoDB Atlas"
```

## Ejecutar el dashboard

```powershell
streamlit run app.py
```

Abre `http://localhost:8501` si el navegador no se inicia automáticamente.

El dashboard consulta las colecciones existentes:
- `bdpcd_atus.accidentes_2025`
- `catalogo_entidades`
- `catalogo_municipios`

Los mapas leen los GeoJSON locales ubicados en `data/geografia/`. Si esos archivos no están presentes, ejecuta:

```powershell
python scripts/descargar_geometrias_inegi.py
```

## Consultas
Con `MONGODB_URI` configurada:

```powershell
python consultas_atus.py
```

## Datos y carga
Los archivos originales y procesados de ATUS no se versionan en este repositorio por su tamaño. Coloca el CSV oficial en `data/raw/atus_anual_2025.csv` cuando necesites reconstruir el procesamiento.

**Precaución:** `scripts/pipeline_atus.py` puede limpiar la colección destino antes de insertar los registros. No lo ejecutes sobre una colección con información que debas conservar. En el estado documentado del proyecto, `accidentes_2025` ya contiene 379,643 documentos; no es necesario recargarla para utilizar el dashboard.

La reconstrucción de catálogos también reemplaza `catalogo_entidades` y `catalogo_municipios`. No la ejecutes si los catálogos actuales ya funcionan.

## Estructura general
```text
BDPCD_ATUS_2025/
├── app.py
├── consultas_atus.py
├── requirements.txt
├── README.md
├── EVIDENCIAS.md
├── INFORME_TERCERA_ENTREGA.md
├── diccionario_datos.md
├── modelo_nosql.md
├── resultados_consultas_atus.txt
├── data/
│   └── geografia/
│       ├── entidades.geojson
│       └── municipios_01.geojson ... municipios_32.geojson
└── scripts/
    ├── pipeline_atus.py
    └── descargar_geometrias_inegi.py
```

## Seguridad y control de versiones
- No subir `.venv/`, credenciales, archivos `.env`, CSV/ZIP originales ni archivos JSONL de gran tamaño.
- Mantener `MONGODB_URI` únicamente como variable de entorno.
- Los archivos GeoJSON se conservan porque el dashboard los necesita localmente.
- Los resultados reportados corresponden a la ejecución analítica documentada; las discrepancias de variables y las limitaciones se describen en el informe y el diccionario.

## Fuente
Instituto Nacional de Estadística y Geografía (INEGI), Accidentes de Tránsito Terrestre en Zonas Urbanas y Suburbanas (ATUS), año 2025.
