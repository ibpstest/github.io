from dataclasses import dataclass

from algo_trading.feeds.base import Tick


@dataclass(slots=True)
class Signal:
    symbol: str
    side: str
    qty: int


@dataclass(slots=True)
class StrategyContext:
    position_qty: int = 0


class Strategy:
    def on_tick(self, tick: Tick, context: StrategyContext) -> Signal | None:
        raise NotImplementedError
