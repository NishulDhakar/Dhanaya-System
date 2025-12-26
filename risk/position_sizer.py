MIN_STOP_DISTANCE = 0.005  # 0.5% of price
MAX_CAPITAL_FRACTION = 0.25

def risk_based_position_size(
    cash,
    max_risk_per_trade,
    stop_loss_distance,
    risk_pct=0.01
):
    if stop_loss_distance <= 0:
        raise ValueError("Invalid stop_loss_distance")

    risk_amount = min(cash * risk_pct, max_risk_per_trade)
    quantity = risk_amount / stop_loss_distance

    return int(quantity)
