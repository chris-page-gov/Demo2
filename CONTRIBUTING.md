# Contributing

Thanks for contributing to this repository.

## Before You Start

- Review `README.md` for current project scope and operating notes.
- Review `Agents.md` for the active documentation lockstep rule.
- Check `Progress.md` and `Context.md` before changing project scope or implementation direction.
- If your change was triggered by a bug or tooling problem, update `Debug.md` as part of the same work.

## Development Workflow

1. Create a focused branch for your work.
2. Keep changes small and easy to review.
3. Update documentation in lockstep when behavior, setup, or project assumptions change.
4. Add or update tests when implementation code is added.
5. Update `Changelog.md` under `Unreleased` for meaningful changes.

## Pull Request Expectations

- Describe what changed and why.
- Link any related issue.
- Note any manual verification performed.
- Call out open questions, tradeoffs, or follow-up work.

## Documentation Requirements

For any meaningful change, review and update the relevant files:

- `README.md`
- `Agents.md`
- `Context.md`
- `Progress.md`
- `Debug.md`
- `Tooling-Notes.md`
- `Changelog.md`

## Code Standards

- Prefer small, reviewable commits.
- Keep implementation aligned with the existing project style.
- Avoid unrelated refactors in the same change.
- Handle API failures explicitly when integrating with external services.

## Reporting Security Issues

Do not open public issues for security-sensitive problems. Follow `SECURITY.md` instead.
