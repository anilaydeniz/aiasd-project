# API contract — KitchenOps

| Method | Path | Request | Response | Errors | REQ |
|---|---|---|---|---|---|
| GET | /health | — | 200 {"status": "ok"} | — | — |
| POST | /auth/code | {"email": "chef@kitchenops.internal"} | 200 {"sent": true} | 422 invalid email format · 429 code requested less than one minute ago | REQ-001 |
| POST | /auth/token | {"email": "chef@kitchenops.internal", "code": "1234"} | 200 {"token": "kops_session_token_xyz", "token_type": "bearer"} | 401 wrong or expired code · 422 missing field or invalid format | REQ-001 |
| GET | /auth/me | Header: Authorization: Bearer <token> | 200 {"email": "chef@kitchenops.internal", "role": "chef"} | 401 missing or invalid session token | REQ-001 |
