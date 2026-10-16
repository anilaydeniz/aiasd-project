# AIASD · Week 4 — Clickable Prototype and Test Cases

*Atlas University · Fall 2026–27 · Prof. Dr. Vedat Coşkun*
*Presented from this page. Scroll one section at a time; each `---` is a slide.*

<!-- Instructor: zoom the browser to 150 % and collapse the GitHub header. Total ≈ 3 h:
25 min explanation · build until about 10:30 (push at 10:00) · walk-through until about 11:30,
12 min per prototype (push at 11:00) · files, checker and the last push at 11:45 · freeze right after it. -->

---

## Today

1. Why a prototype, and why now
2. The prototype: plain HTML screens in `week04/prototype/`
3. From an acceptance criterion to a test case
4. Build time: the prototype and `test_cases.json`
5. The walk-through: your collaborator runs your test cases on your prototype
6. By Saturday: fix, run again, update, S1, the AI log
7. How the week is graded

---

## Where an assistant helps this week

| Part | Assistant |
|---|---|
| The HTML and CSS of each screen (the REQ lines in the prompt; one screen, one commit) | **Helps** |
| A draft of your test cases from your acceptance criteria (you check each one against its criterion) | **Helps**, the approval is yours |
| The invented data, proposed from your criteria | **Helps**, the approval is yours |
| Fixing the prototype after a `fail` | **Helps** |

---

## … and where it does not help at all

| Part | Assistant |
|---|---|
| Your main flow, and the criteria written before the prompt | **No help**: you decide |
| What your collaborator says: your notes, `walkthrough_04.json`, the quoted sentence, `accepted` and `why` | **No help at all, grammar and translation included**: by hand |
| The Change log lines, your decision on each `fail`, whether a document changes | **No help** |
| `ai_log_04.md` outside the Evidence block and the bold quotes | **No help** |
| `store.json`, the developer account, the screenshot | **No help** |

<!-- Instructor: read the "No help" rows aloud. The new one is the second: what the collaborator says is written by hand, the grammar and any translation included. -->

---

## Why a prototype, and why now

Nobody can write all the requirements of a product without seeing it.

When someone else clicks through your screens, they look for a button that is not there, or they expect a message that no requirement mentions. Each of those is a missing or unclear requirement.

**Found today, it costs you one screen. Found in Week 8, it costs you a server change and two clients.**

That is why your requirements stay open until the end of Week 5: this week shows you what is missing.

---

## The prototype — `week04/prototype/`

- **One HTML file for each screen.** `index.html` is the first. A double click opens it: no server, no framework, no build step.
- **Every screen can be reached by clicking.** Write links as `href="rooms.html"`: the full name, lower case, in quotes.
- **Every screen names its requirements:** `<!-- serves: REQ-002, REQ-006 -->`
- **The invented data is fixed**, so that your collaborator can follow the steps. The login code is always **1234**. Your own values go in `prototype/README.md`.
- **Three starter screens** arrive with the checker: the login that everyone shares (REQ-001). Your main flow starts at `home.html`.
- **No server, so no memory:** after a booking, the next screen shows the same fixed data with the booking already in it.

**By the end of the lecture (11:45): at least five screens. By Saturday: the whole flow, at least seven.**

---

## Build it with your assistant — criteria first

`AI_Doc5` §1: before you ask for a screen, paste the REQ lines it must meet, with their acceptance criteria. Then check the answer against them.

What assistants like to add, and what it breaks:

| The assistant adds | It breaks |
|---|---|
| a password field, "Sign in with Google" | REQ-001: a code by e-mail, no password |
| a layout 480 px wide | REQ-006: 390 px, no horizontal scroll |
| no message when something goes wrong | the test case for the wrong code |

**Tell it what you want:** plain HTML and CSS, one file for each screen, the shared `style.css`, no framework. One screen at a time, and **one commit for each screen**.

**The invented data:** let the assistant propose it from your criteria (a free slot and a busy one, a right code and a wrong one, an empty list, the edge values). You approve it and write it in `prototype/README.md`. No data there means the collaborator's result is `blocked`.

