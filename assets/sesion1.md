## **Sesión 1. Base de datos para Ciencia de Datos** 

## **¿Por qué estudiar base de datos en ciencia de datos?**

El estudio de bases de datos en Ciencia de Datos es fundamental porque los datos constituyen la materia prima para generar conocimiento y apoyar la toma de decisiones. Para aprovechar su valor, es necesario almacenarlos, organizarlos, consultarlos y procesarlos de manera eficiente, considerando que la tecnología utilizada para su almacenamiento influye directamente en el análisis y los resultados obtenidos. Además, las fuentes de información pueden presentarse en distintos formatos, desde datos estructurados y semiestructurados hasta grandes volúmenes de información, por lo que es indispensable comprender cómo gestionarlos adecuadamente.

### Fuentes de Información: Estructurada

La **información estructurada** es aquella que se encuentra organizada de forma lógica y siguiendo un esquema previamente definido. Sus datos se almacenan en campos, registros, tablas o categorías específicas, lo que permite que tanto las personas como los sistemas informáticos puedan acceder, interpretar y procesar la información de manera rápida y eficiente.

Este tipo de información es ampliamente utilizado en bases de datos, sistemas de gestión empresarial, aplicaciones web, hojas de cálculo y otros entornos donde es necesario mantener un orden y consistencia en los datos. Gracias a su estructura uniforme, facilita la automatización de procesos, la generación de reportes y la toma de decisiones basada en información confiable.

### Características

- Está organizada en **campos, categorías, registros o tablas**.
- Sigue una **estructura uniforme y consistente** para todos los datos almacenados.
- Facilita el almacenamiento en **bases de datos relacionales** y hojas de cálculo.
- Permite realizar búsquedas, filtros, consultas y análisis de manera eficiente.
- Puede ser procesada automáticamente por aplicaciones y algoritmos.
- Favorece la integridad y calidad de los datos al reducir errores de captura.
- Facilita la generación de estadísticas, reportes e indicadores de desempeño.
- Es escalable y puede manejar grandes volúmenes de información de forma ordenada.

### Ventajas

- Mayor rapidez para localizar información específica.
- Facilita la actualización y mantenimiento de los datos.
- Permite compartir información entre diferentes sistemas.
- Mejora la precisión en los procesos de análisis y toma de decisiones.
- Reduce la duplicidad de información y los errores de registro.

### Ejemplo de Información Estructurada

La siguiente información puede almacenarse en una tabla de base de datos:

| Nombre | Departamento | Edad | Correo Electrónico |
|----------|----------|------|-------------------|
| María López | Recursos Humanos | 35 | maria.lopez@empresa.com |

En este ejemplo, cada dato ocupa un campo específico (nombre, departamento, edad y correo electrónico), lo que permite realizar consultas, filtros o reportes de manera sencilla.

### Aplicaciones Comunes

La información estructurada se encuentra habitualmente en:

- Sistemas de Recursos Humanos.
- Sistemas de control escolar.
- Inventarios y almacenes.
- Registros de clientes y proveedores.
- Sistemas bancarios y financieros.
- Expedientes médicos electrónicos.
- Plataformas de comercio electrónico.

### Fuentes de Información: Semiestructurada

La **información semiestructurada** es un tipo de información que no se encuentra organizada bajo un esquema rígido como el de las bases de datos relacionales, pero que sí incorpora ciertos elementos de organización que facilitan su identificación, clasificación y procesamiento. Estos elementos pueden ser etiquetas, metadatos, campos o marcas que aportan estructura al contenido, aunque sin imponer un formato completamente fijo.

Este tipo de información representa un punto intermedio entre la información estructurada y la no estructurada. Gracias a su flexibilidad, puede adaptarse a diferentes necesidades y formatos, permitiendo almacenar información variada sin perder la capacidad de ser interpretada por sistemas informáticos.

La información semiestructurada es ampliamente utilizada en aplicaciones modernas, sitios web, servicios en la nube, sistemas de mensajería y procesos de intercambio de datos entre diferentes plataformas.

### Características

