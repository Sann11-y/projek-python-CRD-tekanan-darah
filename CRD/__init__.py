'''Inisialisasi Modul CRD'''
from .database import inisialisasiData, read

'''Impor Fungsi Interaksi dari interaksi_data.py'''
from .interaksiData import (
    lihatData, 
    buatData,     
    hapusData,    
    analisisData  
)