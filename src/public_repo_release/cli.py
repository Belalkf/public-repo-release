"""Explicit local commands; installing this package never publishes anything."""
import argparse
from importlib.metadata import version
import json
from pathlib import Path

from ._skill.scripts.audit_history import audit
from .install import install_skill


def bounded_seconds(value):
    try:
        seconds = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('Use a whole number of seconds from 1 to 3600')
    if not 1 <= seconds <= 3600:
        raise argparse.ArgumentTypeError('Use a whole number of seconds from 1 to 3600')
    return seconds


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', action='version', version=version('public-repo-release'))
    commands = parser.add_subparsers(dest='command', required=True)
    history = commands.add_parser('audit', help='Check local committed Git history; output JSON')
    history.add_argument('repository', type=Path)
    history.add_argument('--seconds', type=bounded_seconds, default=60,
                         help='Time limit from 1 to 3600 seconds (default: 60)')
    install = commands.add_parser('install-skill', help='Copy the bundled agent instructions')
    destination = install.add_mutually_exclusive_group(required=True)
    destination.add_argument('--user', action='store_true', help='Use ~/.agents/skills/public-repo-release')
    destination.add_argument('--destination', type=Path, help='Create this new skill folder')
    args = parser.parse_args(argv)
    if args.command == 'audit':
        result = audit(args.repository, seconds=args.seconds)
        print(json.dumps(result, indent=2))
        return int(bool(result['findings']) or not result['complete'])
    target = Path.home() / '.agents/skills/public-repo-release' if args.user else args.destination
    try:
        installed = install_skill(target)
    except OSError:
        parser.exit(2, 'Skill installation failed. Existing files were preserved; '
                    'check the destination and permissions. A partial new folder may remain.\n')
    print('Skill installed at {}. Refresh your agent to discover it.'.format(installed))
    return 0
