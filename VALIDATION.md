# Validation scope

## What the checks establish

The Python/Git tests exercise the bundled history helper and the installable package:

- Detection of removed synthetic secrets and annotated-tag contents without printing candidate values.
- Correct repository selection, read-only handling of supported roots/worktrees, and explicit rejection or incomplete coverage for unsupported history settings, missing history and content limits.
- Internal documentation links and helper execution from an installed-folder copy outside the checkout.

Use the commands in [README](README.md#validate) to reproduce them. The [Checks workflow](https://github.com/Belalkf/public-repo-release/actions/workflows/checks.yml) records results for each tested commit; its supported matrix is described in [Contributing](CONTRIBUTING.md). Skill-creator's optional format validator checks metadata and scaffolding, not decision quality.

## What remains unverified

Helper/package tests do not establish that an agent follows the workflow, chooses good settings or completes a publication correctly. Independent end-to-end agent evaluation remains unverified. The skills CLI installs instructions for supported hosts, including Codex and Claude Code; successful installation does not evaluate their decisions. Discovery refresh and invocation depend on the host, and compatibility with other hosts is not established by the helper tests.

A successful history pass covers only its supported local committed objects and recognized patterns. The exact exclusions and unsupported inputs are documented in [the history reference](skills/public-repo-release/references/private-to-public.md). It is not publication approval or a complete security audit.

## Choosing a version

The original v0.1.0 helper predates input-boundary fixes available on main. See [Changes](CHANGELOG.md) before choosing a tagged copy. [Hosting policy](CONTRIBUTING.md#hosting-policy) describes the maintained repository settings; per-commit test results remain in GitHub Actions and pull requests.
