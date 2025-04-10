filename="input1.txt"

f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok) # ['1 2 3 4 5']
s=sorok[0]
print(s) # '1 2 3 4 5'
szokozonkent_elvalasztva=s.split(" ")
print(szokozonkent_elvalasztva) # ['1', '2', '3', '4', '5']
szamok=[]
for i in range(len(szokozonkent_elvalasztva)):
    szam=int(szokozonkent_elvalasztva[i])
    szamok.append(szam)
print(szamok) # [1, 2, 3, 4, 5]

#újra, rövidebben
s=sorok[0]
szokozonkent_elvalasztva=s.split(" ")
szamok=[]
for i in range(len(szokozonkent_elvalasztva)):
    szam=int(szokozonkent_elvalasztva[i])
    szamok.append(szam)
print(szamok) # [1, 2, 3, 4, 5]

# még rövidebben
szokozonkent_elvalasztva=sorok[0].split(" ")
szamok=[]
for i in range(len(szokozonkent_elvalasztva)):
    szamok.append(int(szokozonkent_elvalasztva[i]))
print(szamok) # [1, 2, 3, 4, 5]

# függvényként
def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    szokozonkent_elvalasztva=sorok[0].split(" ")
    szamok=[]
    for i in range(len(szokozonkent_elvalasztva)):
        szamok.append(int(szokozonkent_elvalasztva[i]))
    return szamok

filename="input1.txt"
lista=beolvas(filename)
print(lista) # [1, 2, 3, 4, 5]