import math

print("===Program Lingkaran===")

jari_jari = float(input("masukkan nilai jari_jari (r):"))
print("\npilihan Menu:")
print("1. Menghitug keliling lingkaran")
print("2. Menghitung Luas Lingkaran")
pilihan= input("masukkan pilihan angka:")
if pilihan =="1":
    keliling=2*math.pi*jari_jari
    print(f"\nHasil Keliling Lingkaran:{keliling:.2f}")

elif pilihan == "2":
    luas=math.pi*(jari_jari ** 2)
    print(f"\nHasil Luas Lingkaran: {luas:.2f}")

else:
    print("\nPilihan tidak valid! Silahkan jalankan ulang dan pilih 1 atau 2.")