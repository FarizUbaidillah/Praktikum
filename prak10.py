# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:36:29 2021

@author: FARIZ UBAIDILLAH
"""

def writte():
    data = "Nama: {}\nUmur: {}\nAlamat: {}\nEmail: {}\nDosen Wali: {}".format(nama, umur, alamat, email, dosen)

    file_bio = open("Bio.txt", "w")
    file_bio.writelines(data)
    file_bio.close()
    
    read()

def read():
    file_biodata = open("Bio.txt", "r")
    print(file_biodata.read())
    file_biodata.close()




nama = input('Masukkan Nama : ')
umur = input('Masukkan Umur : ')
alamat = input('Masukkan Alamat : ')
email = input('Masukkan Email : ')
dosen = input('Siapa Dosen Wali : ')

writte()