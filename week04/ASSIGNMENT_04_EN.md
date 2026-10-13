# Week 4 Assignment — Clickable Prototype and Test Cases

**Due:** lab part pushed by the end of the lecture (11:45) · the rest Saturday 23:59 · Commit to your project repository

> ## The AI log is written by a human. No exceptions.
>
> `week04/ai_log_04.md` is written by **you**, in your own words. Outside the Evidence block and the
> bold quotes of its answer (§9) no assistant is used: not to write it, not to "improve" it, not even
> for the English. **A log written by an assistant earns 0.** Your English is not graded; a person
> reads every log.

> ## What your collaborator says, you write by hand. No assistant, not even for the grammar.
>
> This week one classmate of your choice, your **collaborator**, tests your prototype. Your
> notes of what they say, the notes in `walkthrough_04.json`, the sentence you quote from
> them and your decisions in `group_04.json` are typed by **you**, in your own words. No
> assistant writes them, translates them or corrects them, not even a comma. Your English or
> Turkish is not graded; a person reads every record.

> **Before the lecture:** open `week02/requirements.json` and note which of your
> requirements are `must`. Then decide on your **main flow**: the path a user takes, from
> logging in to the one thing your app exists for. For StudyRoom it is: log in → see
> today's free rooms → book a room → see the booking.

Last week your requirement ids became permanent. This week you see your requirements as
screens, and another person tests them. You build a clickable prototype of your main flow, you turn your acceptance
criteria into test cases, and your collaborator, a classmate you choose, runs those test cases
on your prototype.

Why now, before any code? Nobody can write all the requirements of a product without
seeing it. When someone else clicks through your screens, they look for a button that is not
there, or they expect a message that no requirement mentions. Each of those is a missing
or unclear requirement, and finding it today costs you one screen. Finding it in Week 8
means changing the server and both clients.

---

## What arrives with this week

Run the checker once:

```bash
python .github/check_deliverables.py
```

It brings `week04/prototype/` (three starter screens, `style.css` and a `README.md` with
the rules), `week04/test_cases.json`, `week04/walkthrough_04.json`,
`week04/group_04.json` (this week it holds your collaborator), `week04/store.json` and
`week04/ai_log_04.md`.

---

## Where an assistant helps this week, and where it does not

| Part | Assistant |
|---|---|
| The HTML and CSS of each screen (the REQ lines in the prompt; one screen, one commit) | **Helps** |
| A draft of your test cases from your acceptance criteria (you check each one against its criterion) | **Helps**, the approval is yours |
| The invented data, proposed from your criteria | **Helps**, the approval is yours |
| Fixing the prototype after a `fail` | **Helps** |
| Choosing your main flow, and writing the criteria before the prompt: which requirements the screen must meet | **No help**: you decide |
| What your collaborator says: your paper notes, the notes in `walkthrough_04.json`, the sentence you quote, `accepted` and `why` in `group_04.json` | **No help at all, the grammar and any translation included**: you write it by hand |
| The Change log lines, and your decision on each `fail` | **No help** |
| `ai_log_04.md`, outside the Evidence block and its bold quotes | **No help** |
| `store.json`, the developer account, the screenshot | **No help** |

---

## In the lab — pushed by the end of the lecture (11:45)

The lab has three parts. About 25 minutes of explanation; then you build until about
10:30 (push at 10:00, whatever state the work is in); then the walk-through with your
collaborator until about 11:30 (push at 11:00, or right after your own turn if 11:00 falls in it); and
the last fifteen minutes for your files, the checker and the push at the end of the lecture (11:45).

### 1. The prototype — `week04/prototype/`

A prototype shows how the app will be used before any of it is built. There is no server
and the data is invented; what is real is the flow: which screen comes after which, what
each screen asks for, and what the user sees when something goes wrong.

- **One HTML file for each screen**, all in `week04/prototype/`. `index.html` is the first
  screen. It opens with a double click: no server, no framework, no build step.
- **Every screen can be reached by clicking** from `index.html`, and every link leads to a
  screen that exists.
- **Every screen has a comment near the top that names the requirements it serves**:
  `<!-- serves: REQ-002, REQ-006 -->`. This is how a screen is traced back to the
  requirement it exists for. If your phone-screen requirement is not REQ-006, change
  REQ-006 to its id in the starter screens and in TC-006-01.
- **Links use the full file name, in lower case and in quotes**: `href="rooms.html"`. The
  checker follows only links written this way.
