# do not use mutable default parameters in functions, as they are shared across all calls to the function. 
# This can lead to unexpected behavior if the mutable object is modified.

from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def add_grade(self, grade: int):
        self.grades.append(grade)

student1 = Student("Alice")
student1.add_grade(90)

student2 = Student("Bob")
print(student2.grades)  # This will print [90], which is unexpected because we intended for each student to have their own list of grades.

# To avoid this issue, we can use None as the default value and create a new list inside the function if the parameter is None.

class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        if grades is None:
            grades = []
        self.grades = grades

    def add_grade(self, grade: int):
        self.grades.append(grade)

student1 = Student("Alice")
student1.add_grade(90)
student2 = Student("Bob")
print(student2.grades)  # This will print [], which is the expected behavior. Each student has their own list of grades.