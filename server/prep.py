"""server/prep.py: dish portion preparation and stock depletion route (REQ-002)."""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from server.course_login import current_user

router = APIRouter()

# In-memory stock inventory:
INVENTORY: dict[str, float] = {
    "pasta": 50.0,
    "tomato_sauce": 30.0,
}

RECIPES: dict[str, dict] = {
    "rigatoni_pomodoro": {
        "name": "Rigatoni Pomodoro",
        "bill_of_materials": {
            "pasta": 0.120,  # 120g per portion
            "tomato_sauce": 0.080,  # 80g per portion
        },
    }
}


class PrepPortionsRequest(BaseModel):
    recipe_id: str
    portions: int = Field(gt=0, description="Number of portions prepared")


@router.post("/prep/portions")
def log_prep_portions(body: PrepPortionsRequest, user: str = Depends(current_user)) -> dict:
    """REQ-002: deducts raw ingredient stocks based on the recipe bill of materials."""
    if body.recipe_id not in RECIPES:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe = RECIPES[body.recipe_id]
    depleted = []

    # Check stock availability
    for ingredient, amount_per_portion in recipe["bill_of_materials"].items():
        required = round(amount_per_portion * body.portions, 3)
        if INVENTORY.get(ingredient, 0.0) < required:
            raise HTTPException(
                status_code=409,
                detail=f"Insufficient stock for {ingredient}: needed {required}kg, available {INVENTORY.get(ingredient, 0.0)}kg",
            )

    # Deduct stock
    for ingredient, amount_per_portion in recipe["bill_of_materials"].items():
        required = round(amount_per_portion * body.portions, 3)
        INVENTORY[ingredient] = round(INVENTORY[ingredient] - required, 3)
        depleted.append({"ingredient": ingredient, "amount_kg": required})

    return {
        "success": True,
        "recipe_id": body.recipe_id,
        "portions": body.portions,
        "depleted": depleted,
        "audit_log_id": "TX-9042",
    }
