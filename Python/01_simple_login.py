# 🎯 Your mission

# Make a program that:

# Asks the user for a username
# Asks the user for a password
# Correct username = admin
# Correct password = 12345

# If both are correct:

# Login berhasil!

# If either one is wrong:

# Username atau password salah!

username_benar = 'admin'
password_benar = '12345'

username = input("Masukan Username anda : ")
password = input("Masukan Password anda : ")

if username == username_benar and password == password_benar:
    print("Login Berhasil!")
else:
    print("Username atau password salah!")