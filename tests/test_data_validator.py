import pytest
import pandas as pd
from csv_datamanp.csv_data_filter import data_filter


@pytest.fixture
def df_validator_set():
    df = pd.read_csv(
        "tests/test_data/validator_set.csv", header=0, sep=",", keep_default_na=False
    )
    return df


def test_validator(df_validator_set):
    df_test = df_validator_set
    s_test = data_filter(df_test)
    assert all(s_test.values == df_test[df_test.columns[1]].values) == True
