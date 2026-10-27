"""server/tests/test_prep.py: tests for REQ-002 dish portion prep and stock depletion."""

from fastapi.testclient import TestClient

from server.course_login import current_user
from server.main import app
from server.prep import INVENTORY

client = TestClient(app)


def test_TC_002_01_log_prep_portions_depletes_stock():
    """TC-002-01: Log 10 portions of Rigatoni Pomodoro to deplete raw ingredients."""
    # Reset baseline inventory
    INVENTORY["pasta"] = 50.0
    INVENTORY["tomato_sauce"] = 30.0

    # Override authentication for testing authenticated user
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"

    try:
        response = client.post(
            "/prep/portions",
            json={"recipe_id": "rigatoni_pomodoro", "portions": 10},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["recipe_id"] == "rigatoni_pomodoro"
        assert data["portions"] == 10
        assert data["audit_log_id"] == "TX-9042"

        # Verify stock depletion: 10 * 120g = 1.2kg pasta, 10 * 80g = 0.8kg sauce
        assert INVENTORY["pasta"] == 48.8
        assert INVENTORY["tomato_sauce"] == 29.2
    finally:
        app.dependency_overrides.clear()


def test_TC_002_01_unauthenticated_prep_is_refused():
    """TC-002-01: Unauthorized request without bearer token is rejected with 401."""
    app.dependency_overrides.clear()
    response = client.post(
        "/prep/portions",
        json={"recipe_id": "rigatoni_pomodoro", "portions": 10},
    )
    assert response.status_code == 401
