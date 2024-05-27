from pydantic import BaseModel
from typing import Optional


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
