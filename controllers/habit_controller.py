from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import HabitCreate, HabitUpdate, HabitResponse, HabitLogCreate, HabitLogResponse,chat
from services import habit_service

router = APIRouter(prefix="/api/v1/habits", tags=["Habits"])


# Habit Routes

@router.get("", response_model=list[HabitResponse])
def get_all_habits(db: Session = Depends(get_db)):
    """Get all habits"""
    return habit_service.get_all_habits(db)


@router.get("/{habit_id}", response_model=HabitResponse)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    """Get a specific habit by ID"""
    habit = habit_service.get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit


@router.post("", response_model=HabitResponse)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    """Create a new habit"""
    return habit_service.create_habit(db, habit)


@router.put("/{habit_id}", response_model=HabitResponse)
def update_habit(habit_id: int, habit_update: HabitUpdate, db: Session = Depends(get_db)):
    """Update a habit"""
    habit = habit_service.update_habit(db, habit_id, habit_update)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit


@router.delete("/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    """Delete a habit"""
    habit = habit_service.delete_habit(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted successfully"}
