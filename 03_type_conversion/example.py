# Type Conversion is the process of converting a value from one data type to another. 
# In Python, there are two types of type conversion: implicit and explicit.

# Implicit Type Conversion
num1 = 10
num2 = 5.5
result = num1 + num2  # num1 is implicitly converted to float
print("Result of implicit type conversion:", result)  # Output: 15.5

# Explicit Type Conversion
num3 = "20"
num4 = int(num3)  # Explicitly converting string to integer
print("Result of explicit type conversion:", num4)  # Output: 20

# Another example of explicit type conversion
num5 = 3.14
num6 = int(num5)  # Explicitly converting float to integer (truncates decimal)
print("Result of explicit type conversion (float to int):", num6)  # Output: 3

# Example of converting a string to a float
num7 = "2.718"
num8 = float(num7)  # Explicitly converting string to float
print("Result of explicit type conversion (string to float):", num8)  # Output: 2.718

# Example of converting an integer to a string
num9 = 42
num10 = str(num9)  # Explicitly converting integer to string
print("Result of explicit type conversion (int to string):", num10)  # Output: "42"