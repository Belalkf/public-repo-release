---
name: public-repo-release
description: Prepare, audit, or publish a repository as a public GitHub project, including a clean public edition of private work, portfolio readiness, hosted checks, and repository protections. Use for an explicit public-release request; not for ordinary commits, unrelated security audits, deployment, or package-registry uploads.
---

# Public Repo Release

Carry the authorized release through to a concrete, verifiable result. A source tree, a push, working software, and a protected hosting workflow are separate deliverables. Preserve the user's scope and existing approvals; do not keep returning feasible release work as a checklist for them to request again.

## Establish the release boundary

Read the repository's own instructions, Git/worktree state and current work owners. Identify the source, intended public edition, account/destination, and whether the user authorized preparation, public publication, or both. A request to make a reusable skill does not itself authorize publishing that skill.

Use the actual connected account. Prefer a suitable service connector; use an existing authenticated CLI/API or browser for capabilities the connector lacks. Never print, copy into files, or commit credentials. Keep account-wide settings and unrelated repositories outside scope. Preserve a private original when the user requests a separate public edition.

If the product decision is still open, check current primary alternatives and licences before spending effort on packaging. Establish the concrete audience and benefit, honest limitations and whether improving an existing tool is preferable. Do not invent uniqueness, adoption or efficiency claims.

## Prepare a newcomer-usable project

Make installation, one small synthetic demo and the common workflow work from a fresh checkout outside the author's workspace. Choose language/platform support from real evidence. Check declared runtime and build-tool compatibility, packaged resources, invalid inputs, cancellation, preservation of existing files and visible coverage gaps as relevant to the product. Resolve declared build requirements on the oldest supported toolchain; preinstalled tools can conceal incompatible manifest changes.

Use existing documentation and add a file only for a distinct reader need. Keep the first-use journey, current behaviour, material design rationale and support limits easy to find. Put per-commit execution logs and test results in pull requests/CI or the handoff; do not create session diaries, repeated readiness reports or a permanent document for every change. Release notes should explain user-visible changes and upgrade implications. Add a licence only within the author's rights. Include appropriate issue/security reporting routes and release metadata. Logos, marketplaces and registry uploads are optional, not public-readiness prerequisites.

For prompt-generating tools, distinguish deterministic measurements from model judgment. Generate common instructions once, keep file entries factual, and put optional evidence behind a disclosure without omitting safety-critical gaps from the copied request. Do not describe a fixed prompt or path heuristic as architectural understanding.

For repositories that distribute agent skills, including this skill itself, read [skill packages](references/skill-packages.md). Apply the same publication permissions and privacy review; invoking a skill on its own source grants no extra authority.

## Review what would become public

For private-to-public copies, read [private-to-public](references/private-to-public.md). Review the intended reachable Git history and identities, deleted files, binaries/screenshots and distributable archives as well as current source. Use synthetic examples. An empty pattern scan is supporting evidence, not a privacy certificate.

Run the bundled read-only `scripts/audit_history.py PATH` when useful. It scans local reachable history and reports finding types and object IDs without printing candidate secrets. It does not fetch, rewrite, upload, revoke keys or prove that hidden remote refs are clean. Inspect any finding locally before classifying it. A completed history pass does not cover uncommitted files, external Git LFS payloads or submodule contents; review the actual distribution boundary separately. If the helper rejects an input, preserve it and report the reason rather than fetching missing data or changing its history settings.

If an actual secret was published, revoke/rotate it first through the appropriate authorized process. Removing a current file or rewriting Git cannot retrieve other people's clones. Do not rewrite public history for ordinary bug fixes or to manufacture a development timeline.

## Publish and protect when authorized

For each GitHub publication or hosting audit, proactively research current official security/settings guidance and relevant recent changelog entries, then inspect the actual target settings. Read [hosting and maintenance](references/github.md) for the research and selection criteria; saved feature lists are not current evidence. Recheck the destination immediately before writing; stop an unexpected advance rather than overwrite it. Create a separate empty public repository if the chosen name belongs to a private original. Verify the public target and the private original after publishing.

Run proportional hosted checks on the supported platforms using standard public runners when available. Prefer existing tools or standard hosted runners; a local VM, new service or billable usage needs a concrete task benefit and authorization. Inspect the actual job results and findings; enabling a scanner or having a workflow file does not establish successful analysis or absence of alerts.

Scale the setup to the deliverable: a documentation-only package may have no code-scanning language or build matrix. Record inapplicable checks rather than installing irrelevant infrastructure. Configure useful protections before calling hosting complete: force-push/deletion protection, workable pull-request and CI gates, suitable secret/dependency/code scanning, private reporting, read-only workflow defaults and appropriate fork approvals. Avoid impossible self-approval rules for a solo maintainer. Inspect optional features and their costs instead of switching every checkbox on. Re-read settings after saving; a blank ruleset editor with enforcement disabled is not the active ruleset.

Review pending dependency requests rather than merging solely because they are newer or superficially green. Verify upstream changes, minimum toolchain/runtime requirements and the combined result against the current base. Merge suitable changes through the protected workflow; replace or close unsuitable proposals with an explicit compatibility reason within the authorized task. Keep human review meaningful; do not add automatic merging by default.

## Finish and report

Reassess the whole newcomer journey, complete owned diff, publishing boundary and wider failure cases. Repair in-scope defects with regressions and rerun affected checks. Confirm the actual remote tip, visibility, protections and clean/retained local work. Keep jobs bounded, owned and cleaned up.

Report the public URL or prepared local package, exact published commit, checks actually run, findings triaged versus defects fixed, and concrete missing acceptance. Separate implemented, unsupported and unverified behaviour. Stop only at completion or a concrete access, authorization or resource blocker; a difficult but feasible step or an intermediate update is not a stopping condition.
