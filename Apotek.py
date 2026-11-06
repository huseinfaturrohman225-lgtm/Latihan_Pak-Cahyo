
obat = {
    "A001": {
        "nama": "Paracetamol",
        "harga": 5000,
        "stok": 20
    },
    "A002": {
        "nama": "Vitamin C",
        "harga": 10000,
        "stok": 15
    },
    "A003": {
        "nama": "Obat Batuk",
        "harga": 8000,
        "stok": 10
    },
    "A004": {
        "nama": "Antasida",
        "harga": 7000,
        "stok": 12
    }
}

def tampilkan_obat():
    print("\n========== DAFTAR OBAT ==========")
    for kode, data in obat.items():
        print("Kode  :", kode)
        print("Nama  :", data["nama"])
        print("Harga : Rp", data["harga"])
        print("Stok  :", data["stok"])
        print("---------------------------------")

def tambah_obat():
    print("\n========== TAMBAH OBAT ==========")

    kode = input("Masukkan kode obat: ")
    if kode in obat:
        print("Kode obat sudah digunakan!")
    else:
        nama = input("Masukkan nama obat: ")
        harga = int(input("Masukkan harga obat: "))
        stok = int(input("Masukkan jumlah stok: "))

        obat[kode] = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }

        print("Obat berhasil ditambahkan!")

def cari_obat():
    print("\n========== CARI OBAT ==========")

    nama_cari = input("Masukkan nama obat: ").lower()
    ditemukan = False

    for kode, data in obat.items():

        if nama_cari in data["nama"].lower():
            print("\nObat ditemukan!")
            print("Kode  :", kode)
            print("Nama  :", data["nama"])
            print("Harga : Rp", data["harga"])
            print("Stok  :", data["stok"])

            ditemukan = True

    if ditemukan == False:
        print("Obat tidak ditemukan.")

def transaksi():
    print("\n========== TRANSAKSI ==========")
    keranjang = []
    total = 0
    while True:
        tampilkan_obat()
        kode = input("\nMasukkan kode obat: ")
        if kode not in obat:
            print("Kode obat tidak ditemukan!")
            continue
        data = obat[kode]
        print("\nNama obat :", data["nama"])
        print("Harga     : Rp", data["harga"])
        print("Stok      :", data["stok"])
        jumlah = int(input("Jumlah yang dibeli: "))
        if jumlah <= 0:
            print("Jumlah pembelian tidak valid!")
            continue
        if jumlah > data["stok"]:
            print("Stok tidak mencukupi!")
            continue
        subtotal = data["harga"] * jumlah
        keranjang.append({
            "kode": kode,
            "nama": data["nama"],
            "harga": data["harga"],
            "jumlah": jumlah,
            "subtotal": subtotal
        })
        total = total + subtotal
        print("\nBarang berhasil ditambahkan ke transaksi!")
        print("Subtotal : Rp", subtotal)
        lagi = input("\nApakah ingin membeli obat lain? (y/n): ")
        if lagi.lower() == "n":
            break
    if len(keranjang) == 0:
        print("Tidak ada barang yang dibeli.")
        return

    print("\n======================================")
    print("              STRUK APOTEK")
    print("======================================")

    for item in keranjang:
        print(
            item["nama"],
            "|",
            item["jumlah"],
            "x Rp", item["harga"],
            "= Rp", item["subtotal"]
        )

    print("--------------------------------------")
    print("Total : Rp", total)

    bayar = int(input("Bayar  : Rp"))

    if bayar < total:
        print("Uang pembayaran kurang!")
        return

    kembalian = bayar - total

    for item in keranjang:
        obat[item["kode"]]["stok"] = (
            obat[item["kode"]]["stok"] - item["jumlah"]
        )

    print("Kembali: Rp", kembalian)
    print("======================================")
    print("       TRANSAKSI BERHASIL!")
    print("======================================")



def main():
    while True:
        print("\n================================")
        print("     SISTEM PENGELOLAAN APOTEK")
        print("================================")
        print("1. Tampilkan Daftar Obat")
        print("2. Tambah Obat")
        print("3. Cari Obat")
        print("4. Transaksi")
        print("5. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            tampilkan_obat()

        elif pilihan == "2":
            tambah_obat()

        elif pilihan == "3":
            cari_obat()

        elif pilihan == "4":
            transaksi()

        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak tersedia!")
main()