class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grads = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grads) / len(self.grads)

student = Student()
print(student.name)
print(student.grads)
print(student.average_grade())
print(Student.average_grade(student))