# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 23:06:42 2021
NIM :065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""

f = False

def satu():
    print("(", x,  "'st')")
def dua():
    print("(", x, "'nd')")
def tiga():
    print("(", x, "'rd')")
def semua():
    print("(", x, "'th')")


while (not f) :
    print('Masukkan 0 Untuk Memberhentikan Program')
    x = int(input("Masukkan Angka :"))
    
    if (x == 0):
        f = True
        print('Thank you for using our program')
    elif x == 1:
        satu()
    elif x == 2:
        dua()
    elif x == 3:
        tiga()
    elif x >= 4:
        semua()
    else :
        print('Masukkan Angka Yang Benar !')

