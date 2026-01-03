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
    
    hitungBMI = bb / ((tb / 100) ** 2)

    dataBaru = {
        'nama': nama,
        'beratBadan': bb,
        'tinggiBadan': tb,
        'umur': umur,
        'sistol': sistol,
        'diastol': diastol,
        'diagnosa': klasifikasiTekanan(umur, sistol, diastol),
        'bmi': hitungBMI, 
        'kategoriBmi': klasifikasiBmi(hitungBMI), 
        'saranGemini': "" 
    }
    dfPasien.append(dataBaru)
    return True

'''
Membaca data pasien dari list (Operasi READ).
Jika indeks diberikan, kembalikan data pasien tunggal sebagai dict.
Jika tidak, kembalikan seluruh list.
'''
def read(indeks=None):
    if indeks is None:
        return dfPasien 
    elif 0 <= indeks < len(dfPasien):
        return dfPasien[indeks] 
    else:
        return False

'''
Mengupdate kolom 'saranGemini' untuk pasien tertentu berdasarkan indeks (Operasi UPDATE).
'''
# penyimpanan saran daru ai dalam memori dan diupdate ke dfpasien sehingga data dapat dibaca lagi di opsi menu 2 atau opsi menu 3 tanpa harus analisis ulang
#  selagi program tetap berjalan
def updateSaran(indeks, saranText):
    global dfPasien
    if 0 <= indeks < len(dfPasien):
        dfPasien[indeks]['saranGemini'] = saranText #  update saran gemini
        return True
    else:
        return False
    
'''
Menghapus data pasien dari list berdasarkan indeks (Operasi DELETE).
'''
def delete(indeks):
    global dfPasien
    if 0 <= indeks < len(dfPasien):
        dfPasien.pop(indeks)
        return True
    else:
        return False

