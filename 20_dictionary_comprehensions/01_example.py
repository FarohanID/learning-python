user = [
    (0, "Bob", "password"),
    (1, "Rolf", "1234"),
    (2, "Jose", "abcd"),
    (3, "username", "xyz"),
]

username_mapping = {user[1]: user for user in user}
print(username_mapping)
print(username_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Access granted")
else:
    print("Access denied")