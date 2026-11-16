# Modelo NoSQL propuesto

## Base de datos

`eic2025_nosql`

## Colección principal: `indicadores_territoriales`

Cada documento representa un dominio analítico formado por:

**Entidad federativa × tamaño de localidad**

Ejemplo:

```json
{
  "_id": "01_2",
  "fuente": {
    "institucion": "INEGI",
    "programa": "Encuesta Intercensal 2025",
    "tabla_origen": "PERSONAS",
    "periodo": 2025
  },
  "territorio": {
    "cve_ent": "01",
    "tamloc": "2",
    "tamloc_descripcion": "De 2 500 a 14 999 habitantes"
  },
  "universo": {
    "sexo": "Mujer",
    "edad_min": 15,
    "edad_max": 49
  },
  "conteos": {
    "registros_microdato": 100,
    "poblacion_ponderada": 1250
  },
  "indicadores": {
    "escolaridad_promedio": 10.5,
    "participacion_economica_pct": 52.4,
    "mujeres_unidas_pct": 48.1,
    "autoadscripcion_indigena_pct": 2.2,
    "habla_lengua_indigena_pct": 0.9,
    "promedio_hijos_nacidos_vivos": 1.3
  }
}
```

## Justificación

El documento agrupa campos relacionados en subdocumentos (`fuente`, `territorio`, `universo`, `conteos`, `indicadores`). Esto evita una estructura completamente plana y facilita consultas analíticas sin requerir uniones entre varias tablas.

## Colección opcional: `personas_procesadas`

Puede incorporarse posteriormente para conservar microdatos seleccionados y limpios. Para la segunda entrega se prioriza `indicadores_territoriales` porque representa una base compacta y directamente utilizable en la etapa de análisis.
