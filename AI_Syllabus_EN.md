# Course Syllabus

**Department of Software Engineering · Atlas University** · version 1 · 2026-09-21

*Türkçesi: [`AI_Syllabus_TR.md`](AI_Syllabus_TR.md)*

| | |
|---|---|
| **Course Code** | 1413002043 |
| **Course Name** | AI – Assisted Software Development |
| **Year & Semester** | 2026 – 2027 Fall |
| **Instructor** | Prof. Dr. Vedat COSKUN |

## Course Description

Students use AI as a disciplined engineering instrument across the software development life cycle. Each student builds one product alone for the whole term. The product consists of a mobile client, a web client and a server, and users log in with a code sent by e-mail or with an OTP (a one-time password, a short code that is valid only once). The product also contains a chatbot that answers questions about the project itself, and the chatbot runs on open-weight models (AI models whose weights are published, so that the student can run them on their own computer). The student publishes the product on a public app store: Google Play, Huawei AppGallery, Samsung Galaxy Store or Apple App Store. The app may be native (written in the platform's own language) or hybrid (written once for both platforms), and the student makes that choice.

The course grades the evaluation, not the generation: it does not grade what the assistant produced, but how well the student specified, checked, corrected and accounted for it. Every week's work is pushed to the student's own GitHub repository, which the student creates from the course template (a ready-made repository that GitHub copies for the student), and the work is checked automatically on every push.

## Course Objectives

On completing the course the student can:

1. **Write a project proposal.** The student starts from a real problem of their own and writes Part A, which describes the problem and the solution, names the stakeholders and gives the use cases, and Part B, which analyses the market and the competitors, judges the commercial potential and lists the technical risks, and pitches it in five minutes (Weeks 2–3).
2. **Engineer requirements.** The student manages the functional and non-functional requirements as an SRS (Software Requirements Specification, the document that lists what the system must do). Every requirement carries an identifier of the form REQ-NNN, is traceable, keeps its meaning once given, and enters a baseline after the prototype review, and the student makes every later change visible with a dated change log; test cases are written from the acceptance criteria and walked through on the prototype (Weeks 2–5).
3. **Design and prototype.** The student draws the architecture, the data model, the system-context diagram and the deployment diagram in Mermaid (a text notation for diagrams that GitHub draws inside a markdown file) in the repository, builds a clickable prototype and revises it after peer review (Weeks 4–5).
4. **Develop a full-stack application.** The student builds a server with login by e-mail code or OTP, a web client and a mobile client, and the same feature runs on all three tiers (Weeks 5, 8).
5. **Develop a mobile application.** The student builds the mobile client with Flutter, React Native–Expo, Kotlin or Swift, and the client runs on a phone and is ready for a store (Weeks 7–8).
6. **Build a chatbot on open-weight models.** The student builds a retrieval-augmented chatbot (a chatbot that first looks up the relevant passages in a set of documents and then answers from them) on Ollama (a program that runs open-weight models locally) with the Qwen model and BGE-M3 embeddings (numeric representations of text that make similar passages findable) over the project's own documents, writes the chat endpoint and integrates it into the clients (Weeks 6–7).
7. **Use AI assistants as an engineering instrument.** The student prompts the assistant, verifies and corrects its output, documents its errors with evidence in a weekly AI log, and uses the assistant as a hostile reviewer of the student's own work. The course grades the evaluation, not the generation (every week).
8. **Practise version control and continuous integration.** The student makes small daily commits, lets automatic checks run on GitHub, keeps the code quality up with ruff (a tool that reports style and error problems in Python code) and keeps secrets such as passwords out of the repository (every week; CI, continuous integration, from Week 7).
9. **Run formal testing.** The student writes unit and integration tests, runs a beta test with enrolled testers, keeps a bug list, writes a test report, and runs a User Acceptance Test (a session in which real users try the product and say whether it meets their needs) with real users (Weeks 7, 9–10).
10. **Publish an application on a store.** The student follows the S0–S6 track: they choose the store, open a developer account, create the app record, upload a build to a test track, enrol testers, submit the app, apply the review fixes and release it (Weeks 3–11).
11. **Review and collaborate.** The student takes part in a weekly review in a fixed group of four, records the feedback as quotes with an accept or reject decision and a reason, and contributes to classmates' work as a stakeholder, a reviewer or a tester (from Week 3).
12. **Defend the product.** The student installs the app from the store in front of the examiner, justifies the decisions in the code and the documents, and prepares a poster and a presentation (Weeks 12–14).

## Course Material

The course template and the weekly assignments are at github.com/vedatcoskun-course/aiasd-template. Each week's `ASSIGNMENT_NN` is there in English and Turkish, and `AI_SETUP_CARD`, `AI_WEEKLY_WORKFLOW_STUDENT` and `AI_SKELETON` are at the root.

The pre-reading for Week 1 is the paper by Vaswani et al., "Attention Is All You Need" (2017), and four course documents: AI Technical Background; Development Environment and Tools; Working with AI Tools; and Using AI Properly in Software Development (`AI_Doc5`, which describes the eight techniques that the weekly AI log asks for; it is examinable). For Week 2 the students read two complete SDLC document sets (an exam-hall allocation system; a lift controller with a simulator) and the Platforms and Stores handout.

The tools are Python 3.12, Git/GitHub, VS Code, Streamlit, Ollama with an open-weight model, two chat assistants of the student's choice on free tiers, and one mobile framework (Flutter / React Native–Expo / Kotlin / Swift). Students bring their own laptop every week.

## Grading

| Item | Points | Explanation |
|---|---|---|
| Weekly Projects | 60 | 12 weeks × 10 points, scaled to 60. Each week, 5 points are read from the repository at the end of the lecture and 5 at Saturday 23:59 (Week 1 is worth 5 points, all read on Saturday). The automatic checks give 5 points at the lecture and 2 on Saturday; the instructor gives the marks for the AI log (2) and for commit discipline (1, judged every week: several pushes at different times in the lecture (at least three), each with new work in it, and outside it several commits made as the work progresses, each with some new work in it (a commit does not need to be a finished part); earlier weeks are consulted when something looks doubtful). There is no make-up for a missed lecture. |
| Bonus-Store | 15 | Bonus for publishing. The store track S0–S6 (the student chooses the store, opens a developer account, creates the app record, uploads a test-track build, enrols testers, submits the app, and the app goes live) is graded step by step in the week each step is due. The classmates who help in a week (the contributors) earn a share of the student's mark. |
| Presentation | 15 | Project defence in Weeks 13–14. The student installs the app from the store in front of the examiner and answers questions about the decisions in the code and the documents. The app is run from the store build, not from a development machine. |
| Final Exam | 40 | Written final exam in the university's exam period. It covers the SDLC documents, the AI-log practice and the technical material of the twelve weeks. |

## In-Class Rules

- A minimum of 70% attendance is mandatory. Every reason for an absence must fit within the remaining 30% allowance. So please try to attend all classes from the beginning, to keep some flexibility for urgent issues later.
- Keep conversations during class to a minimum. Extended or disruptive discussions are not permitted. A student who violates this rule will be asked to change their seat or to leave the room.
- Phone calls, text messages, instant messages, e-mail and general web surfing are not allowed during class time. Computers may be used only to follow the material of the class.
- Voice or video recording during the class is strictly forbidden.
- Cheating or academic dishonesty in any form will be dealt with according to the applicable legal rules.

## Course Plan

| Week | Date | Subject |
|---|---|---|
| 1 | 22/09 · 23/09 | Foundations: the students set up the tools, learn Git/GitHub and meet LLMs (large language models) and transformers for the first time |
| 2 | 29/09 · 30/09 | Proposal Part A and Requirements (SRS): the students describe the problem and the solution, name the stakeholders and write the use cases |
| 3 | 06/10 · 07/10 | Pitch and review in groups of four; Proposal Part B, in which the students analyse the market and competitors, judge the commercial potential and list the risks; the store is chosen (S0); from here a requirement id never changes its meaning |
| 4 | 13/10 · 14/10 | Clickable prototype and test cases: the students write test cases from their acceptance criteria, walk through them on the prototype and update the requirements; the developer account is registered (S1) |
| 5 | 20/10 · 21/10 | Design and API contract; development starts with the server skeleton and the login by e-mail code / OTP; requirements and test cases become the baseline |
| 6 | 27/10 · 28/10 | Chatbot I, the engine: the students run Ollama + Qwen, build BGE-M3 embeddings and write the chat endpoint; the app record is created (S2) |
| 7 | 03/11 · 04/11 | Chatbot II: the chatbot goes into the web and mobile clients; tests; CI |
| 8 | 10/11 · 11/11 | The project's own core feature runs on all three tiers; the first build goes onto a test track (S3) |
| 9 | 17/11 · 18/11 | Beta test: testers are enrolled, and the students keep a bug list and write a test report (S4) |
| 10 | 24/11 · 25/11 | UAT and submission: the students write the UAT report and the deployment diagram, and the app is submitted for review (S5) |
| 11 | 01/12 · 02/12 | Release and hardening: the students apply the review fixes, the app goes live on the store and the final README is written (S6) |
| 12 | 08/12 · 09/12 | Closure: poster and defence rehearsal |
| 13 | 15/12 · 16/12 | **Project defence (presentations)** |
| 14 | 22/12 · 23/12 | **Project defence (presentations)** |
| | | **Final Exam** |

*Note: the weekly plan may be modified according to the progress of the class.*
