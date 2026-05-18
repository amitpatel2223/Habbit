from fastapi import FastAPI
from database import engine, Base
from models import Habit, HabitLog
from controllers.habit_controller import router as habit_router
from controllers.habit_log_controller import router as habit_log_router
from controllers.ai_controller import router as ai_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Daily Habit Tracker API", description="Habit Tracking API")

# Include routers
#app.include_router(habit_router)
#app.include_router(habit_log_router)
app.include_router(ai_router)

# from controllers.ai_controller import router as ai_router
# from ai.initialize_data import initialize_vector_db
# @app.on_event("startup")
# def startup_event():

#     initialize_vector_db()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