- **The invented data is fixed**, so that your collaborator can follow a test case: in `code.html`
  the correct code is always 1234. Write your own invented values in
  `prototype/README.md` (for StudyRoom: "Room 3 is busy from 14:00 to 15:00").
- **Choose the invented data from your acceptance criteria.** A test case can only be run
  if the values it needs exist: a free slot and a busy one, a right code and a wrong one,
  an empty list and a list with entries, the edge values (30 and 120 minutes). Ask your
  assistant to propose them from your criteria, approve them yourself, write them under
  "Invented data" in `prototype/README.md` and use the same values on every screen. A
  collaborator who cannot find the data there cannot run the test case, and the result is
  `blocked`. Use no real names or e-mail addresses.
- **There is no server, so a screen remembers nothing.** After a user books a slot, the
  next screen simply shows the same fixed data with that booking already in it.
- The three starter screens (`index.html`, `code.html`, `home.html`) are the login that
  everyone shares (REQ-001). Replace their [bracketed] parts, then build your main flow
  from `home.html` onwards: the screens you listed in `week03/screens_03.md`, one HTML
  file for each row.

**By the end of the lecture (11:45): at least five screens**, which means the three starter screens and at least
two of your own. The rest of the flow follows by Saturday.

**Build it with your assistant, but give it your criteria first** (`AI_Doc5` §1). Before
you ask for a screen, paste into the prompt the REQ lines that the screen must meet, with
their acceptance criteria. Then check the answer against them. Assistants like to add
things that no requirement asks for: a password field and a "Sign in with Google" button
on a login screen (both against REQ-001), a layout 480 px wide (against REQ-006), a screen
with no message for the case where something goes wrong. Keep one of these exchanges; it
is this week's AI log.

**Your assistant writes the screens; you decide what they do.** The flow, the invented
data and the check of every screen are yours. Tell the assistant to use plain HTML and
CSS, one file for each screen, the shared `style.css` and no framework: an assistant that
answers with React, or with one page that swaps its content, gives you something the
checker cannot follow. Ask for one screen at a time, open it in the browser, check it
against your criteria and commit it before you ask for the next one: one screen, one
commit.

### 2. The test cases — `week04/test_cases.json`

A test case is one acceptance criterion turned into steps that anyone can follow and a
result that anyone can check. Here is how one StudyRoom requirement becomes two test
cases:

| | |
|---|---|
| **REQ-002** | A student books a free slot of 30 to 120 minutes in a room. |
| **Acceptance** | A booking for a free slot is saved and shown as busy; a booking for a busy slot is refused with a message. |
| **TC-002-01** | *Precondition:* logged in. *Steps:* open Rooms; choose Room 3, today, 16:00 to 17:30; tap Book. *Expected:* "Booked: Room 3, 16:00–17:30" appears, and the slot is shown as busy. |
| **TC-002-02** | *Precondition:* Room 3 is busy from 14:00 to 15:00. *Steps:* choose Room 3, today, 14:00 to 15:00; tap Book. *Expected:* the message "This slot is taken" appears, and nothing is booked. |

The rules:

- **Every `must` requirement has at least one test case.** Write them in the lab, because
  your collaborator runs them before the end of the lecture (11:45).
- **The id says which requirement it tests**: TC-002-01 and TC-002-02 both test REQ-002.
  A test case id never changes its meaning, as with the REQ ids.
