from dataclasses import dataclass


@dataclass
class Position:
    def __init__(self, symbol, quantity, entry_price, entry_time=None, reason=None):
        self.symbol = symbol
        self.quantity = quantity
        self.entry_price = entry_price
        self.entry_time = entry_time
        self.reason = reason
