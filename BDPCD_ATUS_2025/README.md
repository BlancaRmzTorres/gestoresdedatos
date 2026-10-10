# Segunda entrega — BDPCD: análisis de accidentes ATUS 2025

## Propósito
Preparar los datos oficiales de Accidentes de Tránsito Terrestre (ATUS) 2025 del INEGI, generar archivos limpios en CSV y JSON Lines y permitir una carga inicial opcional a MongoDB.

## Estructura
- `data/raw/`: archivo CSV original de ATUS 2025 (no incluido en este paquete).
- `data/processed/`: resultados generados por el programa.
- `scripts/pipeline_atus.py`: limpieza, validaciones, exportación y carga opcional.
- `diccionario_datos.md`: diccionario inicial de variables principales.
- `modelo_nosql.md`: propuesta de modelo documental.
- `requirements.txt`: dependencias de Python.

## Preparar el archivo
Extrae el ZIP oficial del INEGI y copia `conjunto_de_datos/atus_anual_2025.csv` en:
`data/raw/atus_anual_2025.csv`

## Ejecutar
Desde la carpeta raíz del proyecto:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python scripts/pipeline_atus.py
```

El programa genera:
- `data/processed/atus_2025_limpio.csv`
- `data/processed/atus_2025.jsonl`
- `data/processed/reporte_calidad.json`

## Carga en MongoDB (opcional)
Configura la variable de entorno `MONGODB_URI` con la cadena de conexión de tu instancia MongoDB. Opcionalmente, configura `MONGODB_DATABASE` y `MONGODB_COLLECTION`.

Windows PowerShell:
```powershell
$env:MONGODB_URI="mongodb+srv://USUARIO:CONTRASENA@CLUSTER/..."
python scripts/pipeline_atus.py
```

No publiques ni subas credenciales al repositorio. La carga actual limpia la colección destino antes de insertar; úsala solo en una colección de práctica dedicada.

## Criterios de limpieza aplicados
1. Recorta espacios en cadenas.
2. Convierte cadenas vacías a valores faltantes.
3. Elimina filas exactamente duplicadas.
4. Convierte variables cuantitativas seleccionadas a números enteros anulables.
5. Reporta valores faltantes por columna sin borrar automáticamente todos los registros que los contienen.
6. Reporta registros cuyo año no sea 2025.

## Limitaciones y decisiones
- La limpieza es preliminar: los códigos categóricos deben interpretarse con el diccionario oficial del INEGI antes de recodificarlos.
- Un valor nulo no se considera automáticamente un error; su tratamiento depende del significado de cada variable.
- El script no inventa valores faltantes ni elimina registros solo por tener campos vacíos.
- La colección es documental: cada documento representa un registro de accidente conforme a la estructura tabular de ATUS.
