from typing import Optional
from pydantic import BaseModel
from src.schemas.status_endpoints import StatusEndpoints


class Status(BaseModel):
    title: str
    description: Optional[str] = None
    models_used: Optional[list[str]] = None
    endpoints: list[StatusEndpoints] = None
