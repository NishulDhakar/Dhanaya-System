# 🧠 Deterministic Paper Trading & Analytics Engine

> A **research-grade, deterministic paper trading engine** built to study trading behavior, risk, and system correctness — not to chase short-term profits.

This project focuses on **correctness, reproducibility, and explainability** before optimization or machine learning.

---

## 🚀 Why This Project Exists

Most trading projects jump directly to:
- ML predictions
- complex indicators
- profitability claims

This engine does the opposite.

**Core philosophy:**

> If a system cannot explain *why* it traded and *how* money moved,  
> any ML trained on it will be garbage.

So this project builds a **solid, auditable foundation** first.

---

## 🧩 What This System Is (and Is Not)

### ✅ This system **IS**
- Deterministic (same input → same output)
- Auditable (every trade & decision logged)
- Replayable (historical data backtests)
- Research-ready (ML & GenAI can plug in later)

### ❌ This system is **NOT**
- A live trading bot
- A profit-optimized strategy
- An ML-first system (by design)

Losses are **expected and valuable** — they are labeled data, not bugs.

---

## 🏗️ System Architecture

Market Data
   ↓
Indicators
   ↓
Strategy (rules only)
   ↓
PaperTrader
   ↓
Broker (deterministic)
   ↓
Portfolio
   ├── Positions (open)
   ├── Trades (closed)
   └── Logs (CSV)
   ↓
Analytics

Each layer has **one responsibility** and no hidden side effects.

---

## 🔁 Trade Lifecycle (Explicit & Safe)

1. **Order Created**
2. **Execution Simulated**
   - deterministic slippage
   - deterministic fees
3. **Position Opened**
4. **Position Closed**
5. **Trade Created (immutable)**
6. **Trade Logged to CSV**
7. **Analytics Consume Logs**

> PnL is computed **only at close**, never before.

---

## 🛡️ System Guarantees (Hard Rules)

- ❌ No negative cash allowed
- ❌ No zero or negative quantity trades
- ❌ No duplicate open positions
- ❌ No NaN prices
- ❌ No silent failures (fail fast)

If any rule is violated → the system **raises an exception immediately**.

---

## 📊 Analytics Implemented

- Total trades
- Win rate
- Average win / loss
- Max drawdown
- Sharpe ratio
- Equity curve over time

Analytics are **derived from logs**, not from in-memory guesses.

---

## 🗂️ Logging (Single Source of Truth)

### Trade Log (`logs/trades.csv`)
Each closed trade records:

| Field | Purpose |
|-----|--------|
| timestamp | sequencing |
| symbol | multi-asset ready |
| quantity | risk visibility |
| entry_price | execution |
| exit_price | outcome |
| pnl | performance |
| reason_entry | explainability |
| reason_exit | explainability |
| stop_loss_distance | risk context |
| capital_at_trade | system state |

This file is:
- the ML dataset
- the audit trail
- the behavioral memory

---

## 🧪 Validation Philosophy

The system is considered **correct** only if it passes:

- Zero-trade scenario (HOLD-only strategy)
- Flat market data
- Trending market data
- Volatile market data
- Stress tests (frequent signals, tight stops)

Profitability is **not** a validation criterion at this stage.

---

## 🧠 Why ML Is Not Added Yet

ML and GenAI are **layers**, not foundations.

They answer different questions:

- **ML:** “When should I trust a rule?”
- **GenAI:** “Why am I behaving this way as a trader?”

Adding them too early would:
- amplify noise
- hide bugs
- destroy interpretability

They will be added **only after the core is locked and validated**.

---

## 🧭 Roadmap (High-Level)

- ✅ Core Engine (DONE)
- ✅ Deterministic Execution (DONE)
- ✅ Trade & Decision Logging (DONE)
- ✅ Analytics (DONE)
- 🔒 Core Freeze (`core-v1.0`)
- 🧪 Multi-run Validation
- 🤖 ML Phase 1: Trade Outcome Classification
- 🧠 GenAI Phase: Behavioral Analysis & Coaching

---

## 🎯 Intended Use

- Learning how real trading systems are built
- Demonstrating system design & correctness
- Creating clean datasets for ML research
- Interview-ready backend project

---

## 📌 Final Note

> This project optimizes for **trust before intelligence**.

Only a trustworthy system deserves ML.

---

