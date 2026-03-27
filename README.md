# Demo2

Python project for retrieving Eventbrite data from the API and preparing it for downstream use.

## Status

This repository is in setup phase. The project scaffolding, governance files, and documentation trackers are in place, but the Eventbrite API integration has not been implemented yet.

## Scope

- Authenticate to the Eventbrite API
- Fetch Eventbrite event data from one or more endpoints
- Handle pagination, request failures, and rate limits
- Normalize or emit the resulting data for downstream consumption

## Repository Standards

This repository now includes the baseline governance files expected for a production-ready public repository:

- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CONTRIBUTORS.md`
- `.github/CODEOWNERS`
- `Changelog.md`

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

## Next Steps

1. Decide which Eventbrite endpoint to implement first.
2. Add configuration for API credentials.
3. Add an HTTP client and request flow.
4. Add pagination and error handling.
5. Document real setup and usage once implementation begins.
