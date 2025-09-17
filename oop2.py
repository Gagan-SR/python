# Object-Oriented Programming Example in Python

# Class (Blueprint)
class Student:
    # Constructor (to initialize objects)
    def __init__(self, name, roll):
        self.name = name      # Attribute
        self.roll = roll      # Attribute

    # Method (Behavior)
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Inheritance Example
class GraduateStudent(Student):
    def __init__(self, name, roll, course):
        super().__init__(name, roll)   # Call parent constructor
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Course: {self.course}")

# Polymorphism Example
def show_info(student):
    student.display()

# Objects (Instances of class)
s1 = Student("Rahul", 101)
s2 = GraduateStudent("Priya", 201, "Computer Science")

# Encapsulation: Accessing data via methods
show_info(s1)
show_info(s2)
