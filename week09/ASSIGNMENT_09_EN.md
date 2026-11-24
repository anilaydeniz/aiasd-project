# Week 9 Assignment: The Beta Test

## 1. Rules and grading

### 1.1 Rules

- **Use one unshared computer and one unshared GitHub account.** You must work in the lecture on a computer that is
  listed in your `student.json` (Week 8 §4.1), and after the lecture on the same computer. Lecture work that you do
  on a computer that is not listed in `student.json`, or under another person's Git identity, earns nothing for the
  lecture. If you arrive late and a significant part of the lecture work was already done before you arrived, your
  lecture work will earn 0 points.

- **List in every commit the work that it belongs to, and never 'force push'.** From this week, a single commit for
  a piece of work is enough. After the first line of the commit message, each commit must list the work that it
  belongs to, one line each, beginning with `- ` (§5.7). A force push costs you the commit point of the week,
  whatever it changed.

- **Open an issue before you move on to the Saturday work in the lecture.** If you finish the lecture work before
  the end of the lecture, you must first open an issue in your own repository that says you have finished it. Only
  after that may you start the Saturday work, so that I can tell your lecture work from your Saturday work.

- **Fill in the AI log without any AI help. If an assistant helps you with the AI log in any way, your AI log earns
  0.** Do not use an assistant to write the log, to improve it, to translate it or to correct its language.

**Where an assistant helps this week, and where it cannot:**

The beta test is the week of real people. What your testers saw, and what you decide about it, must come from you
and from them, not from an assistant.

| The work | The assistant |
|---|---|
| Find the cause of a bug, and write or fix the code. | The assistant helps. You must check every change before you commit it. |
| Write the chatbot's tests with a fake model, and the code of the Report button. | The assistant helps. |
| Run the test cases of a classmate on their app, and write what you saw. | The assistant cannot help. |
| Write `beta_runs.json`, `bug_list.json` and `tested_by_me.json`. | The assistant cannot help. |
| Write the change requests, the requirements and the test cases. | The assistant cannot help. |
| Write `test_report_09.md`. | The assistant cannot help. |
| Fill in S4 in `week04/store.json`. | The assistant cannot help. |
| Write `ai_log_09.md`. | The assistant cannot help in any way. If an assistant helps you, your AI log earns 0. |

### 1.2 How your performance will be graded

Your performance in the lecture will be graded out of 5 points. I will read the last commit that you pushed by the
end of the lecture, and I will check the following:

- Each of your classmate testers who was in the lecture ran your test cases on your app, installed from the test
  track, and you wrote each of their runs in `week09/beta_runs.json` (§4.2).
- Every run that failed, and every other problem that your testers found, is in `week09/bug_list.json` (§4.3).
- You tested the app of every classmate who listed you as a tester and who was in the lecture, and you wrote each
  of them in `week09/tested_by_me.json` (§4.4).

The first item will earn you 2 points, the second 1 point and the third 2 points.

Your performance before Saturday 23:59 will be graded out of 5 points. I will read the last commit that reached
GitHub by 23:59. GitHub's push time counts, not the time on a commit.

- Green checks will earn you 2 points.
- The AI log will earn you 2 points when it tells your real use of the whole week, matches your commits, shows how
  you checked the answers and names the commits. It will earn you 1 point when it is too general or when it does
  not show how you checked the answers. It will earn you 0 points when an assistant wrote it, when your commits
  contradict it, or when it is empty.
- Commit discipline will earn you 1 point (§5.7).

I will give you a warning first for a format error. If you repeat the same error in a later week, you will lose 1
point.

---

## 2. Semester plan at a glance

