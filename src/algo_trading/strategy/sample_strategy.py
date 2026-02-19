from collections import deque

from algo_trading.feeds.base import Tick
from algo_trading.indicators.moving_average import simple_moving_average
from algo_trading.strategy.base import Signal, Strategy, StrategyContext


class MovingAverageCrossStrategy(Strategy):
    def __init__(self, symbol: str, fast: int = 5, slow: int = 20, qty: int = 1) -> None:
        self.symbol = symbol
        self.fast = fast
        self.slow = slow
        self.qty = qty
        self.prices = deque(maxlen=slow)

    def on_tick(self, tick: Tick, context: StrategyContext) -> Signal | None:
        if tick.symbol != self.symbol:
            return None
        self.prices.append(tick.price)
        if len(self.prices) < self.slow:
            return None

        fast_ma = simple_moving_average(list(self.prices), self.fast)
        slow_ma = simple_moving_average(list(self.prices), self.slow)
        if fast_ma > slow_ma and context.position_qty <= 0:
            return Signal(symbol=tick.symbol, side="BUY", qty=self.qty)
        if fast_ma < slow_ma and context.position_qty > 0:
            return Signal(symbol=tick.symbol, side="SELL", qty=context.position_qty)
        return None
