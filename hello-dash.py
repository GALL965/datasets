import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Video Games Analytics Dashboard", page_icon="🎮", layout="wide"
)

st.title("Video Games Market & Analytics Dashboard")
st.markdown(
    "Exploración interactiva de datos globales de videojuegos, tendencias y métricas clave."
)
st.divider()

@st.cache_data
def load_data():
    df = pd.read_csv("Video Games Data.csv")
    return df


df = load_data()

st.sidebar.header("Panel de Control")
st.sidebar.markdown("Filtra la información para refinar el análisis.")

st.sidebar.info(f"Total de registros analizados: {len(df):,}")

# --- SECCIÓN 1: MÉTRICAS PRINCIPALES (KPIs) ---
# Creamos columnas para mostrar tarjetas con indicadores clave
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total de Juegos en la Base", value=f"{df.shape[0]:,}"
    )

with col2:
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        val_promedio = round(df[numeric_cols[0]].mean(), 2)
        st.metric(label=f"Promedio ({numeric_cols[0]})", value=val_promedio)
    else:
        st.metric(label="Columnas de Datos", value=len(df.columns))

with col3:
    st.metric(label="Variables Registradas", value=df.shape[1])

st.markdown("")  # Espaciador

st.subheader("Análisis Gráfico de Tendencias")

if len(numeric_cols) >= 2:
    st.bar_chart(df[numeric_cols[:2]].head(15), use_container_width=True)
else:
    st.line_chart(df.select_dtypes(include=["number"]).head(15))

st.divider()

st.subheader("Explorador de Registros Detallados")

num_filas = st.slider(
    "Selecciona cuántas filas deseas visualizar:", 5, 50, 10
)

st.dataframe(df.head(num_filas), use_container_width=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Desarrollado para Análisis de Datos e Ingeniería de Software 🚀</p>",
    unsafe_allow_html=True,
)