<table>
<tr><th width="10%" align="center">Week</th><th width="15%" align="center">Dates</th><th width="70%" align="left">What we do</th></tr>
<tr><td align="center">1</td><td align="center">22–23 Sep</td><td>You set up the tools, learned Git and GitHub, and took a first look at LLMs.</td></tr>
<tr><td align="center">2</td><td align="center">29–30 Sep</td><td>You wrote Proposal Part A, the requirements, and the SRS with its use cases.</td></tr>
<tr><td align="center">3</td><td align="center">6–7 Oct</td><td>You pitched your project in your group, wrote Proposal Part B and chose your store (S0).</td></tr>
<tr><td align="center">4</td><td align="center">13–14 Oct</td><td>You made the clickable prototype and wrote the test cases (S1).</td></tr>
<tr><td align="center">5</td><td align="center">20–21 Oct</td><td>You wrote the design and the API contract, and you started the server. Your requirements became your baseline.</td></tr>
<tr><td align="center">6</td><td align="center">27–28 Oct</td><td>Your feature worked end to end, on the server and on the web (S2).</td></tr>
<tr><td align="center">7</td><td align="center">3–4 Nov</td><td>Your app ran on the phone.</td></tr>
<tr><td align="center">–</td><td align="center">10–11 Nov</td><td>There was no lecture.</td></tr>
<tr><td align="center">8</td><td align="center">17–18 Nov</td><td>Your product got its chatbot, your server kept its data after a restart, and your first build went to your testers (S3).</td></tr>
<tr><td align="center"><b>9</b></td><td align="center"><b>24–25 Nov</b></td><td><b>This week, your testers will test your app in the beta test. You will fix the bugs, write the tests of the chatbot and add the Report button to its answers (S4).</b></td></tr>
<tr><td align="center">10</td><td align="center">1–2 Dec</td><td>You will do the UAT, draw the deployment diagram and submit your app to the store (S5). <i>Start early: see the list below.</i></td></tr>
<tr><td align="center">11</td><td align="center">8–9 Dec</td><td>You will apply the review fixes, release your app on the store and write the final README (S6). <i>Start early: see the list below.</i></td></tr>
<tr><td align="center">12</td><td align="center">15–16 Dec</td><td>You will make the poster and rehearse the defence. <i>Start early: see the list below.</i></td></tr>
<tr><td align="center">13</td><td align="center">22–23 Dec</td><td>Students whose app is live on the store will present their projects.</td></tr>
<tr><td align="center">14</td><td align="center">29 Dec</td><td>The other students will present their projects.</td></tr>
</table>

**Start early.** Some work of the coming weeks will take days, not hours, so I kindly ask you to start it early:

- **Week 10:** You will need the store listing of your app: its icon, its screenshots, its descriptions and the
  address of your privacy text. You will also need the five people of your pitch for the UAT. Ask them this week.
- **Weeks 10 and 11:** The review of your app by the store can take several days, and this time is your
  responsibility. Submit your app in Week 10 as planned, so that you have time to apply the review fixes in Week 11.
  The other 3 points of the presentation in Week 13 also require that you submitted your app by Saturday 5 Dec 23:59.
  On Google Play, your testers must stay enrolled for 14 days in a row before you can apply for production.
- **Week 12:** You will need the screenshots of your app and your architecture diagram for your poster.

---

## 3. This week

### 3.1 This week at a glance

Since Week 8, your app has been on the test track of your store, and your testers have been enrolled on it. This
week, real people will use it for the first time. Your classmate testers will test your app in the lecture, and you
will test the apps of the classmates who listed you as their tester. Your testers who are not in this course will
test your app by Saturday 23:59.

```text
your testers install your app from the test track (before the lecture)
  ↓    they run your test cases, and they use the app freely
  ↓    you write each run in beta_runs.json, and each problem in bug_list.json
  ↓    you fix the bugs (one BUG id per line in the commit message)
  ↓    the failed runs run again (round 2)
  ↓    test_report_09.md: what the beta test showed
```

Each test with a classmate is recorded twice: once by the owner of the app (`beta_runs.json`) and once by the tester
(`tested_by_me.json`). So both of you must write the same test, each in your own repository.

**What you do in the lecture**

<table>
<tr><th width="15%" align="left">Time</th><th width="75%" align="left">Your work</th><th width="10%" align="center">§</th></tr>
<tr><td>before the class</td><td>Your testers have installed your app from the test track, and you have installed the apps that you will test. The issue "Prepare for Week 9" in your repository explains this.</td><td align="center">4.2</td></tr>
<tr><td>start of the lecture</td><td>Run the checker: it brings <code>week09/</code>. Commit the course files, and push.</td><td align="center">4.1</td></tr>
<tr><td>until about 11:15</td><td>The beta test. Your classmate testers run your test cases on your app, and you run the test cases of the classmates who listed you. Right after each turn, write the runs: the owner in <code>beta_runs.json</code>, the tester in <code>tested_by_me.json</code>.</td><td align="center">4.2, 4.4</td></tr>
<tr><td>about 11:15</td><td>Write your bug list from the failed runs and the other problems.</td><td align="center">4.3</td></tr>
<tr><td>11:45</td><td>Push for the last time.</td><td align="center">4.5</td></tr>
</table>

