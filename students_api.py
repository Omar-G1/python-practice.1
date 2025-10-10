from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json, os

router = APIRouter()
FILE_PATH = "app/students_data.json"

# ---------------- Pydantic model ---------------- #
class Student(BaseModel):
    name: str
    grade: float
    age: int

# ---------------- Helper functions ---------------- #
def load_students():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)

# ---------------- CRUD Endpoints ---------------- #

# GET all → now relative to /students/
@router.get("/")
def get_students():
    return {"students": load_students()}

# POST new → now relative to /students/
@router.post("/")
def add_student(student: Student):
    students = load_students()
    students.append(student.dict())
    save_students(students)
    return {"message": f"✅ {student.name} added successfully"}

# GET one by name → becomes /students/{name}
@router.get("/{name}")
def get_student(name: str):
    students = load_students()
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    raise HTTPException(status_code=404, detail="Student not found")

# PUT update by name → becomes /students/{name}
@router.put("/{name}")
def update_student(name: str, student: Student):
    students = load_students()
    for s in students:
        if s["name"].lower() == name.lower():
            s.update(student.dict())
            save_students(students)
            return {"message": f"🔄 {name} updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

# DELETE by name → becomes /students/{name}
@router.delete("/{name}")
def delete_student(name: str):
    students = load_students()
    new_students = [s for s in students if s["name"].lower() != name.lower()]
    if len(new_students) == len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    save_students(new_students)
    return {"message": f"🗑️ {name} deleted successfully"}


