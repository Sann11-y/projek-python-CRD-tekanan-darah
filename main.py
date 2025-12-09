import os # buat operasi sistem seperti membersihkan layar terminal
import CRD 
import dotenv #pastiin library dotenv sudah terinstal
from google import genai #pastiin library google-genai sudah terinstal

sistemOperasi = os.name # 'nt' untuk Windows, 'posix' untuk Linux/Mac

dotenv.load_dotenv("GeminiApi.env") #memuat file GeminiApi.env yang berisi API key Gemini
try:
    client = genai.Client() #inisialisasi klien Gemini
except Exception as e:
    print(f"ERROR: Gagal inisialisasi klien Gemini. Pastikan API key sudah diatur. Detail: {e}")
    client = None # Tetep lanjutkan meskipun klien gagal diinisialisasi

def main():
    '''
    Fungsi Utama Program
    Fungsi ini adalah fungsi utama program yang akan dijalankan ketika program dijalankan.
    Fungsi ini akan memanggil fungsi-fungsi lainnya untuk menjalankan operasi program.
    '''
    CRD.inisialisasiData() 
    while True:
        os.system('cls' if sistemOperasi == 'nt' else 'clear') # kalau Windows pakai 'cls', kalau Linux/Mac pakai 'clear'
        
        print(
            "-" * 60 + "\n" +
            "VITALALIZE".center(60) + "\n" +
            "SISTEM MONITORING KESEHATAN TEKANAN DARAH & BMI".center(60) + "\n" +
            "-" * 60 + "\n" +
            "1. Buat Data Pasien Baru\n" +
            "2. Lihat Data Pasien\n" +
            "3. Analisis Kesehatan Pasien dengan Gemini AI\n" +
            "4. Hapus Data Pasien\n" +
            "5. Keluar\n" +
            "-" * 60
        )
        
        listPasien = CRD.read()
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
                    print("Tidak Bisa, Masukin angka 1 sampai 5.")
            except ValueError:
                print("Tidak Bisa, Harus Masukin Angka.")

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
            print(
                "\nTerima kasih! Program selesai.\n"+
                "Catatan: Semua data akan hilang karena disimpan di memory saja."
            )
            break


main()
