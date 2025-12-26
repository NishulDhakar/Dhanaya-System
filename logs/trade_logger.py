import csv
from pathlib import Path

LOG_FILE = Path("logs/trades.csv")
LOG_FILE.parent.mkdir(exist_ok=True)


def log_trade(trade, capital_at_trade, stop_loss_distance):
    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "symbol",
                "quantity",
                "entry_price",
                "exit_price",
                "pnl",
                "reason_entry",
                "reason_exit",
                "stop_loss_distance",
                "capital_at_trade",
            ])

        writer.writerow([
            trade.exit_time,
            trade.symbol,
            trade.quantity,
            trade.entry_price,
            trade.exit_price,
            trade.pnl,
            trade.reason_entry,
            trade.reason_exit,
            stop_loss_distance,
            capital_at_trade,
        ])
