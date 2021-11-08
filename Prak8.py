# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:34:19 2021
@NIM :065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""


print("Menentukan Bilangan Prima")
bagi = 2

def prima(nilai) :
        print('NILAI', nilai, 'Adalah Bilangan Prima')

def bukan_prima(nilai) :
    print('NILAI', nilai, 'Bukan Bilangan Prima')
    if nilai % 2 == 0 :
        genap = nilai / 2 
        print('2 Dikali', int(genap), '=', nilai)
    else :
        ganjil = nilai / 3
        print('3 Dikali', int(ganjil), '=', nilai)


nilai = int(input('Masukkan Nilai : '))
while nilai % bagi != 0 :
    bagi = bagi + 1
if bagi == nilai :
    prima(nilai)
else :
    bukan_prima(nilai)
    
