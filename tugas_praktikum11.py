# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:47:46 2021

@author: FARIZ UBAIDILLAH
"""

def penukaran(A, m, p):
    temp = A[m]
    A[m] = A[p]
    A[p] = temp

def bubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            penukaran(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)

A = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(A, len(A))
print("List yang sudah disorting")
print(A)