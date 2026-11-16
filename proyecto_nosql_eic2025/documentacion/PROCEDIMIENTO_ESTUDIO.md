# Puente de la tercera entrega hacia el estudio de fecundidad

## Delimitación

- Fuente central prevista: Encuesta Intercensal 2025 (INEGI).
- Universo inicial: mujeres de 15 a 49 años.
- Unidad territorial: entidad × cuatro tamaños (<2 500, 2 500–14 999, 15 000–49 999 y 50 000+ habitantes).
- Datos en la demostración heredada: 5 tamaños y 153 dominios disponibles.
- No imputar como cero los dominios sin documentos ni interpretar el total de registros del microdato como el total de la población.

## Validaciones previas a un resultado publicable

1. Contrastar cada variable, valor especial, pase y recodificación con `eic2025_micro_fd` y criterios de tabulados oficiales.
2. Verificar el significado del factor de expansión (`FACTOR`), su aplicación a numeradores/denominadores y unidades con respuesta válida.
3. Definir el estimador de nacimientos recientes según las variables originales y el periodo de referencia; **no usar el promedio de hijos acumulados como TGF**.
4. Construir estimaciones específicas por edad 15–19, ..., 45–49; documentar denominadores, periodo y fórmula TGF compatible con criterios oficiales.
5. Comprobar si los cuatro tamaños por entidad admiten estimaciones con precisión aceptable; calcular error estándar, CV e intervalo de confianza con el procedimiento que corresponda al diseño muestral.
6. Contrastar agregados contra resultados publicados; si hay diferencias, auditar universo, imputación, codificaciones y factor antes de interpretar.
7. Para análisis correlacional, justificar dependencia de dominios dentro de entidad, covariables, efecto de la urbanización y falacia ecológica.

## Por qué recombinar con componentes

Si las categorías 4 y 5 tienen promedios `A4=N4/D4` y `A5=N5/D5`, el valor conjunto se calcula como `(N4+N5)/(D4+D5)`; en general **no** equivale a `(A4+A5)/2`. Además, los denominadores válidos pueden ser distintos entre escolaridad, actividad económica y fecundidad acumulada por no respuesta.

El nuevo archivo `indicadores_territoriales_4.csv` incluye `esc_num`, `esc_den`, `pea_num`, `pea_den`, etc. para documentar estas operaciones. Esta mejora solo se materializa al reprocesar el CSV oficial.

## Uso correcto del dashboard

Utilizar los resultados para generar **hipótesis** y perfiles territoriales iniciales, no para determinar causas ni confirmar diferencias estadísticamente significativas. El estudio definitivo añadirá nacimientos de periodo y varianzas antes de evaluar relaciones con TGF.
