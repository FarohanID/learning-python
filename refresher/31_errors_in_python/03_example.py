def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return dividend / divisor

students = [
    {"name": "Alice", "grades": [75, 90]},
    {"name": "Bob", "grades": [50]},
    {"name": "Charlie", "grades": [90, 92]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name}'s average grade is: {average}")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades. {e}")
else:
    print("All students' average grades calculated successfully.")
finally:
    print("Grade calculation process completed.")
        