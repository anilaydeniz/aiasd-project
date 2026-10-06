# Week 3 Assignment — Pitch, Review, Proposal Part B

**Due:** lab part pushed by the end of the lecture (11:45) · the rest Saturday 23:59 · Commit to your project repository

> **Before the lecture:** your `PITCH_03.md` must be written and pushed. The first hour
> of the lecture is spent presenting it — there is no time to write it then. Bring your
> laptop charged; you present from it.
>
> **In this lecture your project becomes final: its title and its content.** You work on
> it for the rest of the term, so give this decision the time it needs, today, with your
> group. Come with your project ready to be questioned, not with a project you are still
> looking for.

Last week you decided what to build. This week three classmates tell you what they
think of it, you decide what to change, and you write the second half of the proposal —
the half that says why it is worth building and what could stop you.

---

## What arrives with this week

Run the checker once:

```bash
python .github/check_deliverables.py
```

It brings `week03/PITCH_03.md`, `week03/group_03.json`, `week03/contributors_03.json`,
`week03/screens_03.md` and `week03/ai_log_03.md`.
`PROPOSAL.md` you already have; Part B (§8–§12) and the Change log are in it, waiting.

---

## Before the lecture — `week03/PITCH_03.md`

Your five-minute pitch, six slides, in Markdown: the file **is** the deck, every `---`
is a new slide. Open it in VS Code; the **Marp for VS Code** extension shows it as
slides (preview button, top right) and exports PDF or PPTX if you want one. Without the
extension, VS Code's normal Markdown preview is enough to present from.

The six slides, each with its own instructions inside the file:

1. the product in one sentence;
2. **the last time the problem happened** — to you, or in front of you — date, place, who, what they did instead;
3. **five real people who will test it in Week 9** — name, how you know them;
4. three things it does, one thing it does not;
5. the main screen, **drawn by hand** (photo in `week03/`) or in text;
6. the one thing you are not sure about.

Slide 7 is fixed: the three questions your reviewers answer.

**Write it yourself — no AI for this file.** Not the text, not the structure. Everything
on these slides is about your life and your people; an assistant cannot know it, and I
will ask about any slide, in the group or in class. The rest of the week's work is
different: AI is a tool there, as before, and `ai_log_03.md` asks you to use it.

Two rules behind slides 2 and 3, and they stay for the whole term: **the project solves
a problem of yours — your own, your friends' at the university, or your social
circle's**, and **it is usable by real people around you** — at Atlas, in your family, in
a club — because in Week 9 those people test it, and you will need them. If you cannot
name the last time the problem happened, or five people who would use the product, the
problem is with the project, not the slide: change the project in this lecture.

**At the end of the lecture (11:45) your project becomes final for the term: its title and its content.**
The same title, the same problem and the same product until the end. Its details (features,
requirements, scope) may still change, each with a line in the Change log; the project
itself may not. This is the most important decision of the term, so give it time: use the
review round to test the project, then take at least half an hour after the round to
settle §1 (the title) and §3–§4 (the problem and the product) with your group's answers in
front of you. Ask them whether the project is real and whether it can be finished. Only a
project that turns out to be technically impossible can change after today, and only with
my written approval in an issue.

---

## In the lab — pushed by the end of the lecture (11:45)

### 1. Review round — groups of four, first hour

You form a group of four yourselves, at the start of the lecture. If the class does not
divide into fours, the students left over join a group, which then has five members; do not
form a group of three. **Then every member writes the group into `week03/group_03.json`**:
the student numbers of all members, your own included. Every member writes exactly the same
list. After the lecture I compare the lists, and if they are not the same, every member of
the group loses one point of the end-of-lecture mark. Each person presents for five minutes from their own
laptop; the other three listen, then **write** one sentence for each of the three
questions on slide 7 — on paper or in a text file, handed to the presenter. Four rounds,
about 45 minutes. Say what you think; a polite "it is good" helps nobody and earns nobody
anything.

**This group is your group for the rest of the term.** From Week 4 the four of you meet
**online for one hour every week, between the lecture and Saturday** — Teams, Meet,
Discord, whatever you like — and each of you presents what changed in your project that
week; the other three say what they think. The three entries in your
`weekNN/contributors_NN.json` come from that meeting from then on: who said what, quoted,
and what you did about it. Nobody can write those three entries for someone who was not
there, so missing the meeting shows by itself. You may hold the first one this week
already.

### 2. `week03/contributors_03.json` — three reviewers

Your three reviewers are the three other members of your group (in a group of five,
three of the four). Role `reviewer`, student numbers, and for each **the most useful
sentence they wrote** — quoted, not summarised. Then `accepted: true` or `false`, and
`why`. Rejecting advice with a reason is fine; accepting everything without a trace of
what changed is not. Each reviewer you name earns the contributors' bonus, as last week.

### 3. `PROPOSAL.md` — Part A revised, Change log started

Go back over §1–§7 with the three answers in front of you and change what the review
changed. Every change gets **one dated line in the Change log** at the end of the file:
what changed, in which section, why — "2026-10-07 — §4: dropped group chat; two
reviewers said nobody would use it next to WhatsApp". A proposal is allowed to change;
it is not allowed to change silently.

