# -*- coding: utf-8 -*-
"""

@Judul : Praktikum 2 Algoritma
@Materi : Operasi Aritmatika pada Python
@Author: Nia Suhernawati
@NIM : 065002100005
@Mata Kuliah : Algoritma dan Pemrograman
@Program Studi : Sistem Informasi
@Hari/tanggal : Senin/20210927
"""

import math
print("menghitung jarak antara dua titik di permukaan bumi")
lat1=float(input("insert lattitude city first= "))
lon1=float(input("insert longitude city first= "))
lat2=float(input("insert lattitude city second= "))
lon2=float(input("insert longitude city second= "))

#rumus
dlat=(lat2-lat1)
dlon=(lon2-lon1)
a=math.sin(math.radians(dlat/2))**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(math.radians(dlon/2))**2
b=2*math.atan2(math.sqrt(a), math.sqrt(1-a))
R=6371.01
d= R*b
print("Jarak antara dua titik di permukaan bumi tersebut adalah", d, "kilometer")
 
      
                                                                                            
