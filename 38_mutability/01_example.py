# mutable is a type of data that can be changed after it is created, 
# while immutable is a type of data that cannot be changed after it is created. 
# Lists are mutable, while tuples are immutable.
# immutable data types include: int, float, bool, str, tuple, frozenset

a = [] # a is an empty list
b = a # b is a reference to the same list as a, so a and b point to the same list in memory
c = [] # c is a new empty list, different from a and b
d = () # d is an empty tuple, which is immutable

a.append(35)

print(id(a))
print(id(b))