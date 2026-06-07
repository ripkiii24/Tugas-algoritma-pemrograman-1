daftar_harga = {
    "Buku Tulis": 5000,
    "Pensil 2B" : 3000,
    "Penghapus" : 2000
}

keranjang_belanja = []

print("PROGRAM KASIR INTERAKTIF\n")

print("1. DAFTAR BARANG")
for barang, harga in daftar_harga.items():
    print(f"- {barang:<12} : Rp{harga}")
print("-" * 40 + "\n")

print("2. INPUT BARANG")
while True:
    pilihan_barang = input("Masukkan nama barang: ").title()
    if pilihan_barang in daftar_harga:
        break
    else:
        print("Barang tidak valid, coba lagi.")
print("-" * 40 + "\n")

print(" 3. INPUT JUMLAH")
jumlah_beli = 0
while jumlah_beli <= 0:
    jumlah_beli = int(input(f"Jumlah beli {pilihan_barang}: "))
    if jumlah_beli <= 0:
        print("Jumlah harus lebih dari 0!")

keranjang_belanja.append((pilihan_barang, jumlah_beli))
print("-" * 40 + "\n")

print("4. STRUK")
for baris in range(3):
    if baris == 0 or baris == 2:
        for kolom in range(30):
            print("=", end="")
        print()
    else:
        barang, jumlah = keranjang_belanja[0]
        total = daftar_harga[barang] * jumlah
        print(f" {jumlah}x {barang} = Rp{total}")