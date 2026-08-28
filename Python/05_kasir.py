# Buat program yang:

# Input harga barang
# Input jumlah barang
# Hitung total = harga × jumlah
# Jika total ≥ 500000 → diskon 10%
# Jika total ≥ 250000 → diskon 5%
# Selain itu → tidak ada diskon
# Tampilkan total bayar

harga_barang = int(input("Masukan Harga barang : "))
jumlah_barang = int(input("Masukan Jumlah barang : "))

total = harga_barang * jumlah_barang

if total >= 500000:
    diskon = 0.10
    print(f"Selamat anda mendapat diskon sebesar : 10% ")
    total = total - ( total * diskon )
    print(f"Total belanja anda sebesar : Rp.{total}00")

elif total >= 250000:
    diskon = 0.5
    print(f"Selamat anda mendapat diskon sebesar : 5% ")
    total = total - ( total * diskon )
    print(f"Total belanja anda sebesar : Rp.{total}00")
else:
    print(f"Total belanja anda sebesar : Rp.{total}00")