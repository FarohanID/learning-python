def devide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Error: Division by zero is not allowed."
    
result = devide(15, 3)
print("The result is:", result)