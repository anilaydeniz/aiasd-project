# Week 5 Assignment — Design, API Contract and the Server Skeleton

**Due:** the lecture part pushed by 11:45 · the rest Saturday 23:59 · Commit to your project repository

## Your project so far, and where it is going

A month ago your project was an idea in your head. Look at what it has become:

- **Week 1:** your tools, and your first real conversations with two AI assistants.
- **Week 2:** a real problem, real people who have it, and the first list of what your product must do.
- **Week 3:** you pitched it to your group, looked at the market and the competition, and the project became yours for good.
- **Week 4:** it became screens. A classmate clicked through them, and you saw your product through someone else's eyes.

From this week on it becomes software. Your product gets a skeleton: you decide what it is made of, you write
the promise its parts make to each other (the API contract), and a real server answers you for the first time.
Next week a user logs in with a code that arrives in their mailbox. In Week 7 the same login runs on a phone.
In Week 8 your product does the one thing it exists for, on the server, the web and the phone. Then come real
testers and the store's review, and in December you install your own app from a store in front of the examiner.

This week is the one engineers enjoy most: the moment a design turns into code. You write a few lines of a
contract by hand, watch your server list its endpoints at `/docs`, and write tests that fail on purpose,
because the code they are waiting for does not exist yet. Next week you make them turn green, one by one.

## This week: what you build, and its place in the project

This week you build the part that everything else stands on:

- **The design** (`week05/DESIGN.md`): the parts your product is made of, and which requirement each part serves.
- **The API contract** (`week05/api.md`): the promise your server makes to its clients: what they may ask, what
  they get back, and every way a request can fail.
- **The server skeleton** (`server/`): a real server that already answers every endpoint of the contract, even
  if for now only with "not built yet".
- **The first tests**: your login test cases turned into code, waiting for the login.

Why it matters: in Week 6 you build the login behind the endpoints you list today, and your web client calls
exactly those endpoints. In Week 7 your mobile client calls the same endpoints, unchanged. In Week 8 your
product's own feature adds new rows to the same contract and new components to the same design. Every test you
write now keeps watching your code whenever an assistant changes it in a later week. A mistake in the contract
found today costs you one line; found in Week 8, it costs you the server and both clients.

### What you need to know this week

| | What it is |
|---|---|
| **Server and clients** | The server keeps the data and the rules. The web client and the mobile client show the screens and ask the server for everything. |
| **Component** | One part of your system with one job: "Server: login", "Database", "Mobile client". |
| **Endpoint** | One thing the server answers: a method and a path, such as `POST /auth/code`. `GET` reads, `POST` sends or creates, `PUT` and `PATCH` change, `DELETE` removes. |
| **Request, response, status code** | What the client sends, what comes back, and a number that says how it went: 200 it worked, 401 not logged in, 422 a wrong field, 501 not built yet. |
| **JSON** | The text both sides use for requests and responses: `{"email": "deniz@example.com"}`. |
| **API contract** | All the endpoints in one table, `api.md`: the page that the server, both clients and every test agree on. |
| **FastAPI, route, uvicorn** | FastAPI is the Python library of your server; a route is one function that answers one endpoint; uvicorn runs the server, and `/docs` lists every route. In one page: `week05/FASTAPI_CARD_EN.md`. |
| **Test, pytest** | A test case turned into code; `pytest` runs them all. A test's name begins with its test case id. Red means it failed, green that it passed. |
| **Baseline, change request** | From Saturday your requirements and test cases are fixed; changing them then takes a written change request. |
| **Mermaid** | The text notation for diagrams that you know from Week 2; this week it draws your architecture. |

## When is what due

| When | What you do | Where |
|---|---|---|
| **Before the lecture** | Run the checker once, install `week05/requirements.txt`, see the starter test pass, read `week05/FASTAPI_CARD_EN.md` (10 minutes) | the box below |
| **In the lecture, pushed by 11:45** | **The login rows of `api.md`, written by you, by hand, pushed at 10:00** · the Components table in `DESIGN.md` (at least four components) · a route in `server/` for every row of `api.md` · the first login test, named by its test case id, run and failing for the right reason · pushes at 10:00, 11:00 and 11:45 | §1–§5 |
| **By Saturday 23:59** | `api.md` complete · at least three login tests, named by test case ids · every functional `must` requirement served by a component · the architecture in Mermaid · `ai_log_05.md` · the last changes to `requirements.json` and `test_cases.json`: they become your **baseline** | §6–§11 |

The login rows of `api.md` cannot be written after the code: they are read from your
10:00 push, before your server has its routes.

