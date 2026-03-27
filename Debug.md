# Debug

## Objective

Track integration issues, failed assumptions, and verification steps while building the Eventbrite API client.

## Current Debug State

- No live Eventbrite API validation has been recorded yet.

## Debug Checklist

- Verify the API token is present before making requests.
- Confirm the organization ID is valid for the provided token.
- Log HTTP status codes and relevant response bodies for failures.
- Check pagination behavior against real multi-page event responses.
- Distinguish authentication failures from permission failures.
- Capture rate-limit responses and retry behavior.

## Investigation Log

### 2026-03-27

- Created initial debug tracker.
- No runtime API integration existed yet, so there were no request failures to record.
- Added the first implementation slice: config loading, authenticated client, organization-scoped event enrichment, JSON output, and unit tests.
- Live API verification is still pending.

## Useful Signals To Capture

- Request URL
- Query parameters
- Response status code
- Response headers related to rate limits
- Shortened response body for errors
- Environment variables expected by the script

## Tooling Mismatch

### 2026-03-27

- Search tools could see the repository at `/workspaces/Demo2`.
- Shell commands could read and write the repository normally.
- Editor-side read and edit tools failed to resolve the same absolute path.
- One file creation tool reported success without creating a file on disk.
- Temporary mitigation: use shell-backed writes and verify every change with `ls` and `git status --short`.

### 2026-03-27 Documentation Governance

- Added a temporary rule in `Agents.md` to enforce shell-verified writes while the workspace path mismatch remains unresolved.
- Added a lockstep documentation policy so tracking docs and the changelog are updated together.
- Added `Changelog.md` as the baseline history for repo-visible changes.
- Added baseline repository governance files for license, contribution policy, security reporting, code ownership, and contributor guidance.
- Added Git and editor-level cross-platform controls for line endings, formatting defaults, and OS-specific ignore patterns.
