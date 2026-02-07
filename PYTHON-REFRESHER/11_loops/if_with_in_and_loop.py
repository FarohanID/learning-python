number = 7

while True:
    user_input = input("Would you like to play? (y/n): ")

    if user_input == "y":
        break
    elif user_input == "n":
        print("Maybe next time!")
        exit()

user_number = int(input("Guess our number: "))
if user_number == number:
    print("You guessed correctly!")
elif abs(number - user_number) == 1:
    print("You were off by one!")
else:
    print("Sorry, better luck next time.")