# GitHub hosting and maintenance

Recheck current official documentation and the actual account's available settings; feature names, licences, runtimes and billing change. A public repository usually supports standard hosted CI and public security scanning without adding a local VM or a third-party service. Verify the actual feature before asserting that it is free or enabling a credit-consuming option.

## Research current options before selecting them

At each publication or hosting audit, consult GitHub's current [security quickstart](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository), relevant [repository settings guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features) and targeted [changelog entries](https://github.blog/changelog/). Search for changes affecting this deliverable, account type, supported languages, runner/runtime versions or intended distribution. Follow relevant discoveries into their current feature and billing documentation; do not conduct an exhaustive news sweep or assume a preview remains a preview.

Compare those sources with the actual repository settings and effective rules. For relevant options, record a short decision in the pull request or release handoff: checked date, primary source, benefit/coverage, availability, cost or data-access implications, and enabled/left off/not applicable. Keep enduring policy and non-obvious rationale in existing maintainer documentation; add a separate dated audit record only for an actual traceability requirement. Reuse still-current evidence within the same run; research does not authorize enabling everything. If online or account access is unavailable, distinguish prepared work from unverified hosting and do not invent current availability.

Choose settings for the project's actual code and contribution workflow. A source-only skill release is different from an application deployment or registry upload. Unsupported code scanning or unnecessary deployment controls are not release blockers. Public repository access to a feature does not imply its AI usage is free; verify feature-level billing.

Distinguish scanning an application for its use of AI from using AI to scan ordinary code. The latter can help a project that never calls a model. Select it by additional coverage, data handling and cost, rather than by whether the product itself uses AI. Re-read after saving and check actual results, not just a toggle.

## Establish the target and evidence

Verify the destination owner, repository URL, visibility and current remote tip before each publication. Treat an existing same-name private repository as an original to preserve, not a target to make public by default. Use a public/noreply identity chosen for the task. Review both author and committer metadata; server-generated squash merges may need an explicit author email. Never fabricate a development timeline.

Try the documented first-use journey in a fresh checkout and the installed command outside the source folder. Test the supported platform/toolchain matrix on standard hosted runners. Inspect actual run IDs, commit SHAs, job steps, package resources and installation results. Distinguish workflow configuration, successful execution, scanner findings, visible UI behaviour and human acceptance.

## Protect a workable contribution path

Use a saved, active ruleset covering the intended branch. Block force pushes and deletion, require appropriate pull requests, current-base status checks and resolution of review conversations. Bind required checks to their real integration where supported. For a solo owner, do not require self-approval or an unavailable second reviewer. Avoid an unrestricted bypass that makes the claimed protection ineffective. A new ruleset editor defaults to Disabled and is not evidence about the active saved rule. Re-read the effective branch rules after saving.

Configure useful dependency alerts and security-update proposals, secret scanning and push protection, private vulnerability reporting and supported code scanning. Review malware-alert coverage when available. Keep default workflow tokens read-only, prevent workflows approving their own pull requests and require approval for untrusted fork workflows as appropriate. Use pinned official actions, finite job limits and cancellable runs. Keep necessary scanner permissions at the narrow job/service level.

Select optional settings for the product: deployment gates need real deployment environments; signed-commit gates need a workable signing route; generic secret patterns can add noise; validity checks may contact secret providers; AI review/agentic repair may consume credits. Do not change account-wide security, install a new app or activate paid usage without its actual authorization. Leave automatic merging off unless requested and justified.

## Triage findings and update requests

A successful scanner job may still report alerts. Inspect the actual source/sink and trust boundary. Repair real defects with regressions. For intentional test execution or a legitimate local operator-selected path, document a specific classification and its reconsideration condition. Do not disable a language, query, local-input analysis or merge gate to clear the dashboard. Verify repaired alerts close on the published default branch; distinguish fixed, dismissed and still-open alerts.

Review all ready task-related dependency requests. Check the official upstream release and supported runtime requirements; a newer build tool can drop the oldest Python/Node version even when a no-build-isolation test remains green. Preserve supported versions unless a deliberate product decision changes them. Update stale branches safely, inspect the combined result and merge appropriate changes through the active gates. Replace or close incompatible proposals with a recorded reason rather than leaving a known bad suggestion unattended. Do not merge unrelated requests or infer that passing tests prove every compatibility claim.

After merging, verify the remote tip, current default-branch checks, active rules and actual alert state. Preserve unrelated work and uncertain ownership. Record open limitations without handing feasible authorized work back to the user as a new checklist.

Primary references: [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review), [CodeQL setup](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning), [malware alerts](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-malware-alerts), and [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
