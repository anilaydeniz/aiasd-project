# FastAPI in ten minutes — how to read what your assistant writes

*AIASD · Week 5 · one page. You will not write much FastAPI by hand; you will read a lot of it.
This card is what you need to read it, run it and say no to it.*

## 1. The app and a route

```python
from fastapi import FastAPI

app = FastAPI(title="StudyRoom")          # the server; uvicorn runs this object


@app.get("/health")                      # method + path: one row of api.md
def health() -> dict:
    return {"status": "ok"}               # a dict becomes JSON: {"status": "ok"}
```

`@app.get`, `@app.post`, `@app.put`, `@app.patch`, `@app.delete`: the decorator says which method
and which path the function answers. **Check it against your `api.md` row first**: the same
method, the same path, letter for letter.

## 2. What the client sends: the request

```python
from pydantic import BaseModel


class CodeRequest(BaseModel):             # the JSON body, field by field
    email: str


@app.post("/auth/code")
def ask_for_code(body: CodeRequest) -> dict:
    ...
```

A `BaseModel` lists the fields of the JSON body. If a field is missing, FastAPI answers **422**
by itself, before your function runs. **Read every field**: an assistant that adds
`password: str` to a login model has broken REQ-001.

A part of the path that changes: `@app.get("/rooms/{room_id}")` and `def room(room_id: int)`.

## 3. When it does not work: the error

```python
from fastapi import HTTPException

raise HTTPException(status_code=401, detail="Wrong code")
```

Every error in your `api.md` row becomes one `raise HTTPException(...)` with its status code.
This week every route that is not built yet does exactly one thing:
`raise HTTPException(status_code=501, detail="Not built yet: Week 6")`.

## 4. Run it, and look

```bash
uvicorn server.main:app --reload          # from the root of your repository
```

- http://127.0.0.1:8000/docs lists every route. **A route that is not there does not exist**,
  whatever the assistant said. "Try it out" sends a real request.
- `--reload` restarts the server at every save. Ctrl+C stops it.
- The terminal shows each request with its status code: `"POST /auth/code HTTP/1.1" 501`.

## 5. A test

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)                  # a client that talks to the app without a network


def test_TC_002_02_a_busy_slot_is_refused():
    response = client.post("/bookings", json={"room": 3, "start": "14:00", "minutes": 60})
    assert response.status_code == 409
```

`python -m pytest` runs every function whose name begins with `test_`. Each `assert` is one
expected result of the test case. The last line counts them: `1 failed, 2 passed`.

## 6. Five things to refuse

1. A route whose method or path differs from `api.md`.
2. A field that no requirement asks for: `password`, `phone`, `is_admin`.
3. A login code, a password or a token printed with `print()` or written to a log.
4. A test whose expected value was changed so that it passes.
5. A change to a file you did not ask about.
