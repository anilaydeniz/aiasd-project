#!/usr/bin/env python3
"""
Checks this week's deliverables — the same checks the instructor runs.

Every week from 1 up to the current one is verified, not just the latest. That is
deliberate: a change that breaks Week 3 should not pass silently in Week 7.

Which week is "current" is not yours to set. It is published by the course and
read from there on every run, so the checks you see are always the checks being
run against you. The CURRENT_WEEK_CACHE.txt file is only a cache of that number, refreshed
automatically, so this still works on a train with no signal.

Run it locally before you push:
    python .github/check_deliverables.py

To look at one specific week — say, to confirm Week 2 still passes:
    AIASD_WEEK=2 python .github/check_deliverables.py
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

results: list[tuple[str, str, str, str]] = []


def check(week: int, name: str, ok: bool, detail: str = "", slot: str = SESSION) -> None:
    results.append((f"W{week}", name, PASS if ok else f"{FAIL} — {detail}", slot))


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
    check(
        week,
        f"{ai_log_path(week)} filled in",
        len(ai_log_section(week)) > 80,
        "section empty or untouched",
        DEADLINE,
    )
    evidence = ai_log_evidence(week)
    check(
        week,
        f"{ai_log_path(week)} evidence pasted",
        len(evidence) >= 80,
        f"{len(evidence)} characters in the code block — paste the real exchange",
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
        check(1, "student.json present", False, "file missing from repo root")
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        check(1, "student.json is valid JSON", False, str(exc))
        return

    fields = ("student_id", "first_name", "last_name", "nickname", "section")
    missing = [f for f in fields if not str(data.get(f, "")).strip()]
    check(1, "student.json fully filled in", not missing, f"empty: {', '.join(missing)}")
    if missing:
        return

    sid = str(data["student_id"]).strip()
    check(
        1,
        "student_id looks like a number",
        sid.isdigit() and len(sid) >= 5,
        f"got {sid!r}",
    )

    # One check, not three. Length and character set are the same requirement seen
    # from two angles, and a nickname that fails either fails for the same reason:
    # it cannot go on the board. Splitting it inflated a five-minute task into
    # three of the week's marks.
    nick = str(data["nickname"]).strip()
    usable = 2 <= len(nick) <= 20 and bool(re.fullmatch(r"[A-Za-z0-9_\-]+", nick))
    check(
        1,
        "nickname is usable on the class board",
        usable,
        f"{len(nick)} characters; use 2-20 of letters, digits, - and _",
    )

    section = str(data.get("section", "")).strip().lower()
    check(
        1,
        "section is 'en' or 'tr'",
        section in ("en", "tr"),
        f"got {section!r} — this is how your repo knows which week to check",
    )


def week1() -> None:
    check_identity()
    proof = read("week01/setup_proof.md")
    check(
        1,
        "week01/setup_proof.md present",
        bool(proof and len(proof) > 80),
        "missing or too short",
    )

    src = read("week01/hello.py")
    check(
        1,
        "week01/hello.py parses",
        parses("week01/hello.py"),
        "missing or has a syntax error",
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
            check(1, "hello.py uses an f-string", has_fstring, "no f-string found")
            check(1, "hello.py uses a list", has_list, "no list literal found")
            check(1, "hello.py uses a for-loop", has_for, "no for-loop found")
            check(1, "hello.py reads input()", has_input, "input() is never called")

    notes = prose_words(read("week01/llm_notes.md") or "")
    check(
        1,
        "week01/llm_notes.md ~300 words",
        notes >= 250,
        f"{notes} words of your own — headings, instructions and pasted blocks do "
        "not count",
        DEADLINE,
    )

    gi = read(".gitignore") or ""
    check(
        1,
        ".gitignore covers .venv and .env",
        ".venv" in gi and ".env" in gi,
        "add them",
    )
    check(
        1,
        ".env.example present",
        (ROOT / ".env.example").is_file(),
        "create it (names only)",
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
        check(week, "PROPOSAL.md at the root", False, "file missing or headings changed", slot)
        return
    for n in numbers:
        sec = secs.get(n)
        label = f"PROPOSAL.md §{n} {PROPOSAL_SECTIONS.get(n, '')}".rstrip()
        if sec is None:
            check(week, f"{label} present", False, "heading missing or altered", slot)
            continue
        floor = 60 if n > 1 else 3
        if sec["chars"] < floor:
            check(week, f"{label} filled in", False, f"{sec['chars']} characters — still the scaffold", slot)
        else:
            # The length in the heading is an ideal, not a limit (decision of 30 Sep):
            # a longer section passes.
            check(week, f"{label} filled in", True, "", slot)


def contributors(week: int) -> list[dict] | None:
    raw = read(f"week{week:02d}/contributors_{week:02d}.json")
    if raw is None:
        return None
    try:
        data = json.loads(raw.lstrip("\ufeff"))
    except json.JSONDecodeError:
        return None
    items = data.get("contributors", data) if isinstance(data, dict) else data
    return items if isinstance(items, list) else None


def check_contributors(week: int, role: str, slot: str = SESSION) -> None:
    path = f"week{week:02d}/contributors_{week:02d}.json"
    items = contributors(week)
    if items is None:
        check(week, f"{path} valid JSON", False, "missing or does not parse", slot)
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
          f"{len(ids)} entries, {len(good_ids)} valid 9-digit numbers — at most two, different, no placeholders", slot)
    me = ""
    try:
        me = str(json.loads(read("student.json") or "{}").get("student_id", "")).strip()
    except json.JSONDecodeError:
        pass
    check(week, f"{path} does not list yourself", me == "" or me.split("-")[0] not in [g.split("-")[0] for g in good_ids],
          "your own number is in it", slot)
    roles_ok = all(str(i.get("role", "")).strip() == role for i in items if isinstance(i, dict))
    check(week, f"{path} role is '{role}' for everyone listed", roles_ok, "wrong or empty role", slot)
    thin = [i for i in items if isinstance(i, dict) and len(str(i.get("what", "")).strip()) < 20]
    check(week, f"{path} says what each one did", not thin,
          f"{len(thin)} entries with no real sentence in 'what'", slot)


def week2() -> None:
    # In the lab: Part A of the proposal, two stakeholders, the first requirement list.
    check_proposal(2, range(1, 5), SESSION)
    check_contributors(2, "stakeholder", SESSION)

    raw = read("week02/requirements.json")
    ids: list[str] = []
    if raw is None:
        check(2, "week02/requirements.json present", False, "file missing")
    else:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            check(2, "requirements.json is valid JSON", False, str(exc))
        else:
            items = data.get("requirements", data) if isinstance(data, dict) else data
            if not isinstance(items, list):
                items = []
            items = [i for i in items if isinstance(i, dict) and not i.get("dropped")]
            real = [i for i in items if str(i.get("description", "")).strip() not in ("", "…")]
            check(2, "requirements.json has ≥8 entries", len(real) >= 8, f"{len(real)} filled in")
            ids = [str(i.get("id", "")).strip() for i in real]
            bad = [i for i in ids if not re.fullmatch(r"REQ-\d{3}", i)]
            dup = sorted({i for i in ids if ids.count(i) > 1})
            check(2, "IDs follow REQ-NNN, no duplicates", not bad and not dup and bool(ids),
                  f"bad: {bad[:3]} duplicated: {dup[:3]}")
            f = sum(1 for i in real if i.get("functional") is True)
            nf = sum(1 for i in real if i.get("functional") is False)
            check(2, "≥5 functional and ≥3 non-functional", f >= 5 and nf >= 3, f"{f} functional, {nf} non-functional")
            phone = any(re.search(r"phone|mobile|390", str(i.get("description", "")), re.I)
                        for i in real if i.get("functional") is False)
            check(2, "the phone-screen requirement is kept", phone, "no non-functional requirement mentions the phone screen")
            # By Saturday: every requirement prioritised and testable.
            prio = [str(i.get("priority", "")).strip().lower() for i in real]
            badp = [i.get("id") for i, pr in zip(real, prio) if pr not in ("must", "should", "could")]
            check(2, "every requirement has priority must/should/could", len(real) >= 8 and not badp,
                  f"missing or wrong: {badp[:4]}", DEADLINE)
            check(2, "not every requirement is a must", len(real) >= 8 and any(pr in ("should", "could") for pr in prio),
                  "all of them are 'must' — decide what could be cut", DEADLINE)
            thin = [i.get("id") for i in real if len(str(i.get("acceptance", "")).strip().strip("…")) < 25]
            check(2, "every requirement has an acceptance criterion", len(real) >= 8 and not thin,
                  f"missing or too short: {thin[:4]}", DEADLINE)

    # By Saturday: the rest of Part A, the SRS, the log.
    check_proposal(2, range(5, 8), DEADLINE)
    secs = proposal_sections()
    s5 = secs.get(5, {})
    if s5:
        t = s5["text"].lower()
        check(2, "PROPOSAL.md §5 names mobile, web and server",
              all(k in t for k in ("mobile", "web", "server")), "one of the three tiers is not mentioned", DEADLINE)
        check(2, "PROPOSAL.md §5 has its system context diagram", s5["mermaid"], "no ```mermaid block under §5", DEADLINE)

    srs = read("week02/SRS.md") or ""
    prose = re.sub(r"<!--.*?-->", "", srs, flags=re.DOTALL)
    check(2, "week02/SRS.md filled in", len(re.sub(r"```.*?```", "", prose, flags=re.DOTALL).strip()) > 600,
          "missing or still the scaffold", DEADLINE)
    blocks = [b for b in re.findall(r"```mermaid\n(.*?)```", prose, re.DOTALL) if "%% EXAMPLE" not in b]
    usecases = sum(len(re.findall(r"\(\[", b)) for b in blocks)
    check(2, "SRS.md use case diagram with ≥3 use cases", usecases >= 3,
          f"{usecases} use-case nodes ([…]) found in mermaid blocks", DEADLINE)
    in_srs = set(re.findall(r"REQ-\d{3}", prose))
    check(2, "SRS.md lists every REQ id from requirements.json", bool(ids) and set(ids) <= in_srs,
          f"missing in SRS: {sorted(set(ids) - in_srs)[:4]}", DEADLINE)
    check_ai_log(2)


def week3() -> None:
    """Pitch and review in the lab; Part B of the proposal and the hostile-reviewer log
    by Saturday. The pitch is read as it was pushed by the end of the lecture (11:45)."""
    # --- the pitch: six slides, each with the student's own words -----------------
    pitch = read("week03/PITCH_03.md")
    if pitch is None:
        check(3, "week03/PITCH_03.md present", False, "file missing — run the checker to fetch it, then write it")
    else:
        body = re.sub(r"<!--.*?-->", "", pitch, flags=re.DOTALL)
        slides = [x.strip() for x in re.split(r"^---\s*$", body, flags=re.M) if x.strip()]
        slides = [x for x in slides if not re.match(r"^marp:", x)]  # the front matter
        check(3, "PITCH_03.md has 7 slides", len(slides) == 7, f"{len(slides)} slides found (6 yours + the fixed reviewers' slide)")
        holes = sum(len(re.findall(r"\[[^\]\n]{1,80}\]", re.sub(r"```.*?```", "", x, flags=re.DOTALL))) for x in slides[:6])  # not inside a drawing
        check(3, "PITCH_03.md placeholders replaced", holes == 0, f"{holes} [bracketed] placeholders still there")
        def slide(n):  # 1-based, after the title slide
            return slides[n] if len(slides) > n else ""
        check(3, "slide 2 — the last time it happened, to you or in front of you", len(re.sub(r"\*\*[^*]+\*\*", "", slide(1)).strip()) > 120 and "[" not in slide(1),
              "when / where / what you did instead / what it cost — write it")
        people = len([r for r in re.findall(r"^\|\s*\d\s*\|([^|\n]{3,})\|([^|\n]{3,})\|", slide(2), re.M) if "[" not in r[0] + r[1]])
        check(3, "slide 3 — five named testers", people >= 5, f"{people} rows filled in the table")
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
        check(3, "slide 4 — three requirements, as in requirements.json", len(set(same)) >= 3,
              f"{len(set(same))} of {len(cited)} match an id + description in week02/requirements.json — copy them, do not paraphrase")
        dn = re.search(r"(does not|yapmaz)\s*:?\**\s*(.+)$", slide(3), re.I | re.M)
        check(3, "slide 4 — says what it does not do", bool(dn and len(dn.group(2).strip()) > 15 and "[" not in dn.group(2)), "the one sentence from §4")
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
        check(3, "slide 5 — the main screen, drawn", img_ok or boxes,
              "no image from your repository linked on the slide, and no text-box drawing")
        check(3, "slide 6 — one honest doubt", len(slide(5).strip()) > 60 and "[" not in slide(5), "the question and two lines on why")
    # --- the review: three reviewers, quoted sentences, a decision each -----------
    items = contributors(3) or []
    if not items:
        check(3, "week03/contributors_03.json valid JSON", False, "missing or does not parse")
    else:
        ids = [str(i.get("student_id", "")).strip() for i in items if isinstance(i, dict)]
        good = [i for i in ids if re.fullmatch(r"\d{9}(-\d+)?", i)]
        check(3, "contributors_03.json names three reviewers", len(good) == 3 and len(set(good)) == 3,
              f"{len(good)} valid numbers — need three, different")
        me = ""
        try:
            me = str(json.loads(read("student.json") or "{}").get("student_id", "")).strip()
        except json.JSONDecodeError:
            pass
        check(3, "contributors_03.json does not list yourself", me == "" or me.split("-")[0] not in [g.split("-")[0] for g in good], "your own number is in it")
        check(3, "contributors_03.json role is 'reviewer'", all(str(i.get("role", "")).strip() == "reviewer" for i in items if isinstance(i, dict)), "wrong or empty role")
        thin = [i for i in items if isinstance(i, dict) and len(str(i.get("what", "")).strip()) < 25]
        check(3, "contributors_03.json quotes what each reviewer wrote", not thin, f"{len(thin)} entries without a real sentence")
        undecided = [i for i in items if isinstance(i, dict) and (i.get("accepted") not in (True, False) or len(str(i.get("why", "")).strip()) < 15)]
        check(3, "contributors_03.json accepted/why decided for each", not undecided, f"{len(undecided)} entries without a decision and a reason")
    # --- Part A revised: the change log has started --------------------------------
    text = read("PROPOSAL.md") or ""
    m = re.search(r"^## Change log.*?$", text, re.M)
    log = re.sub(r"<!--.*?-->", "", text[m.end():], flags=re.DOTALL) if m else ""
    dated = re.findall(r"20\d\d-\d\d-\d\d", log)
    check(3, "PROPOSAL.md change log has a dated line", len(dated) >= 1, "no '2026-10-07 — §N: …' line after the review")
    # --- the group: the same list in every member's repository (added 5 Oct 2026). Whether
    # the lists of the members agree can only be seen across repositories, so that part is
    # the instructor's (grade.py groups); here: a list that can be right, and reviewers in it.
    gdata = load_json("week03/group_03.json")
    glist = gdata.get("group") if isinstance(gdata, dict) else None
    if not isinstance(glist, list):
        check(3, "week03/group_03.json valid JSON", False, "missing or does not parse — run the checker to fetch it")
    else:
        nums = [str(x).strip().split("-")[0] for x in glist if str(x).strip()]
        valid = [n for n in nums if re.fullmatch(r"\d{9}", n)]
        me = my_number()
        check(3, "group_03.json lists your group: 4 or 5 different numbers, yours included",
              len(valid) == len(nums) and len(set(valid)) == len(valid) and len(valid) in (4, 5) and (me == "" or me in valid),
              f"{len(valid)} valid numbers of {len(nums)}" + ("" if me in valid else " — your own number is missing"))
        reviewers = [str(i.get("student_id", "")).strip().split("-")[0] for i in (contributors(3) or []) if isinstance(i, dict)]
        reviewers = [r for r in reviewers if re.fullmatch(r"\d{9}", r)]  # empty entries are not reviewers (6 Oct 2026)
        outside = [r for r in reviewers if r not in valid]
        check(3, "your reviewers are members of your group", bool(reviewers) and not outside,
              f"not in group_03.json: {outside[:3]}" if outside else "no reviewers in contributors_03.json")
    # --- the main flow: the screens the Week 4 prototype is built from (added 5 Oct 2026;
    # the project is fixed at this push, and a project that cannot name its screens is not)
    sc = read("week03/screens_03.md")
    if sc is None:
        check(3, "week03/screens_03.md present", False, "file missing — run the checker to fetch it, then fill it in")
    else:
        body = re.sub(r"<!--.*?-->", "", sc, flags=re.DOTALL)
        rows = re.findall(r"^\|\s*\d+\s*\|([^|\n]*)\|([^|\n]*)\|([^|\n]*)\|\s*$", body, re.M)
        filled = [r for r in rows if "[" not in "".join(r) and r[0].strip()
                  and len(r[1].strip()) >= 5 and re.search(r"REQ-\d{3}", r[2])]
        check(3, "screens_03.md lists at least five screens of the main flow", len(filled) >= 5,
              f"{len(filled)} rows filled — each with a name, what the user does there and REQ ids")
        unknown = sorted({rid for r in filled for rid in re.findall(r"REQ-\d{3}", r[2])} - set(requirement_index()))
        check(3, "screens_03.md names only requirements that exist", bool(filled) and not unknown,
              f"not in week02/requirements.json: {unknown[:4]}")
    # --- Saturday: Part B, the store, the log ---------------------------------------
    check_proposal(3, range(8, 13), DEADLINE)
    s12 = (proposal_sections().get(12) or {}).get("text", "").lower()
    check(3, "PROPOSAL.md §12 names the store", any(k in s12 for k in ("google play", "app store", "appgallery", "galaxy store", "testflight", "play store")),
          "which store (S0), its fee and its review time", DEADLINE)
    log3 = read("week03/ai_log_03.md") or ""
    prose = re.sub(r"<!--.*?-->|```.*?```", "", log3, flags=re.DOTALL)
    objections = len([m for m in re.findall(r"^\s*[123]\.\s+(\S.{2,})$", prose, re.M) if not m.startswith("[")])
    check(3, "ai_log_03.md lists three objections", objections >= 3, f"{objections} numbered objections", DEADLINE)
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


def check_group(week: int, role: str, slot: str = SESSION) -> list[str]:
    """The three other members of the group in weekNN/contributors_NN.json; returns their numbers."""
    path = f"week{week:02d}/contributors_{week:02d}.json"
    items = contributors(week)
    if items is None:
        check(week, f"{path} valid JSON", False, "missing or does not parse", slot)
        return []
    items = [i for i in items if isinstance(i, dict)]
    ids = [str(i.get("student_id", "")).strip() for i in items]
    good = [i for i in ids if re.fullmatch(r"\d{9}(-\d+)?", i)]
    check(week, f"{path} names the three members of your group", len(good) == 3 and len(set(good)) == 3,
          f"{len(good)} valid numbers — need three, different", slot)
    me = my_number()
    check(week, f"{path} does not list yourself", me == "" or me not in [g.split("-")[0] for g in good],
          "your own number is in it", slot)
    check(week, f"{path} role is '{role}'", bool(items) and all(str(i.get("role", "")).strip() == role for i in items),
          "wrong or empty role", slot)
    thin = [i for i in items if len(str(i.get("what", "")).strip()) < 25]
    check(week, f"{path} quotes what each one found or said", bool(items) and not thin,
          f"{len(thin)} entries without a real sentence", slot)
    undecided = [i for i in items if i.get("accepted") not in (True, False) or len(str(i.get("why", "")).strip()) < 15]
    check(week, f"{path} accepted/why decided for each", bool(items) and not undecided,
          f"{len(undecided)} entries without a decision and a reason", DEADLINE)
    return [g.split("-")[0] for g in good]


def week4() -> None:
    """A clickable prototype and test cases in the lab, run by the group on the prototype;
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
              "no .html files in week04/prototype/ — run the checker to bring the starter screens")
        check(4, "prototype has at least 7 screens", False, "no screens yet", DEADLINE)
    else:
        check(4, "week04/prototype/index.html present", "index.html" in screens,
              "the first screen must be week04/prototype/index.html")
        check(4, "prototype has at least 5 screens", len(screens) >= 5,
              f"{len(screens)} .html files in week04/prototype/ — the 3 starter screens and at least 2 of yours")
        broken = sorted({f"{name} → {to}" for name, html in screens.items() for to in screen_links(html) if to not in screens})
        check(4, "every link in the prototype leads to a screen that exists", bool(screens) and not broken,
              f"broken: {broken[:3]}")
        seen, todo = set(), ["index.html"] if "index.html" in screens else []
        while todo:
            name = todo.pop()
            if name in seen or name not in screens:
                continue
            seen.add(name)
            todo.extend(screen_links(screens[name]))
        unreachable = sorted(set(screens) - seen)
        check(4, "every screen can be reached from index.html", bool(screens) and not unreachable,
              f"no link leads to: {unreachable[:3]}")
        holes = sorted(n for n, html in screens.items() if re.search(r"\[[^\]\n]{1,80}\]", visible_text(html)))
        check(4, "prototype [bracketed] parts replaced", bool(screens) and not holes, f"still in: {holes[:3]}")
        check(4, "prototype has at least 7 screens", len(screens) >= 7,
              f"{len(screens)} screens — the full flow by Saturday", DEADLINE)
        unnamed = sorted(n for n, html in screens.items() if not serves(html) or any(r not in reqs for r in serves(html)))
        check(4, "every screen names the requirements it serves", bool(screens) and not unnamed,
              f"no '<!-- serves: REQ-… -->' line, or an id that is not in requirements.json: {unnamed[:3]}", DEADLINE)
        if RUN_WEEK <= 4:  # the prototype is not kept up to date once Week 5 starts
            shown = {r for html in screens.values() for r in serves(html)}
            missing = [r for r in musts if live[r].get("functional") is True and r not in shown]
            check(4, "every functional must requirement has a screen", bool(screens) and not missing,
                  f"no screen serves: {missing[:4]}", DEADLINE)

    # --- the test cases --------------------------------------------------------------
    cases = test_cases()
    if cases is None:
        check(4, "week04/test_cases.json valid JSON", False, "missing or does not parse")
        cases = []
    else:
        ids = [str(t.get("id", "")).strip() for t in cases]
        bad = [i for i in ids if not re.fullmatch(r"TC-\d{3}-\d{2}", i)]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        check(4, "test case ids follow TC-NNN-NN, no duplicates", bool(ids) and not bad and not dup,
              f"bad: {bad[:3]} duplicated: {dup[:3]}")
        wrong = [i for i, t in zip(ids, cases)
                 if str(t.get("req", "")).strip() not in reqs or i[3:6] != str(t.get("req", "")).strip()[4:]]
        check(4, "every test case tests a requirement that exists", bool(ids) and not wrong,
              f"req missing from requirements.json, or not the number in the id: {wrong[:3]}")
        thin = [i for i, t in zip(ids, cases)
                if not (isinstance(t.get("steps"), list) and t["steps"] and all(filled(s) for s in t["steps"]))
                or len(filled(t.get("expected"))) < 15]
        check(4, "every test case has steps and an expected result", bool(ids) and not thin,
              f"empty steps or an expected result under 15 characters: {thin[:3]}")
    active = [t for t in cases if not t.get("dropped")]
    covered = {str(t.get("req", "")).strip() for t in active}
    uncovered = [r for r in musts if r not in covered]
    check(4, "every must requirement has a test case", bool(musts) and not uncovered,
          f"no test case for: {uncovered[:4]}")
    per_req = {r: sum(1 for t in active if str(t.get("req", "")).strip() == r) for r in covered}
    check(4, "at least three requirements have a second test case", sum(1 for n in per_req.values() if n >= 2) >= 3,
          f"{sum(1 for n in per_req.values() if n >= 2)} requirements with two or more — add one for when something goes wrong",
          DEADLINE)

    # --- the walk-through and the testers ----------------------------------------------
    testers = check_group(4, "prototype-tester")
    data = load_json("week04/walkthrough_04.json")
    runs = data.get("runs", data) if isinstance(data, dict) else data
    if not isinstance(runs, list):
        check(4, "week04/walkthrough_04.json valid JSON", False, "missing or does not parse")
        runs = []
    runs = [r for r in runs if isinstance(r, dict) and (filled(r.get("tc")) or filled(r.get("tester")))]
    round1 = [r for r in runs if round_of(r) == 1]
    count: dict[str, int] = {}
    for r in round1:
        t = str(r.get("tester", "")).strip().split("-")[0]
        if re.fullmatch(r"\d{9}", t):
            count[t] = count.get(t, 0) + 1
    me = my_number()
    enough = [t for t, n in count.items() if n >= 2 and t != me]
    check(4, "walk-through: three testers ran at least two test cases each", len(enough) >= 3,
          f"{len(enough)} testers with two or more runs in round 1")
    none = "no runs recorded in week04/walkthrough_04.json yet"
    check(4, "walk-through: the testers are the people in contributors_04.json",
          bool(count) and set(count) == set(testers),
          none if not runs else f"testers {sorted(count)} — contributors {sorted(testers)}")
    tested = {str(r.get("tc", "")).strip()[3:6] for r in round1} - {"001"}
    check(4, "walk-through: round 1 covers at least three requirements besides the login",
          len(tested) >= 3, none if not runs else f"{len(tested)} — run test cases of your main flow, not only REQ-001")
    known = {str(t.get("id", "")).strip() for t in cases}
    unknown = sorted({str(r.get("tc", "")).strip() for r in runs} - known)
    check(4, "walk-through: every run names a test case in test_cases.json", bool(runs) and not unknown,
          none if not runs else f"not in test_cases.json: {unknown[:3]}")
    odd = [r for r in runs if str(r.get("result", "")).strip().lower() not in ("pass", "fail", "blocked")
           or (str(r.get("result", "")).strip().lower() in ("fail", "blocked") and len(str(r.get("note", "")).strip()) < 15)]
    check(4, "walk-through: each result is pass, fail or blocked, with a note for fail and blocked",
          bool(runs) and not odd,
          none if not runs else f"{len(odd)} runs without a valid result, or a fail/blocked without a note")
    dropped = {str(t.get("id", "")).strip() for t in cases if t.get("dropped")}
    failed = {str(r.get("tc", "")).strip() for r in round1 if str(r.get("result", "")).strip().lower() == "fail"}
    rerun = {str(r.get("tc", "")).strip() for r in runs if round_of(r) == 2}
    open_fails = sorted(failed - rerun - dropped)
    check(4, "walk-through: every failed test case was run again in round 2", bool(runs) and not open_fails,
          none if not runs else
          f"no round 2 for: {open_fails[:3]} — run it again after the fix, or drop it with a Change log line", DEADLINE)

    # --- what the walk-through changed: the Change log ---------------------------------
    text = read("PROPOSAL.md") or ""
    m = re.search(r"^## Change log.*?$", text, re.M)
    log = re.sub(r"<!--.*?-->", "", text[m.end():], flags=re.DOTALL) if m else ""
    lines = [ln for ln in log.splitlines()
             if any(d >= WEEK4_FROM for d in re.findall(r"20\d\d-\d\d-\d\d", ln))
             and re.search(r"REQ-\d{3}|TC-\d{3}-\d{2}", ln)]
    check(4, "PROPOSAL.md change log: a line from the walk-through that names the ids", bool(lines),
          f"no line dated {WEEK4_FROM} or later that names a REQ or TC id", DEADLINE)

    # --- S1: the developer account -------------------------------------------------------
    st = load_json("week04/store.json")
    if not isinstance(st, dict):
        check(4, "week04/store.json valid JSON", False, "missing or does not parse", DEADLINE)
    else:
        name = " ".join(str(st.get("store", "")).lower().split())
        check(4, "store.json names the store", name in STORES,
              "one of 'Google Play', 'Huawei AppGallery', 'Samsung Galaxy Store', 'Apple App Store'", DEADLINE)
        s1 = st.get("S1") if isinstance(st.get("S1"), dict) else {}
        ok = (re.fullmatch(r"20\d\d-\d\d-\d\d", str(s1.get("date", "")).strip()) and filled(s1.get("developer_name"))
              and str(s1.get("status", "")).strip().lower() in ("applied", "verified"))
        check(4, "store.json S1 filled in (date, developer name, applied/verified)", bool(ok),
              "date as 2026-10-13, your developer name, status 'applied' or 'verified'", DEADLINE)
        ev = str(s1.get("evidence", "")).strip()
        ev_ok = (bool(ev) and ".." not in ev and not Path(ev).is_absolute() and ":" not in ev
                 and ((ROOT / ev).is_file() or (ROOT / "week04" / ev).is_file()))
        check(4, "store.json S1 screenshot saved", ev_ok, "the file named in 'evidence' is not in week04/", DEADLINE)
        s12 = (proposal_sections().get(12) or {}).get("text", "").lower()
        check(4, "store.json and PROPOSAL.md §12 name the same store",
              name in STORES and any(k in s12 for k in STORES[name]),
              "change one of them, with a Change log line", DEADLINE)

    # --- the log: acceptance criteria first ----------------------------------------------
    check(4, "ai_log_04.md names the requirements it gave the assistant",
          bool(re.search(r"REQ-\d{3}", ai_log_section(4))), "no REQ id outside the comments and the evidence", DEADLINE)
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
                print(f"  SECRET  {rel} — looks like a {label}")
                clean = False
    return clean


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
        print("  WARNING: could not reach the course on GitHub, so this run uses the")
        print("  checker copy stored in your repository, which may be out of date.")
        print("  Connect to the network and run it again before trusting the list.\n")
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

    print("  (using the current checker published by the course)\n")
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
        print("  Course files brought into this repository (add them with `git add .`):")
        for rel in fetched:
            print(f"    + {rel}")
        print()


