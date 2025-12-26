from pathlib import Path

# ------------------
# Data
# ------------------
from data.data_loader import fetch_data, load_data

# ------------------
# Indicators
# ------------------
from indicators.sma import sma
from indicators.rsi import rsi
from indicators.macd import macd

# ------------------
# Strategy
# ------------------
from strategies.rsi_strategy import RSIStrategy

# ------------------
# Trading Core
# ------------------
from portfolio.portfolio import Portfolio
from risk.risk_manager import RiskManager
from broker.simulator import BrokerSimulator
from engine.paper_trader import PaperTrader

# ------------------
# Analytics
# ------------------
from analytics.equity_curve import EquityCurve
from analytics.metrics import (
    win_rate,
    avg_win_loss,
    max_drawdown,
    sharpe_ratio
)

# ======================================================
# CONFIG
# ======================================================
SYMBOL = "SUZLON.NS"
START_DATE = "2025-01-01"

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

INITIAL_CASH = 100_000
MAX_RISK_PER_TRADE = 20_000


# ======================================================
# MAIN PIPELINE
# ======================================================
def main():
    # --------------------------------------------------
    # 1. Fetch & load raw data
    # --------------------------------------------------
    fetch_data(SYMBOL, START_DATE, RAW_DIR)
    df = load_data(SYMBOL, RAW_DIR)

    # --------------------------------------------------
    # 2. Compute indicators
    # --------------------------------------------------
    df["SMA_14"] = sma(df, 14)
    df["RSI_14"] = rsi(df, 14)
    df["MACD"] = macd(df)

    df = df.dropna()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / f"{SYMBOL}.csv", index=False)

    # --------------------------------------------------
    # 3. Initialize components
    # --------------------------------------------------
    strategy = RSIStrategy()
    portfolio = Portfolio(initial_cash=INITIAL_CASH)
    risk_manager = RiskManager(max_risk_per_trade=MAX_RISK_PER_TRADE)
    broker = BrokerSimulator()
    equity_curve = EquityCurve(initial_cash=INITIAL_CASH)

    trader = PaperTrader(
        strategy=strategy,
        portfolio=portfolio,
        risk_manager=risk_manager,
        broker=broker,
        symbol=SYMBOL,
    )

    # --------------------------------------------------
    # 4. Paper trading loop (candle by candle)
    # --------------------------------------------------
    for _, row in df.iterrows():
        trader.on_candle(row)

        equity_curve.update(
            timestamp=row.name,
            cash=portfolio.cash,
            open_positions_value=portfolio.market_value(row["Close"])
        )

    # --------------------------------------------------
    # 5. Final report
    # --------------------------------------------------
    print("\n====== PAPER TRADING RESULT ======")
    print("Symbol:", SYMBOL)
    print("Final Cash:", round(portfolio.cash, 2))
    print("Open Positions:", len(portfolio.positions))
    print("Closed Trades:", len(portfolio.closed_trades))

    if portfolio.closed_trades:
        total_pnl = portfolio.cash - INITIAL_CASH
        print("Total PnL:", round(total_pnl, 2))

    # --------------------------------------------------
    # 6. Analytics summary
    # --------------------------------------------------
    trades = portfolio.closed_trades
    equity_values = equity_curve.values()
    returns = equity_curve.returns()

    print("\n===== ANALYTICS SUMMARY =====")
    print("Total Trades:", len(trades))
    print("Win Rate:", round(win_rate(trades) * 100, 2), "%")

    avg_win, avg_loss = avg_win_loss(trades)
    print("Avg Win:", round(avg_win, 2))
    print("Avg Loss:", round(avg_loss, 2))

    print("Max Drawdown:", round(max_drawdown(equity_values) * 100, 2), "%")

    if returns:
        print("Sharpe Ratio:", round(sharpe_ratio(returns), 2))


# ======================================================
# ENTRY POINT
# ======================================================
if __name__ == "__main__":
    main()
