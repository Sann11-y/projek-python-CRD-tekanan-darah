import random
import string

def random_string(panjang:int) -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(panjang))

def bmi_klasifikasi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi <= 24.9:
        return "Normal" 
    elif 25 <= bmi <= 29.9:
        return "Gemuk"
    else:
        return "Obesitas"
    
def klasifikasi_tekanan(umur,systolic, diastolic):
    if 6<=umur<=12:
        if systolic<96 or diastolic<55: return "Hipotensi"
        elif systolic>131 or diastolic>62: return "Hipertensi"
        else: return "Normal" 
    elif 13<=umur<=18:
        if systolic<112 or diastolic<62: return "Hipotensi"
        elif systolic>128 or diastolic>80: return "Hipertensi"
        else: return "Normal"
    elif 19<=umur<=65:
        if systolic<90 or diastolic<60: return "Hipotensi"
        elif systolic>120 or diastolic>80: return "Hipertensi"
        else: return "Normal"
    else:
        if systolic<90 or diastolic<60: return "Hipotensi"
        elif systolic>150 or diastolic>90: return "Hipertensi"
        else: return "Normal"

def saran_kesehatan(tekanan, bmi):
    saran_tekanan = ""
    saran_bmi = ""
    
    if tekanan=="Hipotensi":
        saran_tekanan = "Perbanyak minum, makan bergizi, hindari berdiri lama"
    elif tekanan=="Hipertensi":
        saran_tekanan = "Kurangi garam, olahraga teratur, jaga berat ideal"
    else:
        saran_tekanan = "Pertahankan pola hidup sehat!"
    
    if bmi<18.5:
        saran_bmi = "Tingkatkan asupan kalori dan gizi"
    elif 18.5<=bmi<=24.9:
        saran_bmi = "Pertahankan pola makan sehat"
    elif 25<=bmi<=29.9:
        saran_bmi = "Kurangi lemak/gula, perbanyak olahraga"
    else:
        saran_bmi = "Konsultasi dokter untuk diet sehat"
    
    return saran_tekanan, saran_bmi