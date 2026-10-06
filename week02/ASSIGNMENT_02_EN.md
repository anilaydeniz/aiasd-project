# Week 2 Assignment — Proposal Part A + Requirements

**Due:** Saturday 23:59 · Commit to your project repository

> **Before the lecture** read `AI_PLATFORMS_AND_STORES_EN.md` at the root of your
> repository — the choice of stack starts this week.

This is the week you decide what you are building. You will live with the decision
for ten weeks, publish it on a store, and defend it in December — so the proposal is
not a formality. It is the first document the checker reads every week from now on.

---

## What arrives with this week

Run the checker once, **before you write anything**:

```bash
python .github/check_deliverables.py
```

It brings this week's files into your repository: `PROPOSAL.md` at the root and, in
`week02/`, `SRS.md`, `requirements.json`, `contributors_02.json`, `ai_log_02.md` — plus any
course document that changed at the root. Every one of them is a scaffold. Read the
instructions in it before you write: each section says **what** to write and shows a
**weak** and a **strong** example, all for one invented project ("StudyRoom", booking a
library study room) so you can see how the documents fit together. It is not your project
— write about yours. Fill the files in; do not rename them. (Offline, or if it does not
work: `git fetch template && git checkout template/main -- week02 PROPOSAL.md` does the
same, see the setup card.)

---

## In the lab — pushed before the lecture ends

### 1. `PROPOSAL.md` — Part A, §1–§4

Title, one-paragraph summary, problem, solution. Each heading gives an ideal length; it is
a guide, not a limit — write more if your idea needs it. The comments are invisible on GitHub and not counted, so
you may leave them in place while you write. Write §3 first, then §4; leave the §2 summary
and the §1 title for last — you can only summarise what you have already written. Two things the lecture will show you side by side and
that the checker cannot see but I can: a problem written as a concrete situation beats
three general claims, and a solution that says what it **does not** do is the one that
gets finished.

The product has three mandatory parts — a **mobile app, a web client and a server**,
with login by e-mail code or OTP — and it is published on a **public app store** by
Week 11. Choose something you care about and that fits in ten weeks; you can always add
in Week 10, you can never subtract in Week 11.

### 2. Pitch it to two classmates — `week02/contributors_02.json`

Tell two people in the room what you are building, in two minutes, from §1–§4. They
are your first **stakeholders**: they ask what it is for, what it does not do, and what
they would need from it. Write their student numbers in `week02/contributors_02.json`
with role `stakeholder` and **one sentence each on what they actually said** — a
question they asked, a feature they wanted, an objection. Two numbers with nothing
behind them is a list, not evidence, and it earns neither you the human-involvement
points nor them the bonus.

They must be two different people from anyone you will name next week. Rotate.

### 3. `week02/requirements.json` — the first list

At least **8 requirements**: at least **5 functional** (what the system does — "a student
books a free slot") and at least **3 non-functional** (how well — speed, security,
privacy, capacity; always with a number). Each one has an id `REQ-001`, `REQ-002` …, a
`description` of one testable behaviour, and `functional: true/false`. The scaffold
explains every field at the top.

Two are the same for everyone and already filled in: **REQ-001 login by e-mail code** and
**REQ-006 usable on a phone screen**. Keep them; adjust the wording to your product if you
need to. Requirement ids never change after this week; the design, the tests and the
traceability matrix all point at them. A requirement you drop later keeps its id and gets
`"dropped": true`.

In the lab, the descriptions are enough. By Saturday every requirement also gets:

- `priority` — `must` (the product is pointless without it), `should` (important, cut only
  if time runs out) or `could` (nice to have). Not everything is a must: deciding what
  could be cut is the point of the field, and the checker fails a list that is all musts.
- `acceptance` — the test that proves it is met: what you do and what you must see.
  *"Enter the code from the e-mail within 10 minutes: logged in. A wrong code three times:
  locked for 15 minutes."* It is the test you will actually run in Week 9, so write one
  you can run.

