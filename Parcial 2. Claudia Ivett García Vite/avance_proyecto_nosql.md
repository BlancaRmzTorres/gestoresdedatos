# Diseño y Preparación de Datos NoSQL
## Del dato crudo a una base de datos lista para el análisis

**Materia:** Bases de Datos para Ciencia de Datos  
**Profesora:** Blanca Esthela Torres Ramírez  
**Alumna:** Claudia Ivett García Vite  
**Programa:** Maestría en Ciencia de Datos  
**Fecha:** Octubre de 2026  

---

## 1. Introducción y descripción de la fuente de datos

El presente proyecto tiene como finalidad trabajar con una fuente de datos real relacionada con el registro de señales fisiológicas de personas con epilepsia, con el propósito de aplicar los conocimientos adquiridos en la materia de Bases de Datos para Ciencia de Datos. El trabajo se centra en el diseño y la preparación de los datos para almacenarlos en una base de datos NoSQL, de manera que puedan organizarse y consultarse posteriormente para realizar análisis.

La fuente seleccionada es **SeizeIT2**, un conjunto de datos disponible en la plataforma OpenNeuro. Este conjunto forma parte de un estudio multicéntrico realizado en unidades de monitoreo de epilepsia de Europa. Incluye información de 125 personas con epilepsia focal que fueron sometidas a monitoreo durante su evaluación clínica. Los registros fueron obtenidos entre enero de 2020 y junio de 2022.

La información se encuentra organizada siguiendo la estructura BIDS, un estándar que permite ordenar y describir datos relacionados con estudios de neuroimagen y registros neurofisiológicos. El conjunto contiene archivos con señales fisiológicas, archivos de anotaciones y archivos de metadatos que describen las características de los registros y de los participantes.

La fuente principal de consulta es OpenNeuro:

- **Nombre del conjunto de datos:** SeizeIT2.
- **Identificador:** `ds005873`.
- **Versión consultada:** `1.1.0`.
- **DOI:** `10.18112/openneuro.ds005873.v1.1.0`.
- **Licencia declarada:** CC0.
- **Formato de organización:** BIDS 1.8.0.
- **Enlace:** https://openneuro.org/datasets/ds005873

También se consultó el artículo científico asociado al conjunto de datos, publicado en la revista *Scientific Data*, para conocer el contexto de su recopilación y las características generales de la información:

https://www.nature.com/articles/s41597-025-05580-x

### 1.1 ¿Qué información contiene el conjunto de datos?

SeizeIT2 incluye registros fisiológicos obtenidos mediante dispositivos de monitoreo que registran diferentes tipos de señales de manera simultánea. Entre las modalidades disponibles se encuentran:

- **EEG (electroencefalografía):** registra la actividad eléctrica cerebral. En los archivos revisados del participante `sub-001`, la frecuencia de muestreo declarada es de 256 Hz y se indican dos canales.
- **ECG (electrocardiografía):** registra la actividad eléctrica del corazón. En los metadatos revisados se declara una frecuencia de muestreo de 256 Hz y un canal, mediante electrodos colocados en el pecho.
- **EMG (electromiografía):** registra la actividad eléctrica de los músculos. En el ejemplo revisado se declara una frecuencia de muestreo de 256 Hz y un canal, con electrodos colocados en el músculo deltoides izquierdo.
- **MOV (movimiento):** contiene información relacionada con el movimiento corporal, obtenida mediante sensores de movimiento. En los metadatos del participante revisado se declara una frecuencia de muestreo de 25 Hz y 12 canales.

Estos valores corresponden a los metadatos del participante `sub-001` y sirven como ejemplo de la información técnica disponible. Para describir los demás registros deben consultarse sus propios metadatos, sin asumir que todos tienen exactamente las mismas características.

Los archivos de señales se almacenan principalmente en formato EDF, mientras que los archivos JSON contienen información descriptiva sobre las grabaciones y los archivos TSV almacenan tablas de datos y anotaciones.

### 1.2 ¿Qué significan los eventos del conjunto de datos?

Además de las señales fisiológicas, el conjunto contiene archivos de anotaciones denominados `events.tsv`. Estos archivos describen eventos registrados durante el monitoreo e incluyen campos como el tiempo de inicio, la duración, el tipo de evento, la lateralización, la localización, el estado de vigilancia y la confianza de la anotación.

