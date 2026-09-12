# Evaluación del Proyecto Final

## Análisis y clasificación de perfiles de madurez digital en México mediante XML y XQuery

**Alumno:** Alexis Jaisiel Ortiz Lara  
**Asignatura:** Bases de Datos para Ciencia De Datos

---

## 1. Descripción del proyecto

El acceso a internet y a dispositivos tecnológicos ha aumentado en México; sin embargo, disponer de tecnología no significa necesariamente contar con las mismas habilidades para utilizarla y aprovecharla. La brecha digital también se relaciona con el tipo de dispositivos disponibles, la frecuencia de uso de internet, las actividades realizadas y las habilidades digitales de los usuarios.

El proyecto propone analizar y clasificar distintos **perfiles de madurez digital en México** utilizando los microdatos de la **ENDUTIH 2024 del INEGI**. Se considerarán cuatro dimensiones principales:

- **Conectividad:** disponibilidad y acceso a internet.
- **Equipamiento:** disponibilidad de computadora, laptop, tablet y smartphone.
- **Uso digital:** frecuencia y diversidad de actividades realizadas mediante las TIC.
- **Habilidades digitales:** capacidades para utilizar documentos, hojas de cálculo, presentaciones, bases de datos, programación y otras herramientas.

A partir de estas dimensiones se desarrollará un **Índice de Madurez Digital (IMD)** que permitirá clasificar los registros en perfiles de **brecha digital, básico, intermedio y avanzado**. El IMD será un indicador desarrollado específicamente para este proyecto y no corresponde a un indicador oficial del INEGI.

Como parte tecnológica, los datos seleccionados serán transformados a **XML** y posteriormente consultados mediante **XPath y XQuery**, permitiendo filtrar, ordenar, agrupar y comparar los diferentes perfiles.

El proyecto permitirá identificar diferencias entre simplemente disponer de tecnología y contar con las capacidades necesarias para aprovecharla, generando una visión más completa de la brecha digital.

---

## 2. Objetivo general y objetivos específicos

### Objetivo general

**Analizar y clasificar el nivel de madurez digital de los usuarios en México mediante información de la ENDUTIH 2024, estructurando los datos en XML y utilizando XPath y XQuery para identificar perfiles relacionados con conectividad, equipamiento, uso y habilidades digitales.**

### Objetivos específicos

1. Seleccionar las variables de la ENDUTIH 2024 relacionadas con conectividad, equipamiento, uso de internet y habilidades digitales.
2. Preparar y transformar los datos seleccionados a una estructura XML adecuada para su consulta.
3. Diseñar un **Índice de Madurez Digital (IMD)** que integre las principales características tecnológicas de los registros analizados.
4. Clasificar los registros en perfiles de madurez digital: brecha digital, básico, intermedio y avanzado.
5. Desarrollar consultas mediante XPath y XQuery para analizar y comparar los perfiles obtenidos.

---

## 3. Alcance del proyecto

### Datos que serán analizados

Se utilizarán variables de la ENDUTIH 2024 agrupadas en las siguientes dimensiones:

| Dimensión | Información considerada |
|---|---|
| Conectividad | Disponibilidad y características del acceso a internet |
| Equipamiento | Computadora, laptop, tablet, celular y smartphone |
| Uso digital | Uso de internet, frecuencia y actividades realizadas |
| Habilidades digitales | Documentos, hojas de cálculo, presentaciones, bases de datos, programación, entre otras |

Antes de integrar las variables se verificará el universo de aplicación de cada pregunta, los códigos de respuesta, valores faltantes y los identificadores necesarios para relacionar correctamente los registros.

### Tecnologías

Los microdatos originales de la ENDUTIH 2024 se encuentran disponibles en **DBF**. El **Descriptor de archivos (FD)** proporcionado por INEGI en formato XLSX permitirá identificar e interpretar las variables.

Los datos seleccionados serán posteriormente transformados a **XML**, creando una estructura semiestructurada propia para el proyecto.

