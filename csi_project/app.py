from fastapi import FastAPI
from .routes import users
from .routes import courses


app = FastAPI()
app.include_router(courses.coursesrouter)
app.include_router(users.userrouter)