- No sigue un esquema rígido de filas y columnas.
- Utiliza **etiquetas, metadatos o marcadores** para organizar la información.
- Presenta una estructura flexible que puede variar según las necesidades.
- Puede ser interpretada tanto por personas como por sistemas informáticos.
- Facilita el intercambio de información entre aplicaciones y servicios.
- Permite almacenar datos heterogéneos sin requerir una estructura uniforme.
- Ofrece un equilibrio entre flexibilidad y organización.
- Es común en formatos como XML, JSON, correos electrónicos y documentos con metadatos.

### Ventajas

- Mayor flexibilidad para almacenar diferentes tipos de datos.
- Facilita la interoperabilidad entre sistemas.
- Permite agregar nuevos campos sin modificar toda la estructura.
- Reduce las limitaciones de los esquemas estrictamente definidos.
- Favorece el intercambio de información en entornos digitales y web.

### Ejemplo de Información Semiestructurada

### Correo electrónico

```text
De: juan.perez@empresa.com
Para: maria.lopez@empresa.com
Asunto: Reunión de seguimiento

Hola María,

Te comparto la información para la reunión programada el día viernes a las 10:00 a.m.

Saludos,
Juan Pérez
```

### **Fuentes de Información: Gran Volumen (Big Data)**

La **información de gran volumen**, conocida comúnmente como **Big Data**, se refiere a conjuntos de datos que, debido a su enorme tamaño, diversidad y velocidad de generación, no pueden ser gestionados eficientemente mediante las herramientas tradicionales de almacenamiento y procesamiento de datos.

El crecimiento exponencial de Internet, las redes sociales, los dispositivos móviles, los sensores inteligentes y las transacciones digitales ha provocado que las organizaciones generen y recopilen cantidades masivas de información todos los días. Para analizar estos datos y extraer información valiosa, se requieren tecnologías especializadas capaces de procesar grandes volúmenes de información en tiempo real o casi real.

Big Data permite identificar patrones, tendencias y relaciones ocultas en los datos, contribuyendo a una mejor toma de decisiones en ámbitos como negocios, salud, educación, manufactura, finanzas y gobierno.

### Características Principales: Las 5 V de Big Data

#### 1. Volumen

Se refiere a la enorme cantidad de datos generados y almacenados continuamente por personas, organizaciones y dispositivos. Estos volúmenes pueden alcanzar desde terabytes hasta petabytes o incluso exabytes de información.

#### 2. Velocidad

Hace referencia a la rapidez con la que los datos son generados, transmitidos y procesados. Algunos sistemas requieren analizar la información prácticamente en tiempo real para obtener resultados útiles.

#### 3. Variedad

Los datos provienen de múltiples fuentes y formatos, incluyendo información estructurada, semiestructurada y no estructurada, como textos, imágenes, videos, audios, documentos y registros de sensores.

#### 4. Veracidad

Se relaciona con la calidad, precisión y confiabilidad de los datos. No toda la información recopilada es exacta o útil, por lo que es necesario validar y depurar los datos antes de analizarlos.

#### 5. Valor

Representa el beneficio que puede obtenerse a partir del análisis de los datos. El verdadero propósito de Big Data es transformar grandes cantidades de información en conocimiento útil para apoyar la toma de decisiones.

### Ventajas

- Permite analizar grandes cantidades de información en poco tiempo.
- Facilita la identificación de tendencias y patrones de comportamiento.
- Mejora la toma de decisiones basada en datos.
- Ayuda a optimizar procesos y reducir costos operativos.
- Permite personalizar productos y servicios según las necesidades de los usuarios.
- Favorece la detección de riesgos, anomalías y fraudes.
- Contribuye al desarrollo de soluciones innovadoras y estrategias más efectivas.

### Ejemplos de Información de Gran Volumen

#### Redes Sociales

Plataformas como Facebook, X (Twitter), Instagram, TikTok y LinkedIn generan millones de publicaciones, comentarios, imágenes y videos diariamente.

#### Comercio Electrónico

Tiendas en línea registran constantemente información sobre compras, búsquedas, clics, preferencias de productos y comportamiento de los clientes.

#### Internet de las Cosas (IoT)

Sensores inteligentes instalados en vehículos, fábricas, hogares o ciudades generan datos de manera continua sobre temperatura, ubicación, consumo energético y funcionamiento de equipos.

