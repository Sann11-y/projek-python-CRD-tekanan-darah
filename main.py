import os
import CRD 

sistem_operasi = os.name

# Clear screen based on OS
if sistem_operasi == "nt":
    os.system("cls")
else:
    os.system("clear")

# Initialize database
CRD.init_console()

while True:
    # Clear screen
    if sistem_operasi == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    print("-" * 60)
    print("SELAMAT DATANG DI PROGRAM".center(60))
    print("Sistem Monitoring Tekanan Darah dan BMI".center(60))
    print("-" * 60)

    print("1. Buat Data Pasien Baru")
    print("2. Lihat riwayat Data Pasien")
    print("3. Analisis")
    print("4. Hapus Riwayat Data Pasien")
    print("\n")

    user_option = input("Masukan opsi: ")

    if user_option == "1":
        CRD.create_console()
    elif user_option == "2":
        CRD.read_console()
    elif user_option == "3":
        CRD.analisis_console()
    elif user_option == "4":
        CRD.delete_console()
    else:
        print("Opsi tidak valid!")

    is_done = input("Apakah Selesai (y/n)? ")
    if is_done.lower() == "y":
        break

print("Program Berakhir, Terima Kasih KAKAAAAAA!!!")