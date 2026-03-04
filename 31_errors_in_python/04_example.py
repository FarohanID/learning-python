# Try - Except - Else - Finally Example

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("ERROR: You cannot divide by zero.")
except ValueError:
    print("ERROR: Invalid input. Please enter a valid number.")
else:
    print(f"The result of 10 divided by {num} is: {result}")
finally:
    print("Program execution completed.")

# try: code that may raise an exception
# except: code that runs if an exception occurs
# else: code that runs if no exception occurs
# finally: code that runs regardless of whether an exception occurred or not

# in short:
# - Error happens: except block runs
# - No error: else block runs
# - Finally block always runs at the end

# Why this structure is useful:
# - Keep error handling separate from normal code
# - Ensure cleanup code runs no matter what
# - Helpful for closing files, releasing resources, etc.
# - Makes programs safer and more predictable when errors occur