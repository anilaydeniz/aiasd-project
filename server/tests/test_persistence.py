"""server/tests/test_persistence.py: tests for server data persistence across restarts (§5.2)."""

from fastapi.testclient import TestClient

from server.course_login import current_user
from server.main import app
from server.orders import PURCHASE_ORDERS
from server.prep import INVENTORY
from server.storage import DB_FILE, load_db, save_state

client = TestClient(app)


def test_prep_stock_depletion_persists_to_disk():
    """Verify that dish portion preparation deducts stock and persists to kitchenops_db.json."""
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"

    # Reset baseline inventory to known state
    INVENTORY["pasta"] = 50.0
    INVENTORY["tomato_sauce"] = 30.0
    save_state(inventory=INVENTORY)

    try:
        response = client.post(
            "/prep/portions",
            json={"recipe_id": "rigatoni_pomodoro", "portions": 5},
            headers={"Authorization": "Bearer test_token"},
        )
        assert response.status_code == 200

        # Check in-memory stock: 5 * 120g = 0.6kg pasta depleted -> 49.4kg
        assert INVENTORY["pasta"] == 49.4

        # Verify disk persistence across simulated restart
        reloaded = load_db()
        assert reloaded["inventory"]["pasta"] == 49.4
        assert reloaded["inventory"]["tomato_sauce"] == 29.6
    finally:
        # Reset inventory
        INVENTORY["pasta"] = 50.0
        INVENTORY["tomato_sauce"] = 30.0
        save_state(inventory=INVENTORY)
        app.dependency_overrides.clear()


def test_purchase_order_dispatch_persists_to_disk():
    """Verify that purchase order dispatch updates order status and persists to disk."""
    app.dependency_overrides[current_user] = lambda: "manager@kitchenops.internal"

    PURCHASE_ORDERS["PO-2026-041"]["status"] = "draft"
    save_state(purchase_orders=PURCHASE_ORDERS)

    try:
        response = client.post(
            "/orders/dispatch",
            json={"po_id": "PO-2026-041"},
            headers={"Authorization": "Bearer test_token"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == "dispatched"

        # Verify disk persistence across simulated restart
        reloaded = load_db()
        assert reloaded["purchase_orders"]["PO-2026-041"]["status"] == "dispatched"
        assert (
            reloaded["purchase_orders"]["PO-2026-041"]["dispatched_by"]
            == "manager@kitchenops.internal"
        )
    finally:
        PURCHASE_ORDERS["PO-2026-041"]["status"] = "draft"
        save_state(purchase_orders=PURCHASE_ORDERS)
        app.dependency_overrides.clear()


def test_database_file_exists():
    """Verify that the database file exists in server/data/kitchenops_db.json."""
    assert DB_FILE.is_file()
