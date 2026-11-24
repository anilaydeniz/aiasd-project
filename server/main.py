"""
server/main.py: the server of your project (FastAPI).
AIASD · Atlas University · Fall 2026-27 · Week 5

Run it from the root of your repository:

    uvicorn server.main:app --reload

then open http://127.0.0.1:8000/docs in the browser: FastAPI lists every endpoint there,
and you can try each one. Stop the server with Ctrl+C.

The rule of this file: every endpoint here is a row of week05/api.md, with the same method
and the same path, and every row of week05/api.md is an endpoint here. The checker
compares the two.
"""

import json
import os
import urllib.request
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from server import chat, course_login, orders, prep

# --- Brevo HTTPS Email Delivery Bridge (REQ-001) ---
_orig_deliver = course_login._deliver


def _send_brevo_api(email: str, code: str, app_name: str) -> bool:
    api_key = os.environ.get("BREVO_API_KEY")
    if not api_key:
        return False
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key.strip(),
        "content-type": "application/json",
    }
    sender_email = (
        os.environ.get("SMTP_FROM")
        or "anilaydeniz76@gmail.com"
    )
    payload = {
        "sender": {"name": app_name, "email": sender_email},
        "to": [{"email": email}],
        "subject": f"Your login code for {app_name}",
        "htmlContent": (
            f"<p>Your login code for <strong>{app_name}</strong> is <strong>{code}</strong>. "
            "It is valid for 10 minutes.</p>"
        ),
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status in (200, 201)


def _custom_deliver(email: str, code: str) -> None:
    # 1. During course tests / CI: write to code file
    if os.environ.get("AIASD_CODE_FILE"):
        return _orig_deliver(email, code)

    # 2. Try Brevo HTTPS REST API (guaranteed delivery across cloud / Render free tier):
    if os.environ.get("BREVO_API_KEY"):
        try:
            app_name = course_login._field("app_name", "KitchenOps")
            if _send_brevo_api(email, code, app_name):
                return
        except Exception:
            pass

    # 3. Fallback to standard SMTP:
    try:
        return _orig_deliver(email, code)
    except Exception:
        pass


course_login._deliver = _custom_deliver

app = FastAPI(title="KitchenOps")
app.include_router(course_login.router)
app.include_router(prep.router)
app.include_router(orders.router)
app.include_router(chat.router)

WEB = Path(__file__).resolve().parent.parent / "web"
if WEB.is_dir():
    app.mount("/web", StaticFiles(directory=WEB, html=True), name="web")


@app.get("/health")
def health() -> dict:
    """The server is running. A technical endpoint: it serves no requirement."""
    return {"status": "ok"}
