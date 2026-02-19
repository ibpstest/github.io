from collections.abc import Iterator

from algo_trading.feeds.base import Tick


class LiveFeed:
    """Placeholder for websocket/streaming integrations."""

    def stream(self) -> Iterator[Tick]:
        # TODO: map Dhan websocket feed events to Tick.
        return iter(())
