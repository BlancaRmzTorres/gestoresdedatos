"""Ejecutor multiplataforma. Requiere dependencias instaladas y Docker Desktop/Engine."""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from config import BASE_DIR, SALIDAS_DIR, ARCHIVO_PREDETERMINADO


def docker_executable() -> str:
    ruta = shutil.which("docker")
    if ruta:
        return ruta
    if os.name == "nt":
        for posible in (
            Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Docker/Docker/resources/bin/docker.exe",
            Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
            / "Programs/DockerDesktop/resources/bin/docker.exe",
        ):
            if posible.is_file():
                return str(posible)
    raise RuntimeError("No se encontro Docker CLI. Instala/abre Docker Desktop y verifica su instalacion.")


def correr(comando: list[str], capturar: bool = False) -> subprocess.CompletedProcess:
    print(" > " + " ".join(str(x) for x in comando), flush=True)
    return subprocess.run(comando, cwd=BASE_DIR, check=True,
                          text=True, capture_output=capturar)


def esperar_mongodb(docker: str) -> None:
    for intento in range(30):
        r = subprocess.run([docker, "compose", "exec", "-T", "mongodb", "mongosh",
                            "--quiet", "--eval", "db.adminCommand({ping: 1}).ok"],
                           cwd=BASE_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=15, check=False)
        if r.returncode == 0 and r.stdout.strip().splitlines()[-1:] == ["1"]:
            print("MongoDB responde al ping.")
            return
        if intento < 29:
            time.sleep(2)
    raise RuntimeError("MongoDB no respondio. Ejecuta 'docker compose logs mongodb' para diagnosticar.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--modo", choices=("demo", "completo", "validar"), default="demo")
    p.add_argument("--archivo", type=Path, default=ARCHIVO_PREDETERMINADO,
                   help="CSV original (solo modo completo), relativo a la raiz del proyecto o absoluto")
    p.add_argument("--chunksize", type=int, default=100000)
    args = p.parse_args()
    json_path = SALIDAS_DIR / "indicadores_territoriales.json"
    try:
        if args.modo == "completo":
            archivo = args.archivo if args.archivo.is_absolute() else BASE_DIR / args.archivo
            if not archivo.is_file():
                p.error(f"No se encontro {archivo}. Copia personas00.csv a datos/ o usa --archivo.")
            correr([sys.executable, str(BASE_DIR / "ejecutar_pipeline.py"),
                    "--archivo", str(archivo), "--chunksize", str(args.chunksize)])
        if not json_path.is_file():
            p.error(f"No existe {json_path}. Usa --modo completo con el CSV original.")
        correr([sys.executable, str(BASE_DIR / "verificar_documentos.py")])
        if args.modo == "validar":
            print("Validacion local completada. No se ha modificado MongoDB.")
            return
        docker = docker_executable()
        correr([docker, "compose", "version"])
        correr([docker, "info", "--format", "{{.ServerVersion}}"])
        correr([docker, "compose", "up", "--build", "-d"])
        esperar_mongodb(docker)
        correr([sys.executable, str(BASE_DIR / "05_cargar_mongodb.py")])
        correr([sys.executable, str(BASE_DIR / "06_consultas_mongodb.py")])
        print("\nOK: validacion, carga y consultas completadas.")
    except (RuntimeError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        p.exit(1, f"ERROR: {exc}\nRevisa el mensaje anterior y el README.md.\n")


if __name__ == "__main__":
    main()
