class EquityCurve:
    def __init__(self, initial_cash):
        self.initial_cash = initial_cash
        self.points = []  # (timestamp, equity)

    def update(self, timestamp, cash, open_positions_value=0.0):
        equity = cash + open_positions_value
        self.points.append((timestamp, equity))

    def values(self):
        return [e for _, e in self.points]

    def returns(self):
        values = self.values()
        returns = []
        for i in range(1, len(values)):
            returns.append((values[i] - values[i - 1]) / values[i - 1])
        return returns
