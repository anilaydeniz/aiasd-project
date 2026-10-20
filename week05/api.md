# API contract — KitchenOps

| Method | Path | Request | Response | Errors | REQ |
|---|---|---|---|---|---|
| GET | /health | — | 200 {"status": "ok"} | — | — |
| POST | /auth/code | {"email": "chef@kitchenops.internal"} | 200 {"sent": true} | 422 geçersiz e-posta formatı · 429 bir dakikadan kısa sürede tekrar kod istendi | REQ-001 |
| POST | /auth/token | {"email": "chef@kitchenops.internal", "code": "1234"} | 200 {"token": "kops_session_token_xyz", "token_type": "bearer"} | 401 hatalı veya süresi geçmiş kod · 422 eksik alan veya geçersiz kod formatı | REQ-001 |
