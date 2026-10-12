# Diccionario de datos — Proyecto NoSQL SeizeIT2

## 1. Fuente de datos

**Nombre:** SeizeIT2  
**Repositorio:** [OpenNeuro — ds005873](https://openneuro.org/datasets/ds005873)  
**DOI:** 10.18112/openneuro.ds005873.v1.1.0  
**Formato de origen:** archivos TSV y JSON para metadatos y anotaciones, y EDF para señales fisiológicas.  
**Base de datos destino:** MongoDB.  
**Nombre de la base de datos:** `seizeit2`.

SeizeIT2 es un conjunto de datos de investigación que contiene registros fisiológicos de personas con epilepsia. Para este proyecto se consideran las modalidades EEG, ECG, EMG y movimiento, así como los datos de participantes y las anotaciones de eventos.

## 2. Diccionario de participantes

| Campo | Tipo de dato | Descripción | Regla de validación |
|---|---|---|---|
| `participant_id` | String | Identificador único del participante. | No debe estar vacío y debe ser único. |
| `sex` | String | Sexo registrado en la fuente. | Se validan los valores permitidos por el conjunto de datos: `m` y `f`. |

## 3. Diccionario de grabaciones

| Campo | Tipo de dato | Descripción | Regla de validación |
|---|---|---|---|
| `participant_id` | String | Identificador del participante asociado a la grabación. | Debe corresponder a un participante existente. |
| `session_id` | String | Identificador de la sesión. | Se obtiene del nombre real del archivo o de la estructura del conjunto de datos. |
| `modality` | String | Modalidad registrada: EEG, ECG, EMG o MOV. | Debe corresponder a una modalidad identificada en los archivos. |
| `SamplingFrequency` | Number | Frecuencia de muestreo, expresada en Hz. | Debe ser positiva. |
| `channel_count` | Integer | Número de canales declarados para la modalidad. | Debe ser un entero positivo. |
| `RecordingType` | String | Tipo de registro, por ejemplo, discontinuo. | Debe conservar el valor de la fuente. |
| `RecordingDuration` | Number | Duración declarada de la grabación, en segundos. | Debe ser positiva cuando esté disponible. |
| `PlacementScheme` | String | Descripción de la ubicación de los electrodos o del dispositivo. | Puede estar ausente o contener un valor no disponible. |
| `TaskName` | String | Nombre de la tarea de monitoreo. | Se conserva el valor original. |
| `TaskDescription` | String | Descripción de la tarea registrada. | Se conserva el valor original. |
| `InstitutionName` | String | Contexto institucional declarado en los metadatos. | Se conserva el valor original. |

Los campos originales específicos de cada modalidad, como `EEGChannelCount` y `ECGChannelCount`, se transformarán a una estructura uniforme durante la preparación de datos, conservando su correspondencia con la fuente.

## 4. Diccionario de anotaciones de eventos

| Campo | Tipo de dato | Descripción | Regla de validación |
|---|---|---|---|
| `participant_id` | String | Identificador del participante. | Debe corresponder a un participante existente. |
| `recording_id` | String | Identificador de la grabación asociada. | Debe identificar la grabación de origen. |
| `onset` | Number | Tiempo de inicio del evento desde el comienzo de la grabación, en segundos. | Debe ser mayor o igual a cero. |
| `duration` | Number | Duración del evento, en segundos. | Debe ser mayor o igual a cero. |
| `eventType` | String | Tipo de evento anotado en la fuente. | Se conservan las categorías originales. |
| `lateralization` | String | Lateralización del evento, cuando aplica. | Se conserva el valor original. |
| `localization` | String | Localización asociada al evento, cuando aplica. | Se conserva el valor original. |
| `vigilance` | String | Estado de vigilia registrado. | Se conserva el valor original. |
| `confidence` | Number | Nivel de confianza de la anotación, cuando está disponible. | Si existe, debe estar entre 0 y 1. |
| `channels` | String | Canales asociados al evento, cuando se especifican. | Se conserva el contenido original. |
| `dateTime` | String | Fecha y hora de referencia registradas en el archivo. | Se conserva el valor original hasta confirmar su interpretación. |
| `recordingDuration` | Number | Duración declarada de la grabación, en segundos. | Debe ser positiva cuando esté disponible. |

## 5. Reglas generales de limpieza

1. Eliminar espacios innecesarios en los campos de texto.
2. Identificar registros duplicados mediante sus identificadores o una combinación de campos que permita reconocerlos.
3. Rechazar o separar registros sin identificadores esenciales.
4. Convertir los tiempos, las frecuencias y las duraciones a tipos numéricos.
5. Tratar los valores `n/a` como valores no disponibles o no aplicables, según el campo; nunca convertirlos automáticamente en cero.
6. Validar que los tiempos de inicio y las duraciones no sean negativos.
7. Conservar las categorías originales de los eventos para evitar perder información.
8. Registrar los problemas detectados durante la limpieza.

## 6. Modelo de almacenamiento NoSQL

Se proponen tres colecciones en MongoDB:

- `participantes`: información básica de cada participante.
- `grabaciones`: metadatos técnicos de las grabaciones y sus modalidades.
- `eventos`: anotaciones vinculadas con su participante y grabación.

Los archivos EDF originales se conservarán fuera de MongoDB. La base almacenará sus metadatos y referencias, evitando incorporar directamente grandes volúmenes de muestras fisiológicas crudas.

## 7. Alcance y limitaciones

El proyecto se enfoca en el diseño, preparación y carga inicial de datos en una base NoSQL. No pretende demostrar en esta etapa que sea posible predecir crisis epilépticas ni construir un sistema de alertas.

Las reglas y los tipos descritos se verificarán durante la implementación con los archivos reales. Los valores ausentes y las diferencias entre modalidades se documentarán antes de su carga definitiva.