from dataclasses import dataclass


@dataclass(slots=True)
class Tick:
    symbol: str
    price: float
    timestamp: int
