"""Funções de preparação do dataset de desempenho estudantil."""

from __future__ import annotations
import pandas as pd

SCORE_COLUMNS = ["math score", "reading score", "writing score"]


def prepare_student_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cria métricas derivadas sem alterar os dados originais."""
    data = df.copy()
    data["average score"] = data[SCORE_COLUMNS].mean(axis=1).round(2)
    data["passed_all_60"] = (data[SCORE_COLUMNS] >= 60).all(axis=1)
    return data
