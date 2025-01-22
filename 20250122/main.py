from adatsor import *
from fajlkezeles import *
        
        
a=Adatsor("Géza", [3,2,1,6])
print(a.nev)
print(a.szamok)
print(a)

sorok=beolvas("input")
adatoklista=feldolgozo(sorok)

kerdesesNev="Eszter"
index=adatoklista.getIndexByName(kerdesesNev)
print(index)

print(adatoklista.getElementByIndex(index).atlag())