age = input("Enter your age: ")
print("Your age is:", age)
print("Your age plus 10 is:", int(age) + 10)  # This will now work because age is cast to an integer

# Explanation:
# By default, input() returns a string
# If you want to perform numerical operations, you need to cast the input to the appropriate type (e.g., int or float)
# If the user enters a non-numeric value, this will raise a ValueError
# To handle this, you can use a try-except block to catch the error and prompt the user to enter a valid number