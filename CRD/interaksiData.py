from google import genai
from google.genai import types #memberi instruksi peran ai dalam program sehingga tidak keluar dari konetks program yang berjalan

from . import database 

'''
Klassifikasi BMI dan Tekanan Darah
Fungsi-fungsi untuk mengklasifikasikan BMI dan tekanan darah berdasarkan standar medis
'''
def klasifikasiBmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi <= 24.9:
        return "Normal" 
    elif 25 <= bmi <= 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

'''Fungsi Klasifikasi Tekanan Darah Berdasarkan Umur'''
def klasifikasiTekanan(umur, sistol, diastol):
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
        if sistol > 120 or diastol > 80: 
            return "Hipertensi"
        elif sistol < 90 or diastol < 60: 
            return "Hipotensi"
        else:
            return "Normal" 
    else: 
        if sistol > 150 or diastol > 90: 
            return "Hipertensi"
        elif sistol < 90 or diastol < 60: 
            return "Hipotensi"
        else:
            return "Normal"

'''
Fungsi Rekomendasi Kesehatan dengan Gemini AI
Menghasilkan rekomendasi kesehatan berdasarkan data pasien menggunakan model Gemini.
'''
def rekomendasiKesehatan (client: genai.Client , userInput: str) -> str:
    """
    Memberikan rekomendasi kesehatan atau saran berdasarkan input pengguna
    menggunakan model Gemini. (Dipindahkan dari main.py)
    """
    # kegunaan systemprompt untuk memberi tau ai apa perannya dalam program ini (pemberi analisis dan saran kesehatan )
    systemPrompt = """
    Anda adalah asisten informasi kesehatan yang sangat ringkas dan berhati-hati.
    Tugas Anda adalah:
    1. Memberikan analisis kesehatan ringkas berdasarkan data pasien.
    2. Memberikan TEPAT 3 rekomendasi kesehatan dasar yang relevan dan tidak bertele-tele.
    3. Format respons harus rapi dan mudah dibaca (gunakan list/bullet point untuk saran).
    4. Selalu ingatkan untuk konsultasi ke profesional medis.
    5. JIKA INPUT PENGGUNA TIDAK TERKAIT DENGAN KESEHATAN, JAWAB DENGAS TEGAS: "Input anda di luar konteks kesehatan. Silahkan masukan pertanyaan yang berhubungan dengan kesehatan."
    """
    
    print(f'Memproses data dengan Gemini...')
    try:
        config = types.GenerateContentConfig(
            system_instruction=systemPrompt
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents = userInput,
            config=config
        )
        return response.text

    except Exception as e:
        print(f'APi EROR: Gagal mendapat respon dari gemini. \n Detail: {e}')
        return 'Maaf terjadi masalah teknis saat memproses permintaan Anda.'

'''
Buat Data Pasien (CREATE)
Menangani alur pembuatan data pasien melalui input pengguna.
'''
def buatData():
    print(
        "\n" + "="*50 + "\n" +
        "TAMBAH DATA PASIEN".center(50) + "\n" +
        "="*50
    )    
    nama = input("Nama\t\t\t: ")
    
    while True:
        try:
            bb = float(input("Berat Badan (kg)\t: "))
            tb = float(input("Tinggi Badan (cm)\t: "))
            if bb <= 0 or tb <= 0:
                print("Berat badan dan tinggi badan harus positif!")
                continue
            break
        except ValueError:
            print("Input harus angka!")

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
            print("Input harus angka!")

    while True:
        try:
            sistol = int(input("Tekanan Darah (Systolic): "))
            diastol = int(input("Tekanan Darah(Diastolic): "))

            if sistol <= 0 or diastol <= 0 or sistol < 50 or diastol < 30 or sistol > 300 or diastol > 200:
                print("Nilai tekanan darah tidak masuk akal!")
                continue
            elif sistol <= diastol: 
                print("Tekanan sistolik harus lebih besar dari diastolik!")
                continue
            else:
                break
        except ValueError:
            print("Input harus angka!")
    
    if database.create(nama, bb, tb, umur, sistol, diastol):
        print(
            "\nData berhasil ditambahkan!\n"+
            f"Total data sekarang: {len(database.read())} pasien"
        )
    else:
        print("\nGagal menambah data!")

'''
Tampilkan Semua Data Pasien (READ)
'''
def lihatData():
    listPasien = database.read()
    
    if len(listPasien) == 0:
        print("\nTidak ada data pasien!")
        return

    print(
        "\n" + "="*115 + "\n" +
        "DAFTAR PASIEN".center(115) + "\n" +
        "="*115 + "\n" +
        "No  | Nama                 | BB(kg) | TB(cm) | BMI   | Umur | Tekanan      | Diagnosa     | Kategori BMI | Saran   " + "\n" +
        "-"*115 
    )
    
    for indeks, baris in enumerate(listPasien):
        nama = baris['nama'][:20]
        bb = f"{baris['beratBadan']:.1f}"
        tb = f"{baris['tinggiBadan']:.1f}"
        bmi = f"{baris['bmi']:.1f}"
        umur = str(int(baris['umur']))
        tekananDarah = f"{int(baris['sistol'])}/{int(baris['diastol'])} mmHg"
        diagnosa = baris['diagnosa'][:12]
        kategoriBmi = baris['kategoriBmi'][:12]
        
        if baris['saranGemini']:
            saranAi = "Ada"
        else:
            saranAi = "Kosong"
        
        print(f"{indeks+1:3} | {nama:<20} | {bb:<6} | {tb:<6} | {bmi:<5} | {umur:<4} | {tekananDarah:<12} | {diagnosa:<12} | {kategoriBmi:<12} | {saranAi:<10}")

    print(
        "="*115 + "\n" +
        f"Total: {len(listPasien)} pasien"
    )

