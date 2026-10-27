import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


@pytest.fixture(autouse=True)
def setup_test_code_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    from server.course_login import reset_for_tests

    reset_for_tests()
    code_path = tmp_path / "test_login_code.txt"
    monkeypatch.setenv("AIASD_CODE_FILE", str(code_path))
    return code_path
