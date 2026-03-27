# Context

## Project Goal

Build a Python project that retrieves Eventbrite data from the API and prepares it for downstream use.

## Current State

- The repository is a minimal Python project scaffold.
- `main.py` currently prints a placeholder message.
- `pyproject.toml` defines the package but has no dependencies yet.
- `README.md` documents the project scope, current status, governance baseline, cross-platform controls, and workspace operating rules.
- Baseline repository governance files are present for licensing, contribution guidance, conduct, security reporting, ownership, and changelog tracking.
- Git and editor-level configuration now enforce consistent line endings and common formatting across macOS, Windows, and Linux.

## Known Requirements

- Use the Eventbrite API as the source of truth.
- Add tracking artifacts for project coordination and execution.
- Keep operator-facing documentation in `README.md` aligned with workflow changes.
- Maintain repository governance files for licensing, contribution, and security expectations.
- Maintain cross-platform Git and editor settings so the repository behaves consistently on Mac and PC.

## Expected Technical Needs

- Authentication with an Eventbrite private token or other approved credential flow.
- HTTP client support for API requests.
- Pagination handling for list endpoints.
- Error handling for rate limits, timeouts, and invalid credentials.
- Configuration via environment variables.
- Logging or debug output for failed requests.

## Open Questions

- Which Eventbrite endpoint should be implemented first?
- What exact fields need to be captured from the API response?
- Should the first version persist data or just print or save raw results?
- What execution model is expected: CLI, scheduled task, or reusable module?