'''
Analisis Kesehatan & Integrasi Panggilan Gemini (ANALYZE)
'''
def analisisData(geminiClient):
    listPasien = database.read()
    if len(listPasien) == 0:
        print("\nTidak ada data pasien!")
        return
        
    lihatData()
    
    while True:
        try:
            nomorData = int(input("\nPilih nomor data untuk dianalisis: ")) - 1 # memilih data yang sudah ada, data -1 karena indeks data dimulai dari 0
            dataPasien = database.read(nomorData)
            
            if dataPasien is not None: #memeriksa apakah indeks valid atau data ada, dan apabila valid maka program lanjut
                break
            else: # akan menampilkan nomor tidak valid ketika indeks tidak valid atau data tidak ada
                print("Nomor tidak valid!")
        except ValueError:
            print("Input harus angka!")
    
    saranGemini = dataPasien.get('saranGemini') #ngambil data yang baru aja dipilih (apabila data sudah pernah dianalisis gemini, maka akan menampilkan saran gemini.) 
    # jika belum maka akan kosong
    saranBaruDibuat = False # false apabila saran sudah ada, dan menajadi true jika program harus bikin saran baru yang nanti bakal disimpan di database

    # JIKA SARAN BELUM ADA, MAKA PANGGIL GEMINI UNTUK MEMBUAT SARAN
    if not saranGemini and geminiClient is not None:
        
        nama = dataPasien['nama']
        sistolik = dataPasien['sistol']
        diastolik = dataPasien['diastol']
        bmi = dataPasien['bmi']
        berat = dataPasien['beratBadan']
        tinggi = dataPasien['tinggiBadan']
        
        detailPasien = (
            f"Nama: {nama}\n"
            f"Tekanan Darah: {sistolik}/{diastolik} mmHg\n"
            f"BMI: {bmi:.1f}\n"
            f"Berat: {berat} kg, Tinggi: {tinggi} cm"
        )

        promptInput = (
            f"Data Pasien:\n"
            f"{detailPasien}\n"
            f"Berdasarkan data di atas, berikan analisis singkat dan TEPAT 3 saran kesehatan."
        )
        print(
            "\n"+"="*60+"\n"+
            "MENGANALISIS DATA PASIEN DENGAN GEMINI AI".center(60) + "\n" +
            "="*60
        )
        responseText = rekomendasiKesehatan(geminiClient, promptInput)
        saranGemini = responseText
        saranBaruDibuat = True

    elif not saranGemini and geminiClient is None:
        print("\nGemini API gagal diinisialisasi. Tidak bisa membuat saran fleksibel.")
    
    print(
        "\n" + "="*60 + "\n" +
        "HASIL ANALISIS KESEHATAN".center(60) + "\n" +
        "="*60 + "\n" +
        f"Nama Pasien\t: {dataPasien['nama']}\n" +
        f"Umur\t\t: {int(dataPasien['umur'])} tahun\n" +
        f"Berat/Tinggi\t: {dataPasien['beratBadan']} kg / {dataPasien['tinggiBadan']} cm\n" +
        f"BMI\t\t: {dataPasien['bmi']:.1f} ({dataPasien['kategoriBmi']})" + "\n" +
        f"Tekanan Darah\t: {int(dataPasien['sistol'])}/{int(dataPasien['diastol'])} mmHg\n" +
        f"Diagnosa\t: {dataPasien['diagnosa']}"
    )
    
    print(
        "="*60 + "\n" +
        "SARAN FLEKSIBEL DARI GEMINI AI:".center(60) + "\n" +
        "="*60
    )
    if saranGemini:
        print(saranGemini)
    else:
        print("Saran Gemini belum tersedia.")
    if saranBaruDibuat and geminiClient is not None:
        print("\n"+"--- PROSES PENYIMPANAN DATA ---".center(60))
        if database.updateSaran(nomorData, saranGemini):
            print("✅ Saran Gemini baru telah disimpan otomatis ke database.")
        else:
            print("❌ Gagal menyimpan saran baru ke database.")
        print("-"*60)
'''
Hapus Data Pasien (DELETE)
'''
def hapusData():
    listPasien = database.read()
    if len(listPasien) == 0:
        print("\nTidak ada data pasien!")
        return
        
    lihatData()
    
    while True:
        try:
            nomorData = int(input("\nPilih nomor data yang akan dihapus: ")) - 1
            dataPasien = database.read(nomorData)
            if dataPasien is not None:
                break
            else:
                print("Nomor tidak valid!")
        except ValueError:
            print("Input harus angka!")
    
    print(
        "="*60+"\n"+
        "KONFIRMASI PENGHAPUSAN DATA".center(60)+"\n"+
        "="*60+"\n"+
        "Data yang akan dihapus\n"+
        f"Nama\t\t\t: {dataPasien['nama']}\n"+
        f"Umur\t\t\t: {int(dataPasien['umur'])} tahun\n"+
        f"Berat/Tinggi\t\t: {dataPasien['beratBadan']} kg / {dataPasien['tinggiBadan']} cm\n"+
        f"Tekanan Darah\t\t: {int(dataPasien['sistol'])}/{int(dataPasien['diastol'])} mmHg"
        )
    
    konfirmasi = input("\nApakah Anda yakin? (y/n): ").lower()
    if konfirmasi == 'y':
        if database.delete(nomorData):
            print(
                "Data berhasil dihapus! \n"+
                f"Sisa data sekarang: {len(database.read())} pasien"
                )
        else:
            print("Gagal menghapus data!")
    else:
        print("Penghapusan dibatalkan.")