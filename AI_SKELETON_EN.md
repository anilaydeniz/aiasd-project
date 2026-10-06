# AIASD — The Term at a Glance

**AI-Assisted Software Development · Atlas University · Fall 2026–2027 · Prof. Dr. Vedat Coşkun**

*Türkçesi: [`AI_SKELETON_TR.md`](AI_SKELETON_TR.md)*

This document is the whole term on two pages: it says what each week teaches, what you do
in the room, what you finish by Saturday, and what arrives in your repository. It is shown
in the first lecture and it lives in your repository. It may change during the term, and
every change is logged at the end of this file, in the same way that you log changes to
your own proposal.

## What holds every week

- You build **one project, alone, for the whole term**. The project is a mobile client, a
  web client and a server, with login by e-mail code and/or OTP (a one-time password, a
  short code that is valid only once), and it is **published on a public app store** by
  the end of the term. Which store you use, and whether the app is native or hybrid, is
  your choice (`AI_PLATFORMS_AND_STORES_EN/TR.md`). The defence in Weeks 13–14 is run from
  the store-installed app.
- **Your project includes a chatbot about itself.** You build it in Weeks 6–7 with
  open-weight models that you run yourself (BGE-M3 for embeddings, which are numeric
  representations of text used to find similar passages, and Qwen via Ollama for the
  answers), over your own documents and data, and it is reachable from both clients. No
  cloud model APIs may be used for this feature.
- You earn **10 points a week**: 5 are read from your repository at the end of the lecture,
  and 5 at Saturday 23:59. Week 1 is worth 5, and all of them are read on Saturday. The
  term grade is made up of weekly projects 60 · store bonus 15 · presentation (the
  defence, Weeks 13–14) 15 · final exam 40.
- **From Week 3 you work in a group of four** that you form yourselves in the Week 3
  lecture, and the group stays together for the term. The three other members are your
  contributors in `weekNN/contributors_NN.json`; from Week 4 the four of you also meet
  online for one hour every week. They earn a bonus from your mark, and you earn one from
  theirs. In Week 2, contributors are optional.
- **You prove the human work**: you prove yours in `weekNN/ai_log_NN.md`, and your helpers
  prove theirs beside their names. Two of the Saturday points depend on that proof.
- **`PROPOSAL.md` lives at the root** and may change in any week, provided that you add a
  dated line to its change log. A silent change costs points; a logged change is
  engineering. **The project itself is fixed at the end of the Week 3 lecture (11:45)**: from
  then on its details may change, but not its problem or its product.
- **Publishing is graded step by step** (the steps S0–S6 in the plan), in the week in
  which each step is due. Nothing about the store can be done in the last week.
- **Every diagram is Mermaid** (a text notation for diagrams), written inside the markdown
  file. GitHub draws it, and the checker reads it.

How the points are computed, what the checker looks for, and the fine print of the bonus
are in `AI_WEEKLY_WORKFLOW_STUDENT_EN.md` / `_TR.md`.

## Weekly plan

### What happens each week

