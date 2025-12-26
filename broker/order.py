from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    def __init__(self, symbol, side, quantity, price, reason=None):
        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.price = price
        self.reason = reason
        self.timestamp = datetime.utcnow()
    
