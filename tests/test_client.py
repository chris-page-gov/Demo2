from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
import requests

import eventbrite.client as client_module
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

    def get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        timeout: float = 0.0,
    ) -> FakeResponse:
        self.calls.append((url, params, timeout))
        return self.responses.pop(0)


class ErrorSession:
    def __init__(self) -> None:
        self.headers: dict[str, str] = {}

    def get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        timeout: float = 0.0,
    ) -> FakeResponse:
        raise requests.RequestException("boom")


def make_settings(**overrides: Any) -> EventbriteSettings:
    values = {
        "api_token": "token",
        "organization_id": "org-1",
        "output_path": Path("out.json"),
        "page_size": 2,
    }
    values.update(overrides)
    return EventbriteSettings(**values)


def test_client_creates_session_when_none_provided(monkeypatch: pytest.MonkeyPatch) -> None:
    created_session = FakeSession([FakeResponse(200, {"ok": True})])
    monkeypatch.setattr(client_module.requests, "Session", lambda: created_session)

    client = EventbriteClient(settings=make_settings())

    assert client.session is created_session
    assert created_session.headers["Authorization"] == "Bearer token"


def test_paginate_collects_multiple_pages() -> None:
    session = FakeSession(
        [
            FakeResponse(200, {"events": [{"id": "1"}], "pagination": {"has_more_items": True}}),
            FakeResponse(200, {"events": [{"id": "2"}], "pagination": {"has_more_items": False}}),
        ]
    )
    client = EventbriteClient(settings=make_settings(), session=session)

    events = client.paginate("organizations/org-1/events/", "events")

    assert [event["id"] for event in events] == ["1", "2"]
    assert session.headers["Authorization"] == "Bearer token"
    assert session.calls[0][1]["page"] == 1
    assert session.calls[1][1]["page"] == 2


def test_paginate_stops_at_page_limit() -> None:
    session = FakeSession(
        [
            FakeResponse(200, {"events": [{"id": "1"}], "pagination": {"has_more_items": True}}),
            FakeResponse(200, {"events": [{"id": "2"}], "pagination": {"has_more_items": True}}),
        ]
    )
    client = EventbriteClient(settings=make_settings(page_limit=1), session=session)

    events = client.paginate("organizations/org-1/events/", "events")

    assert [event["id"] for event in events] == ["1"]


def test_paginate_rejects_non_list_collection() -> None:
    session = FakeSession(
        [FakeResponse(200, {"events": {"id": "1"}, "pagination": {"has_more_items": False}})]
    )
    client = EventbriteClient(settings=make_settings(), session=session)

    with pytest.raises(EventbriteAPIError, match="Expected list"):
        client.paginate("organizations/org-1/events/", "events")


def test_get_wraps_request_exceptions() -> None:
    client = EventbriteClient(settings=make_settings(), session=ErrorSession())

    with pytest.raises(EventbriteAPIError, match="boom"):
        client.get("organizations/org-1/events/")


def test_get_retries_on_rate_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    sleep_calls: list[float] = []
    monkeypatch.setattr(client_module.time, "sleep", lambda seconds: sleep_calls.append(seconds))
    session = FakeSession(
        [
            FakeResponse(429, {}, headers={"Retry-After": "0"}),
            FakeResponse(200, {"ok": True}),
        ]
    )
    client = EventbriteClient(settings=make_settings(), session=session)

    payload = client.get("organizations/org-1/events/")

    assert payload == {"ok": True}
    assert sleep_calls == [0.0]


def test_get_retries_on_server_error(monkeypatch: pytest.MonkeyPatch) -> None:
    sleep_calls: list[float] = []
    monkeypatch.setattr(client_module.time, "sleep", lambda seconds: sleep_calls.append(seconds))
    session = FakeSession(
        [
            FakeResponse(500, {}, text="server down"),
            FakeResponse(200, {"ok": True}),
        ]
    )
    client = EventbriteClient(settings=make_settings(), session=session)

    payload = client.get("organizations/org-1/events/")

    assert payload == {"ok": True}
    assert sleep_calls == [1]


def test_get_raises_for_non_ok_response() -> None:
    session = FakeSession([FakeResponse(404, {}, text="missing")])
    client = EventbriteClient(settings=make_settings(), session=session)

    with pytest.raises(EventbriteAPIError, match="404"):
        client.get("organizations/org-1/events/")
