# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:35:46 2021
NIM : 065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""

print('Membuat program pemangkatan positif dan negatif')

def pos(x) :
       y = int(input('Masukkan Pangkatnya :'))
       pangkat = x ** y
       print('Hasilnya Adalah', pangkat) 

def neg(x) : 
       y = int(input('Masukkan Pangkatnya :')) 
       pangkat = x ** y
       print('Hasilnya Adalah', pangkat) 
x = int(input('Masukkan Angka :')) 
if x >= 0 :
    pos(x) 
elif x <= 0 :
    neg(x) 
else :
    print('Tolong Masukkan Angka')