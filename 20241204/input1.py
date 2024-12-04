file=open("input1")
sorok=file.readlines()
file.close()

print(sorok)

szamlista=[]
for i in range(len(sorok)):
    adat=sorok[i].strip()
    szam=int(adat)
    szamlista.append(szam)
    
print(szamlista)

s=0
for i in range(len(szamlista)):
    s+=szamlista[i]
print(f"összeg: {s}")
print(f"átlag: {s/len(szamlista)}")