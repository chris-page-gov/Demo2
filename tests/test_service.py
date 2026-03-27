from __future__ import annotations

from pathlib import Path
from typing import Any

import eventbrite.service as service
from eventbrite.config import EventbriteSettings


class FakeClient:
    def __init__(self, settings: EventbriteSettings) -> None:
        self.settings = settings
        self.requested_paths: list[str] = []

    def paginate(self, path: str, collection_key: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        assert path == "organizations/org-1/events/"
        assert collection_key == "events"
        assert params == {"expand": "venue,organizer,ticket_classes"}
        return [
            {
                "id": "evt-1",
                "name": {"text": "Sample event"},
                "venue_id": "ven-1",
                "organizer_id": "orgzr-1",
            }
        ]

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        self.requested_paths.append(path)
        responses = {
            "venues/ven-1/": {"id": "ven-1", "name": "Venue"},
            "organizers/orgzr-1/": {"id": "orgzr-1", "name": "Organizer"},
            "events/evt-1/ticket_classes/": {"ticket_classes": [{"id": "tc-1", "name": "General"}]},
        }
        return responses[path]


def test_fetch_organization_snapshot_enriches_related_entities(monkeypatch) -> None:
    settings = EventbriteSettings(
        api_token="token",
        organization_id="org-1",
        output_path=Path("out.json"),
    )
    monkeypatch.setattr(service, "EventbriteClient", FakeClient)

    payload = service.fetch_organization_snapshot(settings)

    assert payload["organization_id"] == "org-1"
    assert payload["event_count"] == 1
    record = payload["events"][0]
    assert record["venue"]["id"] == "ven-1"
    assert record["organizer"]["id"] == "orgzr-1"
    assert record["ticket_classes"][0]["id"] == "tc-1"
