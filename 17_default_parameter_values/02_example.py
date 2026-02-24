default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(f"{x} + {y} = {sum}")

add(2)
default_y = 4
add(2)  # Still uses default_y as 3