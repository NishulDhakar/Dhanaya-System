from broker.order import Order
from strategies.base import Strategy
from portfolio.portfolio import Portfolio
from risk.risk_manager import RiskManager
from broker.simulator import BrokerSimulator
from risk.position_sizer import risk_based_position_size
import math

class PaperTrader:

    def __init__(
        self,
        strategy: Strategy,
        portfolio: Portfolio,
        risk_manager: RiskManager,
        broker: BrokerSimulator,
        symbol: str
    ):
        self.strategy = strategy
        self.portfolio = portfolio
        self.risk_manager = risk_manager
        self.broker = broker
        self.symbol = symbol

    def on_candle(self, data_row):
        price = data_row["Close"]

        if price is None or math.isnan(price):
            raise ValueError("Invalid price: NaN")

        if self.portfolio.cash < 0:
            raise ValueError("Negative cash detected")

        decision = self.strategy.generate_signal(data_row)
        signal = decision["signal"]
        reason = decision["reason"]

        # =========================
        # BUY
        # =========================
        if signal == "BUY" and self.symbol not in self.portfolio.positions:
            stop_loss_distance = abs(
                data_row["Close"] - data_row["SMA_14"]
            )

            quantity = risk_based_position_size(
                cash=self.portfolio.cash,
                max_risk_per_trade=self.risk_manager.max_risk_per_trade,
                stop_loss_distance=stop_loss_distance
            )
            if quantity <= 0:
                raise ValueError("Invalid quantity calculated")

            if self.symbol in self.portfolio.positions:
                raise ValueError("Duplicate position detected")

            # 🔒 Guard clause (VERY IMPORTANT)
            if quantity <= 0:
                return

            order = Order(
                symbol=self.symbol,
                side="BUY",
                quantity=quantity,
                price=data_row["Close"],
                reason=reason
            )

            if self.risk_manager.approve(order, self.portfolio.cash):
                execution = self.broker.execute(order)
                self.portfolio.open_position(execution)

        # =========================
        # SELL
        # =========================
        elif signal == "SELL" and self.symbol in self.portfolio.positions:
            position = self.portfolio.positions[self.symbol]

            execution = self.broker.execute(
                Order(
                    symbol=self.symbol,
                    side="SELL",
                    quantity=position.quantity,
                    price=data_row["Close"],
                    reason=reason
                )
            )

            self.portfolio.close_position(
                symbol=self.symbol,
                exit_price=execution["price"],
                timestamp=execution["timestamp"],
                reason=reason
            )
