import shutil
import pytest


@pytest.fixture
def delete_temp_dir():
    print("Deleting `tests/temp/`")
    shutil.rmtree("tests/temp/", ignore_errors=True)
    yield
    print("Deleting `tests/temp/`")
    # shutil.rmtree("tests/temp/", ignore_errors=True)
