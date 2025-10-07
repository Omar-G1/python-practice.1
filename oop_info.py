

class student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}")
