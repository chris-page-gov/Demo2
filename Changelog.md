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
- Unit tests for configuration, pagination, enrichment, JSON output, and main orchestration behavior.
- `.pre-commit-config.yaml` to run repository checks before commit.
- `.github/workflows/ci.yml` to run linting, typing, tests, and the coverage gate on GitHub.
- `.github/pull_request_template.md` to require verification details and test-driven workflow evidence.
- `Makefile` convenience targets for install, lint, type-check, tests, and coverage checks.
- This `Changelog.md` to track meaningful repository changes.
- Documentation noting that branch protection remains a manual GitHub follow-up while the CI and coverage gates are already in place.

### Changed

- `.gitignore` now excludes generated Eventbrite output under `data/` in addition to OS, Python, and editor-generated files.
- `README.md` now includes real installation, configuration, usage, TDD expectations, typing policy, and quality-gate guidance.
- `CONTRIBUTING.md` now defines a TDD-first workflow, iterative local testing without coverage, a final coverage gate, and a definition of done.
- `Agents.md` now includes engineering rules for test-driven development, fast local test loops, and required quality checks.
- `Context.md` now reflects the repository engineering baseline around CI, pre-commit, strict typing, and separate coverage enforcement.
- `Progress.md` now reflects the addition of the 90% coverage gate and strict typing policy.
- `Debug.md` now records the addition of the engineering guardrails alongside the tooling mismatch mitigation.
- `pyproject.toml` now defines runtime dependencies, dev tooling dependencies, shared config for `pytest`, `ruff`, and strict `mypy`, and a separate 90% coverage threshold.
- `main.py` now runs the real Eventbrite ingestion flow instead of a placeholder print statement.

### Fixed

- Replaced the placeholder application flow with a real organization-scoped Eventbrite ingestion path.
