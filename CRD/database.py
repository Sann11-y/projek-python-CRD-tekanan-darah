# Database in-memory pakai list
patients_data = []  # ← LIST KOSONG untuk nyimpen data

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
    patients_data.clear()  # Pastikan list kosong
    print("✅ Database in-memory siap!")

def get_all_data():
    """Get all patient data"""
    return patients_data

def add_data(patient_dict):
    """Add new patient to list"""
    patients_data.append(patient_dict)
    return True

def delete_data(index):
    """Delete patient by index"""
    if 0 <= index < len(patients_data):
        patients_data.pop(index)
        return True
    return False

def get_data_by_index(index):
    """Get specific patient by index"""
    if 0 <= index < len(patients_data):
        return patients_data[index]
    return None