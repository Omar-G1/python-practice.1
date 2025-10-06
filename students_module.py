students = []
def add_student(name, grade, age):
    student = {"name": name, "grade": grade, "age": age}
    students.append(student)
    print(f"✅ Added student: {name}.")

def view_all_students():
    if not students:
        print("No students available.")
        return
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}")
        
def search_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Found student: Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}")
            return
    print("Student not found.")

def statistics():
    if not students:
        print("No students available for statistics.")
        return
    total_students = len(students)
    avg_age = sum(student['age'] for student in students) / total_students
    avg_grade = sum(student['grade'] for student in students) / total_students
    print(f"Total Students: {total_students}, Average Age: {avg_age:.2f}, Average Grade: {avg_grade:.2f}")
    
def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."
    