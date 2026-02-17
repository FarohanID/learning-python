def divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both dividend and divisor must be numbers."
    
# Example usage:
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Cannot divide by zero.
print(divide(10, 'a'))  # Output: Error: Both dividend and divisor must be numbers.