- **The steps use real values** ("Room 3, 16:00 to 17:30", not "a room and a time"), and
  **the expected result is something a tester can see** ("the message 'This slot is
  taken'", not "it works").
- **By Saturday, at least three requirements also have a test case for when something
  goes wrong**: a wrong code, an empty field, a slot that is already taken. TC-001-02 in
  the file is the first one.

Your assistant may draft the test cases from your acceptance criteria. Check each one
against its criterion: does it test what the criterion says, or something the assistant
invented? A test case for a behaviour that no requirement describes is either a missing
requirement (add it, with a Change log line) or a test case to delete.

WEAK: *"TC-002-01 — Booking works. Steps: book a room. Expected: success."*
STRONG: the two rows in the table above.

### 3. The walk-through — with your collaborator

Your **collaborator** is one classmate of your choice, from your own lecture, from any group.
Agree on who it is before the walk-through starts. Two classmates often choose each other and
take turns, but they do not have to. Each prototype gets about twelve minutes.

- **The owner** (you) opens the prototype on their own laptop, 390 px wide (F12, then the
  phone icon), shows the collaborator the invented data in `prototype/README.md`, and then
  hands over the laptop. From then on the owner watches, does not explain and does not help.
  The owner notes each run on paper, with the collaborator's most useful sentence, and types
  the runs into `walkthrough_04.json` right after the turn.
- **Your collaborator** reads the steps of one test case aloud, does exactly what they say,
  and says what they see. They run **at least four** of your test cases, and at least two of
  them belong to the main flow, not to the login.
- **Each run has one result.** `pass`: the collaborator saw what "expected" says. `fail`:
  they did not, and the note says what they saw instead. `blocked`: it cannot be checked on a
  prototype, for example "the code arrives within one minute", which needs the real
  server; it is checked on the real system from Week 5. A screen that does not exist
  yet is a `fail`.

The collaborator works on your laptop because the prototype is in your private repository.
That is allowed: you are still the one who types into your repository.

**What your collaborator says, you write by hand.** Your paper notes, the notes in
`walkthrough_04.json`, the sentence you quote and your decisions are typed by you, in your own
words. No assistant writes them, translates them or corrects them: not for the grammar, not for
the English, not even a comma. Write down what your collaborator said as they said it. Your
English or Turkish is not graded; a person reads every record.

**The feedback comes from your collaborator and from nobody else.** The student number in the
`tester` field of every run in `walkthrough_04.json` is theirs, and the same number is in
`group_04.json`.

**Nobody loses points for a fail.** The points are for running the test cases honestly
and for what you do about each fail. Listen for the other kind of finding too: "I looked
for a way to cancel the booking". No test case covers it, because no requirement asks for
it. Write it in a note; by Saturday you decide whether it becomes a requirement.

### 4. `week04/group_04.json` — your collaborator

The file keeps its name from Week 3, but this week it holds **one entry: your collaborator**, role
`collaborator`, with their 9-digit student number (not yours). For them, **the most useful
thing they found or said, quoted** as one full sentence, in their words, typed by you.
`accepted` and `why` can wait until Saturday, when you know what you changed. Your
collaborator does not have to name you back, and no point is taken if they do not. The
collaborator you name earns the contributors' bonus.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week04: prototype, test cases, walk-through"
git push
```

Push at 10:00, at 11:00 and at the end of the lecture, **11:45**. Right after it I
freeze every repository. What is not pushed does not exist.

---

## By Saturday 23:59

### 6. Fix, run again, update

- **Fix every fail.** Usually the prototype changes. Sometimes the test case was wrong,
  or the requirement was: then change that instead, and say why in the Change log.
- **Round 2 with your collaborator, online.** Each failed test case is run again after the
  fix: you share the screen with the fixed prototype, your collaborator reads the steps of
  each failed test case aloud, and you click exactly what they say. Your group meeting is the
  natural place if your collaborator is in your group; otherwise use any call you both choose.
  Add these runs to `walkthrough_04.json` with `"round": 2`, written by you. A test case that you
  dropped instead (`"dropped": true`, with a Change log line) needs no round 2.
- **Update `requirements.json` and `test_cases.json`** with what the walk-through showed:
  a requirement that was missing (with a new id), an acceptance criterion that was
  unclear, a test case that was missing. Each change gets **one dated line in the
  Change log of `PROPOSAL.md`** that names the ids:
  "2026-10-13 — REQ-011 added: my collaborator looked for a way to cancel a booking and
  found none; TC-011-01 written."

Both files can still change for one more week. At the end of Week 5 they become your
**baseline**. After that, every change needs a change request: a short written request
that names the change and every file it affects.

### 7. The full screen flow

Every functional `must` requirement has at least one screen that serves it, and every
screen names its requirements in the `serves:` comment. In all you need **at least seven
screens**. Colours and fonts do not matter; the flow does.

### 8. S1 — your developer account, `week04/store.json`

Open your developer account with the store you named in §12 of your proposal, and do it
**on the day of the lecture**: the identity check takes from one day to a week, and no
later step can start without it. If you already applied in Week 3, write that date in
`store.json`, with the status your account has now.

| Store | Fee | What it asks for | How long the check takes |
|---|---|---|---|
| Google Play | about 25 $, once | a Google account and an identity document that matches your payments profile. A new personal account also confirms once, with the Play Console app, on a real Android phone (Android 10 or later; an emulator is not accepted). No Android phone? Borrow a classmate's for one minute. | a few days |
| Huawei AppGallery | free | a Huawei ID, an identity card or passport, and a bank document | 1–2 working days |
| Samsung Galaxy Store | free | a Samsung account and the Seller Portal sign-up | a few days |
| Apple App Store | about 99 $ every year | an Apple ID with two-factor authentication, an identity check and the payment | usually a day or two after the payment |

Fill in `store.json`: the store, the date you applied, your developer name and the status
(`applied` is enough for this week). Save a screenshot of your developer console or of
your application in `week04/`, with your address, your ID number and any card details
covered, and write its file name in `evidence`. **Never write a password, a card number or an ID number anywhere in the
repository.** Whether you pay a fee is your decision: Huawei AppGallery and Samsung
Galaxy Store cost nothing.

### 9. Acceptance criteria first — `week04/ai_log_04.md`

Choose one screen that your assistant built. Before the prompt, you wrote down the REQ
lines it had to meet and the test cases that would run on it. Show them, the answer
measured against each of them, and what you changed. The instructions and a weak/strong
pair are inside the file. **The AI log is written by a human: you.** Outside the Evidence block and the bold quotes below no assistant is used, not to write it, not to improve it, not even for the language. **A log written by an assistant earns 0.**

Two kinds of words, and the reader must see which is which. Your words are plain text: every word, the grammar too. The assistant's words are bold, and only where they must come from it: a phrase or one sentence of its answer that you point at (what it claimed, what it added), such as: the answer ended with **All requirements are met**. Each bold phrase must also stand, letter for letter, in the Evidence block. Bold is for nothing else: no bold for emphasis, headings or labels. In the Evidence block your prompt goes under `ME:` and the answer, untouched, under `AI:`.

### 10. Push again, checks green

Several commits as you work, each with some new work in it and a message that says what changed; a commit does not need to be a finished part. Everything the checker
asks for is listed below.

---

## Deliverables checklist

**In the lab, by the end of the lecture (11:45)**
- [ ] `week04/prototype/` — at least five screens, `index.html` included, all reachable by clicking, no [bracketed] parts left
- [ ] `week04/test_cases.json` — at least one test case for every `must` requirement
- [ ] `week04/walkthrough_04.json` — your collaborator ran at least four of your test cases, at least two of them from the main flow; a note for every `fail` and `blocked`; written by you, by hand
- [ ] `week04/group_04.json` — your collaborator (one entry), a quoted finding from them, written by you, by hand

**By Saturday**
- [ ] Every failed test case run again in round 2, or dropped with a Change log line
- [ ] `requirements.json` and `test_cases.json` updated; a Change log line that names the ids
- [ ] At least seven screens; every functional `must` requirement has a screen; every screen has its `serves:` comment
- [ ] At least three requirements with a test case for when something goes wrong
- [ ] `group_04.json` — `accepted` and `why` decided for your collaborator's finding, written by you, by hand
- [ ] `week04/store.json` — S1 filled in, the screenshot saved
- [ ] `week04/ai_log_04.md` — your criteria, the answer measured against them, the exchange pasted; written by you, not by an assistant (that earns 0)
- [ ] Checks green on GitHub; Weeks 1–3 still pass

---

## Not this week

No server code and no design documents yet (both in Week 5). No framework for the
prototype: React, Flutter and the rest come with the real clients. No real e-mail is sent;
the code is 1234.

---

## How this week is graded

**End of the lecture — 5 points.** The prototype, the test cases, the walk-through with
your collaborator, and a quoted finding from them, read from your repository as it stands at the end of the lecture (11:45).

**Saturday 23:59 — 5 points.** Checks green on your final state: **2**. Human
involvement: **2**, which means your `ai_log_04.md` with its evidence, written by you (a log written by an assistant earns **0**), the record of what your collaborator said, written by you by hand, and real findings
with real decisions behind them. Commit discipline: **1**, which means several pushes at
different times in the lecture (at least three) and several commits as you work, each with some new work in it.

**S1** is also a graded step of the store bonus, as S0 was in Week 3.

**Contributors' bonus.** The collaborator you name earns 10% of your week's mark; you earn the
same for the test cases you run for the classmate who names you.

**One student, one computer, one GitHub account.** Work done on a classmate's machine or
under a classmate's session earns nothing for the lecture. The walk-through is the one
exception: your collaborator uses your laptop, and you type the results.
