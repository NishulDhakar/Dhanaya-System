import math

def total_return(initial_cash, final_cash):
    return (final_cash - initial_cash) / initial_cash


def win_rate(trades):
    if not trades:
        return 0.0
    wins = [t for t in trades if t.pnl > 0]
    return len(wins) / len(trades)


def avg_win_loss(trades):
    wins = [t.pnl for t in trades if t.pnl > 0]
    losses = [t.pnl for t in trades if t.pnl < 0]

    avg_win = sum(wins) / len(wins) if wins else 0.0
    avg_loss = sum(losses) / len(losses) if losses else 0.0

    return avg_win, avg_loss


def max_drawdown(equity_curve):
    """
    equity_curve: list of equity values
    """
    peak = equity_curve[0]
    max_dd = 0.0

    for equity in equity_curve:
        if equity > peak:
            peak = equity
        dd = (peak - equity) / peak
        max_dd = max(max_dd, dd)

    return max_dd


def sharpe_ratio(returns, risk_free_rate=0.0):
    if len(returns) < 2:
        return 0.0

    avg_return = sum(returns) / len(returns)
    variance = sum((r - avg_return) ** 2 for r in returns) / (len(returns) - 1)
    std_dev = math.sqrt(variance)

    if std_dev == 0:
        return 0.0

    return (avg_return - risk_free_rate) / std_dev
