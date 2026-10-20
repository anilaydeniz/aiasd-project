# AIASD · Week 5 — Design, API Contract and the Server Skeleton

*Atlas University · Fall 2026–27 · Prof. Dr. Vedat Coşkun*
*Presented from this page. Scroll one section at a time; each `---` is a slide.*

<!-- Instructor: zoom the browser to 150 % and collapse the GitHub header. Total ≈ 2 h 45 min:
20 min explanation + a short FastAPI demonstration · components and the login rows of api.md by hand
until 10:00 (push) · the routes until 11:00 (push) · the first login test, the checker and the last
push at 11:45 · freeze right after it. -->

---

## Today

1. Your project so far, and why the contract comes before the code
2. The design: the components of your product, `week05/DESIGN.md`
3. The API contract: the login rows of `week05/api.md`, **by hand**, push at 10:00
4. FastAPI in ten minutes, and the server skeleton in `server/`, push at 11:00
5. Tests first: the first login test, named by its test case id, push at 11:45
6. By Saturday: the whole contract, three tests, the architecture, the baseline, the AI log
7. How the week is graded

---

## Your project so far, and where it is going

A month ago your project was an idea in your head.

- **Week 1:** your tools, and your first real conversations with AI assistants
- **Week 2:** a real problem, real people who have it, the first requirements
- **Week 3:** the pitch and the market; the project became yours for good
- **Week 4:** screens, and a classmate who clicked through them
- **This week, it becomes software:** a skeleton, a contract, a server that answers you for the first time
- **Next:** a login with a code from your mailbox (6) · the same login on a phone (7) · your product's own feature everywhere (8) · real testers, the store, and in December your app, installed from a store

On Saturday your requirements and test cases become your **baseline**.

<!-- Instructor: tell it as a story, not a list: what each of them has built in four weeks. Ask two or three students what their product does now. -->

---

## This week: the part everything else stands on

- **The design:** the parts of your product, and the requirement each part serves
- **The API contract:** the promise your server makes to its clients
- **The server skeleton:** a real server that answers every endpoint, for now with "not built yet"
- **The first tests:** your login test cases as code, waiting for the login

Week 6 builds the login behind today's endpoints, and the web client calls them. Week 7's mobile client calls the same ones, unchanged. Week 8 adds rows to the same contract.

**A mistake in the contract found today costs one line. Found in Week 8, it costs the server and both clients.**

---

## Where an assistant helps this week

| Part | Assistant |
|---|---|
| The FastAPI code of a route, with its `api.md` row in the prompt (one route, one commit) | **Helps** |
| The code of a test from one of your test cases (you check it against the test case) | **Helps**, the approval is yours |
| A proposal of components from your requirements | **Helps**, the decision is yours |
| The Mermaid syntax of your architecture | **Helps** |
| Explaining an error message | **Helps** |

---

## … and where it does not help at all

| Part | Assistant |
|---|---|
| The login rows of `api.md`: method, path, request, response, errors | **No help**: you write them before any code |
| Running the tests and the server, and reading what they print | **No help**: you run them yourself |
| The Change log lines, and from Sunday the change requests | **No help** |
| `ai_log_05.md` outside the Evidence block and its bold quotes | **No help** |

<!-- Instructor: read the "No help" rows aloud. The new one is the first: the login rows are written by hand, before any code. -->

---

<h1 align="center">THE LOGIN ROWS OF api.md<br>YOU WRITE BY HAND.</h1>

<h1 align="center">BEFORE ANY CODE.</h1>

<p align="center"><b>What the client sends. What comes back. Every way it can fail.<br>No assistant writes them, corrects them or completes them.</b></p>

<p align="center">They are read from your 10:00 push, before your server has its routes.</p>

---

<h1 align="center">THE AI LOG IS WRITTEN<br>BY A HUMAN.</h1>

<p align="center"><b>Outside the Evidence block and its bold quotes: no assistant.<br>Not to write it. Not to improve it. Not even for the English.</b></p>

<h1 align="center">A log written by an assistant earns 0.</h1>

