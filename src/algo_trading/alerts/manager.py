import httpx

from algo_trading.observability.logging_setup import logger


class AlertManager:
    def __init__(self, webhook_url: str = "") -> None:
        self.webhook_url = webhook_url

    def notify(self, message: str) -> None:
        if not self.webhook_url:
            logger.info("Alert: %s", message)
            return
        httpx.post(self.webhook_url, json={"text": message}, timeout=5.0)
