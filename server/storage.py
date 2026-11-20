"""server/storage.py: file-backed JSON database persistence for KitchenOps server state (§5.2).

Ensures that ingredient stock levels, purchase orders and chat quotas survive server restarts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_FILE = DATA_DIR / "kitchenops_db.json"

DEFAULT_INVENTORY: dict[str, float] = {
    "pasta": 50.0,
    "tomato_sauce": 30.0,
    "cooking_cream": 3.5,
}

DEFAULT_PURCHASE_ORDERS: dict[str, dict[str, Any]] = {
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


def _ensure_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_db() -> dict[str, Any]:
    """Load persistent kitchen state from disk or initialize with baseline defaults."""
    _ensure_dir()
    if not DB_FILE.is_file():
        state = {
            "inventory": dict(DEFAULT_INVENTORY),
            "purchase_orders": dict(DEFAULT_PURCHASE_ORDERS),
            "user_message_counts": {},
        }
        save_db(state)
        return state

    try:
        content = DB_FILE.read_text(encoding="utf-8")
        data = json.loads(content)
        if not isinstance(data, dict):
            raise ValueError("Corrupted database format")
        if "inventory" not in data or not isinstance(data["inventory"], dict):
            data["inventory"] = dict(DEFAULT_INVENTORY)
        if "purchase_orders" not in data or not isinstance(data["purchase_orders"], dict):
            data["purchase_orders"] = dict(DEFAULT_PURCHASE_ORDERS)
        if "user_message_counts" not in data or not isinstance(data["user_message_counts"], dict):
            data["user_message_counts"] = {}
        return data
    except Exception:
        state = {
            "inventory": dict(DEFAULT_INVENTORY),
            "purchase_orders": dict(DEFAULT_PURCHASE_ORDERS),
            "user_message_counts": {},
        }
        save_db(state)
        return state


def save_db(data: dict[str, Any]) -> None:
    """Atomically write persistent database state to disk."""
    _ensure_dir()
    temp_file = DB_FILE.with_suffix(".tmp")
    payload = json.dumps(data, indent=2, ensure_ascii=False)
    temp_file.write_text(payload, encoding="utf-8")
    temp_file.replace(DB_FILE)


def save_state(
    inventory: dict[str, float] | None = None,
    purchase_orders: dict[str, dict[str, Any]] | None = None,
    user_message_counts: dict[str, int] | None = None,
) -> None:
    """Save updated server state to persistent disk storage."""
    current = load_db()
    if inventory is not None:
        current["inventory"] = inventory
    if purchase_orders is not None:
        current["purchase_orders"] = purchase_orders
    if user_message_counts is not None:
        current["user_message_counts"] = user_message_counts
    save_db(current)