`requirements.json` may change this week too — add, drop (keep the id, set
`"dropped": true`), reword. **From Saturday an id never changes its meaning**; the list
itself stays open until the end of Week 5, when it becomes your baseline after the
prototype review.

### 4. `week03/screens_03.md` — the screens of your main flow

Your main flow is the path a user takes, from logging in to the one thing your app exists
for. List its screens in order, at least five with the login included. For each screen,
write in a few words what the user does there, and name the requirements that the screen
serves. For StudyRoom: Log in · Today's rooms · Book a slot · My bookings · Check in.

This is where the project becomes concrete. If you cannot name five screens and the
requirements behind them, the project is not ready yet, and it is better to find that out
today, with your group next to you. In Week 4 each row becomes one screen of your
clickable prototype.

**If you have time left** after the screens, use it in your group:

- read the acceptance criteria of each other's `must` requirements, and mark every one
  that a tester could not check (item 8 below);
- agree on the day and the tool of your weekly one-hour online meeting;
- start Part B, especially §8 and the store choice in §12, while I am in the room to answer.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week03: pitch, review, proposal revised, main flow"
git push
```

Push after the review round, and again at the end of the lecture, **11:45** — the usual 10:00 / 11:00 / end of the lecture (11:45). Right after it I freeze every repository. What is not pushed does not exist.

---

## By Saturday 23:59

### 6. `PROPOSAL.md` — Part B, §8–§12

The half that says why it is worth building. Each section has a WHY, a WHAT and a
weak/strong pair inside the file; the StudyRoom examples continue.

- **§8 Market and target users** — who, how many, how you know. Your five testers from
  slide 3 are the first row of this section.
- **§9 Competitors** — three things that solve the problem today; a paper list counts.
- **§10 Comparison and your advantage** — a small table, the user's criteria, one sentence.
- **§11 Commercial potential** — how it pays for itself; "no commercial intent, the value
  is X" is an honest answer if you argue it.
- **§12 Technical risks** — three things most likely to stop you by Week 11, with a plan
  and a fallback each. **The store you choose (S0)** is named here, with its fee and its
  review or test-track time: read `AI_PLATFORMS_AND_STORES_EN.md` before you decide. If
  your choice is firm, you may already open the developer account this week (S1, marked
  in Week 4), because the identity check takes from one day to a week.

### 7. Use AI as a hostile reviewer — `week03/ai_log_03.md`

This week the assistant plays the investor who wants to say no. Give it your Part B and
ask for the three strongest objections. Then **answer one of them in the proposal** and
**show one objection to be wrong** — with evidence: a number, a source, a thing you
checked. Paste the exchange. A log that says "it gave useful feedback" earns nothing.

### 8. Get your acceptance criteria ready for Week 4

In Week 4 every acceptance criterion in `requirements.json` becomes a test case, and the
members of your group run those test cases on your clickable prototype. A criterion that
nobody can check, such as "users are satisfied", cannot become a test case. Read your
criteria again this week and rewrite the ones that do not say what a tester should see.
This is not marked this week; next week it is the starting point.

### 9. Push again, checks green

Several commits as you work, each with some new work in it and a message that says what changed; a commit does not need to be a finished part. Everything the checker
asks for is listed below.

---

## Deliverables checklist

**Before the lecture**
- [ ] `week03/PITCH_03.md` — six slides filled, written by you, pushed

**In the lab, by the end of the lecture (11:45)**
- [ ] `week03/group_03.json` — the numbers of all members of your group, the same list as theirs
- [ ] `week03/contributors_03.json` — three reviewers from your group, a quoted sentence each, accepted/why
- [ ] `PROPOSAL.md` §1–§7 revised where the review changed them
- [ ] `PROPOSAL.md` Change log — at least one dated line
- [ ] `week03/screens_03.md` — at least five screens of the main flow, each with what the user does there and its REQ ids
- [ ] Your project's title and content are final: from this push on, only its details may change

**By Saturday**
- [ ] `PROPOSAL.md` §8–§12 filled; §12 names the store, its fee and its review time
- [ ] `week03/ai_log_03.md` — three objections, one answered in the proposal, one shown wrong, exchange pasted
- [ ] `requirements.json` updated — from here an id never changes its meaning
- [ ] Checks green on GitHub; Weeks 1–2 still pass

---

## Not this week

No code, no prototype yet (Week 4), no design documents yet (Week 5), no environment
set-up. Naming the store in §12 is enough; opening the developer account (S1) is
optional this week and marked in Week 4.

---

## How this week is graded

**End of the lecture — 5 points.** Pitch pushed and complete, the group listed, three
reviewers with real sentences, Change log started, the screens of the main flow listed —
read from your repository as it stands at the end of the lecture (11:45). A group whose members did not
write the same list loses one point, every member.

**Saturday 23:59 — 5 points.** Checks green on your final state: **2**. Human
involvement: **2** — your `ai_log_03.md` with its evidence, and reviews with real
sentences and real decisions behind them. Commit discipline: **1** — several pushes at
different times in the lecture (at least three) and several commits as you work, each with some new work in it.

**Contributors' bonus.** Each reviewer you name earns 10% of your week's mark; you earn
the same for the reviews you give. From Week 4 the names are your group.

**One student, one computer, one GitHub account.** Work done on a classmate's machine or
under a classmate's session earns nothing for the lecture.