#### Sistemas Bancarios y Financieros

Las instituciones financieras procesan millones de transacciones electrónicas diariamente para detectar fraudes, evaluar riesgos y ofrecer productos personalizados.

#### Dispositivos Móviles

Los teléfonos

### El Papel de las Bases de Datos en la Ciencia de Datos

Las **bases de datos** desempeñan un papel fundamental en la Ciencia de Datos, ya que constituyen el principal mecanismo para almacenar, organizar, administrar y recuperar grandes volúmenes de información. Gracias a ellas, los datos pueden mantenerse de forma estructurada y accesible, permitiendo su posterior procesamiento y análisis para la generación de conocimiento útil.

En los proyectos de Ciencia de Datos, las bases de datos funcionan como el punto central donde se recopilan datos provenientes de múltiples fuentes, como sistemas empresariales, aplicaciones web, sensores, redes sociales, dispositivos móviles y plataformas de comercio electrónico. Sin una adecuada gestión de estos datos, sería difícil obtener información confiable para la toma de decisiones.

### Flujo de las Bases de Datos en la Ciencia de Datos

#### 1. Fuente de Datos

La información se genera a partir de distintas fuentes, entre las que se incluyen:

- Sistemas de información empresariales.
- Aplicaciones web y móviles.
- Redes sociales.
- Sensores IoT (Internet de las Cosas).
- Transacciones bancarias y comerciales.
- Archivos y documentos digitales.

En esta etapa, los datos pueden presentarse en formatos estructurados, semiestructurados o no estructurados.

#### 2. Almacenamiento

Una vez recopilados, los datos se almacenan en bases de datos o repositorios especializados para garantizar su disponibilidad, seguridad y organización.

Los sistemas más utilizados incluyen:

- Bases de datos relacionales (MySQL, PostgreSQL, SQL Server, Oracle).
- Bases de datos NoSQL (MongoDB, Cassandra, Redis).
- Data Warehouses.
- Data Lakes.

El objetivo es conservar la información de forma eficiente para facilitar su consulta y procesamiento posterior.

#### 3. Procesamiento

En esta fase, los datos son preparados para su análisis mediante diversas actividades, tales como:

- Limpieza de datos.
- Eliminación de registros duplicados.
- Corrección de errores.
- Integración de diferentes fuentes de información.
- Transformación y normalización de datos.

La calidad de los resultados obtenidos depende en gran medida de la calidad de este proceso.

#### 4. Análisis

Los datos procesados son examinados utilizando técnicas estadísticas, minería de datos, inteligencia artificial y aprendizaje automático.

Durante esta etapa se busca:

- Identificar patrones y tendencias.
- Detectar anomalías o comportamientos inusuales.
- Realizar predicciones.
- Obtener indicadores de desempeño.
- Generar conocimiento para la organización.

Herramientas como Python, R, Power BI y Tableau son frecuentemente utilizadas para estas tareas.

#### 5. Toma de Decisiones

Finalmente, los resultados obtenidos se transforman en información útil para apoyar la toma de decisiones estratégicas y operativas.

Algunos ejemplos incluyen:

- Optimización de procesos empresariales.
- Personalización de productos y servicios.
- Detección de fraudes financieros.
- Predicción de demanda de productos.
- Mejora de la experiencia del cliente.
- Planeación de recursos y presupuestos.

### Importancia de las Bases de Datos en la Ciencia de Datos

Las bases de datos aportan múltiples beneficios dentro de los proyectos de análisis de datos:

- Centralizan la información proveniente de diversas fuentes.
- Garantizan la integridad y consistencia de los datos.
- Facilitan el acceso rápido a grandes volúmenes de información.
- Permiten realizar consultas complejas de manera eficiente.
- Favorecen la seguridad y el control de acceso a los datos.
- Soportan procesos de análisis avanzados y modelos predictivos.

#### Ejemplo Práctico

Una empresa de comercio electrónico registra diariamente miles de transacciones. Los datos de ventas, productos, clientes y pagos se almacenan en una base de datos. Posteriormente, estos datos son procesados y analizados para identificar:

- Los productos más vendidos.
- Los hábitos de compra de los clientes.
- Las temporadas de mayor demanda.
- Las recomendaciones personalizadas para cada usuario.

