from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


class ConfigurationError(ValueError):
    pass


@dataclass(frozen=True)
class EventbriteSettings:
    api_token: str
    organization_id: str
    output_path: Path
    page_size: int = 50
    page_limit: int | None = None
    timeout_seconds: float = 30.0
    api_base_url: str = "https://www.eventbriteapi.com/v3"


def _get_required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ConfigurationError(f"Missing required environment variable: {name}")
    return value


def _get_positive_int(name: str, default: int | None = None) -> int | None:
    raw_value = os.getenv(name)
    if raw_value is None or raw_value == "":
        return default
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ConfigurationError(f"{name} must be an integer") from exc
    if value <= 0:
        raise ConfigurationError(f"{name} must be greater than zero")
    return value


def _get_positive_float(name: str, default: float) -> float:
    raw_value = os.getenv(name)
    if raw_value is None or raw_value == "":
        return default
    try:
        value = float(raw_value)
    except ValueError as exc:
        raise ConfigurationError(f"{name} must be a number") from exc
    if value <= 0:
        raise ConfigurationError(f"{name} must be greater than zero")
    return value


def load_settings() -> EventbriteSettings:
    load_dotenv()
    output_path = Path(os.getenv("EVENTBRITE_OUTPUT_PATH", "data/eventbrite-events.json"))
    return EventbriteSettings(
        api_token=_get_required("EVENTBRITE_API_TOKEN"),
        organization_id=_get_required("EVENTBRITE_ORGANIZATION_ID"),
        output_path=output_path,
        page_size=_get_positive_int("EVENTBRITE_PAGE_SIZE", 50) or 50,
        page_limit=_get_positive_int("EVENTBRITE_PAGE_LIMIT"),
        timeout_seconds=_get_positive_float("EVENTBRITE_TIMEOUT_SECONDS", 30.0),
        api_base_url=os.getenv("EVENTBRITE_API_BASE_URL", "https://www.eventbriteapi.com/v3").rstrip("/"),
    )
