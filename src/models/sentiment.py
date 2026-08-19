"""Sentiment classifier, allenato su Financial PhraseBank.

Da implementare (vedi docs/project_steps.md, Fase 2.2-2.4):
    - train_baseline: TF-IDF + LogisticRegression
    - train_neural: embedding (sentence-transformers) + piccola rete neurale
    - confronta le metriche delle due versioni prima di scegliere quale usare in produzione
"""


def train_baseline(texts, labels):
    """TODO: baseline TF-IDF + LogisticRegression, Fase 2.2"""
    raise NotImplementedError


def train_neural(texts, labels):
    """TODO: embedding + piccola rete neurale, Fase 2.3"""
    raise NotImplementedError


def predict_sentiment(text: str) -> float:
    """TODO: carica il modello allenato e restituisce uno score, usato in Fase 4.3"""
    raise NotImplementedError
