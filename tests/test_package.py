"""Verify the installable folder without workspace siblings or third-party tools."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_internal_markdown_links_resolve(self):
        for document in ROOT.rglob('*.md'):
            if '.git' in document.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue((document.parent / target.split('#')[0]).is_file())

    def test_standalone_install_runs_outside_the_checkout(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            installed = root / 'installed-skill'
            shutil.copytree(ROOT / 'skills/public-repo-release', installed,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            entry = (installed / 'SKILL.md').read_text(encoding='utf-8')
            self.assertTrue(entry.startswith('---\nname: public-repo-release\n'))
            for target in re.findall(r'\]\(([^)]+)\)', entry):
                if '://' not in target:
                    self.assertTrue((installed / target).is_file())
            fixture = root / 'example'
            fixture.mkdir()
            subprocess.run(['git', '-C', str(fixture), 'init', '-q'], check=True,
                           capture_output=True, timeout=10)
            subprocess.run(['git', '-C', str(fixture), '-c', 'user.name=Synthetic maintainer',
                            '-c', 'user.email=fixture@users.noreply.github.com',
                            '-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm',
                            'Synthetic example'], check=True, capture_output=True, timeout=10)
            result = subprocess.run([sys.executable, str(installed / 'scripts/audit_history.py'),
                                     str(fixture)], cwd=root, capture_output=True,
                                    text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertTrue(report['complete'])
            self.assertEqual(report['findings'], [])
