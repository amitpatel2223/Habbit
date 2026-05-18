from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import HabitLogCreate, HabitLogResponse
from services import habit_service

router = APIRouter(prefix="/api/v1/logs", tags=["Habit Logs"])


@router.get("/{habit_id}", response_model=list[HabitLogResponse])
def get_habit_logs(habit_id: int, db: Session = Depends(get_db)):
    """Get all logs for a specific habit"""
    habit = habit_service.get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit_service.get_habit_logs(db, habit_id)


@router.post("", response_model=HabitLogResponse)
def log_habit(habit_log: HabitLogCreate, db: Session = Depends(get_db)):
    """Log a habit completion"""
    habit = habit_service.get_habit_by_id(db, habit_log.habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit_service.log_habit(db, habit_log)


@router.get("/log/{log_id}", response_model=HabitLogResponse)
def get_log(log_id: int, db: Session = Depends(get_db)):
    """Get a specific log by ID"""
    log = habit_service.get_log_by_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log


@router.put("/log/{log_id}")
def update_log_completion(log_id: int, is_completed: bool, db: Session = Depends(get_db)):
    """Update log completion status"""
    log = habit_service.update_log_completion(db, log_id, is_completed)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log
