from pathlib import Path

from data.data_loader import fetch_data, load_data
from indicators.sma import sma
from indicators.rsi import rsi
from indicators.macd import macd
from strategies.rsi_strategy import RSIStrategy


# ------------------
# Config
# ------------------
SYMBOL = "SUZLON.NS"
START_DATE = "2025-01-01"

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def main():
    # 1. Fetch raw data
    fetch_data(SYMBOL, START_DATE, RAW_DIR)

    # 2. Load raw data
    df = load_data(SYMBOL, RAW_DIR)

    # 3. Compute indicators
    df["SMA_14"] = sma(df, 14)
    df["RSI_14"] = rsi(df, 14)
    df["MACD"] = macd(df)

    # 4. Drop NaNs from indicators
    df = df.dropna()

    # 5. Save processed data
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / f"{SYMBOL}.csv", index=False)

    # 6. Run strategy
    strategy = RSIStrategy()
    result = strategy.generate_signal(df)

    # 7. Print decision (ONLY for now)
    print("Latest Signal:", result["signal"])
    print("Reason:", result["reason"])

if __name__ == "__main__":
    main()
