# AIASD · Week 3 — Pitch, Review, Proposal Part B

*Atlas University · Fall 2026–27 · Prof. Dr. Vedat Coşkun*
*Presented from this page. Scroll one section at a time; each `---` is a slide.*

<!-- Instructor: zoom the browser to 150 % and collapse the GitHub header (press "." for
the editor view if you prefer a cleaner page). Timings in the notes. Total ≈ 3 h:
10 min intro · 50 min review round · at least 30 min settling the project (title, §3–§4) · 20 min screens · work until 11:45 · freeze right after 11:45. -->

---

## Today

1. Week 2 — how it went
2. Two rules that stay for the whole term
3. **Today your project becomes final: its title and its content**
4. What a pitch is, and why you wrote one
5. The review round — groups of four, first hour
6. After the round: three reviewers, a revised proposal, a change log, the screens of your main flow
7. By Saturday: Part B, the store, the hostile reviewer
8. How the week is graded

---

## Week 2 in numbers

| | English | Turkish |
|---|---|---|
| Registered | 78 | 33 |
| Pushed during the lecture | 62 | 26 |
| Lecture slot 5 / 5 | 42 | 21 |
| Saturday: checks all green | 57 | 21 |

Marks and the checker's remarks reached you as an **issue in your own repository** on
Sunday. Questions about a mark go there, as a comment — not by e-mail.

---

## Two rules that stay for the whole term

**1. The project solves a problem of *yours* — your own, your friends' at the
university, or your social circle's.**
Not "students struggle with X". The last time it happened — to you, or in front of you:
date, place, who, what they did instead.

**2. Real people around you can use it.**
At Atlas, in your family, in a club. In Week 9 five of them test it — the User
Acceptance Test. You name them today.

If you cannot name the last time, or the five people: the problem is the project, not
the slide. **Change the project in this lecture:** at the end of the lecture (11:45) it becomes fixed.

---

## Today your project becomes final

**At the end of the lecture (11:45): its title and its content.** The same title, the same problem and the same product until the end of the term.

Its details may still change: features, requirements, scope. Each change gets a line in the Change log. The project itself may not change.

**This is the most important decision of the term. Give it time.** Test the project in the review round; then take at least half an hour to settle §1 (the title) and §3–§4 (the problem and the product), with your group's answers in front of you.

Only a project that turns out to be technically impossible can change after today, and only with my written approval in an issue.

---

## What a pitch is

A pitch is a short, ordered, concrete case for an idea, made to someone who decides
something — money, time, a yes.

- **Short**, because attention is the scarce resource.
- **Ordered**: problem → solution → who → why you → what you ask.
- **Concrete**: numbers, names, one example. Adjectives are not evidence.

> "An innovative platform for everyone" is not a pitch.
> "3,000 students use the Atlas library each term; one in six walks away without a room;
> StudyRoom shows the free one and books it in 30 seconds" is.

---

## The same thing, with 2.5 million euros behind it

**EIC Accelerator** — the European Union's grant for start-ups (Horizon Europe).

Step 1 of the application is exactly this: a **pitch deck of at most 10 slides**, a
**3-minute video**, a short form. Hundreds of applications are filtered on those three
things. The ten slides: problem · solution · why now · market with numbers · competitors
and your edge · business model · roadmap and risks · team · the ask · next step.

Your six slides today are the first half of that list. Part B of the proposal, due
Saturday, is the second half. The December defence is a small jury.

---

## Your six slides — `week03/PITCH_03.md`

1. The product in one sentence
2. **The last time it happened — to you, or in front of you**
3. **Five people who will test it in Week 9** — name, how you know them, why
4. Three requirements — *the same id and text as `requirements.json`* — and one "does not"
5. The main screen, **drawn by hand**
6. The one thing you are not sure about

Slide 7 is fixed: the three questions your reviewers answer.

**Written by you, no AI.** Everything on it is your life and your people. I will ask
about any slide.

---

## Presenting from your laptop

Open `week03/PITCH_03.md` in VS Code.

- With the **Marp for VS Code** extension: the preview button (top right) shows slides;
  the same button exports PDF or PPTX.
- Without it: VS Code's normal Markdown preview (`⌘⇧V` / `Ctrl+Shift+V`) — scroll one
  slide at a time. Good enough.
- Not from GitHub's website: you will edit the file after the round.

<!-- Show both on the projector with the test student's PITCH_03.md: Marp preview, then
plain preview. 2 minutes. -->

---

## The review round — groups of four

**Form your group of four now, yourselves.** It stays with you for the term, so choose people you can meet online once a week. Left over when the class does not divide into fours? Join a group: it becomes five. No groups of three.

**Write your group in `week03/group_03.json`:** the numbers of all members, yours included. Every member writes the same list. If the lists differ, every member of the group loses one point.

Each person: **5 minutes** presenting, from your own laptop. The other three listen,
then **write** one sentence for each of the three questions and hand it over — paper or a
text file. Then the next person. Four rounds, about **45 minutes**.

Reviewers: say what you think. "It's good" helps nobody and earns nobody anything.

<!-- Give them three minutes to form groups; nudge the leftovers together. Walk around. Ring at 12-minute marks. -->

---

## The three questions — slide 7

1. **Real?** Did they convince you this problem happens to them, and to the five people
   on slide 3?
2. **Usable here?** Could those five people actually use this in Week 9 — what would
   stop them?
3. **Too much or too little?** Which part will not be finished by Week 11 — or has the
   product shrunk to one screen?

One sentence each. The presenter copies your sentences into their repository — your name
goes next to them, and you earn the contributors' bonus for them.

---

## After the round — by the end of the lecture (11:45)

