'''Database Module
Menyediakan fungsi CRUD untuk mengelola data pasien tekanan darah dan BMI menggunakan Pandas Data'''
import pandas as pd

'''Fungsi dari jantung_console.py yang diperlukan'''
from .jantung_console import klasifikasi_bmi, klasifikasi_tekanan

'''
Database Pandas DataFrame untuk menyimpan data pasien tekanan darah dan BMI.
Kolom:
- nama: Nama pasien
- berat_badan: Berat badan dalam kg
- tinggi_badan: Tinggi badan dalam cm
- umur: Umur pasien dalam tahun
- sistol: Tekanan darah sistol dalam mmHg
- diastol: Tekanan darah diastol dalam mmHg
- diagnosa: Hasil diagnosa tekanan darah
- bmi: Indeks Massa Tubuh
- kategori_bmi: Kategori BMI
- saran_gemini: Saran Gemini AI
'''
KOLOM = [
    'nama', 'berat_badan', 'tinggi_badan', 
    'umur', 'sistol', 'diastol', 'diagnosa', 'bmi', 'kategori_bmi', 'saran_gemini'
]

df_pasien = pd.DataFrame(columns=KOLOM)

'''
Inisialisasi DataFrame Pandas untuk menyimpan data pasien tekanan darah dan BMI.
'''
def init_console():
    """Inisialisasi database pandas DataFrame"""
    global df_pasien
    df_pasien = pd.DataFrame(columns=KOLOM)
    # print("Database Pandas DataFrame siap!") # Hilangkan print untuk kerapihan

'''
Menambahkan data pasien ke dalam DataFrame Pandas.
'''
def create(nama, bb, tb, umur, sistol, diastol):
    global df_pasien
    
    try:
        diagnosa = klasifikasi_tekanan(umur, sistol, diastol)
        # Konversi cm ke meter saat perhitungan BMI
        bmi = bb / ((tb/100) ** 2) 
        kategori_bmi = klasifikasi_bmi(bmi)
        
        df_pasien.loc[len(df_pasien)] = {
            'nama': nama,
            'berat_badan': bb,
            'tinggi_badan': tb,
            'umur': umur,
            'sistol': sistol,
            'diastol': diastol,
            'diagnosa': diagnosa,
            'bmi': round(bmi, 2),
            'kategori_bmi': kategori_bmi,
            'saran_gemini': "" # Kosongkan saran saat create
        }
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

'''
Membaca data pasien dari DataFrame Pandas.
Jika indeks diberikan, kembalikan data pasien sebagai dict.
Jika tidak, kembalikan DataFrame.
'''
def read(indeks=None):
    if indeks is not None:
        if 0 <= indeks < len(df_pasien):
            return df_pasien.iloc[indeks].to_dict()
        return None
    return df_pasien

'''
Menghapus data pasien dari DataFrame Pandas berdasarkan indeks.
'''
def delete(indeks):
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            # Drop baris dan reset index
            df_pasien = df_pasien.drop(indeks).reset_index(drop=True)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

'''
Mengupdate kolom 'saran_gemini' untuk pasien tertentu berdasarkan indeks.
'''
def update_saran(indeks, saran_text):
    """Update kolom saran_gemini untuk pasien tertentu berdasarkan indeks."""
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            # Menggunakan .loc untuk memperbarui nilai di kolom 'saran_gemini'
            df_pasien.loc[indeks, 'saran_gemini'] = saran_text
            return True
        return False
    except Exception as e:
        print(f"Error saat update saran: {e}")
        return False