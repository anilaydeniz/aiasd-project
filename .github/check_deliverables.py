#!/usr/bin/env python3
"""
Checks this week's deliverables — the same checks the instructor runs.

A run shows one week: the current one, or the week whose number you add. Under the
list, one line says how many checks of earlier weeks still fail, so a change that
breaks Week 1 does not pass silently in Week 7 — and the list does not grow by a
screenful every week. (The instructor's own capture still reads every week from 1 and
counts only the week it is marking.)

Which week is "current" is not yours to set. It is published by the course and
read from there on every run, so the checks you see are always the checks being
run against you. The CURRENT_WEEK_CACHE.txt file is only a cache of that number, refreshed
automatically, so this still works on a train with no signal.

Run it locally before you push:
    python .github/check_deliverables.py

To look at another week — say, to confirm Week 2 still passes:
    python .github/check_deliverables.py 2

Türkçe için sonuna `tr` ekle (her şey Türkçe yazılır; not hesabı aynı checker'la, İngilizce okunur):
    python .github/check_deliverables.py tr
    python .github/check_deliverables.py 2 tr
"""

from __future__ import annotations

import ast
import json
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Normally the repository this file sits in. AIASD_ROOT overrides it, which is
# how the self-update below keeps pointing at your repository while running a
# freshly downloaded copy of itself from a temporary file.
ROOT = (
    Path(os.environ["AIASD_ROOT"]).resolve()
    if os.environ.get("AIASD_ROOT")
    else Path(__file__).resolve().parent.parent
)

# A string the published checker must contain for us to trust and run it. If a
# proxy or a captive portal hands back an HTML error page, it will not have this.
MARKER = "AIASD-CHECKER-v1"  # AIASD-CHECKER-v1

PASS, FAIL = "PASS", "FAIL"

# When a deliverable is due. Work that belongs in the lab, where you can still
# ask, is SESSION; work that is genuinely done alone afterwards — writing,
# diagrams, reflection — is DEADLINE.
#
# This is not cosmetic. Half the week's mark is taken at the end of the session,
# so checking for a diagram you were told to draw at home would mark everyone
# down for following the instructions.
SESSION, DEADLINE = "session", "deadline"

# One row per check: (week, what a pass says, PASS/FAIL, slot, what a failure says).
results: list[tuple[str, str, str, str, str]] = []


def check(week: int, name: str, ok: bool, detail: str = "", slot: str = SESSION) -> None:
    """`name` is the sentence shown when the check passes; `detail` is the sentence shown
    when it fails. Both are complete sentences with the file named in them, because
    each is printed alone on its line, after PASS or FAIL.

    A failure says what is needed, then 'Found: ...' with what is actually there, so a
    student who reads English slowly can still see both halves."""
    results.append((f"W{week}", name, PASS if ok else FAIL, slot, detail or name))


def pl(n: int, one: str, many: str | None = None) -> str:
    """The count with its noun in the right number: '1 entry', '3 entries'."""
    return f"{n} {one if n == 1 else (many or one + 's')}"


def read(path: str) -> str | None:
    p = ROOT / path
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else None


def parses(path: str) -> bool:
    src = read(path)
    if src is None:
        return False
    try:
        ast.parse(src)
    except SyntaxError:
        return False
    return True


def ai_log_path(week: int) -> str:
    """Where this week's log lives.

    One file per week, inside the week's own folder, rather than one file at the
    root with twelve sections. A student's repository freezes the day they create
    it: a twelve-week scaffold written in Week 1 can never be changed afterwards,
    while a per-week file arrives with its week and can take whatever shape that
    week needs — including not existing, for a week that does not ask for one.
    """
    return f"week{week:02d}/ai_log_{week:02d}.md"


def ai_log_evidence(week: int) -> str:
    """The pasted exchange backing this week's claim — a fenced block with content.

    An untouched template block holds only an HTML comment, which is stripped here,
    so the placeholder does not count as evidence.
    """
    text = read(ai_log_path(week)) or ""
    blocks = re.findall(r"```[^\n]*\n(.*?)```", text, re.DOTALL)
    cleaned = [re.sub(r"<!--.*?-->", "", b, flags=re.DOTALL).strip() for b in blocks]
    return "\n".join(c for c in cleaned if c).strip()


def check_ai_log(week: int) -> None:
    """Every week: a filled-in reflection, and the exchange that backs it up.

    Due at the deadline, not at the end of the session: the honest version of
    this is written once the week's work has actually happened.
    """
    path = ai_log_path(week)
    check(
        week,
        f"{path} is filled in",
        len(ai_log_section(week)) > 80,
        f"{path} must be filled in, in your own words. Found: the section is empty or untouched.",
        DEADLINE,
    )
    evidence = ai_log_evidence(week)
    check(
        week,
        f"{path} holds the real conversation, pasted in the code block",
        len(evidence) >= 80,
        f"{path} must contain the real conversation, pasted inside the code block. "
        f"Found: {pl(len(evidence), 'character')} there.",
        DEADLINE,
    )