| Week | Content | In class | After class | Notes |
|---|---|---|---|---|
| 1 | Course intro; tools; Git; first contact with LLMs (large language models) | • The assignment is explained step by step<br>• nothing is built yet | Install the tools, create the private repo from the template, add the Collaborator, fill in student.json, write hello.py and explore two LLMs | • The week is worth 5 pts, all read on Saturday (3 auto · 1 commits · 1 AI log)<br>• There are no contributors this week |
| 2 | Proposal Part A + Requirements (SRS, the document that lists what the system must do) | • Write the problem and the solution<br>• interview two stakeholders<br>• start the requirement list | • Finish proposal Part A<br>• write the SRS with its diagrams | • The proposal lives at the root, and you may revise it in any week with a change-log line<br>• Role: stakeholder |
| 3 | Pitch, review, Proposal Part B | • Form your group of four<br>• present your pitch in the group; the other three write their answers<br>• revise Part A and start the change log<br>• list the screens of the main flow; the project is fixed at the end of the lecture (11:45) | • Write Part B: market, competitors, comparison, commercial potential, technical risks with the store choice<br>• AI log: the assistant as a hostile reviewer<br>• make every acceptance criterion testable for Week 4 | • S0: §12 of the proposal names the store, the fee and the review time<br>• From Saturday a requirement id never changes its meaning; the list stays open until the baseline at the end of Week 5<br>• Role: reviewer; the group stays for the term |
| 4 | Clickable prototype and test cases | • Build the main flow as plain HTML screens<br>• write a test case for every must requirement<br>• the group runs them on the prototype (the walk-through) | • Fix what failed; round 2 in the group meeting<br>• update the requirements and the test cases<br>• complete the screen flow<br>• open the developer account | • S1: apply on the day of the lecture, because the identity check takes days<br>• Role: prototype-tester |
| 5 | Design and API contract; development starts | • Write the design (the components and the REQ ids they serve)<br>• the server skeleton runs locally | • Write the API contract (every endpoint of the server)<br>• the login by e-mail code / OTP works end to end<br>• the first automated tests, named by their TC ids | • On Saturday the requirements and the test cases become your baseline; after that a change goes through a change request<br>• Role: design-reviewer |
| 6 | Chatbot I — the engine | • Ollama + Qwen are running<br>• BGE-M3 embeddings are built over the project's own documents<br>• a chat endpoint on the server answers a question about the project | • Tune the retrieval (chunking, which is how the documents are cut into pieces, and top-k, which is how many pieces are given to the model)<br>• write the model notes: which models you tried and what they got wrong<br>• create the app record in the store | • S2: the app record / bundle id (the unique name under which the store knows your app)<br>• Role: code-reviewer |
| 7 | Chatbot II — in the clients | The chat screen in the web client talks to the server | • Build the chat screen in the mobile client<br>• write the tests<br>• set up CI (continuous integration, the checks that run on every push) | • The first feature is live on all three tiers<br>• Role: chat-tester |
| 8 | Development — the project's own feature | The project's core feature runs on all three clients | • Complete the feature<br>• upload the first build to a test track | • S3 starts the store's mandatory test period<br>• Role: test-user |
| 9 | Beta test | • Enrol the testers on the track<br>• open the bug list | • Fix the bugs<br>• write the test report | • The beta testers must be the same people as the store's testers<br>• Role: beta-tester |
| 10 | UAT (User Acceptance Test, a session in which real users try the product) + submission | Run the UAT session with the participants | • Write the UAT report<br>• draw the deployment diagram<br>• submit the app for review | • S5 leaves a week for a rejection and a resubmission<br>• Role: uat-participant |
| 11 | Release + hardening | • Apply the review fixes<br>• the release-tester installs the app from the store | • Go live<br>• write the final README | • S6: the app is live<br>• Role: release-tester |
| 12 | Closure | • The poster draft is reviewed<br>• defence rehearsal | Finish the final poster | • The defence itself is in Weeks 13–14, and it is run from the store install<br>• Role: poster-reviewer |

### File flow — what the student receives and what she pushes

Assignments come as `_EN` and `_TR`, and the suffix is omitted below. The readings (`AI_DocN`) are in English. The lecture deck is not a file in the repository.

