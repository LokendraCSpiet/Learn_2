
"""
Exercise 4: Classes and Objects
Task:
1.	Create a class called Person with attributes for name, age, and email.
2.	Write a method called display_info that prints the person's details.
3.	Create a subclass called Student that inherits from Person and
adds an attribute for student_id.
4.	Write a method in the Student class that prints the student's details,
including the student_id.
"""


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


# Create an instance of Person
person1 = Person("Alice", 25, "alice@example.com")
print("Person:")
person1.display_info()
print()

# Create an instance of Student
student1 = Student("Bob", 20, "bob@student.com", "S12345")
print("Student:")
student1.display_info()
