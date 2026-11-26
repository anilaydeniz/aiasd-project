"""server/tests/test_chat.py: tests for REQ-009 AI kitchen assistant and REQ-010 content report."""

from fastapi import HTTPException
from fastapi.testclient import TestClient

from server.chat import DAILY_QUOTA, USER_MESSAGE_COUNTS
from server.course_login import auth_header_for_tests
from server.main import app

client = TestClient(app)


def test_TC_009_02_the_chatbot_answers(monkeypatch):
    """TC-009-02: verify chatbot responds to authenticated user with mock model (§5.3)."""
    monkeypatch.setattr(
        "server.chat.ask_model",
        lambda prompt: "Rigatoni Pomodoro takes 120g pasta and 80g sauce.",
    )
    headers = auth_header_for_tests(client, "chef_chat02@example.edu.tr")
    r = client.post(
        "/chat",
        json={"message": "When is my next booking?"},
        headers=headers,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["answer"] == "Rigatoni Pomodoro takes 120g pasta and 80g sauce."
    assert "reply" in data
    assert "remaining_quota" in data


def test_TC_009_03_without_token_the_answer_is_401():
    """TC-009-03: verify unauthenticated request without token returns HTTP 401 (§5.3)."""
    r = client.post("/chat", json={"message": "Hello without token"})
    assert r.status_code == 401


def test_TC_009_04_after_the_daily_limit_the_answer_is_429():
    """TC-009-04: verify exceeding the daily limit of 20 messages returns HTTP 429 (§5.3)."""
    email = "chef_quota_04@example.edu.tr"
    headers = auth_header_for_tests(client, email)
    USER_MESSAGE_COUNTS[email] = DAILY_QUOTA

    r = client.post(
        "/chat",
        json={"message": "Another message after daily limit"},
        headers=headers,
    )
    assert r.status_code == 429
    assert "quota" in r.json()["detail"].lower()


def test_TC_009_05_when_the_llm_api_fails_the_answer_is_503(monkeypatch):
    """TC-009-05: verify LLM API failure returns HTTP 503 cleanly without crashing (§5.3)."""

    def _failing_ask(prompt):
        raise HTTPException(
            status_code=503,
            detail="LLM service unavailable or timed out within 20 seconds",
        )

    monkeypatch.setattr("server.chat.ask_model", _failing_ask)
    headers = auth_header_for_tests(client, "chef_fail_05@example.edu.tr")
    r = client.post("/chat", json={"message": "Test fail"}, headers=headers)
    assert r.status_code == 503
    assert "503" in str(r.status_code)


def test_TC_010_01_report_ai_answer():
    """TC-010-01: verify POST /chat/report persists user report of AI answer (§5.4)."""
    # Without token -> 401
    r_unauth = client.post("/chat/report", json={"answer": "Inaccurate info", "reason": "wrong"})
    assert r_unauth.status_code == 401

    # With valid token -> 200
    headers = auth_header_for_tests(client, "chef_report_01@example.edu.tr")
    r = client.post(
        "/chat/report",
        json={
            "answer": "Rigatoni recipe contains nuts",
            "reason": "inaccurate allergen info",
        },
        headers=headers,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "reported"
    assert "report_id" in data
