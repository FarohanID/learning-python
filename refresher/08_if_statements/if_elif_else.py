day_of_week = input("Enter the day of the week: ").strip().lower()

if day_of_week == "monday":
    print("It's the start of the work week!")
elif day_of_week == "wednesday":
    print("We're halfway through the week!")
else:
    print("It's just another day.")

print("Have a great day!")