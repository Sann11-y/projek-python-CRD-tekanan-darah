from . import database
from .util import klasifikasi_bmi, klasifikasi_tekanan

def create(nama, bb, tb, umur, sistol, diastol):
    """Create new patient record"""
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
        
        return database.add_data(pasien_baru)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def read(indeks=None):
    """Read patient data"""
    try:
        if indeks is not None:
            return database.get_data_by_index(indeks)
        else:
            return database.get_all_data()
    except:
        return None

def delete(indeks):
    """Delete patient data"""
    try:
        return database.delete_data(indeks)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False