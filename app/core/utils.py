from __future__ import annotations

from datetime import datetime
from typing import Optional


def parse_date(date: str | datetime | None) -> Optional[datetime] | None:
    if isinstance(date, str):
        return datetime.strptime(date, "%Y-%m-%d")
    return date