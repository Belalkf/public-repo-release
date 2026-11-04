import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/public-repo-release/scripts/audit_history.py'
spec = importlib.util.spec_from_file_location('history_audit', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HistoryAuditTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic maintainer')
        self.git('config', 'user.email', 'fixture@users.noreply.github.com')

    def git(self, *arguments):
        return subprocess.run(['git', '-C', str(self.root), *arguments],
                              capture_output=True, check=True, timeout=10)

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'Synthetic fixture')

    def test_clean_history_is_read_only_and_complete(self):
        (self.root / 'file.txt').write_text('synthetic text\n')
        self.commit()
        index = (self.root / '.git/index').read_bytes()
        result = module.audit(self.root)
        self.assertTrue(result['complete'])
        self.assertEqual(result['commits'], 1)
        self.assertEqual(result['findings'], [])
        self.assertEqual((self.root / '.git/index').read_bytes(), index)

    def test_deleted_secret_is_found_without_echoing_its_value(self):
        secret = 'gh' + 'p_' + 'A' * 40
        path = self.root / 'removed.txt'
        path.write_text(secret)
        self.commit()
        path.unlink()
        self.commit()
        result = module.audit(self.root)
        self.assertTrue(any(item['kind'] == 'github-token' for item in result['findings']))
        self.assertNotIn(secret, json.dumps(result))
        self.assertEqual(result['commits'], 2)

    def test_inherited_git_redirects_do_not_switch_the_repository(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        with patch.dict(os.environ, {'GIT_DIR': '/invalid/history-audit'}):
            self.assertTrue(module.audit(self.root)['complete'])

    def test_limits_do_not_claim_complete_coverage(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        for options in [{'seconds': 0}, {'max_objects': 0}, {'max_bytes': 1}, {'total_bytes': 1}]:
            with self.subTest(options=options):
                self.assertFalse(module.audit(self.root, **options)['complete'])

    def test_binary_is_explicitly_unreviewed(self):
        (self.root / 'image.bin').write_bytes(b'\x00\xff')
        self.commit()
        result = module.audit(self.root)
        self.assertFalse(result['complete'])
        self.assertTrue(result['unreviewed'])

    def test_empty_history_and_invalid_repository_are_not_clean_results(self):
        self.assertFalse(module.audit(self.root)['complete'])
        with tempfile.TemporaryDirectory() as other:
            self.assertFalse(module.audit(Path(other))['complete'])

    def test_annotated_tag_messages_are_inspected(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        secret = 'gh' + 'p_' + 'B' * 40
        self.git('tag', '-a', 'synthetic-tag', '-m', secret)
        result = module.audit(self.root)
        self.assertTrue(any(item['kind'] == 'github-token' for item in result['findings']))
        self.assertNotIn(secret, json.dumps(result))

    def test_shallow_clone_does_not_claim_complete_history(self):
        (self.root / 'file.txt').write_text('first')
        self.commit()
        (self.root / 'file.txt').write_text('second')
        self.commit()
        with tempfile.TemporaryDirectory() as other:
            target = Path(other) / 'shallow'
            subprocess.run(['git', 'clone', '-q', '--depth=1', self.root.as_uri(), str(target)],
                           capture_output=True, check=True, timeout=10)
            result = module.audit(target)
        self.assertFalse(result['complete'])
        self.assertTrue(any('Shallow' in issue for issue in result['issues']))

    def test_replace_ref_cannot_hide_original_secret(self):
        secret = 'gh' + 'p_' + 'C' * 40
        (self.root / 'file.txt').write_text(secret)
        self.commit()
        original = self.git('rev-parse', 'HEAD:file.txt').stdout.strip().decode()
        replacement = subprocess.run(['git', '-C', str(self.root), 'hash-object', '-w', '--stdin'],
                                     input=b'safe replacement', capture_output=True, check=True,
                                     timeout=10).stdout.strip().decode()
        self.git('replace', original, replacement)
        result = module.audit(self.root)
        self.assertTrue(any(item['object'] == original and item['kind'] == 'github-token'
                            for item in result['findings']))
        self.assertNotIn(secret, json.dumps(result))
