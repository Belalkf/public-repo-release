# Public Repo Release

A local command for checking committed Git history for sensitive-data patterns, plus an optional agent skill for preparing and verifying public GitHub projects. The command works without an AI account. The skill helps finish an authorized release, including the hosting protections and verification that are easy to miss.

This is an experimental skill; independent end-to-end evaluation of agent behaviour remains open.

The skill covers the product boundary, newcomer workflow, privacy/history review, supported toolchains, hosted checks, practical branch protection, dependency maintenance, scanner triage and a truthful final handoff. It does not publish anything merely by being installed, and it does not activate paid services or rewrite history by default.

## Install with pip

Python 3.9+ is required; history checks also need Git on your command path. In a virtual environment, run:

```sh
python -m pip install public-repo-release
public-repo-release audit /path/to/repository
```

The audit prints JSON without candidate secret values. Exit status is 0 only when the supported history was completely checked and no recognized patterns were found; status 1 means findings or incomplete coverage, and 2 means invalid command arguments. `--seconds 120` changes the audit time limit from its default of 60 seconds. This is a bounded pattern check of local committed history, not a complete security audit or permission to publish. Unsaved files, external Git LFS payloads and submodule contents are excluded; binary objects require manual review. See [the history reference](skills/public-repo-release/references/private-to-public.md) for supported inputs and limits.

Pip installs the command and bundled instructions. To make the optional skill discoverable in Codex, explicitly copy it to your user skill folder:

```sh
public-repo-release install-skill --user
```

This creates `~/.agents/skills/public-repo-release`. Refresh skill discovery in your agent, then invoke `$public-repo-release`. Use `install-skill --destination /path/to/new-skill-folder` for another explicit destination. Existing files, folders and links are refused without replacement. A failed or cancelled copy can leave a partial new folder; inspect it and choose another destination rather than overwrite it. Pip installation alone never changes your agent's skill folder or publishes a repository. `python -m public_repo_release` is an alternative when the command is not on your path.

## Install with the skills CLI

From the project where you use your coding agent, run:

```sh
npx skills add Belalkf/public-repo-release
```

Choose `public-repo-release` and your agent when prompted. Installation applies to the current project by default. Add `-g` to install for your user across projects:

```sh
npx skills add Belalkf/public-repo-release -g
```

This downloads the installer and the skill. It does not publish a repository or install the Python/Git prerequisites for the optional history helper. The [skills CLI](https://github.com/vercel-labs/skills) requires Node.js and supports Codex and Claude Code; consult its documentation for current Node requirements and agent paths. Review the skill before use, then refresh your agent's skill discovery as required by that host. In Codex, invoke `$public-repo-release`.

The supported source location is `skills/public-repo-release/SKILL.md`. To inspect discovery without installing, run `npx skills add Belalkf/public-repo-release --list`. The installer uses network access and optional installation telemetry; see its [privacy controls](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md).

## Use a local checkout

The skill is in [skills/public-repo-release](skills/public-repo-release/SKILL.md). In a Codex environment that supports local skills, link that folder into your user skill directory, then invoke `$public-repo-release`. For example, from this checkout:

```sh
mkdir -p "$HOME/.agents/skills"
destination="$HOME/.agents/skills/public-repo-release"
if [ -e "$destination" ] || [ -L "$destination" ]; then
  printf 'Skill destination already exists; choose another name.\n'
else
  ln -s "$PWD/skills/public-repo-release" "$destination"
fi
```

Choose a different destination if that name already exists; preserve its contents. The command uses one source folder so edits and future Git history stay here. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery paths and refresh behaviour. Installer compatibility is separate from whether an agent follows the workflow well.

Example requests:

- “Prepare a clean public edition of this private tool; do not push yet.”
- “Publish this repository on my GitHub account and finish appropriate protections and hosted checks.”
- “Audit what is still missing from this public release, then complete the authorized fixes.”
- “Use $public-repo-release to publish this skill repository on GitHub, including a current options review and proportionate hosted checks; do not create a marketplace or registry listing.”

This is an initial public source release under the MIT licence. Installing it grants no permission to publish any target repository. The skills CLI can install directly from this GitHub repository; a skills.sh leaderboard entry depends on that directory's indexing and installation telemetry, not a separate Python or npm release.

## Try the helper safely

Create a disposable example with no private files, then inspect its history from this checkout:

```sh
demo="$(mktemp -d)"
git -C "$demo" init -q
git -C "$demo" -c user.name="Synthetic maintainer" -c user.email="fixture@users.noreply.github.com" commit --allow-empty -qm "Synthetic example"
python3 skills/public-repo-release/scripts/audit_history.py "$demo"
```

Expect `complete: true` and an empty findings list. The demo creates only a temporary repository; remove that directory when finished. For the agent workflow, start with the preparation-only example above and review its evidence before authorizing publication.

## Validate

The installed command has no runtime Python dependencies. To validate this checkout with Python 3.9+ and Git:

```sh
python3 -m pip install build twine
python3 scripts/check_distribution.py
python3 skills/public-repo-release/scripts/audit_history.py .
```

The distribution check downloads build tools into isolated environments, builds a source archive and wheel (the ready-to-install archive), rebuilds from the source archive, and tests a fresh installation outside the checkout. It creates `dist` and refuses to replace an existing output folder; choose a new one with `--output-dir /path/to/new-output`. After installing this checkout with `python -m pip install .`, focused tests can also run with `python -m unittest discover -s tests -v`.

Run the history helper after creating a local commit. It returns nonzero for findings, incomplete coverage or binary objects requiring manual review.

Pass the repository root, not an exported folder inside another checkout. Ordinary roots, linked worktrees and bare repositories are supported. Partial-clone settings and legacy graft files are rejected without changing them; use a separately authorized full clone or inspect those cases manually.

A successful result covers committed Git history only, not unsaved files, submodule repositories or external Git LFS content. It is a pattern audit, not a security certificate, and reports no candidate secret values. The skill's frontmatter can also be checked with the `quick_validate.py` supplied by Codex's built-in skill-creator; that check does not evaluate model judgment.

[Maintainer rules](AGENTS.md) · [MIT licence](LICENSE) · [Validation and limits](VALIDATION.md) · [Contributing](CONTRIBUTING.md) · [Security reporting](SECURITY.md) · [Changes](CHANGELOG.md)