Your lecture performance will be graded out of 5 points, and Saturday performance will be graded out of 5 points.
The details are in §1.2.

### 3.2 What you are going to learn this week

This week, you are going to learn:

- how a beta test with real people finds problems that you and an assistant did not expect;
- how to turn what testers saw into a bug list, and fix each bug with a traceable commit;
- how to test code that calls an LLM API without calling the API, with a fake model.

You will also use these new terms:

| Term | What it means |
|---|---|
| Beta test | The beta test is the test of a nearly finished product by real users before it goes to the public. Your testers install your app from the test track, and they use it like users. |
| Beta tester | A beta tester is a person who is enrolled on your test track and who tests your app. Your beta testers are the testers that you enrolled at S3. |
| Bug | A bug is a difference between what your product does and what your requirement or your test case says it must do. A crash, a wrong answer and a screen that a tester cannot understand are all bugs. |
| Severity | The severity of a bug says how much it hurts the user: `high` (the user cannot finish the main task, or data is lost or exposed), `medium` (the user can finish it, but with difficulty), `low` (a cosmetic problem). |
| Round 2 | Round 2 is the run of a failed test case again, after the fix. |
| Fake model | A fake model is a small function in your test that answers in place of the LLM API. The test then checks your code without the internet, without a key and without cost. |
| Coverage | Coverage is the share of the lines of your server that your tests run. `pytest-cov` measures it. |
| S4 | S4 is the fourth store step. In S4, your beta test runs on the test track of your store, with the testers that you enrolled at S3. |

### 3.3 What the checker brings this week

When you run the checker at the start of the lecture (§4.1), it brings the new folder `week09/` into your
repository. The folder holds:

- `ASSIGNMENT_09_EN.md` and `ASSIGNMENT_09_TR.md`: this assignment, in English and in Turkish;
- `beta_runs.json`: the runs of your testers on your app (§4.2);
- `bug_list.json`: your bug list (§4.3);
- `tested_by_me.json`: the apps that you tested (§4.4);
- `test_report_09.md`: the form of your test report, which you will fill in on Saturday (§5.5);
- `ai_log_09.md`: the form of your AI log, which you will fill in on Saturday (§5.6);
- `requirements.txt`: the packages of this week, `pytest-cov` among them.

Install the packages of this week once:

```bash
pip install -r week09/requirements.txt
```

The checker itself also gets new checks this week. It will check the three files of the beta test. I will compare
your `tested_by_me.json` with the `beta_runs.json` of each classmate whose app you tested. On Saturday, it
will also check the chatbot's tests, the Report button, the test report and S4 in `week04/store.json`.

---

## 4. Your work in the lecture

### 4.1 The course files

Run the checker at the start of the lecture. It brings `week09/`. Then commit the course files, and push:

```bash
python .github/check_deliverables.py
git add .
git commit -m "week09: course files"
git push
```

The checker also reads the name of your computer and your `git config user.email`, and it tells you if this
computer is not listed in `student.json`.

### 4.2 The beta test: `week09/beta_runs.json`

Your classmate testers are the classmates whom you wrote in `"classmate_testers"` of S3 in `week04/store.json`.
Each of them who is in the lecture tests your app, and you test the app of each classmate who listed you.

- **The app comes from the test track.** The tester uses your app as it was installed from the test track of your
  store, on the tester's own phone. A build that runs only on your laptop or in an emulator is not a beta test.
- **The tester runs your test cases.** The tester runs at least three of your test cases from
  `week04/test_cases.json`, and at least one of them must be outside the login. The chatbot's test case is a good
  choice.
