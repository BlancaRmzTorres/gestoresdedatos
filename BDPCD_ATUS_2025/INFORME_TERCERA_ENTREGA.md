# Informe de resultados — Tercera entrega

## 1. Objetivo
Presentar el análisis descriptivo de los registros ATUS 2025 preparados y consultados mediante Python y MongoDB, así como documentar los resultados que alimentan el dashboard.

## 2. Preparación y almacenamiento
El conjunto original contenía 380,391 filas y 46 columnas. Durante la preparación se identificaron y eliminaron 748 duplicados exactos, con lo que se obtuvieron 379,643 registros. La colección `bdpcd_atus.accidentes_2025` fue verificada con 379,643 documentos. También se cuenta con `catalogo_entidades` (32 documentos) y `catalogo_municipios` (2,478 documentos).

La unidad documental es el registro de accidente. Los catálogos geográficos se mantienen separados de la colección principal. Las geometrías estatales y municipales se consultan desde archivos GeoJSON locales.

## 3. Resultados descriptivos

### 3.1 Distribución mensual
| Mes | Accidentes |
|---|---:|
| Enero | 29,931 |
| Febrero | 30,035 |
| Marzo | 34,637 |
| Abril | 30,575 |
| Mayo | 32,917 |
| Junio | 30,673 |
| Julio | 30,399 |
| Agosto | 31,542 |
| Septiembre | 31,167 |
| Octubre | 33,437 |
| Noviembre | 31,908 |
| Diciembre | 32,422 |

Marzo presenta el mayor conteo mensual (34,637), seguido de octubre (33,437). Enero presenta el menor (29,931). Son conteos observados; no se ajustan por días de exposición, movilidad o volumen vehicular.

### 3.2 Entidades con mayor número de registros
| Entidad | Accidentes |
|---|---:|
| Nuevo León | 70,921 |
| Chihuahua | 26,583 |
| Estado de México | 24,933 |
| Sonora | 21,774 |
| Guanajuato | 19,872 |
| Jalisco | 17,375 |
| Michoacán | 16,821 |
| Tamaulipas | 14,111 |
| Veracruz | 12,613 |
| Puebla | 12,212 |

Nuevo León concentra el mayor número de registros en esta extracción. La comparación es de volumen absoluto y no permite concluir que sea la entidad con mayor riesgo sin incorporar denominadores de exposición comparables.

### 3.3 Tipos de accidente
| Tipo | Accidentes | Porcentaje reportado |
|---|---:|---:|
| Colisión con vehículo automotor | 221,588 | 58.37% |
| Colisión con motocicleta | 68,471 | 18.04% |
| Colisión con objeto fijo | 43,300 | 11.41% |
| Volcadura | 15,405 | 4.06% |
| Colisión con peatón (atropellamiento) | 10,607 | 2.79% |
| Salida del camino | 9,993 | 2.63% |

La colisión con vehículo automotor es la categoría más frecuente, seguida por colisiones con motocicleta y con objeto fijo.

### 3.4 Causas registradas
| Causa | Accidentes |
|---|---:|
| Conductor | 362,926 |
| Mala condición del camino | 7,093 |
| Falla del vehículo | 4,091 |
| Otra | 3,130 |
| Peatón o pasajero | 2,403 |

La categoría registrada como conductor representa la mayor parte de los casos. La interpretación de las categorías debe conservarse conforme al catálogo oficial del INEGI; no se infieren subcausas que no estén presentes en los datos.

### 3.5 Personas fallecidas y lesionadas
La suma de las categorías desglosadas arroja 4,570 personas fallecidas y 86,937 lesionadas. El dashboard utiliza estas sumas categóricas para presentar los totales.

| Categoría | Fallecidos | Lesionados |
|---|---:|---:|
| Conductores | 2,630 | 47,508 |
| Pasajeros | 1,004 | 25,863 |
| Peatones | 775 | 11,240 |
| Ciclistas | 127 | 2,105 |
| Otros | 34 | 221 |

