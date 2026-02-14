class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grads = grades

    def average_grade(self):
        return sum(self.grads) / len(self.grads)
    
student = Student("Rolf", (90, 90, 93, 78, 90))
student2 = Student("Bob", (100, 90, 93, 78, 90))

print(student.name)
print(student.grads)
print(student.average_grade())
print(Student.average_grade(student))

print(student2.name)
print(student2.grads)
print(student2.average_grade())
print(Student.average_grade(student2))