from . import database
from .util import random_string, bmi_klasifikasi, klasifikasi_tekanan
import time

def create(nama, bb, tb, umur, systolic, diastolic):
    """Create new patient record in memory"""
    try:
        # Calculate medical values
        diagnosa = klasifikasi_tekanan(umur, systolic, diastolic)
        bmi = bb / ((tb/100) ** 2)
        kategori_bmi = bmi_klasifikasi(bmi)
        
        # Create patient dictionary
        new_patient = {
            'id': random_string(6),
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'nama': nama,
            'berat_badan': bb,
            'tinggi_badan': tb,
            'umur': umur,
            'systolic': systolic,
            'diastolic': diastolic,
            'diagnosa': diagnosa,
            'bmi': round(bmi, 2),
            'kategori_bmi': kategori_bmi
        }
        
        # Add to in-memory list
        return database.add_data(new_patient)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def read(index=None):
    """Read data from memory"""
    try:
        if index is not None:
            # Return specific patient
            return database.get_data_by_index(index)
        else:
            # Return all patients
            return database.get_all_data()
    except:
        return None

def delete(index):
    """Delete patient from memory"""
    try:
        return database.delete_data(index)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False