# Modelo NoSQL propuesto

## Base de datos y colección
- Base de datos: `bdpcd_atus`
- Colección: `accidentes_2025`
- Unidad documental: un registro de accidente tal como aparece en el conjunto anual ATUS 2025.

## Ejemplo conceptual de documento
Los valores siguientes son ilustrativos de estructura, no representan un accidente real:

```json
{
  "COBERTURA": "código",
  "CVEGEO": "código_geográfico",
  "CVE_ENT": "código_entidad",
  "CVE_MUN": "código_municipio",
  "ANIO": 2025,
  "MES": 1,
  "ID_DIA": 1,
  "ID_HORA": 14,
  "ID_MINUTO": 30,
  "DIASEMANA": "código",
  "URBANA": "código",
  "SUBURBANA": "código",
  "TIPACCID": "código",
  "CAUSAACCI": "código",
  "AUTOMOVIL": 1,
  "MOTOCICLET": 0,
  "BICICLETA": 0,
  "NEMUERTO": 0,
  "NEHERIDO": 1,
  "CLASACC": "código",
  "ESTATUS": "código"
}
```

## Justificación
El modelo documental permite conservar los atributos de cada registro en un documento JSON, facilita filtros por ubicación y tiempo, y evita diseñar numerosas tablas relacionadas para esta primera versión. La estructura original tiene muchas variables de una misma unidad de observación, por lo que una colección de documentos es una opción inicial sencilla.

## Índices sugeridos
Después de validar la carga:
- índice compuesto por `CVE_ENT`, `CVE_MUN`;
- índice compuesto por `ANIO`, `MES`;
- índice por `TIPACCID`;
- índice por `CAUSAACCI`.

Los índices se crearán cuando se pruebe que esas consultas son frecuentes. Antes de interpretar códigos, consultar el diccionario oficial de INEGI.
