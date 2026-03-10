# logical operators are used to combine boolean expressions and return a boolean result.

# and
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# or
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# not
print(not True)  # False
print(not False) # True

# logical operators with non-boolean values
print(0 and 1)   # 0
print(1 and 0)   # 0
print(0 or 1)    # 1
print(1 or 0)    # 1
print(not 0)     # True
print(not 1)     # False