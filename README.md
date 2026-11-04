# Public Repo Release

A reusable agent skill for taking a repository from private/local work to a usable public GitHub project, including the hosting protections and verification that are easy to miss. It helps finish an authorized release without treating a successful push or an empty scanner dashboard as the whole job.

This is an experimental skill; independent end-to-end evaluation of agent behaviour remains open.

The skill covers the product boundary, newcomer workflow, privacy/history review, supported toolchains, hosted checks, practical branch protection, dependency maintenance, scanner triage and a truthful final handoff. It does not publish anything merely by being installed, and it does not activate paid services or rewrite history by default.

## Use locally

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

Choose a different destination if that name already exists; preserve its contents. The command uses one source folder so edits and future Git history stay here. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery paths and refresh behaviour. Other hosts can read SKILL.md and its references directly if they support agent skills; automatic discovery outside the tested environment is not claimed.

Example requests:

- “Prepare a clean public edition of this private tool; do not push yet.”
- “Publish this repository on my GitHub account and finish appropriate protections and hosted checks.”
- “Audit what is still missing from this public release, then complete the authorized fixes.”
- “Use $public-repo-release to publish this skill repository on GitHub, including a current options review and proportionate hosted checks; do not create a marketplace or registry listing.”

This is an initial public source release under the MIT licence. The install folder is `skills/public-repo-release`. Installing it grants no permission to publish any target repository. No marketplace or package-registry listing is provided.

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

No runtime or test dependencies beyond Python 3.9+ and Git:

```sh
python3 -m unittest discover -s tests -v
python3 skills/public-repo-release/scripts/audit_history.py .
```

Run the history helper after creating a local commit. It returns nonzero for findings, incomplete coverage or binary objects requiring manual review.

Pass the repository root, not an exported folder inside another checkout. Ordinary roots, linked worktrees and bare repositories are supported. Partial-clone settings and legacy graft files are rejected without changing them; use a separately authorized full clone or inspect those cases manually.

A successful result covers committed Git history only, not unsaved files, submodule repositories or external Git LFS content. It is a pattern audit, not a security certificate, and reports no candidate secret values. The skill's frontmatter can also be checked with the `quick_validate.py` supplied by Codex's built-in skill-creator; that check does not evaluate model judgment.

[Maintainer rules](AGENTS.md) · [MIT licence](LICENSE) · [Validation and limits](VALIDATION.md) · [Contributing](CONTRIBUTING.md) · [Security reporting](SECURITY.md) · [Changes](CHANGELOG.md)
