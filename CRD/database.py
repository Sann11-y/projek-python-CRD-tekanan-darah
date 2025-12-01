from .jantung_console import klasifikasi_bmi, klasifikasi_tekanan

df_pasien = [] 

'''Inisialisasi Data Pasien
Membuat list kosong untuk menyimpan data pasien.
'''
def init_console():
    global df_pasien
    df_pasien = [] 

'''
Menambahkan data pasien ke dalam list.
'''
def create(nama, bb, tb, umur, sistol, diastol):
    global df_pasien
    
    try:
        diagnosa = klasifikasi_tekanan(umur, sistol, diastol)
        
        tinggi_meter = tb / 100.0 
        bmi_hitung = bb / (tinggi_meter * tinggi_meter) 
        kategori_hasil_bmi = klasifikasi_bmi(bmi_hitung) 
        
        data_baru = {
            'nama': nama,
            'berat_badan': bb,
            'tinggi_badan': tb,
            'umur': umur,
            'sistol': sistol,
            'diastol': diastol,
            'diagnosa': diagnosa,
            'bmi': round(bmi_hitung, 2), 
            'kategori_bmi': kategori_hasil_bmi, 
            'saran_gemini': "" 
        }
        df_pasien.append(data_baru)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

'''
Membaca data pasien dari list.
Jika indeks diberikan, kembalikan data pasien sebagai dict.
Jika tidak, kembalikan seluruh list.
'''
def read(indeks=None):
    if indeks is not None:
        if 0 <= indeks < len(df_pasien):
            return df_pasien[indeks] 
        return None
    return df_pasien

'''
Menghapus data pasien dari list berdasarkan indeks.
'''
def delete(indeks):
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            df_pasien.pop(indeks) 
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

'''
Mengupdate kolom 'saran_gemini' untuk pasien tertentu berdasarkan indeks.
'''
def update_saran(indeks, saran_text):
    global df_pasien
    try:
        if 0 <= indeks < len(df_pasien):
            # Update nilai di dictionary dalam list
            df_pasien[indeks]['saran_gemini'] = saran_text
            return True
        return False
    except Exception as e:
        print(f"Error saat update saran: {e}")
        return False