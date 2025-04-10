filename="input2.txt"

f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok) # ['1\n', '2\n', '3\n', '4\n', '5']

szamok=[]
for i in range(len(sorok)):
    listaelem=sorok[i] # '1\n'
    feleslegNelkuliSzoveg=listaelem.strip() # '1'
    szam=int(feleslegNelkuliSzoveg) # 1
    szamok.append(szam)
print(szamok) # [1, 2, 3, 4, 5]

# rövidebben
szamok=[]
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok) # [1, 2, 3, 4, 5]

# még rövidebben
szamok=[int(sorok[i].strip()) for i in range(len(sorok))]
print(szamok)

# függvényként
def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    szamok=[]
    for i in range(len(sorok)):
        szamok.append(int(sorok[i].strip()))
    return szamok

filename="input2.txt"
lista=beolvas(filename)
print(lista)