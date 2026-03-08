# function with user input

def user_age_in_seconds():
    user_age = int(input("Enter your age in years: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    return age_seconds

print("Welcome to the age in seconds calculator!")
age_in_seconds = user_age_in_seconds()
print(f"Your age in seconds is approximately: {age_in_seconds} seconds")
print("Thank you for using the calculator!")