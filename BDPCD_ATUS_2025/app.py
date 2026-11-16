import os
import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from pymongo import MongoClient
from pymongo.errors import PyMongoError

st.set_page_config(page_title="ATUS 2025 | Dashboard", page_icon="🚦", layout="wide")
st.title("🚦 Análisis de accidentes de tránsito terrestre | México 2025")
st.caption("ATUS 2025 · MongoDB Atlas · Cartografía del Marco Geoestadístico de INEGI")

DB, COLL = "bdpcd_atus", "accidentes_2025"
BASE_DIR = Path(__file__).resolve().parent
GEO_DIR = BASE_DIR / "data" / "geografia"

VEHICLES = ["AUTOMOVIL","CAMPASAJ","MICROBUS","PASCAMION","OMNIBUS","TRANVIA","CAMIONETA","CAMION","TRACTOR","FERROCARRI","MOTOCICLET","BICICLETA","OTROVEHIC"]
DEAD = ["CONDMUERTO","PASAMUERTO","PEATMUERTO","CICLMUERTO","OTROMUERTO"]
INJURED = ["CONDHERIDO","PASAHERIDO","PEATHERIDO","CICLHERIDO","OTROHERIDO"]
MONTHS = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

uri = os.getenv("MONGODB_URI")
if not uri:
    st.error("No se encontró MONGODB_URI. Configúrala en PowerShell antes de iniciar el dashboard.")
    st.code('$env:MONGODB_URI = Read-Host "Pega tu URI de MongoDB Atlas"', language="powershell")
    st.stop()

@st.cache_resource
def connect(connection_string):
    client = MongoClient(connection_string, serverSelectionTimeoutMS=15000)
    client.admin.command("ping")
    db = client[DB]
    return client, db[COLL], db["catalogo_entidades"], db["catalogo_municipios"]

try:
    client, col, ent_col, mun_col = connect(uri)
    total_all = col.count_documents({})
    entity_docs = list(ent_col.find({}, {"_id": 0, "CVE_ENT": 1, "NOM_ENT": 1}))
    municipality_docs = list(mun_col.find({}, {"_id": 0, "CVEGEO": 1, "CVE_ENT": 1, "NOM_MUN": 1}))
except Exception as e:
    st.error(f"No fue posible conectar con MongoDB: {e}")
    st.stop()

state_names = {str(x["CVE_ENT"]).zfill(2): x["NOM_ENT"] for x in entity_docs}
municipality_names = {str(x["CVEGEO"]).zfill(5): x["NOM_MUN"] for x in municipality_docs}
municipality_state = {str(x["CVEGEO"]).zfill(5): str(x["CVE_ENT"]).zfill(2) for x in municipality_docs}

def distinct(field):
    vals = [v for v in col.distinct(field) if v is not None and str(v).strip()]
    return sorted(vals, key=lambda v: str(v))

def sum_expr(fields):
    return {"$add": [{"$convert": {"input": {"$ifNull": [f"${f}", 0]}, "to": "double", "onError": 0, "onNull": 0}} for f in fields]}

def group_count(match, field):
    return list(col.aggregate([{"$match": match}, {"$group": {"_id": f"${field}", "total": {"$sum": 1}}}, {"$sort": {"total": -1}}], allowDiskUse=True))

def group_sum(match, field, fields):
    return list(col.aggregate([{"$match": match}, {"$group": {"_id": f"${field}", "total": {"$sum": sum_expr(fields)}}}, {"$sort": {"total": -1}}], allowDiskUse=True))

def label(v):
    return "Sin dato" if v is None or str(v).strip() == "" else str(v)

def load_geojson(filename):
    path = GEO_DIR / filename
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