- **Then the tester uses the app freely** for a few minutes, like a user, without your test cases.
- **You watch, and you do not help.** Do not explain your screens. When a tester does not know what to do, that is a
  finding.

If your store did not accept your app or your account on its test track for a reason that you cannot change, for example because of the store's own rules, your testers may install an APK of your app on their own phones. Save the store's message of refusal as a screenshot in `week04/`, with your personal details covered. In `beta_runs.json`, add "(APK)" to the device, and in S4 write "APK" and the reason in `track`. A step that was late or not done, such as a build that was not uploaded in time or testers who were not enrolled, is not such a reason.

Right after each turn, type each run into `week09/beta_runs.json` by hand. The form is the same as
`mobile_runs.json` of Week 7:

```json
{ "tc": "TC-012-01", "tester": "123456789", "device": "Samsung A52, Android 14", "round": 1,
  "result": "fail", "note": "The chat screen showed an empty bubble when the server answered 503." }
```

- `tc` is the id of the test case. For a problem that the tester found while using the app freely, write `"free"`.
- `tester` is the 9-digit student number of the tester. For a tester who is not in this course, write
  `"outside: "` and the first name and the first letter of the surname, for example `"outside: Ayşe Y."`. Never
  write an e-mail address.
- `device` names the phone of the tester.
- `round` is 1 for the beta test, and 2 for a run again after a fix (§5.2).
- `result` is `pass`, `fail` or `blocked`. `note` must say in one full sentence what the tester saw. A `fail` run or a
  `blocked` run must have a note.

### 4.3 The bug list: `week09/bug_list.json`

Right after the beta test, write your bug list. Every `fail` run and every `blocked` run, and every other problem
that a tester found, is one entry, unless it is the same problem as an earlier entry:

```json
{ "id": "BUG-01", "found_by": ["123456789"], "tc": "TC-012-01", "severity": "high",
  "what": "The chat screen shows an empty bubble when the server answers 503.",
  "status": "open", "fix_commit": "", "why": "" }
```

- `id` is `BUG-` and a number: `BUG-01`, `BUG-02`, and so on. An id never changes its meaning.
- `found_by` lists the testers who found it, as in `beta_runs.json`.
- `tc` is the id of the test case, or `"free"`.
- `severity` is `high`, `medium` or `low` (§3.2). You decide it.
- `what` says in one full sentence what is wrong, so that someone who has never seen your app understands it.
- `status` is `open` in the lecture. On Saturday, it becomes `fixed` or `not fixed` (§5.2).

### 4.4 The apps that you tested: `week09/tested_by_me.json`

You are a beta tester too. Test the app of each classmate who listed you as a tester and who is in the lecture, in
the way that §4.2 describes. Right after each turn, write it in your own `week09/tested_by_me.json`:

```json
{ "owner": "234567891", "device": "Xiaomi Redmi Note 12, Android 14", "tcs": ["TC-001-01", "TC-004-01", "TC-009-01"],
  "free_use": true, "problems": 2, "note": "The list did not refresh after I added a record." }
```

- `owner` is the 9-digit student number of the owner of the app.
- `tcs` lists the test cases that you ran. `free_use` is `true` if you also used the app freely.
- `problems` is the number of problems that you saw. `note` says the most important one in one full sentence, or
  `"no problem"`.

If no classmate listed you as a tester, set `"nobody_listed_me"` to `true` at the top of the file.

The owner's `beta_runs.json` and your `tested_by_me.json` must describe the same test. I will compare them.

### 4.5 Push, and check the result on GitHub

Run the checker, commit and push. The lecture mark reads the last commit that you pushed by the end of the lecture.
A test with a classmate that you missed in the lecture cannot be made up.

---

## 5. Your work by Saturday 23:59

### 5.1 The testers who are not in this course

Your testers who are not in this course test your app by Saturday 23:59, in the same way: they run at least three of
your test cases and then use the app freely. You write each of their runs in `beta_runs.json` with
`"outside: "` and the first name (§4.2), and each problem in `bug_list.json`.

A tester who is not in this course has no repository, so the second side of the record is a screenshot. For each
of these testers, save one screenshot in `week09/`: either their message to you that says what they saw, or their
feedback in the console of your store. Cover the e-mail address and the phone number before you save it. Write the
file name in the `evidence` field of each of their runs, for example `"evidence": "outside_ayse.png"`.

