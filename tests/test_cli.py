"""Exercise installed commands outside the source tree, with synthetic history."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def command(self, *args, env=None):
        return subprocess.run([sys.executable, '-m', 'public_repo_release', *map(str, args)],
                              cwd=self.root, env=env, capture_output=True, text=True, timeout=20)

    def git(self, *args):
        subprocess.run(['git', '-C', str(self.root), *args], check=True,
                       capture_output=True, timeout=10)

    def fixture(self):
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic maintainer')
        self.git('config', 'user.email', 'fixture@users.noreply.github.com')
        self.git('-c', 'commit.gpgsign=false', 'commit', '--allow-empty', '-qm', 'Synthetic fixture')

    def test_help_version_and_no_automatic_skill_install(self):
        environment = dict(os.environ, HOME=str(self.root), USERPROFILE=str(self.root))
        result = self.command('--help', env=environment)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('install-skill', result.stdout)
        self.assertEqual(self.command('--version').stdout.strip(), '0.2.0')
        self.assertFalse((self.root / '.agents').exists())

    def test_clean_history_outside_checkout(self):
        self.fixture()
        result = self.command('audit', self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['complete'])

    def test_findings_return_failure_without_printing_value(self):
        self.fixture()
        candidate = 'gh' + 'p_' + 'X' * 40
        (self.root / 'removed.txt').write_text(candidate)
        self.git('add', '.')
        self.git('-c', 'commit.gpgsign=false', 'commit', '-qm', 'Synthetic history')
        result = self.command('audit', self.root)
        self.assertEqual(result.returncode, 1)
        self.assertTrue(json.loads(result.stdout)['findings'])
        self.assertNotIn(candidate, result.stdout + result.stderr)

    def test_missing_repository_and_nested_folder_are_incomplete(self):
        self.fixture()
        nested = self.root / 'exported'
        nested.mkdir()
        for target in [self.root / 'missing', nested]:
            with self.subTest(target=target.name):
                result = self.command('audit', target)
                self.assertEqual(result.returncode, 1)
                self.assertFalse(json.loads(result.stdout)['complete'])

    def test_missing_git_is_incomplete(self):
        result = self.command('audit', self.root, env=dict(os.environ, PATH=''))
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)['complete'])

    def test_invalid_arguments_never_report_success(self):
        cases = [[], ['audit'], ['install-skill'], ['unknown']]
        cases += [['audit', str(self.root), '--seconds', limit]
                  for limit in ['0', '-1', '3601', 'nan', '1.5']]
        cases += [['install-skill', '--user', '--destination', str(self.root / 'new')]]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(self.command(*args).returncode, 2)

    def test_install_copies_complete_standalone_skill_and_refuses_replacement(self):
        target = self.root / 'مهارة release'
        result = self.command('install-skill', '--destination', target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((target / 'SKILL.md').is_file())
        self.assertTrue((target / 'references/skill-packages.md').is_file())
        self.fixture()
        audit = subprocess.run([sys.executable, str(target / 'scripts/audit_history.py'),
                                str(self.root)], cwd=self.root, capture_output=True,
                               text=True, timeout=20)
        self.assertEqual(audit.returncode, 0, audit.stderr)
        before = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
        result = self.command('install-skill', '--destination', target)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(before, {p.relative_to(target): p.read_bytes()
                                 for p in target.rglob('*') if p.is_file()})

    def test_user_install_uses_explicit_temporary_home(self):
        environment = dict(os.environ, HOME=str(self.root), USERPROFILE=str(self.root))
        result = self.command('install-skill', '--user', env=environment)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / '.agents/skills/public-repo-release/SKILL.md').is_file())
