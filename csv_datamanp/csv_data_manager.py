import re
import pandas as pd


def data_cleaner(df: pd.DataFrame, column_name: str = None) -> pd.Series:
    if not column_name:
        column_name = df.columns[0]
    pattern = re.compile(r"[0-9a-zA-Z]+")
    s = df[column_name].apply(lambda x: "".join(re.findall(pattern, x)).upper())
    return s


def data_subsetter(
    df_big: pd.DataFrame, df_sub: pd.DataFrame, on_key: str = None
) -> pd.DataFrame:
    if not on_key:
        on_key = df_sub.columns[0]
    #
    df_null = pd.DataFrame(columns=["Big Set", "Small Set", "Error Message"])
    try:
        error_msg = f"{df_big.shape} has fewer rows than {df_sub.shape}"
        if not (on_key in df_big.columns) or not (on_key in df_sub.columns):
            raise ValueError(f"{on_key} must be present in both dataset")

        assert (df_big.shape > df_sub.shape) == True, error_msg
    except AssertionError as e:
        print(e)
        data = [df_big.shape, df_sub.shape, error_msg]
        new_dict = {k: [data[idx]] for idx, k in enumerate(df_null.columns)}
        df_null = df_null.from_dict(new_dict)
        return df_null

    except AttributeError as e:
        print(e)
        error_msg = "Data input are not of expected type: pd.DataFrame"
        data = [type(df_big), type(df_sub), error_msg]
        new_dict = {k: [data[idx]] for idx, k in enumerate(df_null.columns)}
        df_null = df_null.from_dict(new_dict)
        return df_null

    except ValueError as e:
        print(e)
        data = [df_big.columns, df_sub.columns, e]
        new_dict = {k: [data[idx]] for idx, k in enumerate(df_null.columns)}
        df_null = df_null.from_dict(new_dict)
        return df_null

    else:
        new_df = pd.merge(df_big, df_sub, how="inner", on=on_key)
        return new_df


def data_mapper(df_dict: pd.DataFrame, df_sample: pd.DataFrame) -> \
        pd.DataFrame:

    df_null = pd.DataFrame(columns=["Data input", "Error Message"])

    try:
        assert df_dict.shape[1] == 2, "Mapper is expected 2 columns in look " \
                                      "up table"

    except AssertionError as e:
        df_null = df_null.from_dict({"Data input": [df_dict.shape], "Error Message": e})
        return df_null

    else:
        d1 = df_dict.set_index([df_dict.columns[0]]).to_dict()
        s_map = df_sample[df_sample.columns[0]].apply(
            lambda x: d1[df_dict.columns[1]].get(x, "Not Found"))
        df_sample["Mapped Values"] = s_map
        return df_sample




