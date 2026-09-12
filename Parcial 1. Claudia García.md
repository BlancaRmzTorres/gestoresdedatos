<div align="center">
<img src="https://enlace.ucags.edu.mx/img/logotipos/logo_gu.png" width="320">

# Análisis de datos fisiológicos para la identificación de cambios previos a crisis epilépticas

**Profesora:**  
Blanca Esthela Torres Ramírez

<br>

**Alumna:**  
Claudia Ivett García Vite

<br>

**Maestría en Ciencia de Datos**

<br><br>

**Septiembre 2026**</div>

---

## 1. Descripción del Proyecto

### Problema que se desea resolver

Las personas con epilepsia pueden presentar crisis de manera inesperada, lo que puede ocasionar caídas, accidentes o lesiones. Por esta razón, resulta de interés estudiar si existen cambios en algunas señales fisiológicas o de actividad que puedan presentarse antes de una crisis.

Este proyecto propone analizar datos obtenidos mediante dispositivos de monitoreo de personas con epilepsia, con la finalidad de identificar posibles cambios o patrones durante el periodo previo a una crisis epiléptica.

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
* Señales de EEG (Electroencefalografía).
* Señales de ECG (Electrocardiografía).
* Señales de EMG (Electromiografía).
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

Para el desarrollo del proyecto se consideran diferentes conjuntos de datos académicos de acceso público, relacionados con personas con epilepsia y registros obtenidos mediante dispositivos de monitoreo. La selección final dependerá de las variables disponibles, la cantidad y calidad de los datos, el formato, el tamaño del conjunto y el tiempo disponible para su procesamiento.

### 4.1 My Seizure Gauge Long-term Wearable Data

**Fuente:** Zenodo
**Enlace:** https://zenodo.org/records/17380899

Este conjunto de datos contiene registros de monitoreo a largo plazo de personas con epilepsia. Incluye información obtenida mediante dispositivos portátiles como Empatica E4 y Fitbit Charge HR, además de información relacionada con los momentos en que ocurrieron las crisis.

**¿Por qué podría ser útil para el proyecto?**
Permite estudiar los datos registrados antes de una crisis y compararlos con periodos en los que no ocurrió una crisis, con el objetivo de identificar posibles cambios o patrones.

---

### 4.2 Seizure Diary + Heart Rate (Wearable Data)

**Fuente:** University of Melbourne – Figshare
**Enlace:** https://figshare.unimelb.edu.au/articles/dataset/Seizure_Diary_Wearable_Data/15109896

Este conjunto contiene información de frecuencia cardíaca obtenida mediante dispositivos Fitbit y registros de las crisis reportadas por los participantes mediante un diario electrónico.

**¿Por qué podría ser útil para el proyecto?**
Permite analizar la relación temporal entre la frecuencia cardíaca y los momentos en que se presentaron crisis, buscando posibles cambios durante el periodo previo a una crisis.

---

### 4.3 Wearable Seizure Forecasting Pilot

**Fuente:** University of Melbourne – Figshare
**Enlace:** https://figshare.unimelb.edu.au/articles/dataset/Wearable_Seizure_Forecasting_Pilot/23206445

Este conjunto de datos corresponde a un estudio piloto enfocado en el análisis de información obtenida mediante dispositivos portátiles y registros de crisis en personas con epilepsia. El estudio está relacionado con el análisis de cambios en la probabilidad de presentar una crisis.

**¿Por qué podría ser útil para el proyecto?**
Es especialmente relevante para el objetivo del proyecto porque permite explorar datos relacionados con el periodo previo a una crisis y analizar si existen patrones que puedan estudiarse como posibles señales tempranas.

---

### 4.4 SeizeIT2

**Fuente:** OpenNeuro
**Enlace:** https://openneuro.org/datasets/ds005873

SeizeIT2 es un conjunto de datos que contiene registros de personas con epilepsia obtenidos mediante diferentes dispositivos y sensores. Incluye señales como EEG, ECG, EMG y datos de movimiento, además de información temporal sobre las crisis.

**¿Por qué podría ser útil para el proyecto?**
La variedad de señales permite analizar diferentes tipos de información fisiológica y de movimiento alrededor de las crisis, lo que puede ser útil para explorar qué cambios podrían presentarse antes de ellas.