Con esta información, la empresa puede diseñar mejores estrategias comerciales y aumentar sus ingresos.

### ¿Qué ocurre cuando los datos no están organizados como una tabla?

No toda la información se encuentra organizada en filas y columnas como sucede en las bases de datos tradicionales. En la actualidad, una gran parte de los datos generados por personas y sistemas se presentan en formatos más flexibles, como documentos de texto, imágenes, videos, correos electrónicos, publicaciones en redes sociales, archivos multimedia y registros de actividad.

Cuando los datos no están organizados como una tabla, se consideran **datos no estructurados** o, en algunos casos, **datos semiestructurados**. Este tipo de información puede contener una gran cantidad de conocimientos valiosos, pero requiere técnicas y herramientas especializadas para su almacenamiento, procesamiento y análisis.

### ¿Por qué representa un desafío?

Los datos tabulares tienen una estructura claramente definida, donde cada registro ocupa una fila y cada atributo corresponde a una columna. Esto facilita su consulta y análisis.

Sin embargo, cuando los datos carecen de esta organización:

- Resulta más difícil localizar información específica.
- Su procesamiento requiere métodos más complejos.
- Pueden existir múltiples formatos y fuentes de datos.
- El volumen de información suele ser mucho mayor.
- Es necesario utilizar tecnologías avanzadas para extraer conocimiento útil.

### Tipos de datos no organizados en tablas

#### Documentos de texto

Incluyen archivos PDF, documentos de Word, reportes, artículos y libros digitales.

**Ejemplo:**

> "La empresa registró un incremento del 15% en sus ventas durante el último trimestre."

Aunque la información es valiosa, no está organizada en columnas específicas.

#### Correos electrónicos

Los correos contienen algunos campos estructurados (remitente, destinatario y asunto), pero el contenido principal suele ser libre.

#### Redes Sociales

Las publicaciones, comentarios, reacciones, imágenes, videos y mensajes generados diariamente en plataformas digitales representan enormes cantidades de información no estructurada. Cada interacción de los usuarios genera datos valiosos que pueden ser analizados para identificar tendencias, preferencias, comportamientos de consumo y opiniones sobre productos o servicios.

Entre las principales fuentes de este tipo de información se encuentran plataformas como:

- Facebook
- Instagram
- X (Twitter)
- TikTok
- YouTube
- LinkedIn

Debido a su volumen y diversidad, el análisis de los datos provenientes de redes sociales suele requerir herramientas especializadas de Big Data e Inteligencia Artificial.

##### Imágenes y Videos

Las fotografías y grabaciones contienen información visual que no puede analizarse directamente como una tabla de datos. Sin embargo, mediante técnicas avanzadas de procesamiento de imágenes y visión por computadora, es posible extraer información relevante para distintos propósitos.

#### Ejemplos

- Fotografías médicas.
- Cámaras de seguridad.
- Videos de tráfico.
- Imágenes satelitales.

Este tipo de datos se utiliza en áreas como la seguridad, la salud, la agricultura, la investigación científica y el transporte inteligente.

#### Registros de Sensores y Dispositivos Inteligentes

Los sistemas del **Internet de las Cosas (IoT)** generan datos de manera continua a través de sensores, dispositivos conectados y equipos inteligentes. Estos datos suelen provenir de múltiples fuentes y formatos, por lo que requieren procesamiento especializado antes de ser analizados.

#### Ejemplos

- Sensores de temperatura y humedad.
- Medidores inteligentes de energía eléctrica.
- Dispositivos GPS.
- Equipos industriales automatizados.
- Relojes y dispositivos inteligentes (smartwatches).

La información obtenida permite monitorear procesos, optimizar recursos y detectar anomalías en tiempo real.

---

#### ¿Cómo se gestionan estos datos?

Para trabajar con información no estructurada se utilizan tecnologías y técnicas avanzadas capaces de almacenar, procesar y analizar grandes volúmenes de datos provenientes de diversas fuentes.

Entre las más importantes se encuentran:

