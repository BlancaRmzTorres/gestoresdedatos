# Actualizar la tercera entrega y preparar la demostración

La versión anterior de Docker ya fue comprobada en Windows. Esta versión añade una agregación `$avg`, un informe académico de cinco páginas y una interpretación documental. **No se han añadido nuevas gráficas**.

## A. Actualizar desde el paquete anterior (Windows / PowerShell)

1. Si ya está corriendo el paquete viejo, abre la terminal **en la carpeta anterior** y ejecuta:

   ```powershell
   docker compose down
   ```

   Este comando detiene los contenedores y **conserva** el volumen de MongoDB. **No ejecutes `docker compose down -v`**.
2. Haz una copia de tu carpeta anterior por si has agregado microdatos o salidas. Descomprime el ZIP actualizado en una carpeta distinta.
3. Abre esa nueva carpeta `proyecto_nosql_eic2025` en VS Code. Ejecuta:

   ```powershell
   docker compose up --build -d
   docker compose ps -a
   docker compose logs carga
   ```

4. Abre `http://localhost:8501`. En **Consultas MongoDB**, comprueba la tabla de la nueva agregación `$avg`.
5. Genera evidencias del análisis:

   ```powershell
   docker compose exec dashboard python 06_consultas_mongodb.py
   docker compose exec dashboard python 07_analisis_perfiles.py --agrupacion 5
   docker compose exec dashboard python -m unittest discover -s tests -v
   ```

6. Revisa los resultados en `salidas/`:

   - `perfiles_5_tamloc.csv`
   - `resumen_exploratorio_5_tamloc.md`
   - `media_escolaridad_no_ponderada_dominios_5_tamloc.csv`

## B. Archivos relevantes para la entrega

- Informe: `documentacion/Tercera_Entrega_NoSQL_EIC2025_Informe.docx`
- Matriz de rúbrica: `documentacion/RUBRICA_TERCERA_ENTREGA.md`
- Interpretación: `documentacion/INTERPRETACION_RESULTADOS_TERCERA_ENTREGA.md`
- Evidencias: `documentacion/EVIDENCIAS_EJECUCION.md` y `documentacion/evidencias/`
- Código: `analisis/consultas.py`, `06_consultas_mongodb.py`, `07_analisis_perfiles.py`, `dashboard.py`, `tests/`

## C. Consideraciones para presentar

La nueva operación `$avg` es **la media no ponderada de indicadores entre dominios**; no es un estimador poblacional. La correlación ecológica tampoco identifica causalidad. Se utilizan 153 dominios históricos en cinco tamaños; no es todavía el estudio definitivo de 128 dominios potenciales bajo cuatro tamaños. La TGF y la inferencia muestral se incorporarán a la tesina en una fase posterior.