Es importante aclarar que **no todos los eventos representan una crisis epiléptica**. Por ejemplo, en el archivo de eventos revisado para `sub-001` aparecen registros con el tipo `impd`, que corresponde a una comprobación de impedancia. Este tipo de anotación se relaciona con una revisión técnica del registro y no debe interpretarse como una crisis epiléptica.

En los metadatos también se describen categorías relacionadas con crisis focales, como `sz_foc` y otras variantes. La interpretación de cada categoría debe basarse en la documentación del conjunto de datos.

Por lo tanto, los eventos son anotaciones que ayudan a describir lo que se identificó durante el monitoreo. Su inclusión en la base de datos permitirá conservar la relación entre las grabaciones y los eventos registrados, sin asumir que todas las anotaciones tienen el mismo significado clínico.

### 1.3 Justificación de la elección de MongoDB

El conjunto de datos presenta diferentes tipos de información: participantes, características técnicas de las grabaciones, modalidades fisiológicas y anotaciones de eventos. Estos elementos tienen estructuras y atributos distintos, por lo que una base de datos documental como MongoDB resulta apropiada para organizar los metadatos mediante documentos flexibles.

MongoDB permite representar atributos relacionados dentro de un mismo documento, utilizar estructuras anidadas y establecer relaciones mediante identificadores. Además, facilita incorporar nuevas propiedades cuando sea necesario, sin exigir que todos los documentos tengan exactamente los mismos campos.

Debido al tamaño del conjunto completo, que es de aproximadamente 117 GB, el proyecto no contempla descargar ni procesar todos los archivos de señales en esta etapa. El avance se concentra en los metadatos y en una primera carga de los participantes. La integración de las grabaciones y de las anotaciones se plantea como una etapa posterior.

---

## 2. Objetivo del proyecto

Diseñar y preparar una estructura de base de datos NoSQL para organizar los metadatos del conjunto de datos SeizeIT2, mediante la identificación de sus entidades, la elaboración de un diccionario de datos, la definición de un modelo documental, la limpieza de los registros de participantes y su carga inicial en MongoDB, con la finalidad de disponer de información estructurada y consultable para futuros análisis.

### 2.1 Alcance

El proyecto comprende la revisión de la documentación disponible, la identificación de los principales tipos de información, la definición de las colecciones propuestas, la validación y limpieza de los datos de participantes, y su almacenamiento en MongoDB.

En esta etapa, la colección `participantes` se encuentra implementada y contiene 125 registros. Las colecciones `grabaciones` y `eventos` forman parte del modelo propuesto, pero todavía requieren la extracción, preparación y carga de sus respectivos registros.

El proyecto se enfoca en preparar y organizar los datos. No contempla desarrollar un modelo de aprendizaje automático, predecir crisis epilépticas ni construir un sistema de alertas.

---

## 3. Diccionario de datos

El diccionario de datos permite identificar los campos que integran la información, describir su significado y establecer las reglas que deben respetarse durante su preparación y almacenamiento.

Para este proyecto se consideran tres entidades principales: participantes, grabaciones y eventos.

### 3.1 Entidad: participantes

Esta entidad contiene información básica de cada participante identificado en el conjunto de datos.

| Campo | Tipo de dato | Descripción | Regla de validación |
|---|---|---|---|
| `participant_id` | Cadena de texto | Identificador único del participante. Ejemplo: `sub-001`. | Debe iniciar con `sub-` y continuar con dígitos. No debe repetirse. |
| `sex` | Cadena de texto | Sexo registrado en los metadatos del participante. | En el archivo revisado se utilizan los valores `m` y `f`. |

Esta entidad se alimenta del archivo `participants.txt`. Para la carga en MongoDB se conserva el identificador como una cadena de texto, ya que forma parte de la identificación del participante y no de una operación numérica.

### 3.2 Entidad: grabaciones

