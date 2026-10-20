"""An example test. Your login tests go into test_login.py, one test for each test case,
named by its id: test_TC_001_01_..., test_TC_001_02_..."""

from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_health_answers_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
