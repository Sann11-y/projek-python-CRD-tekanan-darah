import random
import string

def random_string(panjang:int) -> str:
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string

def bmi_klasifikasi(bmi):
    if bmi < 18.5:
        return "Kekurangan Berat Badan"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Kelebihan Berat Badan"
    else:
        return "Obesitas"
    
def klasifikasi_tekanan(umur,systolic, diastolic):
    try:
        if 6<=umur<=12:
            if systolic<96 or diastolic<55:
                return "Hipotensi"
            elif systolic>131 or diastolic>62:
                return "Hipertensi" 
            else:
                return "Normal" 
        elif 13<=umur<=18:
            if systolic<112 or diastolic<62:
                return "Hipotensi"
            elif systolic>128 or diastolic>80:
                return "Hipertensi"
            else:
                return "Normal"
        elif 19<=umur<=65:
            if systolic<90 and diastolic<60:
                return "Hipotensi"
            elif systolic>120 or diastolic>80:  
                return "Hipertensi"
            else:
                return "Normal"
        else:
            if systolic<90 and diastolic<60:
                return "Hipotensi"
            elif systolic>150 or diastolic>90:
                return "Hipertensi"
            else:
                return "Normal"
    except:
        return "Umur Tidak Valid"

def faktorPemicu(tekanan):
    if tekanan=="Hipotensi":
        return """Faktor pemicu Hipotensi anda adalah:
            -Dehidrasi, 
            -Kurangnya Nutrisi, 
            -Masalah Jantung, 
            -Masalah Endokrin, 
            -Kehamilan, 
            -Anafilaksis, 
            -Penggunaan Obat-obatan Tertentu, 
            -Pendarahan, 
            -Infeksi Berat (Sepsis), 
            -Berdiri Terlalu Lama"""
    elif tekanan=="Hipertensi":
        return """Faktor pemicu Hipertensi anda adalah: 
            -Konsumsi Garam Berlebih, 
            -Obesitas, 
            -Kurang Aktivitas Fisik, 
            -Stres, 
            -Konsumsi Alkohol Berlebih, 
            -Merokok, 
            -Faktor Genetik, 
            -Usia, 
            -Penyakit Ginjal, 
            -Gangguan Hormon"""
    else:
        return "Tekanan darah normal, pertahankan pola hidup sehat!"

def saranKesehatan(tekanan, bmi):
    saran_tekanan = ""
    saran_bmi = ""
    
    if tekanan=="Hipotensi":
        saran_tekanan = "Perbanyak Minum Air Putih, Konsumsi Makanan Bergizi, Hindari Berdiri Terlalu Lama, Gunakan Stoking Kompresi"
    elif tekanan=="Hipertensi":
        saran_tekanan = "Kurangi Asupan Garam, Konsumsi Makanan Sehat (Buah dan Sayur), Rutin Berolahraga, Pertahankan Berat Badan Ideal"
    else:
        saran_tekanan = "Tekanan darah normal, pertahankan pola hidup sehat!"
    
    if bmi<18.5:
        saran_bmi = "Konsumsi Makanan Bergizi dan Tingkatkan Asupan Kalori"
    elif 18.5<=bmi<=24.9:
        saran_bmi = "Pertahankan Pola Makan Sehat dan Rutin Berolahraga"
    elif 25<=bmi<=29.9:
        saran_bmi = "Kurangi Asupan Makanan Tinggi Lemak dan Gula, Rutin Berolahraga"
    else:
        saran_bmi = "Konsultasi dengan Profesional Kesehatan untuk Rencana Penurunan Berat Badan"
    
    return saran_tekanan, saran_bmi