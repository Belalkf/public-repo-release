# Changes

## After v0.1.0 — available on main

Installation instructions now include the skills CLI, with separate project and user scopes and an explicit distinction between installed instructions and helper prerequisites.

The bundled history helper now rejects inputs that could invalidate its local, read-only audit. Users of the original tag should use current main for these fixes:

- Require the selected repository root instead of silently auditing a parent repository.
- Reject legacy graft files that can hide earlier committed content.
- Reject partial-clone settings, including included configuration, and disable lazy fetching and transports so an audit does not download missing objects.

Normal repository roots, bare roots and linked worktrees remain supported. The input is preserved when rejected. See [PR 2](https://github.com/Belalkf/public-repo-release/pull/2) for the implementation and regression evidence. The published v0.1.0 tag has not moved.

## v0.1.0 — initial experimental release

Initial release of the agent skill and read-only Git history helper, with standalone-folder installation checks and explicit coverage limits. See the [published prerelease](https://github.com/Belalkf/public-repo-release/releases/tag/v0.1.0).
