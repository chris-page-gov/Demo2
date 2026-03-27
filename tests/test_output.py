import json
from pathlib import Path

from eventbrite.output import write_events_json


def test_write_events_json_creates_parent_directory(tmp_path: Path) -> None:
    output_path = tmp_path / "nested" / "events.json"

    write_events_json({"events": [{"id": "1"}]}, output_path)

    assert output_path.exists()
    assert json.loads(output_path.read_text(encoding="utf-8")) == {"events": [{"id": "1"}]}
