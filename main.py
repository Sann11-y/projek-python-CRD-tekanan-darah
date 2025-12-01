import os
import CRD
import dotenv
from google import genai

'''Deteksi Sistem Operasi
Mendeteksi sistem operasi untuk penentuan platform pengguna.
'''
sistem_operasi = os.name

dotenv.load_dotenv("GeminiApi.env")
try:
    client = genai.Client()
except Exception as e:
    print(f"ERROR: Gagal inisialisasi klien Gemini. Pastikan API key sudah diatur. Detail: {e}")
    client = None
'''
2. Fungsi Opsi Pembuatan Data Pasien
Menangani alur pembuatan data pasien tanpa memanggil Gemini.
'''
def opsi_buat_data_pasien():
    """Menangani alur pembuatan data tanpa memanggil Gemini."""
    
    CRD.create_console()
    
    input("\nTekan Enter untuk lanjut...") 

def main():
    CRD.init_console()
    while True:
        os.system("cls" if sistem_operasi == "nt" else "clear")
        
        print("-" * 60)
        print("SISTEM MONITORING KESEHATAN TEKANAN DARAH & BMI".center(60))
        print("-" * 60)
        print("1. Buat Data Pasien Baru")
        print("2. Lihat Data Pasien") 
        print("3. Analisis Kesehatan (Otomatis buat saran Gemini)") # Update Deskripsi
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("-" * 60)
        
        list_pasien = CRD.database.read()
        print(f"Data saat ini: {len(list_pasien)} pasien" if len(list_pasien) > 0 else "Data saat ini: Kosong")
        print("-" * 60)

        pilihan_user = input("Pilih opsi: ")

        if pilihan_user == "1":
            opsi_buat_data_pasien()
        elif pilihan_user == "2":
            CRD.read_console()
            input("Tekan Enter untuk lanjut...")
        elif pilihan_user == "3":
            CRD.analisis_console(client) 
            input("Tekan Enter untuk lanjut...")
        elif pilihan_user == "4":
            CRD.delete_console()
        elif pilihan_user == "5":
            print("\nTerima kasih! Program selesai.")
            print("Catatan: Semua data akan hilang karena disimpan di memory saja.")
            break
        else:
            print("Opsi tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()