Keep one of these exchanges. It is this week's AI log.

---

<h1 align="center">THE AI LOG IS WRITTEN<br>BY A HUMAN.</h1>

<h1 align="center">YOU WRITE IT.<br>NOT AN ASSISTANT.</h1>

<p align="center"><b>Outside the Evidence block and its bold quotes: no assistant.<br>Not to write it. Not to improve it. Not even for the English.</b></p>

<h1 align="center">A log written by an assistant earns 0.</h1>

<!-- Instructor: read it aloud once, and leave it on the screen for a few seconds before moving on. -->

---

## The AI log: two kinds of words

Your words: plain text. Every word, every comma, the grammar too. You type them.

The assistant's words: bold. Only where they must come from the assistant: a phrase or one sentence of its answer that you point at.

What it looks like in your log:

> The first answer ended with **All requirements are met**. But it had a password field, and REQ-001 says no password. I had written that criterion before the prompt.

1. A bold phrase must also stand, letter for letter, in the Evidence block.
2. A phrase or one sentence, never a paragraph. The whole answer goes in the Evidence block under `AI:`, your prompt under `ME:`.
3. Bold is for the assistant and for nothing else: no bold for emphasis, headings or labels.
4. Everything else you type yourself: not the sentences, not the grammar, not the translation, not the "polish" from an assistant.

<!-- Instructor: point at the example. Bold is the assistant, the rest is the student. The reader of the log must see it in one glance. -->

---

## From an acceptance criterion to a test case

| | |
|---|---|
| **REQ-002** | A student books a free slot of 30 to 120 minutes in a room. |
| **Acceptance** | A booking for a free slot is saved and shown as busy; a booking for a busy slot is refused with a message. |
| **TC-002-01** | *Pre:* logged in. *Steps:* open Rooms; Room 3, today, 16:00 to 17:30; tap Book. *Expected:* "Booked: Room 3, 16:00–17:30"; the slot is shown as busy. |
| **TC-002-02** | *Pre:* Room 3 is busy 14:00–15:00. *Steps:* Room 3, today, 14:00 to 15:00; tap Book. *Expected:* "This slot is taken"; nothing is booked. |

The id says which requirement it tests. **TC-002-01** and **TC-002-02** both test **REQ-002**, and an id never changes its meaning.

---

## What makes a good test case

- **One requirement.** The `req` field names it.
- **Steps with real values:** "Room 3, 16:00 to 17:30", not "a room and a time".
- **An expected result a tester can see:** "the message 'This slot is taken'", not "it works".
- **The wrong path too:** a wrong code, an empty field, a slot that is taken. By Saturday, at least three requirements have one.

WEAK: *"Booking works. Steps: book a room. Expected: success."*

STRONG: the two rows on the previous slide.

---

## Test cases with an assistant

Your assistant may draft test cases from your acceptance criteria. Then check each one against its criterion.

**Does it test what the criterion says, or something the assistant invented?**

A test case for a behaviour that no requirement describes is one of two things:

- a **missing requirement**: add it, with a new id and a Change log line;
- a **test case to delete**.

Every `must` requirement has at least one test case by **the end of the lecture (11:45)**, because your collaborator runs them today.

---

## The earlier documents are still open

`requirements.json`, the use cases in `SRS.md`, `screens_03.md`, `PROPOSAL.md`: none is frozen. Building the screens is their first real test, and it will show gaps. **Noticing the gap and recording the change is the work.**

Ids never change meaning: new id, or `"dropped": true`. **Every change: one dated Change log line that names the ids.** The decision is yours alone, no assistant.

---

## Signs that a document must change

- you cannot write a screen's `serves:` comment → a requirement is missing, or the screen is not needed
- a `must` has no screen when the flow is complete → a gap in the flow, or not really `must`
- a criterion cannot become a result a tester can see → the criterion is unclear
- the invented data needs a value the criterion never mentions → the criterion has no edge
- a `fail` where the prototype does what the requirement says → the requirement is wrong, not the prototype

