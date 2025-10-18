import pandas as pd


def load_data(path):
    """
    Load a csv file.

    Parameters
    ----------
    path : str
    """
    return pd.read_csv(path, sep=":")
