# default parameter adalah parameter yang memiliki nilai default, sehingga jika kita tidak memberikan nilai saat memanggil fungsi, maka parameter tersebut akan menggunakan nilai default yang telah ditentukan.

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet() # Memanggil fungsi tanpa argumen, sehingga akan menggunakan nilai default "Guest".
greet("Alice") # Memanggil fungsi dengan argumen "Alice", sehingga akan menggunakan nilai "Alice" untuk parameter name.