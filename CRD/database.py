# Database in-memory pakai list
dataPasien = []  # ← LIST KOSONG untuk nyimpen data

# Template structure untuk setiap pasien
PATIENT_TEMPLATE = {
    'id': '',
    'timestamp': '', 
    'nama': '',
    'berat_badan': 0,
    'tinggi_badan': 0,
    'umur': 0,
    'systolic': 0,
    'diastolic': 0,
    'diagnosa': '',
    'bmi': 0,
    'kategori_bmi': ''
}

def init_console():
    """Initialize in-memory database"""
    dataPasien.clear()  # Pastikan list kosong
    print("✅ Database in-memory siap!")

def get_all_data():
    """Get all patient data"""
    return dataPasien

def add_data(patient_dict):
    """Add new patient to list"""
    dataPasien.append(patient_dict)
    return True

def delete_data(index):
    """Delete patient by index"""
    if 0 <= index < len(dataPasien):
        dataPasien.pop(index)
        return True
    return False

def get_data_by_index(index):
    """Get specific patient by index"""
    if 0 <= index < len(dataPasien):
        return dataPasien[index]
    return None