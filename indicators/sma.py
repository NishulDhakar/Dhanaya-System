import pandas as pd

def sma(df : pd.DataFrame, window : int) -> pd.DataFrame:
    return df['Close'].rolling(window=window).mean()