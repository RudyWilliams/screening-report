import pandas as pd


def read_data_from_excel(filepath):
    return pd.read_excel(filepath, index_col=0)
