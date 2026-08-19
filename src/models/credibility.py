"""Credibility classifier, allenato sul Fake/Real News Dataset.

Da implementare (vedi docs/project_steps.md, Fase 2.2-2.4):
    - stesso pattern di sentiment.py: baseline prima, poi rete neurale, poi confronto
"""


def train_baseline(texts, labels):
    """TODO: baseline TF-IDF + LogisticRegression, Fase 2.2"""
    raise NotImplementedError


def train_neural(texts, labels):
    """TODO: embedding + piccola rete neurale, Fase 2.3"""
    raise NotImplementedError


def predict_credibility(text: str) -> float:
    """TODO: carica il modello allenato e restituisce uno score, usato in Fase 4.3"""
    raise NotImplementedError
