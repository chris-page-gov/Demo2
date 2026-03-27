# Tooling Notes

## Workspace Tool Mismatch

Date observed: 2026-03-27

### Summary

In this workspace, the shell and search tools resolve the repository correctly at `/workspaces/Demo2`, but some editor-side file tools do not operate on that same path reliably.

### Confirmed Behavior

- `run_in_terminal` reads and writes the real repository correctly.
- `file_search` and `grep_search` can see real files in the repository.
- `read_file`, `list_dir`, and `apply_patch` failed to resolve `/workspaces/Demo2`.
- `create_file` reported success for new files that did not appear on disk.
- Shell verification with `ls` and `git status` showed the true repository state.

### Safe Operating Procedure

1. Treat shell output as the source of truth for this workspace.
2. After any file write, verify with `ls` and `git status --short`.
3. Avoid relying on editor-side write success messages unless the shell confirms the result.
4. Prefer shell-backed file creation and editing until the workspace mapping issue is fixed.

### Impact

- Reported write success may be false.
- Verification steps are required before claiming changes were applied.
- Editor-side file operations may fail even when search/indexing succeeds.
