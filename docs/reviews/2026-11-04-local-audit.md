# Local audit boundary review — November 4, 2026

The first public release's history helper could report a completed pass for the wrong repository, miss earlier content hidden by legacy graft settings, or let Git fetch missing objects into a partial clone. These are defects in the helper's local-read-only and input-boundary promises. They are separate from the two reviewed synthetic CodeQL findings recorded for the initial release.

## Reproduced and repaired

Three synthetic regressions failed against the original implementation before the repair. An ordinary subfolder caused Git to discover its parent repository. A local `info/grafts` file made the latest commit appear to have no parent, hiding a removed fake token. A configured partial clone with a missing blob and a disposable local remote completed rather than rejecting the input.

The helper now requires the exact repository root and rejects graft files or partial-clone settings before inspecting content. Included Git configuration is checked too. Git transport protocols and lazy fetching are disabled as additional safeguards. Inputs are preserved; no history settings are rewritten and no missing objects are downloaded. Ordinary repositories, linked worktrees and bare repository roots remain supported.

## Evidence and limits

Seventeen local tests passed on Python 3.9.6 and Git 2.39.5, including six new tests for these boundaries. The partial-clone fixture compares all local Git-file contents before and after the audit; the included-config case does the same. The graft fixture confirms its file is preserved. A linked-worktree test verifies both normal operation and rejection of a graft file in the shared metadata directory. Temporary repositories are cleaned automatically. Hosted results belong to the associated pull request and final commit checks; this local result alone does not establish platform acceptance.

Partial-clone configuration is conservatively unsupported even if all currently reachable objects happen to be present. An existing graft file is rejected even when empty. Git's reference enumeration is still buffered before the content-object cap, so this is not a strict memory bound for arbitrarily large repositories. Working-tree edits, ignored/untracked files, submodule repositories, external Git LFS payloads and hidden remote history remain outside the committed-history pass. The helper assumes a trusted installed Git and local metadata; it does not sandbox an arbitrary `.git` directory. Agent judgment remains independently unevaluated.

The original v0.1.0 tag and release record are preserved. This repair uses new commits through the protected contribution workflow; it does not rewrite the release history or change hosting permissions or paid features.
