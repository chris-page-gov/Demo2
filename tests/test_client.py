from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
import requests

from eventbrite.client import EventbriteAPIError, EventbriteClient
from eventbrite.config import EventbriteSettings


@dataclass
class FakeResponse:
    status_code: int
    payload: dict[str, Any]
    text: str = ""
    headers: dict[str, str] | None = None

    @property
    def ok(self) -> bool:
        return self.status_code < 400

    def json(self) -> dict[str, Any]:
        return self.payload


class FakeSession:
    def __init__(self, responses: list[FakeResponse]) -> None:
        self.responses = responses
        self.headers: dict[str, str] = {}
        self.calls: list[tuple[str, dict[str, Any] | None, float]] = []

    def get(self, url: str, params: dict[str, Any] | None = None, timeout: float = 0.0) -> FakeResponse:
        self.calls.append((url, params, timeout))
        return self.responses.pop(0)


class ErrorSession:
    def __init__(self) -> None:
        self.headers: dict[str, str] = {}

    def get(self, url: str, params: dict[str, Any] | None = None, timeout: float = 0.0) -> FakeResponse:
        raise requests.RequestException("boom")


def test_paginate_collects_multiple_pages() -> None:
    settings = EventbriteSettings(
        api_token="token",
        organization_id="org-1",
        output_path=Path("out.json"),
        page_size=2,
    )
    session = FakeSession(
        [
            FakeResponse(200, {"events": [{"id": "1"}], "pagination": {"has_more_items": True}}),
            FakeResponse(200, {"events": [{"id": "2"}], "pagination": {"has_more_items": False}}),
        ]
    )
    client = EventbriteClient(settings=settings, session=session)

    events = client.paginate("organizations/org-1/events/", "events")

    assert [event["id"] for event in events] == ["1", "2"]
    assert session.headers["Authorization"] == "Bearer token"
    assert session.calls[0][1]["page"] == 1
    assert session.calls[1][1]["page"] == 2


def test_get_wraps_request_exceptions() -> None:
    settings = EventbriteSettings(
        api_token="token",
        organization_id="org-1",
        output_path=Path("out.json"),
    )
    client = EventbriteClient(settings=settings, session=ErrorSession())

    with pytest.raises(EventbriteAPIError, match="boom"):
        client.get("organizations/org-1/events/")
