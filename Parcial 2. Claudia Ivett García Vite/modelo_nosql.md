# Diseño del modelo NoSQL — SeizeIT2

## 1. Objetivo del modelo

Diseñar una estructura flexible en MongoDB para almacenar la información de los participantes, los metadatos de las grabaciones y las anotaciones de eventos del conjunto de datos SeizeIT2.

El modelo permitirá consultar los registros por participante, modalidad y tiempo del evento, y servirá como base para preparar posteriormente los datos destinados al análisis.

## 2. Tipo de base de datos

Se utilizará MongoDB, un sistema de gestión de bases de datos NoSQL orientado a documentos. La información se almacenará en documentos con estructura JSON/BSON, organizados en colecciones.

**Base de datos:** `seizeit2`

## 3. Colecciones propuestas

### 3.1. Colección `participantes`

Contendrá un documento por participante.

Ejemplo ilustrativo:

```json
{
  "participant_id": "sub-001",
  "sex": "f"
}
```

El sexo mostrado es únicamente un ejemplo de estructura; el valor definitivo debe corresponder al archivo de origen.

**Clave de identificación:** `participant_id`.

Se establecerá un índice único para evitar que un mismo participante se registre más de una vez.

### 3.2. Colección `grabaciones`

Contendrá los metadatos técnicos de las grabaciones. Las modalidades se organizarán dentro de un documento para facilitar su consulta.

Ejemplo ilustrativo:

```json
{
  "recording_id": "sub-001_ses-01_task-szMonitoring_run-01",
  "participant_id": "sub-001",
  "task": "szMonitoring",
  "modalities": {
    "ECG": {
      "sampling_frequency": 256,
      "channel_count": 1,
      "recording_duration_seconds": 65319
    },
    "EEG": {
      "sampling_frequency": 256,
      "channel_count": 2,
      "recording_duration_seconds": 65319
    },
    "EMG": {
      "sampling_frequency": 256,
      "channel_count": 1,
      "recording_duration_seconds": 65319
    },
    "MOV": {
      "sampling_frequency": 25,
      "channel_count": 12,
      "recording_duration_seconds": 65319
    }
  }
}
```

El identificador es un ejemplo de formato y deberá confirmarse con los nombres reales de los archivos antes de insertar documentos.

**Clave de identificación:** `recording_id`.

**Relación:** `participant_id` vincula la grabación con su participante.

### 3.3. Colección `eventos`

Almacenará las anotaciones que describen eventos identificados durante las grabaciones.

Ejemplo ilustrativo:

```json
{
  "participant_id": "sub-001",
  "recording_id": "sub-001_ses-01_task-szMonitoring_run-01",
  "onset": 14080.0,
  "duration": 84.0,
  "eventType": "impd",
  "lateralization": "n/a",
  "localization": "n/a",
  "vigilance": "n/a",
  "confidence": null
}
```

Este ejemplo representa una anotación de comprobación de impedancia del archivo revisado, no una crisis epiléptica.

**Identificación:** se podrá utilizar un identificador generado por MongoDB y una combinación de campos de origen para reconocer registros repetidos.

**Relación:** `participant_id` identifica al participante y `recording_id` permite asociar el evento con su grabación.

## 4. Relaciones entre las colecciones

- Un participante puede tener varias grabaciones.
- Una grabación puede contener varias anotaciones de eventos.
- Cada grabación debe estar vinculada con un participante existente.
- Cada evento debe poder asociarse con la grabación de origen, cuando esa información esté disponible.

Las relaciones se representarán mediante identificadores, sin duplicar innecesariamente la información del participante en todos los documentos.

## 5. Índices y consultas

Se proponen los siguientes índices:

- Índice único en `participantes.participant_id`.
- Índice único en `grabaciones.recording_id`.
- Índice en `eventos.participant_id`.
- Índice compuesto en `eventos.recording_id` y `eventos.onset`.

Estos índices facilitarán la búsqueda de participantes, grabaciones y eventos ordenados por tiempo.

## 6. Justificación del modelo

El modelo orientado a documentos permite almacenar metadatos con campos diferentes entre modalidades, sin exigir que todos los documentos tengan exactamente la misma estructura.

La separación en tres colecciones facilita la validación, reduce la duplicación de datos y permite ampliar el modelo posteriormente con variables derivadas de EEG, ECG, EMG y movimiento.

Las señales crudas se conservarán en sus archivos originales. MongoDB almacenará la información descriptiva, las referencias y las anotaciones necesarias para organizar los datos.

## 7. Alcance

Este diseño corresponde a una propuesta inicial. Los nombres definitivos de las grabaciones, la integridad de las relaciones y las reglas de identificación de eventos se verificarán durante la preparación y la carga de datos.