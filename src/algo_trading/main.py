from algo_trading.alerts.manager import AlertManager
from algo_trading.api.factory import build_broker_client
from algo_trading.config import settings
from algo_trading.feeds.base import Tick
from algo_trading.observability.logging_setup import configure_logging, logger
from algo_trading.orders.manager import OrderManager
from algo_trading.risk.manager import RiskManager
from algo_trading.strategy.base import StrategyContext
from algo_trading.strategy.sample_strategy import MovingAverageCrossStrategy


def bootstrap() -> None:
    configure_logging(settings.log_level)
    broker_client = build_broker_client(settings.broker)
    risk_manager = RiskManager(
        max_daily_loss=settings.max_daily_loss,
        max_position_qty=settings.max_position_qty,
    )
    order_manager = OrderManager(broker_client=broker_client, risk_manager=risk_manager)
    alert_manager = AlertManager(webhook_url=settings.slack_webhook_url)

    strategy = MovingAverageCrossStrategy(symbol="NSE:SBIN")
    sample_tick = Tick(symbol="NSE:SBIN", price=801.25, timestamp=0)
    signal = strategy.on_tick(sample_tick, StrategyContext())

    if signal:
        order = order_manager.create_order_from_signal(signal)
        if order:
            order_manager.place(order)
            alert_manager.notify(f"Placed order: {order}")

    logger.info("Bootstrap completed. Replace sample loop with live feed consumer.")


if __name__ == "__main__":
    bootstrap()
