# Created by Nicholas
# TI-1B

def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Masukkan agka > "))
        if user == secret_number:
            print("Selamat anda berhasil menemukan angkanya")
            break
        else:
            print("Salah!")
            guess += 1
    else:
        print(f"Anda tida menemukan angkanya, angka rahasianya adalah {secret_number}")
