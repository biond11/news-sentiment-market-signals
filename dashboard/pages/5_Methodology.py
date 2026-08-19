import streamlit as st

st.title("Metodologia e limiti")
st.warning(
    "Questo progetto misura CORRELAZIONE, non causalita'. "
    "Vedi docs/project_brief.md sezione 2 per la spiegazione completa: confondenti comuni, "
    "causalita' inversa, e perche' il linguaggio dei risultati usa 'associato a' e non 'causa'."
)
st.info("TODO (Fase 6.2, docs/project_steps.md): riporta qui i limiti specifici emersi durante l'analisi.")
