s = {"Bob", "Alice", "John"}
print(s)
print(type(s))
print(len(s))
print("Bob" in s)  # Check for membership
s.add("Eve")  # Add an element
print(s)
s.remove("Alice")  # Remove an element
print(s)
s.add("Bob")  # Attempt to add a duplicate element (will have no effect)
print(s)
s2 = {"Charlie", "David"}
s_union = s.union(s2)  # Union of two sets
print(s_union)
s_intersection = s.intersection(s2)  # Intersection of two sets
print(s_intersection)
s_difference = s.difference(s2)  # Difference of two sets
print(s_difference)
# Sets are unordered collections, so indexing like s[0] is not allowed and will raise an error.
# Also, sets do not support slicing operations.
# The following operations would raise errors:
# print(s[0])  # Attempt to access by index (will raise TypeError)
# print(s[1:3])  # Attempt to slice (will raise TypeError)
# However, you can convert a set to a list or tuple if needed