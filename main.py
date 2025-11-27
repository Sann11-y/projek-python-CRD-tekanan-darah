import os
import CRD 
from google import genai
import dotenv
dotenv.load_dotenv('GeminiApi.env')
client = None
try:
    client = genai.Client()
except Exception as e:
    print(f'Eror API KEYS gagal dimuat atau tidak valid. \n Detail: {e}')
if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("PEMERKSAAN TEKANAN DARAH")
    print("=========================")

    # check database itu ada atau tidak
    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("PEMERKSAAN TEKANAN DARAH")
        print("=========================")

        print(f"1. Buat Data Pasien Baru")
        print(f"2. Lihat riwayat Data Pasien")
        print(f"4. Hapus Riwayat Data Pasien")
        print(f"\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1": CRUD.create_console()
            case "2": CRUD.read_console()
            case "4": CRUD.delete_console()

        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasiih KAKAAAAAA!!!") 