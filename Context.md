# Context

## Project Goal

Build a Python project that retrieves Eventbrite data from the API and prepares it for downstream use.

## Current State

- The repository now includes an organization-scoped Eventbrite ingestion MVP.
- `main.py` orchestrates configuration loading, snapshot fetching, and JSON output.
- `eventbrite/` contains configuration, client, service, model, and output modules.
- `pyproject.toml` defines runtime dependencies for Eventbrite access and optional test dependencies.
- `README.md` documents installation, configuration, usage, governance, cross-platform controls, and workspace operating rules.
- Baseline repository governance files are present for licensing, contribution guidance, conduct, security reporting, ownership, and changelog tracking.
- Git and editor-level configuration enforce consistent line endings and common formatting across macOS, Windows, and Linux.

## Confirmed MVP Decisions

- Runtime model: reusable Python module with a thin entrypoint.
- Source scope: organization-scoped Eventbrite fetch.
- Related entities: venues, organizers, and ticket classes.
- Output format: JSON file.
- Authentication: environment variables with optional `.env` support for development.

## Known Requirements

- Use the Eventbrite API as the source of truth.
- Keep operator-facing documentation in `README.md` aligned with workflow changes.
- Maintain repository governance files for licensing, contribution, and security expectations.
- Maintain cross-platform Git and editor settings so the repository behaves consistently on Mac and PC.
- Keep shell-verified writes in effect while the workspace tool mismatch remains unresolved.

## Expected Technical Needs

- Real-world verification against a valid Eventbrite API token and organization.
- More robust retry and backoff tuning if rate limits become a problem.
- Additional schema decisions if downstream consumers need a flatter normalized shape.
- Scheduling and deployment decisions once local execution is validated.

## Open Questions

- Should later iterations support additional collection scopes beyond organization-based fetches?
- Should later iterations persist data to CSV or a database in addition to JSON?
- What deployment model is required once the reusable module is validated locally?
