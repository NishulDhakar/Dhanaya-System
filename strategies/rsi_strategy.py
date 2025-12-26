import pandas as pd
from strategies.base import Strategy


class RSIStrategy(Strategy):
    def __init__(self, rsi_col: str = "RSI_14"):
        self.rsi_col = rsi_col

    def generate_signal(self, data: pd.Series):
        latest_rsi = data[self.rsi_col]

        if latest_rsi < 30:
            return {
                "signal": "BUY",
                "reason": f"RSI is {latest_rsi:.2f}, below 30 (oversold condition)"
            }

        elif latest_rsi > 70:
            return {
                "signal": "SELL",
                "reason": f"RSI is {latest_rsi:.2f}, above 70 (overbought condition)"
            }

        else:
            return {
                "signal": "HOLD",
                "reason": f"RSI is {latest_rsi:.2f}, between 30 and 70 (neutral zone)"
            }
