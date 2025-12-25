from pathlib import Path
import pandas as pd
import yfinance as yf


def fetch_data(symbol: str, start_date: str, raw_dir: Path) -> Path:

    if raw_dir.exists():
        return raw_dir / f"{symbol}.csv"

    raw_dir.mkdir(parents=True, exist_ok=True)

    df = yf.download(symbol, start=start_date)

    if df.empty:
        raise ValueError(f"No data downloaded for {symbol}")

    file_path = raw_dir / f"{symbol}.csv"
    df.to_csv(file_path)

    return file_path


def load_data(symbol: str, raw_dir: Path) -> pd.DataFrame:
    file_path = raw_dir / f"{symbol}.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    df = pd.read_csv(file_path)

    # ✅ Normalize data
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")

    # ✅ Force numeric columns
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

