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

    while(True):
        match sistem_operasi:
            case "nt": os.system("cls")
        
        # print(
        # "-"*60,"\n",
        # "|","SELAMAT DATANG DI PROGRAM".center(60),"|","\n",
        # "|","Sistem Monitoring Tekanan Darah dan BMI".center(60),"|","\n"
        # "-"*60,
        # )

        print(f"1. Buat Data Pasien Baru")
        print(f"2. Lihat riwayat Data Pasien")
        print(f"3. analsisi")
        print(f"4. Hapus Riwayat Data Pasien")
        print(f"\n")

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