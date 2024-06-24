from typing import List
import pandas as pd
from pandas import DataFrame


def nan_removal(dataset: DataFrame, desired_column: List[str])-> DataFrame:
    if dataset is None:
        raise Exception("Please insert the dataset!")
    
    if not desired_column:
        raise Exception("Please insert the column name!")
    
    data_cleansing = dataset.dropna(subset=desired_column)

    return data_cleansing
    
def undesired_str_removal(dataset: DataFrame, regex: str)-> DataFrame:
    if dataset is None:
        raise Exception("Please insert the dataset!")
    
    if not regex:
        raise Exception("Please insert the regex!")

    return 
