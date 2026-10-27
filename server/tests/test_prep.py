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


def test_TC_002_01_invalid_portion_count_is_refused():
    """TC-002-01: Portions <= 0 is refused with 422 Unprocessable Entity."""
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        response = client.post(
            "/prep/portions",
            json={"recipe_id": "rigatoni_pomodoro", "portions": 0},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert response.status_code == 422
    finally:
        app.dependency_overrides.clear()


def test_TC_002_01_unknown_recipe_is_refused():
    """TC-002-01: An unrecognized recipe ID is refused with 404 Not Found."""
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        response = client.post(
            "/prep/portions",
            json={"recipe_id": "unknown_recipe", "portions": 5},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert response.status_code == 404
    finally:
        app.dependency_overrides.clear()


def test_TC_002_01_insufficient_stock_is_refused():
    """TC-002-01: Preparation exceeding stock is refused with 409 Conflict."""
    INVENTORY["pasta"] = 1.0  # Only 1kg pasta available
    INVENTORY["tomato_sauce"] = 30.0

    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        # 10 portions requires 1.2kg pasta > 1.0kg available
        response = client.post(
            "/prep/portions",
            json={"recipe_id": "rigatoni_pomodoro", "portions": 10},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert response.status_code == 409
    finally:
        app.dependency_overrides.clear()


def test_TC_002_01_get_inventory_levels_authenticated():
    """TC-002-01: Authenticated user can query current pantry stock levels."""
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        response = client.get(
            "/inventory/levels",
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "pasta" in data["items"]
        assert "tomato_sauce" in data["items"]
    finally:
        app.dependency_overrides.clear()


def test_TC_002_01_unauthenticated_inventory_is_refused():
    """TC-002-01: Unauthorized access to inventory levels is rejected with 401."""
    app.dependency_overrides.clear()
    response = client.get("/inventory/levels")
    assert response.status_code == 401
