import pandas as pd

# DataFrame global untuk menyimpan data
df_pasien = pd.DataFrame()

# Template columns untuk DataFrame
COLUMNS = [
    'id', 'timestamp', 'nama', 'berat_badan', 'tinggi_badan', 
    'umur', 'systolic', 'diastolic', 'diagnosa', 'bmi', 'kategori_bmi'
]

def init_console():
    """Initialize pandas DataFrame"""
    global df_pasien
    df_pasien = pd.DataFrame(columns=COLUMNS)
    print("✅ Database Pandas DataFrame siap!")

def get_all_data():
    """Get all patient data as DataFrame"""
    return df_pasien

def add_data(patient_dict):
    """Add new patient to DataFrame"""
    global df_pasien
    try:
        # Convert dict to DataFrame with one row
        new_row = pd.DataFrame([patient_dict])
        # Append ke DataFrame utama
        df_pasien = pd.concat([df_pasien, new_row], ignore_index=True)
        return True
    except Exception as e:
        print(f"Error adding data: {e}")
        return False

def delete_data(index):
    """Delete patient by index"""
    global df_pasien
    try:
        if 0 <= index < len(df_pasien):
            df_pasien = df_pasien.drop(df_pasien.index[index]).reset_index(drop=True)
            return True
        return False
    except:
        return False

def get_data_by_index(index):
    """Get specific patient by index as dict"""
    try:
        if 0 <= index < len(df_pasien):
            return df_pasien.iloc[index].to_dict()
        return None
    except:
        return None