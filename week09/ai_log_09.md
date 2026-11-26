# Week 9 — AI log

## 1. My assistants

| Assistant | Model | Free or paid | Plan |
|---|---|---|---|
| Antigravity | Gemini 2.5 Pro | paid | Google AI Pro |

## 2. Every use of an assistant this week

| What for | Assistant | What I asked, in short | How I checked it | What I did with it | Commit |
|---|---|---|---|---|---|
| Brevo email REST bridge on Render | Antigravity | how to send OTP emails over HTTPS port 443 without SMTP socket block | tested POST /auth/code on phone; verified OTP received in Gmail | kept the httpx post implementation | e6ae30d |
| Beta error boundary and production API | Antigravity | wrap mobile screens with React ErrorBoundary and point to Render API | ran mobile app on iPhone; triggered deliberate error; checked boundary | kept error boundary and api configuration | 6842b78 |
| Resolving BUG-01 and BUG-02 with designer v2 UI | Antigravity | fix bottom tab overlap on J7 Prime and keyboard hiding chat input | checked diff; verified layout padding and KeyboardAvoidingView on phone | kept safe area padding and keyboard avoidance | af917a3 |
| Resolving BUG-03 and BUG-04 outside tester issues | Antigravity | fix portion counter reset and handle AI 503 timeout gracefully | tested portion prep on mobile; verified counter reset to 1; verified 20s timeout | kept portion reset state and timeout handler | c9c1202 |
| Mock chatbot unit tests and report endpoint | Antigravity | write headless mock unit tests for REQ-009 and POST /chat/report | ran pytest --cov=server; verified 29 passed and 85% coverage | kept test functions and report route | 4e77eb9 |
| Closed testing S4 and test report | Antigravity | structure store.json S4 closed testing track and test report metrics | checked check_deliverables.py tr output; verified table format | kept store track and test report | a70eb22 |

## 3. How I worked with assistants this week

This week I worked with Antigravity as an interactive coding pair for resolving beta test findings, updating mobile design layouts, and implementing server test suites. When dealing with layout collisions on physical Android phones and external LLM timeouts, I asked Antigravity to suggest focused fixes that adhere to our existing API contracts. I checked every proposal by inspecting git diff line by line and running our pytest test suite and deliverable checker. Antigravity was especially helpful for setting up mock unit tests and measuring server coverage, while I personally managed device testing and tester coordination.

## 4. What I did without an assistant

I personally coordinated with all 5 classmate testers in the lab and 6 outside testers on WhatsApp, collected their real feedback screenshots, identified the bugs, and configured Google Play Console closed testing track S4.

## 5. Next week

Next week I will test edge cases across more physical screen resolutions before finalizing the production build for store review.

## 6. Before this course and now

Before this course, I used AI tools mostly to generate standalone code snippets without paying attention to git commit discipline, test contracts, or error handling. Now I approach AI with engineering rigor: verifying changes against automated checkers, writing contract-driven unit tests, and maintaining an auditable development trail.
