"""Client per i prezzi storici/recenti via Stooq (nessuna API key richiesta).

Da implementare (vedi docs/project_steps.md, Fase 1.4):
    Pattern endpoint: https://stooq.com/q/d/l/?s={ticker}&d1={YYYYMMDD}&d2={YYYYMMDD}&i=d
    Esempio ticker: "spy.us" per l'ETF S&P 500 (non dimenticare il suffisso di mercato).
"""


def fetch_daily_prices(ticker: str, start_date: str, end_date: str):
    """TODO: implementare con pandas.read_csv(url), vedi Fase 1.4 in docs/project_steps.md"""
    raise NotImplementedError
