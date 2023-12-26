from typing import Optional, List
from pydantic import BaseModel

import fastapi

router = fastapi.APIRouter()

websites = []


class Website(BaseModel):
    name: str
    is_active: bool


@router.get("/websites", response_model=List[Website])
async def get_all_websites():
    return websites


@router.post("/websites")
async def create_website(website: Website):
    websites.append(website)
    return f"Website {website} added to the Hosting plan."


@router.get("/websites/{id}")
async def get_website_by_id(id: int):
    return {"website": websites[id]}

@router.delete("/websites/{id}")
async def delete_hosting_plan_by_id(id: int):
    websites.pop(id)
    return f"{websites[id].name} removed from the Hosting plan."
