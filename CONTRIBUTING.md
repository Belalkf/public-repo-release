# Contributing

Keep changes focused and preserve publication permissions. Test with synthetic temporary repositories; never use credentials or real private reports as fixtures. Corrected script defects need regression tests. Python 3.9 is the minimum; the helper uses only the standard library and installed Git.

Run the commands in [README](README.md#validate). CI builds both archives, rebuilds a wheel from the source archive and tests that installation on Python 3.9 and 3.14 on Linux, and Python 3.14 on macOS and Windows. These checks exercise the helper and package; they do not establish agent judgment or a complete security audit. [Validation scope](VALIDATION.md) owns those limits.

Keep documentation paragraphs unwrapped and each subject in one place. Include every runtime reference inside the installable skill folder. Document current behaviour and material limits; put per-commit test logs in the pull request or CI. Use [Changes](CHANGELOG.md) for user-visible fixes and version implications.

## Hosting policy

Open a pull request and wait for all four test jobs against the current base. Resolve review conversations. CodeQL blocks high-or-higher security findings and standard errors. No human approval is required for the solo maintainer. Main has no bypass and blocks deletion and force updates; release tags also block deletion and force updates. Fixes use new commits, not retargeted published tags.

Workflow defaults are read-only, cannot approve pull requests and require approval for outside contributors. Actions are pinned, jobs are bounded and no self-hosted runner or deployment credential is needed. Dependabot alerts, security-update proposals, malware alerts and monthly Actions updates are enabled; automatic merging is off.

PyPI releases use new version tags matching `pyproject.toml`. The `publish.yml` workflow validates and tests archives in a read-only build job; only the separate upload job can request a short-lived publishing identity. The `pypi` environment admits version tags only, and PyPI trusts only this repository, workflow and environment. Never move an existing release tag or store a PyPI API key in this repository.

Public secret scanning and push protection are enabled; optional validity-provider calls and generic/AI patterns remain off. Public partner scanning may notify token providers. CodeQL covers Python and Actions. AI Scan and agentic autofix remain off because billable usage has not been authorized; non-agentic Copilot Autofix remains at its public-repository default. Use [private security reporting](SECURITY.md) for vulnerabilities.

Tests intentionally write fake token strings into automatically cleaned temporary repositories. Clear-text-storage findings on these fixtures were classified as false positives. Revisit that classification if fixtures contain real credentials or persist outside temporary folders; do not disable the scanner query.

Before changing the policy, review current [GitHub security guidance](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository), [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [AI feature billing](https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security). Account-wide settings, paid features and external distribution need their own authorization.
