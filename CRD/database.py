from .interaksiData import klasifikasiBmi, klasifikasiTekanan

dfPasien = [] 

'''Inisialisasi Data Pasien
Fungsi untuk mengosongkan (mereset) list data pasien saat program dimulai.
'''
def inisialisasiData():
    global dfPasien
    dfPasien = [] 

'''
Menambahkan data pasien baru ke dalam list (Operasi CREATE).
Data disimpan setelah diklasifikasikan BMI dan Tekanan Darahnya.
'''
def create(nama, bb, tb, umur, sistol, diastol):
    global dfPasien
    
    try:
        diagnosa = klasifikasiTekanan(umur, sistol, diastol) 
        bmiHitung = bb / ((tb / 100.0) ** 2)
        kategoriHasilBmi = klasifikasiBmi(bmiHitung) 

        dataBaru = {
            'nama': nama,
            'beratBadan': bb,
            'tinggiBadan': tb,
            'umur': umur,
            'sistol': sistol,
            'diastol': diastol,
            'diagnosa': diagnosa,
            'bmi': round(bmiHitung, 2), 
            'kategoriBmi': kategoriHasilBmi, 
            'saranGemini': "" 
        }
        dfPasien.append(dataBaru)
        return True
    except Exception as e:
        print(f"Error saat membuat data: {e}")
        return False

'''
Membaca data pasien dari list (Operasi READ).
Jika indeks diberikan, kembalikan data pasien tunggal sebagai dict.
Jika tidak, kembalikan seluruh list.
'''
def read(indeks=None):
    if indeks is not None:
        # Cek apakah indeks valid
        if 0 <= indeks < len(dfPasien):
            return dfPasien[indeks] 
        return None
    # Kembalikan seluruh data jika indeks tidak diberikan
    return dfPasien

'''
Menghapus data pasien dari list berdasarkan indeks (Operasi DELETE).
'''
def delete(indeks):
    global dfPasien
    try:
        if 0 <= indeks < len(dfPasien):
            dfPasien.pop(indeks) # Menghapus item berdasarkan indeks
            return True
        return False
    except Exception as e:
        print(f"Error saat menghapus data: {e}")
        return False

'''
Mengupdate kolom 'saranGemini' untuk pasien tertentu berdasarkan indeks (Operasi UPDATE).
'''
def updateSaran(indeks, saranText):
    global dfPasien
    try:
        if 0 <= indeks < len(dfPasien):
            dfPasien[indeks]['saranGemini'] = saranText 
            return True
        return False
    except Exception as e:
        print(f"Error saat update saran: {e}")
        return False