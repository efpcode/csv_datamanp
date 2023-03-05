import pytest
import pandas as pd
from csv_datamanp.csv_data_manager import data_cleaner, data_subsetter


@pytest.fixture
def df_validator_set():
    df = pd.read_csv(
        "tests/test_data/validator_set.csv", header=0, sep=",", keep_default_na=False
    )
    return df

@pytest.fixture
def df_subsetter_sets():
    df_big = pd.read_csv("tests/test_data/big_dataset.csv", header=0,
                         sep=",", keep_default_na=False)
    df_small = pd.read_csv("tests/test_data/small_dataset.csv", header=0,
                           sep=",", keep_default_na=False)
    df_expected = pd.read_csv("tests/test_data/expected_outcome.csv",
                              header=0, sep=",")
    return df_big, df_small, df_expected
def test_validator(df_validator_set):
    df_test = df_validator_set
    s_test = data_cleaner(df_test)
    assert all(s_test.values == df_test[df_test.columns[1]].values) == True

def test_subsetter(df_subsetter_sets):
    df_big, df_small, df_expected = df_subsetter_sets
    new_df = data_subsetter(df_big, df_small)
    assert all(df_expected == new_df) == True


