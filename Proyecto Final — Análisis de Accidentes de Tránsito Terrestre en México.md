# PROPUESTA DE PROYECTO FINAL

## Análisis de accidentes de tránsito terrestre en México durante 2025 mediante datos semiestructurados y tecnologías NoSQL

---

## 1. Descripción del Proyecto

### 1.1 Problema

Los accidentes de tránsito terrestre generan una gran cantidad de información relacionada con las características de los accidentes, su ubicación, temporalidad, vehículos involucrados, causas y consecuencias.

El conjunto de datos de Accidentes de Tránsito Terrestre (ATUS) del Instituto Nacional de Estadística y Geografía (INEGI) contiene información correspondiente a los accidentes registrados en México. Debido al volumen y diversidad de las variables disponibles, resulta necesario contar con mecanismos que permitan organizar, consultar y analizar la información de manera eficiente.

El problema que se plantea resolver consiste en **organizar y analizar la información de los accidentes de tránsito registrados durante 2025**, con el propósito de identificar patrones y generar indicadores que permitan comprender las principales características de estos accidentes.

### 1.2 Contexto de aplicación

El proyecto se desarrollará utilizando información real proveniente de INEGI, específicamente del conjunto de datos **Accidentes de Tránsito Terrestre (ATUS)**.

El análisis estará enfocado inicialmente en los registros correspondientes al año **2025**, lo que permitirá trabajar con un conjunto de datos delimitado y suficientemente representativo para desarrollar el proyecto dentro del tiempo disponible.

La información contiene variables relacionadas con aspectos como:

- Entidad federativa.
- Municipio.
- Fecha y hora del accidente.
- Tipo de accidente.
- Zona donde ocurrió el accidente.
- Vehículos involucrados.
- Causas del accidente.
- Personas lesionadas.
- Personas fallecidas.
- Características de los conductores.
- Participación de peatones y ciclistas.

### 1.3 Importancia del proyecto

El análisis de los accidentes de tránsito permite transformar los registros disponibles en información que facilite la identificación de comportamientos y patrones.

Mediante el procesamiento y consulta de los datos será posible conocer, por ejemplo:

- En qué entidades se registra una mayor cantidad de accidentes.
- Qué tipos de accidentes son más frecuentes.
- En qué periodos se concentra una mayor cantidad de accidentes.
- Qué vehículos tienen mayor participación.
- Cuáles son las principales causas registradas.
- Cuántas personas resultaron heridas o fallecidas.

La importancia del proyecto radica en demostrar cómo una fuente de datos real puede ser procesada y analizada mediante tecnologías para el manejo de datos semiestructurados y bases de datos NoSQL.

### 1.4 Beneficios esperados

Se espera obtener los siguientes beneficios:

- Organizar de manera eficiente la información de accidentes de tránsito.
- Facilitar la consulta de los registros.
- Identificar patrones relacionados con los accidentes.
- Generar indicadores básicos sobre los accidentes registrados.
- Facilitar la interpretación de la información mediante visualizaciones.
- Aplicar conocimientos relacionados con bases de datos semiestructuradas.
- Explorar el uso de tecnologías NoSQL para almacenar la información.
- Integrar los conocimientos adquiridos durante la asignatura en un proyecto práctico.

---

# 2. Objetivo General y Objetivos Específicos

## 2.1 Objetivo General

**Desarrollar una solución para organizar, consultar y analizar los datos de accidentes de tránsito terrestre registrados en México durante 2025, utilizando tecnologías para el manejo de datos semiestructurados y una base de datos NoSQL, con el propósito de identificar patrones e indicadores relevantes sobre los accidentes registrados.**

## 2.2 Objetivos Específicos

1. **Identificar y seleccionar** las variables relevantes del conjunto de datos de Accidentes de Tránsito Terrestre (ATUS) correspondientes al año 2025.

2. **Explorar y preparar** los datos para facilitar su procesamiento y análisis.

3. **Transformar** parte de la información a formatos semiestructurados como XML y JSON.

4. **Aplicar expresiones XPath y consultas XQuery** para realizar búsquedas y filtrados sobre la información semiestructurada.

5. **Implementar una base de datos NoSQL** para almacenar y consultar la información procesada.

6. **Generar indicadores** relacionados con la cantidad, ubicación, temporalidad, tipo y consecuencias de los accidentes.

7. **Desarrollar una interfaz de visualización** que permita consultar y representar gráficamente los principales resultados obtenidos.

8. **Interpretar los resultados** para identificar patrones y características relevantes de los accidentes de tránsito registrados durante 2025.

---

# 3. Alcance del Proyecto

## 3.1 Datos que serán analizados

El proyecto utilizará como fuente principal el conjunto de datos **Accidentes de Tránsito Terrestre (ATUS)** de INEGI.

Para mantener el proyecto delimitado y factible, el análisis inicial se realizará utilizando los registros correspondientes al **año 2025**.

Las variables que serán consideradas se seleccionarán de acuerdo con su relevancia para el análisis.

Entre las categorías de información disponibles se consideran:

| Categoría | Información |
|---|---|
| Ubicación | Entidad y municipio |
| Temporalidad | Año, mes, día y hora |
| Características | Tipo y zona del accidente |
| Vehículos | Vehículos involucrados |
| Causas | Causa del accidente |
| Víctimas | Personas heridas y fallecidas |
| Conductores | Características de los conductores |
| Usuarios vulnerables | Peatones y ciclistas |

No será necesario utilizar todas las variables disponibles en el conjunto de datos.

---

## 3.2 Tecnologías propuestas

Para el desarrollo del proyecto se propone utilizar:

- **Python:** procesamiento y transformación de los datos.
- **XML:** representación de información semiestructurada.
- **JSON:** representación e intercambio de información.
- **XPath:** navegación y consulta de documentos XML.
- **XQuery:** realización de consultas más avanzadas sobre XML.
- **MongoDB:** almacenamiento de información mediante un modelo NoSQL.
- **MongoDB Atlas:** como alternativa para implementar el almacenamiento en la nube.
- **Herramienta de visualización:** para desarrollar un dashboard con los principales indicadores.

La selección definitiva de las herramientas podrá ajustarse durante el desarrollo de acuerdo con los requerimientos técnicos y la disponibilidad de los recursos.

---

## 3.3 Funcionalidades de la solución

La solución propuesta tendrá como principales funcionalidades:

### Consulta de información

Permitir consultar información relacionada con los accidentes registrados.

### Filtrado de datos

Permitir filtrar los registros utilizando criterios como:

- Entidad.
- Municipio.
- Tipo de accidente.
- Año o periodo.
- Causa.
- Zona.

### Generación de indicadores

Se generarán indicadores como:

- Total de accidentes.
- Accidentes por entidad.
- Accidentes por municipio.
- Accidentes por tipo.
- Accidentes por periodo.
- Personas heridas.
- Personas fallecidas.
- Vehículos involucrados.

### Visualización

La información podrá presentarse mediante:

- Gráficas.
- Tablas.
- Indicadores numéricos.
- Filtros interactivos.

---

## 3.4 Limitaciones

El proyecto tendrá las siguientes limitaciones:

- El análisis se limitará inicialmente a los datos correspondientes a 2025.
- Se utilizará únicamente la información disponible en el conjunto de datos proporcionado por INEGI.
- No se pretende desarrollar un sistema institucional de gestión de accidentes.
- No se realizarán predicciones sobre accidentes futuros.
- No se desarrollarán modelos de inteligencia artificial o aprendizaje automático.
- El proyecto tendrá un propósito académico y de demostración tecnológica.
- La disponibilidad de algunas variables dependerá de la información contenida en el conjunto de datos seleccionado.

Estas limitaciones permitirán mantener un alcance realista y desarrollar el proyecto dentro del periodo establecido.

---

# 4. Fuente de Obtención del Conjunto de Datos

## 4.1 Nombre del conjunto de datos

**Accidentes de Tránsito Terrestre (ATUS)**

## 4.2 Institución responsable

**Instituto Nacional de Estadística y Geografía (INEGI).**

## 4.3 Fuente

El conjunto de datos fue obtenido del portal oficial del Instituto Nacional de Estadística y Geografía (INEGI), mediante la sección correspondiente al programa de Accidentes de Tránsito Terrestre.

## 4.4 Descripción

El conjunto de datos contiene información sobre accidentes de tránsito terrestre registrados en México.

La información permite analizar diferentes características de los accidentes, incluyendo aspectos relacionados con:

- Ubicación.
- Fecha y hora.
- Tipo de accidente.
- Vehículos involucrados.
- Causas.
- Conductores.
- Personas heridas.
- Personas fallecidas.
- Peatones.
- Ciclistas.

El conjunto de datos cuenta con información histórica de diferentes años. Para este proyecto se utilizará inicialmente la información correspondiente a **2025**.

## 4.5 Justificación de la selección

Se seleccionó el conjunto de datos de Accidentes de Tránsito Terrestre de INEGI debido a que constituye una **fuente oficial de información estadística**, además de proporcionar una cantidad importante de registros y diversas variables que permiten realizar diferentes tipos de consultas y análisis.

La información resulta adecuada para el proyecto porque permite aplicar los conceptos estudiados durante la asignatura relacionados con bases de datos, datos semiestructurados, XML, JSON, XPath, XQuery y tecnologías NoSQL.

Además, el conjunto de datos permite desarrollar un proyecto factible y delimitado, evitando la necesidad de utilizar fuentes privadas o información generada artificialmente.

---

# Conclusión de la propuesta

El proyecto propone desarrollar una solución de análisis de accidentes de tránsito terrestre utilizando información real proporcionada por INEGI.

A partir de los datos correspondientes a 2025 se realizará un proceso de exploración, transformación, consulta y almacenamiento utilizando diferentes tecnologías relacionadas con las bases de datos semiestructuradas y NoSQL.

El resultado esperado será una solución que permita consultar la información y visualizar indicadores básicos sobre los accidentes de tránsito, demostrando la aplicación práctica de los conocimientos adquiridos durante la asignatura.

El proyecto se ha delimitado para mantener un alcance factible y permitir su desarrollo dentro del periodo establecido, dejando fuera funcionalidades avanzadas como predicción, inteligencia artificial o aprendizaje automático.