with st.sidebar:
    st.header("Filtros")
    months = sorted([int(v) for v in distinct("MES") if str(v).isdigit()]) or list(range(1, 13))
    month_names = [MONTHS.get(m, str(m)) for m in months]
    chosen_month_names = st.multiselect("Mes", month_names, default=month_names)
    chosen_months = [m for m in months if MONTHS.get(m, str(m)) in chosen_month_names]

    state_codes = sorted(state_names.keys())
    if not state_codes:
        state_codes = sorted({str(v).zfill(2) for v in distinct("CVE_ENT")})
    state_labels = {code: f"{state_names.get(code, 'Entidad ' + code)}" for code in state_codes}
    chosen_state_names = st.multiselect(
        "Entidad federativa",
        [state_labels[c] for c in state_codes],
        default=[state_labels[c] for c in state_codes]
    )
    chosen_states = [c for c in state_codes if state_labels[c] in chosen_state_names]

    types = distinct("TIPACCID")
    chosen_types = st.multiselect("Tipo de accidente", [str(v) for v in types], default=[str(v) for v in types])
    causes = distinct("CAUSAACCI")
    chosen_causes = st.multiselect("Causa registrada", [str(v) for v in causes], default=[str(v) for v in causes])

    st.divider()
    st.subheader("Detalle municipal")
    municipal_state_label = st.selectbox("Estado", ["Selecciona un estado"] + [state_labels[c] for c in state_codes])
    selected_state_code = None
    if municipal_state_label != "Selecciona un estado":
        selected_state_code = next(c for c in state_codes if state_labels[c] == municipal_state_label)
        valid_municipalities = sorted(
            [(code, name) for code, name in municipality_names.items() if municipality_state.get(code) == selected_state_code],
            key=lambda x: x[1]
        )
        municipality_labels = ["Todos los municipios"] + [f"{name} ({code})" for code, name in valid_municipalities]
        selected_municipality_label = st.selectbox("Municipio", municipality_labels)
        selected_municipality = None
        if selected_municipality_label != "Todos los municipios":
            selected_municipality = selected_municipality_label.rsplit("(", 1)[-1].rstrip(")")
    else:
        selected_municipality = None
    st.caption(f"Colección: {DB}.{COLL}")

match = {
    "MES": {"$in": chosen_months},
    "CVE_ENT": {"$in": chosen_states},
    "TIPACCID": {"$in": [next((v for v in types if str(v) == s), s) for s in chosen_types]},
    "CAUSAACCI": {"$in": [next((v for v in causes if str(v) == s), s) for s in chosen_causes]},
}
if selected_municipality:
    match["CVEGEO"] = selected_municipality

try:
    n = col.count_documents(match)
    def total_fields(fields):
        result = list(col.aggregate([{"$match": match}, {"$group": {"_id": None, "total": {"$sum": sum_expr(fields)}}}], allowDiskUse=True))
        return int((result[0]["total"] if result else 0) or 0)
    deaths, injuries, vehicles = total_fields(DEAD), total_fields(INJURED), total_fields(VEHICLES)
except PyMongoError as e:
    st.error(f"Error al consultar MongoDB: {e}")
    st.stop()

if n == 0:
    st.warning("No hay registros con los filtros seleccionados.")
    st.stop()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Accidentes", f"{n:,}", help=f"Total general: {total_all:,}")
k2.metric("Fallecidos*", f"{deaths:,}")
k3.metric("Lesionados*", f"{injuries:,}")
k4.metric("Registros de vehículos**", f"{vehicles:,}")
st.caption("* Suma de campos de víctimas por categoría. ** Suma de campos de vehículos; puede superar los accidentes porque puede haber varios vehículos por evento.")

c1, c2 = st.columns(2)
with c1:
    data = group_count(match, "MES")
    df = pd.DataFrame([{"Mes": MONTHS.get(int(x["_id"]), label(x["_id"])), "Accidentes": x["total"], "orden": int(x["_id"])} for x in data if x["_id"] is not None])
    if not df.empty:
        df = df.sort_values("orden")
        st.plotly_chart(px.bar(df, x="Mes", y="Accidentes", title="Accidentes por mes"), use_container_width=True)
