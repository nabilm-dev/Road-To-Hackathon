# Mission

# Make a login system with:

# Correct username: admin
# Correct password: 12345
# User gets 3 attempts

# If correct:

# Login Berhasil!

# If incorrect:

# Username atau password salah!

# After 3 failed attempts:

# Akun anda diblokir!

username_benar = 'admin'
password_benar = '12345'

for i in range(3):

    username = input("Masukan Username anda : ")
    password = input("Masukan Password anda : ")

    if username == username_benar and password == password_benar:
        print("Login Berhasil!")
        break
    else:
        print("Username atau password salah!")

if i == 2:
    print("Akun anda diblokir!")