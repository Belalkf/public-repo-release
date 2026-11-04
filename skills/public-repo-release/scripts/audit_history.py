"""Bounded, read-only local Git history pattern audit; never print candidate secrets."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import time

PATTERNS = {
    'private-home-path': re.compile(rb'/(?:Users|home)/[A-Za-z0-9_.-]+'),
    'private-key-header': re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'github-token': re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    'aws-access-key': re.compile(rb'\bAKIA[A-Z0-9]{16}\b'),
    'email-to-review': re.compile(rb'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
}


def audit(root, seconds=60, max_objects=5000, max_bytes=2 * 1024 * 1024, total_bytes=32 * 1024 * 1024):
    deadline = time.monotonic() + seconds
    environment = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
    environment.update(GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
                       GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
    command = ['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', '-C', str(Path(root).resolve())]
    result = {'commits': 0, 'inspected_objects': 0, 'findings': [], 'unreviewed': [], 'issues': []}

    def run(arguments, data=None):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Audit deadline reached')
        reply = subprocess.run(command + arguments, input=data, capture_output=True,
                               timeout=min(10, remaining), env=environment)
        if reply.returncode:
            raise ValueError('Git could not read the selected local repository')
        return reply.stdout

    try:
        ids = run(['rev-list', '--objects', '--all', '--no-object-names']).splitlines()
        if not ids:
            result['issues'].append('No reachable committed history to inspect')
        if len(ids) > max_objects:
            result['issues'].append('Object limit reached; history is incomplete')
        selected = ids[:max_objects]
        metadata = run(['cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize)'],
                       b'\n'.join(selected) + b'\n') if selected else b''
        used = 0
        for line in metadata.splitlines():
            oid, kind, size = line.split()
            if kind not in (b'blob', b'commit', b'tag'):
                continue
            identifier = oid.decode('ascii')
            if int(size) > max_bytes or used + int(size) > total_bytes:
                result['unreviewed'].append({'object': identifier, 'reason': 'content byte limit'})
                continue
            data = run(['cat-file', kind.decode('ascii'), identifier])
            used += len(data)
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                result['unreviewed'].append({'object': identifier, 'reason': 'binary or non-UTF-8'})
                continue
            if b'\0' in data:
                result['unreviewed'].append({'object': identifier, 'reason': 'NUL-containing content'})
                continue
            result['inspected_objects'] += 1
            result['commits'] += kind == b'commit'
            for name, pattern in PATTERNS.items():
                matches = pattern.findall(data)
                if name == 'email-to-review':
                    matches = [value for value in matches if not value.endswith(b'@users.noreply.github.com')
                               and value != b'noreply@github.com']
                if matches:
                    result['findings'].append({'object': identifier, 'kind': name, 'count': len(matches)})
    except (OSError, ValueError, subprocess.SubprocessError, TimeoutError):
        result['issues'].append('Git read or deadline failed; coverage is incomplete')
    result['complete'] = not (result['issues'] or result['unreviewed'])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', type=Path)
    args = parser.parse_args()
    result = audit(args.repository)
    print(json.dumps(result, indent=2))
    return int(bool(result['findings']) or not result['complete'])


if __name__ == '__main__':
    raise SystemExit(main())
