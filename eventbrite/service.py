from __future__ import annotations

from typing import Any

from eventbrite.client import EventbriteClient
from eventbrite.config import EventbriteSettings
from eventbrite.models import EventRecord


def _get_nested_id(payload: dict[str, Any], key: str) -> str | None:
    value = payload.get(key)
    if isinstance(value, dict):
        nested_id = value.get("id")
        return str(nested_id) if nested_id else None
    if value:
        return str(value)
    return None


def _fetch_venue(
    client: EventbriteClient,
    cache: dict[str, dict[str, Any]],
    venue_id: str | None,
) -> dict[str, Any] | None:
    if not venue_id:
        return None
    if venue_id not in cache:
        cache[venue_id] = client.get(f"venues/{venue_id}/")
    return cache[venue_id]


def _fetch_organizer(
    client: EventbriteClient,
    cache: dict[str, dict[str, Any]],
    organizer_id: str | None,
) -> dict[str, Any] | None:
    if not organizer_id:
        return None
    if organizer_id not in cache:
        cache[organizer_id] = client.get(f"organizers/{organizer_id}/")
    return cache[organizer_id]


def fetch_organization_snapshot(settings: EventbriteSettings) -> dict[str, Any]:
    client = EventbriteClient(settings)
    event_payloads = client.paginate(
        f"organizations/{settings.organization_id}/events/",
        collection_key="events",
        params={"expand": "venue,organizer,ticket_classes"},
    )

    venue_cache: dict[str, dict[str, Any]] = {}
    organizer_cache: dict[str, dict[str, Any]] = {}
    records: list[dict[str, Any]] = []

    for payload in event_payloads:
        venue = payload.get("venue") if isinstance(payload.get("venue"), dict) else None
        organizer = payload.get("organizer") if isinstance(payload.get("organizer"), dict) else None
        ticket_classes = (
            payload.get("ticket_classes")
            if isinstance(payload.get("ticket_classes"), list)
            else None
        )

        venue_id = _get_nested_id(payload, "venue_id") or _get_nested_id(payload, "venue")
        organizer_id = _get_nested_id(payload, "organizer_id") or _get_nested_id(
            payload,
            "organizer",
        )
        venue = venue or _fetch_venue(client, venue_cache, venue_id)
        organizer = organizer or _fetch_organizer(client, organizer_cache, organizer_id)
        if ticket_classes is None:
            ticket_class_payload = client.get(f"events/{payload['id']}/ticket_classes/")
            ticket_classes = ticket_class_payload.get("ticket_classes", [])

        records.append(
            EventRecord(
                event=payload,
                venue=venue,
                organizer=organizer,
                ticket_classes=ticket_classes,
            ).to_dict()
        )

    return {
        "organization_id": settings.organization_id,
        "event_count": len(records),
        "events": records,
    }