- **Inteligencia Artificial (IA):** permite identificar patrones y generar predicciones a partir de grandes conjuntos de datos.
- **Aprendizaje Automático (Machine Learning):** utiliza algoritmos capaces de aprender automáticamente a partir de los datos.
- **Procesamiento del Lenguaje Natural (NLP):** facilita la interpretación y análisis del lenguaje humano presente en textos y conversaciones.
- **Minería de textos:** extrae información útil de documentos, correos electrónicos, informes y publicaciones.
- **Reconocimiento de imágenes:** identifica objetos, personas, patrones o características dentro de fotografías y videos.
- **Sistemas Big Data:** permiten almacenar y procesar grandes cantidades de información de manera distribuida.
- **Bases de datos NoSQL:** ofrecen mayor flexibilidad para almacenar datos semiestructurados y no estructurados.

Estas tecnologías permiten transformar información compleja en datos analizables y útiles para la toma de decisiones.

#### Ejemplo Práctico

Supongamos que una empresa desea conocer la opinión de sus clientes sobre un nuevo producto lanzado al mercado.

En lugar de analizar únicamente una tabla de datos tradicional, recopila información proveniente de distintas fuentes:

- Comentarios en redes sociales.
- Correos electrónicos recibidos.
- Reseñas de clientes.
- Mensajes de atención al cliente.

Mediante técnicas de análisis de texto e Inteligencia Artificial, la empresa puede identificar:

- Opiniones positivas y negativas.
- Problemas frecuentes reportados por los usuarios.
- Preferencias y necesidades de los clientes.
- Tendencias de consumo y comportamiento.

Con esta información, la organización puede mejorar sus productos, desarrollar nuevas estrategias de marketing y ofrecer una mejor experiencia a sus clientes.

#### Importancia en la Ciencia de Datos

Actualmente, se estima que la mayor parte de la información generada a nivel mundial corresponde a datos no estructurados. Por esta razón, los científicos de datos deben emplear herramientas y metodologías capaces de procesar información que va más allá de las bases de datos tradicionales.

El análisis de estos datos permite:

- Descubrir patrones ocultos.
- Mejorar productos y servicios.
- Optimizar procesos organizacionales.
- Detectar riesgos y oportunidades.
- Comprender mejor el comportamiento de los usuarios.
- Apoyar la toma de decisiones estratégicas.

A medida que el volumen de información digital continúa creciendo, la capacidad de analizar datos no estructurados se convierte en una habilidad fundamental para las organizaciones modernas.

### Bases de Datos Semiestructuradas

En una **base de datos semiestructurada**, los datos no se encuentran organizados en filas y columnas fijas como ocurre en las bases de datos relacionales. En su lugar, la información se almacena mediante estructuras flexibles que permiten que cada registro tenga diferentes atributos según las necesidades de la aplicación.

#### Características

- No existe un esquema rígido de filas y columnas.
- Cada registro puede contener atributos diferentes.
- Los datos se organizan mediante etiquetas, pares clave-valor o documentos.
- Utilizan formatos como **JSON**, **XML** y otros similares.
- La estructura puede modificarse sin afectar a toda la base de datos.
- Facilitan el almacenamiento de información heterogénea y cambiante.
- Son ampliamente utilizadas en aplicaciones web, sistemas distribuidos y plataformas de Big Data.

#### Ejemplo

Un registro puede contener únicamente nombre y edad:

