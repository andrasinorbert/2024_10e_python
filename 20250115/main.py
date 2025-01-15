def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

def feldolgozo(sorok:list[str]):
    #adatok=[]
    adatok=AdatsorLista()
    for i in range(len(sorok)):
        sor=sorok[i].strip()
        felbontott_sor=sor.split(" ")
        nev=felbontott_sor[0]
        szamok=[]
        for j in range(1,len(felbontott_sor)):
            szamok.append(int(felbontott_sor[j]))
        adat=Adatsor(nev, szamok)
        adatok.hozzaad(adat)
    return adatok
        
class Adatsor:
    def __init__(self, nev:str, szamlista:list[int]):
        self.nev=nev
        self.szamok=szamlista
    
    def __str__(self):
        return f"{self.nev} {self.szamok}"
    
    def osszeg(self):
        return sum(self.szamok)
    
    def atlag(self):
        return self.osszeg()/len(self.szamok)
    
class AdatsorLista:
    def __init__(self):
        self.lista=[]
    
    def hozzaad(self, adatsor:Adatsor):
        self.lista.append(adatsor)
    
    def getIndexByName(self, name):
        i=0
        while i<len(self.lista) and self.lista[i].nev!=name:
            i=i+1
        if i<len(self.lista):
            return i
        else:
            return None
    
    def getElementByIndex(self, index):
        return self.lista[index]
        
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