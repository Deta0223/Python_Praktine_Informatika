#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:27:15 2023

@author: deta0223
"""

import matplotlib.pyplot as plt
import csv

def nuskaityti_duomenis(file_path):
    procesoriai = []
    transistoriai = []
    metai = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        duomenys = csv.reader(csvfile)
        next(duomenys)  # Skip the header row
        for eilute in duomenys:
            procesoriai.append(eilute[0])
            transistoriai.append(int(eilute[1]))
            metai.append(int(eilute[2]))
        return procesoriai, transistoriai, metai

file_path = "transistor-counts.csv"

procesoriai, transistoriai, metai = nuskaityti_duomenis(file_path)

plt.scatter(metai, transistoriai)
plt.scatter(metai, transistoriai, label = "Sukurti procesoriai")
plt.title("Muro desnis")
plt.xlabel("Isleidimo metai")
plt.ylabel("Transistoriu skaicius (log)")


# Pakeičiame Y ašies skalę į logaritminę
plt.yscale('log')


def muro_desnio_formule(n0, y0, T2, y):
    return n0 * 2 ** ((y - y0) / T2)

n0 = transistoriai[0]
y0 = metai[0]
T2 = 2

prognozuojami_tranzistoriai = []
prognozuojami_metai= []

for y in range (min(metai), max(metai)+1):
    prognozuojami_metai.append(y)
    prognozuojami_tranzistoriai.append(muro_desnio_formule(n0, y0, T2, y))
    
plt.plot(prognozuojami_metai, prognozuojami_tranzistoriai, linestyle='--', color = 'gray')
plt.plot(prognozuojami_metai, prognozuojami_tranzistoriai, linestyle='--', color = 'gray', label = "Prognoze")
plt.legend(loc = 'upper left')

plt.savefig('moores_law.pdf')
plt.show()