---

## This week you work alone

- No collaborator, no `group_05.json`, no contributors' bonus. Your group meets again from Week 6.
- **One student, one computer, one GitHub account.** Commit from your own computer, under your own account.
- If one day you really must commit from another computer, say so in that week's AI log, with the day and the reason.

---

## Why the contract before the code

Your web client (Week 6) and your mobile client (Week 7) are written against the API contract.

**Written after the code**, the contract describes whatever the assistant happened to write, and your test cases no longer test your requirements.

**Written first**, it is the one page that the server, both clients and every test agree on.

---

## The design — `week05/DESIGN.md`

A **component** is one part of your system with one job. **In the lecture: at least four.**

| Component | What it does | REQ |
|---|---|---|
| Server: login | Sends a 4-digit code to an e-mail address, checks it and gives a token | REQ-001 |
| Server: bookings | Saves a booking for a free slot of 30 to 120 minutes and refuses a busy one | REQ-002, REQ-003 |
| Database | Keeps the users, the rooms and the bookings | REQ-002, REQ-004 |
| Web client | The screens of the prototype, in the browser, 390 px wide | REQ-006 |
| Mobile client | The same screens on a phone | REQ-006 |

---

## Components: the rules

- Name each component as you will name it in your code: "Server: bookings" becomes `server/bookings.py`.
- One sentence of what it does. "And" three times means two components.
- The REQ ids exist in `requirements.json`. A component that serves no requirement needs a reason to exist.
- The assistant may propose; **you decide**.

WEAK: `| Backend | Does everything | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |`

---

## Endpoints, requests, responses

An **endpoint** is one thing your server answers: a method and a path, `POST /auth/code`.

| Code | Meaning |
|---|---|
| 200 / 201 | It worked / something new was created |
| 401 | Not logged in, or the code or token is wrong |
| 404 | No such thing |
| 409 | It conflicts with what is there (a slot that is taken) |
| 422 | A field is missing or has the wrong form |
| 429 | Too many requests: wait |
| 501 | Not built yet |

---

## The login: at least two endpoints

Every project logs in the same way (REQ-001). **The second row, logging in with the code, is yours.** Right code? Wrong code? Too old? Your test cases TC-001-01 and TC-001-02 tell you.

| Method | Path | Request | Response | Errors | REQ |
|---|---|---|---|---|---|
| POST | /auth/code | {"email": "deniz@example.com"} | 200 {"sent": true} | 422 not an e-mail · 429 asked again within a minute | REQ-001 |
| ? | ? | ? | ? | ? | REQ-001 |

---

## Now — until 10:00

1. `week05/DESIGN.md`: at least four components.
2. `week05/api.md`: the login rows, **by hand**, from REQ-001 and your test cases.
3. Checker, commit, **push at 10:00**.

<!-- Start the clock. Walk round and look at the api.md rows on screen: no assistant window open while they are written. -->

---

## FastAPI in ten minutes

```python
from fastapi import FastAPI

app = FastAPI(title="StudyRoom")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

```bash
uvicorn server.main:app --reload
```

Open http://127.0.0.1:8000/docs. **A route that is not there does not exist**, whatever the assistant said.

`week05/FASTAPI_CARD_EN.md`: the same in one page.

<!-- Demonstration: run the starter, open /docs, "Try it out" on /health, then add the /auth/code route below live and watch it appear in /docs with --reload. -->

---

## The server skeleton — one route for every row

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="StudyRoom")


class CodeRequest(BaseModel):
    email: str


@app.post("/auth/code")
def ask_for_code(body: CodeRequest) -> dict:
    """REQ-001: sends a 4-digit code to the e-mail address. Built in Week 6."""
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")
```

A route whose work comes later answers **501** until its week comes.

---

## The skeleton: the rules

- **Every row of `api.md` has its route, and every route has its row**: the same method, the same path. The checker compares them both ways.
- The routes live in `server/main.py`, or in other files of `server/` with `APIRouter`.
- Each route's first line names its requirement.
- **One route, one commit.** The `api.md` row in the prompt; read the whole answer; refuse what you did not ask for.

