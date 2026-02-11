def multiply(*args):
    print("Arguments received:", args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(2, 3, 4))  # Outputs: 24