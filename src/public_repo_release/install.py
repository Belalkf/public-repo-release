"""Copy instructions only when explicitly requested; preserve existing paths."""
from importlib import resources
from pathlib import Path
import shutil
import tempfile


RESOURCE_FILES = (
    'SKILL.md', 'agents/openai.yaml', 'references/private-to-public.md',
    'references/github.md', 'references/skill-packages.md', 'scripts/audit_history.py',
)


def install_skill(destination):
    """Stage complete resources, then claim a new destination without replacing it."""
    destination = Path(destination).expanduser()
    # Use the regular parent package: Python 3.9 cannot read namespace resources.
    source = resources.files('public_repo_release').joinpath('_skill')
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.public-repo-release-', dir=destination.parent))
    try:
        for relative in RESOURCE_FILES:
            target = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.joinpath(relative).read_bytes())
        destination.mkdir()  # Atomic claim also refuses files, directories and broken links.
        for relative in RESOURCE_FILES:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(stage / relative, target)
    finally:
        # Retain a partial new destination on failure; never delete user-owned files.
        shutil.rmtree(stage)
    return destination
