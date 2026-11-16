# Proyecto NoSQL: SeizeIT2

## 1. Descripción

Proyecto desarrollado para la materia **Bases de Datos para Ciencia de Datos**, de la Maestría en Ciencia de Datos.

Se utiliza el conjunto de datos **SeizeIT2**, que contiene registros fisiológicos y anotaciones de eventos de personas con epilepsia focal.

El objetivo es organizar los metadatos y las anotaciones de eventos en una base de datos NoSQL utilizando MongoDB, explorar la información disponible y generar visualizaciones sobre las crisis epilépticas.

## 2. Fuente de datos

**Conjunto de datos:** SeizeIT2: Wearable Dataset of Patients with Focal Epilepsy.

**Repositorio:** [OpenNeuro – SeizeIT2](https://doi.org/10.18112/openneuro.ds005873.v1.1.0)

El conjunto de datos utiliza una estructura BIDS e incluye archivos TSV, JSON y EDF.

Los archivos originales no se incluyen en este repositorio debido a su tamaño. Para reproducir la carga completa es necesario descargarlos desde OpenNeuro.

## 3. Estructura del proyecto

```text
Proyecto_NoSQL_SeizeIT2/
├── codigo/
│   ├── main.py
│   ├── explorar_eventos.py
│   └── exportar_powerbi.py
├── documentos/
├── powerbi/
│   ├── participantes.csv
│   ├── grabaciones.csv
│   ├── crisis.csv
│   ├── ventanas_preictales.csv
│   ├── modalidades_por_segmento.csv
│   └── Visualización_proyecto_tesina.pbix
├── resultados/
│   └── eventos_originales.csv
├── Proyecto_NoSQL_SeizeIT2.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Requisitos

- Python 3.13
- MongoDB Community Server instalado y en ejecución
- Visual Studio Code (recomendado)
- Extensiones Python y Jupyter de VS Code
- Power BI Desktop para abrir el dashboard interactivo

## 5. Instalación y configuración

### 5.1. Descargar el proyecto

Descargar o clonar el repositorio de GitHub y abrir la carpeta principal en Visual Studio Code.

### 5.2. Crear el entorno virtual

Desde PowerShell:

```powershell
python -m venv .venv
```

Activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5.3. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5.4. Descargar los datos originales

Descargar el conjunto de datos SeizeIT2 desde OpenNeuro.

Conservar su estructura original de participantes, sesiones y archivos.

### 5.5. Configurar la ubicación de los datos

Si los datos están fuera del proyecto, establecer la variable de entorno:

```powershell
$env:SEIZEIT2_DATA_DIR = "C:\ruta\a\SeizeIT2"
```

Sustituir la ruta del ejemplo por la ubicación real del conjunto de datos.

Alternativamente, colocar los archivos originales en una carpeta llamada `datos` dentro del proyecto.

### 5.6. Iniciar MongoDB

Verificar que MongoDB Community Server esté instalado y en ejecución.

El proyecto utiliza la conexión:

```text
mongodb://localhost:27017
```

La base de datos se denomina `SeizeIT2_NoSQL`.

## 6. Ejecución del proyecto

Los siguientes comandos se ejecutan desde la carpeta principal del proyecto.

### 6.1. Explorar los archivos originales

```powershell
python .\codigo\explorar_eventos.py
```

Este script identifica los archivos de eventos, explora las variables y sus valores, revisa posibles datos faltantes y genera:

`resultados/eventos_originales.csv`

### 6.2. Cargar los datos en MongoDB

```powershell
python .\codigo\main.py
```

El programa prepara y carga tres colecciones:

- `participantes`
- `grabaciones`
- `eventos`

Al finalizar, valida las relaciones entre participantes, grabaciones y eventos.

### 6.3. Exportar los datos para Power BI

```powershell
python .\codigo\exportar_powerbi.py
```

Este programa consulta MongoDB y genera cinco archivos CSV en la carpeta `powerbi`:

- `participantes.csv`
- `grabaciones.csv`
- `crisis.csv`
- `ventanas_preictales.csv`
- `modalidades_por_segmento.csv`

## 7. Resultados obtenidos

Los siguientes resultados corresponden a los datos procesados durante el desarrollo del proyecto.

| Indicador | Resultado |
|---|---:|
| Participantes | 43 |
| Grabaciones | 6,710 |
| Eventos registrados | 1,888 |
| Crisis epilépticas identificadas | 262 |
| Segmentos con crisis | 153 |
| Ventanas disponibles de 5 minutos | 233 |
| Ventanas disponibles de 10 minutos | 205 |
| Ventanas disponibles de 30 minutos | 133 |

### Validación de MongoDB

La ejecución verificada produjo los siguientes resultados:

| Validación | Resultado |
|---|---:|
| Eventos sin participante | 0 |
| Eventos sin grabación | 0 |
| Archivos JSON sin EDF correspondiente | 0 |

Las cantidades pueden variar si se utiliza una versión o selección diferente del conjunto de datos.

## 8. Visualización en Power BI

El proyecto incluye el archivo:

`powerbi/Visualización_proyecto_tesina.pbix`

El dashboard presenta un análisis exploratorio de las crisis epilépticas registradas en SeizeIT2.

Incluye indicadores y visualizaciones sobre:

- Participantes y crisis registradas.
- Distribución de crisis por participante.
- Tipos de crisis epilépticas.
- Duración de las crisis.
- Disponibilidad de ventanas previas de 5, 10 y 30 minutos.

También permite filtrar la información por participante.

### Cómo abrir el dashboard

1. Instalar Power BI Desktop.
2. Abrir el archivo `.pbix` incluido en la carpeta `powerbi`.
3. Utilizar los filtros y visualizaciones disponibles.

Los archivos CSV utilizados para construir el dashboard también están incluidos en el repositorio.

**Nota:** Si se actualizan las fuentes de datos en Power BI desde otra computadora, puede ser necesario configurar nuevamente las rutas de los CSV.

## 9. Notebook del proyecto

El archivo `Proyecto_NoSQL_SeizeIT2.ipynb` contiene documentación y consultas de validación del trabajo realizado.

Para ejecutarlo:

1. Abrir el notebook en Visual Studio Code.
2. Seleccionar el intérprete del entorno virtual `.venv`.
3. Verificar que MongoDB esté en ejecución y que los datos estén cargados.
4. Ejecutar las celdas en orden.

## 10. Alcance y limitaciones

El proyecto se centra en la organización, exploración y visualización de metadatos y anotaciones de eventos.

Las muestras de las señales fisiológicas contenidas en los archivos EDF no se incorporan a MongoDB en esta etapa.

Las ventanas preictales representan disponibilidad temporal de información previa a las crisis; no constituyen por sí mismas una predicción ni un análisis de patrones fisiológicos.

Los archivos CSV permiten consultar los resultados exploratorios sin necesidad de descargar el conjunto de datos original. Para reconstruir las colecciones de MongoDB desde cero, sí se requiere disponer de los archivos originales de SeizeIT2.

## 11. Referencia

SeizeIT2: Wearable Dataset of Patients with Focal Epilepsy. OpenNeuro.

https://doi.org/10.18112/openneuro.ds005873.v1.1.0
