import pandas as pd

from src.data_cleaning import prepare_student_data


def test_prepare_student_data_creates_average_and_pass_flag():
    sample = pd.DataFrame(
        {
            "math score": [60, 50],
            "reading score": [70, 80],
            "writing score": [80, 90],
        }
    )

    result = prepare_student_data(sample)

    assert result.loc[0, "average score"] == 70.0
    assert result.loc[0, "passed_all_60"]
    assert not result.loc[1, "passed_all_60"]
