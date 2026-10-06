# Weekly Workflow — What You Do Each Week

**AI-Assisted Software Development · Atlas University · Fall 2026–2027**

**Version 1 · 20 September 2026** — this document is revised during the term. It is
delivered together with the rest of each week's files when you fetch them (to "fetch"
or "pull" means to ask git to download the newest files from GitHub into the copy on
your computer), so the copy in your repository (the folder of your project that git
tracks, both on your computer and on GitHub) is the current one as long as you keep
pulling.

> [!IMPORTANT]
> **What changed in this version**
>
> Nothing has changed yet, because this is the first version. When I revise this
> document, this box lists what moved, and the headings that changed carry a
> **`↻ changed in v2`** mark beside them. Both disappear in the version after that one,
> so anything that is marked is new to you.

This document describes the routine that does not change. The *content* of each week
differs, because each week's assignment arrives in that week's folder, but the *rhythm*
is always the same.
Come back here when you are stuck.

---

## At a glance

| When | What you do | Points |
|------|-------------|--------|
| Before the lecture | Read `weekNN/ASSIGNMENT_NN_EN.md` | — |
| During the lecture (3 h) | Work, and push often (a push sends your saved work from your computer to GitHub) | — |
| End of the lecture | Make one last push; right after it I take a snapshot (a copy of your repository exactly as it is at that moment) | 5 |
| After the lecture | Finish the rest and write `ai_log_NN.md` | — |
| By Saturday 23:59 | **Push again.** I take a second snapshot of your repository | 5 |

Each week is worth ten points, split evenly between two moments: **five measured at the
end of the lecture, five at the Saturday deadline.** Both halves are read from GitHub, so
both need a push (a push is the `git push` command, which sends the commits on your
computer to your repository on GitHub). **Week 1 is the one exception:** it is worth five
points, nothing is read at the end of the first lecture, and all five are read from your
repository at Saturday 23:59. Work that is finished but not pushed scores exactly the
same as work that was never done.

It is deliberate that half the week's mark depends on the lecture. The lecture is where
the work belongs: you are in the room, and you can still ask questions. The other half
rests on finishing the week's work, and on two things that a checker (the automatic
script that looks for the files each week requires; §2 shows how to run it) cannot see.
§3 describes those two things.

**The deadline is the same every week: Saturday 23:59.** There is nothing to work out,
because whatever is in your repository at Saturday midnight is what I grade. Most of the
work should happen in the lab, where you can ask questions; the days after the lecture
are for closing gaps, not for starting.

---

## Once, and never again

Three things have to be true before the first lecture starts, and none of them is part
of the course content: (a) you have a GitHub account, (b) you have your repository, and
(c) you have a computer that is allowed to push to that repository. The required
commands are on the [**Setup Card**](AI_SETUP_CARD_EN.md). The card has four steps, and
the last step tells you whether the other three worked.

The card also carries a table of the errors you are most likely to hit and of what each
one actually means. Keep it open; it is probably the only page you need for the
mechanics of git and GitHub.

---

## 1. Before the lecture of that week

Read `weekNN/ASSIGNMENT_NN_EN.md`. It comes down with the rest of the week's folder and
lists exactly which files that week requires. 

If there is pre-reading, read it before you arrive. 

---

## 2. During the lecture

### Know which half you are working on

From the root of your repository (the top folder of your project, the one that contains
the `.github` folder), run:

```bash
python .github/check_deliverables.py
```

It answers in two parts:

```
In the lab:     11 of 14 done
By Saturday:     0 of  3 done
```

The numbers above are only an example; the real numbers change from week to week. What
matters is which of the two lines you are reading.

**In the lab** is the line that I read at the end of the lecture, and it is worth half
the week's mark. These items are worth doing while you are in a room with me and with,
say, twenty-nine other people who are stuck on the same thing.

**By Saturday** is the rest of the week: the write-ups, the diagrams and `ai_log_NN.md`
(your weekly log of the work you did with the AI assistant; §3 explains it). This is
work that you genuinely do alone. It does not make the check fail during the week,
because it is not due yet; but it is the other half of the mark, and the Saturday
snapshot does read it.

If you find yourself writing `ai_log_NN.md` during the lab, you have the week backwards.

### Work, and push often

Commit as the work progresses (a commit is one saved step in git's history, made with
`git commit`), rather than committing everything in one enormous lump at the end. The
message of each commit should say what you did:

```bash
git add .
git commit -m "week01: hello.py reads a name and prints the list"
git push
```

A message such as "update", "fix" or "asdf" says nothing about what happened, and
messages like these cost you the commit-hygiene point (the point for commit discipline
that §3 describes).

