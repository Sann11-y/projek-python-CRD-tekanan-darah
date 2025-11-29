def klasifikasi_tekanan(umur,systolic, diastolic):
    try:
        if 6<=umur<=12:
            status="anak-anak"
            if systolic<131 and diastolic<55:
                return "Hipotensi"
            elif systolic>131 or diastolic>62:
                return "Hipertensi" 
            else:
                return "Normal" 
        elif 14<=umur<=18:
            status="remaja"  
            if systolic<112 and diastolic<62:
                return "Hipotensi"
            elif systolic>128 and diastolic>80:
                return "Hipertensi"
            else:
                return "Normal"
        elif 19<=umur<=65:
            status="dewasa"
            if systolic<90 and diastolic<60:
                return "Hipotensi"
            elif systolic>120 or diastolic>80:  
                return "Hipertensi"
            else:
                return "Normal"
        else:
            status="lansia"
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
        return "Faktor pemicu Hipotensi anda adalah\t: Dehidrasi, Kurangnya Nutrisi, Masalah Jantung, Masalah Endokrin, Kehamilan, Anafilaksis, Penggunaan Obat-obatan Tertentu, Pendarahan, Infeksi Berat (Sepsis), Berdiri Terlalu Lama"
    elif tekanan=="Hipertensi":
        return "Faktor pemicu Hipertensi anda adalah\t: Konsumsi Garam Berlebih, Obesitas, Kurang Aktivitas Fisik, Stres, Konsumsi Alkohol Berlebih, Merokok, Faktor Genetik, Usia, Penyakit Ginjal, Gangguan Hormon"
    else:
        return "Tekanan darah anda normal, pertahankan pola hidup sehat!"
def saranKesehatan(tekanan):
    if tekanan=="Hipotensi":
        return "Saran kesehatan untuk Hipotensi\t: Perbanyak Minum Air Putih, Konsumsi Makanan Bergizi, Hindari Berdiri Terlalu Lama, Gunakan Stoking Kompresi, Konsumsi Kafein Secara Moderat, Hindari Alkohol, Lakukan Olahraga Ringan, Cukup Istirahat"
    elif tekanan=="Hipertensi":
        return "Saran kesehatan untuk Hipertensi\t: Kurangi Asupan Garam, Konsumsi Makanan Sehat (Buah dan Sayur), Rutin Berolahraga, Pertahankan Berat Badan Ideal, Batasi Konsumsi Alkohol, Hindari Merokok, Kelola Stres dengan Baik, Rutin Periksa Tekanan Darah"
    else:
        return "Tekanan darah anda normal, pertahankan pola hidup sehat!"