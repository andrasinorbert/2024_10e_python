file=open("input2")
sorok=file.readlines()
file.close()

print(sorok)

sor=sorok[0]

sorlista=sor.split(" ")
print(sorlista)
szamlista=[]
for i in range(len(sorlista)):
    szam=int(sorlista[i])
    szamlista.append(szam)
print(szamlista)

s=0
for i in range(len(szamlista)):
    s+=szamlista[i]
print(f"összeg: {s}")
print(f"átlag: {s/len(szamlista)}")