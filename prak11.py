# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:36:54 2021

@author: FARIZ UBAIDILLAH
"""

print('ini Sebelum diurutkan [1,15,10,5,20,8,12,6]')
def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def binary_search(arr,num_find):

    mulai = 0
    end = len(arr) - 1
    mid = (mulai + end)//2
    found = False
    position = -1
    bubbleSort(arr)
    while mulai <= end:
        if arr[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > arr[mid]:
            mulai = mid + 1
            mid = (mulai + end)//2
        else:
            end = mid - 1
            mid = (mulai + end)//2

    print("Sesudah diurutkan: ", array)
    return (found, position-1)

array=[1,15,10,5,20,8,12,6]
num = int(input('Silahkan anda Masukkan angka yang dicari: '))

found = binary_search(array,num )
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)