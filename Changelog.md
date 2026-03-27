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
- This `Changelog.md` to track meaningful repository changes.

### Changed

- `.gitignore` now excludes common macOS, Windows, Python, and editor-generated files.
- `README.md` now includes repository governance files and cross-platform standards.
- `Context.md` now reflects the repository governance and cross-platform baseline.
- `Progress.md` now reflects the addition of the cross-platform repository controls.
- `Debug.md` now records the governance and cross-platform documentation work alongside the tooling mismatch mitigation.
- `Agents.md` includes `README.md` in the documentation lockstep policy.

### Fixed

- No code defects fixed yet. Current mitigation is operational: verify repository writes with shell commands until the workspace tooling mismatch is resolved.
