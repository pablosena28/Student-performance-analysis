"""Executa uma análise descritiva do desempenho estudantil."""

from pathlib import Path
import pandas as pd

from src.data_cleaning import SCORE_COLUMNS, prepare_student_data

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "students_performance.csv"


def main() -> None:
    raw = pd.read_csv(DATA_PATH)
    df = prepare_student_data(raw)

    print("=== VISÃO GERAL ===")
    print(f"Estudantes: {len(df)}")
    print(f"Valores ausentes: {raw.isna().sum().sum()}")
    print(f"Duplicatas completas: {raw.duplicated().sum()}")

    print("\n=== MÉDIAS POR ÁREA ===")
    print(df[SCORE_COLUMNS].mean().round(2))

    print("\n=== CURSO PREPARATÓRIO ===")
    print(
        df.groupby("test preparation course")[
            SCORE_COLUMNS + ["average score"]
        ].mean().round(2)
    )

    print("\n=== TIPO DE ALMOÇO ===")
    print(
        df.groupby("lunch")[
            SCORE_COLUMNS + ["average score"]
        ].mean().round(2)
    )

    print("\n=== ESCOLARIDADE PARENTAL ===")
    print(
        df.groupby("parental level of education")["average score"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\n=== CORRELAÇÕES ===")
    print(df[SCORE_COLUMNS].corr().round(3))


if __name__ == "__main__":
    main()