> ## The AI log is written by a human. No exceptions.
>
> `week05/ai_log_05.md` is written by **you**, in your own words. Outside the Evidence block
> and the bold quotes of the assistant's answer (§10) no assistant is used: not to write it,
> not to "improve" it, not even for the English. **A log written by an assistant earns 0.**
> Your English is not graded; a person reads every log.

> ## The login rows of `api.md` you write by hand, before any code.
>
> What a client sends, what comes back, and every way the login can fail are this week's
> decision, and they are yours. Write the rows from REQ-001 and your test cases, before you
> ask an assistant for a single line of code. The code is written from the contract, not
> the other way round.

> **This week you work alone.** There is no collaborator, no `group_05.json` and no
> contributors' bonus. Your group meets again from Week 6.

> **Before the lecture:** run `python .github/check_deliverables.py` once. It brings
> `week05/` and a new folder at the root of your repository, `server/`. Then, with your
> virtual environment active:
>
> ```bash
> pip install -r week05/requirements.txt
> python -m pytest
> ```
>
> The last line must say `1 passed`. If the install fails, come to the lecture with the
> error message, not without it. Read `week05/FASTAPI_CARD_EN.md`: one page, ten minutes.

Why the contract before the code? Your web client (Week 6) and your mobile client (Week 7)
are written against the API contract. If the contract is written after the code, it only
describes whatever the assistant happened to write, and your test cases no longer test your
requirements. Written first, it is the one page that the server, both clients and every
test agree on.

---

## What arrives with this week

Run the checker once:

```bash
python .github/check_deliverables.py
```

It brings into `week05/`: this assignment, `DESIGN.md` and `api.md` (the two documents of the
week, with instructions inside), `ai_log_05.md`, `requirements.txt` (FastAPI and pytest, with
their exact versions) and `FASTAPI_CARD_EN.md` (one page: how to read the code an assistant
writes for FastAPI).

At the root of your repository it brings `server/`: `main.py`, a server with one endpoint,
`/health`, and `tests/test_health.py`, one test that passes. The server lives in `server/`
for the rest of the term; Weeks 6 to 8 build on it.

Start the server from the root of your repository:

```bash
uvicorn server.main:app --reload
```

Then open http://127.0.0.1:8000/docs in your browser. FastAPI lists every endpoint of your
server there, and you can try each one. Stop the server with Ctrl+C.

---

## Where an assistant helps this week, and where it does not

| Part | Assistant |
|---|---|
| The FastAPI code of a route, with its `api.md` row in the prompt (one route, one commit) | **Helps** |
| The code of a test from one of your test cases (you check that it tests what the test case says) | **Helps**, the approval is yours |
| A proposal of components from your requirements | **Helps**, the decision is yours |
| The Mermaid syntax of your architecture | **Helps** |
| Explaining an error message | **Helps** |
| The login rows of `api.md`: method, path, request, response, errors | **No help**: you write them before any code |
| Running the tests and the server, and reading what they print | **No help**: you run them yourself |
| The Change log lines, and from Sunday the change requests | **No help** |
| `ai_log_05.md`, outside the Evidence block and its bold quotes | **No help** |

---

## In the lecture — pushed by 11:45

About twenty minutes of explanation and a short FastAPI demonstration; then the components
and the login rows of `api.md` (push at **10:00**); then the routes of your server (push at
**11:00**); then the first login test, the checker and the push at the end of the lecture
(**11:45**).

### 1. The design — `week05/DESIGN.md`

**When:** at least four components in the lecture, pushed by 11:45; by Saturday every
functional `must` requirement is served by a component, and the architecture is drawn (§8).

A component is one part of your system with one job. The table names each component, says
what it does in one sentence, and lists the requirements it serves. For StudyRoom:

| Component | What it does | REQ |
|---|---|---|
| Server: login | Sends a 4-digit code to an e-mail address, checks it and gives a token | REQ-001 |
| Server: bookings | Saves a booking for a free slot of 30 to 120 minutes and refuses a busy one | REQ-002, REQ-003 |
| Database | Keeps the users, the rooms and the bookings | REQ-002, REQ-004 |
| Web client | The screens of the prototype, in the browser, 390 px wide | REQ-006 |
| Mobile client | The same screens on a phone | REQ-006 |

The rules:

- **Name each component as you will name it in your code.** "Server: bookings" becomes
  `server/bookings.py` in Week 8.
- **One sentence of what it does.** If you need "and" three times, it is two components.
- **The REQ ids exist** in `week02/requirements.json`. A component that serves no requirement
  needs a reason to exist; without one, it does not belong in the table.
