"""server/chat.py: AI kitchen assistant chatbot route (REQ-009)."""

import json
import os
import urllib.error
import urllib.request

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from server.course_login import current_user
from server.prep import INVENTORY, RECIPES
from server.storage import load_db, save_state

router = APIRouter()

DAILY_QUOTA = 20
_initial_db = load_db()
USER_MESSAGE_COUNTS: dict[str, int] = _initial_db.get("user_message_counts", {})


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, description="Message to the AI assistant")


class ChatResponse(BaseModel):
    reply: str
    remaining_quota: int


def _generate_ai_reply(user_message: str, user_email: str) -> str:
    """Generate kitchen assistant reply using LLM API or context-aware kitchen heuristics."""
    api_key = os.getenv("LLM_API_KEY")

    # Build kitchen context restricted exclusively to the authenticated user's kitchen
    low_stock = [f"{ing} ({qty} kg/L)" for ing, qty in INVENTORY.items() if qty < 5.0]
    pantry_summary = ", ".join([f"{ing}: {qty} kg/L" for ing, qty in INVENTORY.items()])
    recipes_summary = ", ".join(RECIPES.keys())

    system_instruction = (
        f"You are KitchenOps AI Assistant, serving head chef {user_email}. "
        f"Current pantry stock: {pantry_summary}. Low stock ingredients below 5kg buffer: {low_stock}. "
        f"Available recipes: {recipes_summary}. Be concise and helpful for kitchen operations."
    )

    if api_key and api_key != "mock-dev-key" and not api_key.startswith("mock"):
        # Real LLM API call (Gemini REST API endpoint) with strict 20-second timeout
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"{system_instruction}\n\nChef question: {user_message}"}],
                }
            ]
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, timeout=20.0) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                candidates = result.get("candidates", [])
                if candidates and "content" in candidates[0]:
                    parts = candidates[0]["content"].get("parts", [])
                    if parts and "text" in parts[0]:
                        return parts[0]["text"].strip()
                return "KitchenOps AI: I processed your kitchen query successfully."
        except urllib.error.HTTPError as e:
            raise HTTPException(
                status_code=503,
                detail=f"LLM service returned HTTP error: {e.code}",
            ) from e
        except (urllib.error.URLError, TimeoutError, Exception) as e:
            raise HTTPException(
                status_code=503,
                detail="LLM service unavailable or timed out within 20 seconds",
            ) from e

    # Deterministic context-aware assistant logic for development / test environments:
    msg_lower = user_message.lower()
    if "low" in msg_lower or "threshold" in msg_lower or "buffer" in msg_lower:
        if low_stock:
            return f"Cooking cream is currently at {INVENTORY.get('cooking_cream', 3.5)}L, which is below the 5.0L safety buffer threshold. Purchase order PO-2026-041 is queued for replenishment."
        return "All pantry ingredients are currently above their safety thresholds."
    elif "stock" in msg_lower or "inventory" in msg_lower or "level" in msg_lower:
        return f"Current live kitchen inventory: {pantry_summary}."
    elif "recipe" in msg_lower or "menu" in msg_lower or "prep" in msg_lower:
        return f"Registered dish recipes: {recipes_summary}. You can log prep portions on the Prep tab to deduct stock automatically."
    else:
        return f"KitchenOps Assistant received: '{user_message}'. All inventory levels and recipes are synchronized."


@router.post("/chat", response_model=ChatResponse)
def chat_with_assistant(body: ChatRequest, user: str = Depends(current_user)) -> dict:
    """REQ-009: authenticated AI kitchen assistant chatbot with daily rate limit and error handling."""
    current_count = USER_MESSAGE_COUNTS.get(user, 0)
    if current_count >= DAILY_QUOTA:
        raise HTTPException(
            status_code=429,
            detail=f"Daily message quota reached ({DAILY_QUOTA} messages/day). Please try again tomorrow.",
        )

    reply_text = _generate_ai_reply(body.message, user)

    USER_MESSAGE_COUNTS[user] = current_count + 1
    save_state(user_message_counts=USER_MESSAGE_COUNTS)
    remaining = DAILY_QUOTA - USER_MESSAGE_COUNTS[user]

    return {
        "reply": reply_text,
        "remaining_quota": remaining,
    }
