# Evidencia técnica y estado de comprobaciones

## 1. Evidencia local aportada por el usuario en la conversación

La ejecución anterior del paquete base en Windows con Docker Desktop mostró:

- Imagen Python `eic2025-analitica:local`: compilada.
- Contenedor `eic2025_nosql-mongodb-1`: `Healthy`.
- Contenedor de carga: finalizó; log `eic2025_nosql.indicadores_territoriales: 153 documentos, 153 insertados, 0 actualizados, 153 comprobados.`
- Dashboard Streamlit: accesible en `http://localhost:8501`, con filtros de entidad y tamaño de localidad, tablas y gráficas.
- Ejecución de `07_analisis_perfiles.py --agrupacion 5`: produjo rutas de los CSV e informe Markdown previstos en el paquete anterior.

Capturas recortadas de esa ejecución se conservan en `documentacion/evidencias/`. Estas capturas **no** acreditan la nueva consulta `$avg`, incorporada en la presente revisión.

## 2. Evidencia de revisión del paquete actualizado

En el entorno de edición del paquete se ejecutaron satisfactoriamente **9 pruebas automatizadas**, entre ellas una que genera el informe sin conectar a MongoDB mediante un adaptador simulado. Se validó además que el archivo histórico tiene **153 documentos con identificadores territoriales únicos**. El registro completo de estas comprobaciones está en `documentacion/RESULTADOS_PRUEBAS_REVISION.txt`.

### Pendiente de confirmar en Windows con el paquete actualizado

La salida integrada de la nueva agregación `$avg` debe comprobarse ejecutando de nuevo en el equipo del estudiante:

```powershell
docker compose up --build -d
docker compose logs carga
docker compose exec dashboard python 06_consultas_mongodb.py
docker compose exec dashboard python 07_analisis_perfiles.py --agrupacion 5
docker compose exec dashboard python -m unittest discover -s tests -v
```

En el dashboard, abrir **Consultas MongoDB** y verificar la sección **Agregación MongoDB con `$avg`**. El resultado es una **media no ponderada entre dominios** y no un promedio de población.

## 3. Alcance de reproducibilidad

Se dispone de Docker Compose, requisitos Python, instrucciones y pruebas. No está demostrado todavía que el paquete actualizado se haya iniciado en otro equipo diferente; la portabilidad depende de contar con Docker compatible y recursos adecuados. El microdato completo no forma parte del ZIP.
