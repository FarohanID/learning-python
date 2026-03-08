# errors and exceptions
# errors are problems in the code that prevent the program from running
# exceptions are problems that occur during the execution of the program

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    y = int("hello")
except ValueError:
    print("You can't convert a string to an integer!")

try:
    z = [1, 2, 3]
    print(z[5])
except IndexError:
    print("You can't access an index that doesn't exist!")

try:
    a = {"name": "Alice"}
    print(a["age"])
except KeyError:
    print("You can't access a key that doesn't exist!")

try:
    b = None
    print(b[0])
except TypeError:
    print("You can't subscript a NoneType object!")