f=open("input1.txt")
sorok=f.readlines()
f.close()

print(sorok)

lista=sorok[0].split(" ")
print(lista)

szamlista=[]
for i in range(len(lista)):
    szam=int(lista[i])
    szamlista.append(szam)
print(szamlista)

s=0
for i in range(len(szamlista)):
    s=s+szamlista[i]
print(f"összeg: {s}")
print(f"átlag: {s/len(szamlista)}")