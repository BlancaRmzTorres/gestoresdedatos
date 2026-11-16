# Cambios acumulativos respecto de la segunda entrega

- Se conserva la estructura y los scripts de procesamiento `01` a `06` junto con los 153 documentos de demostración.
- Se incorpora Dockerfile y Compose con tres servicios principales (`mongodb`, `carga`, `dashboard`) más `procesamiento` opcional.
- Se incorpora `07_analisis_perfiles.py`, consultas reutilizables en `analisis/consultas.py` y aplicación `dashboard.py`.
- Se admite el **reprocesamiento correcto de 4 tamaños de localidad** mediante numeradores y denominadores de indicadores; la cuarta categoría combina tamaños originales 4 y 5.
- Se agrega segunda colección `indicadores_territoriales_4`, **únicamente si existe JSON generado con microdatos**.
- Se añade un reporte exploratorio Markdown y exportación CSV, y cuatro nuevas pruebas unitarias.
- Se incluye la matriz instrumental de la tesina como referencia metodológica.
- Las variables de TGF y la precisión inferencial se mantienen expresamente como fases pendientes.


## Cierre de rúbrica (revisión posterior)

- Se añadió `pipeline_promedio_dominios_por_tamano` con `$avg` (media simple de valores entre dominios); está explicitado que **no** es media poblacional ponderada.
- `06_consultas_mongodb.py` demuestra `$group`, `$sum` y `$avg` en salida de terminal.
- La pestaña **Consultas MongoDB** presenta tabla de `$avg` sin agregar gráficas.
- `07_analisis_perfiles.py` ahora produce un tercer CSV de la agregación y un informe con hallazgos de Aguascalientes, conclusiones y recomendaciones.
- Se añadió interpretación documental reproducida desde la exportación JSON de los 153 dominios y un informe académico Word.
- La suite tiene nueve pruebas; no se atribuye verificación con Docker en máquina ajena al entorno de trabajo.