Esta entidad se propone para almacenar los metadatos técnicos de cada grabación y relacionarlos con el participante correspondiente.

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `recording_id` | Cadena de texto | Identificador de la grabación. Debe definirse a partir de los nombres reales de los archivos. |
| `participant_id` | Cadena de texto | Identificador del participante al que corresponde la grabación. |
| `task` | Cadena de texto | Nombre de la tarea o contexto del registro, por ejemplo, `szMonitoring`. |
| `modalities` | Documento anidado | Agrupa los metadatos de las modalidades disponibles. |
| `modalities.EEG.sampling_frequency` | Número | Frecuencia de muestreo declarada para EEG. |
| `modalities.EEG.channel_count` | Número entero | Número de canales EEG declarados. |
| `modalities.ECG.sampling_frequency` | Número | Frecuencia de muestreo declarada para ECG. |
| `modalities.ECG.channel_count` | Número entero | Número de canales ECG declarados. |
| `modalities.EMG.sampling_frequency` | Número | Frecuencia de muestreo declarada para EMG. |
| `modalities.EMG.channel_count` | Número entero | Número de canales EMG declarados. |
| `modalities.MOV.sampling_frequency` | Número | Frecuencia de muestreo declarada para movimiento. |
| `modalities.MOV.channel_count` | Número entero | Número de canales de movimiento declarados. |
| `recording_duration` | Número | Duración declarada de la grabación, en segundos. |
| `recording_type` | Cadena de texto | Tipo de registro descrito en los metadatos. |

Los campos anteriores constituyen una propuesta de estructura. Antes de cargarlos deben verificarse los nombres de los archivos y los metadatos reales, así como la disponibilidad de cada modalidad.

### 3.3 Entidad: eventos

Esta entidad se propone para almacenar las anotaciones asociadas con las grabaciones.

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `event_id` | Cadena de texto | Identificador interno propuesto para cada anotación. |
| `participant_id` | Cadena de texto | Identificador del participante relacionado con el evento. |
| `recording_id` | Cadena de texto | Identificador de la grabación a la que pertenece el evento. |
| `onset` | Número | Tiempo de inicio del evento respecto al comienzo de la grabación, en segundos. |
| `duration` | Número | Duración del evento, en segundos. |
| `eventType` | Cadena de texto | Categoría de la anotación, por ejemplo, `impd` o alguna categoría de crisis focal. |
| `lateralization` | Cadena de texto | Lateralización indicada en la anotación, cuando corresponda. |
| `localization` | Cadena de texto | Localización descrita en la anotación, cuando corresponda. |
| `vigilance` | Cadena de texto | Estado de vigilancia registrado, cuando corresponda. |
| `confidence` | Número | Valor de confianza de la anotación, cuando esté disponible. |
| `dateTime` | Cadena de texto o fecha | Fecha y hora declaradas en los metadatos del evento. |
| `recordingDuration` | Número | Duración de la grabación declarada en los metadatos, en segundos. |
| `channels` | Cadena de texto | Información de canales asociada con la anotación, cuando esté disponible. |

La estructura deberá respetar los nombres y valores presentes en los archivos originales. Si un campo no está disponible, se debe distinguir entre un dato ausente y un valor explícito como `n/a`, según las reglas que se definan para la preparación.

---

## 4. Modelo de datos NoSQL

Para organizar la información se propone un modelo documental en MongoDB con tres colecciones principales: `participantes`, `grabaciones` y `eventos`.

La separación de las entidades permite conservar los datos básicos de cada participante, almacenar los metadatos técnicos de las grabaciones y representar las anotaciones registradas durante el monitoreo. Las colecciones pueden relacionarse mediante los campos `participant_id` y `recording_id`.

### 4.1 Colección `participantes`

Almacena un documento por participante.

Ejemplo de documento:

```json
{
  "participant_id": "sub-001",
  "sex": "f"
}
```

Este ejemplo ilustra la estructura del documento; el valor de `sex` debe corresponder al registro real del participante. La colección ya se encuentra implementada y contiene 125 participantes.

### 4.2 Colección `grabaciones`

Almacena los metadatos técnicos de cada grabación. Las características de las modalidades se agrupan en un documento anidado para mantener relacionada la información de cada tipo de señal.

Ejemplo ilustrativo de la estructura propuesta:

```json
{
  "recording_id": "identificador_por_verificar",
  "participant_id": "sub-001",
  "task": "szMonitoring",
  "modalities": {
    "EEG": {
      "sampling_frequency": 256,
      "channel_count": 2
    },
    "ECG": {
      "sampling_frequency": 256,
      "channel_count": 1
    },
    "EMG": {
      "sampling_frequency": 256,
      "channel_count": 1
    },
    "MOV": {
      "sampling_frequency": 25,
      "channel_count": 12
    }
  },
  "recording_duration": 65319.0,
  "recording_type": "discontinuous"
}
```

Los valores técnicos del ejemplo corresponden a los metadatos revisados para `sub-001`. El campo `recording_id` es un marcador ilustrativo y deberá sustituirse por un identificador construido a partir de los archivos reales. Este documento no representa una grabación ya cargada en MongoDB.

### 4.3 Colección `eventos`

