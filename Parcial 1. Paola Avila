# Base de datos geoespacial para el análisis y priorización de objetos del Conjunto Nacional de Información Topográfica

### Maestría en Ciencia de Datos

**Materia:** Base de Datos para Ciencia de Datos  
**Profesora:** M.C. Blanca Esthela Torres Ramírez  
**Alumna:** Paola de Jesús Ávila Rivera  

## 1. Descripción del proyecto

El Conjunto Nacional de Información Topográfica (CNIT) a escala 1:50 000 integra información georreferenciada de diferentes rasgos naturales y artificiales presentes en el territorio nacional. Para el desarrollo de este proyecto se utilizará la edición 2025 como fuente de información, debido a que se encuentra disponible públicamente y permite realizar una primera evaluación de la metodología propuesta sin depender de información interna de producción.

Los objetos que integran este conjunto no presentan las mismas características ni relevancia para los procesos de actualización. Algunos se encuentran relacionados con aspectos de seguridad, riesgos, dinámica territorial o infraestructura estratégica, mientras que otros presentan mayor estabilidad y un menor impacto operativo. Esto plantea la necesidad de establecer criterios que permitan diferenciarlos y orientar las estrategias de actualización.

Adicionalmente, el proyecto se desarrolla en un contexto de **cambio metodológico en la generación de información geográfica**, mediante el cual se prevé una reorganización del modelo actual. Como resultado de esta transición, los 73 objetos considerados actualmente pasarán a una estructura de 65 objetos, y algunos elementos podrán obtenerse como información derivada de otros objetos fuente.

Este cambio representa una oportunidad para analizar no solamente la prioridad de actualización de los objetos, sino también las relaciones y dependencias existentes entre ellos. La actualización de un objeto fuente puede tener implicaciones sobre uno o varios productos u objetos derivados, aspecto que deberá considerarse dentro de una estrategia de priorización.

Por ello, el proyecto propone diseñar e implementar una **base de datos geoespacial que permita organizar, caracterizar y analizar los objetos del CNIT 2025 mediante un esquema de cinco niveles de prioridad**, considerando además una estructura suficientemente flexible para representar las futuras relaciones entre objetos fuente y objetos derivados.

La clasificación propuesta considera:

* **Prioridad 1 – Máxima:** seguridad, riesgos, dinámica crítica y elementos territoriales estratégicos.
* **Prioridad 2 – Alta:** infraestructura estratégica, alta variabilidad, movilidad, conectividad y servicios básicos.
* **Prioridad 3 – Media:** objetos de importancia territorial o social con dinámica y criticidad intermedia.
* **Prioridad 4 – Moderada:** rasgos naturales o elementos de referencia espacial relativamente estables.
* **Prioridad 5 – Baja:** objetos de baja variación y reducido impacto operativo o programático.

El CNIT 2025 funcionará como **conjunto de datos piloto**. Si los resultados muestran que la metodología es viable, posteriormente podrá evaluarse con información de producción y con la estructura correspondiente al nuevo modelo metodológico.

### Importancia del proyecto

Los cambios previstos en la generación de información geográfica hacen necesario revisar no solamente qué información debe actualizarse primero, sino también la relación que existe entre los diferentes objetos.

Cuando un objeto constituye la fuente para generar o actualizar otros elementos derivados, su relevancia dentro del proceso puede ser mayor que la determinada únicamente por sus características individuales.

Por ello, contar con una base de datos capaz de representar objetos, características, prioridades y relaciones de dependencia permitirá analizar el problema desde una perspectiva integral y proporcionar información que pueda apoyar la definición de futuras estrategias de actualización.

### Beneficios esperados

El proyecto permitirá:

* Integrar los objetos del CNIT 2025 en una base de datos geoespacial.
* Establecer una clasificación mediante cinco niveles de prioridad.
* Relacionar la prioridad con las características de cada tipo de objeto.
* Representar relaciones entre objetos fuente y objetos derivados.
* Analizar la distribución territorial de los diferentes niveles de prioridad.
* Identificar objetos cuya actualización pueda tener impacto sobre otros elementos.
* Preparar una estructura adaptable al cambio metodológico previsto.
* Generar información que posteriormente pueda utilizarse para evaluar estrategias de actualización.
* Preparar los datos para futuros análisis mediante técnicas de Ciencia de Datos.
* Evaluar la viabilidad de la propuesta antes de incorporar información interna de producción.

### Problema que se desea resolver

Los objetos que integran la información topográfica presentan diferentes características, niveles de dinámica e importancia dentro de los procesos de actualización. Sin embargo, su atención no necesariamente parte de un esquema de priorización que considere de manera conjunta aspectos como su relación con riesgos, infraestructura estratégica, función territorial y dependencia con otros objetos.

Ante el cambio metodológico previsto, en el que algunos objetos podrán obtenerse como derivados de otros, resulta necesario contar con una estructura de datos que permita representar estas relaciones y analizar qué elementos deberían tener mayor prioridad de actualización.

El problema consiste, por tanto, en determinar cómo organizar y relacionar estas características dentro de una base de datos geoespacial que permita establecer y posteriormente evaluar criterios de priorización para los objetos de información topográfica.

## 2. Objetivo general

Diseñar e implementar una base de datos geoespacial a partir del Conjunto Nacional de Información Topográfica 2025 que permita integrar y analizar las características, relaciones y niveles de prioridad de sus objetos espaciales, considerando su posible adaptación al nuevo modelo metodológico de generación de información geográfica y su posterior aplicación en estrategias de actualización.

## Objetivos específicos

1. Identificar los objetos y atributos del CNIT 2025 que serán utilizados en el proyecto.

