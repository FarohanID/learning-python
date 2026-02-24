class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
    
person = Person("Alice", 30)
print(str(person))  # Output: Person Alice, 30 years old.
print(repr(person)) # Output: <Person(Alice, 30)>
print(person)       # Output: Person Alice, 30 years old.

# The __str__ method is used for a user-friendly string representation of the object, 
# while the __repr__ method is meant for an unambiguous representation that can be used to recreate the object.