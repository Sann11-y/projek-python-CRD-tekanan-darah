import os
import CRD
import dotenv
from google import genai

'''Deteksi Sistem Operasi
Mendeteksi sistem operasi untuk penentuan platform pengguna.
'''
sistemOperasi = os.name

dotenv.load_dotenv("GeminiApi.env")
try:
    client = genai.Client()
except Exception as e:
    print(f"ERROR: Gagal inisialisasi klien Gemini. Pastikan API key sudah diatur. Detail: {e}")
    client = None

def main():
    CRD.inisialisasiData() 
    while True:
        os.system('cls' if sistemOperasi == 'nt' else 'clear')
        
        print("-" * 60)
        print("SISTEM MONITORING KESEHATAN TEKANAN DARAH & BMI".center(60))
        print("-" * 60)
        print("1. Buat Data Pasien Baru")
        print("2. Lihat Data Pasien") 
        print("3. Analisis Kesehatan Pasien dengan Gemini AI") 
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("-" * 60)
        
        listPasien = CRD.database.read()
        if len(listPasien) > 0:
            print(f"Data saat ini: {len(listPasien)} pasien")
        else:
            print("Data saat ini: Kosong")
        print("-" * 60)

        while True:
            try:
                masukinOpsi = int(input("Pilih opsi: "))
                if 1 <= masukinOpsi <= 5:
                    break 
                else:
                    print("Gabisa, Masukin angka 1 sampai 5.")
            except ValueError:
                print("Gabisa, Harus Masukin Angka.")

        if masukinOpsi == 1:
            CRD.buatData() 
            input("\nTeken Enter untuk kembali ke menu...")
        elif masukinOpsi == 2:
            CRD.lihatData() 
            input("\nTeken Enter untuk kembali ke menu...")
        elif masukinOpsi == 3:
            CRD.analisisData(client)
            input("\nTeken Enter untuk kembali ke menu...")
        elif masukinOpsi == 4:
            CRD.hapusData() 
            input("\nTeken Enter untuk kembali ke menu...")
        elif masukinOpsi == 5:
            print("\nTerima kasih! Program selesai.")
            print("Catatan: Semua data akan hilang karena disimpan di memory saja.")
            break

if __name__ == "__main__":
    main()