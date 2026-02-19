from algo_trading.api.base import BrokerClient
from algo_trading.api.dhan_client import DhanClient


def build_broker_client(name: str) -> BrokerClient:
    if name.lower() == "dhan":
        return DhanClient()
    raise ValueError(f"Unsupported broker: {name}")
