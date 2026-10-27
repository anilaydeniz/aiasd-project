"""The course's tests of the login (REQ-001): the same ten tests for every project.

AIASD · Atlas University · Fall 2026-27 · Week 6

These tests belong to the course, not to you: the checker brings this folder and puts it back
as it was if it is changed. They read server/login_contract.json, where you write, by hand,
the method and path of your three login endpoints exactly as they are in week05/api.md and
the names of the fields. The token must be a top-level key of the login answer, for example
{"token": "..."}, not inside another object.

Run them from the root of your repository, with the Week 6 packages installed:

    pip install -r week06/requirements.txt
    python -m pytest course_tests -q

The rules they check are the same for everyone:
- a code has 4 digits, is valid for 10 minutes and works once;
- the same address asking for a new code within 60 seconds gets 429;
- a wrong or expired code gets 401;
- after 3 wrong codes in a row (a new code does not start the count again), every login for
  that address gets 429 for 15 minutes, even with the right code; after that, a new code works;
- the right code gives a token, and GET me with "Authorization: Bearer <token>" answers 200
  with the address; no token or a wrong one gets 401;
- something that is not an e-mail address gets 422.

The code is not e-mailed here: the tests set the environment variable AIASD_CODE_FILE, and the
course's login (server/course_login.py) writes the code to that file instead of sending it.
Time is moved with freezegun. If a test fails, check server/login_contract.json first, then
check that server/main.py includes the router of server/course_login.py.
"""

from __future__ import annotations

import json
import re
import uuid
from datetime import timedelta
from pathlib import Path

import freezegun
import pytest
from fastapi.testclient import TestClient
from freezegun import freeze_time

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "server" / "login_contract.json"
KEYS = ("request_code", "login", "me", "email_field", "code_field", "token_field")
ENDPOINT = re.compile(r"(GET|POST|PUT|PATCH|DELETE) (/\S*)", re.IGNORECASE)
START = "2026-11-02 10:00:00"

# FastAPI's TestClient runs each endpoint in a worker thread, and freezegun leaves threads on the
# real clock by default; these tests let the worker threads see the moved clock too.
freezegun.configure(
    default_ignore_list=[
        m for m in freezegun.config.DEFAULT_IGNORE_LIST if m not in ("threading", "queue")
    ]
)


def _read_contract() -> dict:
    """The contract as written, or pytest.fail with what is wrong in it."""
    if not CONTRACT.is_file():
        pytest.fail("Fill in server/login_contract.json: the file is missing.")
    try:
        data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    except ValueError as error:
        pytest.fail(f"Fill in server/login_contract.json: it is not valid JSON ({error}).")
    problems = []
    for key in KEYS:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip() or "[" in value:
            problems.append(f"{key} is not filled in")
        elif key in ("request_code", "login", "me") and not ENDPOINT.fullmatch(value.strip()):
            problems.append(f'{key} must be a method and a path, such as "POST /auth/code"')
    if problems:
        pytest.fail("Fill in server/login_contract.json: " + "; ".join(problems) + ".")
    return data


@pytest.fixture
def contract() -> dict:
    return _read_contract()


@pytest.fixture
def client(contract: dict) -> TestClient:
    try:
        from server.main import app
    except Exception as error:  # noqa: BLE001 - any import error is the student's to see
        pytest.fail(f"server/main.py could not be imported: {type(error).__name__}: {error}")
    return TestClient(app)


@pytest.fixture
def code_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "code.txt"
    monkeypatch.setenv("AIASD_CODE_FILE", str(path))
    return path


def _address(contract: dict) -> str:
    domain = str(contract.get("test_email_domain") or "example.com").strip().lstrip("@")
    return f"test-{uuid.uuid4().hex[:10]}@{domain}"


def _call(
    client: TestClient, endpoint: str, *, json_body: dict | None = None, token: str | None = None
):
    method, path = ENDPOINT.fullmatch(endpoint.strip()).groups()
    headers = {"Authorization": f"Bearer {token}"} if token is not None else {}
    return client.request(method.upper(), path, json=json_body, headers=headers)


def _said(response) -> str:
    return f"it answered {response.status_code}: {response.text[:200]}"


def _expect(response, status: int, what: str) -> None:
    ok = 200 <= response.status_code < 300 if status == 200 else response.status_code == status
    wanted = "a 2xx status" if status == 200 else str(status)
    assert ok, f"{what} should answer {wanted}; {_said(response)}"


def _ask_code(client: TestClient, contract: dict, email: str, code_file: Path) -> str:
    """Asks for a code and returns it from the code file."""
    response = _call(client, contract["request_code"], json_body={contract["email_field"]: email})
    _expect(response, 200, f"{contract['request_code']} with a valid e-mail address")
    assert code_file.is_file(), (
        "The server did not write the code to the file named by AIASD_CODE_FILE. "
        "Check that server/main.py includes course_login.router and that request_code in "
        "server/login_contract.json is the course's endpoint."
    )
    code = code_file.read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"\d{4}", code), f"The code in the file should be 4 digits; it is {code!r}."
    return code


def _wrong(code: str) -> str:
    return f"{(int(code) + 1) % 10000:04d}"


def _login(client: TestClient, contract: dict, email: str, code: str):
    body = {contract["email_field"]: email, contract["code_field"]: code}
    return _call(client, contract["login"], json_body=body)


