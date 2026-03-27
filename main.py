import sys

from eventbrite.client import EventbriteAPIError
from eventbrite.config import ConfigurationError, load_settings
from eventbrite.output import write_events_json
from eventbrite.service import fetch_organization_snapshot


def main() -> int:
    try:
        settings = load_settings()
        snapshot = fetch_organization_snapshot(settings)
        write_events_json(snapshot, settings.output_path)
    except (ConfigurationError, EventbriteAPIError) as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"Wrote {len(snapshot['events'])} events to {settings.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