**`week03/contributors_03.json`** — your three reviewers, role `reviewer`, student numbers, and for each **the most useful sentence they wrote, quoted**. Then `accepted: true/false` and `why`. Rejecting with a reason is fine; "they said, I changed" with nothing behind it is not.

**`PROPOSAL.md`** — go over §1–§7 with the three answers in front of you. Every change gets **one dated line in the Change log** at the end of the file:

`2026-10-06 — §4: dropped group chat; two reviewers said nobody would use it next to WhatsApp.`

A proposal may change. It may not change silently. **Settle §1 (the title) and §3–§4 now: at the end of the lecture (11:45) they become final.**

---


## The screens of your main flow — `week03/screens_03.md`

The path a user takes, from logging in to the one thing your app exists for.

| # | Screen | What the user does there | Requirements |
|---|---|---|---|
| 1 | Log in | enters the e-mail address and the 4-digit code | REQ-001, REQ-006 |
| 2 | Today's rooms | sees which rooms are free, hour by hour | REQ-002, REQ-003 |
| 3 | Book a slot | picks a free slot and confirms it | REQ-002 |

**At least five screens**, the login included. If you cannot name five screens and the requirements behind them, the project is not ready yet: find that out today. In Week 4, each row becomes one screen of your prototype.

---

## If you have time left

- Read the acceptance criteria of each other's `must` requirements. Mark every one that a tester could not check, such as "users are satisfied".
- Agree on the day and the tool of your weekly one-hour online meeting.
- Start Part B: §8, and the store choice in §12, while I am here to answer.
- Your store choice is firm? You may already open the developer account (S1). The identity check takes days; S1 is marked in Week 4.

---

## This group stays — every week, one hour online

From **Week 4**: the four of you meet **online, one hour, between the lecture and
Saturday**. Teams, Meet, Discord — your choice.

Each of you: what changed in your project this week. The other three: what they think.

Your **three contributors every week** are these three people — their sentences, quoted,
and what you did about them, in `weekNN/contributors_NN.json`.

Nobody can write that for someone who was not there. First meeting: this week, if you like.

---

## Requirements — ids stay, the list stays open

`requirements.json` may still change: add, reword, drop (the id stays, `"dropped": true`).

**From Saturday an id never changes its meaning.** `REQ-004` must mean the same thing in December.

**The list stays open until the end of Week 5.** In Week 4 you walk through test cases from your acceptance criteria on the clickable prototype; what is missing goes in, with a change-log line.

**End of Week 5: requirements + test cases = your baseline.** After that, changes go through a change request.

REQ-001 (e-mail-code login) and REQ-006 (390 px phone screen) stay as they are for everyone.

---

## Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week03: pitch, review, proposal revised, main flow"
git push
```

Push after the round, and at the end of the lecture, **11:45**. Right after it I
freeze every repository. What is not pushed does not exist.

Push times this term: **10:00, 11:00 and the end of the lecture (11:45)** — and whenever you finish something.

---

## By Saturday 23:59 — Part B, §8–§12

The half that says why it is worth building. WHY / WHAT / weak / strong inside each
section of `PROPOSAL.md`.

- **§8 Market** — who, how many, how you know. Your five testers are the first row.
- **§9 Competitors** — three things that solve it today. A paper list counts.
- **§10 Comparison** — a small table on the *user's* criteria, one sentence.
- **§11 Commercial potential** — how it pays for itself; "no commercial intent, the value
  is X" is honest if argued.
- **§12 Risks** — three things that stop you by Week 11, plan and fallback each. **Name the
  store** (S0): fee, review time. Read `AI_PLATFORMS_AND_STORES_EN.md` first.

---

## By Saturday — the hostile reviewer, `week03/ai_log_03.md`

This week the assistant plays the investor who wants to say **no**.

1. Give it your Part B. Ask for the three strongest objections, specific to your proposal.
2. One objection is **right**: answer it in the proposal, log it in the Change log.
3. One is **wrong**: show why — a number, a source, a thing you checked.
4. Paste the exchange.

"It gave useful feedback" earns nothing. Telling a good objection from a bad one is the
skill.

**Write the log yourself.** Outside the Evidence block, no assistant, not even for the
English. Your language is not graded; a log written by an assistant earns at most 1.

---

## How Week 3 is graded — 10 points

| | Points | What |
|---|---|---|
| End of lecture (11:45) | 5 | pitch complete, three reviewers with real sentences, change log started, five screens listed |
| Saturday checker | 2 | §8–§12 filled, store named, ai_log with three objections |
| Human involvement | 2 | the ai_log and its evidence; reviews with real decisions behind them |
| Commit discipline | 1 | several lecture pushes (at least 3); several commits as you work |

Contributors' bonus: each reviewer you name earns 10 % of your week's mark; so do you, for the reviews you give.

---

## Next week: prototype and test cases

**Week 4:** a clickable prototype of your main flow, and test cases written from your acceptance criteria.

Your group runs the test cases on the prototype; what does not work shows what is missing from the requirements.

**Before next week:** read your acceptance criteria again. Rewrite every criterion that does not say what a tester should see.

---

## Two rules about the room

**One student, one computer, one GitHub account.** Work done on a classmate's machine or
under a classmate's session earns nothing for the lecture. Bring your laptop charged.

**Not registered in the attendance system = absent.** The lecture slot's five points are
then gone, whatever was pushed.

---

## Now

Groups formed. Laptops open, `PITCH_03.md` in the preview.

**First presenter in each group: start.**

**At the end of the lecture (11:45) your project's title and content become final.** Take the time it needs.

<!-- Start the clock. Walk around. After the round: slide "After the round" stays on the
projector until 11:35; "Push" from 11:35. Freeze right after 11:45: push.md block 3. -->
