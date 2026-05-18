from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HabitLogBase(BaseModel):
    habit_id: int
    is_completed: bool


class HabitLogCreate(HabitLogBase):
    pass


class HabitLogResponse(HabitLogBase):
    id: int
    logged_date: datetime

    class Config:
        from_attributes = True
