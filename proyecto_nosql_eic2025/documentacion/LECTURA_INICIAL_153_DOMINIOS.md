# Lectura inicial documentada de la exportación previa (NO inferencia final)

Los siguientes valores son de los 153 documentos JSON incluidos de la segunda entrega, no de una nueva extracción de microdatos ni de tabulados oficiales.

- Dominios: **153**; entidades: **32**; total de registros en dominios: **6,652,318**.
- Cobertura por tamaño: 1: 32, 2: 32, 3: 32, 4: 26, 5: 31.
- Hay 7 cruces sin documento entre 32×5 combinaciones posibles; no se interpretan como cero.

## Perfil de ejemplo: Aguascalientes, mujeres de 15 a 49 años

| Tamaño original | Escolaridad promedio (años) | Participación económica (%) | Promedio HNV |
|---:|---:|---:|---:|
| 1 | 10.38 | 42.94 | 1.615 |
| 2 | 11.18 | 52.15 | 1.537 |
| 3 | 11.59 | 55.43 | 1.443 |
| 4 | 11.44 | 61.48 | 1.462 |
| 5 | 12.31 | 57.94 | 1.290 |

En la exportación inicial, la escolaridad promedio para Aguascalientes aumenta de 10.38 años (tamaño 1) a 12.31 años (tamaño 5), y el promedio de hijos nacidos vivos disminuye de 1.615 a 1.290. **No se ha evaluado la precisión de las diferencias**. Estas cifras requieren contrastarse con las salidas y criterios oficiales.

La correlación descriptiva entre escolaridad promedio y promedio de HNV, usando **153 dominios** como puntos, es `r = -0.843`. Es una asociación ecológica exploratoria, influida por heterogeneidad entre entidades y tamaños, **no causal** ni equivalente a una correlación entre personas.

**Precaución:** promedio de hijos nacidos vivos NO es la tasa global de fecundidad. No se estimaron CV, errores estándar ni intervalos de confianza.
