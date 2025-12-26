from datetime import datetime
from config.settings import DETERMINISTIC, FIXED_SLIPPAGE

class BrokerSimulator:
    def __init__(self, fee_rate: float = 0.001, slippage: float = 0.001):
        self.fee_rate = fee_rate
        self.slippage = slippage

    def execute(self, order):
        slippage = FIXED_SLIPPAGE if DETERMINISTIC else self.slippage

        executed_price = order.price * (1 + slippage)

        return {
            "symbol": order.symbol,
            "side": order.side,
            "quantity": order.quantity,
            "price": executed_price,
            "timestamp": datetime.utcnow(),
        }
