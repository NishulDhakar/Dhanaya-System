# Deterministic Paper Trading & Analytics Engine

A **deterministic, auditable paper trading engine** built to study trading behavior, risk, and system correctness before optimization or machine learning.

The focus is **trust, reproducibility, and explainability**, not profitability.

---

## Purpose

Most trading systems add ML too early.

This project enforces a simple rule:

> If a system cannot explain *why* it traded and *how* capital moved,  
> ML trained on it will be unreliable.

The engine is therefore built **correct first**, not profitable first.

---

## What This System Is

- Deterministic (same input → same output)
- Auditable (every trade and decision logged)
- Replayable (historical data backtests)
- Research-ready (ML/GenAI can be layered later)

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


Each layer has **one responsibility**.

---

## Trade Lifecycle

1. Order created  
2. Execution simulated (deterministic)  
3. Position opened  
4. Position closed  
5. Trade created (immutable)  
6. Trade logged to CSV  
7. Analytics consume logs  

PnL is calculated **only at trade close**.

---

## System Guarantees

- No negative cash
- No zero or negative quantity
- No duplicate open positions
- No NaN prices
- No silent failures (fail fast)

Invalid states raise exceptions immediately.

---

## Analytics Implemented

- Total trades
- Win rate
- Average win / loss
- Maximum drawdown
- Sharpe ratio
- Equity curve

All analytics are derived from **logged trades**.

---

## Logging (Single Source of Truth)

`logs/trades.csv` records for each trade:
- timestamp
- symbol
- quantity
- entry & exit price
- pnl
- entry & exit reason
- stop loss distance
- capital at trade

This file is:
- the ML dataset
- the audit trail
- the behavioral memory

---

## Validation Philosophy

The system is correct only if it passes:
- Zero-trade strategy
- Flat market
- Trending market
- Volatile market
- Stress tests

Profitability is **not** a validation requirement.

---

## ML & GenAI (Deferred by Design)

ML and GenAI are layers, not foundations.

- ML answers: *When should I trust a rule?*
- GenAI answers: *Why is the system behaving this way?*

They will be added **only after the core is locked and validated**.

---

## Status

- Core engine: complete
- Deterministic execution: complete
- Logging & analytics: complete
- Core version: `core-v1.0` (frozen)

---

## Final Principle

> Trust comes before intelligence.

Only a trustworthy system deserves ML.

