from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.user.router import user_routes

Base.metadata.create_all(engine)

app = FastAPI(title="This is my task management app")
app.include_router(task_routes)
app.include_router(user_routes)