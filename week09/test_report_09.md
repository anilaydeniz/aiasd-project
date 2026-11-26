# Week 9 — Test report

## 1. The testers

| Tester | Classmate or outside | When (lecture / by Saturday) |
|---|---|---|
| 220504023 | Classmate | In the lecture |
| 220504008 | Classmate | In the lecture |
| 220504031 | Classmate | In the lecture |
| 220504029 | Classmate | In the lecture |
| 220504048 | Classmate | In the lecture |
| Ali A. | Outside | By Saturday |
| Selahattin A. | Outside | By Saturday |
| Gönül Y. | Outside | By Saturday |
| Hikmet Y. | Outside | By Saturday |
| Zeynep G. | Outside | By Saturday |
| Murat Ç. | Outside | By Saturday |

## 2. What was tested

We tested build version 1.0.1 (2) and fix update 1.0.2 (3). Test cases executed: TC-001-01 (OTP e-mail login), TC-002-01 (recipe portion prep and stock depletion), TC-003-01 (supplier purchase order replenish), and TC-009-01 (chef AI chat assistant). Also conducted unrestricted free use across all screens.

## 3. The numbers

| Runs | pass | fail | blocked | Bugs high / medium / low | Fixed |
|---|---|---|---|---|---|
| 17 | 13 | 4 | 0 | 2 high / 1 medium / 1 low | 4 |

## 4. The three most important findings

1. BUG-01: On Samsung Galaxy J7 Prime, the system navigation bar overlapped the bottom tab icons. Fixed in commit af917a3 by introducing safe area bottom padding in mobile/App.js.
2. BUG-02: On Realme 8, the onscreen software keyboard hid the text input in the chat screen. Fixed in commit af917a3 by wrapping the chat screen in KeyboardAvoidingView in mobile/ChatScreen.js.
3. BUG-03: On Tecno Spark 7, asking the AI assistant triggered HTTP 503 service unavailable due to Gemini API timeout. Fixed in commit c9c1202 by setting a 20-second timeout, error handling, and providing fallback kitchen context in server/chat.py.

## 5. What surprised me

I was surprised that older Android 10 and 11 phones like Oppo A5 and Tecno Spark 7 ran the Expo client smoothly without lag, whereas physical soft keyboards and Android navigation bars caused unexpected layout overlaps on newer devices.

## 6. The chatbot's tests

Server test coverage measured with `pytest --cov=server --cov-report=term` reached 85% across all 29 passing server test cases. The chatbot's server-side test cases with mock model are TC-009-02, TC-009-03, TC-009-04, and TC-009-05. The content reporting endpoint test is TC-010-01.