---

## Build time — until about 10:30

1. Run the checker: `week04/` arrives.
2. Replace the [bracketed] parts of the three starter screens.
3. Build your main flow from `home.html`: the screens in `week03/screens_03.md`, one by one, criteria first.
4. Write `test_cases.json`: at least one test case for every `must`.
5. Open every screen 390 px wide: F12, then the phone icon.

**Push at 10:00**, whatever state it is in.

<!-- Walk around. At 10:00 check the board: who has no week04/ yet. At 10:25 announce five minutes. -->

---

## The walk-through — with your collaborator

**Your collaborator** is one classmate of your choice, from your own lecture, from any group. Agree on who it is before the walk-through starts. Each prototype gets about **twelve minutes**.

**The owner** opens the prototype on their own laptop, 390 px wide, shows the invented data in `prototype/README.md`, and hands over the laptop. Then the owner **watches, does not explain, does not help**, notes each run on paper, and types the runs in right after the turn.

**The collaborator** reads the steps aloud, does exactly what they say, and says what they see. They run **at least four** of the owner's test cases, at least two of them from the main flow.

<!-- Ring at 12-minute marks. Push at 11:00, or right after your own turn. -->

---

<h1 align="center">WHAT YOUR COLLABORATOR SAYS,<br>YOU WRITE BY HAND.</h1>

<p align="center"><b>Your paper notes. The notes in <code>walkthrough_04.json</code>. The sentence you quote. Your decisions.<br>No assistant. Not to write them. Not to translate them. Not even for the grammar.</b></p>

<h1 align="center">THE FEEDBACK COMES FROM YOUR COLLABORATOR,<br>AND FROM NOBODY ELSE.</h1>

<p align="center">Your English or Turkish is not graded. A person reads every record.</p>

<!-- Instructor: read it aloud once, and leave it on the screen for a few seconds before moving on. -->

---

## Pass, fail, blocked

| Result | Meaning | Note |
|---|---|---|
| `pass` | the collaborator saw what "expected" says | a few words |
| `fail` | they did not | what they saw instead |
| `blocked` | it cannot be checked on a prototype, such as "the code arrives within one minute" | why; it is checked on the real system from Week 5 |

A screen that does not exist yet is a `fail`.

**Nobody loses points for a fail.** The points are for running the test cases honestly, and for what you do about each fail.

---

## Listen for what no test case covers

*"I looked for a way to cancel the booking."*

No test case covers it, because no requirement asks for it. That is exactly what the walk-through is for.

Write it in a note. By Saturday you decide: it becomes a requirement, with a new id and a Change log line, or you write down why not.

---

## After the walk-through — by the end of the lecture (11:45)

**`week04/group_04.json`**: one entry, your collaborator, role `collaborator`, their student number (not yours), and **the most useful thing they found or said, quoted**, in their words, typed by you. They do not have to name you back.

`accepted` and `why` can wait until Saturday, when you know what you changed.

```bash
python .github/check_deliverables.py
git add .
git commit -m "week04: prototype, test cases, walk-through"
git push
```

The last push is at **the end of the lecture (11:45)**. Right after it I freeze every repository.

---

## By Saturday — fix, run again, update

- **Fix every fail.** Usually the prototype changes; sometimes the test case or the requirement was wrong.
- **Round 2 with your collaborator, online.** Share your screen; your collaborator reads the steps of each failed test case, and you click exactly what they say: `"round": 2` in `walkthrough_04.json`, written by you. Your group meeting is the natural place if they are in your group; otherwise any call you both choose.
- **Update `requirements.json` and `test_cases.json`.** Each change gets one dated line in the Change log, with the ids:

`2026-10-13 — REQ-011 added: my collaborator looked for a way to cancel a booking and found none; TC-011-01 written.`

---

## By Saturday — the whole flow

Every functional `must` requirement has a screen that serves it. **At least seven screens.** Colours and fonts do not matter; the flow does.

