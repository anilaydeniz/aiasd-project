# Working with AI tools — what they are, what they cost, and how to spend them

*This is a methodology reading. Part I is a map of the tools as they stand at the start of the
2026–27 autumn term. Part II describes the working habits, and those habits change far more
slowly than the tools. The facts in Part I (the model names, the prices and the usage limits)
were checked against the vendors' own web pages on 20 September 2026, and they will be wrong
by spring. Treat them as a snapshot, and treat the pattern behind them as the thing to learn.
This document is handed out as Doc 4, and it is also presented in
Week 1 as a slide deck. The document and the slides say the same things in the same order, so
that a student who read this and a student who listened to the lecture have heard the same
course.*

*It is one of three Week 1 readings, and each reading has one job. **Doc 2, AI Technical
Background**, explains how the machine works: it covers neurons, attention, tokens, embeddings,
sampling and RAG (retrieval-augmented generation, the technique of looking up relevant text and
handing it to the model together with the question). **Doc 3, Development Environment and
Tools**, sets up your machine and walks through every tool you will use. This document is about
the tools as products: it explains what they are, what they cost, how they ration your use of
them, and how to spend them well. Where the three documents touch, this one points at the other
two rather than repeating them.*

---

# Part I · The map

## 1. Three consequences of how a language model works

Doc 2 (§8–9) explains the mechanism: a model takes a sequence of tokens (the short pieces of
text, each roughly three quarters of a word, that a model reads and writes) and returns a
probability for the next one, and everything you experience is that single step repeated many
times. This document takes the mechanism as already understood and draws out the three
consequences that decide how the products behave and what they cost. If the previous sentence
was not obvious to you, read Doc 2's sections 6 to 9 first; they are short.

**It has no memory.** The model is a fixed set of weights (the numbers inside the model that
were set during training and never change afterwards). It does not learn from your
conversation, it does not remember yesterday, and it does not know what you said three turns
ago unless the application puts those turns back in front of it. The "memory" features that
some products advertise are really the application saving notes and inserting them again at
the start of each conversation. This is also why a long conversation costs more with every
turn, which Part II explains in detail.

**It has a window.** A model can only attend to a limited number of tokens at once, and that
limit is called the *context window*. Current frontier models (the largest and most capable
models each vendor sells) offer 200 thousand to a million tokens. That sounds unlimited, and it
is not: a large codebase, or a long chat with pasted files, fills the window, and the model's
quality degrades well before the hard limit is reached. The window is a budget, not a capacity.

**It is trained to a date.** The weights were frozen months before you use them. If you ask
about anything that happened after that date, the model either does not know, or, which is
worse, it answers confidently from a world that no longer exists. Products add web search on
top of the model to compensate for this. The model itself is a photograph of the past.

