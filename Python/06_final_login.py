# 🥊 ROUND 6 — LOGIN + BATAS PERCOBAAN

# Buat program:

# Username benar: admin
# Password benar: 12345
# Maksimal 3 percobaan
# Kalau benar → Login Berhasil!
# Kalau 3x salah → Akun diblokir!

username_benar = 'admin'
password_benar = '12345'
percobaan = 0

while percobaan < 3:
    percobaan += 1

    username = input("Masukan Username anda : ")
    password = input("Masukan Password anda : ")

    if username == username_benar and password == password_benar:
        print("Login Berhasil!")
        break
    else:
        print("Username atau password salah!")

    if percobaan == 3:
        print("Akun anda diblokir!")