# Tercera entrega NoSQL — EIC 2025 y perfiles sociodemográficos

Proyecto **ampliado a partir de la segunda entrega**, con consultas MongoDB, análisis exploratorio, visualizaciones y **dashboard Streamlit**. El núcleo de estudio es el perfil de mujeres de **15 a 49 años**, comparado por **entidad federativa y tamaño de localidad**.

> **Estado del paquete**: se incluye la exportación original de **153 dominios con 5 tamaños** como *datos de demostración reales de la ejecución previa*. El nuevo esquema de **4 tamaños** (el planteado para la tesina) se produce **solo cuando se vuelve a procesar el CSV original**. **NO** se fabrican 4 tamaños mediante medias simples de tasas existentes. Los perfiles no equivalen a estimaciones de TGF ni incorporan aún precisión estadística.

## 1. Inicio rápido en Windows, macOS o Linux — solo Docker

Requisito: **Docker Desktop/Engine con Docker Compose**, abierto y funcionando. En el primer arranque se descargan imágenes y paquetes, por lo que se necesita Internet. No hace falta instalar Python en el equipo anfitrión.

1. Descomprimir el ZIP en una carpeta local con espacio suficiente.
2. Abrir PowerShell o terminal **dentro de `proyecto_nosql_eic2025`**.
3. Ejecutar:

   ```bash
   docker compose up --build -d
   ```

4. En el navegador, abrir **http://localhost:8501**.
5. Si hay un problema, consultar:

   ```bash
   docker compose ps
   docker compose logs carga
   docker compose logs dashboard
   ```

El arranque crea MongoDB, valida/carga los JSON originales, crea índices y abre el dashboard. La base persiste en un volumen Docker. Se puede repetir el arranque; no se duplican registros.

Windows (opcional):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\iniciar_dashboard.ps1
```

macOS/Linux (opcional): `./iniciar_dashboard.sh`. Si los puertos 27018 o 8501 están ocupados, copiar `.env.example` a `.env` y modificar los puertos. Para apagar conservando datos: `docker compose down`. **No usar `docker compose down -v` salvo que se quiera borrar la base**.

## 2. Funciones analíticas listas para usar

- **Consultas y filtros MongoDB** por entidad y tamaño de localidad (`$match`, `$project`, `$sort`).
- **Agregaciones** de cobertura, recuentos, extremos y medias no ponderadas **entre dominios** (`$group`, `$sum`, `$avg`, `$min`, `$max`, `$subtract`). El resultado `$avg` es evidencia de operación NoSQL, **NO** una estimación poblacional. No se suman promedios ni porcentajes.
- **Perfiles** de escolaridad, participación económica, situación conyugal, autoadscripción indígena, lengua indígena y promedio de hijos nacidos vivos.
- **Visualizaciones** comparables entre categorías de localidad; dispersión para asociaciones ecológicas preliminares.
- **Dashboard** con cinco pestañas, filtros interactivos y exportación CSV.
- **Análisis Python** ejecutable con reporte Markdown: usar:

  ```bash
  docker compose exec dashboard python 07_analisis_perfiles.py --agrupacion 5
  ```

  Esto crea `salidas/perfiles_5_tamloc.csv`, `salidas/resumen_exploratorio_5_tamloc.md` y `salidas/media_escolaridad_no_ponderada_dominios_5_tamloc.csv` en la carpeta del anfitrión. Para una interpretación ya redactada y validable desde el JSON histórico, consultar `documentacion/INTERPRETACION_RESULTADOS_TERCERA_ENTREGA.md`.

## 3. Cuando se tenga el CSV original: pasar al diseño de 4 tamaños

El archivo completo **`personas00.csv` no se incluye** (varios GB). Para regenerar los indicadores con las cuatro categorías del estudio:

1. Copiar `personas00.csv` a `datos/personas00.csv`.
2. Con Docker ya iniciado con `docker compose up --build -d`, ejecutar:

   ```bash
   docker compose run --rm procesamiento
   docker compose run --rm carga
   docker compose restart dashboard
   ```

3. En el dashboard, seleccionar **4 tamaños** en la barra lateral.
4. Para exportar también esos resultados:

   ```bash
   docker compose exec dashboard python 07_analisis_perfiles.py --agrupacion 4
   ```

La nueva etapa 3 conserva **numeradores y denominadores ponderados** para recombinar las categorías originales `4` (50 000–99 999) y `5` (100 000+) en **`4` (50 000+)**. La nueva colección `indicadores_territoriales_4` se mantiene separada de `indicadores_territoriales` (cinco tamaños). Un dominio no observado no se reemplaza con un cero.

El reprocesamiento completo requiere **memoria, espacio de disco y tiempo suficientes** para millones de registros. Los datos originales permanecen en el equipo; los volúmenes `datos` y `salidas` se montan de manera local. Se recomienda espacio holgado para el archivo original y productos intermedios.

## 4. Verificación de la tercera entrega

```bash
# Pruebas sin MongoDB: pipeline sintético + consultas + cuatro tamaños
docker compose run --rm --no-deps dashboard python -m unittest discover -s tests -v

