from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class OrderRequest:
    symbol: str
    side: str
    qty: int
    order_type: str = "MARKET"
    price: float | None = None


class BrokerClient(Protocol):
    def place_order(self, order: OrderRequest) -> dict: ...
    def modify_order(self, order_id: str, fields: dict) -> dict: ...
    def cancel_order(self, order_id: str) -> dict: ...
    def get_positions(self) -> list[dict]: ...
    def get_quote(self, symbol: str) -> dict: ...
    def get_historical(self, symbol: str, interval: str, start: str, end: str) -> list[dict]: ...
