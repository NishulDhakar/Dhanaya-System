from broker.order import Order


class RiskManager:
    def __init__(self, max_risk_per_trade: float):
        self.max_risk_per_trade = max_risk_per_trade

    def approve(self, order, cash):
        if cash < 0:
            raise ValueError("Cash < 0")

        if order.quantity <= 0:
            raise ValueError("Order quantity <= 0")

        if not hasattr(order, "price") or order.price <= 0:
            raise ValueError("Invalid order price")

        return True

