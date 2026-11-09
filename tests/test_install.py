"""Preserve existing state and show installation failures instead of success."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from public_repo_release.install import RESOURCE_FILES, install_skill


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.target = self.root / 'skill'

    def assert_no_staging(self):
        self.assertEqual(list(self.root.glob('.public-repo-release-*')), [])

    def test_existing_file_and_directory_are_unchanged(self):
        for kind in ['file', 'directory']:
            target = self.root / kind
            if kind == 'file':
                target.write_text('original')
            else:
                target.mkdir()
                (target / 'original.txt').write_text('original')
            with self.assertRaises(FileExistsError):
                install_skill(target)
            saved = target if kind == 'file' else target / 'original.txt'
            self.assertEqual(saved.read_text(), 'original')
        self.assert_no_staging()

    def test_existing_and_dangling_links_are_preserved(self):
        original = self.root / 'original'
        original.mkdir()
        for destination in [original, self.root / 'missing']:
            link = self.root / ('link-' + destination.name)
            try:
                link.symlink_to(destination, target_is_directory=True)
            except OSError:
                self.skipTest('Creating symlinks is unavailable on this platform')
            with self.assertRaises(FileExistsError):
                install_skill(link)
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.readlink(), destination)
        self.assertEqual(list(original.iterdir()), [])
        self.assert_no_staging()

    def test_missing_resource_leaves_no_claimed_destination(self):
        with patch('public_repo_release.install.RESOURCE_FILES', ('absent-resource.md',)):
            with self.assertRaises(FileNotFoundError):
                install_skill(self.target)
        self.assertFalse(self.target.exists())
        self.assert_no_staging()

    def test_write_failure_retains_partial_folder_and_cleans_stage(self):
        with patch('public_repo_release.install.shutil.copyfile', side_effect=OSError):
            with self.assertRaises(OSError):
                install_skill(self.target)
        self.assertTrue(self.target.is_dir())
        with self.assertRaises(FileExistsError):
            install_skill(self.target)
        self.assert_no_staging()

    def test_cancelled_copy_cleans_stage_and_retains_partial_folder(self):
        with patch('public_repo_release.install.shutil.copyfile', side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                install_skill(self.target)
        self.assertTrue(self.target.is_dir())
        self.assert_no_staging()

    def test_complete_resource_inventory_has_no_cache_or_extra_files(self):
        install_skill(self.target)
        actual = {p.relative_to(self.target).as_posix() for p in self.target.rglob('*') if p.is_file()}
        self.assertEqual(actual, set(RESOURCE_FILES))
        self.assert_no_staging()
