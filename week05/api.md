# API contract — KitchenOps

| Method | Path | Request | Response | Errors | REQ |
|---|---|---|---|---|---|
| GET | /health | — | 200 {"status": "ok"} | — | — |
| POST | /auth/code | {"email": "chef@kitchenops.internal"} | 200 {"sent": true} | 422 invalid email format · 429 code requested less than one minute ago | REQ-001 |
| POST | /auth/token | {"email": "chef@kitchenops.internal", "code": "1234"} | 200 {"token": "kops_session_token_xyz", "token_type": "bearer"} | 401 wrong or expired code · 422 missing field or invalid format | REQ-001 |
| GET | /auth/me | Header: Authorization: Bearer <token> | 200 {"email": "chef@kitchenops.internal", "role": "chef"} | 401 missing or invalid session token | REQ-001 |
| POST | /prep/portions | {"recipe_id": "rigatoni_pomodoro", "portions": 10} | 200 {"success": true, "recipe_id": "rigatoni_pomodoro", "portions": 10, "audit_log_id": "TX-9042"} | 401 missing or invalid session token · 404 recipe not found · 409 insufficient stock · 422 portions must be positive integer | REQ-002 |
| GET | /inventory/levels | Header: Authorization: Bearer <token> | 200 {"items": {"pasta": 50.0, "tomato_sauce": 30.0}, "total_ingredients": 2} | 401 missing or invalid session token | REQ-002 |
| GET | /orders/replenish | Header: Authorization: Bearer <token> | 200 {"orders": [{"po_id": "PO-2026-041", "ingredient": "cooking_cream", "current_stock": 3.5, "threshold": 5.0, "order_amount": 20.0, "unit": "L", "status": "draft"}], "total_orders": 1} | 401 missing or invalid session token | REQ-003 |
| POST | /orders/dispatch | {"po_id": "PO-2026-041"} | 200 {"success": true, "po_id": "PO-2026-041", "status": "dispatched", "dispatched_by": "chef@kitchenops.internal"} | 401 missing or invalid session token · 404 purchase order not found · 409 purchase order already dispatched · 422 missing po_id | REQ-003 |


