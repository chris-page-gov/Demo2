import subprocess
import sys
from pathlib import Path

import main as app_main
from eventbrite.client import EventbriteAPIError


class DummySettings:
    output_path = Path("out.json")


def test_main_returns_zero_on_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(app_main, "load_settings", lambda: DummySettings())
    monkeypatch.setattr(
        app_main,
        "fetch_organization_snapshot",
        lambda settings: {"events": [{"id": "1"}]},
    )
    monkeypatch.setattr(app_main, "write_events_json", lambda payload, output_path: None)

    result = app_main.main()

    captured = capsys.readouterr()
    assert result == 0
    assert "Wrote 1 events" in captured.out


def test_main_returns_one_on_known_error(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        app_main,
        "load_settings",
        lambda: (_ for _ in ()).throw(EventbriteAPIError("bad token")),
    )

    result = app_main.main()

    captured = capsys.readouterr()
    assert result == 1
    assert "bad token" in captured.err


def test_main_script_entrypoint_returns_non_zero_on_missing_env(tmp_path: Path) -> None:
    env = {
        "PATH": sys.executable,
    }
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=Path(__file__).resolve().parent.parent,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "EVENTBRITE_API_TOKEN" in result.stderr
