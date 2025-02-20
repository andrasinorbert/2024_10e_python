"""
3.
Írjon függvényt adatokBeolvasása néven, amelyik beolvassa a fájl tartalmát egy megfelelő
adatszerkezetbe! Ügyeljen arra, hogy az adatok numerikus értékekként legyenek eltárolva az
ön által választott adatszerkezetben!
"""

def adatokBeolvasása(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    adatoklista=[]
    for i in range(len(sorok)):
        sor=sorok[i].strip().split(" ")
        for j in range(len(sor)):
            sor[j]=int(sor[j])
        adatoklista.append(sor)
    return adatoklista
        
x=adatokBeolvasása("selejt.txt")

[print(i) for i in x]