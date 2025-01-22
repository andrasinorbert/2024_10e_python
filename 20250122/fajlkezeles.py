from adatsor import *

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