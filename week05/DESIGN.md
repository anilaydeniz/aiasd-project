# Design — the title from PROPOSAL.md §1

> **You write this file.** An assistant may propose components; the decisions are yours:
> which parts your product has, what each one does, and which requirements each one serves.
>
> **Bu dosyayı siz yazarsınız.** Bir asistan bileşen önerebilir; kararlar sizindir: ürününüzün
> hangi parçalardan oluştuğu, her birinin ne yaptığı ve her birinin hangi gereksinimlere
> hizmet ettiği.
>
> Delete these quoted lines before you commit. / Commit etmeden önce bu alıntı satırlarını silin.

<!--
IN THE LECTURE: the Components table, with at least four components.
BY SATURDAY: every functional `must` requirement is served by at least one component, and
the Architecture diagram is drawn in Mermaid.

A component is one part of your system with one job: the server's login, the server's
part for your main feature, the database, the e-mail sender, the web client, the mobile
client. Name each one as you will name it in your code.

Each row: the name, what it does in ONE sentence, and the REQ ids it serves, exactly as in
week02/requirements.json. A component that serves no requirement must have a reason to
exist; if it has none, it does not belong here.

WEAK:   | Backend | Does everything | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |
STRONG: | Server: bookings | Saves a booking for a free slot of 30 to 120 minutes and refuses a busy one | REQ-002, REQ-003 |

The first row is the login that every project shares (REQ-001). Keep it; adjust the words.
Replace each [bracketed] row with one of yours, and add as many rows as you need.

Bu tablonun Türkçe açıklaması ASSIGNMENT_05_TR.md §1'dedir.
Delete this comment when you are done.
-->

## Components

| Component | What it does | REQ |
|---|---|---|
| Server: login | Sends a 4-digit code to an e-mail address, checks it and gives a token | REQ-001 |
| [component] | [what it does, in one sentence] | [REQ-…] |
| [component] | [what it does, in one sentence] | [REQ-…] |
| [component] | [what it does, in one sentence] | [REQ-…] |

## Architecture

<!-- By Saturday: your components, and an arrow for every "talks to". GitHub draws it.
     The two lines that begin with %% are an example: delete them and write your own. -->

```mermaid
flowchart LR
    %% web[Web client] --> login[Server: login]
    %% login --> mail[E-mail sender]
```
