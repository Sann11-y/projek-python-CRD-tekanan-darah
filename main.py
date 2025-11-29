import os
import CRD

sistem_operasi = os.name

def main():
    # Initialize in-memory database
    CRD.init_console()
    
    while True:
        # Clear screen
        if sistem_operasi == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        print("-" * 50)
        print("SISTEM MONITORING TEKANAN DARAH & BMI".center(50))
        print("-" * 50)
        print("1. Buat Data Pasien Baru")
        print("2. Lihat Data Pasien") 
        print("3. Analisis Kesehatan")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("-" * 50)
        
        # Show current data count
        dataSaatini = CRD.operasi.read()
        if dataSaatini:
            print(f"📊 Data saat ini: {len(dataSaatini)} pasien")
        else:
            print("📊 Data saat ini: Kosong")
        print("-" * 50)

        user_option = input("Pilih opsi: ")

        if user_option == "1":
            CRD.create_console()
        elif user_option == "2":
            CRD.read_console()
            input("Tekan Enter untuk lanjut...")
        elif user_option == "3":
            CRD.analisis_console()
        elif user_option == "4":
            CRD.delete_console()
        elif user_option == "5":
            print("Terima kasih! Program selesai.")
            print("💡 Catatan: Semua data akan hilang karena disimpan di memory saja.")
            break
        else:
            print("Opsi tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()