Almacena las anotaciones y mantiene la referencia a la grabación y al participante correspondientes.

Ejemplo ilustrativo basado en el tipo de evento observado en el archivo revisado:

```json
{
  "event_id": "identificador_por_generar",
  "participant_id": "sub-001",
  "recording_id": "identificador_por_verificar",
  "onset": 14080.0,
  "duration": 84.0,
  "eventType": "impd",
  "lateralization": "n/a",
  "localization": "n/a",
  "vigilance": "n/a",
  "confidence": "n/a"
}
```

Este ejemplo representa una anotación `impd` encontrada en el archivo de eventos de `sub-001`. No corresponde a una crisis epiléptica y no debe interpretarse como tal. Los identificadores internos se deberán generar cuando se implemente la carga de eventos. El tipo de dato definitivo de los campos que contienen `n/a` deberá establecerse de manera consistente con la información original y las reglas de limpieza.

### 4.4 Relaciones entre las colecciones

La relación lógica propuesta es la siguiente:

- Un participante puede tener una o más grabaciones.
- Una grabación pertenece a un participante.
- Una grabación puede tener múltiples anotaciones de eventos.
- Cada evento debe poder vincularse con su grabación y, mediante ella, con el participante correspondiente.

La relación entre las colecciones se establece mediante identificadores, sin necesidad de incorporar todos los datos de una entidad dentro de cada documento de las demás colecciones.

### 4.5 Índices propuestos

Para mejorar las consultas se proponen los siguientes índices:

| Colección | Campo | Finalidad |
|---|---|---|
| `participantes` | `participant_id` | Garantizar la unicidad e identificar a cada participante. |
| `grabaciones` | `participant_id` | Consultar las grabaciones asociadas con un participante. |
| `grabaciones` | `recording_id` | Identificar de manera única cada grabación. |
| `eventos` | `recording_id` | Consultar las anotaciones asociadas con una grabación. |
| `eventos` | `participant_id` | Consultar las anotaciones de un participante. |
| `eventos` | `eventType` | Filtrar las anotaciones por categoría. |

En el estado actual, el índice único de `participant_id` ya se implementó en la colección `participantes`. Los demás índices quedan sujetos a la implementación de las colecciones correspondientes.

---

## 5. Limpieza y preparación de los datos

La preparación de los datos se realiza antes de incorporarlos a la base de datos, con la finalidad de detectar errores de formato, valores faltantes, identificadores incorrectos y registros duplicados.

En esta primera etapa se trabajó con el archivo `participants.txt`, que contiene la identificación de los participantes y el campo `sex`.

### 5.1 Datos originales

El archivo original se encuentra en:

`datos/originales/participants.txt`

El archivo contiene dos columnas principales:

- `participant_id`
- `sex`

El archivo se interpreta como una tabla delimitada por tabuladores, aunque tenga extensión `.txt`.

### 5.2 Reglas de limpieza aplicadas

El script `preparar_participantes.py` realiza las siguientes validaciones:

1. **Identificador del participante:** comprueba que el valor comience con `sub-` y continúe con dígitos.
2. **Sexo registrado:** valida que el campo contenga uno de los valores esperados en el archivo, `m` o `f`.
3. **Campos vacíos:** identifica los registros con campos obligatorios sin información.
4. **Duplicados:** revisa si existen identificadores repetidos.
5. **Separación de resultados:** genera un archivo con los registros válidos y un informe con el resultado de las revisiones.

Estas reglas permiten detectar problemas de estructura y consistencia. No modifican las características clínicas de los participantes ni realizan interpretaciones médicas.

### 5.3 Archivos generados

El proceso produce los siguientes archivos:

- `datos/procesados/participantes_limpios.tsv`: contiene los registros que cumplen las validaciones establecidas.
- `datos/procesados/informe_limpieza_participantes.txt`: contiene el resumen de los resultados de la limpieza.

El archivo original se conserva en `datos/originales/` para mantener la trazabilidad entre la fuente y los datos preparados.

### 5.4 Resultados de la limpieza

Al ejecutar el script se obtuvieron los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Filas revisadas | 125 |
| Registros válidos | 125 |
| Registros con incidencias | 0 |

Los resultados indican que los 125 registros revisados cumplieron las reglas de validación implementadas. No se detectaron incidencias de acuerdo con dichas reglas.

Este resultado no significa que todos los archivos del conjunto de datos estén libres de errores. La revisión se limita al archivo de participantes y a las validaciones programadas.

---

