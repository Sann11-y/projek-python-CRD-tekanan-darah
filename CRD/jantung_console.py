import os
from google import genai
from google.genai import types
from . import database # Tetap impor database

'''
Klassifikasi BMI dan Tekanan Darah
Fungsi-fungsi untuk mengklasifikasikan BMI dan tekanan darah berdasarkan standar medis'''
def klasifikasi_bmi(bmi):
    """Classify BMI into category"""
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi <= 24.9:
        return "Normal" 
    elif 25 <= bmi <= 29.9:
        return "Gemuk"
    else:
        return "Obesitas"
    
def klasifikasi_tekanan(umur, sistol, diastol):
    """Classify blood pressure based on age"""
    if 6 <= umur <= 12:
        if sistol < 96 or diastol < 55: 
            return "Hipotensi"
        elif sistol > 131 or diastol > 62: 
            return "Hipertensi"
        else: 
            return "Normal" 
    elif 13 <= umur <= 18:
        if sistol < 112 or diastol < 62: 
            return "Hipotensi"
        elif sistol > 128 or diastol > 80: 
            return "Hipertensi"
        else: 
            return "Normal"
    elif 19 <= umur <= 65:
        if sistol < 90 or diastol < 60: 
            return "Hipotensi"
        elif sistol > 120 or diastol > 80: 
            return "Hipertensi"
        else: 
            return "Normal"
    else: # > 65
        if sistol < 90 or diastol < 60: 
            return "Hipotensi"
        elif sistol > 150 or diastol > 90: 
            return "Hipertensi"
        else: 
            return "Normal"

