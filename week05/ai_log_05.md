# Week 5 — AI log

## The assistant, and the code I asked it for
I asked Claude to write the initial FastAPI login routes and the pytest login tests for REQ-001.

## What I expected, written before I ran it
Before running pytest, I expected TC-001-01 to fail with HTTP 501 Not Implemented because the login and email sending logic is planned for Week 6.

## The command I ran, and what I saw
I ran python -m pytest in my local terminal. The output showed that test_health.py passed, but the failure for TC-001-01 was assert 404 == 200 instead of 501, because the assistant had generated the endpoint path as **"/auth/send-code"**, whereas my api.md and REQ-001 contract specify /auth/code.

## The line I changed or refused, and why
I changed the endpoint path back to /auth/code by hand so it matches api.md. In addition, the assistant had included a **password: str** field in the request model, which directly violates REQ-001 because KitchenOps uses passwordless OTP login; I refused and deleted that field. After fixing the path, pytest failed with assert 501 == 200, which is the correct reason for Week 5.

## Evidence — the exchange and the terminal output

```text
ME:
Write the FastAPI login route for REQ-001 that accepts a user email and dispatches a code.

AI:
Here is the route for your server:

class CodeRequest(BaseModel):
    email: str
    password: str

@app.post("/auth/send-code")
def send_code(body: CodeRequest):
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")

TERMINAL:
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\Lenovo\.gemini\antigravity-ide\scratch\aiasd-project
plugins: anyio-4.15.1
collected 8 items

server\tests\test_health.py ..                                           [ 25%]
server\tests\test_login.py FFFFFF                                        [100%]

================================== FAILURES ===================================
_______________ test_TC_001_01_a_code_is_sent_to_a_valid_email ________________

    def test_TC_001_01_a_code_is_sent_to_a_valid_email():
        response = client.post("/auth/code", json={"email": "chef@kitchenops.internal"})
>       assert response.status_code == 200
E       assert 501 == 200
E        +  where 501 = <Response [501 Not Implemented]>.status_code

server\tests\test_login.py:10: AssertionError
=========================== short test summary info ===========================
FAILED server/tests/test_login.py::test_TC_001_01_a_code_is_sent_to_a_valid_email
FAILED server/tests/test_login.py::test_TC_001_02_wrong_login_code_is_refused
FAILED server/tests/test_login.py::test_TC_001_03_expired_login_code_is_refused
FAILED server/tests/test_login.py::test_TC_001_04_invalid_email_format_is_refused
FAILED server/tests/test_login.py::test_TC_001_05_second_code_request_too_soon_is_refused
FAILED server/tests/test_login.py::test_TC_001_06_unauthenticated_user_cannot_access_profile
========================= 6 failed, 2 passed in 0.62s =========================
```
