"""pytest fixtures for `my-python-template`."""

import shutil
from collections.abc import Generator

import pytest


@pytest.fixture
def delete_temp_dir() -> Generator[None, None, None]:
    """Fixture to delete the `tests/temp/` directory, before and after a test.

    Yields:
        Generator[None, None, None]: pytest fixture.
    """
    shutil.rmtree('tests/temp/', ignore_errors=True)
    yield None
    # shutil.rmtree('tests/temp/', ignore_errors=True)
