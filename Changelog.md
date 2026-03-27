# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog principles and uses an `Unreleased` section until the project has tagged releases.

## [Unreleased]

### Added

- Tracking documents for project coordination: `Agents.md`, `Context.md`, `Progress.md`, and `Debug.md`.
- `Tooling-Notes.md` documenting the current workspace path mismatch and the shell-verified workaround.
- Documentation operating rules in `Agents.md` for shell-backed writes and lockstep updates.
- `README.md` project overview covering current status, planned scope, temporary workspace rules, and next steps.
- `LICENSE` using the MIT license.
- `CONTRIBUTING.md` with contribution workflow and documentation expectations.
- `CODE_OF_CONDUCT.md` establishing contributor behavior standards.
- `SECURITY.md` documenting vulnerability reporting expectations.
- `CONTRIBUTORS.md` to track maintainers and contributors.
- `.github/CODEOWNERS` assigning default ownership.
- `.gitattributes` to normalize text files and preserve Windows-native script line endings.
- `.editorconfig` to enforce UTF-8, LF endings, final newline, trimming, and indentation defaults.
- `.env.example` documenting required Eventbrite configuration values.
- `eventbrite/` package with configuration loading, API client, enrichment service, models, and JSON output.
- Unit tests for configuration, pagination, enrichment, and JSON output behavior.
- This `Changelog.md` to track meaningful repository changes.

### Changed

- `.gitignore` now excludes generated Eventbrite output under `data/` in addition to OS, Python, and editor-generated files.
- `README.md` now includes real installation, configuration, usage, and MVP scope details.
- `Context.md` now reflects the confirmed MVP decisions and implemented package structure.
- `Progress.md` now reflects that the first implementation slice is complete.
- `Debug.md` now records the implementation milestone and remaining live-validation risk.
- `pyproject.toml` now defines runtime dependencies for `requests` and `python-dotenv` plus optional test dependencies.
- `main.py` now runs the real Eventbrite ingestion flow instead of a placeholder print statement.

### Fixed

- Replaced the placeholder application flow with a real organization-scoped Eventbrite ingestion path.
