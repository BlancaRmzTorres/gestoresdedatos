# Análisis de datos fisiológicos para la identificación de cambios previos a crisis epilépticas

## 1. Descripción del Proyecto

### Problema que se desea resolver

Las personas con epilepsia pueden presentar crisis de manera inesperada, lo que puede ocasionar caídas, accidentes o lesiones. Por esta razón, resulta de interés estudiar si existen cambios en algunas señales fisiológicas o de actividad que puedan presentarse antes de una crisis.

Este proyecto propone analizar datos obtenidos mediante dispositivos de monitoreo y *wearables* de personas con epilepsia, con la finalidad de identificar posibles cambios o patrones durante el periodo previo a una crisis epiléptica.

### Contexto de aplicación

El proyecto se encuentra dentro del área de análisis de datos aplicado a la salud. Se utilizarán conjuntos de datos provenientes de investigaciones académicas que contienen información de personas con epilepsia y registros obtenidos mediante dispositivos como relojes inteligentes y otros dispositivos de monitoreo.

El análisis estará orientado a comparar los registros correspondientes a periodos previos a una crisis con periodos en los que no se presentó una crisis.

### Importancia del análisis

Identificar cambios que puedan estar relacionados con la proximidad de una crisis podría ayudar a comprender mejor el comportamiento de algunas señales fisiológicas y de actividad antes de estos eventos.

Además, este análisis puede servir como una primera etapa para investigaciones posteriores relacionadas con sistemas de monitoreo y alerta temprana para personas con epilepsia.

### Beneficios esperados

Se espera obtener una mejor comprensión de las variables disponibles en los datos y determinar si existen patrones o cambios que puedan ser relevantes durante el periodo previo a una crisis.

También se espera desarrollar un proceso para organizar, transformar y analizar datos provenientes de dispositivos de monitoreo, utilizando diferentes formatos de datos estructurados y semiestructurados.

---

## 2. Objetivo General y Objetivos Específicos

### Objetivo General

Analizar datos fisiológicos y de actividad obtenidos mediante dispositivos de monitoreo de personas con epilepsia, con el propósito de identificar posibles cambios o patrones asociados al periodo previo a una crisis epiléptica.

### Objetivos Específicos

* Identificar y seleccionar un conjunto de datos que contenga información de personas con epilepsia y registros de crisis identificadas.
* Explorar y describir las variables disponibles en el conjunto de datos seleccionado.
* Preparar y transformar los datos para facilitar su procesamiento y análisis.
* Identificar registros correspondientes a periodos previos a una crisis y compararlos con periodos sin crisis.
* Analizar posibles cambios o patrones en las variables fisiológicas y de actividad.
* Representar los resultados mediante tablas y visualizaciones para facilitar su interpretación.
* Documentar los resultados y las limitaciones encontradas durante el análisis.

---

## 3. Alcance del Proyecto

### Datos que serán analizados

Se analizará un conjunto de datos relacionado con personas con epilepsia que contenga información fisiológica, de actividad o movimiento, así como registros que permitan identificar cuándo ocurrieron las crisis.

Dependiendo del conjunto de datos seleccionado, algunas de las variables podrían incluir:

* Frecuencia cardiaca.
* Actividad física.
* Movimiento.
* Señales de EEG.
* Señales de ECG.
* Señales de EMG.
* Información temporal de las crisis.
* Otras variables disponibles en el conjunto seleccionado.

### Tecnologías propuestas

Se contempla utilizar:

* **Python** para el procesamiento y análisis de datos.
* **Pandas** para la manipulación de datos.
* **JSON y/o XML** para la representación y transformación de información.
* **Matplotlib o Plotly** para la generación de visualizaciones.
* **Jupyter Notebook o Google Colab** como entorno de trabajo.

### Funcionalidades propuestas

El proyecto buscará realizar las siguientes funciones:

1. Cargar y organizar el conjunto de datos.
2. Revisar y describir las variables disponibles.
3. Realizar limpieza y transformación de los datos.
4. Identificar los periodos correspondientes a las crisis.
5. Seleccionar y analizar periodos previos a las crisis.
6. Comparar los periodos previos a las crisis con periodos sin crisis.
7. Generar tablas y visualizaciones de los resultados.
8. Identificar posibles patrones o cambios que puedan ser relevantes para estudios posteriores.

### Lo que no incluirá

El proyecto no contempla desarrollar un dispositivo médico ni una aplicación comercial de alerta.

Tampoco se busca realizar un diagnóstico médico ni afirmar que una determinada variable pueda predecir por sí sola una crisis epiléptica.

En esta etapa tampoco se establecerá de antemano un conjunto definitivo de variables predictoras, ya que una parte del proyecto consiste en explorar los datos para determinar cuáles podrían ser relevantes.

### Limitaciones

Una de las principales limitaciones será la disponibilidad y tamaño de los conjuntos de datos. Algunos de ellos contienen grandes cantidades de información, por lo que será necesario seleccionar un subconjunto que pueda ser procesado durante el periodo disponible para el proyecto.

Otra limitación es que los datos disponibles provienen de estudios realizados en otros países y con poblaciones específicas, por lo que los resultados no necesariamente podrán generalizarse a todas las personas con epilepsia.

---

## 4. Fuente de Obtención del Conjunto de Datos

Para el desarrollo del proyecto se consideran como posibles fuentes **conjuntos de datos académicos de acceso abierto** relacionados con epilepsia y registros obtenidos mediante dispositivos *wearables* o sistemas de monitoreo fisiológico.

La selección definitiva del conjunto de datos se realizará después de revisar sus variables, formato, tamaño, disponibilidad y facilidad de procesamiento.

### 4.1 My Seizure Gauge Long-term Wearable Data

* **Repositorio:** [Zenodo](https://zenodo.org/)
* **Conjunto de datos:** [My Seizure Gauge Long-term Wearable Data](https://zenodo.org/records/17380899)
* **País de origen de los participantes:** Estados Unidos.
* **Tipo de datos:** Registros de largo plazo obtenidos mediante dispositivos *wearables*.

Este conjunto contiene información de personas con epilepsia monitoreadas durante periodos prolongados. Incluye datos obtenidos mediante dispositivos como Empatica E4 y Fitbit Charge HR, entre ellos frecuencia cardiaca y actividad, además de información sobre los momentos en que ocurrieron las crisis.

**Posible utilidad para el proyecto:** permitiría comparar las señales registradas antes de una crisis con periodos en los que no se presentó una crisis.

### 4.2 Seizure Diary + Heart Rate (Wearable Data)

* **Repositorio:** University of Melbourne - Figshare.
* **Conjunto de datos:** [Seizure Diary + Heart Rate (Wearable Data)](https://figshare.unimelb.edu.au/articles/dataset/Seizure_Diary_Wearable_Data/15109896)
* **País de origen:** Australia.
* **Tipo de datos:** Frecuencia cardiaca y registros de crisis.

El conjunto contiene datos de frecuencia cardiaca obtenidos mediante dispositivos Fitbit y registros de las crisis reportadas por los participantes mediante una aplicación de registro.

**Posible utilidad para el proyecto:** permitiría analizar si existen cambios en la frecuencia cardiaca asociados temporalmente con los periodos previos a las crisis.

### 4.3 Wearable Seizure Forecasting Pilot

* **Repositorio:** University of Melbourne - Figshare.
* **Conjunto de datos:** [Wearable Seizure Forecasting Pilot](https://figshare.unimelb.edu.au/articles/dataset/Wearable_Seizure_Forecasting_Pilo_)

