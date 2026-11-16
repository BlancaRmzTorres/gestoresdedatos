# Interpretación y recomendaciones de la tercera entrega

**Fuente de este informe:** exportación `salidas/indicadores_territoriales.json` del procesamiento previo EIC 2025; no es una nueva estimación del microdato completo ni un tabulado oficial.

## Cobertura del conjunto de demostración

- **153** documentos por dominio; **32** entidades representadas; **5** tamaños de localidad originales.
- Registros de microdato sumados por dominios: **6,652,318**; no son población expandida.
- Dominios ausentes respecto de una cuadrícula teórica de 32 × 5: **7**. La ausencia no se interpreta como cero.

### Cobertura por tamaño de localidad

| Tamaño original | Dominios | Registros de microdato | Escolaridad media simple entre dominios (años) |
|---|---:|---:|---:|
| 1 | 32 | 2,919,593 | 9.745 |
| 2 | 32 | 1,911,586 | 10.769 |
| 3 | 32 | 985,125 | 11.282 |
| 4 | 26 | 266,996 | 11.605 |
| 5 | 31 | 569,018 | 12.295 |

**Precisiones:** la última columna es una *media no ponderada entre dominios*, calculable en MongoDB mediante `$avg` como evidencia técnica. No corresponde a la escolaridad media de todas las mujeres: ese indicador exige usar estimadores y denominadores adecuados.

## Caso de estudio: Aguascalientes (CVE_ENT = 01)

| Tamaño original | Escolaridad (años) | Participación económica (%) | Hijos nacidos vivos, promedio |
|---|---:|---:|---:|
| 1 | 10.3792 | 42.9428 | 1.6153 |
| 2 | 11.1763 | 52.1529 | 1.5367 |
| 3 | 11.5858 | 55.4335 | 1.4431 |
| 4 | 11.4353 | 61.4784 | 1.4624 |
| 5 | 12.3122 | 57.9423 | 1.2898 |

**Resultado descriptivo 1.** La participación económica registrada en los cinco dominios de Aguascalientes varía desde **42.9428 %** (tamaño 1: menos de 2 500 habitantes) hasta **61.4784 %** (tamaño 4: de 50 000 a 99 999 habitantes); la amplitud es de **18.5356 puntos porcentuales**. Para el tamaño 5, el valor registrado es **57.9423 %**; por ello la secuencia no aumenta estrictamente con el tamaño de localidad.

**Resultado descriptivo 2.** La escolaridad promedio va de **10.3792 años** (tamaño 1) a **12.3122 años** (tamaño 5), una diferencia descriptiva de **1.9330 años**. En el mismo contraste, el promedio de hijos nacidos vivos pasa de **1.6153** a **1.2898** (diferencia de **−0.3255**). Estas cifras no permiten atribuir la diferencia a la escolaridad ni constituyen una TGF.

## Asociaciones exploratorias entre dominios

- Pearson entre escolaridad promedio y promedio de hijos nacidos vivos: **r = -0.843**, n = 153 dominios.
- Pearson entre participación económica y promedio de hijos nacidos vivos: **r = -0.784**, n = 153 dominios.

Ambas correlaciones son **ecológicas, preliminares y no ajustadas**: cada observación es un dominio territorial, no una mujer. Los dominios dentro de una entidad comparten contexto; no se han calculado errores estándar, intervalos de confianza ni pruebas de significancia que consideren el diseño muestral. No son evidencia causal.

## Conclusiones

1. La estructura MongoDB permite recuperar documentos, filtrar dominios, agrupar registros e inspeccionar indicadores; el dashboard facilita su consulta sin alterar las cifras del JSON heredado.
2. La distribución por localidad ofrece diferencias descriptivas que justifican explorar perfiles sociodemográficos, pero no permite interpretar diferencias como significativas.
3. La disponibilidad irregular de tamaños requiere reportar cobertura por dominio y mantener separados los indicadores de cinco tamaños respecto de la futura clasificación de cuatro.
4. El promedio de hijos nacidos vivos **no es** la tasa global de fecundidad; no debe presentarse como resultado de fecundidad de periodo.

## Recomendaciones

1. Verificar cada variable, código, universo y factor de expansión contra diccionario y criterios de tabulados de la EIC 2025.
2. Reprocesar los microdatos completos para obtener numeradores y denominadores válidos, con la desagregación final de cuatro tamaños; nunca combinar promedios simples 4 y 5.
3. Incluir edad quinquenal, calidad de estimaciones y diseño muestral antes de realizar inferencia o construir la TGF.
4. Al aplicar correlación y perfiles, controlar la composición etaria y reconocer la estructura jerárquica de dominios anidados dentro de entidades.

## Procedimiento reproducible de validación

```powershell
docker compose up --build -d
docker compose ps -a
docker compose logs carga
docker compose exec dashboard python 06_consultas_mongodb.py
docker compose exec dashboard python 07_analisis_perfiles.py --agrupacion 5
docker compose exec dashboard python -m unittest discover -s tests -v
```

**Evidencia de ejecución local proporcionada en la conversación:** MongoDB `Healthy`, dashboard `Started`, carga reportada como `153 documentos, 153 insertados, 0 actualizados, 153 comprobados`; generación de `perfiles_5_tamloc.csv` y `resumen_exploratorio_5_tamloc.md` confirmada. La nueva agregación `$avg` incluida en esta versión requiere ejecutar los comandos con el paquete actualizado para verificar su salida en la instalación destino.

**No verificado todavía:** arranque de la versión actualizada de Docker en un segundo equipo, procesamiento completo de `personas00.csv` y validación de indicadores contra tabulados oficiales.
