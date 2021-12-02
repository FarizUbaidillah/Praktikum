# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:04:22 2021
NIM : 065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""
def membuat(nfile):
    nama = input('Masukkan Nama : ')
    nim = input('Masukkan NIM : ')
    tahun = input('Masukkan Tahun Angkatan : ')
    teks = 'Nama: {}\nNIM: {}\nTahun Angkatan{}'.format(nama, nim, tahun)

    file_sertifikasi = open(str(nfile), "w")
    file_sertifikasi.write(teks)
    file_sertifikasi.close()
    print('SELAMAT File Berhasil  DItambahkan')
    
    
def membaca(bfile):
    file_biodata = open(str(bfile), "r")
    print(file_biodata.read())
    print()
    file_biodata.close()


def tambah(tfile) :
    friends = input('Masukkan Nama Sahabat : ')
    notes = input('Masukkan Catatan Tambahan : ')
    
    teks = 'Nama Sahabat: {}\nCatatan: {}'.format(friends, notes)
    file_serti = open(str(tfile), "a")
    file_serti.write(teks)
    file_serti.close()
    
    
    
n = ''

print('>>> Program File <<<')
print('1. Membaca File')
print('2. Membuat dan Menulis File')
print('3. Menambah Text Pada File')
print('4. Keluar Dari Program File')

while (n != '4'):
    n = int(input('Silahkan Pilih Berupa Angka Yang Tertera Diatas : '))
    
    if n == 4:
        print('Terima Kasih Telah Menggunakan Program Kami')
        break
    if n == 1:
        bf = str(input('Masukkan Nama File Yang Ingin Dibaca :'))
        membaca(bf)
    elif n == 2 :
        nf = str(input('Masukkan Nama File  : '))
        membuat(nf)
    elif n == 3 :
        tf = str(input('Masukkan Nama File Yang Ingin Ditambah : '))
        tambah(tf)
    else : 
        print('Masukkan Sesuai Angka Diatas !')
