"""server/tests/test_chat.py: tests for REQ-009 AI kitchen assistant chatbot route."""

from unittest.mock import patch
from urllib.error import URLError

from fastapi.testclient import TestClient

from server.chat import DAILY_QUOTA, USER_MESSAGE_COUNTS
from server.course_login import current_user
from server.main import app

client = TestClient(app)


def test_tc_009_01_chat_unauthenticated_returns_401():
    """Unauthenticated request to POST /chat must return HTTP 401 Unauthorized."""
    app.dependency_overrides.clear()
    response = client.post("/chat", json={"message": "What is our stock?"})
    assert response.status_code == 401


def test_tc_009_02_chat_authenticated_responds_with_quota():
    """Authenticated request returns HTTP 200 with AI reply and decremented quota."""
    test_user = "chef_test_01@kitchenops.internal"
    USER_MESSAGE_COUNTS[test_user] = 0
    app.dependency_overrides[current_user] = lambda: test_user

    try:
        response = client.post(
            "/chat",
            json={"message": "Which ingredients are currently low?"},
            headers={"Authorization": "Bearer valid_token"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "reply" in data
        assert "cooking_cream" in data["reply"] or "safety buffer" in data["reply"]
        assert data["remaining_quota"] == DAILY_QUOTA - 1
    finally:
        app.dependency_overrides.clear()


def test_tc_009_03_chat_daily_quota_exceeded_returns_429():
    """Exceeding the daily quota of 20 messages must return HTTP 429 Too Many Requests."""
    test_user = "chef_rate_limit@kitchenops.internal"
    USER_MESSAGE_COUNTS[test_user] = DAILY_QUOTA
    app.dependency_overrides[current_user] = lambda: test_user

    try:
        response = client.post(
            "/chat",
            json={"message": "Another message beyond daily limit"},
            headers={"Authorization": "Bearer valid_token"},
        )
        assert response.status_code == 429
        assert "quota" in response.json()["detail"].lower()
    finally:
        app.dependency_overrides.clear()


def test_tc_009_04_chat_service_failure_returns_503():
    """Simulated LLM API network/timeout failure must return HTTP 503 without crashing server."""
    test_user = "chef_error_test@kitchenops.internal"
    USER_MESSAGE_COUNTS[test_user] = 0
    app.dependency_overrides[current_user] = lambda: test_user

    with patch.dict("os.environ", {"LLM_API_KEY": "real-api-key-test"}):
        with patch("urllib.request.urlopen", side_effect=URLError("Connection timed out")):
            try:
                response = client.post(
                    "/chat",
                    json={"message": "Test error handling"},
                    headers={"Authorization": "Bearer valid_token"},
                )
                assert response.status_code == 503
                assert "503" in str(response.status_code)
            finally:
                app.dependency_overrides.clear()
