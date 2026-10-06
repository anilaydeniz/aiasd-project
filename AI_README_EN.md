# AIASD Project — Student Repository

**AI-Assisted Software Development · Atlas University · Fall 2026–2027**
**Prof. Dr. Vedat Coşkun**

*Türkçesi: [`AI_README_TR.md`](AI_README_TR.md)*

---

## How to use this repository

This is your personal project repository (the folder of your project that git tracks,
on your computer and on GitHub) for the entire 12-week course. You create it from the
course template (a ready-made repository that GitHub copies for you) on Week 1, and you
commit to it every week (a commit is a saved snapshot of your files, recorded by git).

Each week arrives with its own assignment, in its own folder, and the assignment tells
you exactly what to build and what to hand in. [`AI_SKELETON_EN.md`](AI_SKELETON_EN.md)
describes the whole term on two pages: it says what each week teaches, what you push
(to push means to send your commits from your computer to GitHub) and when. During the
term you build one product, and it is yours: a mobile client, a web client and a
server. You publish it on a public app store of your choice, and at the end of the term
you defend it from the app that you installed from that store.

Most weeks also ask for an AI log (a written record of how you used an AI assistant
that week). The log is the file `weekNN/ai_log_NN.md`, inside that week's folder.

### What is in here now, and what is not

Right now this repository holds the files that live here all term, plus `week01/`.
There is no `week02/` folder, and there should not be one, because **you create each
week's folder when that week's assignment tells you to.** Putting the file in the right
place is part of the work. When you put it in the wrong place, the checker (the
automatic script that looks for the files each week requires; see "Automatic checks"
below) names the exact path it is looking for.

The following files are at the root, and they stay there all term:

| | |
|---|---|
| `app.py` | This file is your application. It is empty for now, and it grows week by week until it is the whole product |
| `week01/ASSIGNMENT_01_EN.md`, `_TR.md` | These files say what this week asks for, in both languages. They arrive together with the week's folder, and they are the only place where the tasks are written |
| `week01/ai_log_01.md` | This file is this week's AI log, and it sits in this week's folder. Every week has one, and it arrives together with the week |
| `student.json` | This file says who you are. Fill it in once, in Week 1 |
| `requirements.txt`, `weekNN/requirements.txt` | These files list the dependencies (the Python packages your app needs). They arrive week by week |
| `.github/` | This folder holds the checks that run on every push |
| `CURRENT_WEEK.txt` | This file is bookkeeping that the checker manages. Do not edit it. The first time you run the checker, a file called `CURRENT_WEEK_CACHE.txt` appears next to it. That file is the checker's offline cache (a saved copy of the week number), git does not track it, and you can ignore it |

A few weeks hand you a scaffold (a starter folder with files that are partly written,
so that you do not start from nothing). When that happens, the assignment opens with one
command, and you run that command **before** you create anything in that folder:

```bash
git remote add template https://github.com/vedatcoskun-course/aiasd-template.git
git fetch template
git checkout template/main -- week06
```

You need the first line only once in the whole term. If you run these commands after
you have already written files in that folder, the commands overwrite your files. So
run them first, or do not run them at all.

**Start here:** [`AI_SETUP_CARD_EN.md`](AI_SETUP_CARD_EN.md) / [`AI_SETUP_CARD_TR.md`](AI_SETUP_CARD_TR.md)
is one page that holds every command you will run all term, together with an
explanation of what the common errors mean. Do its four setup steps before Week 1.

**New here?** The whole weekly routine is written out step by step in
[`AI_WEEKLY_WORKFLOW_STUDENT_EN.md`](AI_WEEKLY_WORKFLOW_STUDENT_EN.md) /
[`AI_WEEKLY_WORKFLOW_STUDENT_TR.md`](AI_WEEKLY_WORKFLOW_STUDENT_TR.md). It says what you
do before, during and after each lecture, how the marks are split, and what to try when
you are stuck.

