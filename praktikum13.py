# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:45:16 2021

@author: FARIZ UBAIDILLAH
"""

import pandas as pd
data = pd.read_csv('C:/Praktikum/Negara.csv')

df=pd.DataFrame(data)
RataRata=df.groupby(['Benua']).mean()
std=df.groupby(['Benua']).std()

print("Berikut Data Framenya:\n")
print(df)
print("\nBerikut Data Mean:")
print(RataRata)
print("\nBerikut Data Standard Deviation:")
print(std)
