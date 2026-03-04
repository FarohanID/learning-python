# Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates. 
# Dictionaries are written with curly brackets, and they have keys and values.

my_dict = {"name": "Farhan", "age": 29, "city": "Bandung"}
print(my_dict)
print("Its data type is", type(my_dict))

# Explaining the dictionary elements:
# "name": "Farhan" - The key is "name" and the value is "Farhan"
# "age": 29 - The key is "age" and the value is 29
# "city": "Bandung" - The key is "city" and the value is "Bandung"
# Note: In a dictionary, keys must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type and can be duplicated.

# Accessing values in a dictionary:
print("The name is:", my_dict["name"])
print("The age is:", my_dict["age"])
print("The city is:", my_dict["city"])