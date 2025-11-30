import os
import CRD

sistem_operasi = os.name

def main():
    # Initialize DataFrame
    CRD.init_console()
    
    while True:
        # Clear screen
        if sistem_operasi == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        print("-" * 60)
        print("SISTEM MONITORING KESEHATAN TEKANAN DARAH & BMI".center(60))
        print("-" * 60)
        print("1. Buat Data Pasien Baru")
        print("2. Lihat Data Pasien") 
        print("3. Analisis Kesehatan")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("-" * 60)
        
        # Show current data count
        df = CRD.database.get_all_data()
        if len(df) > 0:
            print(f"📊 Data saat ini: {len(df)} pasien")
        else:
            print("📊 Data saat ini: Kosong")
        print("-" * 60)

        pilihan_user = input("Pilih opsi: ")

        if pilihan_user == "1":
            CRD.create_console()
        elif pilihan_user == "2":
            CRD.read_console()
            input("Tekan Enter untuk lanjut...")
        elif pilihan_user == "3":
            CRD.analisis_console()
        elif pilihan_user == "4":
            CRD.delete_console()
        elif pilihan_user == "5":
            print("\nTerima kasih! Program selesai.")
            print("💡 Catatan: Semua data akan hilang karena disimpan di memory saja.")
            break
        else:
            print("Opsi tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()