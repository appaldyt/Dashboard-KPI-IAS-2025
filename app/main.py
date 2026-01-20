import sys
from pathlib import Path

import streamlit as st

#Melakukan update data

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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