def main() -> int:
    global RUN_WEEK
    maybe_update()
    current, source = resolve_week()
    RUN_WEEK = current
    sync_course_files(current)

    print("=" * 64)
    print("  Secret scan")
    print("=" * 64)
    secrets_ok = check_secrets()
    if secrets_ok:
        print("  no API keys found\n")
    else:
        print("  KEYS FOUND — remove them and rotate them NOW")
        print("  This is an automatic 10-point deduction. Remove the key, rotate it")
        print("  at the provider, and never commit one again.\n")

    if current < 1:
        if source.startswith("cached"):
            print("Cannot tell which week it is.")
            print(
                "The course could not be reached and there is no cached week number\n"
                "yet — this is the first run on this machine, offline. Connect once\n"
                "and run it again; after that it works without a network."
            )
        else:
            print(f"Week 0 ({source}) — nothing to check yet.")
            print("The course has not started checking deliverables. Nothing for you to do.")
        return 0 if secrets_ok else 1

    print(f"Checking weeks 1-{current}  ({source})\n")

    for week in range(1, current + 1):
        if week in CHECKS:
            CHECKS[week]()

    # Which slots this run is scored on. The instructor's end-of-session capture
    # passes AIASD_SLOT=session and is therefore blind to work that was never
    # due yet; the Saturday capture passes deadline and sees everything.
    scored = os.environ.get("AIASD_SLOT", "").strip().lower()
    if scored == SESSION:
        slots = [SESSION]
    elif scored == DEADLINE:
        slots = [SESSION, DEADLINE]
    else:
        slots = None  # a student's own run: show both, score the session

    def show(rows: list[tuple[str, str, str, str]], heading: str) -> None:
        if not rows:
            return
        width = max(len(name) for _, name, _, _ in rows)
        print("=" * 64)
        print(f"  {heading}")
        print("=" * 64)
        seen = None
        for wk, name, status, _ in rows:
            if wk != seen:
                print(f"  -- Week {wk[1:]} " + "-" * (58 - len(wk)))
                seen = wk
            mark = "✓" if status == PASS else "✗"
            print(f"  {mark}  {name.ljust(width)}   {status}")
        print()

    session_rows = [r for r in results if r[3] == SESSION]
    deadline_rows = [r for r in results if r[3] == DEADLINE]

    if slots is not None:
        rows = [r for r in results if r[3] in slots]
        show(rows, f"Weeks 1-{current}")
        failed = [r for r in rows if r[2] != PASS]
        print("-" * 64)
        print(
            f"  {len(rows) - len(failed)} passed, {len(failed)} failed  "
            f"(weeks 1-{current}, {scored})"
        )
        print("-" * 64)
        return 0 if (not failed and secrets_ok) else 1

    show(session_rows, "Due at the end of the session")
    show(deadline_rows, "Due by Saturday 23:59")

    s_bad = [r for r in session_rows if r[2] != PASS]
    d_bad = [r for r in deadline_rows if r[2] != PASS]
    print("-" * 64)
    print(f"  In the lab:     {len(session_rows) - len(s_bad)} of {len(session_rows)} done")
    print(f"  By Saturday:    {len(deadline_rows) - len(d_bad)} of {len(deadline_rows)} done")
    print(f"  (weeks 1-{current}, {source})")
    print("-" * 64)
    if d_bad and not s_bad:
        print(
            f"\n  {len(d_bad)} still to do before Saturday 23:59. Those do not fail "
            "this run —\n  they are not due yet. The lab items are what the "
            "end-of-session mark reads."
        )
    return 0 if (not s_bad and secrets_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
