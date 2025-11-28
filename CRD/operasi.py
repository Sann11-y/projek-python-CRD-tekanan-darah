from time import time
from .import database
from .util import random_string, klasifikasi_tekanan
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
        
        # Hapus file lama dan rename file temp
        os.remove(database.DB_NAME)
        os.rename("data_temp.txt", database.DB_NAME)
    except Exception as e:
        print(f"database error: {e}")
        # Hapus file temp jika ada error
        if os.path.exists("data_temp.txt"):
            os.remove("data_temp.txt")


def create(nama,bb,tb,umur,systolic,diastolic):
    diagnosa = klasifikasi_tekanan(int(umur),int(systolic),int(diastolic))
    
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + database.TEMPLATE["nama"][len(nama):]
    bb_str=str(bb)
    tb_str=str(tb)
    data["Berat Badan"] = bb_str+database.TEMPLATE["Berat Badan"]
    data["Tinggi Badan"] = tb_str+database.TEMPLATE["Tinggi Badan"]
    data["umur"] = str(umur)
    data["systolic"] = str(systolic)
    data["diastolic"] = str(diastolic)
    data["diagnosa"] = diagnosa + database.TEMPLATE["diagnosa"][len(diagnosa):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["Berat Badan"]},{data["Tinggi Badan"]},{data["umur"]},{data["systolic"]},{data["diastolic"]},{data["diagnosa"]}\n'
    
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

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + database.TEMPLATE["nama"][len(nama):]
    data["Berat Badan"] = database.TEMPLATE["Berat Badan"]
    data["Tinggi Badan"] = database.TEMPLATE["Tinggi Badan"]
    data["umur"] = str(umur)
    data["systolic"] = str(systolic)
    data["diastolic"] = str(diastolic)
    data["diagnosa"] = diagnosa + database.TEMPLATE["diagnosa"][len(diagnosa):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["Berat Badan"]},{data["Tinggi Badan"]},{data["umur"]},{data["systolic"]},{data["diastolic"]},{data["diagnosa"]}\n'
    
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