### 4. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week02: proposal part A, stakeholders, first requirements"
git push
```

At the end of the lecture I freeze every repository. What is not pushed does not exist.

---

## By Saturday 23:59

### 5. `PROPOSAL.md` — §5–§7

**§5 How it works** must name the three pieces — mobile, web, server — say where data
lives and how login works, and carry a **system context diagram** in Mermaid directly
under the heading: your system as one box, every actor and external service around it.
**§6 Technologies**: one line per layer, only things you will install this term (`AI_PLATFORMS_AND_STORES_EN.md`
tells you what your laptop and phone allow). **§7 Success criteria**: three to five
statements someone can measure in December — each names a user, an action and a number.
"It works" is not one.

Also in `requirements.json`: a `priority` and an `acceptance` test for every requirement
(see step 3).

### 6. `week02/SRS.md`

The requirements as a document: purpose and scope, actors, at least **three use cases**,
one **use case diagram** in Mermaid under the use-case heading, then the functional and
non-functional requirements — the same ids as `requirements.json`, nothing more and
nothing less, each with its priority and acceptance test — and your constraints. A page or
two, not thirty.

Write each use case in the shape the scaffold shows: a name, the actor, the requirements
it covers, the **main flow** in three to six numbered steps, and **what can go wrong**.
The last part is the one people skip, and the one that finds the missing requirements.

### 7. Use AI to draft — then catch it being wrong — `week02/ai_log_02.md`

Ask two different assistants to draft requirements for *your* project from your §1–§4 —
eight of them, with priorities and acceptance criteria. Give both the same prompt (the
scaffold suggests one). They will produce requirements that sound authoritative and
are wrong for your product — invented features, data you do not have, constraints that
contradict your §4. **Document one such error**, paste the exchange in the Evidence
block, say how you noticed and what you changed. A log that says the AI was helpful and
nothing else earns nothing; so does an empty Evidence block.

### 8. Push again, checks green

```bash
python .github/check_deliverables.py
git add .
git commit -m "week02: proposal part A complete, SRS, requirements"
git push
```

Commits spread across the week, with messages that say what changed. One push on
Saturday night costs the commit-discipline point.

---

## Deliverables checklist

**In the lab**
- [ ] `PROPOSAL.md` §1–§4 filled, headings untouched
- [ ] `week02/contributors_02.json` — two stakeholders, numbers and one sentence each
- [ ] `week02/requirements.json` — ≥8 entries, `REQ-NNN` ids, ≥5 functional, ≥3 non-functional

**By Saturday**
- [ ] `PROPOSAL.md` §5–§7 filled; §5 names mobile, web and server and has its Mermaid diagram
- [ ] `week02/requirements.json` — every requirement has a `priority` (not all `must`) and an `acceptance` test
- [ ] `week02/SRS.md` — actors, ≥3 use cases with main flow and what can go wrong, use case diagram, requirements with the same ids
- [ ] `week02/ai_log_02.md` — one documented AI error, the pasted Evidence block, how you noticed
- [ ] Checks green on GitHub; Week 1 still passes
- [ ] At least three commits across the week

---

## Not this week

No code, no API keys, no Ollama. Part B of the proposal — market, competitors,
commercial potential, technical risks and **the store you choose** — is next week,
together with the design. Do not write it now; you will change your mind after the
design, and the change log exists for exactly that.

---

## How this week is graded

**End of the lecture — 5 points.** §1–§4, the two stakeholders, the first requirement
list — read from your repository as it stands when the lecture ends, and shown on the
class board.

**Saturday 23:59 — 5 points.** Checks green on your final state: **2**. Human
involvement: **2** — your own `ai_log_02.md` with its evidence, and the two stakeholders
with a real sentence behind each name. Commit discipline: **1**.

**Contributors' bonus.** Each stakeholder you name earns 10% of your week's mark; you
earn the same for the pitches you listen to. At most two a week, and at least one new
name every week — the point is that the whole class hears the whole class.

An LLM can write every section of this proposal. What it cannot do is know which of its
sentences are wrong about your idea, or make the proposal agree with the design you
will write next week. That is what is being assessed.
