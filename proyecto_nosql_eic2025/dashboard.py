"""Panel exploratorio EIC 2025 con consultas reales a MongoDB."""
from __future__ import annotations
import os
import pandas as pd
import plotly.express as px
import streamlit as st
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from analisis.consultas import (
    METRICAS, DESCRIPCIONES_TAMLOC_4, pipeline_dominios, pipeline_conteos_por_tamano,
    pipeline_extremos, pipeline_promedio_dominios_por_tamano,
)
from config import MONGO_DB, MONGO_URI, TAMLOC_DESC

st.set_page_config(page_title="EIC 2025 | Perfiles territoriales", page_icon="📊", layout="wide")

st.title("EIC 2025 · Perfiles territoriales de fecundidad y contexto socioeconómico")
st.caption("Tercera entrega NoSQL · Python + MongoDB + Streamlit · Exploración de dominios entidad × tamaño de localidad")

@st.cache_data(ttl=30, show_spinner=False)
def obtener(nom_col, entidades, tamanos):
    with MongoClient(MONGO_URI, serverSelectionTimeoutMS=7000) as cli:
        cli.admin.command("ping")
        col = cli[MONGO_DB][nom_col]
        datos = list(col.aggregate(pipeline_dominios(entidades, tamanos, 500), maxTimeMS=15000))
        grupos = list(col.aggregate(pipeline_conteos_por_tamano(entidades, tamanos), maxTimeMS=15000))
    return datos, grupos

@st.cache_data(ttl=30, show_spinner=False)
def conteo_colecciones():
    with MongoClient(MONGO_URI, serverSelectionTimeoutMS=7000) as cli:
        cli.admin.command("ping")
        bd = cli[MONGO_DB]
        nombres = bd.list_collection_names()
        return {n: bd[n].count_documents({}) for n in ("indicadores_territoriales", "indicadores_territoriales_4") if n in nombres}

try:
    colecciones = conteo_colecciones()
except (PyMongoError, OSError) as exc:
    st.error("MongoDB no responde. Inicia Docker Compose (`docker compose up --build -d`) y verifica los contenedores.")
    st.code(str(exc))
    st.stop()

if not colecciones:
    st.error("No hay colecciones de indicadores. Ejecuta la carga del JSON antes de abrir el panel.")
    st.stop()

opciones = {f"{('5' if col.endswith('territoriales') else '4')} tamaños · {n} dominios": col for col, n in colecciones.items() if n > 0}
if not opciones:
    st.warning("Las colecciones existen, pero no contienen documentos.")
    st.stop()

st.sidebar.header("Parámetros del estudio")
agrup = st.sidebar.selectbox("Desagregación territorial", list(opciones), index=0)
col_actual = opciones[agrup]
cuatro = col_actual.endswith("_4")
mapa_tam = DESCRIPCIONES_TAMLOC_4 if cuatro else TAMLOC_DESC
entidades = st.sidebar.multiselect("Entidades (CVE_ENT)", [f"{i:02d}" for i in range(1, 33)], default=[])
tamanos = st.sidebar.multiselect("Tamaño de localidad", list(mapa_tam), format_func=lambda x: f"{x} · {mapa_tam[x]}", default=[])
metrica = st.sidebar.selectbox("Indicador principal", list(METRICAS), format_func=lambda x: METRICAS[x])

try:
    docs, grupos = obtener(col_actual, tuple(entidades), tuple(tamanos))
except (PyMongoError, OSError) as exc:
    st.error("No fue posible consultar los datos en MongoDB.")
    st.code(str(exc))
    st.stop()
if not docs:
    st.warning("No hay documentos para los filtros seleccionados. Ajusta entidad o tamaño de localidad.")
    st.stop()

