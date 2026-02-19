def simple_moving_average(values: list[float], period: int) -> float:
    if period <= 0:
        raise ValueError("period must be positive")
    if len(values) < period:
        raise ValueError("not enough values for requested period")
    window = values[-period:]
    return sum(window) / period
