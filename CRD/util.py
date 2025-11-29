def klasifikasi_bmi(bmi):
    """Classify BMI into category"""
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi <= 24.9:
        return "Normal" 
    elif 25 <= bmi <= 29.9:
        return "Gemuk"
    else:
        return "Obesitas"
    
def klasifikasi_tekanan(umur, sistol, diastol):
    """Classify blood pressure based on age"""
    if 6 <= umur <= 12:
        if sistol < 96 or diastol < 55: 
            return "Hipotensi"
        elif sistol > 131 or diastol > 62: 
            return "Hipertensi"
        else: 
            return "Normal" 
    elif 13 <= umur <= 18:
        if sistol < 112 or diastol < 62: 
            return "Hipotensi"
        elif sistol > 128 or diastol > 80: 
            return "Hipertensi"
        else: 
            return "Normal"
    elif 19 <= umur <= 65:
        if sistol < 90 or diastol < 60: 
            return "Hipotensi"
        elif sistol > 120 or diastol > 80: 
            return "Hipertensi"
        else: 
            return "Normal"
    else:
        if sistol < 90 or diastol < 60: 
            return "Hipotensi"
        elif sistol > 150 or diastol > 90: 
            return "Hipertensi"
        else: 
            return "Normal"

def saran_kesehatan(tekanan, bmi):
    """Generate health advice based on diagnosis"""
    saran_tekanan = ""
    saran_bmi = ""
    
    if tekanan == "Hipotensi":
        saran_tekanan = "Perbanyak minum, makan bergizi, hindari berdiri lama"
    elif tekanan == "Hipertensi":
        saran_tekanan = "Kurangi garam, olahraga teratur, jaga berat ideal"
    else:
        saran_tekanan = "Pertahankan pola hidup sehat!"
    
    if bmi < 18.5:
        saran_bmi = "Tingkatkan asupan kalori dan gizi"
    elif 18.5 <= bmi <= 24.9:
        saran_bmi = "Pertahankan pola makan sehat"
    elif 25 <= bmi <= 29.9:
        saran_bmi = "Kurangi lemak/gula, perbanyak olahraga"
    else:
        saran_bmi = "Konsultasi dokter untuk diet sehat"
    
    return saran_tekanan, saran_bmi