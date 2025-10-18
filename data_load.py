import pandas as pd


def load_data(path):
    """
    Load a csv file.
    """
    return pd.read_csv(path)
