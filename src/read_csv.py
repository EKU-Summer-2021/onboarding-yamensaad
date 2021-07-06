"""
This module handles csv files
"""
import pandas as pd


def read_csv(path):
    """
   this function read csv file.
    """
    df_csp = pd.read_csv(path)
    return df_csp
