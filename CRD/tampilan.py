from . import database
from .util import saran_kesehatan

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
            elif sistol < 50 or diastol < 30 or sistol > 300 or diastol > 200:
                print("Error: Tekanan darah terlalu ekstrem!")
                continue
            elif sistol - diastol <= 20:
                print("Error: Tekanan Nadi sangat sempit!")
                continue 
            elif sistol - diastol >= 60:
                print("Error: Tekanan Nadi sangat lebar!")
                continue
            else:
                break
        except ValueError:
            print("Error: Input harus angka!")
    
    if database.create(nama, bb, tb, umur, sistol, diastol):
        print("\nData berhasil ditambahkan!")
        print(f"Total data sekarang: {len(database.read())} pasien")
    else:
        print("\nGagal menambah data!")
    
    input("\nTekan Enter untuk lanjut...")

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

def analisis_console():
    """Analyze patient health console"""
    df = database.read()
    
    if len(df) == 0:
        print("Tidak ada data pasien!")
        input("\nTekan Enter untuk lanjut...")
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
    
    print("\n" + "="*60)
    print("HASIL ANALISIS KESEHATAN")
    print("="*60)
    print(f"Nama Pasien\t: {data_pasien['nama']}")
    print(f"Umur\t\t: {int(data_pasien['umur'])} tahun") 
    print(f"Berat/Tinggi\t: {data_pasien['berat_badan']} kg / {data_pasien['tinggi_badan']} cm")
    print(f"BMI\t\t: {data_pasien['bmi']:.1f}")
    print(f"Tekanan Darah\t: {int(data_pasien['sistol'])}/{int(data_pasien['diastol'])} mmHg")
    print(f"Diagnosa\t: {data_pasien['diagnosa']}")
    
    saran_tekanan, saran_bmi = saran_kesehatan(data_pasien['diagnosa'], data_pasien['bmi'])
    
    print(f"\nSARAN KESEHATAN (Standar):")
    print(f"• Tekanan Darah: {saran_tekanan}")
    print(f"• BMI: {saran_bmi}")
    
    # Integrasi Saran Gemini
    saran_gemini = data_pasien.get('saran_gemini') 

    if saran_gemini:
        print("\nSARAN FLEKSIBEL DARI GEMINI AI:")
        print("---------------------------------------")
        print(saran_gemini) 
    else:
        print("\nSARAN FLEKSIBEL DARI GEMINI AI:")
        print("---------------------------------------")
        print("Saran Gemini belum dibuat untuk pasien ini.")
        print("Anda dapat membuatnya melalui opsi 'Buat Data Pasien Baru'.")
    
    print("="*60)
    
    input("\nTekan Enter untuk lanjut...")

def delete_console():
    """Delete patient record console"""
    df = database.read()
    
    if len(df) == 0:
        print("Tidak ada data pasien!")
        input("\nTekan Enter untuk lanjut...")
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
    
    input("\nTekan Enter untuk lanjut...")