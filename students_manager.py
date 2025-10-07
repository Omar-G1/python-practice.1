import json
import os
import statistics as stats

FILE_PATH = "students.json"

class StudentManager:
    def __init__(self):
        self.students = self._load_students()

    def _load_students(self):
        if os.path.exists(FILE_PATH):
            try:
                with open(FILE_PATH, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("⚠️ Students file is corrupted. Starting with an empty list.")
        return []

    def _save_students(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, grade, age):
        student = {"name": name, "grade": grade, "age": age}
        self.students.append(student)
        self._save_students()
        print(f"✅ Added {name}")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            print(f"{s['name']} - Grade: {s['grade']}, Age: {s['age']}")

    def search_student(self, name):
        found = [s for s in self.students if s["name"].lower() == name.lower()]
        if found:
            for s in found:
                print(f"Found: {s['name']} (Grade: {s['grade']}, Age: {s['age']})")
        else:
            print("Student not found.")

    def statistics(self):
        if not self.students:
            print("No students for stats.")
            return
        grades = [s["grade"] for s in self.students]
        print(f"Average grade: {stats.mean(grades):.2f}")
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")

    def calculator(self, num1, num2, operation):
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2 if num2 != 0 else "Error: divide by zero"
        else:
            return "Error: unknown operation"

