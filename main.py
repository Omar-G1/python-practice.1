from students_manager import StudentManager
import logging

sm = StudentManager()

logging.info("Application started.")

while True:
    try:
        print("\nWelcome to Student Manager")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Statistics")
        print("5. Calculator")
        print("6. Quit")
        
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            age = int(input("Enter student age: "))
            sm.add_student(name, grade, age)
        elif choice == '2':
            sm.view_all_students()
        elif choice == '3':
            name = input("Enter student name to search: ")
            sm.search_student(name)
        elif choice == '4':
            sm.statistics()
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (add, subtract, multiply, divide): ")
            result = sm.calculator(num1, num2, operation)
            print(f"Calculator Result: {result}")
        elif choice == '6':
            print("Exiting Student Manager.")
            logging.info("Application finished.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        logging.warning("Invalid input: Non-numeric value entered for grade or age.")
        print("Invalid input. Please enter numeric values for grade and age.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        print(f"⚠️ Unexpected error: {e}")

