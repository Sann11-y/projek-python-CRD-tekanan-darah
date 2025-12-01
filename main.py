import os
import CRD
import dotenv
from google import genai
from google.genai import types
import sys

# Variabel untuk sistem operasi
sistem_operasi = os.name

# 1. Inisialisasi Klien Gemini
dotenv.load_dotenv("GeminiApi.env")
try:
    client = genai.Client()
except Exception as e:
    print(f"ERROR: Gagal inisialisasi klien Gemini. Pastikan API key sudah diatur. Detail: {e}")
    client = None

# -----------------------------------------------------------------
# 2. Fungsi Pembantu untuk Rekomendasi Kesehatan
# -----------------------------------------------------------------

def rekomendasi_kesehatan (client: genai.Client , user_input: str) -> str:
    """
    Memberikan rekomendasi kesehatan atau saran berdasarkan input pengguna
    menggunakan model Gemini.
    """
    system_prompt = """
    Anda adalah asisten informasi kesehatan yang sangat ringkas dan berhati-hati.
    Tugas Anda adalah:
    1. Memberikan analisis kesehatan ringkas berdasarkan data pasien.
    2. Memberikan TEPAT 3 rekomendasi kesehatan dasar yang relevan dan tidak bertele-tele.
    3. Format respons harus rapi dan mudah dibaca (gunakan list/bullet point untuk saran).
    4. Selalu ingatkan untuk konsultasi ke profesional medis.
    5. JIKA INPUT PENGGUNA TIDAK TERKAIT DENGAN KESEHATAN, JAWAB DENGAN TEGAS: "Input anda di luar konteks kesehatan. Silahkan masukan pertanyaan yang berhubungan dengan kesehatan."
    """
    
    print(f'memproses input: "{user_input[:50]}..." dengan Gemini...')
    try:
        config = types.GenerateContentConfig(
            system_instruction=system_prompt
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents = user_input,
            config=config
        )
        return response.text

    except Exception as e:
        print(f'APi EROR: Gagal mendapat respon dari gemini. \n Detail: {e}')
        return 'Maaf terjadi maslaah teknis saat memproses permintaan anda.'

# -----------------------------------------------------------------
# 3. Fungsi Utama Saran Fleksibel Setelah Data Dibuat
# -----------------------------------------------------------------

def panggil_saran_pasien_terakhir():
    """
    Mengambil data pasien terakhir yang baru dimasukkan, memanggil Gemini
    untuk analisis dan saran, lalu mencetaknya.
    """
    
    if client is None:
        print("\nGemini API gagal diinisialisasi. Cek kunci API Anda.")
        input("Tekan Enter untuk lanjut...")
        return
        
    df = CRD.database.read()
    
    if df.empty:
        print("\nData Pasien Kosong. Tidak ada data untuk dianalisis.")
        return

    try:
        data_pasien = df.iloc[-1] 
        nama = data_pasien.get('nama', 'Pasien Tidak Diketahui') 
        sistolik = data_pasien.get('sistol', 'N/A')
        diastolik = data_pasien.get('diastol', 'N/A')
        bmi = data_pasien.get('bmi', 'N/A')
        
        berat = data_pasien.get('berat_badan', 'N/A')
        tinggi = data_pasien.get('tinggi_badan', 'N/A')
        
        data_string = (
            f"Nama: {nama}\n"
            f"Tekanan Darah: {sistolik}/{diastolik} mmHg\n"
            f"BMI: {bmi}\n"
            f"Berat: {berat} kg, Tinggi: {tinggi} m"
        )

        prompt_input = (
            f"Data Pasien Baru:\n"
            f"{data_string}\n"
            f"Berdasarkan data di atas, berikan analisis singkat dan TEPAT 3 saran kesehatan."
        )
        
        os.system("cls" if sistem_operasi == "nt" else "clear")
        print("-" * 60)
        print("SARAN FLEKSIBEL UNTUK DATA BARU OLEH GEMINI AI".center(60))
        print("-" * 60)
        print(f"Menganalisis data pasien '{nama}'...")

        response_text = rekomendasi_kesehatan(client, prompt_input)
        
        print("\n[Gemini AI]:")
        print(response_text)
        print("-" * 60)
        
        index_pasien_terakhir = len(df) - 1
        
        if CRD.database.update_saran(index_pasien_terakhir, response_text):
            print("Saran Gemini telah disimpan ke database!")
        else:
            print("Gagal menyimpan saran ke database.")
            
        
    except Exception as e:
        print(f"\nERROR saat memproses data/memanggil Gemini API: {e}")
    
    input("Tekan Enter untuk kembali ke menu utama...")

# -----------------------------------------------------------------
# 4. Fungsi Pembungkus (Wrapper) untuk Opsi 1
# -----------------------------------------------------------------

def opsi_buat_data_pasien():
    """Menangani seluruh alur pembuatan data, pertanyaan saran, dan pemanggilan Gemini."""
    
    CRD.create_console()
    
    if not CRD.database.read().empty:
        print("-" * 60)
        saran_choice = input("Data berhasil disimpan. Apakah Anda memerlukan saran kesehatan fleksibel dari Gemini AI? (y/n): ")
        if saran_choice.lower() == 'y':
            panggil_saran_pasien_terakhir()
        else:
            input("Tekan Enter untuk lanjut...")
    else:
        input("Tekan Enter untuk lanjut...")


def main():
    CRD.init_console()
    
    while True:
        os.system("cls" if sistem_operasi == "nt" else "clear")
        
        print("-" * 60)
        print("SISTEM MONITORING KESEHATAN TEKANAN DARAH & BMI".center(60))
        print("-" * 60)
        print("1. Buat Data Pasien Baru")
        print("2. Lihat Data Pasien") 
        print("3. Analisis Kesehatan")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("-" * 60)
        
        df = CRD.database.read()
        print(f"Data saat ini: {len(df)} pasien" if len(df) > 0 else "Data saat ini: Kosong")
        print("-" * 60)

        pilihan_user = input("Pilih opsi: ")

        if pilihan_user == "1":
            opsi_buat_data_pasien()
        elif pilihan_user == "2":
            CRD.read_console()
            input("Tekan Enter untuk lanjut...")
        elif pilihan_user == "3":
            CRD.analisis_console()
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