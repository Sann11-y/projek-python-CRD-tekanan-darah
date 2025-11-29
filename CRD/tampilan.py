from . import operasi
from .util import faktorPemicu, saranKesehatan, bmi_klasifikasi

def analisis_console():
    data_file = operasi.read()
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return
        
    read_console()
    while(True):
        print("Silahkan pilih nomor data untuk analisis kesehatan")
        try:
            no_data = int(input("Nomor Data: "))
            data_pasien = operasi.read(index=no_data)

            if data_pasien:
                break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        except:
            print("Input harus angka")
    
    data_break = data_pasien.split(',')
    nama = data_break[2].strip()
    bb = float(data_break[3].strip())
    tb = float(data_break[4].strip())
    umur = data_break[5].strip()
    systolic = data_break[6].strip()
    diastolic = data_break[7].strip()
    diagnosa = data_break[8].strip()
    
    # Ambil BMI dari data atau hitung jika tidak ada
    if len(data_break) >= 11:
        bmi = float(data_break[9].strip())
        kategori_bmi = data_break[10].strip()
    else:
        bmi = bb / ((tb/100) ** 2)
        kategori_bmi = bmi_klasifikasi(bmi)
    
    # Ambil saran kesehatan
    saran_tekanan, saran_bmi = saranKesehatan(diagnosa, bmi)
    
    print("\n"+"="*80)
    print("ANALISIS KESEHATAN TEKANAN DARAH DAN BMI".center(80))
    print("="*80)
    print(f"Nama Pasien\t\t: {nama}")
    print(f"Berat Badan\t\t: {bb} kg")
    print(f"Tinggi Badan\t\t: {tb} cm")
    print(f"BMI\t\t\t: {bmi:.2f}")
    print(f"Kategori BMI\t\t: {kategori_bmi}")
    print(f"Umur\t\t\t: {umur} tahun")
    print(f"Tekanan Darah\t\t: {systolic}/{diastolic} mmHg")
    print(f"Diagnosa Tekanan Darah\t: {diagnosa}")
    
    print("\n" + "="*80)
    print("FAKTOR PEMICU")
    print("="*80)
    print(faktorPemicu(diagnosa))
    
    print("\n" + "="*80)
    print("SARAN KESEHATAN")
    print("="*80)
    print(f"\nUntuk Tekanan Darah:")
    print(f"  {saran_tekanan}")
    print(f"\nUntuk BMI:")
    print(f"  {saran_bmi}")
    print("="*80)
    input("\nTekan Enter untuk melanjutkan...")

def delete_console():
    data_file = operasi.read()
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return
        
    read_console()
    while(True):
        print("Silahkan pilih nomor data yang akan di delete")
        try:
            no_data = int(input("Nomor Data: "))
            data_pasien = operasi.read(index=no_data)

            if data_pasien:
                data_break = data_pasien.split(',')
                nama = data_break[2]
                bb = data_break[3]
                tb = data_break[4]
                systolic = data_break[6]
                diastolic = data_break[7]
                diagnosa = data_break[8].strip()
                
                print("\n"+"="*80)
                print("Data yang ingin anda Hapus")
                print(f"1. Nama\t\t: {nama:.40}")
                print(f"2. Berat Badan\t: {bb:12}")
                print(f"3. Tinggi Badan\t: {tb:12}")
                print(f"4. Systolic\t: {systolic:3}")
                print(f"5. Diastolic\t: {diastolic:3}")
                print(f"6. Diagnosa\t: {diagnosa:.40}")
                is_done = input("Apakah anda yakin (y/n)? ")
                if is_done.lower() == "y":
                    operasi.delete(no_data)
                    break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        except:
            print("Input harus angka")

    print("Data berhasil di hapus")


def create_console():
    print("\n\n"+"="*80)
    print("Silahkan tambah data tekanan darah\n")
    nama = input("Nama Pasien\t: ")
    
    while True:
        try:
            bb = float(input("Berat Badan (kg)\t: "))
            tb = float(input("Tinggi Badan (cm)\t: "))
            if bb > 0 and tb > 0:
                break
            else:
                print("Berat badan dan tinggi badan harus lebih dari 0")
        except:
            print("Berat badan dan tinggi badan harus angka")
    
    while True:
        try:
            umur = int(input("Umur\t\t: "))
            if umur > 0:
                break
            else:
                print("Umur harus lebih dari 0")
        except:
            print("Umur harus angka")
    
    while True:
        try:
            systolic = int(input("Systolic\t: "))
            if systolic > 0:
                break
            else:
                print("Systolic harus lebih dari 0")
        except:
            print("Systolic harus angka")
    
    while True:
        try:
            diastolic = int(input("Diastolic\t: "))
            if diastolic > 0:
                break
            else:
                print("Diastolic harus lebih dari 0")
        except:
            print("Diastolic harus angka")

    operasi.create(nama,bb,tb,umur,systolic,diastolic)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = operasi.read()
    
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return

    print("\n"+"="*135)
    print(f"{'No':3} | {'Nama':20} | {'BB(kg)':7} | {'TB(cm)':7} | {'BMI':6} | {'Umur':4} | {'Sys':4} | {'Dias':4} | {'Diagnosa TD':13} | {'Kategori BMI':22}")
    print("-"*135)
    
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        
        if len(data_break) < 9:
            continue
        
        nama = data_break[2].strip()
        bb = data_break[3].strip()
        tb = data_break[4].strip()
        umur = data_break[5].strip()
        systolic = data_break[6].strip()
        diastolic = data_break[7].strip()
        diagnosa = data_break[8].strip()
        
        # Ambil BMI dari data atau hitung
        if len(data_break) >= 11:
            bmi = data_break[9].strip()
            kategori_bmi = data_break[10].strip()
        else:
            try:
                bmi_calc = float(bb) / ((float(tb)/100) ** 2)
                bmi = f"{bmi_calc:.2f}"
                kategori_bmi = bmi_klasifikasi(bmi_calc)
            except:
                bmi = "N/A"
                kategori_bmi = "N/A"
        
        print(f"{index+1:3} | {nama:20.20} | {bb:7} | {tb:7} | {bmi:6} | {umur:4} | {systolic:4} | {diastolic:4} | {diagnosa:13.13} | {kategori_bmi:22.22}")

    print("="*135+"\n")