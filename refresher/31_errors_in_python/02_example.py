def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return dividend / divisor

grades = []

print("Welcome to the average grade program!")

try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is: {average}")
except ZeroDivisionError as e:
    print(f"Error: {e}")