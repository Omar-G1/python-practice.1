import logging
logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from app.students_api import router as students_router

app = FastAPI()
# Use a prefix for student-related endpoints and assign tags for documentation
app.include_router(students_router, prefix="/students", tags=["Students"])

@app.get("/")
def home():
    return {"message": "Welcome to the Student Manager API 🚀"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}



