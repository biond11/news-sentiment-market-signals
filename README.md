# News Sentiment vs Market Signals

Pipeline end-to-end che misura la **correlazione** (non causalita', vedi `docs/project_brief.md` sezione 2) tra sentiment/credibilita' della copertura mediatica e movimenti di mercato.

## Stack
MongoDB (raw) -> Postgres + pgvector (warehouse) -> dbt (trasformazioni) -> modelli NN (sentiment, credibilita', embeddings) -> FastAPI (servizio) -> Streamlit (dashboard).

## Documentazione
- [`docs/project_brief.md`](docs/project_brief.md) - architettura, domanda di business, spiegazione correlazione vs causalita'
- [`docs/project_steps.md`](docs/project_steps.md) - guida step-by-step con link e risultati attesi

## Quick start

1. Copia `.env.example` in `.env` e compila i valori (chiave NewsAPI, credenziali DB)
2. `docker compose up -d` per avviare Postgres (con pgvector) e MongoDB
3. `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
4. `uvicorn api.main:app --reload` - verifica su http://localhost:8000/docs
5. `streamlit run dashboard/app.py` - verifica che l'app si apra

## Stato del progetto

- [x] Fase 0 - setup scaffold
- [ ] Fase 1 - import dataset storici
- [ ] Fase 2 - modelli NN
- [ ] Fase 3 - dbt
- [ ] Fase 4 - ingestion live
- [ ] Fase 5 - analisi
- [ ] Fase 6 - dashboard
- [ ] Fase 7 - finalizzazione

## Licenza / uso
Progetto personale a scopo di portfolio.