df = pd.DataFrame(docs)
df["Tamaño de localidad"] = df["tamloc"].map(mapa_tam)
df["Entidad"] = df["cve_ent"]
for c in list(METRICAS) + ["registros_microdato", "poblacion_ponderada"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

if not cuatro:
    st.info("Vista histórica con **5 tamaños originales**: 153 dominios disponibles en el paquete. "
            "El estudio final plantea **4 categorías**; para combinar 50 000+ correctamente "
            "debe ejecutarse el procesamiento completo con numeradores y denominadores.")

st.warning("Indicadores descriptivos, no TGF. No se incorporaron errores estándar, CV ni intervalos de confianza; "
           "las diferencias visuales no deben interpretarse como estadísticamente significativas.", icon="⚠️")

c1,c2,c3,c4=st.columns(4)
c1.metric("Dominios disponibles", f"{len(df):,}")
c2.metric("Entidades representadas", df["cve_ent"].nunique())
c3.metric("Tamaños representados", df["tamloc"].nunique())
c4.metric("Registros del microdato", f"{int(df['registros_microdato'].sum()):,}")

t1,t2,t3,t4,t5=st.tabs(["Panorama", "Perfil por entidad", "Asociaciones", "Consultas MongoDB", "Metodología"])
with t1:
    st.subheader("Indicadores por dominio territorial")
    fig = px.scatter(df, x="cve_ent", y=metrica, color="Tamaño de localidad",
                     hover_data=["tamloc", "registros_microdato"],
                     labels={"cve_ent":"Entidad (clave)", metrica: METRICAS[metrica]},
                     title=f"{METRICAS[metrica]} por entidad y tamaño")
    fig.update_layout(height=470)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Cada punto es un dominio con observaciones válidas. El orden horizontal corresponde a CVE_ENT; no representa una serie temporal.")
    st.dataframe(df[["Entidad", "Tamaño de localidad", "registros_microdato", "poblacion_ponderada"]+list(METRICAS)]
                 .rename(columns={"registros_microdato":"Registros", "poblacion_ponderada":"Población ponderada", **METRICAS}),
                 hide_index=True, use_container_width=True)
    st.download_button("Exportar dominios filtrados (CSV)", data=df.to_csv(index=False).encode("utf-8-sig"),
                       file_name="eic2025_perfiles_filtrados.csv", mime="text/csv")

with t2:
    st.subheader("Perfil socioeconómico de una entidad")
    claves = sorted(df["cve_ent"].unique().tolist())
    ent_elegida = st.selectbox("Entidad", claves)
    ent_df = df.loc[df["cve_ent"] == ent_elegida].sort_values("tamloc")
    st.dataframe(ent_df[["Tamaño de localidad"] + list(METRICAS)].rename(columns=METRICAS),
                 hide_index=True, use_container_width=True)
    fig = px.bar(ent_df, x="Tamaño de localidad", y=metrica,
                 labels={metrica:METRICAS[metrica]}, title=f"Entidad {ent_elegida} · {METRICAS[metrica]}")
    st.plotly_chart(fig, use_container_width=True)
    vals = ent_df[metrica].dropna()
    if len(vals) >= 2:
        st.write(f"Rango descriptivo entre tamaños representados: **{vals.min():.2f} a {vals.max():.2f}** "
                 f"(amplitud {vals.max()-vals.min():.2f}).")
    st.caption("La amplitud describe los dominios disponibles, no demuestra diferencias estadísticamente significativas.")

with t3:
    st.subheader("Relación ecológica exploratoria")
    xmet = st.selectbox("Variable explicativa candidata (eje X)",
                        [v for v in METRICAS if v != "promedio_hijos_nacidos_vivos"],
                        format_func=lambda x: METRICAS[x])
    ymet = "promedio_hijos_nacidos_vivos"
    valido = df.dropna(subset=[xmet, ymet]).copy()
    grafico = px.scatter(valido, x=xmet, y=ymet, color="Tamaño de localidad", symbol="Entidad",
                         labels={xmet: METRICAS[xmet], ymet: METRICAS[ymet]},
                         hover_data=["cve_ent", "tamloc", "registros_microdato"])
    st.plotly_chart(grafico, use_container_width=True)
    if len(valido) >= 10 and valido[xmet].nunique() > 1 and valido[ymet].nunique() > 1:
        r = valido[xmet].corr(valido[ymet])
        st.write(f"Correlación descriptiva de Pearson entre dominios representados: **r = {r:.3f}** (n = {len(valido)} dominios).")
    st.caption("Comparación ecológica; dominios de la misma entidad pueden estar correlacionados. "
               "El resultado no es un efecto individual, causal ni una prueba de hipótesis ajustada por diseño de encuesta.")

with t4:
    st.subheader("Evidencia de consultas sobre MongoDB")
    st.markdown("El panel consulta **MongoDB en tiempo real**, no un CSV precargado. "
                "La consulta incluye `$match`, `$project`, `$sort` y `$limit`; la segunda utiliza `$group`.")
    st.code(str(pipeline_dominios(tuple(entidades), tuple(tamanos), 500)), language="python")
    st.write("**Agregación de cobertura por tamaño de localidad**")
    st.code(str(pipeline_conteos_por_tamano(tuple(entidades),tuple(tamanos))), language="python")
    st.dataframe(pd.DataFrame(grupos).rename(columns={"_id":"Tamaño", "dominios":"Dominios", "registros_microdato":"Registros", "poblacion_ponderada":"Población ponderada"}),
                 hide_index=True, use_container_width=True)
    if st.button("Ejecutar agregación de extremos del indicador principal"):
        with MongoClient(MONGO_URI, serverSelectionTimeoutMS=7000) as cli:
            resultado = list(cli[MONGO_DB][col_actual].aggregate(
                pipeline_extremos(metrica, tuple(entidades), tuple(tamanos)), maxTimeMS=15000))
        st.json(resultado)
    st.write("**Agregación MongoDB con `$avg`: media NO ponderada entre dominios**")
    promedio_pipeline = pipeline_promedio_dominios_por_tamano(metrica, tuple(entidades), tuple(tamanos))
    st.code(str(promedio_pipeline), language="python")
    with MongoClient(MONGO_URI, serverSelectionTimeoutMS=7000) as cli:
        promedios_dominios = list(cli[MONGO_DB][col_actual].aggregate(promedio_pipeline, maxTimeMS=15000))
    st.dataframe(pd.DataFrame(promedios_dominios).rename(columns={
        "_id": "Tamaño", "dominios_validos": "Dominios válidos",
        "media_no_ponderada_de_dominios": "Media de dominios (no ponderada)",
        "min": "Mínimo entre dominios", "max": "Máximo entre dominios",
    }), hide_index=True, use_container_width=True)
    st.caption("IMPORTANTE: `$avg` se aplica a cada dominio como una observación. No estima una media o tasa poblacional; "
               "para eso se requieren los componentes y factores de expansión de microdatos. "
               "Sumar registros de microdato sirve para describir la cobertura, no para sumar porcentajes.")

with t5:
    st.subheader("Alcance y advertencias del estudio")
    st.markdown("""
- **Fuente declarada:** Encuesta Intercensal 2025, INEGI, microdatos de personas procesados en la segunda entrega.
- **Universo:** mujeres de 15 a 49 años. **Unidad de análisis de este panel:** dominio territorial entidad × tamaño de localidad.
- **Datos de demostración:** exportación preexistente de 153 dominios con cinco tamaños, sin recalcular el archivo original en este paquete.
- **Cinco vs. cuatro tamaños:** el diseño de tesina propone 4 (<2 500, 2 500–14 999, 15 000–49 999, 50 000+). Para conseguirlos correctamente debe reprocesarse el archivo `personas00.csv` y usar componentes sumables de los estimadores.
- **No estimado:** tasa global de fecundidad, errores estándar, coeficientes de variación e intervalos de confianza. El promedio de hijos nacidos vivos es otra medida.
- **Validez:** revisar reglas de recodificación, factor de expansión, no respuesta, estimadores publicados y método oficial de precisión antes de publicar conclusiones.
- **Comparaciones:** son exploratorias y ecológicas. No permiten inferir causalidad ni diferencias significativas sin análisis adicional.
""")
    st.code("docker compose up --build -d\ndocker compose ps\ndocker compose logs carga", language="bash")
