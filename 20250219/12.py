"""
1. a)
A példában látható módon kérjen be a felhasználótól egy listaméretet! A program csak 5 és
25 közötti értéket fogadjon el! Ha a felhasználó által megadott érték nem esik bele a megadott
tartományba, akkor a program írjon ki egy hibaüzenetet és kérje be újra a listaméretet!

Add meg a lista méretét [5...25]: 3
Hibás adatbevitel! Próbáld újra!
Add meg a lista méretét [5...25]: 10
A lista tartalma: [-10, 1, 5, -2, -3, 2, 8, 0, 4, 0]
"""

while True:
    meret= int(input("Add meg a lista méretét [5...25]: "))
    if 5 <= meret and meret <= 25:
        break
    print("Hibás adatbevitel! Próbáld újra!")

"""
1. b)
Hozzon létre egy üres listát számok néven és töltse fel ezt a listát annyi darab -10 és 10
közötti egész véletlen számmal, amekkora értéket a felhasználó az a) feladatrészben megadott!
"""
import random

számok=[]
for _ in range(meret):
    számok.append(random.randint(-10,10))
    
#számok=[random.randint(-10,10) for _ in range(meret)]

"""
Írja ki a lista tartalmát a példában látható módon!
A lista tartalma: [-10, 1, 5, -2, -3, 2, 8, 0, 4, 0]
"""

print(f"A lista tartalma: {számok}")

"""
2. a)
a) A példában látható módon írja ki a listában lévő elemek összegét!
A listában lév˝o elemek összege: 5
"""

osszeg=0
for i in range(len(számok)):
    osszeg+=számok[i]
print(f"A listában lévő elemek összege: {osszeg}")

osszeg=0
for i in számok:
    osszeg+=i
print(f"A listában lévő elemek összege: {osszeg}")

osszeg=[i for i in számok]
osszeg=[számok[i] for i in range(len(számok))]

print(f"A listában lévő elemek összege: {sum(számok)}")

"""
2. b)
A példában látható módon írja ki, hogy igaz-e az az állítás, hogy a listában több 0 szám
szerepel, mint negatív érték!

A listában lév˝o 0 elemek száma: 2
A listában lév˝o negatív elemek száma: 3
Nem igaz az állítás!
"""

nullakszama=0
for i in range(len(számok)):
    if számok[i]==0:
        nullakszama+=1
negativakszama=0
for i in range(len(számok)):
    if számok[i]<0:
        negativakszama+=1
if nullakszama>negativakszama:
    print(f"Igaz az állítás!")
else:
    print(f"Nem igaz az állítás!")
    
nullakszama=számok.count(0)

print(f"{"Igaz" if nullakszama>negativakszama else "Nem igaz"} az állítás!")

