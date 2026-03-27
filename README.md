# Demo2

Python project for retrieving Eventbrite data from the API and exporting an organization-scoped JSON snapshot for downstream use.

## Status

This repository includes the first implementation slice for Eventbrite ingestion:

- configuration loading from environment variables and optional `.env`
- authenticated Eventbrite API client with pagination and basic retry handling
- event enrichment for venues, organizers, and ticket classes
- JSON file output
- unit tests for config, client, service, output, and top-level orchestration
- repo-enforced quality tooling for linting, typing, tests, pre-commit, and CI

The current implementation is designed as a reusable library module with a thin top-level entrypoint.

## Engineering Guardrails

This repository follows a test-driven workflow for implementation changes.

- Write or update a failing test first when changing behavior.
- Make the smallest production change needed to satisfy the test.
- Run focused local tests without coverage during iteration.
- Run the full quality gate before considering work complete.
- Keep documentation in lockstep with behavior and workflow changes.

Local iterative quality gate:

```bash
python3 -m ruff check .
python3 -m mypy
python3 -m pytest
```

Full coverage gate:

```bash
make coverage
```

The coverage gate enforces a minimum of 90% total coverage and is intended for final local validation and CI, not every small iterative test run.

GitHub branch protection is still a required follow-up, but it must be enabled in the repository settings outside this workspace.

Install local hooks:

```bash
python3 -m pre_commit install
```

## Typing Policy

The repository uses `mypy` in strict mode for production code under `eventbrite/` and `main.py`.

That means typing is strict for application code, but not globally universal across every possible file type in the repo. Tests are not currently included in the strict `mypy` target, which is intentional to keep the signal focused on shipped code.

## Current MVP Scope

- Fetch events for a single Eventbrite organization
- Enrich events with venue, organizer, and ticket-class data
- Write a JSON snapshot to disk
- Fail clearly when required configuration is missing or an API request fails

## Installation

```bash
/usr/bin/python3 -m pip install --user --break-system-packages -e .
/usr/bin/python3 -m pip install --user --break-system-packages -e .[dev]
```

## Configuration

Copy `.env.example` to `.env` for local development or provide equivalent environment variables.

Required variables:

- `EVENTBRITE_API_TOKEN`
- `EVENTBRITE_ORGANIZATION_ID`

Optional variables:

- `EVENTBRITE_OUTPUT_PATH` default: `data/eventbrite-events.json`
- `EVENTBRITE_PAGE_SIZE` default: `50`
- `EVENTBRITE_PAGE_LIMIT` default: unset
- `EVENTBRITE_TIMEOUT_SECONDS` default: `30`
- `EVENTBRITE_API_BASE_URL` default: `https://www.eventbriteapi.com/v3`

## Usage

Run the entrypoint directly:

```bash
/usr/bin/python3 main.py
```

When required configuration is missing or an API request fails, the program exits with status code `1` and prints a concise error message to stderr.

Run the tests:

```bash
/usr/bin/python3 -m pytest
```

## Repository Standards

This repository includes the baseline governance and cross-platform controls expected for a production-ready public repository:

- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CONTRIBUTORS.md`
- `.github/CODEOWNERS`
- `.github/workflows/ci.yml`
- `.github/pull_request_template.md`
- `.gitattributes`
- `.editorconfig`
- `.pre-commit-config.yaml`
- `Changelog.md`
- `Makefile`

Branch protection should be configured on the default branch to require the CI workflow before merge.

## Cross-Platform Rules

The repository is configured to work consistently across macOS, Windows, and Linux:

- Git normalizes text files to LF with `.gitattributes`.
- Windows-native script files such as `.bat`, `.cmd`, and `.ps1` are preserved as CRLF.
- Editors are guided by `.editorconfig` for UTF-8, final newline, trimming, and indentation.
- Common macOS, Windows, Python, editor-generated files, and generated output under `data/` are excluded in `.gitignore`.

## Working Docs

- `Agents.md`: ownership and workflow rules
- `Context.md`: project context and open questions
- `Progress.md`: status and next steps
- `Debug.md`: investigation and mitigation log
- `Tooling-Notes.md`: workspace-specific tooling constraints

## Temporary Workspace Rule

This workspace currently has a tool-path mismatch between shell access and some editor-side file tools. Until that is fixed:

1. Use shell-backed writes for repository changes.
2. Verify every write with `ls` and `git status --short`.
3. Treat shell state as authoritative if tools disagree.
