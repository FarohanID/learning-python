# Type hinting in Python allows you to specify the expected types of variables, function parameters, and return values. This can help improve code readability and catch potential type-related errors during development.
# Type hinting example

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Example usage
if __name__ == "__main__":
    print(greet("Alice"))

# Type hinting with a list
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)

# Example usage
if __name__ == "__main__":
    print(sum_numbers([1, 2, 3, 4, 5]))

# Type hinting with a dictionary
def count_occurrences(items: list[str]) -> dict[str, int]:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

# Example usage
if __name__ == "__main__":
    print(count_occurrences(["apple", "banana", "apple", "cherry", "banana", "apple"]))