# Validación del JSON incluido
docker compose exec dashboard python verificar_documentos.py

# Evidencia de consultas y conexión
docker compose exec dashboard python 06_consultas_mongodb.py
```

Hay una tabla de trazabilidad en `documentacion/RUBRICA_TERCERA_ENTREGA.md`. El **informe académico entregable** está en `documentacion/Tercera_Entrega_NoSQL_EIC2025_Informe.docx`, junto con capturas de ejecución y el informe interpretativo Markdown.

**Si ya ejecutaste una versión anterior del proyecto:** descomprime esta versión en una carpeta nueva o sustituye los archivos de código y documentación conservando tu carpeta `salidas` si contiene exportaciones nuevas. Luego ejecuta `docker compose up --build -d` para incorporar los cambios del código al contenedor. Los volúmenes de MongoDB persisten si no se usa `down -v`.

## 5. Estructura

```text
proyecto_nosql_eic2025/
├── 01_diagnostico.py ... 06_consultas_mongodb.py  # Pipeline previo, conservado
├── 07_analisis_perfiles.py                       # Consultas y reporte Markdown
├── dashboard.py                                 # Streamlit / Plotly
├── analisis/consultas.py                        # Agregaciones MongoDB reutilizables
├── src/                                         # Limpieza y recodificación
├── tests/                                       # Pruebas sintéticas
├── datos/                                       # Microdato original opcional (excluido)
├── salidas/                                     # JSON existente, exportaciones y reportes
├── documentacion/                              # Modelo, matriz, método y rúbrica
├── docker-compose.yml / Dockerfile             # Contenedores reproducibles
├── requirements.txt / .env.example             # Dependencias y configuración
└── iniciar_dashboard.ps1 / iniciar_dashboard.sh # Accesos rápidos
```

## 6. Alcance metodológico de esta versión

| Estado | Componente | Observación |
|---|---|---|
| ✅ | 153 documentos de la ejecución previa (5 tamaños) | Fuente de la demostración; **no recalculados** aquí con el CSV completo. |
| ✅ | MongoDB + consultas + agregaciones + dashboard | Se ejecutan contra la base, no contra un CSV visualizado localmente. |
| ✅ | Perfiles exploratorios | Se pueden explorar asociaciones sin atribuir efectos causales. |
| ✅ | Generador correcto de 4 tamaños | Requiere microdatos para aplicarse; usa componentes ponderados sumables. |
| ⏳ | TGF y perfiles por edad | Requiere validar variables/criterios para nacimientos y población femenina por edades quinquenales. |
| ⏳ | Errores estándar, CV e intervalos de confianza | Validar diseño de encuesta y método de varianza por dominio. |
| ⏳ | Validación contra estimaciones oficiales | Contrastarlas antes de comunicar hallazgos sustantivos. |

**Cautelas principales**: el promedio de hijos nacidos vivos **no** es TGF; sexo/edad, codificaciones y filtros tienen que contrastarse con el diccionario publicado; las correlaciones de dominios no equivalen a relaciones individuales. La estructura conserva el trabajo previo en lugar de rehacerlo.

## 7. Compatibilidad y seguridad

Funciona en equipos **con una instalación compatible de Docker Compose**, procesador y recursos suficientes; no significa que corra en cualquier equipo sin requisitos. MongoDB (puerto 27018 externo; 27017 dentro de Docker) y Streamlit (8501) publican puertos **solo en `127.0.0.1`**. No exponerlos a Internet sin autenticación, cifrado y controles de acceso. En un equipo sin Docker se puede seguir utilizando el flujo local legado (`iniciar.ps1`/`iniciar.py`), pero ese flujo **también requiere Docker** para MongoDB.

**Pruebas incluidas**: las pruebas de módulos y el pipeline sintético son ejecutables sin MongoDB. El arranque real Docker/Streamlit debe verificarse en el equipo destino, pues este paquete se construyó sin un motor Docker disponible en el entorno de desarrollo.
