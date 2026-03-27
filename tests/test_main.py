from pathlib import Path

import main as app_main
from eventbrite.client import EventbriteAPIError


class DummySettings:
    output_path = Path("out.json")


def test_main_returns_zero_on_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(app_main, "load_settings", lambda: DummySettings())
    monkeypatch.setattr(app_main, "fetch_organization_snapshot", lambda settings: {"events": [{"id": "1"}]})
    monkeypatch.setattr(app_main, "write_events_json", lambda payload, output_path: None)

    result = app_main.main()

    captured = capsys.readouterr()
    assert result == 0
    assert "Wrote 1 events" in captured.out


def test_main_returns_one_on_known_error(monkeypatch, capsys) -> None:
    monkeypatch.setattr(app_main, "load_settings", lambda: (_ for _ in ()).throw(EventbriteAPIError("bad token")))

    result = app_main.main()

    captured = capsys.readouterr()
    assert result == 1
    assert "bad token" in captured.err
