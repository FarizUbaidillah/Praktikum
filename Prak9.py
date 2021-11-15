# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:21:08 2021
@NIM :065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""
def penjumlahan(nilai = 0, jumlah=0 ,o=1):
    if (jumlah<=0):
        return 0
    else:
        nilai = int(input('Masukkan Angka Ke-'+str(o)+':'))
        if(jumlah==1):
            return nilai

        else:
            o+=1
            return nilai + penjumlahan (nilai,jumlah-1,o)

jmlh = int(input('masukan jumlah bilangan:'))
nilai = penjumlahan(jumlah=jmlh)
print('hasil dari penjumlahan adalah:'+str(nilai))
        

        
      
    
    
     
    
    
    