### 5.2 Fix the bugs

Every entry of `bug_list.json` must have a decision by Saturday:

- **Fix it.** Set `status` to `fixed`, and write the commit of the fix in `fix_commit`. The commit message must name
  the bug in its list (§5.7), for example `- BUG-03: the chat screen shows the 503 message`. Then the failed test
  case must run again: write a new run with `"round": 2` in `beta_runs.json`. You may run round 2 yourself.
- **Do not fix it.** Set `status` to `not fixed`, and write in `why` in one full sentence why not. A `high` bug may
  stay unfixed only when it is outside your requirements, and then you must write which change request removes it
  from your plan.

If a fix changes a requirement, a test case, a screen or an `api.md` row, write the change in the Change log of
`PROPOSAL.md`, as in every week.

### 5.3 The chatbot's tests, with a fake model

In Week 8, the test case of the chatbot was `"run": "manual"`. This week, its behaviour is tested on the server too,
without the internet and without a key: the test replaces the call to the LLM API with a fake model.

- Add the test cases below to `week04/test_cases.json` with `"run": "server"`, each named by your chatbot's
  requirement. Adding test cases is a change request: write one `CR-` line for them in the Change log of
  `PROPOSAL.md`.
  - the chatbot answers a logged-in user;
  - without a token, the answer is 401;
  - after the daily limit, the answer is 429;
  - when the LLM API fails or does not answer in time, the answer is 503, and the server does not crash.
- Write a test for each of them in `server/tests/`, named by its id, for example
  `test_TC_012_03_after_the_daily_limit_the_answer_is_429`.
- In each test, replace the function of your server that calls the LLM API with a fake one. For example, with
  pytest's `monkeypatch`:

```python
from fastapi.testclient import TestClient

from server.course_login import auth_header_for_tests
from server.main import app

client = TestClient(app)


def test_TC_012_02_the_chatbot_answers(monkeypatch):
    monkeypatch.setattr("server.chat.ask_model", lambda messages: "Your next booking is on Monday.")
    headers = auth_header_for_tests(client, "chat02@example.edu.tr")
    r = client.post("/chat", json={"message": "When is my next booking?"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["answer"] == "Your next booking is on Monday."
```

  The names `server.chat` and `ask_model`, the field `answer` and the address are examples: use the module, the
  function and the fields of your own server, and a different address in each test. If your server calls the API in
  the middle of a long function, first move the call into a function of its own.
- The tests must never call the real LLM API, and they must stay green on GitHub, where there is no key.

Then measure the coverage of your server once:

```bash
pytest --cov=server --cov-report=term
```

Write the total percentage in your test report (§5.5). The percentage itself will not be graded.

### 5.4 The Report button

A model can write a wrong or an offensive answer. Google Play's policy on AI-generated content asks apps whose AI
chatbot is a central feature to let the user report offensive content without leaving the app. Whatever your store
is, every answer of your chatbot gets a **Report** button this week.

- **Add it as a change request.** Add a requirement for it to `week02/requirements.json` with the next free id, its
  test case to `week04/test_cases.json`, and the row of its route to `week05/api.md`. Name all three in one `CR-`
  line of the Change log.
- **The route.** For example, `POST /chat/report` receives the answer and a short reason from the user. It requires
  the login (401 without a token), and your server keeps the report in its data, as it keeps your other records.
- **The screen.** Next to each "AI answer" in the chat screen of `mobile/`, a Report button sends the answer to this
  route, and the screen tells the user that the report was received.
- **The test.** Write a test of the route in `server/tests/`, named by its test case.

### 5.5 The test report: `week09/test_report_09.md`

Fill in the test report yourself. It has these parts:

1. **The testers.** The student numbers of your classmate testers, and the first names of your other testers. Write
   who tested in the lecture and who tested by Saturday.
2. **What was tested.** The build (the version of S4), the test cases that ran, and the free use.
3. **The numbers.** How many runs, how many `pass`, `fail` and `blocked`, how many bugs by severity, and how many of
   them are fixed.