**Read before Week 1.** The three pre-readings and the paper are at the root. The
pre-readings are `AI_Doc2` AI Technical Background, `AI_Doc3` Development Environment
and Tools, and `AI_Doc4` Working with AI Tools. The paper is `AI_Doc1`, the Transformer
paper (the research paper behind today's AI assistants). The lecture is a twenty-minute
summary of these four documents. Later readings arrive in the same way, numbered in
order. `AI_Doc5` Using AI Properly in Software Development describes the eight
techniques that your weekly AI log asks for. From Week 4, one technique is compulsory
each week, and this document is in the final exam.

Both sections receive the same files. The assignments, the setup card and the workflow
come in two languages, marked `_EN` and `_TR`. Read the one in your language and ignore
the other. The readings (`AI_DocN`) are in English. The folder and file names that the
checker looks for (`week01/`, `hello.py`, `student.json`) are the same for everyone.

---

## Running the app

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Dependencies arrive week by week, so that you do not download gigabytes of packages in
Week 1. The root `requirements.txt` is the minimum. A heavier week has its own
`weekNN/requirements.txt`, and that week's assignment tells you when to install it:

```bash
pip install -r weekNN/requirements.txt
```

---

## Who you are — `student.json`

Fill this file in on Week 1, at the repo root:

```json
{
  "student_id": "20210042",
  "first_name": "Ayşe",
  "last_name": "Yılmaz",
  "nickname": "kaplumbaga",
  "section": "en"
}
```

Your **section** is `en` if you are in the English section, and it is `tr` if you are
in the Turkish one. If you get this wrong, the checker tests you against the other
section's week, so check it before you push.

Your **nickname** is the name that appears on the class board, which is projected at
the end of each lecture, so that you can find your own row at a glance. It may contain
letters, digits, `-` and `_`, and it must be 2–20 characters long. Choose whatever you
like, but pick something that you will still recognise in December.

Keep this repository **private** while the course runs, because it carries your student
number and your name.

---

## Automatic checks

Every push runs the same checks that your instructor runs. You see a green tick or a
red cross next to your commit in GitHub, and you can see exactly which check failed.

**There is nothing for you to switch on.** Every time the checker runs, it asks the
course which week it is, so what you see is always what is being run against you. The
`CURRENT_WEEK_CACHE.txt` file at the repo root is only a cache of that week number. It
updates itself, and you never need to touch it.

The output comes in two parts, because the week has two deadlines:

```
In the lab:     11 of 13 done
By Saturday:     2 of  8 done
```

**In the lab** is the part that the end-of-lecture snapshot reads (the snapshot is a
copy of your repository exactly as it is at that moment). It is worth five of the
week's ten points. **By Saturday** is everything else, which means the write-ups, the
diagrams and `ai_log_NN.md`. Items in the second group do not fail the run while the
week is still open, because they are not due yet. Nothing in the first group is
something that you should be doing at home. (Week 1 is the exception: nothing is read
at the end of the first lecture, and all five of its points are read on Saturday.)

Weeks are checked cumulatively, which means that Week 3 also re-checks Weeks 1 and 2.
If a later change breaks something earlier, you want to hear about it from CI (the
automatic checks that GitHub runs on every push), not in December.

To look at one week on its own, for example to confirm that Week 2 still passes, run:

```bash
AIASD_WEEK=2 python .github/check_deliverables.py
```

Run the checks locally (on your own computer) before you push:

```bash
python .github/check_deliverables.py
```

A red cross is not a grade. It is a list of what is still missing, and it is far better
to see that list on Tuesday than after the deadline.

**The secret scan runs on every push, at every week.** The secret scan searches your
files for passwords and keys. If an API key (a secret string that lets a program use a
service in your name) reaches the repository, the check fails loudly. Remove the key,
rotate it immediately (that is, cancel the old key and create a new one), and remember
that a committed key is an automatic 10-point deduction.

---

## Repository rules

- Push **several times in every lecture** (at least three), each time with new work in it, and outside the lecture **commit several times as you work**, each time with some new work in it; a commit does not need to be a finished part. One push on Saturday night and nothing else costs you the commit-discipline point.
- Fill in that week's `ai_log_NN.md`. Every week has one, and a person reads it.
- Do **not** commit `.venv/`, `__pycache__/`, or API keys.
- Run `ruff check .` before committing (`ruff` is a tool that reports common mistakes in Python code). It catches the unused imports that AI tends to leave behind.
- Use `.env` (a small file that holds secret values) for secrets, and keep it in `.gitignore` (the list of files that git must never commit).
- Your app must work on a phone as well as on a laptop. Narrow your browser window to ~390px now and then. If something is cut off or scrolls sideways, fix it while the page is small, not in Week 10.
