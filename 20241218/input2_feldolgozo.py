f=open("input2.txt")
sorok=f.readlines()
f.close()

print(sorok)

matrix=[]
for i in range(len(sorok)):
    print(sorok[i])
    sor=sorok[i].strip() # sortörés eltüntetése
    print(sor)
    lista=sor.split(" ")
    print(lista)
    szamlista=[]
    for j in range(len(lista)):
        szam=int(lista[j])
        szamlista.append(szam)
    print(szamlista)
    matrix.append(szamlista)
print(matrix)

s=0
for i in range(len(matrix)):
    szamlista=matrix[i]
    print(szamlista)
    for j in range(len(szamlista)):
        s=s+szamlista[j]
        
print(f"összeg: {s}")