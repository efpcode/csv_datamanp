import re
import pandas as pd


def data_filter(df: pd.DataFrame, column_name: str = None) -> pd.Series:
    if not column_name:
        column_name = df.columns[0]
    pattern = re.compile(r"[0-9a-zA-Z]+")
    s = df[column_name].apply(lambda x: "".join(re.findall(pattern, x)).upper())
    return s
