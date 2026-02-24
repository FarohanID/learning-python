def add(x, y=8):
    print(x + y)

add(5, 8) # 13
add(5) # 13 (y defaults to 8)
add(x=5) # 13 (y defaults to 8)
add(x=5, y=10) # 15