4. **The three most important findings.** For each one, what the testers saw, and what you did about it.
5. **What surprised you.** The problem that you did not expect at all, and why you think you did not expect it.
6. **The chatbot's tests.** The coverage of your server (§5.3).

### 5.6 The AI log: `week09/ai_log_09.md`

The form is the same as in Week 8. The log must tell how you used AI assistants in the whole week, in all of your
work. I will compare it with your commits. Fill it in yourself on Saturday:

1. **My assistants.** Each assistant that you used, its model, and whether it is free or paid, with the plan.
2. **Every use of an assistant this week.** One row for each real use, in the order of the week: what you asked, how
   you checked the answer, what you did with it, and the commit.
3. **How I worked with assistants this week.** Your way of working over the whole week, in a few sentences.
4. **What I did without an assistant.** Which part of the work you did yourself.
5. **Next week.** One thing that you will do differently next week.
6. **Before this course and now.** This part will not be graded, so I kindly ask you to write it honestly.

For 2 points, each row must say concretely how you checked the answer, and each kept result must name its commit.
If a coding agent made a commit, the row must also say which commit it made and how you checked it. **You must
write the AI log without any AI help. If an assistant helps you with the log in any way, your AI log earns 0.**

### 5.7 Commits, and green checks

The commit point of the week asks for the following. The list of the work in each commit is new this week, so a commit without it earns you a warning this week, not a deduction. From Week 10, it costs you the commit point.

- **Each commit lists the work that it belongs to.** After the first line of the message, leave an empty line, and
  list the work that the commit belongs to, one line each, beginning with `- `. Name the bug, the requirement, the
  test case or the section of this assignment. For example:

  ```text
  week09: show the 503 message in the chat screen

  - BUG-03: the empty bubble on 503
  - TC-012-04: the screen part of the 503 test case
  ```

  A line such as `- fix` or `- update` does not count. With `git commit` alone (without `-m`), Git opens an editor
  in which you can write several lines.
- **The list matches the commit.** The lines must describe the files that the commit changes.
- **One commit for a piece of work is enough.** You may commit as often as you like.
- **Never force push.** A force push costs you the commit point of the week.
- **A commit of a coding agent counts only when your AI log describes it.** The row of the log must name the commit
  and say how you checked it. Otherwise, the commit does not count.

**Advice (it costs no point):** a commit should add at most one new screen to `mobile/` and at most one new route to
`server/`. Smaller commits are easier to check, and the checker keeps warning you.

The ten course tests, and the tests of every test case with `"run": "server"`, must stay green on GitHub. Never
change `.github/workflows/check.yml` or `.github/check_deliverables.py`. Git must not hold the build folders of your
app (Week 7 §12).

### 5.8 S4 in `week04/store.json`

Fill in S4 yourself:

```json
  "S4": {
    "date": "2026-11-28",
    "track": "closed testing",
    "version": "1.0.1 (2)",
    "testers_in_lecture": ["123456789", "234567891", "345678912"],
    "testers_outside": ["Ayşe Y.", "Mehmet D."],
    "bugs": 7,
    "fixed": 5
  }
```

- `version` is the build that your testers tested. If you upload a new build with the fixes, write its version too,
  for example `"1.0.1 (2), fixes in 1.0.2 (3)"`.
- The testers must be the same people as the testers of S3. The e-mail addresses of your testers must never go into
  your repository.

### 5.9 Your documents: a checklist

Before your last push on Saturday, check that your documents describe your product as it is now:

- The Change log in `PROPOSAL.md` has a line for every change of the week, and a `CR-` line for each change request:
  the chatbot's new test cases, the Report button, and every fix that changed a requirement or a test case.
- Every requirement in `week02/requirements.json` belongs to a use case in `week02/SRS.md`, and the use case of the
  Report button is in the use case diagram.
- Every test case in `week04/test_cases.json` names an existing requirement, and its steps match your screens as
  they are now, after the fixes.
- Every route of your server has its row in `week05/api.md`, `POST /chat/report` too.
- Every screen in `web/` and `mobile/` names an existing requirement in its `serves:` line.
- Every `BUG-` id in `bug_list.json` with `fixed` names a commit that exists.

The checker checks some of the links between the ids. Only you can check the texts.
