from sqlalchemy.orm import Session
from models import Habit, HabitLog
from schemas import HabitCreate, HabitUpdate, HabitLogCreate


# Habit Services
def get_all_habits(db: Session):
    return db.query(Habit).all()


def get_habit_by_id(db: Session, habit_id: int):
    return db.query(Habit).filter(Habit.id == habit_id).first()


def create_habit(db: Session, habit: HabitCreate):
    db_habit = Habit(**habit.dict())
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def update_habit(db: Session, habit_id: int, habit_update: HabitUpdate):
    db_habit = get_habit_by_id(db, habit_id)
    if db_habit:
        update_data = habit_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_habit, field, value)
        db.commit()
        db.refresh(db_habit)
    return db_habit


def delete_habit(db: Session, habit_id: int):
    db_habit = get_habit_by_id(db, habit_id)
    if db_habit:
        db.delete(db_habit)
        db.commit()
    return db_habit


# Habit Log Services
def get_habit_logs(db: Session, habit_id: int):
    return db.query(HabitLog).filter(HabitLog.habit_id == habit_id).all()


def log_habit(db: Session, habit_log: HabitLogCreate):
    db_log = HabitLog(**habit_log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_log_by_id(db: Session, log_id: int):
    return db.query(HabitLog).filter(HabitLog.id == log_id).first()


def update_log_completion(db: Session, log_id: int, is_completed: bool):
    db_log = get_log_by_id(db, log_id)
    if db_log:
        db_log.is_completed = is_completed
        db.commit()
        db.refresh(db_log)
    return db_log