Sobre esta estructura se utilizará:

- **XPath:** navegación y selección de elementos.
- **XQuery:** filtrado, ordenamiento, agrupación, conteo y transformación de información.
- **FLWOR:** construcción de consultas más complejas mediante `FOR`, `LET`, `WHERE`, `ORDER BY` y `RETURN`.

El proceso general será:

**ENDUTIH 2024 (DBF) → selección y preparación → transformación a XML → XPath/XQuery → Índice de Madurez Digital → clasificación de perfiles → resultados**

### Índice de Madurez Digital

El IMD integrará indicadores de las cuatro dimensiones seleccionadas. Se utilizará un sistema de puntuación documentado y reproducible, normalizado en una escala de 0 a 100.

De manera general:

**IMD = (Puntos obtenidos / Puntos máximos posibles) × 100**

A partir de la distribución obtenida se establecerán los criterios definitivos para clasificar los registros en:

- **Brecha digital**
- **Digital básico**
- **Digital intermedio**
- **Digital avanzado**

### Funcionalidades

La solución permitirá:

- identificar los perfiles de madurez digital;
- conocer las habilidades digitales más y menos frecuentes;
- comparar niveles de conectividad, equipamiento y uso;
- identificar usuarios con acceso a internet pero con habilidades digitales limitadas;
- realizar consultas y generar resultados mediante XPath y XQuery;
- presentar los resultados mediante tablas y gráficas.

### Limitaciones

El proyecto tendrá un alcance **descriptivo, exploratorio y clasificatorio**. No pretende establecer relaciones causales ni considerar el IMD como un indicador oficial del INEGI.

La selección de variables respetará el diseño y universo de aplicación de la ENDUTIH. Los datos originales no serán modificados; únicamente se generará una estructura XML derivada para realizar el análisis.

---

## 4. Fuente de obtención del conjunto de datos

### Nombre

**Encuesta Nacional sobre Disponibilidad y Uso de Tecnologías de la Información en los Hogares (ENDUTIH) 2024.**

### Institución

**Instituto Nacional de Estadística y Geografía (INEGI).**

### Fuente de consulta

**Portal oficial de ENDUTIH 2024:**  
https://www.inegi.org.mx/programas/endutih/2024/#microdatos

### Descripción

La ENDUTIH proporciona información sobre la disponibilidad y utilización de Tecnologías de la Información y la Comunicación en los hogares y entre los usuarios en México.

Para el proyecto se utilizarán principalmente dos recursos disponibles en la sección de microdatos:

| Recurso | Formato | Uso |
|---|---|---|
| Base de datos | DBF | Obtención de los microdatos |
| Descriptor de archivos (FD) | XLSX | Identificación e interpretación de variables |

### Justificación

La ENDUTIH 2024 fue seleccionada porque es una fuente oficial, confiable y disponible públicamente que contiene información directamente relacionada con el problema estudiado.

Sus variables permiten analizar diferentes niveles de la brecha digital, desde la disponibilidad de tecnología hasta las habilidades necesarias para aprovecharla.

Además, su estructura permite desarrollar un proceso tecnológico de **extracción, transformación y consulta de datos**, convirtiendo los registros seleccionados de DBF a XML y utilizando posteriormente XPath y XQuery para realizar el análisis.

---

## Producto final esperado

El producto final será un **sistema de análisis y clasificación de perfiles de madurez digital**, integrado por:

1. Datos seleccionados de la ENDUTIH 2024.
2. Transformación de los registros de DBF a XML.
3. Estructura semiestructurada XML.
4. Consultas XPath y XQuery.
5. Índice de Madurez Digital (IMD).
6. Clasificación de perfiles digitales.
7. Tablas y gráficas para presentar e interpretar los resultados.

El proyecto permitirá utilizar datos oficiales del INEGI para estudiar la brecha digital desde una perspectiva más amplia, considerando no solamente el acceso a la tecnología, sino también su uso y las habilidades digitales de los usuarios.
