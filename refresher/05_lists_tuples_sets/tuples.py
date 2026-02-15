t = ("Bob", "Alice", "John")
print(t)
print(type(t))
print(len(t))
print(t[0])  # First element
print(t[1])  # Second element
print(t[-1]) # Last element
# Tuples are immutable, so the following operations would raise errors:
# t.append("Eve")  # Attempt to add an element (will raise AttributeError)
# t.remove("Alice")  # Attempt to remove an element (will raise AttributeError)
# t.sort()  # Attempt to sort the tuple (will raise AttributeError)
# However, you can create a new tuple based on existing ones
t2 = t + ("Eve",)  # Create a new tuple by adding an element
print(t2)