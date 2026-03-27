# Bug Report: Workspace File Tool Path Mismatch

## Summary

In the active VS Code agent workspace, search/indexing tools can resolve the repository path `/workspaces/Demo2`, but editor-side filesystem tools do not consistently resolve or mutate that same path.

## Environment

- Date: 2026-03-27
- Repository: `chris-page-gov/Demo2`
- Branch: `master`
- Observed workspace path: `/workspaces/Demo2`
- OS shown to user: macOS
- Runtime environment: dev container on Debian GNU/Linux 13

## Expected Behavior

All workspace-aware tools should resolve the same repository root and agree on file existence and file mutations.

## Actual Behavior

- `run_in_terminal` works against the real repository.
- `file_search` and `grep_search` can see files under `/workspaces/Demo2`.
- `read_file` reports `/workspaces/Demo2/README.md` does not exist.
- `list_dir` reports `/workspaces/Demo2` does not exist.
- `apply_patch` reports file not found for `/workspaces/Demo2/README.md`.
- `create_file` reported success creating files under `/workspaces/Demo2`, but those files were not present on disk afterward.

## Reproduction Steps

1. Open the workspace rooted at `/workspaces/Demo2`.
2. Confirm shell path with `pwd` and list files with `ls -la`.
3. Use search tools to locate `README.md` and `pyproject.toml`.
4. Attempt to read `/workspaces/Demo2/README.md` with the editor-side file read tool.
5. Attempt to patch `/workspaces/Demo2/README.md` with the editor-side patch tool.
6. Attempt to create a new file under `/workspaces/Demo2` with the editor-side file creation tool.
7. Verify on disk with `ls` and `git status --short`.

## Observed Results

- Search can see the repository.
- Shell can mutate the repository.
- Editor-side read and patch tools reject the same absolute path.
- Editor-side file creation may report success without persisting the file.

## Severity

High for agent reliability. It can produce false-positive success messages for file creation and causes verification delays.

## Workaround

Use shell-backed writes and verify every change with:

```bash
ls -la
git status --short
```

## Notes

This appears to be a workspace path binding or tool-layer synchronization problem rather than a repository-specific code issue.