2. Definir criterios que permitan clasificar los objetos mediante cinco niveles de prioridad de acuerdo con su relevancia, dinámica, relación con riesgos, infraestructura y función territorial.

3. Diseñar un modelo de datos que permita relacionar los objetos geoespaciales, sus características y el nivel de prioridad asignado.

4. Implementar una base de datos geoespacial que permita almacenar, gestionar y consultar la información seleccionada del CNIT 2025.

5. Desarrollar consultas que permitan analizar los objetos de acuerdo con sus características, ubicación, relaciones y nivel de prioridad.

6. Analizar la distribución espacial y las características de los objetos correspondientes a cada nivel de prioridad.

7. Evaluar la capacidad del modelo propuesto para adaptarse al cambio metodológico previsto e identificar variables que posteriormente puedan utilizarse en técnicas de Ciencia de Datos orientadas a mejorar los procesos de clasificación y priorización.

## 3. Alcance del proyecto

El proyecto utilizará como conjunto de datos experimental el **Conjunto Nacional de Información Topográfica 2025**, conservando la estructura correspondiente a dicha edición.

No se transformará el conjunto de datos de 2025 para simular directamente la nueva estructura metodológica. En su lugar, el diseño de la base de datos buscará permitir la representación de cambios en el catálogo de objetos y de relaciones entre objetos fuente y derivados.

Esta decisión permitirá diferenciar dos escenarios:

**Escenario experimental:** información pública correspondiente al CNIT 2025 y su estructura vigente.

**Escenario de aplicación futura:** nuevo esquema metodológico de 65 objetos, incluyendo aquellos cuya generación dependa o se derive de otros elementos geográficos.

La separación permitirá utilizar información verificable y disponible para desarrollar el proyecto, sin perder de vista las condiciones bajo las cuales podría aplicarse posteriormente.

### Datos que serán analizados

Se considerarán, de acuerdo con su disponibilidad:

* identificador del objeto;
* tipo de objeto espacial;
* componente geométrico;
* atributos descriptivos;
* ubicación geográfica;
* geometría;
* categoría temática;
* nivel de prioridad;
* criterios de priorización;
* relación con otros objetos;
* condición de objeto fuente o derivado, cuando corresponda.

### Tecnologías propuestas

Se contempla utilizar PostgreSQL, PostGIS, SQL, Python y QGIS para el almacenamiento, gestión, procesamiento, consulta y análisis de la información.

### Funcionalidades propuestas

La base de datos permitirá:

* Almacenar y consultar los objetos geoespaciales seleccionados del CNIT 2025;
* Asociar cada tipo de objeto con los criterios y el nivel de prioridad correspondiente;
* Representar las relaciones existentes entre objetos fuente y objetos derivados;
* Realizar consultas por tipo de objeto, componente geométrico, ubicación y nivel de prioridad;
* Obtener la cantidad y distribución de objetos correspondiente a cada nivel de prioridad;
* Identificar objetos cuya actualización pueda tener implicaciones sobre otros elementos derivados;
* Generar conjuntos de datos que posteriormente puedan utilizarse para análisis espaciales y técnicas de Ciencia de Datos.

### Limitaciones

El proyecto utilizará inicialmente información correspondiente a una sola edición, por lo que no será posible determinar empíricamente la frecuencia real de actualización de los objetos utilizando únicamente el CNIT 2025.

Asimismo, debido a que la nueva metodología representa un escenario de transición, la evaluación inicial se realizará sobre la estructura pública disponible. La incorporación del nuevo catálogo y de información operativa dependerá de su disponibilidad y de las condiciones institucionales para su utilización.

Por este motivo, el proyecto deberá entenderse como una **prueba de concepto y una primera etapa de investigación**, cuyo diseño busca permitir una evolución posterior hacia datos reales de producción.

## 4. Fuente de obtención del conjunto de datos

### Nombre

**Conjunto Nacional de Información Topográfica a escala 1:50 000, 2025.**

### Fuente

Instituto Nacional de Estadística y Geografía (INEGI).

**Enlace de consulta:** https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=794551163047

### Descripción

El CNIT 2025 contiene información georreferenciada de diferentes elementos naturales y artificiales del territorio nacional, representados mediante geometrías de punto, línea y área y acompañados de atributos descriptivos.

### Justificación

Se seleccionó este conjunto debido a que constituye una fuente oficial, pública y estructurada de información geoespacial, además de encontrarse directamente relacionada con el problema que se pretende estudiar.

Su utilización permitirá desarrollar una primera versión de la base de datos utilizando información accesible y reproducible. Esto permitirá evaluar la metodología antes de incorporar información correspondiente a los procesos internos de producción.

La edición 2025 representa además un punto de referencia particularmente útil ante el cambio metodológico previsto, ya que permitirá documentar y analizar posteriormente la transición entre la estructura utilizada actualmente y el nuevo modelo de objetos geográficos.

## Continuidad con el proyecto de Seminario de Tesis

El proyecto de Base de Datos para Ciencia de Datos constituirá una primera etapa técnica del proyecto desarrollado en Seminario de Tesis.

El análisis inicial permitirá estudiar la clasificación de los objetos mediante cinco niveles de prioridad y establecer una estructura capaz de representar relaciones entre objetos.

Posteriormente, la investigación podrá incorporar dos dimensiones adicionales: **el nuevo modelo metodológico y el comportamiento real observado durante los procesos de producción**.

Esto permitirá evaluar si la prioridad definida conceptualmente coincide con factores observados en los datos, como frecuencia de modificación, número de inconsistencias, recurrencia, tiempos de atención y dependencia entre objetos.

De esta manera, la investigación podrá avanzar desde una clasificación conceptual hacia un modelo de priorización sustentado progresivamente en evidencia obtenida de los procesos de actualización.
