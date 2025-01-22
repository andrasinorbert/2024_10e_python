from adatsor import *
from fajlkezeles import *
        
        
a=Adatsor("Géza", [3,2,1,6])
print(a.nev)
print(a.szamok)
print(a)

sorok=beolvas("input")
adatoklista=feldolgozo(sorok)
"""
for i in range(len(lista)):
    print(lista[i].nev, lista[i].szamok)
    
[print(l) for l in lista]

osszeg=0

i=0
while i<len(lista) and lista[i].nev!="Eszter":
    i=i+1
van=i<len(lista)
if van:
    Eszter=lista[i]
    for j in range(0,len(Eszter.szamok)):
        osszeg=osszeg+Eszter.szamok[j]
    atlag=osszeg/len(Eszter.szamok)
    print(f"{Eszter.nev} Átlaga: {atlag}")
else:
    print("Nincs Eszter")
    
# na még egyszer
i=0
while i<len(lista) and lista[i].nev!="Eszter":
    i=i+1
van=i<len(lista)
if van:
    Eszter=lista[i]
    print(f"{Eszter.nev} Átlaga: {Eszter.atlag()}")
else:
    print("Nincs Eszter")
"""

kerdesesNev="Eszter"
index=adatoklista.getIndexByName(kerdesesNev)
print(index)

print(adatoklista.getElementByIndex(index).atlag())