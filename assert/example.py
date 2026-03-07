# Asseert statement example

age = 16

assert age >= 18, "Age must be at least 18 to access this content."

print("Access granted. You are old enough to view this content.")

# If the assertion fails, it will raise an AssertionError with the provided message.
# If the assertion passes, it will continue to the next line of code.

# Why developers use assert statements:
# 1. Debugging: Assert statements help identify and catch bugs early in the development process by validating assumptions about the code.
# 2. Documentation: They serve as a form of documentation, indicating the expected conditions for certain variables or states in the code.
# 3. Testing: Assert statements can be used in unit tests to verify that the code behaves as expected under certain conditions.

# Note: Assert statements should not be used for handling user input or for critical checks in production code, as they can be disabled with optimization flags in Python. They are primarily intended for debugging and testing purposes.