'''
Fungsi Rekomendasi Kesehatan dengan Gemini AI
Menghasilkan rekomendasi kesehatan berdasarkan data pasien menggunakan model Gemini.
'''
def rekomendasi_kesehatan (client: genai.Client , user_input: str) -> str:
    """
    Memberikan rekomendasi kesehatan atau saran berdasarkan input pengguna
    menggunakan model Gemini. (Dipindahkan dari main.py)
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
    
    print(f'Memproses data dengan Gemini...')
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
        return 'Maaf terjadi masalah teknis saat memproses permintaan Anda.'

'''
Fungsi Konsol untuk CRAD Data Pasien
Fungsi-fungsi untuk membuat, membaca, menganalisis, dan menghapus data pasien.
'''
def create_console():
    """Create new patient console"""
    print("\n" + "="*50)
    print("TAMBAH DATA PASIEN")
    print("="*50)
    
    nama = input("Nama\t\t: ")
    
    while True:
        try:
            bb = float(input("Berat Badan (kg)\t: "))
            tb = float(input("Tinggi Badan (cm)\t: "))
            if bb <= 0 or tb <= 0:
                print("Error: Semua nilai harus positif!")
                continue
            break
        except ValueError:
            print("Error: Input harus angka!")

    while True:
        try:
            umur = int(input("Umur\t\t\t: "))
            if umur <= 0:
                print("Error: Umur harus positif!")
                continue
            elif umur < 6:
                print("Error: Umur minimal 6 tahun!")
                continue
            else:
                break
        except ValueError: 
            print("Error: Input harus angka!")

    while True:
        try:
            sistol = int(input("Tekanan Darah (Systolic)\t: "))
            diastol = int(input("Tekanan Darah (Diastolic)\t: "))
            if sistol <= 0 or diastol <= 0:
                print("Error: Semua nilai harus positif!")
                continue
            elif sistol < diastol:
                print("Error: Systolic harus lebih besar dari Diastolic!")
                continue
            elif sistol == diastol:
                print("Error: Systolic dan Diastolic tidak boleh sama!")
                continue
            # Batasan yang lebih longgar, menghilangkan batasan pulse pressure
            elif sistol < 50 or diastol < 30 or sistol > 300 or diastol > 200:
                print("Error: Tekanan darah terlalu ekstrem!")
                continue
            else:
                break
        except ValueError:
            print("Error: Input harus angka!")
    
    if database.create(nama, bb, tb, umur, sistol, diastol):
        print("\nData berhasil ditambahkan!")
        print(f"Total data sekarang: {len(database.read())} pasien")
        # Tidak ada pemanggilan Gemini di sini
    else:
        print("\nGagal menambah data!")

def read_console():
    """Display all patients console"""
    df = database.read()
    
    if len(df) == 0:
        print("\nTidak ada data pasien!")
        return

    # Ubah lebar total menjadi 115
    print("\n" + "="*115) 
    print("DAFTAR PASIEN")
    print("="*115)
    # Tambah kolom baru 'Saran AI'
    print(f"{'No':3} | {'Nama':20} | {'BB(kg)':6} | {'TB(cm)':6} | {'BMI':5} | {'Umur':4} | {'Tekanan':12} | {'Diagnosa':12} | {'Kategori BMI':12} | {'Saran AI':10}")
    print("-"*115) 
    
    for indeks, baris in df.iterrows():
        nama = str(baris['nama'])[:20]
        bb = f"{baris['berat_badan']:.1f}"
        tb = f"{baris['tinggi_badan']:.1f}"
        bmi = f"{baris['bmi']:.1f}"
        umur = str(int(baris['umur']))
        tekanan_darah = f"{int(baris['sistol'])}/{int(baris['diastol'])} mmHg"
        diagnosa = str(baris['diagnosa'])[:12]
        kategori_bmi = str(baris['kategori_bmi'])[:12]
        
        # Logika Kolom Saran AI baru
        saran_ai = "Ada" if baris['saran_gemini'] else "Kosong" 
        
        # Tambahkan kolom saran_ai
        print(f"{indeks+1:3} | {nama:20} | {bb:6} | {tb:6} | {bmi:5} | {umur:4} | {tekanan_darah:12} | {diagnosa:12} | {kategori_bmi:12} | {saran_ai:10}")

    print("="*115) 
    print(f"Total: {len(df)} pasien")


def analisis_console(gemini_client):
    """Analyze patient health console & integrate Gemini call"""
    df = database.read()
    sistem_operasi = os.name 

    if len(df) == 0:
        print("\nTidak ada data pasien!")
        return
        
    read_console()
    
    while True:
        try:
            nomor_data = int(input("\nPilih nomor data untuk dianalisis: ")) - 1
            data_pasien = database.read(nomor_data)
            
            if data_pasien is not None:
                break
            else:
                print("Nomor tidak valid!")
        except ValueError:
            print("Input harus angka!")
    
    # Ambil saran yang sudah tersimpan
    saran_gemini = data_pasien.get('saran_gemini') 
    saran_baru_dibuat = False # Flag untuk melacak apakah saran baru dihasilkan

    # JIKA SARAN BELUM ADA, PANGGIL GEMINI
    if not saran_gemini and gemini_client is not None:
        
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
            f"Berat: {berat} kg, Tinggi: {tinggi} cm"
        )

        prompt_input = (
            f"Data Pasien:\n"
            f"{data_string}\n"
            f"Berdasarkan data di atas, berikan analisis singkat dan TEPAT 3 saran kesehatan."
        )
        
        # Tampilkan proses loading di layar
        print("\n" + "-" * 60)
        print("MENGANALISIS DATA PASIEN DENGAN GEMINI AI".center(60))
        print("-" * 60)

        response_text = rekomendasi_kesehatan(gemini_client, prompt_input)
        saran_gemini = response_text # Gunakan saran baru
        saran_baru_dibuat = True # Set flag bahwa saran baru telah dibuat

        # HAPUS: Logika penyimpanan dan input pengguna di sini

    elif not saran_gemini and gemini_client is None:
        print("\nGemini API gagal diinisialisasi. Tidak bisa membuat saran fleksibel.")

    # TAMPILKAN HASIL ANALISIS
    
    print("\n" + "="*60)
    print("HASIL ANALISIS KESEHATAN")
    print("="*60)
    print(f"Nama Pasien\t: {data_pasien['nama']}")
    print(f"Umur\t\t: {int(data_pasien['umur'])} tahun") 
    print(f"Berat/Tinggi\t: {data_pasien['berat_badan']} kg / {data_pasien['tinggi_badan']} cm")
    print(f"BMI\t\t: {data_pasien['bmi']:.1f}")
    print(f"Tekanan Darah\t: {int(data_pasien['sistol'])}/{int(data_pasien['diastol'])} mmHg")
    print(f"Diagnosa\t: {data_pasien['diagnosa']}")
    
    
    # Tampilkan saran yang sudah ada (baik dari load atau baru dibuat)
    print("\nSARAN FLEKSIBEL DARI GEMINI AI:")
    print("---------------------------------------")
    if saran_gemini:
        print(saran_gemini) 
    else:
        print("Saran Gemini belum tersedia.")
        
    # LOGIKA PENYIMPANAN DAN NOTIFIKASI BARU (SETELAH TAMPILAN SARAN)
    if saran_baru_dibuat and gemini_client is not None:
        print("\n--- PROSES PENYIMPANAN DATA ---")
        if database.update_saran(nomor_data, saran_gemini):
            print("✅ Saran Gemini baru telah disimpan otomatis ke database.")
        else:
            print("❌ Gagal menyimpan saran baru ke database.")
        print("-------------------------------")
    
    print("="*60)
def delete_console():
    """Delete patient record console"""
    df = database.read()
    
    if len(df) == 0:
        print("\nTidak ada data pasien!")
        return
        
    read_console()
    
    while True:
        try:
            nomor_data = int(input("\nPilih nomor data yang akan dihapus: ")) - 1
            data_pasien = database.read(nomor_data)
            
            if data_pasien is not None:
                break
            else:
                print("Nomor tidak valid!")
        except ValueError:
            print("Input harus angka!")
    
    nama = data_pasien['nama']
    
    print(f"\nKONFIRMASI PENGHAPUSAN")
    print(f"Data yang akan dihapus: {nama}")
    print(f"Umur: {int(data_pasien['umur'])} tahun")
    print(f"Tekanan Darah: {int(data_pasien['sistol'])}/{int(data_pasien['diastol'])} mmHg")
    
    konfirmasi = input("\nApakah Anda yakin? (y/n): ").lower()
    
    if konfirmasi == 'y':
        if database.delete(nomor_data):
            print("Data berhasil dihapus!")
            print(f"Sisa data: {len(database.read())} pasien")
        else:
            print("Gagal menghapus data!")
    else:
        print("Penghapusan dibatalkan.")
    
    # Tidak perlu input di sini karena akan dihandle oleh main()