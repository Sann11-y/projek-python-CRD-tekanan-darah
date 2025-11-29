from time import time
from .import database
from .util import bmi_klasifikasi, random_string, klasifikasi_tekanan
import time
import os

def delete(no_data):
    try:
        with open(database.DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_data - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
        
        os.remove(database.DB_NAME)
        os.rename("data_temp.txt", database.DB_NAME)
    except Exception as e:
        print(f"database error: {e}")
        if os.path.exists("data_temp.txt"):
            os.remove("data_temp.txt")


def create(nama,bb,tb,umur,systolic,diastolic):
    diagnosa = klasifikasi_tekanan(int(umur),int(systolic),int(diastolic))
    bmi = float(bb) / ((float(tb)/100) ** 2)
    kategori_bmi = bmi_klasifikasi(bmi)

    data = database.TEMPLATE.copy()

    bb_str = str(bb)
    tb_str = str(tb)
    bmi_str = f"{bmi:.2f}"
    umur_str = str(umur)
    systolic_str = str(systolic)
    diastolic_str = str(diastolic)

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + database.TEMPLATE["nama"][len(nama):]
    data["Berat Badan"] = bb_str + database.TEMPLATE["Berat Badan"][len(bb_str):]
    data["Tinggi Badan"] = tb_str + database.TEMPLATE["Tinggi Badan"][len(tb_str):]
    
    # FIX: Tambahkan spasi untuk padding, bukan ambil dari template "yyy"
    data["umur"] = umur_str + " " * (len(database.TEMPLATE["umur"]) - len(umur_str))
    data["systolic"] = systolic_str + " " * (len(database.TEMPLATE["systolic"]) - len(systolic_str))
    data["diastolic"] = diastolic_str + " " * (len(database.TEMPLATE["diastolic"]) - len(diastolic_str))
    
    data["diagnosa"] = diagnosa + database.TEMPLATE["diagnosa"][len(diagnosa):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["Berat Badan"]},{data["Tinggi Badan"]},{data["umur"]},{data["systolic"]},{data["diastolic"]},{data["diagnosa"]},{bmi_str},{kategori_bmi}\n'
    
    try:
        with open(database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan, gagal menambahkan data")

def create_first_data():
    print("Membuat data pertama")
    nama = input("Nama Pasien: ")

    while True:
        try:
            bb = float(input("Berat Badan (kg): "))
            tb = float(input("Tinggi Badan (cm): "))
            if bb > 0 and tb > 0:
                break
            else:
                print("Berat badan dan tinggi badan harus lebih dari 0")
        except:
            print("Berat badan dan tinggi badan harus angka")
    
    while True:
        try:
            umur = int(input("Umur: "))
            if umur > 0:
                break
            else:
                print("Umur harus lebih dari 0")
        except:
            print("Umur harus angka")
    
    while True:
        try:
            systolic = int(input("Systolic: "))
            if systolic > 0:
                break
            else:
                print("Systolic harus lebih dari 0")
        except:
            print("Systolic harus angka")
    
    while True:
        try:
            diastolic = int(input("Diastolic: "))
            if diastolic > 0:
                break
            else:
                print("Diastolic harus lebih dari 0")
        except:
            print("Diastolic harus angka")

    diagnosa = klasifikasi_tekanan(umur,systolic,diastolic)

    data = database.TEMPLATE.copy()
    bmi = float(bb) / ((float(tb)/100) ** 2)
    kategori_bmi = bmi_klasifikasi(bmi)

    bb_str = str(bb)
    tb_str = str(tb)
    bmi_str = f"{bmi:.2f}"
    umur_str = str(umur)
    systolic_str = str(systolic)
    diastolic_str = str(diastolic)

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + database.TEMPLATE["nama"][len(nama):]
    data["Berat Badan"] = bb_str + database.TEMPLATE["Berat Badan"][len(bb_str):]
    data["Tinggi Badan"] = tb_str + database.TEMPLATE["Tinggi Badan"][len(tb_str):]
    
    # FIX: Tambahkan spasi untuk padding
    data["umur"] = umur_str + " " * (len(database.TEMPLATE["umur"]) - len(umur_str))
    data["systolic"] = systolic_str + " " * (len(database.TEMPLATE["systolic"]) - len(systolic_str))
    data["diastolic"] = diastolic_str + " " * (len(database.TEMPLATE["diastolic"]) - len(diastolic_str))
    
    data["diagnosa"] = diagnosa + database.TEMPLATE["diagnosa"][len(diagnosa):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["Berat Badan"]},{data["Tinggi Badan"]},{data["umur"]},{data["systolic"]},{data["diastolic"]},{data["diagnosa"]},{bmi_str},{kategori_bmi}\n'
    
    try:
        with open(database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
        print("Data pertama berhasil dibuat!")
    except:
        print("Gagal membuat data pertama")

def read(**kwargs):
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_data = len(content)
            if "index" in kwargs:
                index_data = kwargs["index"]-1
                if index_data < 0 or index_data > jumlah_data:
                    return False
                else:    
                    return content[index_data]
            else:
                return content
    except:
        print("Membaca database error")
        return False