# --- 1. MENULIS KE FILE ('w' = Write) ---
# Mode 'w' akan membuat file baru jika belum ada, 
# atau menimpa isi file jika sudah ada.
with open("40_file_handling/data.txt", "w") as file:
    file.write("Halo! Ini adalah baris pertama di data.txt\n")
    file.write("Python membuat pengelolaan file jadi sangat mudah.\n")
    print("Selesai menulis ke file.")

# --- 2. MEMBACA DARI FILE ('r' = Read) ---
with open("40_file_handling/data.txt", "r") as file:
    konten = file.read()
    print("\nIsi dari data.txt:")
    print(konten)

# --- 3. MENAMBAH DATA ('a' = Append) ---
# Mode 'a' tidak menghapus data lama, tapi menambahkannya di akhir.
with open("40_file_handling/data.txt", "a") as file:
    file.write("Baris ini ditambahkan tanpa menghapus yang lama.\n")
    print("\nData baru berhasil ditambahkan.")

# --- 4. MEMBACA BARIS DEMI BARIS ---
print("\nMembaca baris satu per satu:")
with open("40_file_handling/data.txt", "r") as file:
    for line in file:
        # .strip() digunakan untuk menghapus karakter enter (\n) di akhir baris
        print(f"-> {line.strip()}")