| Week | Handed out (arrives in `weekNN/`, or root) | Pushed by end of lecture (5) | Pushed by Saturday (5) |
|---|---|---|---|
| 1 | • `AI_Doc1`–`AI_Doc4` pre-reading (root)<br>• `week01/ASSIGNMENT_01`<br>• the scaffolds (files that arrive with headings but no content) `llm_notes.md`, `ai_log_01.md`<br>• root: `student.json`, `README`, `SETUP_CARD`, `WEEKLY_WORKFLOW_STUDENT` | — | • `student.json`<br>• `week01/setup_proof.md`<br>• `hello.py`<br>• `llm_notes.md`<br>• `ai_log_01.md` (all 5 pts) |
| 2 | • `week02/ASSIGNMENT_02`<br>• root `PROPOSAL.md` scaffold<br>• `week02/SRS.md` scaffold<br>• `requirements.json` scaffold<br>• `contributors_02.json`<br>• `ai_log_02.md`<br>| • `PROPOSAL.md` §1–§4<br>• `week02/requirements.json` first list<br>• `contributors_02.json` | • `PROPOSAL.md` §5–§7<br>• `week02/SRS.md` + diagrams<br>• `requirements.json` final<br>• `ai_log_02.md` |
| 3 | • `week03/ASSIGNMENT_03`<br>• `PITCH_03.md`<br>• `group_03.json`<br>• `contributors_03.json`<br>• `screens_03.md`<br>• `ai_log_03.md`<br>• root `AI_Doc5` | • `PITCH_03.md` (before the lecture)<br>• `group_03.json` (the same list for every member)<br>• `contributors_03.json` (three reviewers)<br>• `PROPOSAL.md` Part A revised + change log<br>• `screens_03.md` (the main flow) | • `PROPOSAL.md` §8–§12<br>• `requirements.json` updated<br>• `ai_log_03.md` |
| 4 | • `week04/ASSIGNMENT_04`<br>• `prototype/` with three starter screens<br>• `test_cases.json`, `walkthrough_04.json` and `store.json` scaffolds<br>• `contributors_04.json`<br>• `ai_log_04.md` | • `week04/prototype/` (at least five screens)<br>• `test_cases.json` (every must)<br>• `walkthrough_04.json` (round 1)<br>• `contributors_04.json` | • the full screen flow (at least seven screens)<br>• round 2; `requirements.json` and `test_cases.json` updated<br>• `week04/store.json` S1<br>• `ai_log_04.md` |
| 5 | • `week05/ASSIGNMENT_05`<br>• `DESIGN.md` and `api.md` scaffolds<br>• `contributors_05.json`<br>• `ai_log_05.md` | • `week05/DESIGN.md`, first version<br>• the server skeleton<br>• `contributors_05.json` | • `week05/api.md`<br>• the login working<br>• the first tests, named by TC id<br>• `ai_log_05.md` |
| 6 | • `week06/ASSIGNMENT_06`<br>• `week06/requirements.txt` (Ollama client, sentence-transformers)<br>• `embedder.py`/`chat` scaffolds<br>• `model_notes.md` scaffold<br>• `contributors_06.json`<br>• `ai_log_06.md` | • `embedder.py`<br>• the `chat` endpoint answering one question<br>• `contributors_06.json` | • retrieval working over all project docs<br>• `week06/model_notes.md`<br>• `store.json` S2<br>• `ai_log_06.md` |
| 7 | • `week07/ASSIGNMENT_07`<br>• test + CI scaffold<br>• `contributors_07.json`<br>• `ai_log_07.md` | • the chat screen in the web client<br>• `contributors_07.json` | • the chat screen in the mobile client<br>• tests + CI green<br>• `ai_log_07.md` |
| 8 | • `week08/ASSIGNMENT_08`<br>• `contributors_08.json`<br>• `ai_log_08.md` | • the core feature on all three clients<br>• `contributors_08.json` | • the feature complete<br>• `store.json` S3 (first build, track)<br>• `ai_log_08.md` |
| 9 | • `week09/ASSIGNMENT_09`<br>• test report scaffold<br>• `contributors_09.json`<br>• `ai_log_09.md` | • the testers enrolled (= `contributors_09.json`)<br>• the bug list | • the fixes<br>• the test report<br>• `store.json` S4<br>• `ai_log_09.md` |
| 10 | • `week10/ASSIGNMENT_10`<br>• UAT report scaffold<br>• `contributors_10.json`<br>• `ai_log_10.md` | • the UAT findings<br>• `contributors_10.json` | • the UAT report<br>• the deployment diagram<br>• `store.json` S5<br>• `ai_log_10.md` |
| 11 | • `week11/ASSIGNMENT_11`<br>• final README scaffold<br>• `contributors_11.json`<br>• `ai_log_11.md` | • the review fixes<br>• `contributors_11.json` | • `store.json` S6 (store URL + web URL)<br>• the final README<br>• `ai_log_11.md` |
| 12 | • `week12/ASSIGNMENT_12`<br>• poster spec<br>• `contributors_12.json`<br>• `ai_log_12.md` | • the poster draft<br>• `contributors_12.json` | • the final poster<br>• `ai_log_12.md`<br>• the defence from the store install |

## Change log

- 21 Sep 2026 — v2, first version shown.
- 26 Sep 2026 — term grade per the syllabus (60 · 15 · 15 · 40, final exam); defence moved to Weeks 13–14.
- 26 Sep 2026 — store choice is the student's (any of four stores; native or hybrid), the Platforms and Stores handout (`AI_PLATFORMS_AND_STORES_EN/TR.md`) at the root; Week 1 readings are `AI_Doc1–4` at the root; `GRADING.md` reference replaced by the student workflow.
- 4 Oct 2026 — Week 3 row and the contributors rule updated (pitch, groups of four, requirement ids permanent with the baseline at the end of Week 5).
- 4 Oct 2026 — Weeks 4 and 5 rewritten: Week 4 is the clickable prototype with test cases written from the acceptance criteria and run by the group; Week 5 is the design, the API contract, the server skeleton and the login, and the requirements and test cases become the baseline at its end. The `store.json` file lives in `week04/`.
- 5 Oct 2026 — Week 3: the project becomes fixed at the end of the lecture (11:45), and later only details may change, each with a change-log line; the screens of the main flow are listed in `week03/screens_03.md` during the lecture; the developer account (S1) may already be opened in Week 3; every member writes the same group list in `week03/group_03.json`.
