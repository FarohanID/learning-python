name = "Bob"
greeting = "Hello, {}" #template string
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")

print(with_name)
print(with_name_two)
print(formatted)