def ai_log_section(week: int) -> str:
    """What the student actually wrote in this week's log."""
    body = read(ai_log_path(week)) or ""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)  # evidence is checked apart
    # Drop the template's own headings and bold prompt labels — an untouched file
    # is then empty, which is what "not filled in" has to mean.
    body = re.sub(r"^\s*#.*$", "", body, flags=re.MULTILINE)
    # A line that is nothing but a bold label — with or without a colon — is the
    # template's own prompt, not an answer.
    body = re.sub(r"^\s*\*\*[^*]+\*\*:?\s*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"^\s*>.*$", "", body, flags=re.MULTILINE)
    # A line that is only a [bracketed hint] is the scaffold's, not the student's.
    body = re.sub(r"^\s*(\d+\.\s*)?\[[^\]]*\]\s*$", "", body, flags=re.MULTILINE)
    return body.strip()


# ── per-week checks ──────────────────────────────────────────────────


def check_identity() -> None:
    """student.json — who you are. Nickname goes on the class board; the rest is
    for the official record and never leaves the instructor's machine."""
    raw = read("student.json")
    if raw is None:
        check(1, "student.json is in the repository root", False,
              "student.json is missing from the repository root. Restore it: it holds your student number and section.")
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        check(1, "student.json is valid JSON", False,
              f"student.json is not valid JSON ({exc}). Check the commas and the quotation marks.")
        return

    fields = ("student_id", "first_name", "last_name", "nickname", "section")
    missing = [f for f in fields if not str(data.get(f, "")).strip()]
    check(1, "student.json is fully filled in", not missing,
          f"student.json is not fully filled in. Empty fields: {', '.join(missing)}. Fill in every field.")
    if missing:
        return

    sid = str(data["student_id"]).strip()
    check(
        1,
        "student_id in student.json is a number",
        sid.isdigit() and len(sid) >= 5,
        f"student_id in student.json must be your student number, digits only. Found: {sid!r}.",
    )

    # One check, not three. Length and character set are the same requirement seen
    # from two angles, and a nickname that fails either fails for the same reason:
    # it cannot go on the board. Splitting it inflated a five-minute task into
    # three of the week's marks.
    nick = str(data["nickname"]).strip()
    usable = 2 <= len(nick) <= 20 and bool(re.fullmatch(r"[A-Za-z0-9_\-]+", nick))
    check(
        1,
        "nickname in student.json can go on the class board",
        usable,
        f"nickname in student.json must be 2-20 characters: letters, digits, - and _ only. Found: {nick!r}.",
    )

    section = str(data.get("section", "")).strip().lower()
    check(
        1,
        "section in student.json is 'en' or 'tr'",
        section in ("en", "tr"),
        f"section in student.json must be 'en' or 'tr'. Found: {section!r}. "
        "This is how your repository knows which week to check.",
    )


def week1() -> None:
    check_identity()
    proof = read("week01/setup_proof.md")
    check(
        1,
        "week01/setup_proof.md is there and long enough",
        bool(proof and len(proof) > 80),
        "week01/setup_proof.md is missing or too short. Create it and fill it in as the Week 1 assignment says.",
    )

    src = read("week01/hello.py")
    check(
        1,
        "week01/hello.py has no syntax error",
        parses("week01/hello.py"),
        "week01/hello.py is missing or has a syntax error. Create it, or run it to see the error.",
    )
    if src:
        try:
            tree = ast.parse(src)
        except SyntaxError:
            tree = None
        if tree is not None:
            nodes = list(ast.walk(tree))
            has_fstring = any(isinstance(n, ast.JoinedStr) for n in nodes)
            has_list = any(isinstance(n, (ast.List, ast.ListComp)) for n in nodes)
            has_for = any(isinstance(n, (ast.For, ast.comprehension)) for n in nodes)
            has_input = any(
                isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "input"
                for n in nodes
            )
            check(1, "week01/hello.py contains an f-string", has_fstring,
                  'week01/hello.py must contain an f-string, for example f"Hello {name}". Found: none.')
            check(1, "week01/hello.py contains a list", has_list,
                  'week01/hello.py must contain a list, for example names = ["Ada", "Alan"]. Found: none.')
            check(1, "week01/hello.py contains a for-loop", has_for,
                  "week01/hello.py must contain a for-loop, for example: for name in names: ... Found: none.")
            check(1, "week01/hello.py asks the user for input", has_input,
                  "week01/hello.py must ask the user for input with input(). Found: input() is never called.")

    notes = prose_words(read("week01/llm_notes.md") or "")
    check(
        1,
        "week01/llm_notes.md has about 300 words of your own",
        notes >= 250,
        f"week01/llm_notes.md must have about 300 words written by you. Found: {notes}. "
        "Headings, instructions and pasted blocks do not count.",
        DEADLINE,
    )

    gi = read(".gitignore") or ""
    check(
        1,
        ".gitignore covers .venv and .env",
        ".venv" in gi and ".env" in gi,
        ".gitignore must contain .venv and .env, so they are never committed. Add both lines.",
    )
    check(
        1,
        ".env.example is in the repository root",
        (ROOT / ".env.example").is_file(),
        ".env.example is missing. Create it with the NAMES of your settings only, never the secret values.",
    )
    check_ai_log(1)


PROPOSAL_SECTIONS = {  # number -> title start, as in the scaffold
    1: "Title", 2: "One-paragraph summary", 3: "Problem", 4: "Solution",
    5: "How it works", 6: "Technologies", 7: "Success criteria",
    8: "Market", 9: "Competitors", 10: "Comparison", 11: "Commercial potential",
    12: "Technical risks",
}


def proposal_sections() -> dict[int, dict]:
    """PROPOSAL.md split by its numbered `### N. Title (about L characters …)` headings.

    For each section: the character limit the heading declares, the prose under it
    (comments and fenced blocks removed) and whether a mermaid block sits under it.
    """
    text = read("PROPOSAL.md") or ""
    heads = list(re.finditer(r"^### (\d+)\. ([^(\n]+?)\s*\(about ([\d,]+) characters[^)]*\)", text, re.M))
    out: dict[int, dict] = {}
    for k, m in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(text)
        body = text[m.end():end]
        # the last section ends where the Change log begins - its lines are not §12's prose
        tail = re.search(r"^## Change log", body, re.M)
        if tail:
            body = body[:tail.start()]
        body = re.sub(r"^---\s*$|^## .*$", "", body, flags=re.M)  # part separators
        mermaid = any("%% EXAMPLE" not in blk for blk in re.findall(r"```mermaid\n(.*?)```", body, re.DOTALL))
        prose = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
        prose = re.sub(r"```.*?```", "", prose, flags=re.DOTALL)
        out[int(m.group(1))] = {
            "title": m.group(2).strip(),
            "limit": int(m.group(3).replace(",", "")),
            "chars": len(prose.strip()),
            "text": prose,
            "mermaid": mermaid,
        }
    return out


def check_proposal(week: int, numbers: range, slot: str) -> None:
    secs = proposal_sections()
    if not secs:
        check(week, "PROPOSAL.md is in the repository root with its headings", False,
              "PROPOSAL.md is missing, or its numbered headings were changed. Restore the headings from the template.", slot)
        return
    for n in numbers:
        sec = secs.get(n)
        label = f"PROPOSAL.md §{n} {PROPOSAL_SECTIONS.get(n, '')}".rstrip()
        if sec is None:
            check(week, f"{label} has its heading", False,
                  f"{label} has lost its heading, or the heading was changed. Restore the heading from the template.", slot)
            continue
        floor = 60 if n > 1 else 3
        if sec["chars"] < floor:
            check(week, f"{label} is written", False,
                  f"{label} is not written yet. Found: {pl(sec['chars'], 'character')}. Write your own text under that heading.", slot)
        else:
            # The length in the heading is an ideal, not a limit (decision of 30 Sep):
            # a longer section passes.
            check(week, f"{label} is written", True, "", slot)


def contributors(week: int) -> list[dict] | None:
    """The people who helped this week: weekNN/contributors_NN.json in Weeks 2-3; from Week 4
    the other members of the group in weekNN/group_NN.json, one file for both (6 Oct 2026)."""
    name, key = (f"group_{week:02d}.json", "members") if week >= 4 else (f"contributors_{week:02d}.json", "contributors")
    raw = read(f"week{week:02d}/{name}")
    if raw is None:
        return None
    try:
        data = json.loads(raw.lstrip("\ufeff"))
    except json.JSONDecodeError:
        return None
    items = data.get(key, data) if isinstance(data, dict) else data
    return items if isinstance(items, list) else None


def check_contributors(week: int, role: str, slot: str = SESSION) -> None:
    path = f"week{week:02d}/contributors_{week:02d}.json"
    items = contributors(week)
    if items is None:
        check(week, f"{path} is valid JSON", False,
              f"{path} is missing or is not valid JSON. Run the checker online to fetch it, and check the commas and quotation marks.", slot)
        return
    # Contributors are optional: none, one or two classmates (decided 4 Oct 2026). What
    # is listed must be real - a valid, distinct student number, the right role and a
    # sentence - but an empty list is a legitimate "I worked alone this week".
    # an untouched scaffold entry (no number, no sentence) is the same as no entry
    items = [i for i in items if isinstance(i, dict)
             and (str(i.get("student_id", "")).strip() or str(i.get("what", "")).strip())]
    ids = [str(i.get("student_id", "")).strip() for i in items]
    good_ids = [i for i in ids if re.fullmatch(r"\d{9}(-\d+)?", i)]
    check(week, f"{path} lists 0-2 classmates with valid numbers",
          len(ids) <= 2 and len(good_ids) == len(ids) and len(set(good_ids)) == len(good_ids),
          f"{path} may list at most two classmates, each with a valid 9-digit student number, all different. "
          f"Found: {pl(len(ids), 'entry', 'entries')}, {len(good_ids)} with a valid number.", slot)
    me = ""
    try:
        me = str(json.loads(read("student.json") or "{}").get("student_id", "")).strip()
    except json.JSONDecodeError:
        pass
    check(week, f"{path} does not list you", me == "" or me.split("-")[0] not in [g.split("-")[0] for g in good_ids],
          f"{path} must not list you. Your own student number is in it: remove that entry.", slot)
    roles_ok = all(str(i.get("role", "")).strip() == role for i in items if isinstance(i, dict))
    check(week, f"{path} gives everyone the role '{role}'", roles_ok,
          f"{path} must give everyone listed the role '{role}'. Found: a wrong or empty role.", slot)
    thin = [i for i in items if isinstance(i, dict) and len(str(i.get("what", "")).strip()) < 20]
    check(week, f"{path} says what each person did", not thin,
          f"{path} must say, for each person, what they did, in a real sentence. "
          f"Found: {pl(len(thin), 'entry', 'entries')} without one.", slot)


def week2() -> None:
    # In the lab: Part A of the proposal, two stakeholders, the first requirement list.
    check_proposal(2, range(1, 5), SESSION)
    check_contributors(2, "stakeholder", SESSION)

    raw = read("week02/requirements.json")
    ids: list[str] = []
    if raw is None:
        check(2, "week02/requirements.json is in the repository", False,
              "week02/requirements.json is missing. Run the checker online to fetch it, then fill it in.")
    else:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            check(2, "week02/requirements.json is valid JSON", False,
                  f"week02/requirements.json is not valid JSON ({exc}). Check the commas and the quotation marks.")
        else:
            items = data.get("requirements", data) if isinstance(data, dict) else data
            if not isinstance(items, list):
                items = []
            items = [i for i in items if isinstance(i, dict) and not i.get("dropped")]
            real = [i for i in items if str(i.get("description", "")).strip() not in ("", "…")]
            check(2, "week02/requirements.json has at least 8 filled-in requirements", len(real) >= 8,
                  f"week02/requirements.json needs at least 8 filled-in requirements. Found: {len(real)}.")
            ids = [str(i.get("id", "")).strip() for i in real]
            bad = [i for i in ids if not re.fullmatch(r"REQ-\d{3}", i)]
            dup = sorted({i for i in ids if ids.count(i) > 1})
            check(2, "every requirement id looks like REQ-001 and none is repeated", not bad and not dup and bool(ids),
                  "Every requirement id in week02/requirements.json must look like REQ-001, and none may be repeated. "
                  + ("Found: no requirements filled in yet." if not ids else f"Found: wrong ids {bad[:3]}, repeated ids {dup[:3]}."))
            f = sum(1 for i in real if i.get("functional") is True)
            nf = sum(1 for i in real if i.get("functional") is False)
            check(2, "week02/requirements.json has at least 5 functional and 3 non-functional requirements", f >= 5 and nf >= 3,
                  "week02/requirements.json needs at least 5 functional and 3 non-functional requirements. "
                  f"Found: {f} functional, {nf} non-functional.")
            phone = any(re.search(r"phone|mobile|390", str(i.get("description", "")), re.I)
                        for i in real if i.get("functional") is False)
            check(2, "the requirement about the phone screen is still there", phone,
                  "week02/requirements.json must keep a non-functional requirement about the phone screen. "
                  "Found: none that mentions it.")
            # By Saturday: every requirement prioritised and testable.
            prio = [str(i.get("priority", "")).strip().lower() for i in real]
            badp = [i.get("id") for i, pr in zip(real, prio) if pr not in ("must", "should", "could")]
            few = "Cannot pass yet: fewer than 8 requirements."
            check(2, "every requirement has a priority: must, should or could", len(real) >= 8 and not badp,
                  "Every requirement in week02/requirements.json must have a priority: must, should or could. "
                  + (few if len(real) < 8 else f"Found: missing or wrong in {badp[:4]}."), DEADLINE)
            check(2, "not every requirement is 'must'", len(real) >= 8 and any(pr in ("should", "could") for pr in prio),
                  "Not every requirement may be 'must': mark the ones that could be cut as should or could. "
                  + (few if len(real) < 8 else "Found: all of them are 'must'."), DEADLINE)
            thin = [i.get("id") for i in real if len(str(i.get("acceptance", "")).strip().strip("…")) < 25]
            check(2, "every requirement has an acceptance criterion", len(real) >= 8 and not thin,
                  "Every requirement must have an acceptance criterion, one sentence saying how to test it. "
                  + (few if len(real) < 8 else f"Found: missing or too short in {thin[:4]}."), DEADLINE)

    # By Saturday: the rest of Part A, the SRS, the log.
    check_proposal(2, range(5, 8), DEADLINE)
    secs = proposal_sections()
    s5 = secs.get(5, {})
    if s5:
        t = s5["text"].lower()
        check(2, "PROPOSAL.md §5 names mobile, web and server",
              all(k in t for k in ("mobile", "web", "server")),
              "PROPOSAL.md §5 must mention all three parts: mobile, web and server. Found: at least one is missing.", DEADLINE)
        check(2, "PROPOSAL.md §5 has its system context diagram", s5["mermaid"],
              "PROPOSAL.md §5 must contain the system context diagram, written as a ```mermaid block. Found: no such block.", DEADLINE)

    srs = read("week02/SRS.md") or ""
    prose = re.sub(r"<!--.*?-->", "", srs, flags=re.DOTALL)
    check(2, "week02/SRS.md is filled in", len(re.sub(r"```.*?```", "", prose, flags=re.DOTALL).strip()) > 600,
          "week02/SRS.md must be filled in. Found: the file is missing, or it is still the template.", DEADLINE)
    blocks = [b for b in re.findall(r"```mermaid\n(.*?)```", prose, re.DOTALL) if "%% EXAMPLE" not in b]
    usecases = sum(len(re.findall(r"\(\[", b)) for b in blocks)
    check(2, "SRS.md has a use case diagram with at least 3 use cases", usecases >= 3,
          f"SRS.md must have a use case diagram with at least 3 use cases. Found: {usecases}.", DEADLINE)
    in_srs = set(re.findall(r"REQ-\d{3}", prose))
    check(2, "SRS.md mentions every REQ id from requirements.json", bool(ids) and set(ids) <= in_srs,
          "SRS.md must mention every REQ id from week02/requirements.json. "
          + ("Found: no requirements filled in yet." if not ids else f"Found: missing {', '.join(sorted(set(ids) - in_srs)[:4])}."), DEADLINE)
    check_ai_log(2)


def week3() -> None:
    """Pitch and review in the lab; Part B of the proposal and the hostile-reviewer log
    by Saturday. The pitch is read as it was pushed by the end of the lecture (11:45)."""
    # --- the pitch: six slides, each with the student's own words -----------------
    pitch = read("week03/PITCH_03.md")
    if pitch is None:
        check(3, "week03/PITCH_03.md is in the repository", False,
              "week03/PITCH_03.md is missing. Run the checker online to fetch it, then write it.")
    else:
        body = re.sub(r"<!--.*?-->", "", pitch, flags=re.DOTALL)
        slides = [x.strip() for x in re.split(r"^---\s*$", body, flags=re.M) if x.strip()]
        slides = [x for x in slides if not re.match(r"^marp:", x)]  # the front matter
        check(3, "PITCH_03.md has 7 slides", len(slides) == 7,
              f"PITCH_03.md must have 7 slides: your six and the fixed reviewers' slide. Found: {len(slides)}. "
              "Slides are separated by a line that contains only ---.")
        holes = sum(len(re.findall(r"\[[^\]\n]{1,80}\]", re.sub(r"```.*?```", "", x, flags=re.DOTALL))) for x in slides[:6])  # not inside a drawing
        check(3, "PITCH_03.md has no [bracketed] text left", holes == 0,
              f"PITCH_03.md still has {pl(holes, 'piece')} of [bracketed] text. Replace each one with your own words and "
              "delete the square brackets too: text left inside [ ] still counts as not filled in.")
        def slide(n):  # 1-based, after the title slide
            return slides[n] if len(slides) > n else ""
        check(3, "slide 2 tells the last time it happened", len(re.sub(r"\*\*[^*]+\*\*", "", slide(1)).strip()) > 120 and "[" not in slide(1),
              "Slide 2 must tell the last time this problem happened to you or in front of you: when, where, "
              "what you did instead, what it cost. Found: too short, or [brackets] left.")
        people = len([r for r in re.findall(r"^\|\s*\d\s*\|([^|\n]{3,})\|([^|\n]{3,})\|", slide(2), re.M) if "[" not in r[0] + r[1]])
        check(3, "slide 3 names five testers in its table", people >= 5,
              f"Slide 3 must list five testers, one name per row of its table. Found: {pl(people, 'filled-in row')}.")
        # slide 4: three requirements, the same id AND description as requirements.json
        reqs = {}
        try:
            rj = json.loads((read("week02/requirements.json") or "[]").lstrip("\ufeff"))
            for it in (rj.get("requirements", rj) if isinstance(rj, dict) else rj):
                if isinstance(it, dict) and it.get("id"):
                    reqs[str(it["id"]).strip()] = " ".join(str(it.get("description", "")).split()).lower()
        except json.JSONDecodeError:
            pass
        cited = re.findall(r"^\s*\d\.\s*(REQ-\d{3})\s*[—–-]+\s*(.+)$", slide(3), re.M)
        same = [rid for rid, desc in cited if rid in reqs and reqs[rid] and (
            " ".join(desc.split()).lower().rstrip(".") == reqs[rid].rstrip(".") or reqs[rid].rstrip(".") in " ".join(desc.split()).lower())]
        check(3, "slide 4 lists three requirements copied from requirements.json", len(set(same)) >= 3,
              "Slide 4 must list three requirements copied word for word (id and description) from week02/requirements.json. "
              + (f"Found: {len(set(same))} of {len(cited)} listed match. Copy them, do not paraphrase."
                 if cited else "Found: none listed in the form: 1. REQ-001 — description."))
        dn = re.search(r"(does not|yapmaz)\s*:?\**\s*(.+)$", slide(3), re.I | re.M)
        check(3, "slide 4 says what the app does not do", bool(dn and len(dn.group(2).strip()) > 15 and "[" not in dn.group(2)),
              'Slide 4 must say what the app does NOT do, in one sentence that starts with "It does not:" '
              '(in Turkish: "Yapmaz:"), the sentence from §4 of your proposal. Found: none.')
        def local_image(md: str) -> bool:
            """An image in the repository, linked from the slide. The link may be relative to
            week03/ (where PITCH_03.md is, so the preview shows it) or to the root (fixed 6 Oct 2026:
            only 'week03/...' counted, which the preview cannot show)."""
            srcs = re.findall(r"!\[[^\]]*\]\(\s*<?([^)>\s]+)", md)
            srcs += re.findall(r"<img[^>]*\bsrc\s*=\s*[\"']([^\"']+)[\"']", md, re.I)
            for src in srcs:
                src = urllib.parse.unquote(src.split("#")[0].split("?")[0]).strip()
                if not src or re.match(r"^[a-z][a-z0-9+.-]*:", src, re.I):
                    continue  # a web address is not a drawing of yours
                for base in (ROOT / "week03", ROOT):
                    f = (base / src.lstrip("/")).resolve()
                    if f.is_file() and ROOT.resolve() in f.parents:
                        return True
            return False
        img_ok = local_image(slide(4))
        boxes = len(re.findall(r"^\s*\+[-+=]+\+\s*$", slide(4), re.M)) >= 2
        check(3, "slide 5 shows the main screen", img_ok or boxes,
              "Slide 5 must show the main screen: link an image from your repository, or draw it with text lines like +-----+. "
              "Found: neither. If you linked an image, check that the file is committed and the path is right.")
        check(3, "slide 6 states one honest doubt", len(slide(5).strip()) > 60 and "[" not in slide(5),
              "Slide 6 must state one honest doubt: the question, and two lines on why you are unsure. "
              "Found: too short, or [brackets] left.")
    # --- the review: three reviewers, quoted sentences, a decision each -----------
    items = contributors(3) or []
    if not items:
        check(3, "week03/contributors_03.json is valid JSON", False,
              "week03/contributors_03.json is missing, empty or not valid JSON. Run the checker online to fetch it, and check the commas and quotation marks.")
    else:
        ids = [str(i.get("student_id", "")).strip() for i in items if isinstance(i, dict)]
        good = [i for i in ids if re.fullmatch(r"\d{9}(-\d+)?", i)]
        check(3, "contributors_03.json names three reviewers", len(good) == 3 and len(set(good)) == 3,
              "week03/contributors_03.json must name three different reviewers, each with a valid 9-digit student number. "
              f"Found: {pl(len(good), 'valid number')}.")
        me = ""
        try:
            me = str(json.loads(read("student.json") or "{}").get("student_id", "")).strip()
        except json.JSONDecodeError:
            pass
        check(3, "contributors_03.json does not list you", me == "" or me.split("-")[0] not in [g.split("-")[0] for g in good],
              "week03/contributors_03.json must not list you. Your own student number is in it: remove that entry.")
        check(3, "contributors_03.json gives every reviewer the role 'reviewer'", all(str(i.get("role", "")).strip() == "reviewer" for i in items if isinstance(i, dict)),
              "week03/contributors_03.json must give every reviewer the role 'reviewer'. Found: a wrong or empty role.")
        thin = [i for i in items if isinstance(i, dict) and len(str(i.get("what", "")).strip()) < 25]
        check(3, "contributors_03.json quotes what each reviewer said", not thin,
              f"week03/contributors_03.json must quote, for each reviewer, a real sentence they said. Found: {pl(len(thin), 'entry', 'entries')} without one.")
        undecided = [i for i in items if isinstance(i, dict) and (i.get("accepted") not in (True, False) or len(str(i.get("why", "")).strip()) < 15)]
        check(3, "contributors_03.json gives a decision and a reason for each reviewer", not undecided,
              "week03/contributors_03.json must say, for each reviewer, whether you accepted the comment (accepted: true or false) and why. "
              f"Found: {pl(len(undecided), 'entry', 'entries')} without a decision and a reason.")
    # --- Part A revised: the change log has started --------------------------------
    text = read("PROPOSAL.md") or ""
    m = re.search(r"^## Change log.*?$", text, re.M)
    log = re.sub(r"<!--.*?-->", "", text[m.end():], flags=re.DOTALL) if m else ""
    dated = re.findall(r"20\d\d-\d\d-\d\d", log)
    check(3, "PROPOSAL.md change log has a dated line", len(dated) >= 1,
          'PROPOSAL.md change log must have a dated line added after the review, like "2026-10-07 — §N: what you changed". Found: none.')
    # --- the group: the same list in every member's repository (added 5 Oct 2026). Whether
    # the lists of the members agree can only be seen across repositories, so that part is
    # the instructor's (grade.py groups); here: a list that can be right, and reviewers in it.
    gdata = load_json("week03/group_03.json")
    glist = gdata.get("group") if isinstance(gdata, dict) else None
    if not isinstance(glist, list):
        check(3, "week03/group_03.json is valid JSON", False,
              "week03/group_03.json is missing or is not valid JSON. Run the checker online to fetch it.")
    else:
        nums = [str(x).strip().split("-")[0] for x in glist if str(x).strip()]
        valid = [n for n in nums if re.fullmatch(r"\d{9}", n)]
        me = my_number()
        check(3, "group_03.json lists your group: 4 or 5 different numbers, yours included",
              len(valid) == len(nums) and len(set(valid)) == len(valid) and len(valid) in (4, 5) and (me == "" or me in valid),
              "week03/group_03.json must list your group: 4 or 5 different 9-digit student numbers, yours included. "
              f"Found: {pl(len(valid), 'valid number')} of {len(nums)}" + (". Your own number is missing." if me not in valid else "."))
        reviewers = [str(i.get("student_id", "")).strip().split("-")[0] for i in (contributors(3) or []) if isinstance(i, dict)]
        reviewers = [r for r in reviewers if re.fullmatch(r"\d{9}", r)]  # empty entries are not reviewers (6 Oct 2026)
        outside = [r for r in reviewers if r not in valid]
        check(3, "your three reviewers are members of your group", bool(reviewers) and not outside,
              f"Your reviewers must be members of your group (week03/group_03.json). Found: not in group_03.json: {outside[:3]}."
              if outside else
              "Your three reviewers must be members of your group (week03/group_03.json). Found: no reviewers in contributors_03.json yet.")
    # --- the main flow: the screens the Week 4 prototype is built from (added 5 Oct 2026;
    # the project is fixed at this push, and a project that cannot name its screens is not)
    sc = read("week03/screens_03.md")
    if sc is None:
        check(3, "week03/screens_03.md is in the repository", False,
              "week03/screens_03.md is missing. Run the checker online to fetch it, then fill it in.")
    else:
        body = re.sub(r"<!--.*?-->", "", sc, flags=re.DOTALL)
        rows = re.findall(r"^\|\s*\d+\s*\|([^|\n]*)\|([^|\n]*)\|([^|\n]*)\|\s*$", body, re.M)
        filled = [r for r in rows if "[" not in "".join(r) and r[0].strip()
                  and len(r[1].strip()) >= 5 and re.search(r"REQ-\d{3}", r[2])]
        check(3, "screens_03.md lists at least five screens of the main flow", len(filled) >= 5,
              "week03/screens_03.md must list at least five screens of the main flow, each with a name, what the user does there, and REQ ids. "
              f"Found: {len(filled)}.")
        unknown = sorted({rid for r in filled for rid in re.findall(r"REQ-\d{3}", r[2])} - set(requirement_index()))
        check(3, "screens_03.md names only requirements that exist in requirements.json", bool(filled) and not unknown,
              "week03/screens_03.md may name only requirements that exist in week02/requirements.json. "
              + (f"Found: not in that file: {unknown[:4]}." if unknown else "Found: no filled-in screens yet."))
    # --- Saturday: Part B, the store, the log ---------------------------------------
    check_proposal(3, range(8, 13), DEADLINE)
    s12 = (proposal_sections().get(12) or {}).get("text", "").lower()
    check(3, "PROPOSAL.md §12 names the store", any(k in s12 for k in ("google play", "app store", "appgallery", "galaxy store", "testflight", "play store")),
          "PROPOSAL.md §12 must name the store (S0), its fee and how long its review takes. Found: no store named.", DEADLINE)
    log3 = read("week03/ai_log_03.md") or ""
    prose = re.sub(r"<!--.*?-->|```.*?```", "", log3, flags=re.DOTALL)
    objections = len([m for m in re.findall(r"^\s*[123]\.\s+(\S.{2,})$", prose, re.M) if not m.startswith("[")])
    check(3, "week03/ai_log_03.md lists three numbered objections", objections >= 3,
          f"week03/ai_log_03.md must list the three objections the assistant gave you, numbered 1. 2. 3. Found: {objections}.", DEADLINE)
    check_ai_log(3)


# ── Week 4: clickable prototype, test cases, walk-through ────────────

WEEK4_FROM = "2026-10-12"  # the Monday of Week 4: the walk-through's Change log lines are dated from here
RUN_WEEK = 0  # the last week this run checks; main() sets it
STORES = {  # the name in store.json -> words that name the same store in PROPOSAL.md §12
    "google play": ("google play", "play store"),
    "huawei appgallery": ("appgallery", "huawei"),
    "samsung galaxy store": ("galaxy store", "samsung"),
    "apple app store": ("app store", "apple", "testflight"),
}


def load_json(path: str):
    raw = read(path)
    if raw is None:
        return None
    try:
        return json.loads(raw.lstrip("﻿"))
    except json.JSONDecodeError:
        return None


def filled(value) -> str:
    """The text of a field, or "" if it is empty or still the scaffold's '…'."""
    text = str(value if value is not None else "").strip()
    return "" if text.strip(".…") == "" else text


def my_number() -> str:
    data = load_json("student.json")
    return str(data.get("student_id", "")).strip().split("-")[0] if isinstance(data, dict) else ""


def requirement_index() -> dict[str, dict]:
    """week02/requirements.json by id, dropped requirements included."""
    data = load_json("week02/requirements.json")
    items = data.get("requirements", data) if isinstance(data, dict) else data
    out: dict[str, dict] = {}
    for it in items if isinstance(items, list) else []:
        rid = str(it.get("id", "")).strip() if isinstance(it, dict) else ""
        if re.fullmatch(r"REQ-\d{3}", rid):
            out[rid] = it
    return out


def test_cases() -> list[dict] | None:
    data = load_json("week04/test_cases.json")
    items = data.get("test_cases", data) if isinstance(data, dict) else data
    if not isinstance(items, list):
        return None
    # an untouched scaffold entry (all '…') is the same as no entry
    return [t for t in items if isinstance(t, dict)
            and (filled(t.get("title")) or filled(t.get("expected")))]


def prototype_screens() -> dict[str, str]:
    """week04/prototype/*.html by file name."""
    folder = ROOT / "week04" / "prototype"
    if not folder.is_dir():
        return {}
    return {p.name: p.read_text(encoding="utf-8", errors="replace")
            for p in sorted(folder.glob("*.html")) if p.is_file()}


def screen_links(html: str) -> set[str]:
    """Every screen a page leads to: an href, a form action or a quoted name in a script."""
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.DOTALL)  # a commented-out link is not a link
    names = re.findall(r"""["']\s*(?:\./)?([\w.\-]+\.html)(?:[?#][^"']*)?\s*["']""", html)
    return {n for n in names if not n.lower().startswith(("http", "www"))}