Se estiman 1.20 fallecidos y 22.90 lesionados por cada 100 accidentes, a partir de los totales anteriores y 379,643 accidentes. Estas razones no son probabilidades. La razón de lesionados puede superar una persona por accidente porque un mismo evento puede involucrar a varias personas lesionadas.

### 3.6 Vehículos involucrados
Se registraron 719,861 registros de vehículos involucrados. Las categorías con mayor frecuencia fueron automóvil (437,373), motocicleta (95,895), CAMPASAJ (85,005), camioneta (48,230), PASCAMION (15,495) y camión (15,220). La suma de registros por tipo de vehículo no equivale al número de accidentes, pues un accidente puede involucrar más de un vehículo. Las etiquetas abreviadas deben validarse con el catálogo oficial.

### 3.7 Temporalidad y zona
Por día de la semana, los mayores conteos corresponden a sábado (59,613), viernes (57,158) y domingo (53,995); el menor corresponde a martes (50,738). Por zona, se reportan 256,672 accidentes en intersección urbana y 95,765 en no intersección urbana. También se registran 18,281 en carretera estatal suburbana, 6,196 en otro camino suburbano y 2,729 en camino rural suburbano.

## 4. Indicadores derivados y cautelas
Entre las razones por cada 100 accidentes según tipo se reportan: colisión con ferrocarril, 10.21; atropellamiento, 6.97; volcadura, 4.80; caída de pasajero, 3.55; y salida del camino, 3.50. Son cocientes de fallecidos entre accidentes de cada categoría multiplicados por 100. No deben denominarse probabilidades individuales ni compararse como riesgo sin revisar cobertura, tamaño de grupo y exposición.

## 5. Calidad y limitaciones detectadas
- `CVE_ENT`, `MES`, `TIPACCID` y `CAUSAACCI` no presentan faltantes en el diagnóstico registrado.
- Se observa una discrepancia: `NEMUERTO` y `NEHERIDO` aparecen en cero, mientras que las variables desglosadas por tipo de persona contienen valores positivos. Por ello, los totales mostrados se calcularon sumando categorías. La discrepancia debe contrastarse con el diccionario y documentación oficial antes de modificar o recodificar campos.
- El diccionario de datos del proyecto es preliminar. Los códigos categóricos y abreviaturas deben validarse con los catálogos oficiales.
- Los conteos estatales y municipales no son tasas de riesgo; faltan denominadores como población, parque vehicular, viajes o kilómetros recorridos.
- Los resultados describen registros reportados en el conjunto ATUS 2025 y no deben extrapolarse automáticamente a todos los accidentes ocurridos en el país o a zonas no cubiertas por la operación estadística.

## 6. Visualización y consultas
El dashboard Streamlit consulta MongoDB Atlas y presenta indicadores, desgloses y mapas. El mapa nacional utiliza polígonos estatales y el detalle municipal se habilita al seleccionar una entidad. Las geometrías permanecen en `data/geografia/` y no se cargan a Atlas.

## 7. Conclusiones
El conjunto preparado contiene 379,643 registros y permite analizar distribución temporal, territorial, tipos de accidente, causas, vehículos involucrados y consecuencias humanas. Las colisiones con vehículo automotor dominan el volumen registrado; Nuevo León presenta el mayor conteo estatal. Los resultados también muestran la importancia de analizar por separado frecuencia y severidad, pues los tipos de accidente con menor frecuencia pueden presentar razones de fallecidos por cada 100 accidentes más elevadas.

Antes de formular conclusiones de riesgo o recomendaciones de política pública, se requiere validar códigos con el diccionario oficial, resolver la discrepancia de los totales `NEMUERTO` y `NEHERIDO` y añadir denominadores de exposición.

## 8. Reproducibilidad y seguridad
La colección de accidentes ya cargada no debe recargarse para ejecutar el dashboard. El pipeline de carga puede limpiar la colección destino. La reconstrucción de catálogos afecta únicamente las colecciones de catálogos y debe realizarse solo cuando sea necesario. Las credenciales de MongoDB deben mantenerse en variables de entorno y nunca versionarse.
