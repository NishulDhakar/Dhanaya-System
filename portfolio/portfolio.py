from typing import Dict, List
from portfolio.position import Position
from broker.trade import Trade
from logs.trade_logger import log_trade


class Portfolio:
    def __init__(self, initial_cash: float):
        self.cash = initial_cash
        self.positions: Dict[str, Position] = {}
        self.closed_trades: List[Trade] = []

    def market_value(self, current_price):
        value = 0.0
        for position in self.positions.values():
            value += position.quantity * current_price
        return value

    def open_position(self, execution):
        symbol = execution["symbol"]
        quantity = execution["quantity"]
        price = execution["price"]
        timestamp = execution["timestamp"]

        cost = quantity * price

        if cost > self.cash:
            raise ValueError("Insufficient cash to open position")

        if symbol in self.positions:
            raise ValueError("Duplicate position detected")

        position = Position(
            symbol=symbol,
            quantity=quantity,
            entry_price=price,
            entry_time=timestamp,
            reason=execution.get("reason"),
        )

        self.cash -= cost
        self.positions[symbol] = position

    def close_position(self, symbol, exit_price, timestamp, reason=None):
        if symbol not in self.positions:
            raise ValueError("Closing non-existent position")

        position = self.positions.pop(symbol)

        trade = Trade(
            symbol=symbol,
            quantity=position.quantity,
            entry_price=position.entry_price,
            exit_price=exit_price,
            entry_time=position.entry_time,
            exit_time=timestamp,
            reason_entry=position.reason,
            reason_exit=reason,
        )

        self.cash += trade.pnl
        self.closed_trades.append(trade)

        # 🔒 single source of truth
        log_trade(
            trade=trade,
            capital_at_trade=self.cash,
            stop_loss_distance=None,  # pass real value if stored
        )

        return trade