---

### Criterios para seleccionar el conjunto de datos

Una vez revisadas las fuentes disponibles, se seleccionará el conjunto de datos que resulte más adecuado para el proyecto considerando principalmente:

* Variables disponibles.
* Cantidad de participantes y registros.
* Información sobre los momentos de las crisis.
* Formato de los datos.
* Tamaño del conjunto de datos.
* Facilidad de acceso y procesamiento.
* Posibilidad de identificar periodos previos a las crisis.
* Tiempo disponible para realizar el análisis.

La selección de una fuente específica se realizará después de revisar con mayor detalle la estructura y las variables disponibles en cada conjunto de datos.

---

# 5. Glosario

| Término                         | Definición                                                                                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EEG**                         | Electroencefalografía. Técnica que registra la actividad eléctrica del cerebro mediante electrodos colocados sobre el cuero cabelludo.                    |
| **ECG**                         | Electrocardiografía. Técnica que registra la actividad eléctrica del corazón.                                                                             |
| **EMG**                         | Electromiografía. Técnica que registra la actividad eléctrica de los músculos.                                                                            |
| **Frecuencia cardíaca**         | Número de latidos del corazón por minuto.                                                                                                                 |
| **Acelerómetro**                | Sensor que permite registrar cambios en el movimiento y la aceleración de un dispositivo.                                                                 |
| **Giroscopio**                  | Sensor que permite registrar cambios en la orientación y rotación de un dispositivo.                                                                      |
| **Wearable**                    | Dispositivo electrónico portátil que puede llevarse puesto y que permite registrar información sobre la actividad o el estado fisiológico de una persona. |
| **Dispositivo portátil**        | Dispositivo electrónico diseñado para ser utilizado o llevado por una persona durante sus actividades cotidianas.                                         |
| **Crisis epiléptica**           | Evento producido por una actividad eléctrica anormal y excesiva en el cerebro, que puede manifestarse de diferentes formas.                               |
| **Periodo previo a una crisis** | Intervalo de tiempo anterior a una crisis que puede analizarse para identificar posibles cambios o patrones.                                              |
| **Señal fisiológica**           | Información que representa alguna función o actividad del organismo, como la actividad cerebral, cardíaca o muscular.                                     |
| **Datos de movimiento**         | Información obtenida mediante sensores que permite registrar desplazamientos, aceleraciones, orientación o actividad física.                              |

# 6. Bibliografía

1. Fisher, R. S., Cross, J. H., French, J. A., Higurashi, N., Hirsch, E., Jansen, F. E., Lagae, L., Moshé, S. L., Peltola, J., Roulet Perez, E., Scheffer, I. E., & Zuberi, S. M. (2017). *Operational Classification of Seizure Types by the International League Against Epilepsy*. Epilepsia, 58(4), 522–530.

2. World Health Organization (WHO). (2025). *Epilepsy*. Disponible en: https://www.who.int/news-room/fact-sheets/detail/epilepsy

3. International League Against Epilepsy (ILAE). (2025). *About Epilepsy*. Disponible en: https://www.ilae.org

4. My Seizure Gauge. (2025). *My Seizure Gauge Long-term Wearable Data*. Zenodo. Disponible en: https://zenodo.org/records/17380899

5. University of Melbourne. (2021). *Seizure Diary + Heart Rate (Wearable Data)*. Figshare. Disponible en: https://figshare.unimelb.edu.au/articles/dataset/Seizure_Diary_Wearable_Data/15109896

6. University of Melbourne. (2023). *Wearable Seizure Forecasting Pilot*. Figshare. Disponible en: https://figshare.unimelb.edu.au/articles/dataset/Wearable_Seizure_Forecasting_Pilot/23206445

7. OpenNeuro. (2025). *SeizeIT2 Dataset*. Disponible en: https://openneuro.org/datasets/ds005873

8. Instituto Nacional de Neurología y Neurocirugía. (2024). *Registro Nacional de Epilepsia en México*. Referencia utilizada como antecedente para el contexto epidemiológico de la epilepsia en México.
