from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email():
    response = client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}


def test_TC_001_02_wrong_login_code_is_refused():
    response = client.post(
        "/auth/token",
        json={"email": "chef@kitchenops.internal", "code": "0000"},
    )
    assert response.status_code == 401


def test_TC_001_03_expired_login_code_is_refused():
    response = client.post(
        "/auth/token",
        json={"email": "chef@kitchenops.internal", "code": "1234"},
    )
    assert response.status_code == 401
