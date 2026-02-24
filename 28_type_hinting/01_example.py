# Type hinting is a way to indicate the expected data types of variables, 
# function parameters, and return values in Python. 
# It helps improve code readability and can assist with static type checking.
# Example of type hinting in a function definition

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!