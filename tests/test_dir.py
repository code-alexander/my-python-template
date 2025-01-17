import copier
from pathlib import Path


def test_folders(delete_temp_dir):
    copier.run_copy(
        src_path="src/my_python_template/",
        dst_path="tests/temp/",
        data={
            "project_name": "Test Project",
            "distribution_name": "test-project",
            "import_name": "test_project",
            "project_description": "`Test Project` is a Python package 🚀",
        },
    )
    assert Path("tests/temp/src/test_project").is_dir()
    assert Path("tests/temp/tests").is_dir()
