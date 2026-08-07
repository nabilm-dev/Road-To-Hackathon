# Loop atau perulangan biasanya pake while atau for 

us = "admin"
pw = "admin123"

ussername = input("Masukan Ussername anda : " )
password = input("Masukan Password anda : " )

while True:
    if ussername != us or password != pw:
        print("Ussername / Password anda salah! Coba Lagi!")

        ussername = input("Masukan Ussername anda : " )
        password = input("Masukan Password anda : " )

    else:
        print("Login Berhasil!")
        break