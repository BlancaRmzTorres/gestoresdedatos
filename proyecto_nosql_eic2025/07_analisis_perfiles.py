"""Tercera entrega: consultas $match/$project/$group, perfiles y resumen exploratorio.

Se ejecuta desde el host o dentro de contenedor con MONGO_URI configurada.
No calcula TGF ni inferencia estadística del diseño muestral.
"""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path

import pandas as pd
from pymongo import MongoClient

from analisis.consultas import (METRICAS, pipeline_dominios, pipeline_conteos_por_tamano,
                               pipeline_promedio_dominios_por_tamano)
from config import MONGO_DB, MONGO_URI, SALIDAS_DIR


def ejecutar(coleccion, carpeta: Path, agrupacion: int) -> tuple[Path, Path, Path]:
    carpeta.mkdir(parents=True, exist_ok=True)
    documentos = list(coleccion.aggregate(pipeline_dominios(limite=500), maxTimeMS=15000))
    if not documentos:
        raise ValueError("Colección vacía. Ejecuta primero la carga de MongoDB.")
    df = pd.DataFrame(documentos).sort_values(["cve_ent", "tamloc"])
    nombre = f"perfiles_{agrupacion}_tamloc.csv"
    csv = carpeta / nombre
    df.to_csv(csv, index=False, encoding="utf-8-sig")

    resumen = list(coleccion.aggregate(pipeline_conteos_por_tamano(), maxTimeMS=15000))
    resumen = sorted(resumen, key=lambda e: e["_id"])
    promedio_dom = list(coleccion.aggregate(
        pipeline_promedio_dominios_por_tamano("escolaridad_promedio"), maxTimeMS=15000))
    promedio_dom = sorted(promedio_dom, key=lambda e: e["_id"])
    media_csv = carpeta / f"media_escolaridad_no_ponderada_dominios_{agrupacion}_tamloc.csv"
    pd.DataFrame(promedio_dom).rename(columns={"_id": "tamloc"}).to_csv(
        media_csv, index=False, encoding="utf-8-sig")
    correlacion = df[list(METRICAS)].corr(method="pearson", min_periods=10)
    corr_esc_hnv = correlacion.loc["escolaridad_promedio", "promedio_hijos_nacidos_vivos"]
    corr_eco_hnv = correlacion.loc["participacion_economica_pct", "promedio_hijos_nacidos_vivos"]

    texto = [
        f"# Exploración inicial — EIC 2025, {agrupacion} categorías de tamaño de localidad",
        "", f"Generado: {date.today().isoformat()} desde MongoDB.", "",
        "## Cobertura de esta exportación", "",
        f"- Documentos/domínios territoriales: **{len(df)}**.",
        f"- Entidades con al menos un dominio: **{df['cve_ent'].nunique()}**.",
        "- Universo representado: mujeres de 15 a 49 años; información almacenada por dominio.",
        "- Cada dominio corresponde a entidad federativa × categoría de tamaño de localidad.",
        "", "## Agregación de cobertura ($group)", "",
        "| Tamaño | Dominios con datos | Registros del microdato |", "|---|---:|---:|",
    ]
    for r in resumen:
        texto.append(f"| {r['_id']} | {r['dominios']} | {int(r['registros_microdato']):,} |")
    texto += [
        "", "## Ejemplo de `$avg` MongoDB: medias NO ponderadas de dominios", "",
        "**No son promedios poblacionales**: cada dominio cuenta una vez; no se pondera por población ni por registros.",
        "| Tamaño | Dominios válidos | Escolaridad media de dominios (años) |",
        "|---|---:|---:|",
    ]
    for r in promedio_dom:
        texto.append(f"| {r['_id']} | {r['dominios_validos']} | {r['media_no_ponderada_de_dominios']:.3f} |")
    texto += [
        "", "## Asociación ecológica preliminar", "",
        f"- Correlación de Pearson entre escolaridad promedio y promedio de HNV: **{corr_esc_hnv:.3f}**.",
        f"- Correlación de Pearson entre participación económica y promedio de HNV: **{corr_eco_hnv:.3f}**.",
        "", "Estas correlaciones son exploratorias, mezclan dominios de entidades y tamaños de localidad,",
        "no tienen corrección por diseño muestral y **no implican causalidad ni significancia**.",
        "Los dominios de una misma entidad no son necesariamente independientes.",
        "", "## Limitaciones críticas", "",
        "- El promedio de hijos nacidos vivos **no es la Tasa Global de Fecundidad (TGF)**.",
        "- Las cifras provienen de una exportación del procesamiento previo; este reporte no contrasta con tabulados oficiales.",
        "- No se han calculado CV, errores estándar ni intervalos de confianza. No interpretar rangos como diferencias significativas.",
        "- La inferencia y comparaciones oficiales necesitan definir el estimador, ponderación y réplicas/varianza aplicables.",
        "- Para 4 tamaños, la categoría 50 000+ se obtiene **solo tras reprocesar numeradores y denominadores**, nunca promediando tasas de las categorías 4 y 5.",
        "", "## Interpretación descriptiva de referencia: Aguascalientes (CVE_ENT=01)", "",
    ]
    ejemplo = df[df["cve_ent"] == "01"].sort_values("tamloc")
    if not ejemplo.empty:
        texto += [
            "| Tamaño | Escolaridad (años) | Participación económica (%) | Promedio HNV |",
            "|---|---:|---:|---:|",
        ]
        for _, fila in ejemplo.iterrows():
            texto.append(
                f"| {fila['tamloc']} | {fila['escolaridad_promedio']:.2f} | "
                f"{fila['participacion_economica_pct']:.2f} | "
                f"{fila['promedio_hijos_nacidos_vivos']:.3f} |"
            )
        if len(ejemplo) >= 2:
            min_pea = ejemplo.loc[ejemplo['participacion_economica_pct'].idxmin()]
            max_pea = ejemplo.loc[ejemplo['participacion_economica_pct'].idxmax()]
            delta = max_pea['participacion_economica_pct'] - min_pea['participacion_economica_pct']
            texto += [
                "", "**Hallazgo A.** En los dominios observados de Aguascalientes, la participación económica "
                f"oscila de {min_pea['participacion_economica_pct']:.2f}% "
                f"(tamaño {min_pea['tamloc']}) a {max_pea['participacion_economica_pct']:.2f}% "
                f"(tamaño {max_pea['tamloc']}): amplitud de {delta:.2f} puntos porcentuales.",
                "", "**Hallazgo B.** La variación no es estrictamente monótona respecto al tamaño: "
                "las categorías deben analizarse por separado y considerando composición por edad, escolaridad y actividad.",
                "", "**Interpretación.** Los resultados describen diferencias entre dominios de la exportación, "
                "no identifican mecanismos causales ni prueban significancia estadística.",
            ]
    else:
        texto.append("No hay dominios de Aguascalientes disponibles con los filtros empleados.")
    texto += [
        "", "## Conclusiones y recomendaciones", "",
        "1. La base heredada permite describir heterogeneidad territorial, pero no inferir patrones individuales de fecundidad.",
        "2. La presencia de dominios faltantes impide tratar una matriz de 32 × 5 como plenamente observada; no imputar ceros.",
        "3. La comparación por tamaño requiere validar universo, codificación de variables y denominadores de cada indicador.",
        "4. Antes de usar resultados sustantivos en la tesina, contrastar los cálculos con criterios oficiales y evaluar precisión muestral.",
        "", "## Próximos pasos para la tesina", "",
        "1. Contrastar codificaciones y estimadores del diccionario INEGI y tabulados publicados.",
        "2. Construir TGF con nacimientos del periodo y población femenina por grupos quinquenales de edad, tras verificar sus variables y criterios.",
        "3. Evaluar precisión de los estimadores por dominio territorial antes de publicar resultados comparativos.",
        "4. Incorporar perfiles de edad y variables socioeconómicas complementarias.",
    ]
    md = carpeta / f"resumen_exploratorio_{agrupacion}_tamloc.md"
    md.write_text("\n".join(texto) + "\n", encoding="utf-8")
    return csv, md, media_csv


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agrupacion", type=int, default=5, choices=(4, 5))
    args = parser.parse_args()
    nombre = "indicadores_territoriales" if args.agrupacion == 5 else "indicadores_territoriales_4"
    with MongoClient(MONGO_URI, serverSelectionTimeoutMS=12000) as client:
        client.admin.command("ping")
        csv, md, media_csv = ejecutar(client[MONGO_DB][nombre], SALIDAS_DIR, args.agrupacion)
    print(f"Perfil CSV: {csv}\nInforme: {md}\nAgregación $avg CSV: {media_csv}")


if __name__ == "__main__":
    main()
