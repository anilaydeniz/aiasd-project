---
marp: true
paginate: true
---

<!--
WEEK 3 — YOUR 5-MINUTE PITCH, SIX SLIDES                      3. HAFTA — 5 DAKİKALIK SUNUMUNUZ, ALTI SLAYT

This file IS your slide deck. Each "---" starts a new slide.   Bu dosya sunumunuzun kendisidir. Her "---" yeni bir slayt.
Open it in VS Code with the "Marp for VS Code" extension        VS Code'da "Marp for VS Code" eklentisiyle açın (sağ üstte
(preview button top right) and present from your own laptop.    önizleme düğmesi) ve kendi bilgisayarınızdan sunun.
Export to PDF or PPTX from the same button if you prefer.        İsterseniz aynı düğmeden PDF ya da PPTX'e aktarın.

WRITE IT YOURSELF. No AI for this file — not the text, not       KENDİNİZ YAZIN. Bu dosyada yapay zekâ yok — ne metin, ne
the structure. Everything here is about YOUR life and YOUR       yapı. Buradaki her şey SİZİN hayatınız ve SİZİN
people; an assistant cannot know it. In the group, and in        çevreniz; bir asistan bunu bilemez. Grupta ve derste
class, I will ask about any slide.                               herhangi bir slayt hakkında soru sorabilirim.

Replace every line in [brackets]. Keep each slide short:         Köşeli parantezli her satırı değiştirin. Slaytlar kısa
you are talking, the slide is only the skeleton.                 olsun: siz konuşuyorsunuz, slayt yalnızca iskelet.
Delete this comment when you are done.                           Bitince bu yorumu silin.
-->

# [Product name]

**[One sentence: who gets what, in plain words — the §2 sentence, no shorter.]**

[Your name] · [your programme] · Week 3

---

## 1. The last time it happened — to me, or in front of me

<!-- A real moment, not a category. Yours, a friend's at the university, or
     someone's in your social circle — but one you saw. Date, place, who, what
     they were trying to do, what they did instead, what it cost. If you cannot
     name the last time, it is not your problem — change the project.
     Gerçek bir an, bir kategori değil. Sizin, üniversitedeki bir arkadaşınızın
     ya da sosyal çevrenizden birinin — ama gördüğünüz bir an. Tarih, yer, kim,
     ne yapmaya çalışıyordu, onun yerine ne yaptı, neye mal oldu. Son seferi
     söyleyemiyorsanız bu sizin sorununuz değildir — projeyi değiştirin. -->

- **When:** [date, roughly]
- **Who / where / doing what:** [...]
- **What they did instead:** [...]
- **What it cost:** [minutes, money, a missed thing]

---

## 2. Five people who will test it in Week 9

<!-- Real people in your reach — classmates, family, a club, a shop you use.
     Name and how you know them is enough. These are the users of your
     User Acceptance Test in Week 9; you will come back to this list.
     Erişebildiğiniz gerçek kişiler — sınıf arkadaşı, aile, kulüp, kullandığınız
     bir dükkân. Ad ve nereden tanıdığınız yeter. 9. haftadaki kullanıcı kabul
     testinin kullanıcıları bunlar; bu listeye geri döneceksiniz. -->

| # | Name | How you know them | Why they have the same problem |
|---|------|-------------------|--------------------------------|
| 1 | [name] | [classmate / cousin / club / …] | [...] |
| 2 | [name] | [...] | [...] |
| 3 | [name] | [...] | [...] |
| 4 | [name] | [...] | [...] |
| 5 | [name] | [...] | [...] |

---

## 3. What it does — and what it does not

<!-- Three requirements, copied from week02/requirements.json: the same id and the
     same description, word for word — the checker compares them. Then the one
     sentence from §4 on what it will NOT do — the sentence that keeps the project
     finishable.
     Üç gereksinim, week02/requirements.json'dan kopyalanmış: aynı id, aynı açıklama,
     kelimesi kelimesine — denetleyici karşılaştırır. Sonra §4'teki "yapmayacağı"
     cümle — projeyi bitirilebilir tutan cümle. -->

1. [REQ-00x — the description from requirements.json]
2. [REQ-00x — ...]
3. [REQ-00x — ...]

**It does not:** [...]

---

## 4. The main screen

<!-- Draw it. On paper, photograph it, put the image in week03/ and link it
     here — or draw it with text boxes below. Not a tool mock-up, not AI: your
     hand, five minutes. The phone frame is 390 px wide (REQ-006).
     Çizin. Kâğıda çizip fotoğraflayın, görseli week03/ içine koyup buraya
     bağlayın — ya da aşağıya metin kutularıyla çizin. Araç taslağı değil,
     yapay zekâ değil: kendi eliniz, beş dakika. Telefon çerçevesi 390 px (REQ-006). -->

![main screen](week03/screen.jpg)

<!-- or / ya da:
+----------------------------+
|  [title bar]               |
|  [what the user sees first]|
|  [the one button]          |
+----------------------------+
-->

---

## 5. What I am not sure about

<!-- One honest doubt. The thing you would ask an experienced developer.
     Dürüst bir şüphe. Deneyimli bir geliştiriciye soracağınız şey. -->

**[The doubt, as a question.]**

[Two lines on why it worries you.]

---

## 6. Reviewers — answer these three, in writing

<!-- Leave this slide as it is. Each listener writes one sentence per question;
     you copy their sentences into week03/contributors_03.json after the round.
     Bu slaydı olduğu gibi bırakın. Her dinleyici soru başına bir cümle yazar;
     turdan sonra cümlelerini week03/contributors_03.json'a siz geçirirsiniz. -->

1. **Real?** Did they convince you this problem happens to them, and to the five people on slide 2?
2. **Usable here?** Could those five people actually use this in Week 9 — what would stop them?
3. **Too much or too little?** Which part will not be finished by Week 11 — or has the product shrunk to one screen?