```json
{
  "nombre": "Ana",
  "edad": 25
}

### ¿Cómo se Relacionan los Temas?

Los diferentes conceptos estudiados en el ámbito de las bases de datos y la Ciencia de Datos están estrechamente conectados y forman parte de un ecosistema tecnológico que permite recopilar, almacenar, procesar y analizar información para generar conocimiento útil y apoyar la toma de decisiones.

#### XML y Datos Semiestructurados

Los formatos como **XML** y **JSON** surgieron como nuevas formas de representar información que no encaja fácilmente en tablas tradicionales.

#### Relación con otros temas

- Permiten almacenar datos con estructuras flexibles.
- Son ampliamente utilizados en servicios web y aplicaciones modernas.
- Facilitan el intercambio de información entre sistemas.
- Constituyen la base de muchas bases de datos NoSQL.

**Ejemplo:** Un documento XML puede almacenar diferentes atributos para cada registro sin necesidad de seguir una estructura fija.

---

### Computación en la Nube (Cloud Computing)

La **Nube** proporciona la infraestructura tecnológica necesaria para almacenar, administrar y procesar grandes cantidades de información de manera escalable.

#### Relación con otros temas

- Permite alojar bases de datos y aplicaciones de análisis de datos.
- Proporciona recursos bajo demanda para proyectos de Big Data.
- Facilita el acceso remoto a los datos desde cualquier lugar.
- Reduce costos de infraestructura física.

**Ejemplos de servicios en la nube:**

- Microsoft Azure
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

---

### Data Warehouse, OLAP y Data Mining

Estas tecnologías están orientadas al análisis de datos y la generación de conocimiento para apoyar la toma de decisiones.

#### Data Warehouse

Es un repositorio centralizado que integra información proveniente de múltiples fuentes.

**Funciones principales:**

- Consolidar información histórica.
- Facilitar consultas analíticas.
- Servir como base para la inteligencia de negocios.

#### OLAP (Online Analytical Processing)

Permite realizar análisis multidimensionales sobre grandes volúmenes de información.

**Beneficios:**

- Consultas rápidas.
- Análisis por regiones, periodos o categorías.
- Generación de reportes estratégicos.

#### Data Mining (Minería de Datos)

Aplica técnicas estadísticas y algoritmos para descubrir patrones ocultos en los datos.

**Aplicaciones comunes:**

- Predicción de ventas.
- Detección de fraudes.
- Segmentación de clientes.
- Identificación de tendencias.

#### Relación entre ellos

```text
Datos Operacionales
        ↓
   Data Warehouse
        ↓
       OLAP
        ↓
   Data Mining
        ↓
 Toma de Decisiones

### ¿Cómo Trabajaremos?

Durante el desarrollo del curso, se utilizará una metodología de aprendizaje dinámica y práctica que permitirá comprender los conceptos teóricos y aplicarlos en situaciones reales. El objetivo es fomentar la participación activa, el análisis crítico y el desarrollo de habilidades para resolver problemas relacionados con las bases de datos y la Ciencia de Datos.

#### Clases Presenciales

Las sesiones presenciales serán el espacio principal para la explicación de conceptos, resolución de dudas y desarrollo de actividades de aprendizaje.

#### Objetivos

- Comprender los fundamentos teóricos de cada tema.
- Interactuar directamente con el docente y compañeros.
- Resolver dudas de manera oportuna.
- Complementar el aprendizaje mediante ejemplos prácticos.

#### Análisis de Casos

Se estudiarán situaciones reales o simuladas que permitan comprender cómo se aplican los conceptos en diferentes contextos organizacionales.

#### Beneficios

- Desarrollar el pensamiento crítico.
- Identificar problemas y proponer soluciones.
- Relacionar la teoría con la práctica.
- Comprender la importancia de los datos en la toma de decisiones.

#### Ejemplos

- Análisis de ventas de una empresa.
- Gestión de información en hospitales.
- Sistemas bancarios y financieros.
- Comercio electrónico y marketing digital.

### Prácticas con Software y Herramientas

El aprendizaje se complementará mediante actividades prácticas utilizando aplicaciones y herramientas tecnológicas relacionadas con la gestión y análisis de datos.

#### Objetivos

- Familiarizarse con herramientas utilizadas en el entorno profesional.
- Aplicar los conceptos aprendidos en clase.
- Desarrollar habilidades técnicas para el manejo de datos.
- Comprender el funcionamiento de sistemas de bases de datos y análisis.

#### Actividades

- Creación de bases de datos.
- Gestión de información.
- Consultas y análisis de datos.
- Interpretación de resultados.
- Desarrollo de ejercicios prácticos.

#### Participación y Discusión

La participación activa de los estudiantes será fundamental para enriquecer el proceso de aprendizaje.

#### Formas de participación

- Preguntas durante las sesiones.
- Comentarios y aportaciones sobre los temas.
- Debates y discusiones grupales.
- Resolución colaborativa de problemas.
- Intercambio de experiencias y conocimientos.

La discusión de ideas permite fortalecer la comprensión de los conceptos y desarrollar habilidades de comunicación y trabajo en equipo.

