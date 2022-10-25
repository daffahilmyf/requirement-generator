import pandas as pd
from typing import List
from pandas import DataFrame


def requirement_txt(path: str, separator: str, title: List[str])-> DataFrame:
    req_df = pd.read_csv(path, sep=separator, names=title, on_bad_lines="skip")

    return req_df