"Reasoning" or "thinking" models are the same mechanism, made to write out intermediate steps
before answering and given more compute (processing time on the vendor's hardware) to do it.
They are better at problems that have a right answer, such as a mathematical proof, a bug or a
timetable, and they are slower and more expensive at everything. Most vendors now let you
choose how much effort to spend on each question. You should make that choice consciously.

## 2. Four kinds of tool, not four brands

The names you will hear, which are Claude, ChatGPT, Gemini, Copilot, Cursor, Replit and Ollama,
are not four competitors selling the same thing. They are different *kinds* of product, and the
useful question is which kind you need for the task in front of you.

| Kind | What it is | Examples | Good for | Poor at |
|---|---|---|---|---|
| **Chat application** | A conversation in a browser or an app, in which the model sees only what you paste into it | Claude, ChatGPT, Gemini | Explaining a topic, drafting text, reviewing a snippet of code that you pasted, and discussing a design | Any task that needs your whole project in view |
| **Coding agent** | The model runs in your project folder or in your terminal; it reads and edits files, runs commands and opens pull requests (proposed sets of changes submitted for review on GitHub) | Claude Code, Codex, GitHub Copilot's agent, Cursor | Changes that span several files, writing tests, refactoring (restructuring code without changing what it does), and requests such as "make CI green" (make the automated build and test pipeline pass) | Vague goals, because it will do *something*, and it will do it quickly |
| **Cloud development environment with an agent** | A whole IDE (integrated development environment, the editor and its surrounding tools) and web hosting in the browser, with an agent that builds and deploys the application | Replit | Getting a prototype live in an afternoon with nothing installed on your machine | Helping you understand what it built; its costs also scale with your ambition |
| **Local model runtime** | A program that runs open-weight models (models whose trained weights are published for anyone to download) on your own machine, so that nothing leaves it | Ollama (also LM Studio, llama.cpp) | Privacy, offline work, learning what a model *is*, and embedding pipelines (programs that turn text into numeric vectors for search) | Frontier-level quality, and any model that your laptop's memory cannot hold |

You will use at least three of the four kinds this term. You will use chat applications from
Week 1, Ollama from Week 3, and a coding agent from the moment your project has more than one
file.

## 3. The vendors, and the models inside them

Each vendor sells a *family* of models, tiered by size and price. The tiers matter more than
the brand names: the largest model in one family is usually closer to the largest model in
another family than it is to the smallest model in its own.

### Anthropic — Claude

Anthropic currently sells four models. All of them accept text and image input, and they offer
a 200K–1M token window:

| Model | Positioning | API price, per million tokens in / out |
|---|---|---|
| Claude Fable 5.1 | The smartest model; it is meant for demanding reasoning and long agentic work, and it is slower | $10 / $50 |
| Claude Opus 5 | The recommended default for complex coding | $5 / $25 |
| Claude Sonnet 5 | Speed and intelligence are balanced; this is the workhorse | $2 / $10 |
| Claude Haiku 4.5 | The fastest and cheapest model; it has a 200K window | $1 / $5 |

(An API, or application programming interface, is the way a program rather than a person
talks to the model; API prices are charged per token used.) Read the price column as a ratio,
not as a bill: the top model costs **ten times** the bottom one for the same conversation. On a
subscription you do not pay per token, but your usage allowance drains at that same ratio.
Asking the smartest model to rename a variable is not wrong; it is simply ten times the price
of asking the fastest one.

The consumer plans are these. **Free** gives you chat, web search, file uploads and artifacts
(documents or small programs that the assistant writes and shows beside the conversation).
**Pro** at $17–20 a month adds Claude Code, projects, the larger models and more usage.
**Max** from $100 gives 5× or 20× Pro's usage. The same account and the same allowance cover
the chat app, the desktop app and Claude Code, so a heavy Claude Code afternoon empties your
chat allowance too.

### OpenAI — ChatGPT

OpenAI's offer has the same shape. There is a free tier that runs the mid-size model, a paid
**Plus** tier that adds the frontier models and the reasoning modes, and an expensive **Pro**
tier with roughly five times Plus's usage and the largest context. OpenAI's model names change
faster than any other vendor's; at the time of writing, the free tier runs GPT-5.6 and Plus
adds GPT-6. Codex is OpenAI's coding agent, and the free tier gives limited access to it.

### Google — Gemini

Google's free tier runs on the fast model (Flash) and gives rationed access to the large one
(Pro). **AI Plus** at about $5 doubles the free limits; **AI Pro** at about $20 gives 4× the
free limits and full access to Gemini 3 Pro; **AI Ultra** from $100 gives up to 20×. Google's
advantage is integration, because Gemini is built into Docs, Drive, Gmail and Android, and it
also offers a very large context window.

**Students:** Google has offered a free year of AI Pro to college students. Eligibility depends
on the country and changes over time; check the current offer before you assume that it
applies in Turkey.

### GitHub Copilot

Copilot is the coding assistant inside VS Code, JetBrains and GitHub itself. The **Free** tier
gives 2,000 completions (suggested pieces of code that appear as you type) a month and a small
chat and agent allowance, on models that include Claude Haiku 4.5 and GPT-5 mini. **Pro** at
$10 gives unlimited completions plus a monthly credit for the premium models. **Pro+** at $39
gives the largest models and four times the usage.

**Students:** the GitHub Student Developer Pack includes **Copilot Student**, which gives you
unlimited completions, an allowance of AI credits, and limited chat and agent use, free for as
long as you are a verified student. If you have not claimed the pack yet, do it this week; it
is the single best-value item in this document.

### Replit

Replit is not a model vendor. It is a cloud IDE whose **Agent** uses the frontier models above
to build and deploy applications. **Core** at $18–20 a month includes about $20 of model usage;
**Pro** at $90–100 includes $100 of model usage and parallel agents. Replit is the place where
the following scene happens: a student has an idea at lunch, describes it to the Agent, and
the application is live on the web by dinner. It is also the place where students most often
hand in something they cannot explain. Use it, and read what it wrote.

### Ollama — and the open-weight models

Ollama is a program you install. When you type `ollama run llama3.1`, Ollama downloads an
open-weight model and answers you from your own machine, and nothing is sent anywhere. Local
models are free, for ever, with no session limit. (Ollama also sells a cloud tier, at $20 a
month for $60 of hosted usage, for models that are too large to run at home.)

The models themselves come from the open-weight families:

| Family | Publisher | Sizes you will meet |
|---|---|---|
| Llama 3.x | Meta | 1B, 3B, 8B, 70B |
| Qwen 2.5 / 3 | Alibaba | 0.6B to 235B |
| Gemma 3 | Google | 270M to 27B |
| Mistral | Mistral AI | 7B and up |
| DeepSeek-R1 | DeepSeek | 1.5B (distilled) to 671B |
| Phi 3 / 4 | Microsoft | 3.8B, 14B |

The "B" stands for billions of parameters (the individual numbers that make up the weights),
and it is the figure that decides whether a model runs on your laptop at all. A model
quantised to 4 bits (stored with its numbers rounded to a coarser precision so that it takes
less memory; Doc 2 §11 explains quantisation) needs roughly **0.6 GB of memory per billion
parameters**, plus room to work. The course has one rule about this, and it is the same in
every document and on every slide: **16 GB of RAM → a 7–8B model; 8 GB → a 3B model; less →
1.5B.** The same rule as a table:

| Model size | Memory needed | Runs on |
|---|---|---|
| 1–3B | 1–3 GB | Anything; it is fast and noticeably limited |
| 7–8B | 5–6 GB | Any laptop with 16 GB RAM; this is the sweet spot for this course |
| 14B | 9–10 GB | A 16 GB machine, uncomfortably; a 24 GB machine, well |
| 27–32B | 18–22 GB | 32 GB machines, or Apple Silicon with unified memory |
| 70B | 40+ GB | Not a laptop |

Speed follows memory bandwidth (the rate at which the processor can read data from memory).
Apple Silicon Macs are unusually good at this because their GPU (graphics processing unit,
the chip that does the model's arithmetic) shares the system memory; this shared arrangement
is what "unified memory" means in the table. A Windows laptop without a discrete GPU (a
separate graphics chip with its own memory) will run an 8B model at a few words per second,
which is usable for a chatbot and painful for a long generation.

An 8B local model is not a frontier model, and it will not become one. What it is, is yours:
it is private, it is free, and it is honest about what a language model actually is when
nobody has wrapped it in a product. Week 3 is built on that.

## 4. What money buys

It is tempting to read the three price points, which are free, about $20 and about $100, as
three sizes of the same bucket. They are not. Tokens are the *last* thing a subscription buys.
The first things it buys are capabilities, and they are the same seven at every vendor,
whether the tiers are called Claude Free / Pro / Max, ChatGPT Free / Plus / Pro, Gemini Free /
AI Pro / Ultra, or Copilot Free / Pro / Pro+.

| What changes | Free | About $20 a month | About $100 a month |
|---|---|---|---|
| **Which models** — the tier decides intelligence before anything else | The mid model; the frontier one is rationed or absent | The frontier model, and the reasoning modes | The same models at higher effort, and the newest ones first |
| **A coding agent** — the difference between advice and work done in your files | A taste: limited Codex, or Copilot's 2,000 completions | Claude Code, Codex, Copilot's agent | Several agents in parallel; 4× and more agent usage |
| **Memory of your project** — what you stop re-typing every conversation | You paste it again each time | Projects, memory, custom GPTs, connectors | The same, with the largest context (ChatGPT Pro: 400K) |
| **Where it can act** — the chat window is the smallest room it works in | The chat window | Your editor, your browser, Docs and Office | The same |
| **Output and context size** — how much it reads at once and how much it may say | Standard | Standard | Higher output limits, and the largest windows |
| **When everyone is online** — capacity is finite and somebody goes last | Last in the queue | Normal | Priority at peak hours |
| **How much you can use** — the token axis, one of seven | One unit | Roughly five units | Five to twenty times the $20 tier |

Read the rows from top to bottom, because that is their order of importance for this course.

**Which models.** On a free tier you are usually talking to the mid-size model, and the
frontier one is rationed. So a judgement of the form "this AI is not very good", made on a free
tier, is a judgement about the mid model. Say which model you used when you report a result;
it is half the result.

**A coding agent.** This is the row that matters most here. An agent is not a better chat; it
is a different kind of tool, because it reads your files, edits them and runs your tests.
Every vendor puts it behind the first paid tier. The one exception is Copilot Student, which is
why §6 tells you to claim the pack before Week 2.

**Memory of your project.** Projects, memory and connectors (links from the assistant to your
other tools, such as your e-mail or your documents) are what stop you re-typing your setup in
every conversation. On Claude they are also the cached content that does not count against your
allowance (cached content is content the vendor has stored once and does not charge for
again), so this row and the last row are related.

**Where it can act.** The paid tiers move the model out of the chat window and into your
editor, your browser and your documents. That is a change of kind, not of degree: the model can
now see what you see instead of only what you paste.

**Output and context size, and the queue.** These two rows only change at the top tier. They
matter to someone who is running long agent jobs on a deadline afternoon, when everyone else
is also online. They do not matter to a student in Week 2.

**How much you can use.** The token axis is the one everybody talks about, and it is placed
last on purpose. Multiply the free allowance by five and you have the $20 tier; multiply that
by another five to twenty and you have the $100 tier. The difference is real, and it is the
smallest of the seven differences in kind.

## 5. The limits, and why they are shaped the way they are

Every hosted assistant rations you, and the rationing has the same two-layer shape everywhere,
because every vendor is solving the same problem: a few users who never stop would otherwise
consume the capacity meant for everyone.

**The session window.** Claude's is the clearest example. A **five-hour window** opens with
your first message and closes five hours later, whether you used it or not. Within that window
you have a fixed allowance. When you hit the allowance, you wait for the window to end. Gemini
and ChatGPT ration per model over shorter rolling windows. The mechanism differs, but the
experience is the same: you hit a wall, and then you watch a countdown.

**The weekly cap.** On paid plans, a second allowance sits above the sessions and resets every
seven days. It exists to stop the pattern in which a user drives every session to the wall,
all week long. If you are on a paid plan, this is the limit that bites during a project
deadline.

**What drains them.** Messages do not drain the limits; *tokens* do, and they are weighted by
model. Concretely, from the vendors' own guidance, the following things drain your allowance.
Long conversations drain it, because the whole history is re-sent every turn. Attachments and
images drain it. The larger models drain it faster. Tool use, such as web search and code
execution, drains it. Long generations drain it. A screenshot of an error costs more than the
error text; the smartest model costs ten times the fastest; and, in an illustrative long chat,
turn forty costs turns one to thirty-nine all over again. Part II is entirely about this.

**What does not.** On Claude, content in a Project is cached and does not count when it is
reused, which is exactly why Part II tells you to put your standing facts in one. Copilot's
code completions never touch its credit allowance. Ollama has no meter at all.

One practical note: the Claude allowance is shared across the chat app and Claude Code.
Students who discover Claude Code in Week 4 tend to discover the session wall the same
afternoon. That is not a malfunction. It is the tool telling you that an agent reading your
whole project is expensive, and that you should tell it *which* files to read.

## 6. What this course expects you to have

You do not need to pay for anything.

- **Two chat assistants** on their free tiers. Week 1 asks you to use two and compare them,
  and it does not matter which two you choose.
- **GitHub Copilot Student**, which is free through the Student Developer Pack. Claim it before
  Week 2.
- **Ollama** with one 7–8B model, installed before Week 3. If your laptop has 8 GB of RAM,
  install a 3B model and tell me; we will work around it.
- **A coding agent** from Week 4 or so. Copilot's agent is included in the student plan. Claude
  Code and Codex need a paid plan or API credits; use them if you have them, not because you
  think you must.

If you do pay for one thing, pay for the tool you will use for the most hours a week, not the
one with the best benchmark score. For most students in this course that is a coding agent,
not a chat app.

## 7. How to read the next announcement

Everything in sections 3 to 5 will have changed by the time you read this in a later term.
The following things will not have changed:

- Vendors sell **tiers**, and the top tier costs about ten times the bottom one.
- Limits are **token-weighted** and **two-layered**, with a short window and a long one.
- Whatever you paste is re-sent every turn.
- Open-weight models trail the frontier by a year or so and are free for ever; the parameter
  count decides whether they run on your machine.
- The student offers are the best deal on the page and the first thing to check.

When a new model is announced, ask three questions: which tier is it replacing, what does it
cost relative to the tier below, and what is its window. Those three numbers tell you how to
use it. The benchmark chart does not.

---

# Part II · The habits

## 8. Why your assistant runs out, and what it costs you

Every assistant you will use this term, whether it is Claude, ChatGPT, Gemini or Copilot,
charges in the same currency: **tokens**. A token is roughly three quarters of a word, or a few
characters of code. Your usage limit is measured in tokens, not in messages, so the question
"how many questions can I ask today" has no fixed answer. Ten careless questions can cost more
than a hundred careful ones.

The part that surprises people is that a conversation has no memory of its own. The model does
not remember your earlier turns; instead, the application **re-sends the entire conversation**
with every new message. In a long session, turn 40 pays for turns 1 through 39 all over again.

That single fact explains most of what follows.

---

## 9. The one habit that matters more than all the others

**Start a new conversation when you start a new task.**

Imagine a student who has a forty-turn thread about her Week 2 requirements and then writes
"now help me with a CSS bug" (CSS is the language that controls how a web page looks) in the
same thread. She pays for all forty earlier turns on every message about CSS, and the model is
worse at the CSS, because it is reading forty turns of irrelevant context while it looks for
the point.

You are not being frugal at the model's expense here. Short, focused conversations get better
answers. Long ones drift, and the assistant keeps referring back to decisions you abandoned
twenty turns ago.

A rough rule: when you catch yourself writing "forget what I said earlier about…", that
conversation is over. Open a new one and paste in the three facts that still matter.

---

## 10. Feed it text, not pictures of text

A page of plain text costs a few hundred tokens. **The same page as a screenshot or a scanned
PDF costs one to two orders of magnitude more** (that is, ten to a hundred times more), because
an image is charged by its area, not by how much it says. In addition, the model has to read
the letters out of the pixels before it can think about them, so you pay more for a worse
starting point.

In practice:

| Instead of | Do this |
|---|---|
| A screenshot of a red error in your terminal | Copy the error text and paste it |
| A screenshot of your code | Paste the code, or give the file |
| A scanned PDF of a paper | Find the text version, or paste the two paragraphs you care about |
| A photo of the whiteboard | Type the six lines that were on it |

Screenshots are the right tool for exactly one thing, which is when the **layout** is the
question. If you ask "why is this button overlapping on a narrow screen", the question is
about a picture, so send a picture. If you ask "why does this traceback happen" (a traceback
is the list of calls that a program prints when it crashes), the question is about text, and
it is always text.

---

## 11. Ask for the format you are actually going to use

Markdown (plain text with simple marks, such as a hash sign for a heading and asterisks for
emphasis) is the
cheapest thing an assistant can produce, because it is simply text. A `.docx` or `.xlsx` file
is a zip archive of XML (compressed folders of structured mark-up files). The assistant cannot
write one directly, so it writes a *program* that builds one, and every later change means
running that program again, or reading the file back in to see what is inside it.

So the advice is this: get the content right in markdown, and convert once, at the end, when
nobody is going to ask for another revision.

The same applies in reverse. Handing an assistant a `.docx` to read means that it has to unpack
the file before it can see a single sentence. If you wrote the file, you probably have the text
somewhere cheaper.

This is not an argument against Word files. It is an argument against *iterating* in Word
files.

---

## 12. Point, don't paste

If your assistant can see your files, as Claude Code, Copilot in an editor, or anything with a
project folder can, tell it **where** to look instead of pasting the contents. It then reads
the twenty lines it needs rather than the two thousand you pasted.

When it cannot see your files, paste the smallest thing that contains the answer: paste the
function, not the module, and the failing test, not the whole suite.

When you want a change to a long file, ask for **the change**, not the file. The request "show
me the diff for the `render` function" (a diff is a listing of only the lines that changed)
costs a fraction of the request "rewrite `app.py` with this fixed", and it is far easier to
review, which is the part that actually protects you.

---

## 13. Batch your questions

Because the whole conversation is re-sent each turn, three follow-up messages cost noticeably
more than one message that contains three questions. If you already know that you have four
things to ask about the same code, ask all four at once.

The corollary is that you should think before you send. A vague question produces a vague
answer, and then you pay again for the clarification. Week 1's assignment asks you to notice
this by asking the same question twice, once vaguely and once with the constraints spelled
out. The cost difference is as real as the quality difference.

---

## 14. Write down what you keep re-explaining

If you find yourself typing "this is a Streamlit app, Python 3.12, and I am using FAISS for
retrieval" at the start of every conversation (Streamlit is a Python library for building web
interfaces, and FAISS is a library for searching through embeddings), put that text in a file
the assistant reads automatically. Depending on the tool, that file is `CLAUDE.md`, a project
instruction, or a pinned note. You stop paying for the text in every new thread, and you stop
forgetting to mention it.

Your `ai_log_NN.md` is doing something related and worth more: it is the record of what went
wrong and how you caught it. That file is for you and for Week 12, not for the model.

---

## 15. What does not help

- **"Be brief."** This instruction is worth adding when you want a short answer, but the output
  is the small half of the bill. Your conversation history is the large half.
- **Compressing your wording.** Dropping "please" saves a token. Starting a fresh conversation
  saves thousands.
- **Avoiding the assistant to save quota.** The point of this course is to use these tools
  well. Being economical means not paying for waste, such as forty irrelevant turns, a
  screenshot of text, or a file pasted whole. It does not mean asking fewer real questions.

---

## 16. The short version

1. New task, new conversation.
2. Text, never a picture of text.
3. Markdown while you iterate; convert at the end.
4. Point at files; ask for diffs, not rewrites.
5. Ask your four questions in one message.
6. Put the standing facts in a file.
