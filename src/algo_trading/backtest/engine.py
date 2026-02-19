from dataclasses import dataclass

import pandas as pd

from algo_trading.feeds.base import Tick
from algo_trading.strategy.base import Strategy, StrategyContext


@dataclass(slots=True)
class BacktestResult:
    trades: int
    signals: int


class BacktestEngine:
    def run(self, data: pd.DataFrame, strategy: Strategy) -> BacktestResult:
        signals = 0
        trades = 0
        context = StrategyContext()

        for row in data.itertuples(index=False):
            tick = Tick(symbol=row.symbol, price=row.close, timestamp=int(row.timestamp))
            signal = strategy.on_tick(tick, context)
            if signal:
                signals += 1
                trades += 1
                context.position_qty = signal.qty if signal.side == "BUY" else 0
        return BacktestResult(trades=trades, signals=signals)
