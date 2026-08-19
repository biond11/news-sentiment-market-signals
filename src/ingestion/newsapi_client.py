"""Client per NewsAPI (https://newsapi.org/docs).

Da implementare (vedi docs/project_steps.md, Fase 4.2):
    - funzione che chiama /v2/everything o /v2/top-headlines
    - gestione della chiave da NEWSAPI_KEY (.env)
    - restituisce una lista di articoli normalizzata (title, description, publishedAt, source)

Nota: il piano free e' solo dev/test, non per produzione pubblica.
"""

import os

NEWSAPI_BASE_URL = "https://newsapi.org/v2"


def fetch_top_headlines(category: str, language: str = "en"):
    """TODO: implementare la chiamata reale, vedi Fase 4.2 in docs/project_steps.md"""
    raise NotImplementedError
