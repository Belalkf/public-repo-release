# Private-to-public boundary

## Select what will become public

Use a fresh destination when the user wants an independent public edition. Copy only the selected implementation and necessary tests/assets, preserving required licence notices. Do not copy `.git`, workspace configuration, credentials, local reports, screenshots of real projects, build caches or private operational instructions. Leave the private original and its remote/visibility unchanged. Review rather than automatically synchronize later fixes.

Inspect the actual Git object boundary before the first push: root commits, all intended branches/tags, alternate object stores/worktrees, author and committer emails, commit messages and deleted files. A current-tree secret scan does not inspect deleted history. An ignored file may still be tracked or present in an older commit. Check archives and image metadata/content separately. For an already-public repository, ordinary fixes should remain visible as normal commits.

## Run the local history helper

Run `python3 scripts/audit_history.py PATH` from this skill folder, or use the helper's absolute path. It uses only installed Git and Python. Defaults: 60-second overall deadline, 10-second Git calls, 5,000 reachable objects, 2 MiB per content object and 32 MiB total content. Git metadata enumeration is buffered before the object cap. It checks UTF-8 blob contents, commit messages/identities and annotated-tag text. Tree entry names, reflogs and unreachable objects require a separate manual review.

### Accepted input

The helper requires the selected path to be the repository root, supports ordinary roots, linked worktrees and bare repositories, ignores Git replacement objects, and marks shallow clones incomplete. Legacy graft files are rejected because they can hide parent commits. Partial-clone configuration, including included settings, is conservatively rejected before object inspection; lazy fetching and all Git transport protocols are disabled as additional safeguards. The helper does not repair or hydrate these repositories.

### Coverage and limits

It reads local reachable refs only, not remote objects, deleted server refs, pull-request caches, forks or other people's clones. A finding never prints the candidate value; it reports its kind and object ID for local inspection. Binary/oversized/unreadable objects and limits remain explicit unreviewed coverage. No network requests or mutations are authorized. Regression fixtures verify that rejected partial clones leave their Git files unchanged. Use trusted local Git metadata; this helper is not a sandbox for arbitrary `.git` directories.

A `complete` result means the supported local committed-history pass finished within its stated limits; it is not publication approval. Working-tree edits, untracked/ignored files, submodule repository contents and external Git LFS payloads are outside that pass. Review the exact files and external content intended for distribution separately. Obtain authorization for any full clone or missing-content download instead of repairing the input during the audit.

Primary Git references: [partial clones and demand fetching](https://git-scm.com/docs/partial-clone), [grafts and repository layout](https://git-scm.com/docs/gitrepository-layout), and [transport/lazy-fetch controls](https://git-scm.com/docs/git).

## Interpret findings

Expected public contact details or synthetic fixtures can trigger a pattern finding. Review their actual role; do not rewrite history, remove useful acknowledgements or dismiss a real credential merely to get a zero. An empty scan is not proof that no secret exists. Keep enduring coverage limits in user documentation and report the actual manual review in the pull request or release handoff.

If a real credential was exposed, revoke or rotate it first. History cleanup needs its own authorization and coordination because force updates, clones and cached references have consequences. See [GitHub's sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Never imply that deleting a commit makes a copied secret safe.
