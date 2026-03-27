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
- This `Changelog.md` to track meaningful repository changes.

### Changed

- `README.md` now includes repository governance files and standards.
- `Context.md` now reflects the repository governance baseline.
- `Progress.md` now reflects the addition of the governance files.
- `Debug.md` now records the governance documentation work alongside the tooling mismatch mitigation.
- `Agents.md` includes `README.md` in the documentation lockstep policy.

### Fixed

- No code defects fixed yet. Current mitigation is operational: verify repository writes with shell commands until the workspace tooling mismatch is resolved.
