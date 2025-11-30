# data_manager.py - Gabungan database.py + operasi.py
import pandas as pd
from .util import klasifikasi_bmi, klasifikasi_tekanan

# Inisialisasi kolom
KOLOM = [
    'nama', 'berat_badan', 'tinggi_badan', 
    'umur', 'sistol', 'diastol', 'diagnosa', 'bmi', 'kategori_bmi'
]

df_pasien = pd.DataFrame(columns=KOLOM)

def init_console():
    """Initialize DataFrame"""
    global df_pasien
    df_pasien = pd.DataFrame(columns=KOLOM)
    print("✅ Database Pandas DataFrame siap!")

def get_all_data():
    """Get all patient data"""
    return df_pasien

def get_data_by_index(indeks):
    """Get specific patient by index"""
    try:
        if 0 <= indeks < len(df_pasien):
            return df_pasien.iloc[indeks].to_dict()
        return None
    except:
        return None

def create(nama, bb, tb, umur, sistol, diastol):
    """Create new patient record"""
    global df_pasien
    try:
        # Calculate medical values
        diagnosa = klasifikasi_tekanan(umur, sistol, diastol)
        bmi = bb / ((tb/100) ** 2)
        kategori_bmi = klasifikasi_bmi(bmi)
        
        # Create patient dictionary
        pasien_baru = {
            'nama': nama,
            'berat_badan': bb,
            'tinggi_badan': tb,
            'umur': umur,
            'sistol': sistol,
            'diastol': diastol,
            'diagnosa': diagnosa,
            'bmi': round(bmi, 2),
            'kategori_bmi': kategori_bmi
        }
        
        # Add to DataFrame
        new_index = len(df_pasien)
        df_pasien.loc[new_index] = pasien_baru
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def read(indeks=None):
    """Read patient data"""
    try:
        if indeks is not None:
            return get_data_by_index(indeks)
        else:
            return get_all_data()
    except:
        return None

def delete(indeks):
    """Delete patient data"""
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            df_pasien = df_pasien.drop(indeks).reset_index(drop=True)
            return True
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False