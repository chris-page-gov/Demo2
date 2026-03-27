from pathlib import Path

import pytest

from eventbrite.config import ConfigurationError, load_settings


@pytest.fixture(autouse=True)
def clear_eventbrite_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in [
        "EVENTBRITE_API_TOKEN",
        "EVENTBRITE_ORGANIZATION_ID",
        "EVENTBRITE_OUTPUT_PATH",
        "EVENTBRITE_PAGE_SIZE",
        "EVENTBRITE_PAGE_LIMIT",
        "EVENTBRITE_TIMEOUT_SECONDS",
        "EVENTBRITE_API_BASE_URL",
    ]:
        monkeypatch.delenv(name, raising=False)


def test_load_settings_reads_required_and_optional_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EVENTBRITE_API_TOKEN", "token-123")
    monkeypatch.setenv("EVENTBRITE_ORGANIZATION_ID", "org-456")
    monkeypatch.setenv("EVENTBRITE_OUTPUT_PATH", "tmp/output.json")
    monkeypatch.setenv("EVENTBRITE_PAGE_SIZE", "25")
    monkeypatch.setenv("EVENTBRITE_PAGE_LIMIT", "3")
    monkeypatch.setenv("EVENTBRITE_TIMEOUT_SECONDS", "12.5")

    settings = load_settings()

    assert settings.api_token == "token-123"
    assert settings.organization_id == "org-456"
    assert settings.output_path == Path("tmp/output.json")
    assert settings.page_size == 25
    assert settings.page_limit == 3
    assert settings.timeout_seconds == 12.5


def test_load_settings_requires_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EVENTBRITE_ORGANIZATION_ID", "org-456")

    with pytest.raises(ConfigurationError, match="EVENTBRITE_API_TOKEN"):
        load_settings()
