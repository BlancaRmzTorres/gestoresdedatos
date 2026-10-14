# Sesión 7. Bases de datos para la toma de decisiones

> Material de estudio elaborado a partir de la presentación `session7(1).pptx`.

## Contenido
1. Bodegas de datos (Data Warehouse)
2. Procesamiento y análisis en línea (OLAP)
3. Granularidad
4. Esquema estrella
5. Tipos de OLAP
6. KPI y toma de decisiones
7. Actividades
8. OLAP con Python

## Diapositiva 1

3. Base de datos para la toma de decisiones


## Diapositiva 2

Contenido

Bodega de datos (Datawarehouse)

Procesamiento y análisis en línea (OLAP)

01

02


## Diapositiva 3

Bodegas de datos (Datawarehouse)

01


## Diapositiva 4

Definición

Un Data Warehouse es un repositorio centralizado diseñado para almacenar grandes volúmenes de datos históricos provenientes de múltiples fuentes, optimizados para consultas analíticas y toma de decisiones.


## Diapositiva 5

¿Cómo funciona el almacenamiento de datos?

Nivel medio

Nivel inferior

Nivel superior


## Diapositiva 6

Corresponde al repositorio central donde se almacenan los datos integrados provenientes de múltiples fuentes. Antes de llegar al almacén, los datos pasan por procesos ETL (extraer, transformar y cargar) o ELT (extraer, cargar y transformar) para garantizar su calidad y consistencia. Este nivel constituye la base sobre la cual se construyen los Data Marts, los cubos OLAP y las herramientas de Business Intelligence para apoyar la toma de decisiones.

Nivel Inferior

Data Mart es un subconjunto de un Data Warehouse diseñado para satisfacer las necesidades de análisis de un área específica de una organización, como ventas, recursos humanos, finanzas o producción.


## Diapositiva 7

Nivel intermedio

Se encuentran los Data Marts y los cubos OLAP, optimizados para el análisis multidimensional de información específica de cada área de negocio.


## Diapositiva 8

Incluye las herramientas de Business Intelligence utilizadas para generar reportes, dashboards y análisis que apoyan la toma de decisiones estratégicas.

Nivel superior


## Diapositiva 10

Procesamiento y análisis en línea (OLAP)


## Diapositiva 11

OLAP (Online Analytical Processing)

Permite analizar grandes volúmenes de datos desde diferentes perspectivas para apoyar la toma de decisiones


## Diapositiva 12

Procesamiento y análisis en línea (OLAP)

45K

$20K


## Diapositiva 13

Paso 1

45K

$20K


## Diapositiva 14

Paso 2

45K

$20K


## Diapositiva 15

Paso 3

45K

$20K


## Diapositiva 16

Paso 4

45K

$20K


## Diapositiva 17

Operaciones OLAP (Online Analytical Processing)

45K

$20K

.

Las operaciones OLAP son técnicas que permiten analizar datos desde diferentes perspectivas o dimensiones para apoyar la toma de decisiones. Se utilizan comúnmente en los Data Warehouse para explorar grandes volúmenes de información de manera rápida y flexible


## Diapositiva 18

Drill Down (Desglosar)

45K

$20K

.

Permite pasar de un nivel de información general a uno más detallado.
Ejemplo:

Objetivo: Obtener un mayor nivel de detalle.


## Diapositiva 19

Roll Up (Consolidar)

45K

$20K

.

Es la operación inversa al Drill Down. Agrupa datos para obtener una visión más resumida.
Ejemplo:

Objetivo: Obtener indicadores ejecutivos o resúmenes.


## Diapositiva 20

Slice (Corte)

45K

$20K

.

Selecciona una dimensión específica del cubo de datos.
Ejemplo:

Analizar únicamente las ventas de:

Objetivo: Filtrar una dimensión concreta para el análisis.


## Diapositiva 21

Dice (Segmentación)

45K

$20K

.

Permite seleccionar múltiples dimensiones y criterios al mismo tiempo.
Ejemplo:

Un subconjunto más pequeño y específico de información.

Objetivo: Analizar datos bajo múltiples condiciones.


## Diapositiva 22

45K

$20K

.


## Diapositiva 23

Actividad. Aplicando operaciones OLAP

45K

$20K

.

Identificar cuándo utilizar Slice, Dice, Drill Down y Roll Up.
Caso
Una empresa registra las siguientes dimensiones:
Tiempo
Producto
Región
Tienda
Y la medida:
Ventas
Preguntas
Indique qué operación OLAP utilizaría para responder cada pregunta:
Mostrar únicamente las ventas del año 2026.
Analizar las ventas de laptops en Aguascalientes durante 2026.
Pasar de ventas anuales a ventas mensuales.
Obtener las ventas totales por región.


## Diapositiva 24

Solución

45K

$20K

.

🎯 Pregunta de Negocio | 🔍 Operación OLAP | 📝 Descripción

¿Cuánto se vendió durante 2026? | 🟦 Slice | Filtra la información para analizar únicamente el año 2026.

