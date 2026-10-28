"""server/tests/test_login.py: tests for REQ-001 login contract using course_login."""

from fastapi.testclient import TestClient

from server.course_login import reset_for_tests
from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email(monkeypatch, tmp_path):
    """TC-001-01: Log in with the 4-digit code sent to e-mail."""
    reset_for_tests()
    code_path = tmp_path / "code.txt"
    monkeypatch.setenv("AIASD_CODE_FILE", str(code_path))

    response = client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}
    assert code_path.read_text(encoding="utf-8").strip().isdigit()


def test_TC_001_02_wrong_login_code_is_refused(monkeypatch, tmp_path):
    """TC-001-02: A wrong login code is refused with an error message."""
    reset_for_tests()
    code_path = tmp_path / "code.txt"
    monkeypatch.setenv("AIASD_CODE_FILE", str(code_path))

    client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
    response = client.post(
        "/auth/token",
        json={"email": "chef@kitchenops.internal", "code": "0000"},
    )
    assert response.status_code == 401


def test_TC_001_03_expired_login_code_is_refused():
    """TC-001-03: An expired or non-existent login code is refused with HTTP 401."""
    reset_for_tests()
    response = client.post(
        "/auth/token",
        json={"email": "chef@kitchenops.internal", "code": "1234"},
    )
    assert response.status_code == 401


def test_TC_001_04_invalid_email_format_is_refused():
    """TC-001-04: An invalid email address format is refused with a 422 error."""
    reset_for_tests()
    response = client.post(
        "/auth/code",
        json={"email": "invalid-email-format"},
    )
    assert response.status_code == 422


def test_TC_001_05_second_code_request_too_soon_is_refused(monkeypatch, tmp_path):
    """TC-001-05: Requesting a second login code within 60 seconds is refused with 429."""
    reset_for_tests()
    monkeypatch.setenv("AIASD_CODE_FILE", str(tmp_path / "code.txt"))

    first = client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
    assert first.status_code == 200

    second = client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
    assert second.status_code == 429


def test_TC_001_06_unauthenticated_user_cannot_access_profile():
    """TC-001-06: Querying current session profile returns 401 when unauthorized."""
    reset_for_tests()
    response = client.get("/auth/me")
    assert response.status_code == 401
