# multiple conditions example

def main():
    age = int(input("Enter your age: "))
    has_license = input("Do you have a driver's license? (yes/no): ").lower()

    if age >= 18 and has_license == "yes":
        print("You are eligible to drive.")
    elif age >= 18 and has_license == "no":
        print("You need a driver's license to drive.")
    else:
        print("You are not eligible to drive.")

if __name__ == "__main__":
    main()