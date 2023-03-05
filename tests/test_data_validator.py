import pytest
import pandas as pd
from csv_datamanp.csv_data_manager import data_cleaner, data_subsetter, data_mapper


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

@pytest.fixture
def df_map_sets():
    df_lookup = pd.read_csv("tests/test_data/look_up_dataset.csv", header=0,
                            sep=",")
    df_expected = pd.read_csv("tests/test_data/look_up_outcome.csv", header=0,
                            sep=",")
    return df_lookup, df_expected


def test_validator(df_validator_set):
    df_test = df_validator_set
    s_test = data_cleaner(df_test)
    assert all(s_test.values == df_test[df_test.columns[1]].values) == True

def test_subsetter(df_subsetter_sets):
    df_big, df_small, df_expected = df_subsetter_sets
    new_df = data_subsetter(df_big, df_small)
    assert all(df_expected == new_df) == True

def test_mapper(df_map_sets):
    df_lookup, df_expected = df_map_sets
    df_new = data_mapper(df_lookup, df_expected)
    assert all(df_new["Expected Outcome"] == df_new["Mapped Values"]) == True
