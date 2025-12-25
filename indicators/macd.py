import pandas as pd

def macd(df: pd.DataFrame) -> pd.Series:
    ema_fast = df["Close"].ewm(span=12, adjust=False).mean()
    ema_slow = df["Close"].ewm(span=26, adjust=False).mean()
    return ema_fast - ema_slow
