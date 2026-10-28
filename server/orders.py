"""server/orders.py: safety threshold monitoring and purchase order replenishment (REQ-003)."""

from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel, Field

from server.course_login import current_user
from server.prep import INVENTORY

router = APIRouter()

# Ingredient safety thresholds (REQ-003)
THRESHOLDS: dict[str, dict] = {
    "cooking_cream": {
        "name": "Cooking Cream 35%",
        "safety_threshold": 5.0,
        "reorder_amount": 20.0,
        "unit": "L",
        "supplier": "Metro Food Wholesale Ltd.",
    },
    "pasta": {
        "name": "Pasta (Rigatoni)",
        "safety_threshold": 5.0,
        "reorder_amount": 20.0,
        "unit": "kg",
        "supplier": "Metro Food Wholesale Ltd.",
    },
    "tomato_sauce": {
        "name": "Tomato Sauce Base",
        "safety_threshold": 4.0,
        "reorder_amount": 10.0,
        "unit": "kg",
        "supplier": "Metro Food Wholesale Ltd.",
    },
}

# In-memory purchase orders store
PURCHASE_ORDERS: dict[str, dict] = {
    "PO-2026-041": {
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
}


class DispatchOrderRequest(BaseModel):
    po_id: str = Field(min_length=1, description="Purchase order identifier")


@router.get("/orders/replenish")
def get_replenishment_orders(user: str = Depends(current_user)) -> dict:
    """REQ-003: Evaluates stock safety buffers and returns automated replenishment purchase orders."""
    # Ensure items below safety buffer have draft purchase orders
    for item_key, cfg in THRESHOLDS.items():
        current_level = INVENTORY.get(item_key, 0.0)
        if current_level < cfg["safety_threshold"]:
            po_id = "PO-2026-041" if item_key == "cooking_cream" else f"PO-AUTO-{item_key}"
            if po_id not in PURCHASE_ORDERS:
                PURCHASE_ORDERS[po_id] = {
                    "po_id": po_id,
                    "ingredient": item_key,
                    "ingredient_name": cfg["name"],
                    "current_stock": current_level,
                    "threshold": cfg["safety_threshold"],
                    "order_amount": cfg["reorder_amount"],
                    "unit": cfg["unit"],
                    "supplier": cfg["supplier"],
                    "status": "draft",
                }
            else:
                PURCHASE_ORDERS[po_id]["current_stock"] = current_level

    orders_list = list(PURCHASE_ORDERS.values())
    return {"orders": orders_list, "total_orders": len(orders_list)}


@router.post("/orders/dispatch")
def dispatch_purchase_order(
    body: Annotated[DispatchOrderRequest, Body()], user: str = Depends(current_user)
) -> dict:
    """REQ-003: Dispatches verified replenishment purchase order to wholesale supplier."""
    po_id = body.po_id.strip()
    if po_id not in PURCHASE_ORDERS:
        raise HTTPException(status_code=404, detail="Purchase order not found")

    order = PURCHASE_ORDERS[po_id]
    if order["status"] == "dispatched":
        raise HTTPException(status_code=409, detail="Purchase order already dispatched")

    order["status"] = "dispatched"
    order["dispatched_by"] = user

    return {
        "success": True,
        "po_id": po_id,
        "status": "dispatched",
        "dispatched_by": user,
        "ingredient": order["ingredient"],
        "order_amount": order["order_amount"],
        "unit": order["unit"],
        "supplier": order["supplier"],
    }

