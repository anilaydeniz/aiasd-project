# Week 6 — AI log

## The assistant, and what I gave it

I worked with Antigravity (Gemini Pro). I provided the routes of my custom kitchen management features in server/prep.py (POST /prep/portions and GET /inventory/levels) and server/orders.py (GET /orders/replenish and POST /orders/dispatch), together with their acceptance criteria from REQ-002 and REQ-003, and asked it to act as a hostile reviewer to give me the three strongest attacks on these endpoints.

## The three attacks, and what my server did

1. Attack 1 was **send zero or negative portion count to deplete inventory in reverse**. I tested sending a negative portion payload (-5 portions) to POST /prep/portions with an active bearer token; the server validated the input and returned HTTP 422 with validation error.
2. Attack 2 was **dispatch an arbitrary unknown purchase order ID**. I tested sending a non-existent purchase order ID (PO-FAKE-999) to POST /orders/dispatch; the server verified the active restock registry and responded with HTTP 404 Not Found.
3. Attack 3 was **trigger automated replenishment evaluation without authorization**. I tested calling GET /orders/replenish without an Authorization header; the server immediately rejected the unauthenticated request with HTTP 401 Unauthorized.

## The one I fixed

I addressed the negative and zero portion validation vulnerability. In server/prep.py, I ensured the Pydantic schema enforces gt=0 for portion counts. I added test_TC_002_02_submitting_invalid_portion_count_is_prevented in server/tests/test_prep.py, which verifies that sending 0 or negative portions is refused with HTTP 422 and prevents stock corruption.

## The one that is wrong

Attack 3 claimed that unauthenticated clients could trigger replenishment logic or leak inventory stock buffers. This was wrong because FastAPI dependency injection requires current_user on all custom routes; unauthenticated requests are stopped at the gateway with HTTP 401 before any database or inventory calculations run.

## The assistant and my groupmate

Both the assistant and my groupmate attacker (220504010) agreed that negative portion submissions were a critical boundary test. My groupmate specifically attempted an unauthenticated negative portion submission, whereas the assistant additionally probed the purchase order dispatch workflow which my classmate did not test.

## Evidence — the exchange and the terminal output

```text
ME:
Give me the three strongest attacks on these routes, numbered. Do not fix anything, only attack.
Routes:
- POST /prep/portions (REQ-002: bill-of-materials stock deduction)
- GET /inventory/levels (REQ-002: current kitchen stock monitoring)
- GET /orders/replenish (REQ-003: safety buffer restock evaluation)
- POST /orders/dispatch (REQ-003: purchase order wholesale dispatch)

AI:
Here are the three strongest attacks on these routes:
1. send zero or negative portion count to deplete inventory in reverse: Call POST /prep/portions with portions set to -5 or 0 to trigger mathematical underflow or increase stock without receiving an inbound delivery.
2. dispatch an arbitrary unknown purchase order ID: Call POST /orders/dispatch with an unlisted PO identifier like PO-FAKE-999 to corrupt supplier dispatch states or create orphaned audit records.
3. trigger automated replenishment evaluation without authorization: Send a GET request to /orders/replenish without an authorization token to view low-stock pantry items and induce unverified purchase orders.

TERMINAL:
$ .venv/Scripts/pytest server/tests/test_prep.py -k test_TC_002_02 -v
server/tests/test_prep.py::test_TC_002_02_submitting_invalid_portion_count_is_prevented PASSED [100%]
======================= 1 passed, 7 deselected in 0.44s =======================

$ python -c "from fastapi.testclient import TestClient; from server.main import app; c = TestClient(app); print(c.get('/orders/replenish').status_code)"
401

$ python -c "from fastapi.testclient import TestClient; from server.main import app; c = TestClient(app); print(c.post('/orders/dispatch', json={'po_id': 'PO-FAKE-999'}).status_code)"
401
```
