"""Build both archives, rebuild from source, and test an isolated wheel installation."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile
import venv
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=ROOT):
    subprocess.run(list(map(str, args)), cwd=cwd, check=True, timeout=240)


def check(output):
    output = output.resolve()
    if output.exists():
        raise SystemExit('Choose a new output directory; existing build files are preserved')
    run(sys.executable, '-m', 'build', '--outdir', output)
    wheel, = output.glob('*.whl')
    source, = output.glob('*.tar.gz')
    run(sys.executable, '-m', 'twine', 'check', wheel, source)
    with tempfile.TemporaryDirectory(prefix='public-release-check-') as folder:
        scratch = Path(folder)
        rebuilt = scratch / 'rebuilt'
        run(sys.executable, '-m', 'pip', 'wheel', '--no-deps', '--wheel-dir', rebuilt,
            source, cwd=scratch)
        rebuilt_wheel, = rebuilt.glob('*.whl')
        with zipfile.ZipFile(wheel) as original, zipfile.ZipFile(rebuilt_wheel) as other:
            names = {name for name in original.namelist() if name.startswith('public_repo_release/')}
            assert names == {name for name in other.namelist()
                             if name.startswith('public_repo_release/')}, 'Rebuilt file list differs'
            for name in names:
                assert original.read(name) == other.read(name), 'Rebuilt resource differs: ' + name
        environment = scratch / 'environment'
        venv.EnvBuilder(with_pip=True).create(environment)
        python = environment / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
        run(python, '-m', 'pip', 'install', '--no-deps', rebuilt_wheel, cwd=scratch)
        run(python, '-m', 'unittest', 'discover', '-s', ROOT / 'tests', '-v', cwd=scratch)
        command = python.with_name('public-repo-release.exe' if sys.platform == 'win32'
                                   else 'public-repo-release')
        run(command, '--version', cwd=scratch)
    print('Both archives validated; source-rebuilt wheel passed installed tests outside the checkout.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    check(parser.parse_args().output_dir)
