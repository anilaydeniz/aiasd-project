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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="KitchenOps")


class CodeRequest(BaseModel):
    email: str


class TokenRequest(BaseModel):
    email: str
    code: str


class TokenResponse(BaseModel):
    token: str
    token_type: str = "bearer"


class UserProfileResponse(BaseModel):
    email: str
    role: str


@app.get("/health")
def health() -> dict:
    """The server is running. A technical endpoint: it serves no requirement."""
    return {"status": "ok"}


@app.post("/auth/code")
def ask_for_code(body: CodeRequest) -> dict:
    """REQ-001: sends a 4-digit code to the e-mail address. Built in Week 6."""
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")


@app.post("/auth/token")
def verify_code(body: TokenRequest) -> dict:
    """REQ-001: verifies the 4-digit code and issues a bearer token. Built in Week 6."""
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")


@app.get("/auth/me")
def get_current_user() -> dict:
    """REQ-001: returns the authenticated user profile from session token. Built in Week 6."""
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")
