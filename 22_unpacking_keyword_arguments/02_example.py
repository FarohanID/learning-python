def named(name, age):
    print(name, age)

details = {"name": "Alice", "age": 30}
named(**details)