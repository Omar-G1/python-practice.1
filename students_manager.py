import json
import logging
logging.basicConfig(
    filename="student_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"  
)
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
                logging.warning("Students file is corrupted. Starting with an empty list.")
                print("⚠️ Students file is corrupted. Starting with an empty list.")
        return []

    def _save_students(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, grade, age):
        student = {"name": name, "grade": grade, "age": age}
        self.students.append(student)
        self._save_students()
        logging.info(f"Added student: {name}, Grade: {grade}, Age: {age}")
        print(f"✅ Added {name}")

    def view_all_students(self):
        if not self.students:
            logging.info("View all students requested, but no students found.")
            print("No students found.")
            return
        logging.info("Viewed all students.")
        for s in self.students:
            print(f"{s['name']} - Grade: {s['grade']}, Age: {s['age']}")

    def search_student(self, name):
        found = [s for s in self.students if s["name"].lower() == name.lower()]
        if found:
            logging.info(f"Search for student '{name}' found {len(found)} match(es).")
            for s in found:
                print(f"Found: {s['name']} (Grade: {s['grade']}, Age: {s['age']})")
        else:
            logging.info(f"Search for student '{name}' found no match.")
            print("Student not found.")

    def statistics(self):
        if not self.students:
            logging.info("Statistics requested, but no students found.")
            print("No students for stats.")
            return
        grades = [s["grade"] for s in self.students]
        logging.info("Calculated statistics.")
        print(f"Average grade: {stats.mean(grades):.2f}")
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")

    def calculator(self, num1, num2, operation):
        logging.info(f"Calculator used: {num1} {operation} {num2}")
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                logging.error("Calculator error: Division by zero.")
                return "Error: divide by zero"
            return num1 / num2
        else:
            logging.warning(f"Calculator error: Unknown operation '{operation}'.")
            return "Error: unknown operation"

