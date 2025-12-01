'''Inisialisasi Modul CRD'''
from .database import init_console

'''Impor Fungsi Konsol dari jantung_console.py'''
from .jantung_console import (
    read_console, 
    create_console, 
    delete_console, 
    analisis_console
)
