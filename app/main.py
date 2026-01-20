import streamlit as st

from src.data import load_data, summarize

st.set_page_config(
    page_title="Dashboard KPI IAS 2025",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Dashboard KPI IAS 2025")
st.write("Data diambil dari Google Sheets.")

with st.spinner("Memuat data..."):
    df = load_data()

st.dataframe(df, use_container_width=True)

st.subheader("Ringkasan numerik")
summary = summarize(df)
st.dataframe(summary, use_container_width=True)