¿Cuánto se vendió de laptops en Aguascalientes durante 2026? | 🟩 Dice | Selecciona simultáneamente varias dimensiones (Producto, Ubicación y Tiempo).

¿Cómo se distribuyeron las ventas de 2026 por mes? | 🟨 Drill Down | Permite pasar de un nivel general (Año) a uno más detallado (Mes).

¿Cuál fue el total de ventas por región? | 🟧 Roll Up | Resume la información agrupando niveles inferiores (Ciudad → Estado → Región).


## Diapositiva 25

45K

$20K

.

Granularidad (nivel de detalle)

La granularidad en OLAP (Online Analytical Processing) se refiere al nivel de detalle con el que se almacenan y analizan los datos dentro de un Data Warehouse o un cubo OLAP.
En términos simples, la granularidad determina qué tan detallada o resumida es la información disponible para el análisis.
Es una característica de los datos que indica que tan detallada es la información.


## Diapositiva 26

45K

$20K

.

Granularidad

Ventajas

Permite análisis profundos.
Facilita identificar patrones específicos.
Ofrece mayor flexibilidad para generar reportes.

Desventajas

Requiere más espacio de almacenamiento.
Las consultas pueden ser más lentas.


## Diapositiva 27

45K

$20K

.

Granularidad y operaciones OLAP

La granularidad está estrechamente relacionada con las operaciones OLAP


## Diapositiva 28

45K

$20K

.


## Diapositiva 29

Esquema Estrella


## Diapositiva 30

45K

$20K

.

Esquema estrella (como se organizan los datos)

Es un modelo de diseño utilizado en los Data Warehouse para organizar la información de forma que las consultas analíticas sean rápidas y eficientes. Su nombre proviene de la forma que adopta el diagrama: una tabla central de hechos rodeada por varias tablas de dimensiones, formando una figura similar a una estrella.


## Diapositiva 31

45K

$20K

.

Tabla de hechos


## Diapositiva 32

Esquema estrella


## Diapositiva 33

45K

$20K

.

Tipos de OLAP

Los tipos de OLAP se refieren a las diferentes arquitecturas utilizadas para almacenar, organizar y consultar la información analítica. La diferencia principal entre ellas radica en dónde se almacenan los datos y cómo se procesan las consultas.


## Diapositiva 34

45K

$20K

.

Ejemplo tipos de OLAP


## Diapositiva 35

45K

$20K

.

Distinguir entre hechos, medidas y dimensiones dentro de un modelo dimensional.
Instrucciones
Analice la siguiente información de una empresa comercial:
Fecha de venta: 15/09/2026
Ciudad: Aguascalientes
Producto: Laptop
Categoría: Tecnología
Cantidad vendida: 5
Importe: $75,000
Sucursal: Centro
Preguntas
¿Cuáles son las medidas?
¿Qué atributos pertenecen a la dimensión Tiempo?
¿Qué atributos pertenecen a la dimensión Producto?
¿Qué atributos pertenecen a la dimensión Geografía?
Diseñe un esquema estrella simplificado.

Actividad. Identificar la tabla de hecho y las dimensiones


## Diapositiva 36

45K

$20K

.

Solución


## Diapositiva 37

KPI  y Toma de decisiones

Los sistemas OLAP permiten transformar grandes volúmenes de datos históricos en información estratégica mediante la generación de indicadores clave de desempeño (KPI). Estos indicadores facilitan la evaluación del cumplimiento de objetivos, la identificación de tendencias y la detección de oportunidades de mejora dentro de una organización.


## Diapositiva 38

45K

$20K

.

Ejemplo de KPI obtenidos mediante OLAP

Ventas totales por período.
Crecimiento porcentual de las ventas.
Participación de mercado por región.
Margen de utilidad por producto.
Rentabilidad por sucursal.
Índice de satisfacción del cliente.


## Diapositiva 39

De los Datos Operacionales a la Toma de Decisiones Estratégicas mediante OLAP


## Diapositiva 40

Ventajas OLAP

Consultas analíticas rápidas.
Análisis multidimensional de la información.
Facilita la identificación de tendencias y patrones.
Apoya la toma de decisiones estratégicas.
Permite consolidar información de múltiples fuentes.
Genera indicadores de desempeño de manera eficiente.


## Diapositiva 41

Desventajas OLAP

Requiere una inversión inicial considerable.
Necesita procesos de integración y limpieza de datos.
Puede requerir gran capacidad de almacenamiento.
El mantenimiento de cubos y modelos puede ser complejo.
La actualización de los datos no siempre es en tiempo real.


## Diapositiva 42

Conclusiones

El Data Warehouse centraliza e integra la información histórica de la organización, mientras que OLAP permite analizarla de manera multidimensional para generar conocimiento útil. Juntos constituyen una plataforma estratégica que transforma datos en información, información en conocimiento y conocimiento en mejores decisiones para la organización.


## Diapositiva 43

45K

$20K

.

OLAP con Python


## Diapositiva 44

Gracias
