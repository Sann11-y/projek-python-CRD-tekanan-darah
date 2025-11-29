from . import operasi, database
from .util import saran_kesehatan
import pandas as pd

def create_console():
    """Create new patient"""
    print("\n" + "="*50)
    print("TAMBAH DATA PASIEN")
    print("="*50)
    
    nama = input("Nama\t\t: ")
    
    while True:
        try:
            bb = float(input("Berat Badan (kg)\t: "))
            tb = float(input("Tinggi Badan (cm)\t: "))
            if bb <= 0 or tb <= 0:
                print("❌ Error: Semua nilai harus positif!")
                continue
            break
        except ValueError:
            print("❌ Error: Input harus angka!")

    while True:
        try:
            umur = int(input("Umur\t\t\t: "))
            if umur <= 0:
                print("❌ Error: Umur harus positif!")
                continue
            elif umur < 6:
                print("❌ Error: Umur minimal 6 tahun!")
                continue
            else:
                break
        except:
            print("❌ Error: Input harus angka!")

    while True:
        try:
            systolic = int(input("Tekanan Darah (Systolic)\t: "))
            diastolic = int(input("Tekanan Darah (Diastolic)\t: "))
            if systolic <= 0 or diastolic <= 0:
                print("❌ Error: Semua nilai harus positif!")
                continue
            elif systolic < diastolic:
                print("❌ Error: Systolic harus lebih besar dari Diastolic!")
                continue
            elif systolic == diastolic:
                print("❌ Error: Systolic dan Diastolic tidak boleh sama!")
                continue
            elif systolic < 50 or diastolic < 30 or systolic > 300 or diastolic > 200:
                print("❌ Error: Tekanan darah terlalu ekstrem dan di luar rentang fisiologis normal.")
                continue
            elif systolic - diastolic <= 20:
                print("❌ Error: Tekanan Nadi (Pulse Pressure) sangat sempit. Input tidak biasa.")
                continue 
            elif systolic - diastolic >= 60:
                print("❌ Error: Tekanan Nadi (Pulse Pressure) sangat lebar. Input tidak biasa.")
                continue
            else:
                break
        except ValueError:
            print("❌ Error: Input harus angka!")
    
    if operasi.create(nama, bb, tb, umur, systolic, diastolic):
        print("\n✅ Data berhasil ditambahkan!")
        df = database.get_all_data()
        print(f"📊 Total data sekarang: {len(df)} pasien")
    else:
        print("\n❌ Gagal menambah data!")
    
    input("\nTekan Enter untuk lanjut...")

def read_console():
    """Display all patients from DataFrame"""
    df = database.get_all_data()
    
    if len(df) == 0:
        print("\n📭 Tidak ada data pasien!")
        return

    print("\n" + "="*100)
    print("DAFTAR PASIEN")
    print("="*100)
    print(f"{'No':3} | {'Nama':20} | {'BB(kg)':6} | {'TB(cm)':6} | {'BMI':5} | {'Umur':4} | {'Tekanan':12} | {'Diagnosa':12} | {'Kategori BMI':12}")
    print("-"*100)
    
    # Loop through DataFrame rows
    for index, row in df.iterrows():
        nama = str(row['nama'])[:20]  # Limit to 20 chars
        bb = f"{row['berat_badan']:.1f}"
        tb = f"{row['tinggi_badan']:.1f}"
        bmi = f"{row['bmi']:.1f}"
        umur = str(int(row['umur']))
        tekanan_darah = f"{int(row['systolic'])}/{int(row['diastolic'])} mmHg"
        diagnosa = str(row['diagnosa'])[:12]  # Limit to 12 chars
        kategori_bmi = str(row['kategori_bmi'])[:12]  # Limit to 12 chars
        
        print(f"{index+1:3} | {nama:20} | {bb:6} | {tb:6} | {bmi:5} | {umur:4} | {tekanan_darah:12} | {diagnosa:12} | {kategori_bmi:12}")

    print("="*100)
    print(f"📈 Total: {len(df)} pasien")

def analisis_console():
    """Analyze patient health"""
    df = database.get_all_data()
    
    if len(df) == 0:
        print("📭 Tidak ada data pasien!")
        input("\nTekan Enter untuk lanjut...")
        return
        
    read_console()
    
    while True:
        try:
            no_data = int(input("\n🔍 Pilih nomor data untuk dianalisis: ")) - 1
            data_pasien = operasi.read(no_data)
            
            if data_pasien is not None:
                break
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus angka!")
    
    # Data langsung dari dictionary
    print("\n" + "="*60)
    print("HASIL ANALISIS KESEHATAN")
    print("="*60)
    print(f"👤 Nama Pasien\t: {data_pasien['nama']}")
    print(f"🎂 Umur\t\t: {int(data_pasien['umur'])} tahun") 
    print(f"⚖️  Berat/Tinggi\t: {data_pasien['berat_badan']} kg / {data_pasien['tinggi_badan']} cm")
    print(f"📊 BMI\t\t: {data_pasien['bmi']:.1f}")
    print(f"💓 Tekanan Darah\t: {int(data_pasien['systolic'])}/{int(data_pasien['diastolic'])} mmHg")
    print(f"🏥 Diagnosa\t: {data_pasien['diagnosa']}")
    
    saran_tekanan, saran_bmi = saran_kesehatan(data_pasien['diagnosa'], data_pasien['bmi'])
    
    print(f"\n💡 SARAN KESEHATAN:")
    print(f"• Tekanan Darah: {saran_tekanan}")
    print(f"• BMI: {saran_bmi}")
    print("="*60)
    
    input("\nTekan Enter untuk lanjut...")

def delete_console():
    """Delete patient record"""
    df = database.get_all_data()
    
    if len(df) == 0:
        print("📭 Tidak ada data pasien!")
        input("\nTekan Enter untuk lanjut...")
        return
        
    read_console()
    
    while True:
        try:
            no_data = int(input("\n🗑️  Pilih nomor data yang akan dihapus: ")) - 1
            data_pasien = operasi.read(no_data)
            
            if data_pasien is not None:
                break
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus angka!")
    
    nama = data_pasien['nama']
    
    print(f"\n⚠️  KONFIRMASI PENGHAPUSAN")
    print(f"Data yang akan dihapus: {nama}")
    print(f"Umur: {int(data_pasien['umur'])} tahun")
    print(f"Tekanan Darah: {int(data_pasien['systolic'])}/{int(data_pasien['diastolic'])} mmHg")
    
    confirm = input("\nApakah Anda yakin? (y/n): ").lower()
    
    if confirm == 'y':
        if operasi.delete(no_data):
            print("✅ Data berhasil dihapus!")
            df = database.get_all_data()
            print(f"📊 Sisa data: {len(df)} pasien")
        else:
            print("❌ Gagal menghapus data!")
    else:
        print("❌ Penghapusan dibatalkan.")
    
    input("\nTekan Enter untuk lanjut...")