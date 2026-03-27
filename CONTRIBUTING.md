# Contributing

Thanks for contributing to this repository.

## Before You Start

- Review `README.md` for current project scope and operating notes.
- Review `Agents.md` for the active documentation lockstep rule.
- Check `Progress.md` and `Context.md` before changing project scope or implementation direction.
- If your change was triggered by a bug or tooling problem, update `Debug.md` as part of the same work.

## Development Workflow

1. Create a focused branch for your work.
2. Start with a failing or missing test for the behavior you are changing.
3. Make the smallest production change needed to satisfy the test.
4. Refactor only after the tests are green.
5. During iteration, run focused local tests without coverage.
6. Run the full quality gate before opening a pull request.
7. Update documentation in lockstep when behavior, setup, or project assumptions change.
8. Update `Changelog.md` under `Unreleased` for meaningful changes.
9. Follow `.editorconfig` and `.gitattributes` so cross-platform formatting stays consistent.

## Local Quality Gate

Iterative local checks:

```bash
python3 -m ruff check .
python3 -m mypy
python3 -m pytest
```

Final local validation:

```bash
make coverage
```

The coverage gate enforces 90% total coverage and is intended for final validation and CI rather than every edit/test cycle.

Optional helpers:

```bash
make check
python3 -m pre_commit run --all-files
```

## Pull Request Expectations

- Describe what changed and why.
- Link any related issue.
- Note the tests that drove the change.
- Include the verification commands you ran.
- Call out open questions, tradeoffs, or follow-up work.

## Definition of Done

A change is not done until all of the following are true:

- The relevant behavior is covered by tests.
- `ruff`, `mypy`, and `pytest` pass.
- The 90% coverage gate passes in CI or via the local coverage command.
- Documentation is updated in lockstep where needed.
- The changelog is updated for meaningful repo-visible changes.

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
- Do not introduce platform-specific line endings or editor-specific formatting drift.
- Do not merge behavior changes without test coverage unless there is a documented reason in the pull request.

## Reporting Security Issues

Do not open public issues for security-sensitive problems. Follow `SECURITY.md` instead.
