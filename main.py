from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

from api import hosting, websites

app = FastAPI(
    title="Busco Hosting API",
    description="API para operações CRUD relacionadas à Planos de Hospedagem e Websites",
    version="0.0.1",
    contact={"name": "VoxelTime", "email": "suporte@thevoxel.live"},
)

app.include_router(hosting.router)
app.include_router(websites.router)