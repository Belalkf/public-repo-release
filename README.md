# Public Repo Release

A reusable agent skill for taking a repository from private/local work to a usable public GitHub project, including the hosting protections and verification that are easy to miss. It helps finish an authorized release without treating a successful push or an empty scanner dashboard as the whole job.

The skill covers the product boundary, newcomer workflow, privacy/history review, supported toolchains, hosted checks, practical branch protection, dependency maintenance, scanner triage and a truthful final handoff. It does not publish anything merely by being installed, and it does not activate paid services or rewrite history by default.

## Use locally

The skill is in [skills/public-repo-release](skills/public-repo-release/SKILL.md). In a Codex environment that supports local skills, link that folder into your user skill directory, then invoke `$public-repo-release`. For example, from this checkout:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/skills/public-repo-release" "$HOME/.agents/skills/public-repo-release"
```

Choose a different destination if that name already exists; preserve its contents. The command uses one source folder so edits and future Git history stay here. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery paths and refresh behaviour. Other hosts can read SKILL.md and its references directly if they support agent skills; automatic discovery outside the tested environment is not claimed.

Example requests:

- “Prepare a clean public edition of this private tool; do not push yet.”
- “Publish this repository on my GitHub account and finish appropriate protections and hosted checks.”
- “Audit what is still missing from this public release, then complete the authorized fixes.”

This source package has no remote or publication by default. Publishing this skill itself is a separate explicit action. A future GitHub skill-installer path is `skills/public-repo-release`; no account URL, registry listing or marketplace availability is invented.

## Validate

No runtime or test dependencies beyond Python 3.9+ and Git:

```sh
python3 -m unittest discover -s tests -v
python3 skills/public-repo-release/scripts/audit_history.py .
```

Run the history helper after creating a local commit. It returns nonzero for findings, incomplete coverage or binary objects requiring manual review. It is a pattern audit, not a security certificate, and reports no candidate secret values. The skill's frontmatter can also be checked with the `quick_validate.py` supplied by Codex's built-in skill-creator; that check does not evaluate model judgment.

[Maintainer rules](AGENTS.md) · [MIT licence](LICENSE) · [Validation and limits](VALIDATION.md)
