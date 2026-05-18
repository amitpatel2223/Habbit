from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[str] = None
    is_active: Optional[bool] = None


class HabitResponse(HabitBase):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
