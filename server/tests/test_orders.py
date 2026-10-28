"""server/tests/test_orders.py: tests for REQ-003 automated threshold replenishment (TC-003-01, TC-003-02)."""

from fastapi.testclient import TestClient

from server.course_login import current_user
from server.main import app
from server.orders import PURCHASE_ORDERS
from server.prep import INVENTORY

client = TestClient(app)


def test_TC_003_01_stock_below_threshold_generates_supplier_po():
    """TC-003-01: Stock dropping below safety threshold generates automated supplier PO."""
    # Reset inventory: cooking cream at 3.5L (< 5.0L threshold)
    INVENTORY["cooking_cream"] = 3.5

    # Reset draft purchase order
    PURCHASE_ORDERS["PO-2026-041"] = {
        "po_id": "PO-2026-041",
        "ingredient": "cooking_cream",
        "ingredient_name": "Cooking Cream 35%",
        "current_stock": 3.5,
        "threshold": 5.0,
        "order_amount": 20.0,
        "unit": "L",
        "supplier": "Metro Food Wholesale Ltd.",
        "status": "draft",
    }

    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        # Step 1: Query replenishment drafts
        get_res = client.get(
            "/orders/replenish",
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert get_res.status_code == 200
        data = get_res.json()
        assert data["total_orders"] >= 1
        po = next(o for o in data["orders"] if o["po_id"] == "PO-2026-041")
        assert po["ingredient"] == "cooking_cream"
        assert po["current_stock"] == 3.5
        assert po["threshold"] == 5.0
        assert po["order_amount"] == 20.0
        assert po["status"] == "draft"

        # Step 2: Dispatch purchase order
        dispatch_res = client.post(
            "/orders/dispatch",
            json={"po_id": "PO-2026-041"},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert dispatch_res.status_code == 200
        dispatched = dispatch_res.json()
        assert dispatched["success"] is True
        assert dispatched["po_id"] == "PO-2026-041"
        assert dispatched["status"] == "dispatched"
        assert dispatched["dispatched_by"] == "chef@kitchenops.internal"
        assert dispatched["order_amount"] == 20.0
    finally:
        app.dependency_overrides.clear()


def test_TC_003_01_unauthenticated_order_endpoints_refused():
    """TC-003-01: Unauthorized access to orders is rejected with 401."""
    app.dependency_overrides.clear()
    assert client.get("/orders/replenish").status_code == 401
    assert client.post("/orders/dispatch", json={"po_id": "PO-2026-041"}).status_code == 401


def test_TC_003_01_dispatch_unknown_po_refused():
    """TC-003-01: Dispatching an unrecognized PO ID is rejected with 404."""
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        res = client.post(
            "/orders/dispatch",
            json={"po_id": "PO-NONEXISTENT"},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert res.status_code == 404
    finally:
        app.dependency_overrides.clear()


def test_TC_003_01_dispatch_already_dispatched_po_refused():
    """TC-003-01: Dispatching an already-dispatched order is rejected with 409 Conflict."""
    PURCHASE_ORDERS["PO-2026-041"] = {
        "po_id": "PO-2026-041",
        "ingredient": "cooking_cream",
        "ingredient_name": "Cooking Cream 35%",
        "current_stock": 3.5,
        "threshold": 5.0,
        "order_amount": 20.0,
        "unit": "L",
        "supplier": "Metro Food Wholesale Ltd.",
        "status": "dispatched",
    }
    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        res = client.post(
            "/orders/dispatch",
            json={"po_id": "PO-2026-041"},
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert res.status_code == 409
    finally:
        app.dependency_overrides.clear()


def test_TC_003_02_stock_above_threshold_does_not_trigger_unneeded_po():
    """TC-003-02: Stock above safety threshold does not trigger unneeded purchase order."""
    # Pasta inventory is healthy at 13.3 kg (> 5.0 kg threshold)
    INVENTORY["pasta"] = 13.3

    # Clean pasta orders from draft list
    if "PO-AUTO-pasta" in PURCHASE_ORDERS:
        del PURCHASE_ORDERS["PO-AUTO-pasta"]

    app.dependency_overrides[current_user] = lambda: "chef@kitchenops.internal"
    try:
        res = client.get(
            "/orders/replenish",
            headers={"Authorization": "Bearer test_valid_token"},
        )
        assert res.status_code == 200
        data = res.json()
        pasta_pos = [o for o in data["orders"] if o.get("ingredient") == "pasta"]
        # No automated replenishment order draft should exist for pasta
        assert len(pasta_pos) == 0
    finally:
        app.dependency_overrides.clear()
