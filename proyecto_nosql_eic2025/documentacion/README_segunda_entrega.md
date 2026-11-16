# EIC 2025 — Proyecto NoSQL con MongoDB

Proyecto reproducible de procesamiento de microdatos de la **Encuesta Intercensal 2025 (INEGI)**, indicadores por **entidad federativa × tamaño de localidad** y consultas en MongoDB.

**Incluye un JSON verificado con 153 documentos** para demostrar MongoDB **sin descargar ni procesar el CSV original de 5.76 GB**. El procesamiento integral está disponible para quien tenga `personas00.csv`.

## Requisitos

- **Windows 10/11** con PowerShell, **Python 3.11–3.14** y **Docker Desktop abierto**. Instalar paquetes requiere conexión a Internet la primera vez. Docker necesita descargar la imagen `mongo:8.0` si aún no está disponible.
- Al menos espacio libre para Docker, dependencias y datos. El **modo completo** requiere varios GB adicionales (el CSV original pesa ~5.76 GB y crea un CSV intermedio grande); utiliza SQLite temporalmente para detectar IDs duplicados con memoria limitada.
- macOS/Linux: Python 3.11–3.14, entorno virtual y Docker Engine/Desktop con Compose, con comandos indicados más abajo.

## Inicio rápido: demostración (recomendado para evaluación)

En **PowerShell**, desde la carpeta del proyecto, ejecutar:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar.ps1 -Modo demo
```

Este comando, sin necesidad del archivo original, crea `.venv` si no existe, instala bibliotecas, busca Docker incluso cuando no está en `PATH`, inicia MongoDB y carga/consulta los 153 documentos incluidos. **No repite las etapas costosas 1 a 4.** La colección utiliza `upsert`, por lo que repetir la ejecución no duplica los documentos.

Para **validar únicamente el JSON** sin Docker:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar.ps1 -Modo validar
```

## Procesamiento completo con el CSV oficial

Colocar los microdatos en `datos/personas00.csv` (no vienen en GitHub) y ejecutar:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar.ps1 -Modo completo
```

O indicar una ruta real, entre comillas si tiene espacios:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar.ps1 -Modo completo -Archivo "D:\Microdatos\personas00.csv"
```

**No usar** `C:\ruta\personas00.csv` literalmente: es solo un ejemplo de ruta. Al terminar, `iniciar.py` valida los documentos, inicia MongoDB y ejecuta las consultas. El procesamiento de millones de registros puede tardar y ocupar espacio considerable.

## Inicio manual (Windows)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe verificar_documentos.py
.\.venv\Scripts\python.exe iniciar.py --modo demo
```

Para el procesamiento original: `python ejecutar_pipeline.py --archivo datos/personas00.csv`, tras activar el entorno o usando su ejecutable; después ejecutar `python iniciar.py --modo demo` para cargar el JSON.

## macOS/Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python iniciar.py --modo demo
```

Para procesamiento completo: `.venv/bin/python iniciar.py --modo completo --archivo datos/personas00.csv`.

## Estructura y secuencia

| Archivo | Función |
| --- | --- |
| `01_diagnostico.py` | Diagnóstico de nulos y duplicados de `ID_PERSONA` (SQLite temporal por defecto). |
| `02_preparar_microdatos.py` | Limpieza y selección de mujeres de 15 a 49 años. |
| `03_construir_indicadores.py` | Indicadores ponderados por entidad y tamaño de localidad. |
| `04_generar_documentos_json.py` | Convierte indicadores CSV a documentos JSON. |
| `05_cargar_mongodb.py` | Carga idempotente mediante upsert; índices. |
| `06_consultas_mongodb.py` | Consultas de comprobación. |
| `ejecutar_pipeline.py` | Orquesta etapas 1–4 y acepta `--archivo`. |
| `verificar_documentos.py` | Validación previa a MongoDB. |
| `iniciar.py` / `iniciar.ps1` | Orquestación para nuevos equipos. |
| `config.py` | Variables, rutas relativas y parámetros de conexión. |
| `docker-compose.yml` | Contenedor MongoDB 8, datos persistentes. |

**Base**: `eic2025_nosql` • **Colección**: `indicadores_territoriales` • **URL**: `mongodb://127.0.0.1:27017/`.

`salidas/indicadores_territoriales.json` se incluye para que la demostración funcione sin microdatos. `salidas/indicadores_territoriales.csv` es la tabla de salida correspondiente. En cambio, `salidas/mujeres_15_49.csv`, los CSV originales, `.venv` y archivos temporales se omiten de GitHub.

## Comprobación y solución de problemas

| Mensaje | Acción |
| --- | --- |
| `No se encontro el CSV` | Copiar el archivo real a `datos/` o utilizar `-Modo demo`. |
| `docker no se reconoce` | `iniciar.py` busca `docker.exe` en directorios usuales, o abrir nueva terminal e incluir Docker en PATH. |
| `Cannot connect to Docker daemon` | Abrir Docker Desktop y verificar que el motor esté iniciado. |
| `port is already allocated` | Cerrar otro MongoDB local o cambiar `MONGO_PORT` tanto para Compose como para Python. |
| `El JSON no es valido` | No editar JSON manualmente; ejecutar etapa 4 con salidas correctas. |
| `No module named pandas/pymongo` | Instalar `requirements.txt` en el entorno virtual correcto. |
| `No space left on device` | Liberar espacio en disco o usar el modo demostración. |

El puerto puede cambiarse en PowerShell **antes** de ejecutar el proyecto: `$env:MONGO_PORT = "27018"`. Docker Compose usa esa variable y Python construye la URL correspondiente. El contenedor usa un nombre fijo; debe evitarse ejecutar dos copias del proyecto simultáneamente en el mismo Docker Desktop.

### Probar código sin MongoDB

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Resultados y alcance

La ejecución reportada por el autor con el CSV completo registró 25,222,336 personas, 6,652,318 mujeres de 15 a 49 años y 153 dominios territoriales. Estos datos son **resultados de la ejecución original**, no resultados de una nueva corrida con microdatos en este paquete. Hay 7 combinaciones sin documento entre las 160 teóricas; no se completan artificialmente con ceros.

**Nota metodológica:** el promedio de hijos nacidos vivos **no** es la tasa global de fecundidad (TGF). Los indicadores describen dominios, no prueban causalidad.

**Importante:** esta aplicación es una **demostración local**. El MongoDB no tiene autenticación de usuarios y expone el puerto solo en `127.0.0.1`. No debe publicarse sin configurar autenticación, secretos y controles de acceso.
