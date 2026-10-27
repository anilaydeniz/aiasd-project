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

from fastapi import FastAPI

from server import course_login, prep

app = FastAPI(title="KitchenOps")
app.include_router(course_login.router)
app.include_router(prep.router)


@app.get("/health")
def health() -> dict:
    """The server is running. A technical endpoint: it serves no requirement."""
    return {"status": "ok"}
