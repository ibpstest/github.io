class RiskManager:
    def __init__(self, max_daily_loss: float, max_position_qty: int) -> None:
        self.max_daily_loss = max_daily_loss
        self.max_position_qty = max_position_qty
        self.realized_pnl = 0.0

    def can_trade(self, qty: int) -> bool:
        if self.realized_pnl <= -abs(self.max_daily_loss):
            return False
        return qty <= self.max_position_qty
