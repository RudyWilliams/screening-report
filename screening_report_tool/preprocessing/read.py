from pathlib import Path
from typing import Union

import pandas as pd


def create_filepath(
    root: str, month: str, year: Union[str, int], filename: str
) -> Path:
    month = month.capitalize()
    return Path(f"{root}/{month} {year}/{filename}")


def read_data_from_excel(filepath: Path) -> pd.DataFrame:
    return pd.read_excel(filepath, index_col=0)

