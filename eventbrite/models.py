from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class EventRecord:
    event: dict[str, Any]
    venue: dict[str, Any] | None
    organizer: dict[str, Any] | None
    ticket_classes: list[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
