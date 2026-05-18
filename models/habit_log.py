from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.config import Base


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), index=True)
    logged_date = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)

    habit = relationship("Habit", back_populates="logs")
