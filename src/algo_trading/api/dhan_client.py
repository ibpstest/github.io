import httpx

from algo_trading.api.base import BrokerClient, OrderRequest
from algo_trading.config import settings


class DhanClient(BrokerClient):
    """Thin Dhan adapter. Map endpoints/payloads per docs v2."""

    def __init__(self) -> None:
        self._client = httpx.Client(
            base_url=settings.dhan_api_base_url,
            headers={
                "access-token": settings.dhan_access_token,
                "client-id": settings.dhan_client_id,
                "Content-Type": "application/json",
            },
            timeout=10.0,
        )

    def place_order(self, order: OrderRequest) -> dict:
        payload = {
            "securityId": order.symbol,
            "transactionType": order.side,
            "quantity": order.qty,
            "orderType": order.order_type,
            "price": order.price,
        }
        # TODO: verify endpoint and payload keys with Dhan docs.
        response = self._client.post("/v2/orders", json=payload)
        response.raise_for_status()
        return response.json()

    def modify_order(self, order_id: str, fields: dict) -> dict:
        response = self._client.put(f"/v2/orders/{order_id}", json=fields)
        response.raise_for_status()
        return response.json()

    def cancel_order(self, order_id: str) -> dict:
        response = self._client.delete(f"/v2/orders/{order_id}")
        response.raise_for_status()
        return response.json()

    def get_positions(self) -> list[dict]:
        response = self._client.get("/v2/positions")
        response.raise_for_status()
        return response.json()

    def get_quote(self, symbol: str) -> dict:
        response = self._client.get("/v2/market/quote", params={"securityId": symbol})
        response.raise_for_status()
        return response.json()

    def get_historical(self, symbol: str, interval: str, start: str, end: str) -> list[dict]:
        response = self._client.get(
            "/v2/charts/historical",
            params={"securityId": symbol, "interval": interval, "fromDate": start, "toDate": end},
        )
        response.raise_for_status()
        return response.json()
