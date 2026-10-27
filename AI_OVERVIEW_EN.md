# Project overview: its parts, how they agree, and what changes together

*Türkçesi: [`AI_OVERVIEW_TR.md`](AI_OVERVIEW_TR.md)*

Your project is not one file. It is a set of parts, and they all talk about the same requirements. From now
on every week adds parts, and the old parts must stay true. This page lists the parts, says how they must
agree, and says what else to change when you change one of them.

## 1. The parts

| # | Part | File | What is in it |
|---|---|---|---|
| 1 | Proposal | `week02/PROPOSAL.md` | the problem, the product, technologies, success criteria, market, risks, your store (§12); at the end, the **Change log** |
| 2 | Requirements | `week02/requirements.json` | each requirement: id, description, functional or not, priority, acceptance criterion |
| 3 | Use cases | `week02/SRS.md` | the actors; each use case with the requirements it serves; the use case diagram |
| 4 | Screens | `week03/screens_03.md`, `week04/prototype/` | the screens of the main flow; each screen names its requirements (`<!-- serves: REQ-… -->`) |
| 5 | Test cases | `week04/test_cases.json` | each acceptance criterion as steps and an expected result, with `"run"` (server, web or manual) |
| 6 | Design | `week05/DESIGN.md` | the components and the requirements each one serves; the architecture in Mermaid |
| 7 | API contract | `week05/api.md` | every request between a client and the server: method, path, request, response, errors, REQ |
| 8 | Server | `server/`, `server/tests/` | the routes of `api.md`; tests named by test case id (`test_TC_002_02_…`) |
| 9 | Web client | `web/` | the prototype's screens, now real pages that call the server (`serves: REQ-…`) |
| 10 | Store path | `week04/store.json` | your store and the steps S1–S6 |

Later parts join the same chain: the mobile client (Week 7), the chatbot (Week 8), the test report and
the UAT report (Weeks 9–10).

## 2. How the parts must agree

- **`requirements.json` is the source.** Every other part follows it. Never change a requirement only to
  make it fit the code.
- **One id, one meaning, everywhere.** REQ-004 means the same thing in every file. TC-004-02 tests
  REQ-004, and its `"req"` says so. A dropped requirement keeps its id and gets `"dropped": true`; after
  that, no other part uses it.
- **The same facts and numbers.** If REQ-002 says "30 to 120 minutes", then UC2, the booking screen,
  TC-002-02, the 422 in `api.md`, the route and its test all say 30 to 120. The priority is the same
  wherever it is written.
- **Every functional `must` has its whole chain:** use case → screen → test case → `api.md` rows →
  route → test → page (from Week 7, the phone too). This is the chain of the Week 6 assignment.
- **No copies.** SRS §4 and §5 hold one line: "The requirements are in `week02/requirements.json`."
- **REQ-001 is the course login.** REQ-001 and the TC-001 test cases say exactly this: a 4-digit code,
  valid for 10 minutes, usable once; a new code only after 60 seconds; 3 wrong codes in a row lock the
  address for 15 minutes; no passwords.
- **The code does what the documents say.** The route follows `api.md`; the test checks what its test
  case expects.
- **One store.** The store in `store.json` is the one in PROPOSAL §12.

## 3. When you change a part, what changes with it

Change the document first, then the code. How you record it:

- `requirements.json` or `test_cases.json` → a **change request**: one Change log line that starts with
  `CR-` and the next number, names the ids, and lists every file it affects.
- any other document (`SRS.md`, the screens, `DESIGN.md`, `api.md`, `store.json`) → a **dated Change log line**.
- the code → only the commit.

| If you change … | also check and change … | Record |
|---|---|---|
| a requirement (its meaning, a number, its priority) | its use case, screens and pages, test cases, `api.md` rows, `DESIGN.md` component, routes, tests | CR |
| drop a requirement | drop its test cases too; take it out of the use cases, screens, `api.md`, `DESIGN.md` and the code | CR |
| add a requirement | the next free id; then its use case, screen, test cases and, for a functional `must`, the rest of the chain | CR |
| a test case (steps, expected result) | the test named by its id | CR |
| an `api.md` row (path, body, status code) | the route, its tests, the pages (later also the phone) that call it | dated line |
| a use case or a screen | its page in `web/`; if it adds a new behaviour, first a requirement (CR) | dated line |
| a component in `DESIGN.md` | `api.md` and `server/`, if what they do changes | dated line |
| the store | `store.json` and PROPOSAL §12 | dated line |

Example: *2026-10-28 — CR-01: REQ-002 now allows 15-minute slots; affects requirements.json,
test_cases.json (TC-002-02), week05/api.md, server/bookings.py.*

Adding a missing `"run"` field to a test case is not a change request.

Before each push, ask yourself: if someone read only this part, would it say the same as the others?
