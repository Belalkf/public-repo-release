# Changes

## v0.2.0 — Python command and optional skill

Install with `python -m pip install public-repo-release`. The new `public-repo-release audit PATH` command runs the existing bounded, read-only history check without an agent. `public-repo-release install-skill --user` separately installs the bundled instructions and refuses to replace existing files, folders or links. Both commands also work through `python -m public_repo_release`.

Source archives and wheels contain the same helper and complete skill resources. Release checks rebuild from the source archive and test the installed command outside the checkout. PyPI publishing uses the repository's `publish.yml` workflow and `pypi` environment without a stored PyPI API key. The skill remains experimental; helper tests do not establish agent judgment.

Installation instructions now include the skills CLI, with separate project and user scopes and an explicit distinction between installed instructions and helper prerequisites.

The bundled history helper now rejects inputs that could invalidate its local, read-only audit. Users of the original tag should use current main for these fixes:

- Require the selected repository root instead of silently auditing a parent repository.
- Reject legacy graft files that can hide earlier committed content.
- Reject partial-clone settings, including included configuration, and disable lazy fetching and transports so an audit does not download missing objects.

Normal repository roots, bare roots and linked worktrees remain supported. The input is preserved when rejected. See [PR 2](https://github.com/Belalkf/public-repo-release/pull/2) for the implementation and regression evidence. The published v0.1.0 tag has not moved.

## v0.1.0 — initial experimental release

Initial release of the agent skill and read-only Git history helper, with standalone-folder installation checks and explicit coverage limits. See the [published prerelease](https://github.com/Belalkf/public-repo-release/releases/tag/v0.1.0).
