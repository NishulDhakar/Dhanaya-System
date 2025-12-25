import pandas as pd
import yfinance as yf
import os

def fetch_data(symbol, start_date):
    if not os.path.exists("data/raw"):
        os.makedirs("data/raw")

    df = yf.download(symbol, start=start_date)

    if df.empty:
        print("No data downloaded")
        return

    df.to_csv("data/raw/" + symbol + ".csv")
    print("Data saved")

def load_data(symbol):
    return pd.read_csv("data/raw/" + symbol + ".csv")
