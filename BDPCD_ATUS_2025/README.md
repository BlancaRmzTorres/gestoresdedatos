# Segunda entrega BDPCD — ATUS 2025

## Análisis de accidentes de tránsito terrestre en México durante 2025 mediante datos semiestructurados y tecnologías NoSQL

Esta carpeta contiene los materiales correspondientes a la segunda entrega del proyecto BDPCD, desarrollado a partir de los datos de Accidentes de Tránsito Terrestre en Zonas Urbanas y Suburbanas (ATUS) 2025 del INEGI.

## Contenido

- `diccionario_datos.md`: descripción de los campos y variables del conjunto de datos.
- `modelo_nosql.md`: diseño del modelo de datos para MongoDB.
- `EVIDENCIAS.md`: registro de evidencias y resultados del proceso.
- `requirements.txt`: dependencias de Python.
- `scripts/`: código para limpieza, preparación y carga de datos.

## Flujo de trabajo

1. Obtención de los datos originales.
2. Limpieza y revisión de calidad.
3. Preparación y conversión a formatos CSV y JSONL.
4. Carga de documentos en MongoDB Atlas.
5. Consultas y análisis preliminar.

## Fuente de datos

INEGI — ATUS:

https://www.inegi.org.mx/programas/accidentes/?ps=Microdatos

## Seguridad

Las credenciales de MongoDB Atlas deben configurarse mediante variables de entorno. No se deben publicar contraseñas, cadenas de conexión privadas ni otros secretos.
