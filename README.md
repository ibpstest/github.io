# Algo Trading System Skeleton (Python)

This repository contains a production-oriented skeleton for an algo trading platform in Python, ready to integrate with Dhan API v2.

## What is included

- Secure API client layer with pluggable broker adapters
- Strategy engine and indicator interfaces
- Risk management and position sizing primitives
- Order management workflow
- Live market feed abstraction (streaming-friendly)
- Backtesting scaffolding
- Logging, journal, and alert modules
- Webhook service entrypoint

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
python -m algo_trading.main
```

## Structure

```text
algo_trading/
  config.py
  main.py
  api/
  strategy/
  risk/
  orders/
  feeds/
  indicators/
  backtest/
  observability/
  alerts/
  webhooks/
```

## Notes for Dhan API integration

- Set `BROKER=dhan` in your `.env`.
- Fill `DHAN_*` secrets and IDs.
- Implement concrete endpoint mapping in `algo_trading/api/dhan_client.py` where marked `TODO`.
- Keep credentials in env vars or a secret manager; never hardcode tokens.
