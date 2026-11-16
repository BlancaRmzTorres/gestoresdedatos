# Matriz de cumplimiento de la tercera entrega (imagen de rúbrica)

| Categoría | Elemento a evaluar | Evidencia del proyecto | Comprobación |
|---|---|---|---|
| Gestión y consulta de datos | Consultas NoSQL | `06_consultas_mongodb.py`, `analisis/consultas.py`; `find`, `$match`, `$project`, `$sort`, `$limit` | Ejecutar `06_consultas_mongodb.py` dentro de `dashboard` y abrir **Consultas MongoDB** |
| Gestión y consulta de datos | Filtros y búsquedas | Selección de entidad y tamaño de localidad en Streamlit | Filtrar `CVE_ENT = 01` y comparar 5 dominios |
| Gestión y consulta de datos | Agregaciones | `pipeline_conteos_por_tamano` (`$sum`), `pipeline_extremos` (`$min`, `$max`) y **`pipeline_promedio_dominios_por_tamano` (`$avg`)** | Abrir **Consultas MongoDB**: tabla por tamaño y tabla de `$avg` (media **no ponderada entre dominios**) |
| Análisis e interpretación | Análisis exploratorio | `07_analisis_perfiles.py`, CSV y correlaciones ecológicas | Ejecutar el script y revisar `salidas/resumen_exploratorio_5_tamloc.md` |
| Análisis e interpretación | Interpretación de resultados | `documentacion/INTERPRETACION_RESULTADOS_TERCERA_ENTREGA.md` | Revisar cobertura, Aguascalientes, limitaciones, conclusiones y recomendaciones |
| Visualización y entrega | Visualización de datos | Gráficas que ya existen en pestañas **Panorama**, **Perfil por entidad**, **Asociaciones** | Explorar las visualizaciones existentes (sin añadir nuevas) |
| Visualización y entrega | Dashboard | `dashboard.py`, Streamlit conectado a MongoDB | Abrir `http://localhost:8501` con Docker Compose |
| Soporte técnico | Código de análisis | Scripts `01`–`07`, `analisis/`, `src/`, `tests/` y Docker Compose | `python -m unittest discover -s tests -v`, `verificar_documentos.py` |

## Material presentable

- Informe en Word: `documentacion/Tercera_Entrega_NoSQL_EIC2025_Informe.docx`.
- Interpretación en Markdown: `documentacion/INTERPRETACION_RESULTADOS_TERCERA_ENTREGA.md`.
- Código fuente, configuraciones, requisitos, JSON de demostración y pruebas en el mismo ZIP.
- Capturas de ejecución local de Streamlit (`documentacion/evidencias/`) proporcionadas por el usuario.

## Distinciones indispensables

La agregación `$avg` promedia **dominios**, no personas; sirve para evaluar un operador NoSQL. El promedio poblacional se calcula con el estimador apropiado. Las correlaciones son exploratorias; no hay TGF, intervalos de confianza ni pruebas ajustadas al diseño. La colección inicial es de **153 dominios con cinco tamaños**, no del estudio final con cuatro.
