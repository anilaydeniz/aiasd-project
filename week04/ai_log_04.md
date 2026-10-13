# Week 4 — AI log

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
> Two kinds of words, and the reader must see which is which.
> Yours are plain text: every word, the grammar too.
> The assistant's are **bold**, and only where they must come from the assistant: a phrase
> or one sentence of its answer that you point at (what it claimed, what it added). Each
> bold phrase must also stand, letter for letter, in the Evidence block, under `AI:`.
> Bold is for nothing else: no bold for emphasis, headings or labels.
>
> İki tür söz var ve okuyan hangisinin hangisi olduğunu görmeli.
> Sizin sözleriniz düz yazıdır: her kelime, dil bilgisi de.
> Asistanın sözleri **kalındır** ve yalnızca asistandan gelmesi gereken yerde: cevabında
> işaret ettiğiniz bir ifade ya da tek cümle (ne iddia ettiği, ne eklediği). Her kalın ifade
> Evidence bloğunda, `AI:` altında, harfi harfine de bulunmalı. Kalın yazı başka hiçbir şey
> için kullanılmaz: vurgu, başlık ya da etiket için değil.
>
> **Worth 2 points, and a person reads it.** It is not graded on how much you used AI,
> but on whether you checked the answer against criteria that you wrote first. The
> Evidence block is not optional. Delete these quoted instructions before you commit.

<!--
THIS WEEK'S TASK — acceptance criteria first (AI_Doc5 §1).
1. Choose one screen of your main flow that you ask the assistant to build.
2. BEFORE you write the prompt, copy below the requirements that this screen must meet,
   from week02/requirements.json (id, description and acceptance), and the ids of the
   test cases from week04/test_cases.json that will run on it. Add two or three things
   that you will check in the answer.
3. Put those lines into the prompt. Then measure the answer against each of them: what
   it met, what it broke, and what it added that no requirement asks for.
4. Say what you changed: the prompt, the screen by hand, or requirements.json (with a
   line in the Change log).

WEAK:   "I asked ChatGPT to make my login screen. It looked good, so I used it."
STRONG: "My criteria before the prompt: REQ-001 (a 4-digit code by e-mail, no password),
         REQ-006 (390 px, no horizontal scroll) and TC-001-02 (a wrong code shows a
         message and keeps the user on the code screen). The first answer ended with
         **All requirements are met**, but it had a password field and a **Sign in with
         Google** button, both against REQ-001, and nothing happened on a wrong code. With
         the REQ lines in the prompt, the second answer met REQ-001 but was 480 px wide, so
         I fixed the width by hand. While checking it I saw that REQ-001 does not say what
         happens after three wrong codes; I added that to its acceptance criterion (Change
         log, 2026-10-13) and wrote TC-001-03."

WHO WROTE WHAT — the reader sees it at once.
  Plain text   = you. Every word, the grammar too. You type it; no assistant, not even
                 to correct a comma. (The REQ lines you copy from requirements.json are
                 your file, so they are plain too.)
  **Bold**     = the assistant, word for word: a phrase or one sentence of its answer that
                 you point at. Only what must come from the assistant: what it claimed,
                 what it added, a line of its code (**`<input type="password">`**).
                 Each bold phrase must also stand, letter for letter, in the Evidence block.
  Nothing else is bold in this file: no bold for emphasis, headings or labels.
  Everything the assistant wrote that you do not point at stays in the Evidence block,
  under AI:. Your prompt goes there too, under ME:.
Delete this comment when you are done.
-->

## Assistant used and the screen I asked for

[...]

## My criteria, written before the prompt

[The REQ lines and the test case ids, and the two or three things you checked.]

## What the answer met, what it broke, what it added

[Criterion by criterion.]

## What I changed

[In the prompt, by hand, or in requirements.json, with the Change log line if there is one.]

## Evidence — the actual exchange

```text
ME:
[your prompt]

AI:
[the answer, untouched]
<!-- ME: is your prompt, AI: is the assistant's answer exactly as it came: nothing removed,
     nothing corrected, not even the grammar. Several rounds: repeat ME: and AI:. -->
```