**End of Week 5: `requirements.json` + `test_cases.json` = your baseline.** After that, a change goes through a change request.

From Week 5 your test cases become automated tests, and each test's name carries its id: `test_TC_002_02_busy_slot_is_refused`.

---

## S1 — open your developer account today

The identity check takes **from one day to a week**, and no later step can start without it.

| Store | Fee | How long |
|---|---|---|
| Google Play | ≈ 25 $, once | a few days |
| Huawei AppGallery | free | 1–2 working days |
| Samsung Galaxy Store | free | a few days |
| Apple App Store | ≈ 99 $, every year | a day or two after payment |

**Google Play:** a new personal account confirms once on a **real Android phone** with the Play Console app; an emulator is not accepted. No Android phone? Borrow a classmate's for one minute.

---

## `week04/store.json` — and your data

Fill in the store, the date you applied, your developer name, and the status: `applied` is enough this week.

Save a **screenshot** of your developer console or your application in `week04/`. **Cover your address, your ID number and any card details** before you save it.

**Never a password, a card number or an ID number anywhere in the repository.**

The fee is your decision. Huawei AppGallery and Samsung Galaxy Store cost nothing.

---

## By Saturday — the AI log, `week04/ai_log_04.md`

**Acceptance criteria first.** Choose one screen that your assistant built.

1. The REQ lines and the test case ids you wrote down **before** the prompt.
2. The answer, measured against each of them: what it met, what it broke, what it added.
3. What you changed: the prompt, the screen by hand, or `requirements.json`.
4. The exchange, pasted, under `ME:` and `AI:`.

**Write the log yourself: the AI log is written by a human.** Your words plain, the assistant's words bold and only where they must come from it. Outside the Evidence block and those bold quotes, no assistant, not even for the English. A log written by an assistant earns 0.

---

## How Week 4 is graded — 10 points

| | Points | What |
|---|---|---|
| End of lecture (11:45) | 5 | prototype, test cases, walk-through, a quoted finding from your collaborator |
| Saturday checker | 2 | round 2, updates, seven screens, S1, the AI log |
| Human involvement | 2 | the AI log; what your collaborator said, written by you by hand; real findings, real decisions |
| Commit discipline | 1 | several lecture pushes (at least 3); several commits as you work |

The collaborator you name earns 10 % of your week's mark; so do you, for the tests you run for the classmate who names you. S1 also counts for the store bonus.

---

## Next week: design and the first real code

**Week 5:** the design and the API contract (the list of what your server answers, and how), the server skeleton, and the login by e-mail code working end to end.

At the end of Week 5, your requirements and test cases become your **baseline**.

---

## Housekeeping — leftovers from the first template

A repository created before 26 September still carries these. Nothing reads them any more, so unless you put something of your own in them, delete them all.

- `requirements/` → now `weekNN/requirements.txt`
- `docs/` → now `AI_Doc1`–`AI_Doc4` and `AI_Doc2_media` at the root
- `SETUP_CARD_EN.md`, `SKELETON.md`, `WEEKLY_WORKFLOW_STUDENT_EN.md` → now with `AI_` in front
- `CURRENT_WEEK.txt` → the checker reads the course's copy online; yours is inert

```
git rm -r --ignore-unmatch requirements docs CURRENT_WEEK.txt \
  SETUP_CARD_EN.md SKELETON.md WEEKLY_WORKFLOW_STUDENT_EN.md
git commit -m "remove leftovers from the first template"
```

---

## Two rules about the room

**One student, one computer, one GitHub account.** Work done on a classmate's machine or under a classmate's session earns nothing for the lecture. In the walk-through your collaborator uses your laptop, and everything written into your repository is written by you.

**Not registered in the attendance system = absent.** The lecture slot's five points are then gone, whatever was pushed.

---

## Now

Run the checker. `week04/prototype/` arrives.

**Replace the [bracketed] parts, then build your main flow from `home.html`.**

<!-- Start the clock. Build until about 10:30, walk-through until about 11:30, files and push until 11:45. Freeze right after 11:45: push.md block 3. -->
