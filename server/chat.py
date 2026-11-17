"""server/chat.py: AI kitchen assistant chatbot route (REQ-009)."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from server.course_login import current_user

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, description="Message to the AI assistant")


class ChatResponse(BaseModel):
    reply: str
    remaining_quota: int = 20


@router.post("/chat", response_model=ChatResponse)
def chat_with_assistant(body: ChatRequest, user: str = Depends(current_user)) -> dict:
    """REQ-009: initial scaffold for authenticated kitchen assistant chatbot."""
    # Draft scaffold: authenticates user and returns acknowledgment before LLM integration
    return {
        "reply": f"KitchenOps Assistant received: {body.message}",
        "remaining_quota": 20,
    }