def visible_text(html: str) -> str:
    html = re.sub(r"<!--.*?-->|<script.*?</script>|<style.*?</style>", " ", html, flags=re.DOTALL | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def serves(html: str) -> list[str]:
    m = re.search(r"<!--\s*serves:(.*?)-->", html, re.DOTALL | re.I)
    if not m or "[" in m.group(1):  # the starter's [placeholder] names nothing yet
        return []
    return re.findall(r"REQ-\d{3}", m.group(1))


def round_of(run: dict) -> int:
    """The walk-through round of a run: 1 unless it says 2 (as 2, "2", 2.0 or "round 2")."""
    m = re.search(r"\d+", str(run.get("round", "1")))
    return int(m.group()) if m else 1


def check_collaborator(week: int, role: str, slot: str = SESSION) -> list[str]:
    """Your collaborator in weekNN/group_NN.json: one classmate of your choice, from any group, who runs
    your test cases on your prototype (VC, 11 Oct 2026; before that the file held the other members of the
    group, 6 Oct). The file keeps its name and its "members" list, with exactly one entry; returns their number."""
    path = f"week{week:02d}/group_{week:02d}.json"
    items = contributors(week)
    if items is None:
        check(week, f"{path} is valid JSON", False,
              f"{path} is missing or is not valid JSON. Run the checker online to fetch it, and check the commas and quotation marks.", slot)
        return []
    items = [i for i in items if isinstance(i, dict)]
    ids = [str(i.get("student_id", "")).strip() for i in items]
    good = [i for i in ids if re.fullmatch(r"\d{9}(-\d+)?", i)]
    check(week, f"{path} names your collaborator", len(items) == 1 and len(good) == 1,
          f"{path} must name your collaborator: exactly one entry, with a valid 9-digit student number. "
          f"Found: {pl(len(items), 'entry', 'entries')}, {len(good)} with a valid number.", slot)
    me = my_number()
    check(week, f"{path} does not list you", me == "" or me not in [g.split("-")[0] for g in good],
          f"{path} must not list you. Your own student number is in it: remove that entry.", slot)
    check(week, f"{path} gives everyone the role '{role}'", bool(items) and all(str(i.get("role", "")).strip() == role for i in items),
          f"{path} must give everyone the role '{role}'. Found: a wrong or empty role.", slot)
    thin = [i for i in items if len(str(i.get("what", "")).strip()) < 25]
    check(week, f"{path} quotes what your collaborator found or said", bool(items) and not thin,
          f"{path} must quote a real sentence that your collaborator found or said. Found: {pl(len(thin), 'entry', 'entries')} without one.", slot)
    undecided = [i for i in items if i.get("accepted") not in (True, False) or len(str(i.get("why", "")).strip()) < 15]
    check(week, f"{path} gives a decision and a reason", bool(items) and not undecided,
          f"{path} must say whether you accepted what your collaborator found (accepted: true or false) and why. "
          f"Found: {pl(len(undecided), 'entry', 'entries')} without a decision and a reason.", DEADLINE)
    return [g.split("-")[0] for g in good]


def week4() -> None:
    """A clickable prototype and test cases in the lab, run on the prototype by the student's
    collaborator (one classmate of their choice, 11 Oct 2026; before that the group);
    by Saturday the fixes, a second round, the updated requirements, S1 and the log.

    The prototype comes before the design on purpose (decided 4 Oct 2026): nobody writes
    every requirement without seeing the product, and a missing screen costs minutes
    today against a server change and two clients in Week 8. The requirements and the
    test cases become the baseline at the end of Week 5.
    """
    reqs = requirement_index()
    live = {r: it for r, it in reqs.items() if not it.get("dropped")}
    musts = sorted(r for r, it in live.items()
                   if str(it.get("priority", "")).strip().lower() == "must" and filled(it.get("description")))

    # --- the prototype ---------------------------------------------------------------
    screens = prototype_screens()
    if not screens:
        check(4, "week04/prototype/ has screens", False,
              "week04/prototype/ has no .html files. Run the checker online to bring the starter screens.")
        check(4, "the prototype has at least 7 screens", False,
              "The prototype must have at least 7 screens by Saturday: the full flow. Found: none yet.", DEADLINE)
    else:
        check(4, "week04/prototype/index.html is there", "index.html" in screens,
              "The first screen must be week04/prototype/index.html. Found: no such file.")
        check(4, "the prototype has at least 5 screens", len(screens) >= 5,
              "The prototype must have at least 5 screens: the 3 starter screens and at least 2 of yours. "
              f"Found: {pl(len(screens), '.html file')} in week04/prototype/.")
        broken = sorted({f"{name} → {to}" for name, html in screens.items() for to in screen_links(html) if to not in screens})
        check(4, "every link in the prototype leads to a screen that exists", bool(screens) and not broken,
              f"Every link in the prototype must lead to a screen that exists. Found: broken links {broken[:3]}.")
        seen, todo = set(), ["index.html"] if "index.html" in screens else []
        while todo:
            name = todo.pop()
            if name in seen or name not in screens:
                continue
            seen.add(name)
            todo.extend(screen_links(screens[name]))
        unreachable = sorted(set(screens) - seen)
        check(4, "every screen can be reached from index.html", bool(screens) and not unreachable,
              f"Every screen must be reachable by links starting from index.html. Found: no link leads to {unreachable[:3]}.")
        holes = sorted(n for n, html in screens.items() if re.search(r"\[[^\]\n]{1,80}\]", visible_text(html)))
        check(4, "the prototype has no [bracketed] text left", bool(screens) and not holes,
              "The prototype screens still have [bracketed] text. Replace it with your own words and delete the square "
              f"brackets too. Found in: {holes[:3]}.")
        check(4, "the prototype has at least 7 screens", len(screens) >= 7,
              f"The prototype must have at least 7 screens by Saturday: the full flow. Found: {len(screens)}.", DEADLINE)
        unnamed = sorted(n for n, html in screens.items() if not serves(html) or any(r not in reqs for r in serves(html)))
        check(4, "every screen names the requirements it serves", bool(screens) and not unnamed,
              "Every screen must say which requirements it serves, in a line like <!-- serves: REQ-001, REQ-004 -->, "
              f"with ids that exist in requirements.json. Found: missing or wrong in {unnamed[:3]}.", DEADLINE)
        if RUN_WEEK <= 4:  # the prototype is not kept up to date once Week 5 starts
            shown = {r for html in screens.values() for r in serves(html)}
            missing = [r for r in musts if live[r].get("functional") is True and r not in shown]
            check(4, "every functional must requirement has a screen", bool(screens) and not missing,
                  "Every functional requirement marked 'must' needs a screen that serves it. "
                  f"Found: no screen serves {missing[:4]}.", DEADLINE)

    # --- the test cases --------------------------------------------------------------
    cases = test_cases()
    if cases is None:
        check(4, "week04/test_cases.json is valid JSON", False,
              "week04/test_cases.json is missing or is not valid JSON. Run the checker online to fetch it.")
        cases = []
    else:
        ids = [str(t.get("id", "")).strip() for t in cases]
        bad = [i for i in ids if not re.fullmatch(r"TC-\d{3}-\d{2}", i)]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        check(4, "test case ids look like TC-001-01 and none is repeated", bool(ids) and not bad and not dup,
              "Test case ids must look like TC-001-01 (the requirement number, then a counter), with no repeats. "
              + ("Found: no test cases yet." if not ids else f"Found: wrong ids {bad[:3]}, repeated ids {dup[:3]}."))
        wrong = [i for i, t in zip(ids, cases)
                 if str(t.get("req", "")).strip() not in reqs or i[3:6] != str(t.get("req", "")).strip()[4:]]
        check(4, "every test case tests a requirement that exists", bool(ids) and not wrong,
              "Every test case must name a requirement that exists in week02/requirements.json, and the number in its id must match it. "
              + ("Found: no test cases yet." if not ids else f"Found: wrong in {wrong[:3]}."))
        thin = [i for i, t in zip(ids, cases)
                if not (isinstance(t.get("steps"), list) and t["steps"] and all(filled(s) for s in t["steps"]))
                or len(filled(t.get("expected"))) < 15]
        check(4, "every test case has steps and an expected result", bool(ids) and not thin,
              "Every test case needs steps and an expected result of at least 15 characters. "
              + ("Found: no test cases yet." if not ids else f"Found: missing in {thin[:3]}."))
    active = [t for t in cases if not t.get("dropped")]
    covered = {str(t.get("req", "")).strip() for t in active}
    uncovered = [r for r in musts if r not in covered]
    check(4, "every must requirement has a test case", bool(musts) and not uncovered,
          "Every requirement marked 'must' needs at least one test case. "
          + ("Found: no 'must' requirements in requirements.json." if not musts else f"Found: none for {uncovered[:4]}."))
    per_req = {r: sum(1 for t in active if str(t.get("req", "")).strip() == r) for r in covered}
    check(4, "at least three requirements have a second test case", sum(1 for n in per_req.values() if n >= 2) >= 3,
          "At least three requirements need a second test case, for when something goes wrong. "
          f"Found: {sum(1 for n in per_req.values() if n >= 2)} with two or more.",
          DEADLINE)

    # --- the walk-through and the testers ----------------------------------------------
    testers = check_collaborator(4, "collaborator")
    data = load_json("week04/walkthrough_04.json")
    runs = data.get("runs", data) if isinstance(data, dict) else data
    if not isinstance(runs, list):
        check(4, "week04/walkthrough_04.json is valid JSON", False,
              "week04/walkthrough_04.json is missing or is not valid JSON. Run the checker online to fetch it.")
        runs = []
    runs = [r for r in runs if isinstance(r, dict) and (filled(r.get("tc")) or filled(r.get("tester")))]
    round1 = [r for r in runs if round_of(r) == 1]
    count: dict[str, int] = {}
    for r in round1:
        t = str(r.get("tester", "")).strip().split("-")[0]
        if re.fullmatch(r"\d{9}", t):
            count[t] = count.get(t, 0) + 1
    me = my_number()
    busiest = max((n for t, n in count.items() if t != me), default=0)
    check(4, "walk-through: your collaborator ran at least four test cases", busiest >= 4,
          "Your collaborator must run at least four of your test cases in round 1 of the walk-through, "
          f"each run recorded under their student number. Found: {pl(busiest, 'run')} by the tester with the most.")
    none = "Found: no runs recorded in week04/walkthrough_04.json yet."
    outside = sorted(set(count) - set(testers))
    check(4, "walk-through: every run is by your collaborator (group_04.json)",
          bool(count) and bool(testers) and not outside,
          "Every run in the walk-through must be by your collaborator, the student named in week04/group_04.json. "
          + (none if not runs else f"Found: not your collaborator: {outside[:3]}." if outside else "Found: no collaborator in group_04.json."))
    main_runs = [r for r in round1 if str(r.get("tc", "")).strip()[3:6] != "001"]
    check(4, "walk-through: round 1 has at least two runs outside the login",
          len(main_runs) >= 2,
          "Round 1 must have at least two runs of test cases outside the login (REQ-001): run test cases of your main flow. "
          + (none if not runs else f"Found: {len(main_runs)}."))
    known = {str(t.get("id", "")).strip() for t in cases}
    unknown = sorted({str(r.get("tc", "")).strip() for r in runs} - known)
    check(4, "walk-through: every run names a test case from test_cases.json", bool(runs) and not unknown,
          "Every run in the walk-through must name a test case that exists in week04/test_cases.json. "
          + (none if not runs else f"Found: not in test_cases.json: {unknown[:3]}."))
    odd = [r for r in runs if str(r.get("result", "")).strip().lower() not in ("pass", "fail", "blocked")
           or (str(r.get("result", "")).strip().lower() in ("fail", "blocked") and len(str(r.get("note", "")).strip()) < 15)]
    check(4, "walk-through: each result is pass, fail or blocked, with a note for fail and blocked",
          bool(runs) and not odd,
          "Every run must have a result (pass, fail or blocked), and a note of at least 15 characters for fail and blocked. "
          + (none if not runs else f"Found: {pl(len(odd), 'run')} without a valid result, or a fail or blocked without a note."))
    dropped = {str(t.get("id", "")).strip() for t in cases if t.get("dropped")}
    failed = {str(r.get("tc", "")).strip() for r in round1 if str(r.get("result", "")).strip().lower() == "fail"}
    rerun = {str(r.get("tc", "")).strip() for r in runs if round_of(r) == 2}
    open_fails = sorted(failed - rerun - dropped)
    check(4, "walk-through: every failed test case was run again in round 2", bool(runs) and not open_fails,
          "Every failed test case must be run again in round 2 after the fix, or dropped with a Change log line. "
          + (none if not runs else f"Found: no round 2 for {open_fails[:3]}."), DEADLINE)

    # --- what the walk-through changed: the Change log ---------------------------------
    text = read("PROPOSAL.md") or ""
    m = re.search(r"^## Change log.*?$", text, re.M)
    log = re.sub(r"<!--.*?-->", "", text[m.end():], flags=re.DOTALL) if m else ""
    lines = [ln for ln in log.splitlines()
             if any(d >= WEEK4_FROM for d in re.findall(r"20\d\d-\d\d-\d\d", ln))
             and re.search(r"REQ-\d{3}|TC-\d{3}-\d{2}", ln)]
    check(4, "PROPOSAL.md change log has a line from the walk-through that names the ids", bool(lines),
          f"PROPOSAL.md change log must have a line dated {WEEK4_FROM} or later that names a REQ or TC id. Found: none.", DEADLINE)

    # --- S1: the developer account -------------------------------------------------------
    st = load_json("week04/store.json")
    if not isinstance(st, dict):
        check(4, "week04/store.json is valid JSON", False,
              "week04/store.json is missing or is not valid JSON. Run the checker online to fetch it.", DEADLINE)
    else:
        name = " ".join(str(st.get("store", "")).lower().split())
        check(4, "store.json names the store", name in STORES,
              "week04/store.json must name the store: one of 'Google Play', 'Huawei AppGallery', 'Samsung Galaxy Store', "
              "'Apple App Store'. Found: something else, or empty.", DEADLINE)
        s1 = st.get("S1") if isinstance(st.get("S1"), dict) else {}
        ok = (re.fullmatch(r"20\d\d-\d\d-\d\d", str(s1.get("date", "")).strip()) and filled(s1.get("developer_name"))
              and str(s1.get("status", "")).strip().lower() in ("applied", "verified"))
        check(4, "store.json S1 is filled in", bool(ok),
              "week04/store.json S1 must have a date like 2026-10-13, your developer name, and a status of 'applied' or "
              "'verified'. Found: one of them missing or wrong.", DEADLINE)
        ev = str(s1.get("evidence", "")).strip()
        ev_ok = (bool(ev) and ".." not in ev and not Path(ev).is_absolute() and ":" not in ev
                 and ((ROOT / ev).is_file() or (ROOT / "week04" / ev).is_file()))
        check(4, "store.json S1 screenshot is saved", ev_ok,
              "The file named in 'evidence' in week04/store.json S1 must be saved in week04/. Found: no such file.", DEADLINE)
        s12 = (proposal_sections().get(12) or {}).get("text", "").lower()
        check(4, "store.json and PROPOSAL.md §12 name the same store",
              name in STORES and any(k in s12 for k in STORES[name]),
              "week04/store.json and PROPOSAL.md §12 must name the same store. Change one of them, and add a Change log line.", DEADLINE)

    # --- the log: acceptance criteria first ----------------------------------------------
    check(4, "week04/ai_log_04.md names the requirements it gave the assistant",
          bool(re.search(r"REQ-\d{3}", ai_log_section(4))),
          "week04/ai_log_04.md must name the REQ ids you gave the assistant, outside the comments and the evidence block. "
          "Found: no REQ id.", DEADLINE)
    check_ai_log(4)


CHECKS = {1: week1, 2: week2, 3: week3, 4: week4}


# ── secrets: this one runs for every week ────────────────────────────

SECRET_PATTERNS = [
    (r"sk-ant-[A-Za-z0-9\-_]{10,}", "Anthropic API key"),
    (r"AIza[0-9A-Za-z\-_]{30,}", "Google API key"),
    (r"sk-[A-Za-z0-9]{32,}", "OpenAI-style API key"),
    (r"ghp_[A-Za-z0-9]{20,}", "GitHub token"),
]


def check_secrets() -> bool:
    """Scan tracked text files for anything that looks like a live key."""
    clean = True
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "/.venv" in str(path):
            continue
        if path.suffix.lower() not in {
            ".py",
            ".md",
            ".txt",
            ".json",
            ".toml",
            ".yml",
            ".yaml",
            ".mmd",
            "",
        }:
            continue
        if path.name in {"check_deliverables.py", ".env.example"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for pattern, label in SECRET_PATTERNS:
            if re.search(pattern, text):
                rel = path.relative_to(ROOT)
                print("  " + say("SECRET  {rel} — looks like a {label}", rel=rel, label=label))
                clean = False
    return clean


# ── Türkçe: `python .github/check_deliverables.py tr` ─────────────────────────────────────
# The checker speaks English by default and for the instructor's capture (AIASD_SLOT set: always
# English). A student can ask for Turkish by adding `tr` (also `2 tr`, `tr 2`). The Turkish is
# NOT written beside each check: it is looked up here, by the English sentence the check
# printed, so the instructor's tools (grading/tr_checks.py → the Turkish block of an issue)
# read the very same table. One entry per sentence the checker can print — the PASS sentence and
# every FAIL sentence of a check:  (English template, Turkish template).
#   {name} stands for any text in the sentence and is available in the Turkish template under
#   the same name ({n} is a number); {{ and }} are literal braces. First match wins, so a
#   more specific sentence goes before a general one. A sentence without an entry is shown in
#   English and counted at the end of the run. When you change a sentence in a check above,
#   change its entry here; `claude-private/scripts/check_tr_coverage.py` lists the ones that
#   no longer match. Weeks in TR_WEEKS are fully covered; a later week is shown in English.

TR_WEEKS = frozenset({1, 2, 3, 4})

TR_RULES: list[tuple[str, str]] = [
    # --- every week: the AI log ---------------------------------------------------------------
    ("{p} must be filled in, in your own words. Found: the section is empty or untouched.",
     "{p} kendi sözlerinle doldurulmalı. Bulunan: bölüm boş ya da hiç dokunulmamış."),
    ("{p} must contain the real conversation, pasted inside the code block. Found: {n} {u} there.",
     "{p} içinde gerçek konuşma, kod bloğunun içine yapıştırılmış olarak bulunmalı. Bulunan: orada {n} karakter."),
    ("{p} holds the real conversation, pasted in the code block",
     "{p} içinde gerçek konuşma kod bloğuna yapıştırılmış"),
    ("{p} is filled in", "{p} dolu"),
    # --- Week 1: student.json ------------------------------------------------------------------
    ("student.json is missing from the repository root. Restore it: it holds your student number and section.",
     "student.json reponun kök klasöründe yok. Geri yükle: öğrenci numaranı ve şubeni içerir."),
    ("student.json is not valid JSON ({e}). Check the commas and the quotation marks.",
     "student.json geçerli bir JSON değil ({e}). Virgüllere ve tırnak işaretlerine bak."),
    ("student.json is not fully filled in. Empty fields: {f}. Fill in every field.",
     "student.json tam doldurulmamış. Boş alanlar: {f}. Her alanı doldur."),
    ("student.json is fully filled in", "student.json tam dolu"),
    ("student_id in student.json must be your student number, digits only. Found: {v}.",
     "student.json içindeki student_id öğrenci numaran olmalı, yalnızca rakamlardan oluşmalı. Bulunan: {v}."),
    ("student_id in student.json is a number", "student.json içindeki student_id bir sayı"),
    ("nickname in student.json must be 2-20 characters: letters, digits, - and _ only. Found: {v}.",
     "student.json içindeki nickname 2-20 karakter olmalı: yalnızca harf, rakam, - ve _ . Bulunan: {v}."),
    ("nickname in student.json can go on the class board",
     "student.json içindeki nickname sınıf panosuna konabilir"),
    ("section in student.json must be 'en' or 'tr'. Found: {v}. This is how your repository knows which week to check.",
     "student.json içindeki section 'en' ya da 'tr' olmalı. Bulunan: {v}. Reponun hangi haftayı kontrol edeceğini böyle bilir."),
    ("section in student.json is 'en' or 'tr'", "student.json içindeki section 'en' ya da 'tr'"),
    # --- Week 1: the files ---------------------------------------------------------------------
    ("week01/setup_proof.md is missing or too short. Create it and fill it in as the Week 1 assignment says.",
     "week01/setup_proof.md eksik ya da çok kısa. 1. hafta ödevinde yazdığı gibi oluştur ve doldur."),
    ("week01/setup_proof.md is there and long enough", "week01/setup_proof.md var ve yeterince uzun"),
    ("week01/hello.py is missing or has a syntax error. Create it, or run it to see the error.",
     "week01/hello.py eksik ya da sözdizimi hatası var. Oluştur ya da hatayı görmek için çalıştır."),
    ("week01/hello.py has no syntax error", "week01/hello.py içinde sözdizimi hatası yok"),
    ('week01/hello.py must contain an f-string, for example f"Hello {{name}}". Found: none.',
     'week01/hello.py içinde bir f-string olmalı, örneğin f"Hello {{name}}". Bulunan: yok.'),
    ("week01/hello.py contains an f-string", "week01/hello.py içinde f-string var"),
    ('week01/hello.py must contain a list, for example names = ["Ada", "Alan"]. Found: none.',
     'week01/hello.py içinde bir liste olmalı, örneğin names = ["Ada", "Alan"]. Bulunan: yok.'),
    ("week01/hello.py contains a list", "week01/hello.py içinde liste var"),
    ("week01/hello.py must contain a for-loop, for example: for name in names: ... Found: none.",
     "week01/hello.py içinde bir for döngüsü olmalı, örneğin: for name in names: ... Bulunan: yok."),
    ("week01/hello.py contains a for-loop", "week01/hello.py içinde for döngüsü var"),
    ("week01/hello.py must ask the user for input with input(). Found: input() is never called.",
     "week01/hello.py kullanıcıdan input() ile girdi istemeli. Bulunan: input() hiç çağrılmıyor."),
    ("week01/hello.py asks the user for input", "week01/hello.py kullanıcıdan girdi istiyor"),
    ("week01/llm_notes.md must have about 300 words written by you. Found: {n}. Headings, instructions and pasted blocks do not count.",
     "week01/llm_notes.md içinde senin yazdığın yaklaşık 300 kelime olmalı. Bulunan: {n}. Başlıklar, yönergeler ve yapıştırılmış bloklar sayılmaz."),
    ("week01/llm_notes.md has about 300 words of your own",
     "week01/llm_notes.md içinde kendi yazdığın yaklaşık 300 kelime var"),
    (".gitignore must contain .venv and .env, so they are never committed. Add both lines.",
     ".gitignore içinde .venv ve .env bulunmalı, böylece asla commit edilmezler. İki satırı da ekle."),
    (".gitignore covers .venv and .env", ".gitignore .venv ve .env'i kapsıyor"),
    (".env.example is missing. Create it with the NAMES of your settings only, never the secret values.",
     ".env.example eksik. Yalnızca ayarlarının ADLARIYLA oluştur, gizli değerleri asla yazma."),
    # --- the proposal (Weeks 2, 3) -------------------------------------------------------------
    ("PROPOSAL.md is missing, or its numbered headings were changed. Restore the headings from the template.",
     "PROPOSAL.md eksik ya da numaralı başlıkları değiştirilmiş. Başlıkları şablondan geri yükle."),
    ("PROPOSAL.md is in the repository root with its headings",
     "PROPOSAL.md reponun kök klasöründe ve başlıkları yerinde"),
    ("{l} has lost its heading, or the heading was changed. Restore the heading from the template.",
     "{l} başlığını kaybetmiş ya da başlık değiştirilmiş. Başlığı şablondan geri yükle."),
    ("{l} has its heading", "{l} başlığı yerinde"),
    ("{l} is not written yet. Found: {n} {u}. Write your own text under that heading.",
     "{l} henüz yazılmamış. Bulunan: {n} karakter. Bu başlığın altına kendi metnini yaz."),
    ("{l} is written", "{l} yazılmış"),
    # --- classmates and group files (Weeks 2, 3, 4) -------------------------------------------
    ("{p} is missing or is not valid JSON. Run the checker online to fetch it, and check the commas and quotation marks.",
     "{p} eksik ya da geçerli bir JSON değil. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır; virgüllere ve tırnak işaretlerine de bak."),
    ("{p} is missing, empty or not valid JSON. Run the checker online to fetch it, and check the commas and quotation marks.",
     "{p} eksik, boş ya da geçerli bir JSON değil. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır; virgüllere ve tırnak işaretlerine de bak."),
    ("{p} is missing or is not valid JSON. Run the checker online to fetch it.",
     "{p} eksik ya da geçerli bir JSON değil. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır."),
    ("{p} is valid JSON", "{p} geçerli bir JSON"),
    ("{p} may list at most two classmates, each with a valid 9-digit student number, all different. Found: {n} {u}, {m} with a valid number.",
     "{p} en fazla iki sınıf arkadaşı içerebilir; her birinin geçerli 9 haneli öğrenci numarası olmalı ve hepsi farklı olmalı. Bulunan: {n} giriş, {m} tanesinde geçerli numara var."),
    ("{p} lists 0-2 classmates with valid numbers", "{p} geçerli numaralı 0-2 sınıf arkadaşı içeriyor"),
    ("{p} must not list you. Your own student number is in it: remove that entry.",
     "{p} içinde sen yer almamalısın. Kendi öğrenci numaran listede: o girişi sil."),
    ("{p} does not list you", "{p} içinde sen yoksun"),
    ("{p} must give everyone listed the role '{r}'. Found: a wrong or empty role.",
     "{p} içinde listelenen herkesin rolü '{r}' olmalı. Bulunan: yanlış ya da boş bir rol."),
    ("{p} must give everyone the role '{r}'. Found: a wrong or empty role.",
     "{p} içinde herkesin rolü '{r}' olmalı. Bulunan: yanlış ya da boş bir rol."),
    ("{p} gives everyone the role '{r}'", "{p} içinde herkesin rolü '{r}'"),
    ("{p} must say, for each person, what they did, in a real sentence. Found: {n} {u} without one.",
     "{p} içinde her kişi için ne yaptığı gerçek bir cümleyle yazılmalı. Bulunan: {n} giriş bunu içermiyor."),
    ("{p} says what each person did", "{p} içinde her kişinin ne yaptığı yazılmış"),
    # --- Week 2: requirements, SRS ------------------------------------------------------------
    ("week02/requirements.json is missing. Run the checker online to fetch it, then fill it in.",
     "week02/requirements.json eksik. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır, sonra doldur."),
    ("{p} is in the repository", "{p} repoda"),
    ("week02/requirements.json is not valid JSON ({e}). Check the commas and the quotation marks.",
     "week02/requirements.json geçerli bir JSON değil ({e}). Virgüllere ve tırnak işaretlerine bak."),
    ("week02/requirements.json needs at least 8 filled-in requirements. Found: {n}.",
     "week02/requirements.json içinde en az 8 dolu gereksinim olmalı. Bulunan: {n}."),
    ("week02/requirements.json has at least 8 filled-in requirements",
     "week02/requirements.json içinde en az 8 dolu gereksinim var"),
    ("Every requirement id in week02/requirements.json must look like REQ-001, and none may be repeated. Found: no requirements filled in yet.",
     "week02/requirements.json içindeki her gereksinim id'si REQ-001 gibi görünmeli ve hiçbiri tekrarlanmamalı. Bulunan: henüz dolu gereksinim yok."),
    ("Every requirement id in week02/requirements.json must look like REQ-001, and none may be repeated. Found: wrong ids {a}, repeated ids {b}.",
     "week02/requirements.json içindeki her gereksinim id'si REQ-001 gibi görünmeli ve hiçbiri tekrarlanmamalı. Bulunan: yanlış id'ler {a}, tekrarlanan id'ler {b}."),
    ("every requirement id looks like REQ-001 and none is repeated",
     "her gereksinim id'si REQ-001 gibi ve hiçbiri tekrarlanmıyor"),
    ("week02/requirements.json needs at least 5 functional and 3 non-functional requirements. Found: {f} functional, {g} non-functional.",
     "week02/requirements.json içinde en az 5 işlevsel ve 3 işlevsel olmayan gereksinim olmalı. Bulunan: {f} işlevsel, {g} işlevsel olmayan."),
    ("week02/requirements.json has at least 5 functional and 3 non-functional requirements",
     "week02/requirements.json içinde en az 5 işlevsel ve 3 işlevsel olmayan gereksinim var"),
    ("week02/requirements.json must keep a non-functional requirement about the phone screen. Found: none that mentions it.",
     "week02/requirements.json içinde telefon ekranıyla ilgili işlevsel olmayan bir gereksinim kalmalı. Bulunan: bunu anan yok."),
    ("the requirement about the phone screen is still there", "telefon ekranıyla ilgili gereksinim hala yerinde"),
    ("Every requirement in week02/requirements.json must have a priority: must, should or could. Cannot pass yet: fewer than 8 requirements.",
     "week02/requirements.json içindeki her gereksinimin bir önceliği olmalı: must, should ya da could. Henüz geçemez: 8'den az gereksinim var."),
    ("Every requirement in week02/requirements.json must have a priority: must, should or could. Found: missing or wrong in {x}.",
     "week02/requirements.json içindeki her gereksinimin bir önceliği olmalı: must, should ya da could. Bulunan: eksik ya da yanlış olanlar {x}."),
    ("every requirement has a priority: must, should or could", "her gereksinimin önceliği var: must, should ya da could"),
    ("Not every requirement may be 'must': mark the ones that could be cut as should or could. Cannot pass yet: fewer than 8 requirements.",
     "Her gereksinim 'must' olamaz: çıkarılabilecek olanları should ya da could olarak işaretle. Henüz geçemez: 8'den az gereksinim var."),
    ("Not every requirement may be 'must': mark the ones that could be cut as should or could. Found: all of them are 'must'.",
     "Her gereksinim 'must' olamaz: çıkarılabilecek olanları should ya da could olarak işaretle. Bulunan: hepsi 'must'."),
    ("not every requirement is 'must'", "her gereksinim 'must' değil"),
    ("Every requirement must have an acceptance criterion, one sentence saying how to test it. Cannot pass yet: fewer than 8 requirements.",
     "Her gereksinimin bir kabul ölçütü olmalı: nasıl test edileceğini söyleyen tek cümle. Henüz geçemez: 8'den az gereksinim var."),
    ("Every requirement must have an acceptance criterion, one sentence saying how to test it. Found: missing or too short in {x}.",
     "Her gereksinimin bir kabul ölçütü olmalı: nasıl test edileceğini söyleyen tek cümle. Bulunan: eksik ya da çok kısa olanlar {x}."),
    ("every requirement has an acceptance criterion", "her gereksinimin kabul ölçütü var"),
    ("PROPOSAL.md §5 must mention all three parts: mobile, web and server. Found: at least one is missing.",
     "PROPOSAL.md §5 üç parçanın hepsini anmalı: mobile, web ve server. Bulunan: en az biri eksik."),
    ("PROPOSAL.md §5 names mobile, web and server", "PROPOSAL.md §5 mobile, web ve server'ı anıyor"),
    ("PROPOSAL.md §5 must contain the system context diagram, written as a ```mermaid block. Found: no such block.",
     "PROPOSAL.md §5 içinde ```mermaid bloğu olarak yazılmış sistem bağlam diyagramı bulunmalı. Bulunan: böyle bir blok yok."),
    ("PROPOSAL.md §5 has its system context diagram", "PROPOSAL.md §5 içinde sistem bağlam diyagramı var"),
    ("week02/SRS.md must be filled in. Found: the file is missing, or it is still the template.",
     "week02/SRS.md doldurulmalı. Bulunan: dosya eksik ya da hala şablon."),
    ("SRS.md must have a use case diagram with at least 3 use cases. Found: {n}.",
     "SRS.md içinde en az 3 use case içeren bir use case diyagramı olmalı. Bulunan: {n}."),
    ("SRS.md has a use case diagram with at least 3 use cases",
     "SRS.md içinde en az 3 use case'li bir use case diyagramı var"),
    ("SRS.md must mention every REQ id from week02/requirements.json. Found: no requirements filled in yet.",
     "SRS.md, week02/requirements.json içindeki her REQ id'sini anmalı. Bulunan: henüz dolu gereksinim yok."),
    ("SRS.md must mention every REQ id from week02/requirements.json. Found: missing {x}.",
     "SRS.md, week02/requirements.json içindeki her REQ id'sini anmalı. Bulunan: eksik olanlar {x}."),
    ("SRS.md mentions every REQ id from requirements.json",
     "SRS.md, requirements.json içindeki her REQ id'sini anıyor"),
    # --- student.json / .env.example in the repository root (Week 1 passes) ---------------------
    ("{p} is in the repository root", "{p} reponun kök klasöründe"),
    # --- Week 3: the pitch ----------------------------------------------------------------------
    ("week03/PITCH_03.md is missing. Run the checker online to fetch it, then write it.",
     "week03/PITCH_03.md eksik. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır, sonra yaz."),
    ("PITCH_03.md must have 7 slides: your six and the fixed reviewers' slide. Found: {n}. "
     "Slides are separated by a line that contains only ---.",
     "PITCH_03.md 7 slayttan oluşmalı: senin altı slaydın ve sabit reviewer slaydı. Bulunan: {n}. "
     "Slaytlar yalnızca --- yazan bir satırla ayrılır."),
    ("PITCH_03.md has 7 slides", "PITCH_03.md 7 slayttan oluşuyor"),
    ("PITCH_03.md still has {n} {u} of [bracketed] text. Replace each one with your own words and "
     "delete the square brackets too: text left inside [ ] still counts as not filled in.",
     "PITCH_03.md içinde hala [köşeli parantez] içinde {n} parça metin var. Her birini kendi sözlerinle değiştir "
     "ve köşeli parantezleri de sil: [ ] içinde kalan metin hala doldurulmamış sayılır."),
    ("PITCH_03.md has no [bracketed] text left", "PITCH_03.md içinde [köşeli parantezli] metin kalmamış"),
    ("Slide 2 must tell the last time this problem happened to you or in front of you: when, where, "
     "what you did instead, what it cost. Found: too short, or [brackets] left.",
     "Slayt 2'de bu sorunun en son sana ya da gözünün önünde ne zaman yaşandığı anlatılmalı: ne zaman, nerede, "
     "onun yerine ne yaptığın, bedeli ne oldu. Bulunan: çok kısa ya da [köşeli parantez] kalmış."),
    ("slide 2 tells the last time it happened", "slayt 2 sorunun en son ne zaman yaşandığını anlatıyor"),
    ("Slide 3 must list five testers, one name per row of its table. Found: {n} {u}.",
     "Slayt 3'te beş tester yazılmalı, tablonun her satırında bir isim. Bulunan: {n} dolu satır."),
    ("slide 3 names five testers in its table", "slayt 3 tablosunda beş tester'ın adı var"),
    ("Slide 4 must list three requirements copied word for word (id and description) from "
     "week02/requirements.json. Found: {x} of {y} listed match. Copy them, do not paraphrase.",
     "Slayt 4'te week02/requirements.json dosyasından kelimesi kelimesine kopyalanmış üç gereksinim (id ve açıklama) "
     "listelenmeli. Bulunan: listelenen {y} gereksinimden {x} tanesi eşleşiyor. Kopyala, kendi sözlerinle yazma."),
    ("Slide 4 must list three requirements copied word for word (id and description) from "
     "week02/requirements.json. Found: none listed in the form: 1. REQ-001 — description.",
     "Slayt 4'te week02/requirements.json dosyasından kelimesi kelimesine kopyalanmış üç gereksinim (id ve açıklama) "
     "listelenmeli. Bulunan: \"1. REQ-001 — açıklama\" biçiminde yazılmış hiçbiri yok."),
    ("slide 4 lists three requirements copied from requirements.json",
     "slayt 4 requirements.json dosyasından kopyalanmış üç gereksinimi listeliyor"),
    ('Slide 4 must say what the app does NOT do, in one sentence that starts with "It does not:" '
     '(in Turkish: "Yapmaz:"), the sentence from §4 of your proposal. Found: none.',
     'Slayt 4\'te uygulamanın NE YAPMADIĞI tek cümleyle yazılmalı; cümle "Yapmaz:" ile başlamalı '
     '(İngilizce yazarsan "It does not:"). Bu, önerinin 4. bölümündeki cümledir. Bulunan: yok.'),
    ("slide 4 says what the app does not do", "slayt 4 uygulamanın ne yapmadığını söylüyor"),
    ("Slide 5 must show the main screen: link an image from your repository, or draw it with text lines like "
     "+-----+. Found: neither. If you linked an image, check that the file is committed and the path is right.",
     "Slayt 5'te ana ekran gösterilmeli: reponda bulunan bir görseli bağla ya da +-----+ gibi metin çizgileriyle çiz. "
     "Bulunan: ikisi de yok. Görsel bağladıysan dosyanın commit edildiğini ve yolun doğru olduğunu kontrol et."),
    ("slide 5 shows the main screen", "slayt 5 ana ekranı gösteriyor"),
    ("Slide 6 must state one honest doubt: the question, and two lines on why you are unsure. "
     "Found: too short, or [brackets] left.",
     "Slayt 6'da dürüst bir kuşku yazılmalı: soru ve neden emin olmadığına dair iki satır. "
     "Bulunan: çok kısa ya da [köşeli parantez] kalmış."),
    ("slide 6 states one honest doubt", "slayt 6 dürüst bir kuşku belirtiyor"),
    # --- Week 3: the review ---------------------------------------------------------------------
    ("week03/contributors_03.json must name three different reviewers, each with a valid 9-digit student number. "
     "Found: {n} {u}.",
     "week03/contributors_03.json içinde üç farklı reviewer yazılmalı, her birinin geçerli 9 haneli öğrenci numarasıyla. "
     "Bulunan: {n} geçerli numara."),
    ("contributors_03.json names three reviewers", "contributors_03.json üç reviewer'ı adlandırıyor"),
    ("week03/contributors_03.json must give every reviewer the role 'reviewer'. Found: a wrong or empty role.",
     "week03/contributors_03.json içinde her reviewer'ın rolü 'reviewer' olmalı. Bulunan: yanlış ya da boş bir rol."),
    ("contributors_03.json gives every reviewer the role 'reviewer'",
     "contributors_03.json içinde her reviewer'ın rolü 'reviewer'"),
    ("week03/contributors_03.json must quote, for each reviewer, a real sentence they said. "
     "Found: {n} {u} without one.",
     "week03/contributors_03.json içinde her reviewer için söylediği gerçek bir cümle alıntılanmalı. "
     "Bulunan: {n} giriş bunu içermiyor."),
    ("contributors_03.json quotes what each reviewer said",
     "contributors_03.json her reviewer'ın söylediğini alıntılıyor"),
    ("week03/contributors_03.json must say, for each reviewer, whether you accepted the comment "
     "(accepted: true or false) and why. Found: {n} {u} without a decision and a reason.",
     "week03/contributors_03.json içinde her reviewer için yorumu kabul edip etmediğin (accepted: true ya da false) "
     "ve nedeni yazılmalı. Bulunan: {n} girişte karar ve neden yok."),
    ("contributors_03.json gives a decision and a reason for each reviewer",
     "contributors_03.json her reviewer için karar ve neden veriyor"),
    # --- Week 3: the change log, the group, the screens ------------------------------------------
    ('PROPOSAL.md change log must have a dated line added after the review, like '
     '"2026-10-07 — §N: what you changed". Found: none.',
     'PROPOSAL.md değişiklik günlüğüne, gözden geçirmeden sonra eklenmiş tarihli bir satır konmalı, örneğin '
     '"2026-10-07 — §N: neyi değiştirdin". Bulunan: yok.'),
    ("PROPOSAL.md change log has a dated line", "PROPOSAL.md değişiklik günlüğünde tarihli bir satır var"),
    ("week03/group_03.json must list your group: 4 or 5 different 9-digit student numbers, yours included. "
     "Found: {n} {u} of {m}. Your own number is missing.",
     "week03/group_03.json grubunu listelemeli: 4 ya da 5 farklı 9 haneli öğrenci numarası, seninki de dahil. "
     "Bulunan: {m} numaradan {n} tanesi geçerli. Kendi numaran eksik."),
    ("week03/group_03.json must list your group: 4 or 5 different 9-digit student numbers, yours included. "
     "Found: {n} {u} of {m}.",
     "week03/group_03.json grubunu listelemeli: 4 ya da 5 farklı 9 haneli öğrenci numarası, seninki de dahil. "
     "Bulunan: {m} numaradan {n} tanesi geçerli."),
    ("group_03.json lists your group: 4 or 5 different numbers, yours included",
     "group_03.json grubunu listeliyor: 4 ya da 5 farklı numara, seninki de dahil"),
    ("Your reviewers must be members of your group (week03/group_03.json). "
     "Found: not in group_03.json: {x}.",
     "Reviewer'ların grubunun üyesi olması gerekir (week03/group_03.json). "
     "Bulunan: group_03.json içinde olmayanlar: {x}."),
    ("Your three reviewers must be members of your group (week03/group_03.json). "
     "Found: no reviewers in contributors_03.json yet.",
     "Üç reviewer'ın da grubunun üyesi olması gerekir (week03/group_03.json). "
     "Bulunan: contributors_03.json içinde henüz reviewer yok."),
    ("your three reviewers are members of your group", "üç reviewer'ın da grubunun üyesi"),
    ("week03/screens_03.md is missing. Run the checker online to fetch it, then fill it in.",
     "week03/screens_03.md eksik. Dosyayı getirmek için checker'ı internete bağlıyken çalıştır, sonra doldur."),
    ("week03/screens_03.md must list at least five screens of the main flow, each with a name, "
     "what the user does there, and REQ ids. Found: {n}.",
     "week03/screens_03.md ana akışın en az beş ekranını listelemeli; her biri için ad, kullanıcının orada ne yaptığı "
     "ve REQ id'leri yazılmalı. Bulunan: {n}."),
    ("screens_03.md lists at least five screens of the main flow",
     "screens_03.md ana akışın en az beş ekranını listeliyor"),
    ("week03/screens_03.md may name only requirements that exist in week02/requirements.json. "
     "Found: not in that file: {x}.",
     "week03/screens_03.md yalnızca week02/requirements.json içinde bulunan gereksinimleri anabilir. "
     "Bulunan: o dosyada olmayanlar: {x}."),
    ("week03/screens_03.md may name only requirements that exist in week02/requirements.json. "
     "Found: no filled-in screens yet.",
     "week03/screens_03.md yalnızca week02/requirements.json içinde bulunan gereksinimleri anabilir. "
     "Bulunan: henüz dolu bir ekran yok."),
    ("screens_03.md names only requirements that exist in requirements.json",
     "screens_03.md yalnızca requirements.json içinde bulunan gereksinimleri anıyor"),
    # --- Week 3: Saturday ------------------------------------------------------------------------
    ("PROPOSAL.md §12 must name the store (S0), its fee and how long its review takes. "
     "Found: no store named.",
     "PROPOSAL.md §12'de mağaza (S0), ücreti ve incelemesinin ne kadar sürdüğü yazılmalı. "
     "Bulunan: adı geçen bir mağaza yok."),
    ("PROPOSAL.md §12 names the store", "PROPOSAL.md §12 mağazayı adlandırıyor"),
    ("week03/ai_log_03.md must list the three objections the assistant gave you, numbered 1. 2. 3. "
     "Found: {n}.",
     "week03/ai_log_03.md içinde asistanın sana verdiği üç itiraz 1. 2. 3. diye numaralanarak listelenmeli. "
     "Bulunan: {n}."),
    ("week03/ai_log_03.md lists three numbered objections", "week03/ai_log_03.md üç numaralı itirazı listeliyor"),
    # --- group file of Week 4: the collaborator ----------------------------------------------------
    ("{p} must name your collaborator: exactly one entry, with a valid 9-digit student number. Found: {n} {u}, {m} with a valid number.",
     "{p} içinde collaborator'ın yazılmalı: tam olarak tek bir giriş ve geçerli 9 haneli öğrenci numarası. "
     "Bulunan: {n} giriş, geçerli numarası olan {m}."),
    ("{p} names your collaborator", "{p} collaborator'ını adlandırıyor"),
    ("{p} must quote a real sentence that your collaborator found or said. Found: {n} {u} without one.",
     "{p} içinde collaborator'ının bulduğu ya da söylediği gerçek bir cümle alıntılanmalı. Bulunan: {n} giriş bunu içermiyor."),
    ("{p} quotes what your collaborator found or said", "{p} collaborator'ının bulduğunu ya da söylediğini alıntılıyor"),
    ("{p} must say whether you accepted what your collaborator found (accepted: true or false) and why. "
     "Found: {n} {u} without a decision and a reason.",
     "{p} içinde collaborator'ının bulduğunu kabul edip etmediğin (accepted: true ya da false) ve nedeni yazılmalı. "
     "Bulunan: {n} girişte karar ve neden yok."),
    ("{p} gives a decision and a reason", "{p} karar ve neden veriyor"),
    # --- Week 4: the prototype -------------------------------------------------------------------
    ("week04/prototype/ has no .html files. Run the checker online to bring the starter screens.",
     "week04/prototype/ içinde .html dosyası yok. Başlangıç ekranlarını getirmek için checker'ı internete bağlıyken çalıştır."),
    ("week04/prototype/ has screens", "week04/prototype/ içinde ekranlar var"),
    ("The prototype must have at least 7 screens by Saturday: the full flow. Found: none yet.",
     "Prototipte Cumartesi'ye kadar en az 7 ekran olmalı: akışın tamamı. Bulunan: henüz hiç yok."),
    ("The prototype must have at least 7 screens by Saturday: the full flow. Found: {n}.",
     "Prototipte Cumartesi'ye kadar en az 7 ekran olmalı: akışın tamamı. Bulunan: {n}."),
    ("the prototype has at least 7 screens", "prototipte en az 7 ekran var"),
    ("The first screen must be week04/prototype/index.html. Found: no such file.",
     "İlk ekran week04/prototype/index.html olmalı. Bulunan: böyle bir dosya yok."),
    ("week04/prototype/index.html is there", "week04/prototype/index.html var"),
    ("The prototype must have at least 5 screens: the 3 starter screens and at least 2 of yours. "
     "Found: {n} {u} in week04/prototype/.",
     "Prototipte en az 5 ekran olmalı: 3 başlangıç ekranı ve senin en az 2 ekranın. "
     "Bulunan: week04/prototype/ içinde {n} .html dosyası."),
    ("the prototype has at least 5 screens", "prototipte en az 5 ekran var"),
    ("Every link in the prototype must lead to a screen that exists. Found: broken links {x}.",
     "Prototipteki her bağlantı var olan bir ekrana gitmeli. Bulunan: kırık bağlantılar {x}."),
    ("every link in the prototype leads to a screen that exists",
     "prototipteki her bağlantı var olan bir ekrana gidiyor"),
    ("Every screen must be reachable by links starting from index.html. Found: no link leads to {x}.",
     "Her ekrana index.html'den başlayan bağlantılarla ulaşılabilmeli. Bulunan: şuna giden bağlantı yok: {x}."),
    ("every screen can be reached from index.html", "her ekrana index.html'den ulaşılabiliyor"),
    ("The prototype screens still have [bracketed] text. Replace it with your own words and delete the square "
     "brackets too. Found in: {x}.",
     "Prototip ekranlarında hala [köşeli parantezli] metin var. Kendi sözlerinle değiştir ve köşeli parantezleri de sil. "
     "Bulunduğu yer: {x}."),
    ("the prototype has no [bracketed] text left", "prototipte [köşeli parantezli] metin kalmamış"),
    ("Every screen must say which requirements it serves, in a line like <!-- serves: REQ-001, REQ-004 -->, "
     "with ids that exist in requirements.json. Found: missing or wrong in {x}.",
     "Her ekran hangi gereksinimlere hizmet ettiğini <!-- serves: REQ-001, REQ-004 --> gibi bir satırla söylemeli; "
     "id'ler requirements.json içinde bulunmalı. Bulunan: eksik ya da yanlış olanlar {x}."),
    ("every screen names the requirements it serves", "her ekran hizmet ettiği gereksinimleri belirtiyor"),
    ("Every functional requirement marked 'must' needs a screen that serves it. Found: no screen serves {x}.",
     "'must' işaretli her işlevsel gereksinimin ona hizmet eden bir ekranı olmalı. Bulunan: şuna hizmet eden ekran yok: {x}."),
    ("every functional must requirement has a screen", "'must' işaretli her işlevsel gereksinimin bir ekranı var"),
    # --- Week 4: the test cases -----------------------------------------------------------------
    ("Test case ids must look like TC-001-01 (the requirement number, then a counter), with no repeats. "
     "Found: no test cases yet.",
     "Test senaryosu id'leri TC-001-01 gibi görünmeli (gereksinim numarası, sonra bir sayaç), tekrar olmamalı. "
     "Bulunan: henüz test senaryosu yok."),
    ("Test case ids must look like TC-001-01 (the requirement number, then a counter), with no repeats. "
     "Found: wrong ids {a}, repeated ids {b}.",
     "Test senaryosu id'leri TC-001-01 gibi görünmeli (gereksinim numarası, sonra bir sayaç), tekrar olmamalı. "
     "Bulunan: yanlış id'ler {a}, tekrarlanan id'ler {b}."),
    ("test case ids look like TC-001-01 and none is repeated",
     "test senaryosu id'leri TC-001-01 gibi ve hiçbiri tekrarlanmıyor"),
    ("Every test case must name a requirement that exists in week02/requirements.json, and the number in its id "
     "must match it. Found: no test cases yet.",
     "Her test senaryosu week02/requirements.json içinde var olan bir gereksinimi anmalı ve id'sindeki numara "
     "onunla eşleşmeli. Bulunan: henüz test senaryosu yok."),
    ("Every test case must name a requirement that exists in week02/requirements.json, and the number in its id "
     "must match it. Found: wrong in {x}.",
     "Her test senaryosu week02/requirements.json içinde var olan bir gereksinimi anmalı ve id'sindeki numara "
     "onunla eşleşmeli. Bulunan: yanlış olanlar {x}."),
    ("every test case tests a requirement that exists", "her test senaryosu var olan bir gereksinimi test ediyor"),
    ("Every test case needs steps and an expected result of at least 15 characters. Found: missing in {x}.",
     "Her test senaryosunun adımları ve en az 15 karakterlik beklenen bir sonucu olmalı. Bulunan: eksik olanlar {x}."),
    ("Every test case needs steps and an expected result of at least 15 characters. Found: no test cases yet.",
     "Her test senaryosunun adımları ve en az 15 karakterlik beklenen bir sonucu olmalı. Bulunan: henüz test senaryosu yok."),
    ("every test case has steps and an expected result", "her test senaryosunun adımları ve beklenen sonucu var"),
    ("Every requirement marked 'must' needs at least one test case. Found: no 'must' requirements in requirements.json.",
     "'must' işaretli her gereksinimin en az bir test senaryosu olmalı. Bulunan: requirements.json içinde 'must' gereksinim yok."),
    ("Every requirement marked 'must' needs at least one test case. Found: none for {x}.",
     "'must' işaretli her gereksinimin en az bir test senaryosu olmalı. Bulunan: şunlar için hiç yok: {x}."),
    ("every must requirement has a test case", "her must gereksinimin bir test senaryosu var"),
    ("At least three requirements need a second test case, for when something goes wrong. "
     "Found: {n} with two or more.",
     "En az üç gereksinimin, bir şeyin ters gittiği durum için ikinci bir test senaryosu olmalı. "
     "Bulunan: iki ya da daha fazla senaryosu olan {n} gereksinim."),
    ("at least three requirements have a second test case", "en az üç gereksinimin ikinci bir test senaryosu var"),
    # --- Week 4: the walk-through ------------------------------------------------------------------
    ("Your collaborator must run at least four of your test cases in round 1 of the walk-through, "
     "each run recorded under their student number. Found: {n} {u} by the tester with the most.",
     "Collaborator'ın 1. turda test senaryolarından en az dördünü çalıştırmalı ve her çalıştırma onun öğrenci numarasıyla "
     "kaydedilmeli. Bulunan: en çok çalıştıran tester {n} çalıştırma yapmış."),
    ("walk-through: your collaborator ran at least four test cases",
     "walk-through: collaborator'ın en az dört test senaryosu çalıştırmış"),
    ("Every run in the walk-through must be by your collaborator, the student named in week04/group_04.json. "
     "Found: no collaborator in group_04.json.",
     "Walk-through'daki her çalıştırma collaborator'ına ait olmalı, yani week04/group_04.json içinde adı geçen öğrenciye. "
     "Bulunan: group_04.json içinde collaborator yok."),
    ("Every run in the walk-through must be by your collaborator, the student named in week04/group_04.json. "
     "Found: no runs recorded in week04/walkthrough_04.json yet.",
     "Walk-through'daki her çalıştırma collaborator'ına ait olmalı, yani week04/group_04.json içinde adı geçen öğrenciye. "
     "Bulunan: week04/walkthrough_04.json içinde henüz kayıtlı çalıştırma yok."),
    ("Every run in the walk-through must be by your collaborator, the student named in week04/group_04.json. "
     "Found: not your collaborator: {x}.",
     "Walk-through'daki her çalıştırma collaborator'ına ait olmalı, yani week04/group_04.json içinde adı geçen öğrenciye. "
     "Bulunan: collaborator'ın olmayanlar: {x}."),
    ("walk-through: every run is by your collaborator (group_04.json)",
     "walk-through: her çalıştırma collaborator'ına ait (group_04.json)"),
    ("Round 1 must have at least two runs of test cases outside the login (REQ-001): run test cases of your main flow. "
     "Found: no runs recorded in week04/walkthrough_04.json yet.",
     "1. turda giriş (REQ-001) dışındaki test senaryolarından en az iki çalıştırma olmalı: ana akışının test senaryolarını çalıştır. "
     "Bulunan: week04/walkthrough_04.json içinde henüz kayıtlı çalıştırma yok."),
    ("Round 1 must have at least two runs of test cases outside the login (REQ-001): run test cases of your main flow. "
     "Found: {n}.",
     "1. turda giriş (REQ-001) dışındaki test senaryolarından en az iki çalıştırma olmalı: ana akışının test senaryolarını çalıştır. "
     "Bulunan: {n}."),
    ("walk-through: round 1 has at least two runs outside the login",
     "walk-through: 1. turda giriş dışında en az iki çalıştırma var"),
    ("Every run in the walk-through must name a test case that exists in week04/test_cases.json. "
     "Found: no runs recorded in week04/walkthrough_04.json yet.",
     "Walk-through'daki her çalıştırma week04/test_cases.json içinde var olan bir test senaryosunu anmalı. "
     "Bulunan: week04/walkthrough_04.json içinde henüz kayıtlı çalıştırma yok."),
    ("Every run in the walk-through must name a test case that exists in week04/test_cases.json. "
     "Found: not in test_cases.json: {x}.",
     "Walk-through'daki her çalıştırma week04/test_cases.json içinde var olan bir test senaryosunu anmalı. "
     "Bulunan: test_cases.json içinde olmayanlar: {x}."),
    ("walk-through: every run names a test case from test_cases.json",
     "walk-through: her çalıştırma test_cases.json içinden bir test senaryosunu anıyor"),
    ("Every run must have a result (pass, fail or blocked), and a note of at least 15 characters for fail and "
     "blocked. Found: no runs recorded in week04/walkthrough_04.json yet.",
     "Her çalıştırmanın bir sonucu (pass, fail ya da blocked) olmalı; fail ve blocked için en az 15 karakterlik bir not "
     "da olmalı. Bulunan: week04/walkthrough_04.json içinde henüz kayıtlı çalıştırma yok."),
    ("Every run must have a result (pass, fail or blocked), and a note of at least 15 characters for fail and "
     "blocked. Found: {n} {u} without a valid result, or a fail or blocked without a note.",
     "Her çalıştırmanın bir sonucu (pass, fail ya da blocked) olmalı; fail ve blocked için en az 15 karakterlik bir not "
     "da olmalı. Bulunan: geçerli sonucu olmayan ya da notsuz fail/blocked olan {n} çalıştırma."),
    ("walk-through: each result is pass, fail or blocked, with a note for fail and blocked",
     "walk-through: her sonuç pass, fail ya da blocked ve fail/blocked için not var"),
    ("Every failed test case must be run again in round 2 after the fix, or dropped with a Change log line. "
     "Found: no round 2 for {x}.",
     "Kalan her test senaryosu düzeltmeden sonra 2. turda yeniden çalıştırılmalı ya da bir değişiklik günlüğü satırıyla "
     "çıkarılmalı. Bulunan: şunlar için 2. tur yok: {x}."),
    ("Every failed test case must be run again in round 2 after the fix, or dropped with a Change log line. "
     "Found: no runs recorded in week04/walkthrough_04.json yet.",
     "Kalan her test senaryosu düzeltmeden sonra 2. turda yeniden çalıştırılmalı ya da bir değişiklik günlüğü satırıyla "
     "çıkarılmalı. Bulunan: week04/walkthrough_04.json içinde henüz kayıtlı çalıştırma yok."),
    ("walk-through: every failed test case was run again in round 2",
     "walk-through: kalan her test senaryosu 2. turda yeniden çalıştırılmış"),
    ("PROPOSAL.md change log must have a line dated {d} or later that names a REQ or TC id. Found: none.",
     "PROPOSAL.md değişiklik günlüğünde {d} ya da sonrası tarihli, bir REQ ya da TC id'si anan bir satır olmalı. "
     "Bulunan: yok."),
    ("PROPOSAL.md change log has a line from the walk-through that names the ids",
     "PROPOSAL.md değişiklik günlüğünde walk-through'dan gelen, id'leri anan bir satır var"),
    # --- Week 4: S1 and the log ----------------------------------------------------------------------
    ("week04/store.json must name the store: one of 'Google Play', 'Huawei AppGallery', 'Samsung Galaxy Store', "
     "'Apple App Store'. Found: something else, or empty.",
     "week04/store.json içinde mağaza yazılmalı: 'Google Play', 'Huawei AppGallery', 'Samsung Galaxy Store' ya da "
     "'Apple App Store'. Bulunan: başka bir şey ya da boş."),
    ("store.json names the store", "store.json mağazayı adlandırıyor"),
    ("week04/store.json S1 must have a date like 2026-10-13, your developer name, and a status of 'applied' or "
     "'verified'. Found: one of them missing or wrong.",
     "week04/store.json içindeki S1'de 2026-10-13 gibi bir tarih, geliştirici adın ve 'applied' ya da 'verified' "
     "durumu olmalı. Bulunan: biri eksik ya da yanlış."),
    ("The file named in 'evidence' in week04/store.json S1 must be saved in week04/. Found: no such file.",
     "week04/store.json S1 içindeki 'evidence' alanında adı geçen dosya week04/ içine kaydedilmeli. "
     "Bulunan: böyle bir dosya yok."),
    ("store.json S1 screenshot is saved", "store.json S1 ekran görüntüsü kaydedilmiş"),
    ("week04/store.json and PROPOSAL.md §12 must name the same store. Change one of them, and add a Change log line.",
     "week04/store.json ile PROPOSAL.md §12 aynı mağazayı yazmalı. Birini değiştir ve bir değişiklik günlüğü satırı ekle."),
    ("store.json and PROPOSAL.md §12 name the same store", "store.json ile PROPOSAL.md §12 aynı mağazayı yazıyor"),
    ("week04/ai_log_04.md must name the REQ ids you gave the assistant, outside the comments and the evidence block. "
     "Found: no REQ id.",
     "week04/ai_log_04.md içinde asistana verdiğin REQ id'leri yorumların ve kanıt bloğunun dışında yazılmalı. "
     "Bulunan: hiç REQ id'si yok."),
    ("week04/ai_log_04.md names the requirements it gave the assistant",
     "week04/ai_log_04.md asistana verilen gereksinimleri anıyor"),
]

# Messages of the run itself (not of a check), same {name} fields; Turkish only when `tr` was asked for.
TR_UI = {
    "Secret scan": "Gizli anahtar taraması",
    "no API keys found": "API anahtarı bulunamadı",
    "KEYS FOUND — remove them and rotate them NOW": "ANAHTAR BULUNDU — hemen sil ve yenile",
    "This is an automatic 10-point deduction. Remove the key, rotate it": "Bu otomatik 10 puan kesintisidir. Anahtarı sil, sağlayıcıda yenile",
    "at the provider, and never commit one again.": "ve bir daha asla anahtar commit etme.",
    "SECRET  {rel} — looks like a {label}": "GİZLİ  {rel} — şuna benziyor: {label}",
    "WARNING: could not reach the course on GitHub, so this run uses the": "UYARI: GitHub'daki derse ulaşılamadı, bu yüzden bu çalıştırma",
    "checker copy stored in your repository, which may be out of date.": "reponda duran checker kopyasını kullanıyor; güncel olmayabilir.",
    "Connect to the network and run it again before trusting the list.": "Listeye güvenmeden önce internete bağlan ve yeniden çalıştır.",
    "(using the current checker published by the course)": "(dersin yayımladığı güncel checker kullanılıyor)",
    "Course files brought into this repository (add them with `git add .`):": "Dersin dosyaları bu repoya getirildi (`git add .` ile ekle):",
    "Cannot tell which week it is.": "Hangi haftada olduğumuz anlaşılamıyor.",
    "The course could not be reached and there is no cached week number\nyet — this is the first run on this machine, offline. Connect once\nand run it again; after that it works without a network.":
        "Derse ulaşılamadı ve henüz önbellekte bir hafta numarası yok —\nbu makinedeki ilk çalıştırma ve internet yok. Bir kez bağlan ve\nyeniden çalıştır; sonrasında internetsiz de çalışır.",
    "Week 0 ({source}) — nothing to check yet.": "Hafta 0 ({source}) — henüz kontrol edilecek bir şey yok.",
    "The course has not started checking deliverables. Nothing for you to do.": "Ders henüz teslimleri kontrol etmeye başlamadı. Yapman gereken bir şey yok.",
    "Give one week number, for example: python .github/check_deliverables.py 2": "Tek bir hafta numarası ver, örneğin: python .github/check_deliverables.py 2 tr",
    "Weeks start at 1.": "Haftalar 1'den başlar.",
    "Week {n} has not started yet. The course is at week {current}.": "{n}. hafta henüz başlamadı. Ders {current}. haftada.",
    "Checking week {shown}  ({source})": "{shown}. hafta kontrol ediliyor  ({source})",
    "To check another week, add its number: python .github/check_deliverables.py {other}": "Başka bir haftayı kontrol etmek için numarasını ekle: python .github/check_deliverables.py {other} tr",
    "published by the course": "dersin yayımladığı",
    "cached — the course could not be reached": "önbellekten — derse ulaşılamadı",
    "There are no checks for week {shown} yet.": "{shown}. hafta için henüz kontrol yok.",
    "Was due at the end of the session": "Oturum sonunda teslim edilmesi gerekiyordu",
    "Due at the end of the session": "Oturum sonunda teslim",
    "Was due Saturday 23:59": "Cumartesi 23:59'a kadar teslim edilmesi gerekiyordu",
    "Due by Saturday 23:59": "Cumartesi 23:59'a kadar teslim",
    "In the lab:     {a} of {b} done": "Derste:           {a} / {b} tamam",
    "By Saturday:    {a} of {b} done": "Cumartesiye dek:  {a} / {b} tamam",
    "Earlier weeks, checks still failing: {listing} — see one with: python .github/check_deliverables.py {n}":
        "Önceki haftalarda hala eksik olan kontroller: {listing} — birine bakmak için: python .github/check_deliverables.py {n} tr",
    "\n  {n} still to do before Saturday 23:59. Those do not fail this run —\n  they are not due yet. The lab items are what the end-of-session mark reads.":
        "\n  Cumartesi 23:59'a kadar yapılacak {n} madde var. Bunlar bu çalıştırmada kalmış sayılmaz —\n  henüz süreleri gelmedi. Oturum sonu notu yalnızca ders içi maddeleri okur.",
    "PASS": "TAMAM",
    "FAIL": "EKSİK",
    "{n} line(s) above have no Turkish yet and are shown in English.": "Yukarıdaki {n} satırın henüz Türkçesi yok, İngilizce gösterildi.",
}

LANG = "en"  # "tr" only in a student's own run that asked for it (see wanted_lang)
_UNTRANSLATED: set[str] = set()


def wanted_lang(argv: list[str] | None = None) -> str:
    """Turkish if the student added `tr` to the command line. The instructor's capture
    (AIASD_SLOT set) is always English: the grading reads the English sentences."""
    if os.environ.get("AIASD_SLOT", "").strip().lower() in (SESSION, DEADLINE):
        return "en"
    args = [a.strip().lower() for a in (sys.argv[1:] if argv is None else argv)]
    return "tr" if "tr" in args else "en"


def say(text: str, **kw) -> str:
    """A message of the run in the language asked for; English when there is no Turkish for it."""
    out = TR_UI.get(text) if LANG == "tr" else None
    out = out or text
    return out.format(**kw) if kw else out


_TR_COMPILED: list | None = None


def _compile_tr() -> list:
    global _TR_COMPILED
    if _TR_COMPILED is None:
        compiled = []
        for en, tr in TR_RULES:
            parts = []
            for tok in re.split(r"(\{\{|\}\}|\{\w+\})", " ".join(en.split())):
                if tok == "{{":
                    parts.append(re.escape("{"))
                elif tok == "}}":
                    parts.append(re.escape("}"))
                elif len(tok) > 2 and tok[0] == "{" and tok[-1] == "}":
                    pat = r"\d+" if tok == "{n}" else ".+?"
                    parts.append("(?P<%s>%s)" % (tok[1:-1], pat))
                else:
                    parts.append(re.escape(tok))
            compiled.append((re.compile("".join(parts)), tr))
        _TR_COMPILED = compiled
    return _TR_COMPILED


def translate_sentence(sentence: str) -> str | None:
    """The Turkish text for one sentence the checker printed (PASS or FAIL), or None if the
    table has no entry for it."""
    s = " ".join((sentence or "").split())
    for rx, tr in _compile_tr():
        m = rx.fullmatch(s)
        if m:
            fields = m.groupdict()
            return re.sub(r"\{\{|\}\}|\{(\w+)\}",
                          lambda t: "{" if t.group(0) == "{{" else "}" if t.group(0) == "}}" else fields.get(t.group(1), t.group(0)), tr)
    return None


def shown_sentence(text: str) -> str:
    """What a check line prints: the Turkish when asked for, the English sentence otherwise."""
    if LANG != "tr":
        return text
    out = translate_sentence(text)
    if out is None:
        _UNTRANSLATED.add(text)
        return text
    return out



# ── main ─────────────────────────────────────────────────────────────


CHECKER_URL = (
    "https://raw.githubusercontent.com/vedatcoskun-course/aiasd-template"
    "/main/.github/check_deliverables.py"
)


def maybe_update() -> None:
    """Run the current published checker instead of this frozen copy.

    A student repository is created from the template once and never updated
    again, so the copy sitting in it is the one from the week they started. By
    Week 8 it would be checking Week 1 and showing a green tick for work it does
    not know how to look at. The grade would still be right — that is computed
    with the instructor's own copy — but the feedback would be silently empty,
    which is worse than no feedback.

    So: fetch the published checker, and if it differs from this one, hand over
    to it. Anything that goes wrong — no network, a captive portal, a truncated
    file, a syntax error — means carrying on with the local copy.
    """
    if os.environ.get("AIASD_NO_SELFUPDATE"):
        return  # we are already the downloaded copy
    if os.environ.get("AIASD_WEEK") or os.environ.get("AIASD_SLOT"):
        return  # the instructor is grading, and grading runs its own copy

    try:
        with urllib.request.urlopen(CHECKER_URL, timeout=6) as response:
            published = response.read().decode("utf-8")
    except (urllib.error.URLError, OSError, TimeoutError, UnicodeDecodeError):
        # Offline, or GitHub unreachable from this network. The copy in the
        # repository may be weeks old and look for files the course no longer
        # asks for - say so loudly rather than let a stale list pass for the truth.
        print("  " + say("WARNING: could not reach the course on GitHub, so this run uses the"))
        print("  " + say("checker copy stored in your repository, which may be out of date."))
        print("  " + say("Connect to the network and run it again before trusting the list.") + "\n")
        return

    mine = Path(__file__).read_text(encoding="utf-8", errors="replace")
    if published == mine:
        return
    if MARKER not in published or len(published) < 4000:
        return
    try:
        compile(published, "check_deliverables.py", "exec")
    except SyntaxError:
        return

    # Keep the repository's own copy current too, so that an offline run later
    # falls back to a recent checker instead of the one from the week the
    # repository was created. Best effort: a read-only file is not an error.
    try:
        Path(__file__).write_text(published, encoding="utf-8")
    except OSError:
        pass

    tmp = Path(tempfile.gettempdir()) / "aiasd_check_deliverables.py"
    try:
        tmp.write_text(published, encoding="utf-8")
    except OSError:
        return

    print("  " + say("(using the current checker published by the course)") + "\n")
    env = {
        **os.environ,
        "AIASD_NO_SELFUPDATE": "1",
        "AIASD_ROOT": str(ROOT),
    }
    raise SystemExit(
        subprocess.run([sys.executable, str(tmp), *sys.argv[1:]], env=env, check=False).returncode
    )


COURSE_WEEK_URL = (
    "https://raw.githubusercontent.com/vedatcoskun-course/aiasd-template/main/CURRENT_WEEK.txt"
)


def cached_week() -> int:
    raw = (read("CURRENT_WEEK_CACHE.txt") or "0").strip().splitlines()
    try:
        return int(raw[0]) if raw and raw[0].strip() else 0
    except ValueError:
        return 0


def prose_words(md: str) -> int:
    """Count only what the student wrote themselves.

    A scaffold with headings, instructions and HTML comments can be hundreds of
    words before anyone has typed anything, and pasted model output is evidence,
    not prose. Counting the raw file would let a word-count check pass on an
    untouched template — so headings, quoted instructions, comments and fenced
    blocks are all removed before counting.
    """
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.DOTALL)
    md = re.sub(r"```.*?```", " ", md, flags=re.DOTALL)
    kept = []
    for line in md.splitlines():
        s = line.strip()
        if not s or s.startswith((">", "#", "|", "---", "***")):
            continue
        kept.append(s)
    return len(" ".join(kept).split())


def my_section() -> str:
    """The section this student is in, from their own student.json."""
    raw = read("student.json")
    if not raw:
        return ""
    try:
        return str(json.loads(raw).get("section", "")).strip().lower()
    except (json.JSONDecodeError, AttributeError):
        return ""


def parse_published(text: str, section: str) -> int | None:
    """Read the published week for one section.

    The file carries a line per section — `en=3`, `tr=2` — because two sections
    drift apart the first time a holiday lands on one of their days. A bare
    number is the older single-section format and applies to everyone.
    """
    weeks: dict[str, int] = {}
    only = None
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            if value.strip().isdigit():
                weeks[key.strip().lower()] = int(value.strip())
        elif line.isdigit():
            only = int(line)
    if section and section in weeks:
        return weeks[section]
    if only is not None:
        return only
    if weeks and len(set(weeks.values())) == 1:
        # No section declared, but the sections happen to be in step, so the
        # answer is the same either way.
        return next(iter(weeks.values()))
    return None


def published_week() -> int | None:
    """The week the course says it is on. None if it cannot be reached."""
    try:
        with urllib.request.urlopen(COURSE_WEEK_URL, timeout=5) as response:
            return parse_published(response.read().decode("utf-8"), my_section())
    except (urllib.error.URLError, ValueError, IndexError, OSError, TimeoutError):
        return None


def resolve_week() -> tuple[int, str]:
    """Decide which week to check, and say where the number came from.

    Order matters. The published number wins over the local file, because the
    failure this prevents is a stale local file quietly checking Week 1 all
    through Week 5 and showing you a green tick you have not earned.
    """
    override = os.environ.get("AIASD_WEEK", "").strip()
    if override:
        try:
            return int(override), "AIASD_WEEK"
        except ValueError:
            print(f"AIASD_WEEK must be a number, not {override!r}")
            raise SystemExit(1) from None

    published = published_week()
    if published is not None:
        if published != cached_week():
            try:
                (ROOT / "CURRENT_WEEK_CACHE.txt").write_text(f"{published}\n", encoding="utf-8")
            except OSError:
                pass  # read-only checkout; the number is still correct
        return published, "published by the course"
    return cached_week(), "cached — the course could not be reached"


MANIFEST_URL = (
    "https://raw.githubusercontent.com/vedatcoskun-course/aiasd-template/main/AI_MANIFEST.txt"
)
RAW_BASE = "https://raw.githubusercontent.com/vedatcoskun-course/aiasd-template/main/"


def sync_course_files(current: int) -> None:
    """Bring the course's files into this repository, so nobody has to fetch the template.

    The template publishes AI_MANIFEST.txt: one line per file, `sha256  path`. Two
    kinds of entry, treated differently:

    - course documents at the root (`AI_*`, `AI_Doc2_media/…`): the course owns them,
      so a missing or changed one is (re)written here;
    - a week's folder (`weekNN/…`) and the `PROPOSAL.md` scaffold: yours once you have
      them, so a file is written only if it does not exist yet — never overwritten —
      and only for weeks the course has published (NN <= current).

    Whatever arrives is untracked until you `git add .`; the run says so. Offline,
    or under CI, nothing happens. Anything that goes wrong means carrying on.
    """
    if os.environ.get("GITHUB_ACTIONS") or os.environ.get("AIASD_WEEK") or os.environ.get("AIASD_SLOT"):
        return
    try:
        with urllib.request.urlopen(MANIFEST_URL, timeout=6) as response:
            manifest = response.read().decode("utf-8")
    except (urllib.error.URLError, OSError, TimeoutError, UnicodeDecodeError):
        return
    fetched: list[str] = []
    for line in manifest.splitlines():
        parts = line.strip().split("  ", 1)
        if len(parts) != 2 or ".." in parts[1] or parts[1].startswith("/"):
            continue
        digest, rel = parts
        target = ROOT / rel
        if rel.startswith("week"):
            m = re.match(r"week(\d{2})/", rel)
            if not m or int(m.group(1)) > current or target.exists():
                continue
        elif rel == "PROPOSAL.md":
            if current < 2 or target.exists():
                continue
        elif rel.startswith("AI_"):
            if target.exists():
                try:
                    if hashlib.sha256(target.read_bytes()).hexdigest() == digest:
                        continue
                except OSError:
                    continue
        else:
            continue
        try:
            with urllib.request.urlopen(RAW_BASE + urllib.parse.quote(rel), timeout=10) as response:
                data = response.read()
        except (urllib.error.URLError, OSError, TimeoutError):
            continue
        if hashlib.sha256(data).hexdigest() != digest:
            continue
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            fetched.append(rel)
        except OSError:
            continue
    if fetched:
        print("  " + say("Course files brought into this repository (add them with `git add .`):"))
        for rel in fetched:
            print(f"    + {rel}")
        print()


def week_to_show(args: list[str], current: int) -> tuple[int, str]:
    """The week a student's run prints: the one named on the command line, else the current one.

    Returns (week, "") or (0, the message to print). Showing every week since Week 1 made the
    list grow by a screenful each week, and an old, finished week buried the one that is due.
    """
    args = [a.strip() for a in args if a.strip() and a.strip().lower() not in ("tr", "en")]  # language words
    if not args:
        return current, ""
    if len(args) > 1 or not args[0].isdigit():
        return 0, say("Give one week number, for example: python .github/check_deliverables.py 2")
    n = int(args[0])
    if n < 1:
        return 0, say("Weeks start at 1.")
    if n > current:
        return 0, say("Week {n} has not started yet. The course is at week {current}.", n=n, current=current)
    return n, ""


def main() -> int:
    global RUN_WEEK, LANG
    LANG = wanted_lang()  # before anything is printed: the update warnings are said in it too
    maybe_update()
    current, source = resolve_week()
    RUN_WEEK = current
    sync_course_files(current)

    print("=" * 64)
    print("  " + say("Secret scan"))
    print("=" * 64)
    secrets_ok = check_secrets()
    if secrets_ok:
        print("  " + say("no API keys found") + "\n")
    else:
        print("  " + say("KEYS FOUND — remove them and rotate them NOW"))
        print("  " + say("This is an automatic 10-point deduction. Remove the key, rotate it"))
        print("  " + say("at the provider, and never commit one again.") + "\n")

    if current < 1:
        if source.startswith("cached"):
            print(say("Cannot tell which week it is."))
            print(say(
                "The course could not be reached and there is no cached week number\n"
                "yet — this is the first run on this machine, offline. Connect once\n"
                "and run it again; after that it works without a network."
            ))
        else:
            print(say("Week 0 ({source}) — nothing to check yet.", source=say(source)))
            print(say("The course has not started checking deliverables. Nothing for you to do."))
        return 0 if secrets_ok else 1

    # The instructor's capture sets AIASD_SLOT; it reads weeks 1..current and counts only the
    # week it asked for. A student's own run shows one week: the current one, or the one
    # named on the command line.
    scored = os.environ.get("AIASD_SLOT", "").strip().lower()
    grading = scored in (SESSION, DEADLINE)
    shown, problem = (current, "") if grading else week_to_show(sys.argv[1:], current)
    if problem:
        print(problem)
        return 2

    if grading:
        print(f"Checking weeks 1-{current}  ({source})\n")
        last = current
    else:
        print(say("Checking week {shown}  ({source})", shown=shown, source=say(source)))
        other = shown - 1 if shown > 1 else (shown + 1 if current > shown else 0)
        if other:
            print(say("To check another week, add its number: python .github/check_deliverables.py {other}", other=other))
        print()
        last = shown

    for week in range(1, last + 1):
        if week in CHECKS:
            CHECKS[week]()

    def show(rows: list[tuple[str, str, str, str, str]], heading: str, by_week: bool) -> None:
        """One line per check, the verdict first so a column of PASS and FAIL can be scanned,
        and nothing padded to a common width: a line is as long as its sentence."""
        if not rows:
            return
        print("=" * 64)
        print(f"  {heading}")
        print("=" * 64)
        seen = None
        for wk, name, status, _, detail in rows:
            if by_week and wk != seen:
                print(f"  -- Week {wk[1:]} " + "-" * (58 - len(wk)))
                seen = wk
            if status == PASS:
                print(f"  ✓ {say('PASS')}  {shown_sentence(name)}")
            else:
                print(f"  ✗ {say('FAIL')}  {shown_sentence(detail)}")
        print()

    if grading:
        slots = [SESSION] if scored == SESSION else [SESSION, DEADLINE]
        rows = [r for r in results if r[3] in slots]
        show(rows, f"Weeks 1-{current}", True)
        failed = [r for r in rows if r[2] != PASS]
        print("-" * 64)
        print(
            f"  {len(rows) - len(failed)} passed, {len(failed)} failed  "
            f"(weeks 1-{current}, {scored})"
        )
        print("-" * 64)
        return 0 if (not failed and secrets_ok) else 1

    mine = [r for r in results if r[0] == f"W{shown}"]
    if not mine:
        print(say("There are no checks for week {shown} yet.", shown=shown))
        return 0 if secrets_ok else 1
    past = shown < current
    session_rows = [r for r in mine if r[3] == SESSION]
    deadline_rows = [r for r in mine if r[3] == DEADLINE]
    show(session_rows, say("Was due at the end of the session" if past else "Due at the end of the session"), False)
    show(deadline_rows, say("Was due Saturday 23:59" if past else "Due by Saturday 23:59"), False)

    s_bad = [r for r in session_rows if r[2] != PASS]
    d_bad = [r for r in deadline_rows if r[2] != PASS]
    older: dict[int, int] = {}
    for r in results:
        n = int(r[0][1:])
        if n < shown and r[2] != PASS:
            older[n] = older.get(n, 0) + 1
    print("-" * 64)
    print("  " + say("In the lab:     {a} of {b} done", a=len(session_rows) - len(s_bad), b=len(session_rows)))
    print("  " + say("By Saturday:    {a} of {b} done", a=len(deadline_rows) - len(d_bad), b=len(deadline_rows)))
    if older:
        listing = " · ".join(f"week{n:02d}: {older[n]}" for n in sorted(older, reverse=True))
        print("  " + say(
            "Earlier weeks, checks still failing: {listing} — see one with: python .github/check_deliverables.py {n}",
            listing=listing, n=max(older)))
    print("-" * 64)
    if d_bad and not s_bad and not past:
        print(say(
            "\n  {n} still to do before Saturday 23:59. Those do not fail this run —\n"
            "  they are not due yet. The lab items are what the end-of-session mark reads.",
            n=len(d_bad)))
    if LANG == "tr" and _UNTRANSLATED:
        print("\n  " + say("{n} line(s) above have no Turkish yet and are shown in English.", n=len(_UNTRANSLATED)))
    return 0 if (not s_bad and secrets_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