The assistant will "help": a complete login with a code that is always 1234, a password field, a database you did not plan. **This week the routes answer 501, nothing more.**

---

## Now — until 11:00

1. A route in `server/` for every row of `api.md`, answering 501.
2. `/docs` shows every row.
3. Checker, commit, **push at 11:00**.

---

## Tests first

A test is a test case turned into code. Its name begins with the test case id.

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email():
    response = client.post("/auth/code", json={"email": "deniz@example.com"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}
```

```bash
python -m pytest
```

---

## Red, for the right reason

Today the test **fails**. It must: the login is built in Week 6.

| The failure says | It means |
|---|---|
| `assert 501 == 200` | **The right reason**: the route is there, its work is not |
| `assert 404 == 200` | The route is missing, or its path differs from `api.md` |
| `ImportError` | The test cannot find your server |

A test that fails for the wrong reason tests nothing. **A test that passes before the code exists tests nothing either.**

An assistant that "fixes" a failing test by changing the expected value has made it useless.

---

## Now — until 11:45

1. `server/tests/test_login.py`: at least one test, named by its test case id.
2. Run it. Read why it fails.
3. Checker, commit, **push at 11:45**.

---

## Commit discipline, from this week

**In the lecture:** a push with new work at each checkpoint, **10:00, 11:00 and 11:45**, within fifteen minutes of each.

**Outside the lecture:** at least two commits with new work, in separate sittings.

One commit at the end scores nothing.

---

## By Saturday 23:59

- `api.md`: every route has its row; request, response with its 2xx code, and every error with its 4xx code.
- **At least three login tests**, each named by a test case id from `test_cases.json`. They fail until Week 6, for the right reason. Commit them before any login code.
- `DESIGN.md`: every functional `must` requirement served; **the architecture as a Mermaid diagram**.
- `ai_log_05.md`: verify by running.
- The last changes to `requirements.json` and `test_cases.json`: the **baseline**.

---

## The baseline, and change requests

**Saturday 23:59:** `requirements.json` and `test_cases.json` become your baseline.

**From Sunday**, a change to either is a **change request**: a Change log line that begins with `CR-` and a number, and lists every file it affects.

> 2026-10-28 — CR-01: REQ-004 now allows 15-minute slots; affects requirements.json, test_cases.json (TC-004-02), week05/api.md, server/bookings.py.

Need a test case that does not exist yet? Add it **before** Saturday.

---

## The AI log — verify by running

Choose one route or one test that the assistant wrote.

1. **Before you run it**, write what you expect, with the test case id.
2. Run it yourself: `python -m pytest`, or the server and `/docs`.
3. Paste the command and its output under `TERMINAL:`, down to the line that counts the tests.
4. One line of the assistant's code that you changed or refused, and why.

Your words plain, the assistant's words bold. **A log written by an assistant earns 0.**

---

## How Week 5 is graded — 10 points

| | Points | What |
|---|---|---|
| End of lecture (11:45) | 5 | components, the login rows of `api.md`, a route for every row, the first login test |
| Saturday checker | 2 | the whole contract, three tests, the design complete, the AI log |
| Human involvement | 2 | the AI log with the real output, written by you; login rows written by hand before the code |
| Commit discipline | 1 | a push at each checkpoint (10:00, 11:00, 11:45); two commits outside the lecture, in separate sittings |

No contributors' bonus this week.

---

## Next week: the login works

**Week 6:** the login by e-mail code, end to end. In the lecture the code is written to a file; **by Saturday it arrives by real e-mail**. The web client gets its login screen. Your Week 5 tests turn green, one by one. S2: the app record in your store.

**Before Week 6:** an e-mail account that the server can send from. For Gmail: two-step verification on, then an app password. Never in the repository: it goes into `.env`.

<!-- Instructor: the slides from "By Saturday" on are for the last fifteen minutes, before the 11:45 push. Freeze right after 11:45. -->
