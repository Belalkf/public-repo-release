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

Make installation, one small synthetic demo and the common workflow work from a fresh checkout outside the author's workspace. Choose language/platform support from real evidence. Check declared runtime and build-tool compatibility, packaged resources, invalid inputs, cancellation, preservation of existing files and visible coverage gaps as relevant to the product. A no-build-isolation build can pass while a new build requirement cannot run on the oldest supported interpreter.

Give each subject one owner: README for the first journey, behaviour/architecture for contracts, contribution guidance for checks, and a release record for actual results and missing acceptance. Add a licence only within the author's rights. Include appropriate issue/security reporting routes and release metadata. Logos, marketplaces and registry uploads are optional, not public-readiness prerequisites.

For prompt-generating tools, distinguish deterministic measurements from model judgment. Generate common instructions once, keep file entries factual, and put optional evidence behind a disclosure without omitting safety-critical gaps from the copied request. Do not describe a fixed prompt or path heuristic as architectural understanding.

## Review what would become public

For private-to-public copies, read [private-to-public](references/private-to-public.md). Review the intended reachable Git history and identities, deleted files, binaries/screenshots and distributable archives as well as current source. Use synthetic examples. An empty pattern scan is supporting evidence, not a privacy certificate.

Run the bundled read-only `scripts/audit_history.py PATH` when useful. It scans local reachable history and reports finding types and object IDs without printing candidate secrets. It does not fetch, rewrite, upload, revoke keys or prove that hidden remote refs are clean. Inspect any finding locally before classifying it.

If an actual secret was published, revoke/rotate it first through the appropriate authorized process. Removing a current file or rewriting Git cannot retrieve other people's clones. Do not rewrite public history for ordinary bug fixes or to manufacture a development timeline.

## Publish and protect when authorized

For GitHub publication, read [hosting and maintenance](references/github.md). Recheck the destination immediately before writing; stop an unexpected advance rather than overwrite it. Create a separate empty public repository if the chosen name belongs to a private original. Verify the public target and the private original after publishing.

Run proportional hosted checks on the supported platforms using standard public runners when available. Do not install a local VM, incur costs or add third-party services just to complete a release check. Inspect the actual job results and findings; enabling a scanner or having a workflow file does not establish successful analysis or absence of alerts.

Configure useful protections before calling hosting complete: force-push/deletion protection, workable pull-request and CI gates, suitable secret/dependency/code scanning, private reporting, read-only workflow defaults and appropriate fork approvals. Avoid impossible self-approval rules for a solo maintainer. Inspect optional features and their costs instead of switching every checkbox on. Re-read settings after saving; a blank ruleset editor with enforcement disabled is not the active ruleset.

Review pending dependency requests rather than merging solely because they are newer or superficially green. Verify upstream changes, minimum toolchain/runtime requirements and the combined result against the current base. Merge suitable changes through the protected workflow; replace or close unsuitable proposals with an explicit compatibility reason within the authorized task. Keep human review meaningful; do not add automatic merging by default.

## Finish and report

Reassess the whole newcomer journey, complete owned diff, publishing boundary and wider failure cases. Repair in-scope defects with regressions and rerun affected checks. Confirm the actual remote tip, visibility, protections and clean/retained local work. Keep jobs bounded, owned and cleaned up.

Report the public URL or prepared local package, exact published commit, checks actually run, findings triaged versus defects fixed, and concrete missing acceptance. Separate implemented, unsupported and unverified behaviour. Stop only at completion or a concrete access, authorization or resource blocker; a difficult but feasible step or an intermediate update is not a stopping condition.
