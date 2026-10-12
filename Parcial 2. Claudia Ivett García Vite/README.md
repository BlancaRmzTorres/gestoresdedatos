# Diseño y Preparación de Datos NoSQL: Del dato crudo a una base de datos lista para el análisis

## 1. Descripción del proyecto

Este proyecto tiene como finalidad organizar y preparar datos reales relacionados con el monitoreo fisiológico de personas con epilepsia mediante una base de datos NoSQL. Se utiliza el conjunto de datos **SeizeIT2**, disponible en la plataforma OpenNeuro, que contiene registros fisiológicos, metadatos y anotaciones de eventos obtenidos durante el monitoreo de personas con epilepsia focal.

El trabajo forma parte de la materia **Bases de Datos para Ciencia de Datos** y se enfoca en transformar los datos originales en información estructurada, validada y preparada para su almacenamiento y consulta.

La base de datos se desarrolla con MongoDB y se utilizan scripts en Python para revisar metadatos, validar registros, generar archivos limpios y realizar la carga inicial.

## 2. Objetivo

Diseñar y preparar una estructura de base de datos NoSQL para organizar los metadatos del conjunto de datos SeizeIT2, mediante la elaboración de un diccionario de datos, la definición de un modelo documental, la limpieza de los registros de participantes y su carga inicial en MongoDB.

## 3. Fuente de datos

- **Conjunto de datos:** SeizeIT2.
- **Repositorio:** OpenNeuro.
- **Identificador:** `ds005873`.
- **Versión:** `1.1.0`.
- **DOI:** `10.18112/openneuro.ds005873.v1.1.0`.
- **Licencia declarada:** CC0.
- **Enlace al conjunto de datos:** https://openneuro.org/datasets/ds005873
- **Artículo científico asociado:** https://www.nature.com/articles/s41597-025-05580-x

El conjunto contiene información de 125 participantes con epilepsia focal. Entre las modalidades fisiológicas documentadas se encuentran:

- **EEG:** actividad eléctrica cerebral.
- **ECG:** actividad eléctrica del corazón.
- **EMG:** actividad eléctrica muscular.
- **MOV:** información relacionada con el movimiento corporal.

Los archivos incluyen señales fisiológicas, metadatos en formato JSON y tablas de anotaciones en formato TSV. En este proyecto se trabaja inicialmente con los metadatos y la información de los participantes, sin procesar la totalidad de los archivos de señales.

## 4. Tecnologías utilizadas

- **Python:** lectura, validación y preparación de datos.
- **MongoDB Community Server:** almacenamiento de documentos.
- **PyMongo:** conexión y operaciones sobre MongoDB desde Python.
- **MongoDB Compass:** visualización y consulta de las colecciones.
- **Formato Markdown:** documentación del proyecto.

## 5. Estructura del proyecto

```text
Proyecto_NoSQL_Epilepsia/
├── README.md
├── datos/
│   ├── originales/
│   │   ├── dataset_description.json
│   │   ├── events.json
│   │   ├── participants.json
│   │   ├── participants.txt
│   │   └── README
│   └── procesados/
│       ├── participantes_limpios.tsv
│       └── informe_limpieza_participantes.txt
├── documentos/
│   ├── avance_proyecto_nosql.md
│   ├── diccionario_datos.md
│   └── modelo_nosql.md
└── scripts/
    ├── probar_conexion.py
    ├── revisar_metadatos.py
    ├── preparar_participantes.py
    └── cargar_participantes.py
```

## 6. Preparación y limpieza de los datos

La primera etapa se centra en el archivo `participants.txt`, que contiene los identificadores de los participantes y el campo `sex`.

El script `preparar_participantes.py` aplica las siguientes validaciones:

- Verifica el formato de los identificadores.
- Comprueba que el campo `sex` contenga uno de los valores esperados (`m` o `f`).
- Identifica campos vacíos.
- Revisa la existencia de identificadores duplicados.
- Genera un archivo limpio y un informe de resultados.

### Resultados obtenidos

| Indicador | Resultado |
|---|---:|
| Registros revisados | 125 |
| Registros válidos | 125 |
| Registros con incidencias | 0 |

Los resultados corresponden exclusivamente a las validaciones aplicadas al archivo de participantes.

## 7. Base de datos en MongoDB

La base de datos utilizada se llama `seizeit2` y la colección implementada hasta el momento es `participantes`.

La colección contiene 125 documentos. Se creó un índice único sobre `participant_id` para evitar duplicados y facilitar la identificación de cada participante.

### Estado de las colecciones

| Colección | Estado |
|---|---|
| `participantes` | Implementada y cargada con 125 registros. |
| `grabaciones` | Definida en el modelo; pendiente de implementación y carga. |
| `eventos` | Definida en el modelo; pendiente de implementación y carga. |

Las colecciones de grabaciones y eventos forman parte del diseño propuesto, pero todavía no se consideran implementadas.

## 8. Instalación y ejecución

### Requisitos previos

- Python instalado.
- MongoDB Community Server instalado y en ejecución.
- PyMongo instalado.

Para instalar PyMongo, abre una terminal y ejecuta:

```bash
python -m pip install pymongo
```

### Paso 1. Comprobar la conexión

Desde la carpeta principal del proyecto, ejecuta:

```bash
python scripts/probar_conexion.py
```

Este script comprueba la conexión con MongoDB.

### Paso 2. Preparar los participantes

Ejecuta:

```bash
python scripts/preparar_participantes.py
```

El proceso genera el archivo `participantes_limpios.tsv` y el informe de limpieza dentro de `datos/procesados/`.

### Paso 3. Cargar los participantes en MongoDB

Ejecuta:

```bash
python scripts/cargar_participantes.py
```

El script lee los registros preparados y los inserta o actualiza en la colección `participantes`, utilizando `participant_id` como identificador único.

**Importante:** Los comandos deben ejecutarse desde la carpeta principal `Proyecto_NoSQL_Epilepsia/`, donde se encuentra este archivo.

## 9. Documentación

La documentación complementaria se encuentra en la carpeta `documentos/`:

- [Reporte de avance del proyecto](documentos/avance_proyecto_nosql.md): describe la fuente de datos, el objetivo, el proceso de preparación, los resultados y las actividades pendientes.
- [Diccionario de datos](documentos/diccionario_datos.md): describe los campos, sus significados y las reglas de validación.
- [Modelo NoSQL](documentos/modelo_nosql.md): presenta la estructura documental propuesta, las colecciones y las relaciones entre ellas.

## 10. Actividades pendientes

Para continuar con el proyecto se contempla:

1. Implementar la colección `grabaciones` a partir de los metadatos reales.
2. Preparar y cargar las anotaciones de los archivos `events.tsv` en la colección `eventos`.
3. Establecer las relaciones entre participantes, grabaciones y eventos.
4. Definir y probar los índices de las nuevas colecciones.
5. Ejecutar consultas para comprobar la integridad y la recuperación de la información.
6. Actualizar la documentación con los resultados de las siguientes etapas.

## 11. Alcance del proyecto

El proyecto se enfoca en el diseño, la limpieza, la preparación y el almacenamiento de los datos. No contempla, en esta etapa, desarrollar un modelo predictivo ni un sistema de detección anticipada de crisis epilépticas.

La finalidad es contar con una estructura organizada que permita consultar y ampliar la información posteriormente.

## 12. Autora

**Claudia Ivett García Vite**  
Maestría en Ciencia de Datos  
Materia: Bases de Datos para Ciencia de Datos  
Profesora: Blanca Esthela Torres Ramírez