with c2:
    data = group_count(match, "TIPACCID")
    df_type = pd.DataFrame([{"Tipo de accidente": label(x["_id"]), "Accidentes": x["total"]} for x in data])
    if not df_type.empty:
        st.plotly_chart(px.bar(df_type.head(12).sort_values("Accidentes"), x="Accidentes", y="Tipo de accidente", orientation="h", title="Accidentes por tipo (12 principales)"), use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    data = group_count(match, "CVE_ENT")
    df_state = pd.DataFrame([{"Entidad federativa": state_names.get(str(x["_id"]).zfill(2), str(x["_id"])), "Accidentes": x["total"]} for x in data])
    if not df_state.empty:
        st.plotly_chart(px.bar(df_state.head(15).sort_values("Accidentes"), x="Accidentes", y="Entidad federativa", orientation="h", title="Entidades con más accidentes (15 principales)"), use_container_width=True)
with c2:
    data = group_count(match, "CAUSAACCI")
    df_cause = pd.DataFrame([{"Causa registrada": label(x["_id"]), "Accidentes": x["total"]} for x in data])
    if not df_cause.empty:
        st.plotly_chart(px.bar(df_cause.head(10).sort_values("Accidentes"), x="Accidentes", y="Causa registrada", orientation="h", title="Accidentes por causa registrada"), use_container_width=True)

# Mapa nacional: polígonos estatales INEGI, sin marcadores ni capitales.
st.subheader("Mapa nacional de accidentes por entidad federativa")
st.caption("El territorio de cada estado se colorea según los registros que cumplen los filtros.")
entities_geo = load_geojson("entidades.geojson")
if entities_geo:
    map_rows = list(col.aggregate([
        {"$match": match},
        {"$group": {"_id": "$CVE_ENT", "Accidentes": {"$sum": 1}}}
    ], allowDiskUse=True))
    map_df = pd.DataFrame([
        {"CVE_ENT": str(x["_id"]).zfill(2), "Accidentes": int(x["Accidentes"])}
        for x in map_rows if x.get("_id") is not None
    ])
    map_df = pd.DataFrame({"CVE_ENT": state_codes}).merge(map_df, on="CVE_ENT", how="left")
    map_df["Entidad"] = map_df["CVE_ENT"].map(state_names)
    map_df["Accidentes"] = map_df["Accidentes"].fillna(0).astype(int)
    try:
        fig_map = px.choropleth_map(
            map_df, geojson=entities_geo, locations="CVE_ENT",
            featureidkey="properties.cvegeo", color="Accidentes",
            hover_name="Entidad", hover_data={"CVE_ENT": True, "Accidentes": ":,"},
            color_continuous_scale="YlOrRd", map_style="carto-positron",
            center={"lat": 23.7, "lon": -102.2}, zoom=3.0, opacity=0.72,
            title="Accidentes registrados por estado"
        )
        fig_map.update_layout(margin={"r": 0, "t": 45, "l": 0, "b": 0}, height=620)
        st.plotly_chart(fig_map, use_container_width=True)
    except Exception as e:
        st.error(f"No se pudo construir el mapa estatal. Revisa la versión de Plotly y las propiedades GeoJSON: {e}")
else:
    st.warning("No se encuentra data/geografia/entidades.geojson. Ejecuta scripts/descargar_geometrias_inegi.py.")

# Mapa municipal para la entidad elegida en el filtro «Detalle municipal».
st.subheader("Mapa de accidentes por municipio")
if selected_state_code is None:
    st.info("Selecciona un estado en la sección «Detalle municipal» de la barra lateral para mostrar sus municipios.")
else:
    municipal_geo = load_geojson(f"municipios_{selected_state_code}.geojson")
    if municipal_geo:
        municipal_match = dict(match)
        municipal_match["CVE_ENT"] = selected_state_code
        municipal_rows = list(col.aggregate([
            {"$match": municipal_match},
            {"$group": {"_id": "$CVEGEO", "Accidentes": {"$sum": 1}}}
        ], allowDiskUse=True))
        counts = pd.DataFrame([
            {"CVEGEO": str(x["_id"]).zfill(5), "Accidentes": int(x["Accidentes"])}
            for x in municipal_rows if x.get("_id") is not None
        ])
        state_municipalities = [(code, name) for code, name in municipality_names.items() if municipality_state.get(code) == selected_state_code]
        municipal_df = pd.DataFrame(state_municipalities, columns=["CVEGEO", "Municipio"])
        municipal_df = municipal_df.merge(counts, on="CVEGEO", how="left")
        municipal_df["Accidentes"] = municipal_df["Accidentes"].fillna(0).astype(int)
        if not municipal_df.empty:
            try:
                fig_mun = px.choropleth_map(
                    municipal_df, geojson=municipal_geo, locations="CVEGEO",
                    featureidkey="properties.cvegeo", color="Accidentes",
                    hover_name="Municipio", hover_data={"CVEGEO": True, "Accidentes": ":,"},
                    color_continuous_scale="YlOrRd", map_style="carto-positron",
                    center={"lat": 23.7, "lon": -102.2}, zoom=4.2, opacity=0.72,
                    title=f"Accidentes por municipio: {state_names.get(selected_state_code, selected_state_code)}"
                )
                fig_mun.update_layout(margin={"r": 0, "t": 45, "l": 0, "b": 0}, height=620)
                st.plotly_chart(fig_mun, use_container_width=True)
                st.caption("Los municipios sin registros para los filtros seleccionados se representan con cero.")
            except Exception as e:
                st.error(f"No se pudo construir el mapa municipal. Revisa la versión de Plotly y las propiedades GeoJSON: {e}")
    else:
        st.warning(f"No se encuentra data/geografia/municipios_{selected_state_code}.geojson.")

st.subheader("Fallecidos y lesionados por tipo de accidente")
dead = group_sum(match, "TIPACCID", DEAD)
inj = group_sum(match, "TIPACCID", INJURED)
df_dead = pd.DataFrame([{"Tipo de accidente": label(x["_id"]), "Fallecidos": x["total"]} for x in dead])
df_inj = pd.DataFrame([{"Tipo de accidente": label(x["_id"]), "Lesionados": x["total"]} for x in inj])
df_victims = df_dead.merge(df_inj, on="Tipo de accidente", how="outer").fillna(0)
if not df_victims.empty:
    long = df_victims.melt(id_vars="Tipo de accidente", var_name="Categoría", value_name="Personas")
    fig = px.bar(long, x="Tipo de accidente", y="Personas", color="Categoría", barmode="group", title="Víctimas por tipo de accidente")
    fig.update_layout(xaxis_title="", xaxis_tickangle=-35)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Vehículos involucrados por categoría")
projection = {f: {"$convert": {"input": {"$ifNull": [f"${f}", 0]}, "to": "double", "onError": 0, "onNull": 0}} for f in VEHICLES}
group = {"_id": None, **{f: {"$sum": f"${f}"} for f in VEHICLES}}
rows = list(col.aggregate([{"$match": match}, {"$project": projection}, {"$group": group}], allowDiskUse=True))
if rows:
    df_veh = pd.DataFrame([{"Tipo de vehículo": f, "Registros": int(rows[0].get(f, 0) or 0)} for f in VEHICLES]).query("Registros > 0").sort_values("Registros", ascending=False)
    st.plotly_chart(px.bar(df_veh, x="Tipo de vehículo", y="Registros", title="Registros por categoría de vehículo"), use_container_width=True)

with st.expander("Consultar tabla por tipo de accidente"):
    st.dataframe(df_type, use_container_width=True, hide_index=True)
with st.expander("Consultar tabla de víctimas"):
    st.dataframe(df_victims, use_container_width=True, hide_index=True)

st.divider()
st.caption("Fuente de datos: ATUS 2025, INEGI. Cartografía: Marco Geoestadístico del INEGI. Análisis descriptivo; las asociaciones observadas no implican causalidad.")
