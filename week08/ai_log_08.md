# Week 8 — AI log

## 1. My assistants

| Assistant | Model | Free or paid | Plan |
|---|---|---|---|
| Antigravity | Gemini 2.5 Pro | paid | Google AI Pro |

## 2. Every use of an assistant this week

| What for | Assistant | What I asked, in short | How I checked it | What I did with it | Commit |
|---|---|---|---|---|---|
| Server chat route scaffold | Antigravity | generate initial draft for POST /chat endpoint serving REQ-009 with token auth | checked git diff to verify authentication dependency and 501 scaffold response | kept as it was for unfinished commit | 3db6f7a |
| LLM API and rate limit | Antigravity | implement 20 msg/day quota, Gemini REST API call with 20s timeout and 429/503 errors | ran pytest to test 429 quota and mocked 503 timeout; verified no secrets in repo | kept after verifying .env reading | 22780d6 |
| Mobile chat screen scaffold | Antigravity | draft React Native ChatScreen with serves comment and input layout | checked file header for serves comment and verified JSX elements render cleanly | kept as unfinished UI commit | d098801 |
| Mobile live chat integration | Antigravity | connect ChatScreen to POST /chat, add AI answer label and quota badge | tested state management and verified AI answer text badge in response container | kept and wired into navigation | c659516 |
| Server data persistence | Antigravity | design file-backed JSON database for pantry stocks, purchase orders and chat quotas | ran pytest persistence tests simulating server process restart and stock depletion | kept after passing 38 unit tests | d0a5e29 |
| Privacy policy documentation | Antigravity | draft PRIVACY.md detailing kitchen data retention and Google Gemini API integration | verified provider name Google Gemini API and checked char count over 300 | kept as it was | d17f8ed |

## 3. How I worked with assistants this week

This week I worked with Antigravity as an interactive coding pair for implementing the chatbot feature and server persistence. When adding the new POST /chat endpoint and React Native chat interface, I first asked Antigravity to generate clean scaffolds to satisfy our unfinished commit requirement, and then expanded them with real business logic. I never committed assistant output without checking git diff line by line and running our pytest test suite. Antigravity was especially helpful for structuring error handling and file-based data persistence across server restarts, while I remained in control of architectural decisions.

## 4. What I did without an assistant

I personally configured our Google Play Console closed testing track, registered the 12 testers' Google accounts, and took the authentic verification screenshot store_s3.png. I also reviewed the requirements baseline and verified the 12 mobile prototype screens.

## 5. Next week

Next week I plan to ask Antigravity to review edge cases in user input validation before implementing unit tests so we catch validation issues earlier.

## 6. Before this course and now

Before this course, I used AI tools mostly to generate quick standalone functions or answer syntax questions without paying much attention to git history or architectural constraints. Now I approach AI with strict engineering discipline: breaking work into verifiable phases, testing outputs against formal contracts and unit tests, and maintaining an accountable development log.