- The first row, the login, is the same for everyone and is already in the file. Keep it and
  adjust its words.

Your assistant may propose components from your requirements. The decision is yours: you
know which parts your product needs, and the assistant does not.

WEAK: *"| Backend | Does everything | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |"*
STRONG: the table above.

### 2. The API contract — the login rows, by hand

**When:** written by hand in the lecture and pushed at 10:00; the rest of `api.md` by
Saturday (§6).

An **endpoint** is one thing your server answers: a method and a path, such as
`POST /auth/code`. The client sends a **request** and gets back a **response** with a
**status code**, a number that says how it went:

| Code | Meaning |
|---|---|
| 200 | It worked; here is the answer |
| 201 | It worked, and something new was created |
| 400 | The request is wrong |
| 401 | You are not logged in, or your code or token is wrong |
| 404 | There is no such thing |
| 409 | It conflicts with what is already there (a slot that is taken) |
| 422 | A field is missing or has the wrong form (not an e-mail address) |
| 429 | Too many requests: wait |
| 501 | Not built yet |

Every project logs in the same way (REQ-001): the user gives an e-mail address, gets a
4-digit code, and logs in with it. The login therefore needs **at least two endpoints**: one
that asks for a code, and one that logs in with the code. Write both rows yourself, from
REQ-001 and your test cases TC-001-01 and TC-001-02: what goes in, what comes back, and
every way it can fail, each with its status code. Here is StudyRoom's first row:

| Method | Path | Request | Response | Errors | REQ |
|---|---|---|---|---|---|
| POST | /auth/code | {"email": "deniz@example.com"} | 200 {"sent": true} | 422 not an e-mail address · 429 a code was asked for less than a minute ago | REQ-001 |

The second row, logging in with the code, is yours to write. Ask yourself what your test
cases need: what does the client get when the code is right, and what when it is wrong or
too old?

**Write these rows by hand, and push them at 10:00, before any code.** No assistant writes,
corrects or completes them. The 10:00 push is read for them.

### 3. The server skeleton — `server/main.py`

**When:** in the lecture, pushed at 11:00 and at 11:45.

For every row of `api.md`, your server gets a **route**: a function with the same method and
the same path. A route whose work comes later answers **501** until its week comes:

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

The rules:

- **Every row of `api.md` has its route, and every route has its row**, with the same method
  and the same path. The checker compares the two in both directions.
- **The routes live in `server/main.py`**, or in other files of `server/` with FastAPI's
  `APIRouter`. Tests live in `server/tests/`.
- **Each route has a first line that names its requirement**, as above.
- **One route, one commit.** Ask your assistant for one route at a time, with its `api.md`
  row in the prompt. Read the whole answer before you accept it, and refuse what you did not
  ask for. Assistants like to "help": a complete login with a code that is always 1234, a
  password field, a database you did not plan. This week the routes answer 501, nothing more.
- You do not need to restart the server: with `--reload` it picks up every save. Open `/docs`
  and check that every row of `api.md` is there.

### 4. The first login test — `server/tests/test_login.py`

**When:** at least one test in the lecture, run, failing for the right reason, pushed by
11:45; at least three by Saturday (§7).

