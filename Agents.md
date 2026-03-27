# Agents

## Purpose

This file tracks the roles needed to deliver the Eventbrite data ingestion project.

## Primary Agent

- Name: Builder
- Responsibility: Implement the Python client, configuration, data fetching flow, and output handling.
- Current focus: Extend the organization-scoped MVP beyond the initial reusable module and JSON export.

## Supporting Agents

- Name: Product
- Responsibility: Define which Eventbrite data needs to be collected, how often it should be refreshed, and what downstream format is required.
- Current focus: Decide whether the MVP should later expand beyond events, venues, organizers, and ticket classes.

- Name: Data
- Responsibility: Define schemas for raw responses and normalized output.
- Current focus: Refine the JSON snapshot schema and determine whether additional normalization is needed.

- Name: Operations
- Responsibility: Manage credentials, environment setup, rate-limit handling, and deployment/runtime concerns.
- Current focus: Decide how the reusable module will be executed in production and how secrets will be managed outside development.

## Working Rules

- Until the workspace path mismatch is fixed, use shell-backed writes for repository changes.
- After every write, verify the result with `ls` and `git status --short` before reporting success.
- Treat shell output as the source of truth when shell state and editor-side tool state disagree.
- Record any recurrence of the tool mismatch in `Debug.md` and `Tooling-Notes.md`.

## Documentation Lockstep

When any project behavior, scope, workflow, operating assumption, or user-facing setup changes, update the related documentation in the same working session.

- `README.md`: project overview, setup, usage, and operator-facing notes.
- `Agents.md`: ownership, working rules, and decision responsibilities.
- `Context.md`: project goals, assumptions, requirements, and open questions.
- `Progress.md`: current status, completed work, next steps, and risks.
- `Debug.md`: failures, investigations, mitigations, and verification notes.
- `Tooling-Notes.md`: workspace-specific operating constraints and workarounds.
- `Changelog.md`: user-visible and repo-visible documentation or implementation changes.

Minimum documentation sync requirement for each meaningful change:

1. Update the source-of-truth document for the change itself.
2. Update `README.md` if setup, usage, scope, or operator expectations changed.
3. Update `Progress.md` if status, next steps, or risks changed.
4. Update `Debug.md` if the change was triggered by a bug, mismatch, or investigation.
5. Update `Changelog.md` with a dated entry under `Unreleased`.

## Decisions Pending

- Confirm whether the source scope should remain organization-based or add support for other collection scopes.
- Confirm whether later output targets should include CSV or database persistence in addition to JSON.
- Confirm how the reusable module should be scheduled or deployed outside local execution.