def _token(response, contract: dict) -> str:
    try:
        token = response.json().get(contract["token_field"])
    except (ValueError, AttributeError):
        token = None
    assert isinstance(token, str) and token, (
        f'The login answer should have a non-empty "{contract["token_field"]}" at its top level; '
        f"{_said(response)}"
    )
    return token


def test_LOGIN_01_code_is_sent_to_a_valid_email(client, contract, code_file):
    """A code of 4 digits is made for a valid e-mail address."""
    _ask_code(client, contract, _address(contract), code_file)


def test_LOGIN_02_not_an_email_is_refused(client, contract, code_file):
    """Something that is not an e-mail address is refused with 422."""
    response = _call(
        client, contract["request_code"], json_body={contract["email_field"]: "not-an-email"}
    )
    _expect(response, 422, f"{contract['request_code']} with 'not-an-email'")


def test_LOGIN_03_right_code_gives_a_token(client, contract, code_file):
    """The right code logs in and gives a token."""
    email = _address(contract)
    code = _ask_code(client, contract, email, code_file)
    response = _login(client, contract, email, code)
    _expect(response, 200, f"{contract['login']} with the right code")
    _token(response, contract)


def test_LOGIN_04_wrong_code_is_refused(client, contract, code_file):
    """A wrong code is refused with 401, also one with a letter that is not ASCII."""
    email = _address(contract)
    code = _ask_code(client, contract, email, code_file)
    _expect(
        _login(client, contract, email, _wrong(code)), 401, f"{contract['login']} with a wrong code"
    )
    _expect(
        _login(client, contract, email, "\u00fc123"),
        401,
        f"{contract['login']} with the code 'ü123'",
    )


def test_LOGIN_05_token_opens_me(client, contract, code_file):
    """The token opens 'me', which shows the e-mail address."""
    email = _address(contract)
    code = _ask_code(client, contract, email, code_file)
    token = _token(_login(client, contract, email, code), contract)
    response = _call(client, contract["me"], token=token)
    _expect(response, 200, f"{contract['me']} with the token")
    assert email in response.text, (
        f"{contract['me']} should show the e-mail address {email}; {_said(response)}"
    )


def test_LOGIN_06_no_token_no_me(client, contract, code_file):
    """Without a token, or with a wrong one, 'me' is refused with 401."""
    _expect(_call(client, contract["me"]), 401, f"{contract['me']} without a token")
    _expect(
        _call(client, contract["me"], token="not-a-token"),
        401,
        f"{contract['me']} with a wrong token",
    )


def test_LOGIN_07_code_works_only_once(client, contract, code_file):
    """A code logs in once; the second time it is refused with 401."""
    email = _address(contract)
    code = _ask_code(client, contract, email, code_file)
    _expect(_login(client, contract, email, code), 200, f"{contract['login']} with the right code")
    _expect(
        _login(client, contract, email, code), 401, f"{contract['login']} with a code already used"
    )


def test_LOGIN_08_code_expires_after_10_minutes(client, contract, code_file):
    """A code older than 10 minutes is refused with 401."""
    email = _address(contract)
    with freeze_time(START, real_asyncio=True) as clock:
        code = _ask_code(client, contract, email, code_file)
        clock.tick(timedelta(minutes=10, seconds=1))
        _expect(
            _login(client, contract, email, code),
            401,
            f"{contract['login']} with a code 10 minutes and 1 second old",
        )


def test_LOGIN_09_new_code_within_a_minute_is_refused(client, contract, code_file):
    """A new code within 60 seconds is refused with 429; after a minute it is sent."""
    email = _address(contract)
    with freeze_time(START, real_asyncio=True) as clock:
        _ask_code(client, contract, email, code_file)
        clock.tick(timedelta(seconds=30))
        again = _call(client, contract["request_code"], json_body={contract["email_field"]: email})
        _expect(again, 429, f"{contract['request_code']} for the same address 30 seconds later")
        clock.tick(timedelta(seconds=31))
        _ask_code(client, contract, email, code_file)


def test_LOGIN_10_three_wrong_codes_lock_for_15_minutes(client, contract, code_file):
    """Three wrong codes lock the address for 15 minutes, even for the right code and even when a new code
    came in between; after the 15 minutes a new code works."""
    email = _address(contract)
    with freeze_time(START, real_asyncio=True) as clock:
        code = _ask_code(client, contract, email, code_file)
        for attempt in (1, 2, 3):
            _expect(
                _login(client, contract, email, _wrong(code)), 401, f"wrong code number {attempt}"
            )
        _expect(_login(client, contract, email, code), 429, "the right code after three wrong ones")
        clock.tick(timedelta(minutes=15, seconds=1))
        new_code = _ask_code(client, contract, email, code_file)
        _expect(_login(client, contract, email, new_code), 200, "a new code after the 15 minutes")
        # The count goes on across new codes: two wrong codes, a new code, one more wrong code.
        other = _address(contract)
        first = _ask_code(client, contract, other, code_file)
        for attempt in (1, 2):
            _expect(
                _login(client, contract, other, _wrong(first)), 401, f"wrong code number {attempt}"
            )
        clock.tick(timedelta(seconds=61))
        second = _ask_code(client, contract, other, code_file)
        _expect(
            _login(client, contract, other, _wrong(second)),
            401,
            "a third wrong code, after a new code",
        )
        _expect(
            _login(client, contract, other, second),
            429,
            "the right code after three wrong codes, even across a new code",
        )
