# Loop control flow statements are used to change the execution flow of a loop.
# The break statement is used to exit a loop prematurely.
# The continue statement is used to skip the current iteration of a loop and continue with the next
# The pass statement is used as a placeholder for code that will be implemented later.

# Example of break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Example of continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

# Example of pass statement
for i in range(10):
    if i == 5:
        pass
    print(i)