import csv
from pathlib import Path


class TradeJournal:
    def __init__(self, path: str = "trade_journal.csv") -> None:
        self.path = Path(path)

    def append(self, record: dict) -> None:
        exists = self.path.exists()
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=record.keys())
            if not exists:
                writer.writeheader()
            writer.writerow(record)
