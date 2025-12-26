from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:
    CREATED = "CREATED"
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def __init__(
        self,
        symbol,
        quantity,
        entry_price,
        exit_price,
        entry_time,
        exit_time,
        reason_entry=None,
        reason_exit=None,
    ):
        self.symbol = symbol
        self.quantity = quantity

        self.entry_price = entry_price
        self.exit_price = exit_price

        self.entry_time = entry_time
        self.exit_time = exit_time

        self.reason_entry = reason_entry
        self.reason_exit = reason_exit
        self.status = Trade.CREATED

        # ✅ PnL computed ONLY here
        self.pnl = (exit_price - entry_price) * quantity