## 6. Carga inicial en MongoDB

Después de la limpieza, los participantes se incorporaron a MongoDB mediante el script `cargar_participantes.py`.

La conexión local se realiza mediante la dirección:

`mongodb://localhost:27017`

La base de datos utilizada se llama `seizeit2` y la colección implementada para esta etapa es `participantes`.

### 6.1 Proceso de carga

El script realiza las siguientes acciones:

1. Establece la conexión con MongoDB.
2. Selecciona la base de datos `seizeit2`.
3. Selecciona la colección `participantes`.
4. Crea un índice único sobre el campo `participant_id`.
5. Lee el archivo limpio `participantes_limpios.tsv`.
6. Inserta o actualiza los documentos según su identificador.
7. Consulta el total de documentos almacenados en la colección.

Para evitar la duplicación de participantes, la carga utiliza una operación de actualización o inserción basada en `participant_id`. Si el identificador ya existe, se actualizan sus datos; si no existe, se crea el documento.

### 6.2 Resultado de la carga

La ejecución del script produjo el siguiente resultado:

| Indicador | Resultado |
|---|---:|
| Registros revisados | 125 |
| Participantes nuevos | 0 |
| Participantes actualizados | 0 |
| Total de participantes en MongoDB | 125 |

El resultado es consistente con una carga que ya se había realizado previamente. Como los 125 participantes existían en la colección y no fue necesario modificarlos, no se insertaron nuevos documentos ni se actualizaron registros. El total se mantuvo en 125.

La operación permite comprobar que la colección conserva los participantes sin duplicarlos al volver a ejecutar el proceso.

### 6.3 Estado de implementación

| Elemento | Estado |
|---|---|
| Instalación y conexión con MongoDB | Implementado y probado |
| Base de datos `seizeit2` | Creada y utilizada |
| Colección `participantes` | Implementada |
| Índice único por participante | Implementado |
| Limpieza de participantes | Ejecutada |
| Carga de participantes | Ejecutada |
| Colección `grabaciones` | Propuesta; pendiente de implementación |
| Colección `eventos` | Propuesta; pendiente de implementación |
| Carga de metadatos de grabaciones | Pendiente |
| Carga de anotaciones de eventos | Pendiente |

---

## 7. Scripts desarrollados

El código del proyecto se organiza en la carpeta `scripts/`. Cada archivo cumple una función específica dentro del proceso de preparación y almacenamiento de los datos.

| Script | Función | Estado |
|---|---|---|
| `probar_conexion.py` | Comprueba la conexión con MongoDB y permite revisar las colecciones disponibles. | Ejecutado |
| `revisar_metadatos.py` | Lee archivos JSON para revisar los metadatos del conjunto de datos. | Desarrollado |
| `preparar_participantes.py` | Valida los identificadores y los campos de participantes; genera el archivo limpio y el informe de limpieza. | Ejecutado |
| `cargar_participantes.py` | Lee los datos preparados y realiza la carga o actualización de documentos en MongoDB. | Ejecutado |

La separación de las funciones en scripts independientes facilita revisar el proceso, detectar errores y repetir las operaciones cuando se actualicen los archivos preparados.

### 7.1 Organización del proyecto

La estructura de carpetas utilizada es la siguiente:

```text
Proyecto_NoSQL_Epilepsia/
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
│   ├── diccionario_datos.md
│   └── modelo_nosql.md
├── scripts/
│   ├── probar_conexion.py
│   ├── revisar_metadatos.py
│   ├── preparar_participantes.py
│   └── cargar_participantes.py
└── README.md
```

Esta estructura separa los datos originales de los datos procesados, el código fuente y la documentación. De esta manera, se conserva una organización clara y se evita mezclar los archivos descargados con los resultados generados durante la limpieza.

---

## 8. Consideraciones y limitaciones

Durante el desarrollo se identificaron aspectos que deben tenerse en cuenta para continuar con el proyecto.

**Tamaño del conjunto de datos.** SeizeIT2 ocupa aproximadamente 117 GB. Por esta razón, la etapa inicial se concentra en los metadatos y no requiere descargar todas las señales fisiológicas.

**Diferencias entre metadatos y señales.** Los archivos JSON describen características técnicas como la frecuencia de muestreo, el número de canales y la duración declarada. Sin embargo, esos valores no garantizan por sí solos que todas las muestras estén disponibles o que el registro sea continuo. Para verificar la integridad de las señales sería necesario inspeccionar los archivos EDF.

