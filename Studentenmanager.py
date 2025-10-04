
students = []

while True:
    # Display the menu
    print("\nWelcome to Student Manager")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Statistics")
    print("5. Calculator")
    print("6. Quit")

    # Get user input for menu choice
    choice = input("Enter your choice (1-6): ")

    # Option 1: Add a new student
    if choice == "1":
        name = input("1. Add student name: ")
        try:
            age = int(input("2. Enter student age: "))
            grade = float(input("3. Enter student grade: "))
            # Create a dictionary for the student
            student = {"name": name, "age": age, "grade": grade}
            # Save it to the students list
            students.append(student)
            print("✅ Student added:", student)
        except ValueError:
            print("❌ Error: Age must be an integer and grade must be a number.")

    # Option 2: View all students
    elif choice == "2":
        if len(students) == 0:
            print("No students added yet.")
        else:
            print("\nAll students:")
            for s in students:
                print(f"- Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

    # Option 3: Search for a student by name
    elif choice == "3":
        search_name = input("Enter student name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == search_name.lower():
                print("Student found:", s)
                found = True
                break
        if not found:
            print("Student not found.")

    # Option 4: Show statistics
    elif choice == "4":
        if len(students) == 0:
            print("No students to calculate statistics.")
        else:
            ages = [s["age"] for s in students]
            grades = [s["grade"] for s in students]

            print("\nStatistics:")
            print("Max age:", max(ages))
            print("Min age:", min(ages))
            print("Avg age:", round(sum(ages) / len(ages), 2))
            print("Max grade:", max(grades))
            print("Min grade:", min(grades))
            print("Avg grade:", round(sum(grades) / len(grades), 2))

    # Option 5: Simple calculator
    elif choice == "5":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Cannot divide by zero!")
            else:
                print("Invalid operator. Please use +, -, *, or /.")
        except ValueError:
            print("Please enter valid numbers.")

    # Option 6: Quit the program
    elif choice == "6":
        print("Goodbye! 👋")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
