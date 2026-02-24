def user_age_in_seconds():
    user_age = int(input("Enter your age in years: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is approximately: {age_seconds} seconds")

print("Welcome to the age in seconds calculator!")
user_age_in_seconds()

print("Thank you for using the calculator!")