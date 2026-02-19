from algo_trading.api.base import BrokerClient, OrderRequest
from algo_trading.strategy.base import Signal


class OrderManager:
    def __init__(self, broker_client: BrokerClient, risk_manager) -> None:
        self.broker_client = broker_client
        self.risk_manager = risk_manager

    def create_order_from_signal(self, signal: Signal) -> OrderRequest | None:
        if not self.risk_manager.can_trade(signal.qty):
            return None
        return OrderRequest(symbol=signal.symbol, side=signal.side, qty=signal.qty)

    def place(self, order: OrderRequest) -> dict:
        return self.broker_client.place_order(order)
