"""FastAPI entrypoint.

Avvio locale:
    uvicorn api.main:app --reload

Endpoint da implementare (vedi docs/project_steps.md, Fase 4):
    POST /ingest/run            -> pull NewsAPI + Stooq, scoring, scrittura DB (Fase 4.3)
    GET  /articles/{id}/similar -> ricerca semantica via pgvector (Fase 4.4)
    GET  /sentiment/daily       -> serve il mart aggregato a Streamlit (Fase 4.3/6)
"""

from fastapi import FastAPI

app = FastAPI(title="News Sentiment vs Market Signals API")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO (Fase 4.3): @app.post("/ingest/run")
# TODO (Fase 4.4): @app.get("/articles/{article_id}/similar")
# TODO (Fase 4.3/6): @app.get("/sentiment/daily")
