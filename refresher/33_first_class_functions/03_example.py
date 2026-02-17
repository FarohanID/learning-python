def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf", "age": 25},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

# def get_friend_name(friend):
#     return friend["name"]

# print(search(friends, "Rolf", get_friend_name))

print(search(friends, "Rolf", lambda friend: friend["name"]))