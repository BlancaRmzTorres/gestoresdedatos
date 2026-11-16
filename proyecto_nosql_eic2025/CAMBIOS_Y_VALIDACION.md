# Registro de ajustes de portabilidad

- Se corrigió el nombre predeterminado del CSV: `datos/personas00.csv`.
- El ZIP original no contenía `requirements.txt`; se creó con versiones compatibles con Python 3.11 a 3.14.
- Se retiraron `.venv` (miles de archivos dependientes de Windows) y `mujeres_15_49.csv` (~714 MB sin comprimir); se conservó el JSON pequeño de 153 documentos para la demo.
- Se creó `iniciar.ps1` para preparar el entorno en Windows y `iniciar.py` para ejecutar validación, Docker Compose, carga y consultas desde la raíz del proyecto.
- El programa detecta Docker aunque no esté en `PATH`, como ocurrió en el equipo original.
- Se mejoró el diagnóstico de ruta/columnas de CSV antes de iniciar el procesamiento intensivo.
- Detección exacta de IDs repetidos ahora puede hacerse con SQLite temporal en disco (por defecto) o en RAM con `--modo-duplicados memoria` para priorizar velocidad.
- Carga `upsert` corregida para no incluir `_id` dentro de `$set`; contadores distinguen insertados/modificados/sin cambios y comparan IDs del JSON con MongoDB.
- Validador de JSON con controles de dominios, duplicados, subdocumentos y porcentajes.
- Consultas con ordenamiento determinista y comprobación de conexión.
- Puerto MongoDB configurable por `MONGO_PORT`, conexión por localhost y volumen de datos persistente.
- `.gitignore` protege microdatos, dependencias y salidas masivas, pero conserva el JSON necesario para el modo demo.
- Se agregaron pruebas sintéticas que no requieren microdatos oficiales ni MongoDB.

## Límites de la verificación

Se verificó el JSON original, se ejecutaron pruebas sobre CSV sintético de 17 columnas para el pipeline, y se validó la sintaxis de los módulos. La ejecución real de Docker y de PyMongo debe verificarse también en un equipo con Docker activo; la salida proporcionada por el autor demuestra que el contenedor original y las consultas funcionaban antes de los ajustes.
