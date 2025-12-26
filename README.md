# Deterministic Paper Trading & Analytics Engine

A **deterministic, auditable paper trading engine** designed to study trading behavior, risk, and system correctness **before** optimization, machine learning, or live trading.

This project prioritizes **trust, reproducibility, and explainability** over profitability.

---

## Purpose

Most trading systems introduce machine learning too early.

This project follows a strict principle:

> If a system cannot explain *why* it traded and *how* capital moved,  
> any machine learning trained on it will be unreliable.

The engine is therefore built **correct-first**, not profit-first.

---

## What This System Is

- **Deterministic** (same input → same output)
- **Auditable** (every trade and decision is logged)
- **Replayable** (historical backtesting)
- **Research-ready** (ML / GenAI can be layered later)

## What This System Is Not

- Not a live trading bot  
- Not a profit-optimized strategy  
- Not ML-driven (by design)

Losses are **expected** and treated as data, not bugs.

---

## Architecture Overview

```
Market Data
    ↓
Indicators
    ↓
Rule-Based Strategy
    ↓
PaperTrader
    ↓
Broker (Deterministic Execution)
    ↓
Portfolio
    ├── Open Positions
    ├── Closed Trades (immutable)
    └── Logs (CSV)
    ↓
Analytics
```

Each layer has **one responsibility** and no hidden side effects.

---

## Trade Lifecycle

1. Order is created  
2. Execution is simulated (deterministic)  
3. Position is opened  
4. Position is closed  
5. Trade object is created (immutable)  
6. Trade is logged to CSV  
7. Analytics consume logged trades  

PnL is calculated **only at trade close**.

---

## System Guarantees

The engine enforces strict invariants:

- No negative cash balances  
- No zero or negative trade quantities  
- No duplicate open positions  
- No NaN prices  
- No silent failures (fail fast)

Any violation raises an exception immediately.

---

## Analytics Implemented

- Total trades  
- Win rate  
- Average win / loss  
- Maximum drawdown  
- Sharpe ratio  
- Equity curve over time  

All analytics are derived from **logged trades**, not in-memory assumptions.

---

## Logging (Single Source of Truth)

### Trade Log (`logs/trades.csv`)

Each closed trade records:

- timestamp  
- symbol  
- quantity  
- entry price  
- exit price  
- pnl  
- entry reason  
- exit reason  
- stop loss distance  
- capital at trade  

This file acts as:

- the ML dataset  
- the audit trail  
- the behavioral memory  

---

## Validation Philosophy

The system is considered **correct** only if it passes:

- Zero-trade scenario (strategy always returns HOLD)
- Flat market data
- Trending market data
- Volatile market data
- Stress tests (frequent signals, tight stops)

Profitability is **not** a validation criterion at this stage.

---

## Machine Learning & GenAI (Deferred by Design)

ML and GenAI are **layers, not foundations**.

They answer different questions:

- **ML:** When should a rule be trusted?  
- **GenAI:** Why is the system behaving this way?  

They will be added **only after the core system is frozen and validated**.

---

## Project Status

- ✅ Core trading engine: complete  
- ✅ Deterministic execution: complete  
- ✅ Risk management & position sizing: complete  
- ✅ Trade & decision logging: complete  
- ✅ Analytics engine: complete  
- 🔒 Core version: `core-v1.0` (frozen)

---

## Intended Use

- Learning how real trading systems are engineered  
- Demonstrating system design and correctness  
- Creating clean datasets for ML research  
- Interview-ready backend / systems project  

---

## Final Principle

> Trust comes before intelligence.

Only a trustworthy system deserves machine learning.

---

## Getting Started

### Prerequisites

```bash
# Add your prerequisites here
python >= 3.8
pandas
numpy
```

### Installation

```bash
# Add installation steps
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
```

### Running the System

```bash
# Add run commands
python main.py
```

### Running Tests

```bash
# Add test commands
pytest tests/
```

---

## License

[Add your license here]

---

## Contributing

This is a research and educational project. Contributions that maintain the core principles of determinism, auditability, and correctness are welcome.








# Deterministic Paper Trading & Analytics Engine

A **deterministic, auditable paper trading engine** designed to study trading behavior, risk, and system correctness **before** optimization, machine learning, or live trading.

This project prioritizes **trust, reproducibility, and explainability** over profitability.

---

## Purpose

Most trading systems introduce machine learning too early.

This project follows a strict principle:

> If a system cannot explain *why* it traded and *how* capital moved,  
> any machine learning trained on it will be unreliable.

The engine is therefore built **correct-first**, not profit-first.

---

## What This System Is

- Deterministic (same input → same output)
- Auditable (every trade and decision is logged)
- Replayable (historical backtesting)
- Research-ready (ML / GenAI can be layered later)

## What This System Is Not

- Not a live trading bot  
- Not a profit-optimized strategy  
- Not ML-driven (by design)

Losses are **expected** and treated as data, not bugs.

---

## Architecture Overview

Market Data
    ↓
Indicators
    ↓
Rule-Based Strategy
    ↓
PaperTrader
    ↓
Broker (Deterministic Execution)
    ↓
Portfolio
    ├── Open Positions
    ├── Closed Trades (immutable)
    └── Logs (CSV)
    ↓
Analytics


Each layer has **one responsibility** and no hidden side effects.

---

## Trade Lifecycle

1. Order is created  
2. Execution is simulated (deterministic)  
3. Position is opened  
4. Position is closed  
5. Trade object is created (immutable)  
6. Trade is logged to CSV  
7. Analytics consume logged trades  

PnL is calculated **only at trade close**.

---

## System Guarantees

The engine enforces strict invariants:

- No negative cash balances  
- No zero or negative trade quantities  
- No duplicate open positions  
- No NaN prices  
- No silent failures (fail fast)

Any violation raises an exception immediately.

---

## Analytics Implemented

- Total trades  
- Win rate  
- Average win / loss  
- Maximum drawdown  
- Sharpe ratio  
- Equity curve over time  

All analytics are derived from **logged trades**, not in-memory assumptions.

---

## Logging (Single Source of Truth)

### Trade Log (`logs/trades.csv`)

Each closed trade records:

- timestamp  
- symbol  
- quantity  
- entry price  
- exit price  
- pnl  
- entry reason  
- exit reason  
- stop loss distance  
- capital at trade  

This file acts as:
- the ML dataset  
- the audit trail  
- the behavioral memory  

---

## Validation Philosophy

The system is considered **correct** only if it passes:

- Zero-trade scenario (strategy always returns HOLD)
- Flat market data
- Trending market data
- Volatile market data
- Stress tests (frequent signals, tight stops)

Profitability is **not** a validation criterion at this stage.

---

## Machine Learning & GenAI (Deferred by Design)

ML and GenAI are **layers, not foundations**.

They answer different questions:

- **ML:** When should a rule be trusted?  
- **GenAI:** Why is the system behaving this way?  

They will be added **only after the core system is frozen and validated**.

---

## Project Status

- Core trading engine: complete  
- Deterministic execution: complete  
- Risk management & position sizing: complete  
- Trade & decision logging: complete  
- Analytics engine: complete  
- Core version: `core-v1.0` (frozen)

---

## Intended Use

- Learning how real trading systems are engineered  
- Demonstrating system design and correctness  
- Creating clean datasets for ML research  
- Interview-ready backend / systems project  

---

## Final Principle

> Trust comes before intelligence.

Only a trustworthy system deserves machine learning.