**Diferencias entre modalidades.** Las frecuencias de muestreo y el número de canales pueden variar según la modalidad y el registro. Por ello, deben obtenerse de los metadatos correspondientes en lugar de asignarse valores generales a todos los participantes.

**Significado de las anotaciones.** Los eventos incluyen distintas categorías y no todos representan crisis epilépticas. La preparación debe conservar la categoría original y evitar interpretaciones que no estén respaldadas por la documentación.

**Datos ausentes.** Los valores vacíos y las expresiones como `n/a` deben tratarse de forma consistente. Antes de convertirlos a valores nulos o cambiar sus tipos de datos, será necesario establecer reglas que respeten el significado de los archivos originales.

**Alcance de la limpieza.** Los resultados actuales corresponden únicamente al archivo de participantes. No se ha validado todavía la totalidad de los metadatos de grabaciones ni de los eventos.

**Alcance geográfico y poblacional.** El conjunto procede de centros europeos y de personas con epilepsia focal sometidas a monitoreo clínico. Por lo tanto, no debe considerarse automáticamente representativo de todas las personas con epilepsia ni de la población mexicana.

**Alcance del proyecto.** El objetivo actual es estructurar y preparar los datos. La detección anticipada de crisis epilépticas y el desarrollo de modelos predictivos quedan fuera de esta primera etapa.

---

## 9. Actividades pendientes

Para completar el proyecto de acuerdo con su objetivo, se propone continuar con las siguientes actividades:

1. Revisar la estructura de los metadatos de las grabaciones y determinar cómo identificar cada registro mediante sus nombres de archivo reales.
2. Implementar la colección `grabaciones` y cargar un conjunto inicial de metadatos verificados.
3. Leer y preparar las filas de los archivos `events.tsv`, conservando los tipos de eventos y los valores originales relevantes.
4. Implementar la colección `eventos` y relacionar cada anotación con su grabación y participante.
5. Definir y probar los índices correspondientes a las nuevas colecciones.
6. Realizar consultas de prueba para verificar que la información se encuentre relacionada correctamente.
7. Actualizar el diccionario de datos con los campos y tipos definitivos observados durante la carga.
8. Documentar los resultados de las pruebas y actualizar el `README.md` con los pasos necesarios para ejecutar los scripts.

Estas actividades permitirán ampliar la base de datos de forma gradual y verificar cada etapa antes de incorporar más información.

---

## 10. Conclusión

El avance del proyecto permitió seleccionar una fuente de datos científica relacionada con el monitoreo fisiológico de personas con epilepsia, revisar su documentación y establecer una primera propuesta de organización mediante una base de datos NoSQL.

Se elaboró un diccionario de datos con las entidades principales, se propuso un modelo documental para participantes, grabaciones y eventos, y se desarrollaron scripts para revisar metadatos, limpiar registros y establecer la conexión con MongoDB. Como resultado de la primera etapa de preparación, los 125 registros de participantes cumplieron las validaciones implementadas y se encuentran almacenados en la colección `participantes` de la base de datos `seizeit2`.

Este avance demuestra que es posible transformar una tabla original en documentos estructurados y realizar una carga inicial sin duplicar los registros existentes. Sin embargo, el proyecto todavía requiere implementar y probar las colecciones de grabaciones y eventos para completar la estructura propuesta.

En conclusión, el trabajo constituye una primera etapa de organización y preparación de los datos. Contar con información documentada, validada y almacenada de manera consistente facilitará su consulta y permitirá ampliar la base de datos en futuras etapas, manteniendo la distinción entre los datos originales, los metadatos y las anotaciones del estudio.

---

## 11. Referencias

OpenNeuro. (s. f.). *SeizeIT2* (Dataset ds005873, versión 1.1.0). https://openneuro.org/datasets/ds005873

*Scientific Data*. (2025). *Artículo científico asociado al conjunto de datos SeizeIT2*. https://www.nature.com/articles/s41597-025-05580-x

MongoDB. (s. f.). *MongoDB Manual*. https://www.mongodb.com/docs/manual/

MongoDB. (s. f.). *PyMongo documentation*. https://www.mongodb.com/docs/languages/python/pymongo-driver/current/

---

**Nota sobre el avance:** La colección `participantes` es la parte implementada y comprobada hasta el momento. Las colecciones `grabaciones` y `eventos`, sus ejemplos de documentos y sus índices se presentan como diseño propuesto, y deberán verificarse y desarrollarse antes de considerarlos terminados.