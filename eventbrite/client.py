from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Any

import requests

from eventbrite.config import EventbriteSettings


class EventbriteAPIError(RuntimeError):
    pass


@dataclass
class EventbriteClient:
    settings: EventbriteSettings
    session: requests.Session | None = None
    max_retries: int = 3

    def __post_init__(self) -> None:
        if self.session is None:
            self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.settings.api_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        assert self.session is not None
        url = f"{self.settings.api_base_url}/{path.lstrip('/')}"
        attempts = 0
        while True:
            try:
                response = self.session.get(url, params=params, timeout=self.settings.timeout_seconds)
            except requests.RequestException as exc:
                raise EventbriteAPIError(f"Eventbrite request failed: {exc}") from exc
            if response.status_code == 429 and attempts < self.max_retries:
                retry_after = response.headers.get("Retry-After") if response.headers else None
                delay = float(retry_after) if retry_after else min(2**attempts, 8)
                time.sleep(delay)
                attempts += 1
                continue
            if response.status_code >= 500 and attempts < self.max_retries:
                time.sleep(min(2**attempts, 8))
                attempts += 1
                continue
            if not response.ok:
                raise EventbriteAPIError(
                    f"Eventbrite request failed with {response.status_code}: {response.text[:500]}"
                )
            return response.json()

    def paginate(self, path: str, collection_key: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        request_params = dict(params or {})
        request_params.setdefault("page_size", self.settings.page_size)
        page_number = 1
        items: list[dict[str, Any]] = []

        while True:
            request_params["page"] = page_number
            payload = self.get(path, dict(request_params))
            page_items = payload.get(collection_key, [])
            if not isinstance(page_items, list):
                raise EventbriteAPIError(f"Expected list at key '{collection_key}'")
            items.extend(page_items)
            pagination = payload.get("pagination", {})
            if not pagination.get("has_more_items"):
                return items
            page_number += 1
            if self.settings.page_limit is not None and page_number > self.settings.page_limit:
                return items
