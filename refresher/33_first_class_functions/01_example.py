# first class functions is a programming language feature that treats functions as first-class citizens. 
# This means that functions can be assigned to variables, passed as arguments to other functions, and returned from other functions.
# In Python, functions are first-class citizens, which means that they can be treated like any other object.
# Example of first class functions in Python

# Assigning a function to a variable
def greet(name): # A simple function that takes a name as an argument and returns a greeting message
    return f"Hello, {name}!" # The function greet takes a name as an argument and returns a greeting message.

greet_function = greet # Assigning the greet function to the variable greet_function
print(greet_function("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument to another function
def call_function(func, arg): # A function that takes another function and an argument, and calls the function with the argument
    return func(arg) # The call_function function takes a function and an argument, and calls the function with the argument.
print(call_function(greet, "Bob"))  # Output: Hello, Bob!

# Returning a function from another function
def create_greeting(greeting): # A function that takes a greeting message and returns a new
    def greet(name): # A nested function that takes a name and returns a greeting message
        return f"{greeting}, {name}!" # The greet function takes a name and returns a greeting message using the greeting provided to create_greeting.
    return greet # The create_greeting function returns the nested greet function.
hello_greeting = create_greeting("Hello") # Creating a new greeting function using create_greeting
print(hello_greeting("Charlie"))  # Output: Hello, Charlie!