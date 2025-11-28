from . import operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "nama":255*" ",
    "Berat Badan":"yyy",
    "Tinggi Badan":"yyy",
    "umur":"yyy",
    "systolic":"yyy", 
    "diastolic":"yyy",
    "diagnosa":255*" "
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        operasi.create_first_data()