# Control de calidad ejecutado durante la construcción

- Fecha: 12 de noviembre de 2026.
- `python -m unittest discover -s tests -v`: **7/7 pruebas satisfactorias**.
- `python -m compileall -q .`: compilación sin errores.
- `python verificar_documentos.py`: **JSON original válido, 153 documentos**.
- Se probaron microdatos **sintéticos** por bloques, con un caso de agregación 50 000+ de 4 y 5 mediante numeradores y denominadores ponderados (HNV combinado 1.8 en la prueba), así como detección de duplicados.
- Docker / MongoDB / Streamlit: **NO se ejecutaron de extremo a extremo en este entorno**, por falta de motor Docker disponible; los comandos e infraestructura se entregan para validación en el equipo destino.
- La exportación incluida proviene de una ejecución previa y **no sustituye** la contrastación con la metodología y las estimaciones oficiales INEGI.
