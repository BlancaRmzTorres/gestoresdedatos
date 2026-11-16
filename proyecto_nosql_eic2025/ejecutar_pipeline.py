"""Procesa los microdatos EIC 2025 (etapas 1 a 4); MongoDB va por separado."""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

from config import ARCHIVO_PREDETERMINADO, BASE_DIR, CHUNKSIZE, VARIABLES


def resolver_archivo(archivo: Path) -> Path:
    # Todas las rutas relativas se interpretan desde la carpeta del proyecto.
    return archivo.resolve() if archivo.is_absolute() else (BASE_DIR / archivo).resolve()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archivo", type=Path, default=ARCHIVO_PREDETERMINADO)
    p.add_argument("--chunksize", type=int, default=CHUNKSIZE)
    p.add_argument("--modo-duplicados", choices=("disco", "memoria"), default="disco",
                   help="En disco utiliza SQLite para reducir consumo de RAM (mas lento).")
    args = p.parse_args()
    archivo = resolver_archivo(args.archivo)
    if not archivo.is_file():
        p.error(f"No existe el CSV: {archivo}. Usa --archivo o inicia en modo demo sin microdatos.")
    if args.chunksize <= 0:
        p.error("--chunksize debe ser mayor que cero")
    try:
        with archivo.open("r", encoding="utf-8-sig", newline="") as f:
            columnas = csv.reader(f).__next__()
    except (UnicodeError, OSError, StopIteration) as exc:
        p.error(f"No se pudo leer la cabecera del CSV: {exc}")
    faltantes = sorted(set(VARIABLES) - set(columnas))
    if faltantes:
        p.error(f"Faltan columnas de la EIC 2025: {', '.join(faltantes)}")

    comandos = [
        [sys.executable, str(BASE_DIR / "01_diagnostico.py"), "--archivo", str(archivo),
         "--chunksize", str(args.chunksize), "--modo-duplicados", args.modo_duplicados],
        [sys.executable, str(BASE_DIR / "02_preparar_microdatos.py"), "--archivo", str(archivo),
         "--chunksize", str(args.chunksize)],
        [sys.executable, str(BASE_DIR / "03_construir_indicadores.py"),
         "--chunksize", str(args.chunksize)],
        [sys.executable, str(BASE_DIR / "04_generar_documentos_json.py")],
    ]
    for etapa, cmd in enumerate(comandos, 1):
        print(f"\n[ETAPA {etapa}/4] Ejecutando {Path(cmd[1]).name}", flush=True)
        try:
            subprocess.run(cmd, check=True, cwd=BASE_DIR)
        except subprocess.CalledProcessError as exc:
            raise SystemExit(f"Fallo la etapa {etapa} (codigo {exc.returncode}). Consulta el error anterior.") from exc

    print("\nPipeline completado. Continua con el modo demo para cargar y consultar MongoDB.")


if __name__ == "__main__":
    main()
