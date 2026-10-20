# Week 5 — AI log

> **THE AI LOG IS WRITTEN BY A HUMAN. NO EXCEPTIONS.**
> **AI LOG KESİNLİKLE İNSAN TARAFINDAN YAZILIR. İSTİSNA YOK.**
>
> **Write this file yourself, in your own words. Outside the Evidence block and the bold
> quotes described below, no assistant is used: not to write it, not to "improve" it, not
> even for the language. A log written by an assistant earns 0.** Your English or Turkish
> is not graded.
>
> **Bu dosyayı kendiniz, kendi cümlelerinizle yazın. Evidence bloğunun ve aşağıda anlatılan
> kalın alıntıların dışında asistan kullanılmaz: ne yazmak için, ne "düzeltmek" için, dil
> için bile. Asistana yazdırılmış bir günlük 0 puan alır.** İngilizceniz ya da Türkçeniz
> notlanmaz.
>
> Two kinds of words, as in Week 4. Yours are plain text: every word, the grammar too. The
> assistant's are **bold**, and only where they must come from it: a phrase, one sentence or
> one line of its code that you point at. Each bold phrase also stands, letter for letter,
> in the Evidence block, under `AI:`. Bold is for nothing else.
>
> İki tür söz var, 4. haftadaki gibi. Sizin sözleriniz düz yazıdır: her kelime, dil bilgisi de.
> Asistanın sözleri **kalındır** ve yalnızca asistandan gelmesi gereken yerde: işaret ettiğiniz
> bir ifade, tek bir cümle ya da kodundan tek bir satır. Her kalın ifade Evidence bloğunda,
> `AI:` altında, harfi harfine de bulunur. Kalın yazı başka hiçbir şey için kullanılmaz.
>
> **Worth 2 points, and a person reads it.** It is not graded on how much you used AI, but
> on whether you ran what the assistant gave you and looked at what really happened. Delete
> these quoted instructions before you commit.

<!--
THIS WEEK'S TASK — verify by running (AI_Doc5 §2). Short answers, one per heading.
1. Choose one route of server/ or one test of server/tests/ that the assistant wrote for you.
2. BEFORE you run it, write what you expect, with the test case id: "TC-001-02 must fail
   with 501 today, because the login is built in Week 6."
3. Run it yourself: python -m pytest, or the server and /docs, or curl. Copy the command and
   its output, untouched, into the Evidence block under TERMINAL:.
4. Say what you saw, and one line of the assistant's code that you changed or refused, and why.

WEAK:   "I asked ChatGPT for the login routes. They work."
STRONG: "Before running: TC-001-01 must fail with 501 until Week 6. pytest said
         1 failed, 1 passed, but the failure was assert 404 == 200, not 501: the
         assistant had written the path as **"/auth/send-code"**, while my api.md says
         /auth/code. I changed the path by hand; now the failure is assert 501 == 200,
         the right reason. It had also added **hashed_password: str** to the model, which
         REQ-001 forbids; I deleted the line."

Delete this comment when you are done.
-->

## The assistant, and the code I asked it for

[Which assistant; which route or which test; one sentence.]

## What I expected, written before I ran it

[With the test case id.]

## The command I ran, and what I saw

[The command as you typed it, and in your words what the output showed.]

## The line I changed or refused, and why

[One line of the assistant's code, what it did, and what you did about it.]

## Evidence — the exchange and the terminal output

```text
ME:
[prompt]

AI:
[answer]

TERMINAL:
[output]
<!-- ME: your prompt. AI: the answer exactly as it came. TERMINAL: the command you typed and
     its output, down to the last line, the one that counts the tests. Nothing removed,
     nothing corrected. Several rounds: repeat ME: and AI:. -->
```
