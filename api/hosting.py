from typing import Optional, List
from pydantic import BaseModel

import fastapi

router = fastapi.APIRouter()

hosting_plans = []


class Hosting(BaseModel):
    name: str
    is_active: bool


@router.get("/hosting", response_model=List[Hosting])
async def get_all_hosting_plans():
    return hosting_plans


@router.post("/hosting")
async def create_hosting_plan(plan: Hosting):
    hosting_plans.append(plan)
    return f"Success."


@router.get("/hosting/{id}")
async def get_hosting_plan_by_id(id: int):
    return {"hosting": hosting_plans[id]}


@router.delete("/hosting/{id}")
async def delete_hosting_plan_by_id(id: int):
    hosting_plans.pop(id)
    return f"{hosting_plans[id].name} plan removed."