**Push at 10:00, at 11:00 and at the end of the lecture (11:45)**, which means at least three pushes in every lecture,
whatever state the work is in. At 10:00 and at 11:00 I look at the class board (the
projected table that shows where every student's repository stands) to see where
everyone is; the push at the end of the lecture (11:45) is the one that counts for the lecture's points. A push
costs nothing, and a half-finished section that is pushed is worth more than a finished
one that is not.

### Run the checks yourself

Run the same command, as often as you like:

```bash
python .github/check_deliverables.py
```

These are exactly the checks that I will run. The output lists what is missing, one line
at a time. It is not a grade; it is a to-do list, and running it costs nothing.

### Push once more before the lecture ends

The last push is at the end of the lecture (11:45). Right after it, I freeze every repository as it stands (I
take a snapshot, a copy of the repository exactly as it is at that moment) and I run the
checks on that snapshot. Work that you have not pushed is invisible: it sits on your
laptop and does not count.

The result is projected as an anonymised table (a table in which nobody's real name
appears); find your row by the nickname in your `student.json` (the file in your
repository that holds your details, including the nickname you chose). That table is
worth **5 points — half the week**.

One student works on one computer with one GitHub account. Work done on a classmate's
machine or under a classmate's GitHub session earns nothing for the lecture.

**Commit discipline (1 point a week) is judged every week.** In the lecture I look for
several pushes at different times (at least three), each with new work in it. Outside the lecture you may work in one sitting; what I
look for is several commits made as you work, each with some new work in it and a message
that says what changed. A commit does not need to be a finished part. I ask three questions: did the work grow step by step, is there real
progress from one commit to the next, and was the text worked on or was it pasted in
finished? A single
commit at the end of the week, or text that arrives in one piece, scores nothing. When
something in a week looks doubtful, I also look back at your earlier weeks before I
decide. I may also ask you a two-minute question about your project in any lecture.
Commit as you work, every week, and this takes care of itself.

### Attendance, and what happens if you are not here

**Bring your laptop every week**, with its charger and whatever cable it needs. The
lecture is a three-hour hands-on study opportunity.

**Attendance is mandatory.** The university allows you some weeks of absence across the
term, and that allowance already covers everything, whether the reason is illness, work,
family or anything else at all. There is no second category on top of it, and there is
no make-up procedure.

**A lecture you miss is a lecture I cannot mark.** Whatever the reason, those 5 points
are gone. I do not weigh reasons against each other, and that is deliberate: with over a
hundred students, a process for judging excuses turns into a process for judging who
explains themselves best.

What stays open is the other half. Do the lecture's work in your own time, push it
before Saturday midnight, and you earn those five points exactly as everyone else does.
Missing a lecture costs you that lecture, not the week.

---

## 3. After the lecture — until Saturday 23:59

Finish the rest of the week's work by Saturday midnight. I take a second snapshot at that
time, and your state at the deadline decides the other 5 points.

### `ai_log_NN.md` — do not skip it

You write one file per week, inside that week's folder, so Week 1 has
`week01/ai_log_01.md`, and so on. The file arrives with the rest of the documents in the
week folder, and you fill it in. You write which assistant you used, what it got right,
what you had to correct, and what you learned. **You write it yourself, in your own
words**: outside the Evidence block no assistant is used, not even to correct the
language. Your English or Turkish is not graded; a log written by an assistant earns at
most 1 of the 2 points, however polished it is.

**The Evidence block is required.** Paste the actual exchange under your claim, inside
the code fence (the block between two lines of three backticks): the prompt you sent and
the wrong answer you got. Do not paste the whole conversation; paste the lines that show
the error, which is usually a short extract, call it ten or fifteen lines. A claim with
an empty Evidence block earns nothing.

Why is this required? Anyone can write "the AI made a mistake and I fixed it". A real
model output is hard to fabricate convincingly, because invented transcripts read too
cleanly and their errors are conveniently easy to spot. And choosing which part of a
long conversation counts as evidence is itself the skill that is being assessed.

If you would rather keep the whole conversation, save it as `weekNN/transcript.md`. I do
not read those files by default, but I will read yours when a log entry does not add
up.

This file is worth 2 points.

### Keep going until the checks are green

```bash
python .github/check_deliverables.py
git add .
git commit -m "week01: llm_notes written up"
git push
```

The **Actions** tab of your repository on GitHub shows the result of every push: GitHub
runs the same checks after every push, and this automatic run is called CI (continuous
integration). A green tick on your Saturday state is worth **2 points**.

### The 3 points that are not automated

**Consistency and commit discipline — 1 point.** Does this week's work actually follow
from the requirements and the design that you wrote in previous weeks, and does your
commit history show the work growing step by step rather than one last-minute dump? If you
changed your plan, did the change get a dated line in the change log of `PROPOSAL.md`?
Changing your mind is normal and healthy, but the change must be visible. The project
itself (its problem and its product) is fixed at the end of the Week 3 lecture (11:45);
after that, only its details change. A requirement
that is silently abandoned costs the mark; a requirement that is dropped with a one-line
justification in `ai_log_NN.md` costs nothing. That is what engineering looks like.

**Human involvement — 2 points.** This is proof that people, and not only models, did
this week's work. Your own part is shown in `weekNN/ai_log_NN.md`: a concrete AI error,
the pasted evidence, and what you changed by hand; these two points are paid for that
log. From Week 2, up to two classmates may help you each week in the role that the
assignment names (for example as stakeholder, as design reviewer or as tester), and you
record them in `weekNN/contributors_NN.json` with one sentence each on what they did,
plus evidence of that work; the evidence can be their notes, their bug list, or a dated
paragraph in your log. In Week 2 contributors are optional: none, one or two, and
working alone costs you nothing. From Week 3 they are not optional: your three
reviewers in the lecture, and from Week 4 the three members of your group, must appear
in the file every week. Whatever you list must be real; names and nothing behind them
is a list, not evidence, and without evidence the contributors' bonus is not paid.

**From Week 4 your contributors are your group.** In Week 3 you form a group of four
yourselves, and that group stays together for the term. Every week, between the lecture and
Saturday, the four of you meet **online for one hour**: each person presents what changed
in their project that week, and the other three say what they think. Your three entries
in `weekNN/contributors_NN.json` are those three people; for each one, you write what
they said, as a quotation, and what you did about it. Nobody can write those entries for
someone who was not there.

**Contributors earn a bonus.** A classmate who helps you earns 10% of your mark for that
week, for at most three contributions a week; the same applies to you when you help
them. In Week 2 the names are your choice; from Week 3 they are your group. Week 1 has
no contributors.

An LLM (a large language model, the kind of model behind AI assistants) can produce
every file that an assignment asks for. What it cannot do is make those files agree with
the ten weeks around them, or notice its own mistakes on your behalf. That is what is
actually being assessed.

---

## 4. Rules that apply every week

**Never put an API key in your code.** (An API key is the secret, password-like string
that lets your program use an external service.) The key lives in `.env` (a small file
of settings that only your own computer reads), and `.env` is listed in `.gitignore`
(the file that tells git which files must never be committed). If a key reaches the
repository, the automatic scan catches it and you lose **10 points**. Once a key has
been pushed, deleting it is not enough, because it stays in the git history. You must
revoke that key and issue a new one.

**Keep the code clean.** Before pushing, run `ruff` (a tool that finds and fixes style
problems in Python code):

```bash
ruff check .          # list problems
ruff check . --fix    # fix what can be fixed automatically
ruff format .         # format
```

AI-generated code frequently leaves unused imports behind (an import line that loads a
module which the code never uses); `ruff` catches them instantly.

**Your app must work on a phone.** Narrow your browser window to about 390 pixels
(roughly the width of a phone screen) now and then. If something is cut off or scrolls
sideways, fix it while the window is small, not in Week 10.

**Do not break earlier weeks.** The checks are cumulative: in Week 5, Weeks 1 to 4 are
re-checked. If a change breaks something older, CI (the automatic run of the checks on
GitHub; see §3) tells you.

---

## When you are stuck

**CI is red and I do not understand why.** Open the **Actions** tab on GitHub and click
the failed run. It says which check failed and why, line by line. The same output comes
from `python .github/check_deliverables.py` when you run it locally (on your own
computer).

**The checks pass locally but fail on GitHub.** The usual cause is a file that you did
not push. Run `git status` (it lists the files that have changed and have not yet been
committed or pushed).

**`ruff` is clean locally but not in CI.** This is a version mismatch: your computer and
CI are running different versions of `ruff`. Install the version pinned in that week's
`requirements.txt` (the list of the packages, with their exact versions, that the week
needs), not whichever one you happen to have.

**Ollama will not run / the model will not download.** (Ollama is the program that runs
an AI model on your own computer.) Drop to a smaller model. If none of them works, use
the cloud backend (a model that runs on a provider's servers and that you reach over the
internet) and write down why in `model_notes.md`; that is an acceptable outcome. Do not
lose the week to it.

**I broke something and cannot undo it.** Do not panic, because git remembers
everything:

```bash
git log --oneline           # commit history
git diff                    # what has changed right now
git checkout -- file.py     # restore one file to the last commit
```

**Still stuck?** Ask in the lecture, or ask an AI. If you ask an AI, verify what it tells
you, and record the exchange in `ai_log_NN.md`. That is precisely what this course is
about.

---

## Command summary

```bash
# while working
python .github/check_deliverables.py     # show me what is missing
AIASD_WEEK=2 python .github/check_deliverables.py   # just one week, if you want
ruff check . --fix                       # clean the code
git add . && git commit -m "weekNN: ..." && git push

# environment
source .venv/bin/activate                # Windows: .venv\Scripts\activate
streamlit run app.py
```
