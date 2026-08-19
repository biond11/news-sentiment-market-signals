"""Entry point Streamlit.

Avvio locale:
    streamlit run dashboard/app.py

Le pagine vere e proprie sono in dashboard/pages/ (vedi docs/project_steps.md, Fase 6).
"""

import streamlit as st

st.set_page_config(page_title="News Sentiment vs Market Signals", layout="wide")
st.title("News Sentiment vs Market Signals")
st.write(
    "Usa il menu a sinistra per navigare tra le pagine. "
    "Questa home page e' un placeholder: sostituiscila con una panoramica del progetto."
)
