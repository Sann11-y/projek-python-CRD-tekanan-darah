import pandas as pd

df_pasien = pd.DataFrame()

KOLOM = [
    'nama', 'berat_badan', 'tinggi_badan', 
    'umur', 'sistol', 'diastol', 'diagnosa', 'bmi', 'kategori_bmi'
]

def init_console():
    """Initialize DataFrame"""
    global df_pasien
    df_pasien = pd.DataFrame(columns=KOLOM)
    print("✅ Database Pandas DataFrame siap!")

def get_all_data():
    """Get all patient data"""
    return df_pasien

def add_data(data_pasien):
    """Add new patient data"""
    global df_pasien
    try:
        baris_baru = pd.DataFrame([data_pasien])
        df_pasien = pd.concat([df_pasien, baris_baru], ignore_index=True)
        return True
    except Exception as e:
        print(f"Error adding data: {e}")
        return False

def delete_data(indeks):
    """Delete patient data by index"""
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            df_pasien = df_pasien.drop(df_pasien.index[indeks]).reset_index(drop=True)
            return True
        return False
    except:
        return False

def get_data_by_index(indeks):
    """Get specific patient by index"""
    try:
        if 0 <= indeks < len(df_pasien):
            return df_pasien.iloc[indeks].to_dict()
        return None
    except:
        return None