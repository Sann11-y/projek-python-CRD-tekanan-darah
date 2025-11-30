import pandas as pd
from .util import klasifikasi_bmi, klasifikasi_tekanan

# Inisialisasi kolom
KOLOM = [
    'nama', 'berat_badan', 'tinggi_badan', 
    'umur', 'sistol', 'diastol', 'diagnosa', 'bmi', 'kategori_bmi', 'saran_gemini'
]

df_pasien = pd.DataFrame(columns=KOLOM)

def init_console():
    """Initialize DataFrame"""
    global df_pasien
    df_pasien = pd.DataFrame(columns=KOLOM)
    print("Database Pandas DataFrame siap!")

def create(nama, bb, tb, umur, sistol, diastol):
    """Create new patient record"""
    global df_pasien
    try:
        diagnosa = klasifikasi_tekanan(umur, sistol, diastol)
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
            'saran_gemini': ""
        }
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def read(indeks=None):
    """Read patient data - returns dict if index provided, DataFrame otherwise"""
    if indeks is not None:
        if 0 <= indeks < len(df_pasien):
            return df_pasien.iloc[indeks].to_dict()
        return None
    return df_pasien

def delete(indeks):
    """Delete patient data"""
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