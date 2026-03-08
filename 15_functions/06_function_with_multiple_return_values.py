# function with multiple return values

def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    perkalian = a * b
    pembagian = a / b
    return penjumlahan, pengurangan, perkalian, pembagian

nilai1 = float(input("Masukkan nilai pertama: "))
nilai2 = float(input("Masukkan nilai kedua: "))

hasil = hitung(nilai1, nilai2)

print(f"Hasil penjumlahan: {hasil[0]}")
print(f"Hasil pengurangan: {hasil[1]}")
print(f"Hasil perkalian: {hasil[2]}")
print(f"Hasil pembagian: {hasil[3]}")