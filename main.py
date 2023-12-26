from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="Meu App",
    description="App de teste para FastAPI",
    version="0.0.1",
    contact={"name": "VoxelTime", "email": "suporte@thvoxel.live"},
    license_info={"name": "MIT"},
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return f"User {user.email} added to the list."


@app.get("/users/{id}")
async def get_user_by_id(
    id: int = Path(..., gt=0, description="O ID do usuário que deseja localizar"),
    q: str = Query(None, max_length=5),
):
    return {"user": users[id], "query": q}
