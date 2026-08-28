# 🥊 ROUND 4 — ATM

# Buat program ATM dengan saldo awal Rp500.000.

# Menu:

# 1. Cek Saldo
# 2. Setor Tunai
# 3. Tarik Tunai
# 4. Keluar

# Ketentuan:

# Menu terus muncul sampai pilih 4.
# Cek Saldo → tampilkan saldo.
# Setor Tunai → tambahkan uang ke saldo.
# Tarik Tunai → kurangi saldo.
# Jika saldo tidak cukup → tampilkan Saldo tidak cukup!.
# Pilihan selain 1–4 → tampilkan Pilihan tidak valid!.

# Gunakan while + if/elif/else.

saldo = 500000

pilihan = 0

while pilihan != 4:

    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Keluar")

    pilihan = int(input("Pilih Menu 1-4 : "))

    if pilihan == 1:
        print(f"Saldo anda : {saldo}")

    elif pilihan == 2:
        setor_tunai = int(input("Masukan Jumlah setor : "))

        saldo = saldo + setor_tunai

        print(f"Saldo anda sekarang : {saldo}")

    elif pilihan == 3:
        tarik = int(input("Masukan Jumlah tarik"))

        if tarik > saldo:
            print("Saldo Anda tidak cukup")

        else:
            tarik = saldo - tarik
            print(f"Saldo Anda sekarang : {tarik}")
    else: 
        print("Terima Kasih")