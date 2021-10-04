# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:16:09 2021
@NIM : 065.00.21.00.016
@author: FARIZ UBAIDILLAH
"""



print ("membuat program mengetahui jenis segitiga")
A = float(input("masukan sisi A = "))
B = float(input("masukan sisi B = "))
C = float(input("masukan sisi C = "))



if (A==B==C) : 
    print("merupakan jenis segitiga sama sisi ")
elif (A==B or B==C or C==A) : 
    print ("merupakan jenis segitiga samakaki ")
elif ((A + B <=C) or (A + C <=B) or (B + C <= A)) :
    print ("bukan merupakan segitiga ")
else :
    print("merupakan segitiga sembarang ")