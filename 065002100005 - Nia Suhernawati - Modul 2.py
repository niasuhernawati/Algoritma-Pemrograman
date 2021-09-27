# -*- coding: utf-8 -*-
"""

@Judul : Praktikum 2 Materi
@Hari/Tanggal : Senin, 20210927
@Mata Kuliah : Algoritma dan Pemrograman
@Program Studi : Sistem Informasi
@NIM : 065002100005
@author: Nia Suhernawati
"""

bilbulA = int(input("masukkan nilai a: "))
bilbulB = int(input("masukkan nilai b: "))

hasiljumlah = bilbulA + bilbulB
print("jumlah nilai a dan b adalah ", hasiljumlah)

hasilselisih = abs(bilbulB - bilbulA)
print("selisih nilai a dan b adalah ", hasilselisih)

hasilkali = bilbulA * bilbulB
print("kali nilai a dan b adalah ", hasilkali)

hasilsisabagi = bilbulA % bilbulB
print("sisa bagi nilai a dan b adalah ", hasilsisabagi)

hasilbagi = bilbulA / bilbulB
print("bagi nilai a dan b adalah ", hasilbagi)

from math import log10
print("logaritma basis 10 dari ", bilbulA, "adalah", log10(bilbulA))

hasilpangkat = bilbulA ** bilbulB
print("pangkat nilai a dan b adalah ", hasilpangkat)