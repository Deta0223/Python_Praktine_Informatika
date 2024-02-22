# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:19:23 2023

@author: Deivydas
"""
import collections

kiekis = 0
ilg = "a"
f = open("Metai.txt", "r", encoding ="utf8")
ZodziuSarasas = []
FiltruotasSarasas = []
Ilgiausias = "a"
for eilute in f:
    eilute = eilute.replace(",", " ")
    eilute = eilute.replace(".", " ")
    eilute = eilute.replace("–", " ")
    eilute = eilute.replace(":", " ")
    eilute = eilute.replace("(", " ")
    eilute = eilute.replace(")", " ")
    eilute = eilute.replace("-", " ")
    eilute = eilute.strip().split(" ")
    ZodziuSarasas += eilute

for i in ZodziuSarasas:
    if len(i) > len(ilg):
        ilg = i
    if all(j.isalpha() for j in i) and len(i)>=1:
        FiltruotasSarasas.append(i.lower())


ZodziuKiekis = collections.Counter(FiltruotasSarasas)

print("Ilgiausias rastas žodis(žodžiai):")
print(ilg)
print("Zodziu kiekis:")
print(len(FiltruotasSarasas))
print ("Panaudotu zodziu kiekis:")
print(ZodziuKiekis)