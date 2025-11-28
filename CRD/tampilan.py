from . import Operasi
from .util import faktorPemicu, saranKesehatan

def analisis_console():
    data_file = Operasi.read()
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return
        
    read_console()
    while(True):
        print("Silahkan pilih nomor data untuk analisis kesehatan")
        try:
            no_data = int(input("Nomor Data: "))
            data_pasien = Operasi.read(index=no_data)

            if data_pasien:
                break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        except:
            print("Input harus angka")
    
    data_break = data_pasien.split(',')
    nama = data_break[2].strip()
    umur = data_break[3].strip()
    systolic = data_break[4].strip()
    diastolic = data_break[5].strip()
    diagnosa = data_break[6].strip()
    
    print("\n"+"="*80)
    print("ANALISIS KESEHATAN TEKANAN DARAH")
    print("="*80)
    print(f"Nama Pasien\t: {nama}")
    print(f"Umur\t\t: {umur} tahun")
    print(f"Tekanan Darah\t: {systolic}/{diastolic} mmHg")
    print(f"Diagnosa\t: {diagnosa}")
    print("\nFaktor Pemicu\t:")
    print(f"  {faktorPemicu(diagnosa)}")
    print("\nSaran Kesehatan\t:")
    print(f"  {saranKesehatan(diagnosa)}")
    print("="*80)
    input("\nTekan Enter untuk melanjutkan...")

def delete_console():
    data_file = Operasi.read()
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return
        
    read_console()
    while(True):
        print("Silahkan pilih nomor data yang akan di delete")
        try:
            no_data = int(input("Nomor Data: "))
            data_pasien = Operasi.read(index=no_data)

            if data_pasien:
                data_break = data_pasien.split(',')
                pk = data_break[0]
                data_add = data_break[1]
                nama = data_break[2]
                umur = data_break[3]
                systolic = data_break[4]
                diastolic = data_break[5]
                diagnosa = data_break[6][:-1]

                print("\n"+"="*80)
                print("Data yang ingin anda Hapus")
                print(f"1. Nama\t\t: {nama:.40}")
                print(f"2. Umur\t\t: {umur:3}")
                print(f"3. Systolic\t: {systolic:3}")
                print(f"4. Diastolic\t: {diastolic:3}")
                print(f"5. Diagnosa\t: {diagnosa:.40}")
                is_done = input("Apakah anda yakin (y/n)? ")
                if is_done.lower() == "y":
                    Operasi.delete(no_data)
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

    Operasi.create(nama,umur,systolic,diastolic)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    if not data_file:
        print("Tidak ada data yang ditemukan")
        return

    no = "No"
    nama = "Nama Pasien"
    umur = "Umur"
    systolic = "Systolic"
    diastolic = "Diastolic"
    diagnosa = "Diagnosa"

    print("\n"+"="*100)
    print(f"{no:4} | {nama:20} | {umur:4} | {systolic:8} | {diastolic:9} | {diagnosa:15}")
    print("-"*100)
    
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        nama = data_break[2].strip()
        umur = data_break[3].strip()
        systolic = data_break[4].strip()
        diastolic = data_break[5].strip()
        diagnosa = data_break[6].strip()
        print(f"{index+1:4} | {nama:20.20} | {umur:4} | {systolic:8} | {diastolic:9} | {diagnosa:15.15}")

    print("="*100+"\n")