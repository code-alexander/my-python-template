"""Tests for the template."""

from collections.abc import Generator
from pathlib import Path

import copier


def test_folders(delete_temp_dir: Generator[None, None, None]) -> None:
    """Test that the directory structure is created correctly.

    Args:
        delete_temp_dir (Generator[None, None, None]):
            pytest fixture to delete the `tests/temp/` directory,
            before and after a test.
    """
    copier.run_copy(
        src_path='.',
        dst_path='tests/temp/',
        data={
            'project_name': 'Test Project',
            'distribution_name': 'test-project',
            'import_name': 'test_project',
            'project_description': '`Test Project` is a Python package 🚀',
        },
    )
    assert Path('tests/temp/src/test_project/__init__.py').is_file(), '`src/test_project/__init__.py` file not found'
    assert Path('tests/temp/src/test_project/py.typed').is_file(), '`src/test_project/py.typed` PEP-561 file not found'
    assert Path('tests/temp/tests').is_dir(), '`tests` folder not found'
    assert Path('tests/temp/.github/workflows/ci.yaml').is_file(), '`.github/workflows/ci.yaml` file not found'
    assert Path('tests/temp/.pre-commit-config.yaml').is_file(), '`.pre-commit-config.yaml` file not found'
    assert Path('tests/temp/README.md').is_file(), '`README.md` file not found'
    assert Path('tests/temp/pyproject.toml').is_file(), '`pyproject.toml` file not found'
    assert Path('tests/temp/.copier-answers.yml').is_file(), '`.copier-answers.yml` file not found'
    assert not Path('tests/temp/__init__.py').exists(), '`__init__.py` file should not be copied to the root dir'