A test is a test case turned into code. Its name begins with the test case id, written with
underscores, so that anyone can find which test case it checks:

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email():
    response = client.post("/auth/code", json={"email": "deniz@example.com"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}
```

Run every test from the root of your repository:

```bash
python -m pytest
```

Today this test **fails**, and it must: the route answers 501, because the login is built in
Week 6. Read why it fails. The line `assert 501 == 200` is the right reason. `assert 404 == 200`
means the route is missing or its path differs from `api.md`; an `ImportError` means the test
cannot find your server. Fix those, because a test that fails for the wrong reason tests
nothing. A test that passes before the code exists tests nothing either (`AI_Doc5` §2).

Your assistant may write the test from your test case. Check it against the test case: the
same values, the same expected result. An assistant that "fixes" a failing test by changing
the expected value has made the test useless.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week05: login rows of the API contract"
git push
```

Push at **10:00**, at **11:00** and at the end of the lecture, **11:45**, each time with new
work in it and within fifteen minutes of that time. The 10:00 push carries your login rows. Right
after 11:45 I freeze every repository. What is not pushed does not exist.

---

## By Saturday 23:59

### 6. The whole API contract — `week05/api.md`

Every endpoint of your server has its row, and every row has its route. So far that is the
login and `/health`. A login usually needs one more endpoint: the one a client calls to know
who is logged in, with the token in an `Authorization` header. Decide whether yours does.

For each endpoint that serves a requirement: the request, the response with its 2xx code,
and every error with its 4xx code. The endpoints of your other features may wait until their
week; if you add one now, its route comes with it.

### 7. The login tests — `server/tests/test_login.py`

At least **three** tests, each named by a test case id from `week04/test_cases.json`: the code
is sent, a wrong code is refused, an old code is refused, a second code too soon is refused.
If a test needs a test case that does not exist yet (the 429 rule, for example), add the test
case to `test_cases.json` with a Change log line, before Saturday: after Saturday it would be
a change request (§9).

They all fail until Week 6, for the right reason. That is the plan: in Week 6 you build the
login until they pass, one by one. Commit the tests before any login code: your history shows
which came first.

### 8. The design, complete — `week05/DESIGN.md`

- Every functional `must` requirement is served by at least one component.
- **The architecture as a Mermaid diagram**, in the same file: your components, and an arrow
  for every "talks to". GitHub draws it.

### 9. The baseline

On **Saturday at 23:59**, `week02/requirements.json` and `week04/test_cases.json` become your
**baseline**. Make your last changes before then, each with its Change log line.

From Sunday on, a change to either file is a **change request**: a Change log line in
`PROPOSAL.md` that begins with `CR-` and a number, names the change and the ids, and lists
every file it affects:

"2026-10-28 — CR-01: REQ-004 now allows 15-minute slots; affects requirements.json,
test_cases.json (TC-004-02), week05/api.md, server/bookings.py."

### 10. Verify by running — `week05/ai_log_05.md`

Choose one route or one test that your assistant wrote. **Before you run it**, write what you
expect, with the test case id. Then run it yourself: `python -m pytest`, or the server and
`/docs`. Paste the command and its output into the Evidence block, under `TERMINAL:`, down to
the last line, the one that counts the tests. Then name one line of the assistant's code that
you changed or refused, and why. The instructions and a weak/strong pair are inside the file.

**The AI log is written by a human: you.** Outside the Evidence block and the bold quotes no
assistant is used, not to write it, not to improve it, not even for the language. **A log
written by an assistant earns 0.** Your words are plain text; the assistant's words, where
you point at them, are bold and also stand in the Evidence block, as in Week 4.

### 11. Push again, checks green

Several commits as you work, each with some new work in it and a message that says what
changed, in at least two separate sittings outside the lecture. Everything the checker asks
for is listed below.

---

## Deliverables checklist

**In the lecture, pushed by 11:45**
- [ ] `week05/api.md` — at least two login rows (REQ-001), written by you, by hand, pushed at 10:00
- [ ] `week05/DESIGN.md` — at least four components, each with what it does and the REQ ids it serves
- [ ] `server/` — a route for every row of `api.md`, the same method and path; the server starts and `/docs` opens
- [ ] `server/tests/test_login.py` — at least one test named by a test case id, run, failing for the right reason

**By Saturday 23:59**
- [ ] `week05/api.md` — every route has its row; request, response and errors for every endpoint that serves a requirement
- [ ] `server/tests/test_login.py` — at least three tests named by test case ids from `test_cases.json`
- [ ] `week05/DESIGN.md` — every functional `must` requirement served; the architecture in Mermaid
- [ ] `requirements.json` and `test_cases.json` — the last changes made, each with its Change log line: the baseline
- [ ] `week05/ai_log_05.md` — your expectation before running, the command and its output pasted, one line changed or refused; written by you, not by an assistant (that earns 0)
- [ ] Checks green on GitHub; Weeks 1–4 still pass

---

## Not this week

No login yet: the routes answer 501, and the code is not sent (Week 6). No e-mail, no database,
no web or mobile client (Weeks 6 and 7). No group work and no contributors' bonus. No store
step: S2 is in Week 6.

---

## How this week is graded

**End of the lecture — 5 points.** The components, the login rows of `api.md`, a route for
every row, and the first login test, read from your repository as it stands at the end of the
lecture (11:45).

**Saturday 23:59 — 5 points.** Checks green on your final state: **2**. Human involvement:
**2**, which means your `ai_log_05.md` with the real output pasted, written by you (a log
written by an assistant earns **0**), and login rows that you wrote by hand before the code.
Commit discipline: **1**, which means a push with new work at each of the three checkpoints
(10:00, 11:00, 11:45, within fifteen minutes) and at least two commits outside the lecture, in
separate sittings.

**One student, one computer, one GitHub account.** Commit from your own computer, under your
own account. Work done on a classmate's machine or under a classmate's session earns nothing
for the lecture. If one day you really must commit from another computer, say so in that
week's AI log, with the day and the reason.