#### Aplicación de los Conceptos a Situaciones Reales

Uno de los principales objetivos del curso es que los conocimientos adquiridos puedan aplicarse a problemas y necesidades del entorno real.

#### Aplicaciones

- Organización y administración de información.
- Análisis de datos para la toma de decisiones.
- Optimización de procesos.
- Solución de problemas empresariales.
- Desarrollo de proyectos basados en datos.

### Beneficios

- Mayor comprensión de los temas estudiados.
- Desarrollo de competencias profesionales.
- Preparación para enfrentar situaciones reales en el ámbito laboral.
- Capacidad para proponer soluciones basadas en información y evidencia.

### Metodología General

El aprendizaje se basará en una combinación de:

1. Exposición de conceptos teóricos.
2. Análisis de casos prácticos.
3. Uso de herramientas tecnológicas.
4. Participación activa de los estudiantes.
5. Aplicación de conocimientos a contextos reales.

### Proyecto Final

- Integrar los conocimientos adquiridos durante la materia.
- Explorar una solución basada en tecnologías de **Nube**, **Big Data** o **NoSQL**.
- Analizar el problema planteado y seleccionar las tecnologías más adecuadas para resolverlo.
- Desarrollar una solución funcional y una interfaz de visualización de datos.
- Justificar técnicamente las decisiones tomadas durante el diseño e implementación del proyecto.

#### Análisis de Redes Sociales (Ideal para Ciencia de Datos)

#### Datos

Para desarrollar un proyecto de análisis de redes sociales, se pueden recopilar distintos tipos de información generada por los usuarios:

- Publicaciones.
- Likes o reacciones.
- Comentarios.
- Usuarios.

Estos datos permiten conocer el comportamiento de la comunidad, medir niveles de interacción y detectar patrones de uso dentro de la plataforma.

#### Análisis

A partir de los datos recopilados, es posible realizar diversos análisis, tales como:

- Identificar las publicaciones más populares.
- Determinar los horarios con mayor interacción de los usuarios.
- Realizar análisis de sentimiento básico sobre los comentarios.
- Medir el nivel de participación de los usuarios.
- Detectar tendencias y temas de interés.
- Comparar el alcance e impacto de diferentes publicaciones.

#### Beneficios

- Comprender mejor el comportamiento de los usuarios.
- Mejorar estrategias de contenido y comunicación.
- Identificar tendencias relevantes.
- Apoyar la toma de decisiones basada en datos.
- Evaluar el impacto de campañas y publicaciones.

#### Herramientas Sugeridas

- Python
- Pandas
- Power BI
- Tableau
- MongoDB
- Apache Spark

#### Resultados Esperados

Como producto final, se puede desarrollar un tablero de visualización que muestre indicadores clave, tales como:

- Publicaciones con más interacción.
- Distribución de comentarios.
- Actividad por horario o día.
- Tendencias de participación.
- Resultados del análisis de sentimiento.

Este tipo de proyecto integra conceptos de bases de datos, análisis de datos, visualización de información y Ciencia de Datos, convirtiéndose en una excelente opción para aplicar los conocimientos adquiridos durante el curso.

### Criterios de Evaluación

La calificación final de la asignatura estará compuesta por los siguientes elementos:

- **Examen Final:** 25%
- **Controles de Lectura:** 25%
- **Presentación de Lectura:** 50%
- **Asistencia:** requisito para el seguimiento adecuado de las actividades y el cumplimiento de los objetivos del curso.

#### Distribución de la Calificación

| Actividad | Porcentaje |
|------------|------------|
| Examen Final | 25% |
| Controles de Lectura | 25% |
| Presentación de Lectura | 50% |

#### Consideraciones

- El **Examen Final** evaluará la comprensión e integración de los conceptos estudiados durante el curso.
- Los **Controles de Lectura** permitirán verificar el análisis y comprensión de los materiales asignados.
- La **Presentación de Lectura** consistirá en la exposición y discusión de temas seleccionados, representando el componente de mayor peso en la evaluación final.
- La **Asistencia** y participación activa contribuirán al aprovechamiento de las actividades desarrolladas en clase.

**Total de la calificación:** 100%



