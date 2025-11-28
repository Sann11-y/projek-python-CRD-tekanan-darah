import os
import CRD 

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "nt": os.system("cls")

    print(
        "-"*60,"\n",
        "|","SELAMAT DATANG DI PROGRAM".center(60),"|","\n",
        "|","Sistem Monitoring Tekanan Darah dan BMI".center(60),"|","\n"
        "-"*60,
    )

    # check database itu ada atau tidak
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

        match user_option:
            case "1": CRD.create_console()
            case "2": CRD.read_console()
            case "4": CRD.delete_console()
            case "3": CRD.analisis_console()

        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasiih KAKAAAAAA!!!") 